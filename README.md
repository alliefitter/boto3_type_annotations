# boto3_type_annotations

A programmatically created package that defines `boto3` services as dummy class with type annotations. `boto3` is an 
incredibly useful, well designed interface to the AWS API. However, we live in an age where even free IDEs like PyCharm 
CE have full code completion (IntelliSense). Because `boto3`'s services are created at runtime, IDEs aren't able to
index its code so that they can provide code completion or infer the type of these services or of the objects created by
them. This can be very frustrating, even more so when you're working with other dependencies which can be indexed.

To reduce this frustration, `boto3_type_annotations` contains dummy objects of the clients, service resources, 
paginators, and waiters provided by `boto3`'s services. Even though the client, service resources, paginators, and 
waiters created by `boto3` are created at runtime, they are still full fledged Python objects, and AWS has been nice 
enough to include documentation in the docstrings of these object's methods. By parsing the docstrings of methods,
we can retrieve both the types of method arguments (We can also determine which arguments are required and which may 
be omitted) and the types of their return values. With that, we have everything we need to create objects which
mimic the class structure of `boto3`'s objects. And with Python's `typing` module, we can annotate the methods of the
dummy objects with the types which we've parsed. What this means is that we can use these dummy objects to declare the
type of `boto3` service objects in our own code.

![types!](https://github.com/alliefitter/boto3_type_annotations/blob/master/img/boto3_type_annotations.gif)

## With or Without Docstrings

This package is available both with docstrings (which contain the same documentation you'll find online), 
`boto3_type_annotations_with_docs`, and without, `boto3_type_annotations`. The reason for this is that, for a python 
package, `boto3_type_annotations_with_docs` is HUGE. `boto3_type_annotations` is pretty large  
itself at 2.2 MB, but `boto3_type_annotations_with_docs` dwarfs it at 41 MB. With `boto3` and `botocore` adding up to be 
34 MB, this is likely not ideal for many use cases. However, there are use cases in which you may want documentation in
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
paginators. Two, it defines it's clients as modules when the objects created by `boto3` are classes. This seems 
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
requirements files: `requirements.txt` and `requirements-dev.txt` (`boto3` does something similar in that they have 
`requirements.txt` for API resource and `requirements-docs.txt` for building documentation.). These two files would 
look like this:

`requirements.txt`
```
boto3_type_annotations
# other dependencies
```

`requirements-dev.txt`
```
boto3_type_annotations_with_docs
# other dependencies
```

You would then install `requirements.txt` in production and `requirements-dev.txt` in development. Because both 
define the `boto3_type_annotations` package, you won't have to change your code. You just need to install the 
appropriate deployment package.

## TODO

- Create an "essentials" deployment package only containing often used services like Lambda, S3, SQS, and CloudFormation

- Package related services into separate deployment packages, to create smaller packages containing only service
  that are essential to a use case, group EC2 and RDS for instance.

- Create custom builds. If a project only uses S3's service resource, provide a way to build a deployment package 
  containing just that package. This would require some sort of configuration and more mature build script.
  
- Reduce the size of `boto3_type_annotations_with_docs`. I'm already cutting out extraneous new lines and some
  whitespaces which reduced the size by 10 MB(!), but I'd like to see it closer to the 34 MB of `boto3` + `botocore`.
