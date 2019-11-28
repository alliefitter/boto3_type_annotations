# DEPRECATED

After reaching out to AWS about releasing a stubs only package as detailed in [PEP-561](https://www.python.org/dev/peps/pep-0561/#stub-only-packages), they asked me to hold off on releasing it as they were [working typing support](https://github.com/boto/botostubs). Then I got bogged down at work for about four months and didn't have time to work on this at all. And now I'm deprecating it. Check out [this fork](https://github.com/vemel/mypy_boto3) for a maintained version. They also uploaded a [boto3-stubs](https://pypi.org/project/boto3-stubs/) package. 

# boto3_type_annotations

A programmatically created package that defines `boto3` services as stand in classes with type annotations. `boto3` is 
an incredibly useful, well designed interface to the AWS API. However, we live in an age where even free IDEs like 
PyCharm CE have full code completion (IntelliSense). Because `boto3`'s services are created at runtime, IDEs aren't 
able to index its code in order to provide code completion or infer the type of these services or of the objects created 
by them. Even if it was able to do so, clients and service resources are created using a service agnostic factory method
and are only identified by a string argument of that method. IDEs don't parse arguments to infer the return type of a
method, and they probably shouldn't. Meaning that the only way for an IDE to know the type of a client created by 
`boto3.client('<service>')` is for it to be explicitly declared in type annotations, type comments, or docstrings, which
brings us back to the original problem of services being defined at runtime. All of that to say that working with 
`boto3` can be very frustrating at times.

To reduce this frustration, `boto3_type_annotations` defines stand in classes for the clients, service resources, 
paginators, and waiters provided by `boto3`'s services. Even though these services are created by `boto3` are created at
runtime, they are still full fledged Python objects, and AWS has been nice enough to include documentation in the 
docstrings of these objects' methods. By parsing those docstrings, we can retrieve the types of method 
arguments--also, which arguments are required and which may be omitted--and the types of their return 
values. With that, we have everything we need to create objects which mimic the class structure of `boto3`'s objects. 
And with Python's `typing` module, we can annotate the methods of the stand in objects with the types which we've 
parsed. What this means is that we can use these stand in objects to declare the type of `boto3` service objects in our 
own code.

![types!](https://github.com/alliefitter/boto3_type_annotations/blob/master/img/boto3_type_annotations.gif)

## With or Without Docstrings

This package is available both with docstrings, named `boto3_type_annotations_with_docs` on PyPi (which contains the 
same documentation you'll find online), and without, named `boto3_type_annotations` on PyPi. The reason for this is 
that, for a python package, `boto3_type_annotations_with_docs` is HUGE. `boto3_type_annotations` is pretty large itself 
at 2.2 MB, but `boto3_type_annotations_with_docs` dwarfs it at 41 MB. Being that `boto3` and `botocore` add up to be 34 
MB, this is likely not ideal for many use cases. However, there are use cases in which you may want documentation in 
your IDE, during development for example. A possible workflow for this use case is detailed below.

## Installation

Without docs:
```
pip install boto3_type_annotations
```

With docs:
```
pip install boto3_type_annotations_with_docs
```

## Usage

Regardless of which deployment package you install, you'll still import the same package, `boto3_type_annotations`.
Its constituent packages and modules can be used to declare the type of `boto3` objects. For instance, everybody's 
favorite, S3:

```python
import boto3
from boto3_type_annotations.s3 import Client, ServiceResource
from boto3_type_annotations.s3.waiter import BucketExists
from boto3_type_annotations.s3.paginator import ListObjectsV2

# With type annotations

client: Client = boto3.client('s3')
client.create_bucket(Bucket='foo')  # Not only does your IDE knows the name of this method, 
                                    # it knows the type of the `Bucket` argument too!
                                    # It also, knows that `Bucket` is required, but `ACL` isn't!

# Waiters and paginators and defined also...

waiter: BucketExists = client.get_waiter('bucket_exists')
waiter.wait('foo')

paginator: ListObjectsV2 = client.get_paginator('list_objects_v2')
response = paginator.paginate(Bucket='foo')

# Along with service resources.

resource: ServiceResource = boto3.resource('s3')
bucket = resource.Bucket('bar')
bucket.create()

# With type comments

client = boto3.client('s3')  # type: Client
response = client.get_object(Bucket='foo', Key='bar')

# In docstrings

class Foo:
    def __init__(self, client):
        """
        :param client: It's an S3 Client and the IDE is gonna know what it is!
        :type client: Client
        """
        self.client = client
        
    def bar(self):
        """
        :rtype: Client
        """
        self.client.delete_object(Bucket='foo', Key='bar')
        return self.client
```

## How Is This Package Different From `pyboto3`?

`pyboto3` has been a useful package which was created for the same purpose and using the same methodology as this 
package. It does have its shortcomings, though. For one, it only defines clients, no service resources, waiters, or 
paginators. Two, it defines2 clients as modules when the objects created by `boto3` are classes. This seems 
nitpicky until you realize that modules can't be used to declare type with type annotations. Even a variable in the 
outermost scope of a module would require rst docstring to declare its type. Also, and this is actually is nitpicky, 
the package structure doesn't mimic that of `boto3`--which you can see in the documentation i.e. `sqs.ServiceResource`, 
`s3.Bucket`, `ec2.waiter.InstanceExists`. Though I don't want to purport that this is perfectly one to one with what is
in the docs. For instance, there's not much consistency in the docs as far as casing. You'll sometimes see 
`S3.Waiter.BucketExists` and in other places `sqs.Bucket`. I chose to go with the pep8 guidelines where module names are
in snake case and classes are in Pascal case.

## Development Workflow With Docstring

As mentioned above, there may be scenarios in which you would want to have docstrings in development, but not want
to package a 41MB dependency with your production code. To accommodate this and similar scenarios, I decided to provide 
two deployment packages, each containing a `boto3_type_annotations` package. So, one workflow may be to have two 
requirements files: requirements.txt and requirements-dev.txt (`boto3` does something similar in that they have 
requirements.txt for the API resource and requirements-docs.txt for building documentation.). These two files would 
look like this:

**requirements.txt**
```
boto3_type_annotations
# other dependencies
```

**requirements-dev.txt**
```
boto3_type_annotations_with_docs
# other dependencies
```

You would then install `requirements.txt` in production and `requirements-dev.txt` in development. Because both 
deployment packages define the `boto3_type_annotations` package, you won't have to change your code. You just need to 
install the appropriate deployment package.

## Custom Builds

In cases when you're only using a small number of `boto3` services, you may not want to depend on a package containing 
every service available. To provide a bit more flexibility, this package provides a way to create a custom build of
the `boto3_type_annotations` package. The `configs/` directory contains configurations for `boto3_type_annotations` and
`boto3_type_annnotations_with_docs`, along with a couple example configurations.

```yaml
services: # A list of services. Use `boto3.session.Session.get_available_services()` to view services. 
  - ec2
  - rds
  - sqs
  - sns
  - lambda
  - s3
with_docs: true # Include docstrings.
with_clients: true # Include client classes
with_service_resources: true # Include service resources.
with_paginators: true # Include paginators
with_waiters: true # Include waiters
package_name: boto3_type_annotations_essentials # The name of the package.
module_name: boto3_type_annotations # The name of the module.
version: 0.2.4 # Version of the package.
readme: README.md # Path to readme file.
license: LICENSE # Path to file containing license.
```

The preceding configuration is the contents of `config/example.essentials.yaml`. When `build.py` is run with this
config, it will parse and write the ec2, rds, sqs, sns, lambda, and s3 services with docstrings and including all
clients, service resources, paginators, and waiters. 

```bash
$ python build_scripts/build.py ../configs/example.essentials.yaml
```

It will create a directory named `boto3_type_annotations_essentials`
in the root directory of the repository. That directory will contain a python module named `boto3_type_annotations`,
a license file, and a `setup.py` file. Now all you need to do is package everything up and install it.

```bash
$ python setup.py sdist bdist_wheel

$ pip3 install dist/boto3_type_annotations_essentials-0.2.4-py3-none-any.whl --user

```

## TODO

- Create an "essentials" deployment package only containing often used services like Lambda, S3, SQS, and CloudFormation

- Package related services into separate deployment packages, to create smaller packages containing only services
  which are essential to a certain use case, group EC2 and RDS for instance.

- ~~Create custom builds. If a project only uses S3's service resource, provide a way to build a deployment package 
  containing just that package. This would require some sort of configuration and more mature build script.~~
  
- Reduce the size of `boto3_type_annotations_with_docs`. I'm already cutting out extraneous new lines and some
  whitespaces which reduced the size by 10 MB(!), but I'd like to see it closer to the 34 MB of `boto3` + `botocore`.
