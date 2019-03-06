import builtins
import re
from collections import defaultdict
from inspect import getmodule
from keyword import kwlist
from os import mkdir
from os.path import isdir, dirname, abspath
from shutil import rmtree, copyfile
from typing import IO, Set, Union, Tuple, List, Generator, Dict, Optional

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.session import Session
from botocore.client import BaseClient

from parsers import parse_service_resources, parse_clients, parse_service_waiters, parse_service_paginators
from structures import Method, Client, ServiceResource, Resource, Attribute, Collection, ServiceWaiter, \
    ServicePaginator, Config


def add_indentation_to_docstring(docstring: str, levels: int) -> str:
    indention = "".join(["    " for _ in range(levels)])
    return '\n'.join([f'{indention}{line}' for line in docstring.split('\n')])


def clean_doc(doc: str) -> str:

    def append_line(section: List, next_line: str):
        section.append(next_line.replace('\'', '\\\'').replace('"', '\\\"').rstrip())

    parameters = []
    preamble = []
    indices_to_remove = []
    parameter_regex = re.compile('^:(.*[a-zA-Z]):')
    lines = doc.split('\n')
    for i, line in enumerate(lines):
        if parameter_regex.search(line.strip()):
            append_line(parameters, line)
            indices_to_remove.append(i)
            n = i + 1
            while n < len(lines) and not parameter_regex.search(lines[n].strip()) and line.strip() != ':returns:':
                if lines[n].strip():
                    append_line(parameters, lines[n])
                    indices_to_remove.append(n)
                n += 1
    for i in reversed(indices_to_remove):
        del lines[i]
    for i, line in enumerate(lines):
        if '::' == line.strip() or line.strip().startswith('**') and line.strip().endswith('**'):
            lines[i] = line.strip()
    for line in lines:
        if line.strip():
            if line.strip().startswith('**') and line.strip().endswith('**'):
                preamble.append('')
            preamble.append(line)
    return '\n'.join(preamble + parameters)


def create_import_statements(types: Set[type]) -> Generator[str, None, None]:
    for _type in types:
        if getmodule(_type) != builtins and getmodule(_type) is not None:
            yield f'from {normalize_type_name(getmodule(_type))} import {normalize_type_name(_type)}'


def create_module_directory(config: Config):
    print(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}')
    if isdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}'):
        rmtree(f'{normalized_repository_path()}/{config.package_name}')
    mkdir(f'{normalized_repository_path()}/{config.package_name}')
    mkdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}')
    init_path = f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/__init__.py'
    with open(init_path, 'w') as file_object:
        file_object.write('\n')


def format_arguments(method) -> Generator[str, None, None]:
    for argument in sorted(method.arguments, key=lambda m: m.required, reverse=True):
        _type = normalize_type_name(argument.type) if argument.required \
            else f'{normalize_type_name(argument.type)} = None'
        yield f'{argument.name}: {_type}'


def normalized_repository_path():
    return dirname(dirname(abspath(__file__)))


def normalize_module_name(name: str) -> str:
    name = name.replace('-', '_')
    if name in kwlist:
        name = f'{name}_'
    return name


def normalize_type_name(type_: Union[type, Tuple, str]):
    if isinstance(type_, tuple):
        return f'Union[{", ".join([normalize_type_name(t) for t in type_])}]'
    if isinstance(type_, str):
        return type_
    if type_ == Union:
        return 'Union'
    if type_ == Optional:
        return 'Optional'
    return type_._name if hasattr(type_, '_name') and not hasattr(type_, '__name__') else type_.__name__


def retrieve_argument_types(method: Method) -> Set[type]:
    types = set()
    for arg in method.arguments:
        types.add(arg.type) if not isinstance(arg.type, tuple) else [types.add(t) for t in arg.type]
    return types


def retrieve_types_from_client(client: Client) -> Set[type]:
    types = set()
    for method_types in retrieve_method_types(client.methods):
        types = types.union(method_types)
    return types


def retrieve_types_from_service_resource(service_resource: ServiceResource) -> Set[type]:
    types = set()
    types = types.union(retrieve_types_from_methods(service_resource.methods))
    types = types.union({a.type for a in service_resource.attributes})
    types = types.union(retrieve_types_from_collection(service_resource))
    for resource in service_resource.sub_resources:
        types = types.union(retrieve_types_from_methods(resource.methods))
        types = types.union({a.type for a in resource.attributes})
        types = types.union(retrieve_types_from_collection(resource))
    return types


def retrieve_types_from_methods(methods: List[Method]) -> Set[type]:
    types = set()
    for method_types in retrieve_method_types(methods):
        types = types.union(method_types)
    return types


def retrieve_types_from_collection(service_resource: Union[ServiceResource, Resource]) -> Set[type]:
    types = set()
    for collection in service_resource.collections:
        types = types.union(retrieve_types_from_methods(collection.methods))
    return types


def retrieve_method_types(methods: List[Method]) -> Generator[Set, None, None]:
    for m in methods:
        argument_types = retrieve_argument_types(m)
        argument_types.add(m.return_type)
        yield argument_types


def write_attributes(attributes: List[Attribute], file_object: IO):
    for attribute in attributes:
        file_object.write(f'\n    {attribute.name}: {normalize_type_name(attribute.type)}')


def write_client(client: Client, config: Config):
    print(f'Writing: {client.name}')
    normalized_module_name = normalize_module_name(client.name)
    if not isdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}'):
        mkdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}')
    file_path = f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}' \
        f'/client.py'
    with open(file_path, 'w') as file_object:
        types = retrieve_types_from_client(client).union({Optional, BaseClient, Union})
        file_object.write('\n'.join(list(create_import_statements(types))))
        file_object.write(f'\n\n\nclass Client(BaseClient):')
        write_methods(client.methods, file_object, include_doc=config.with_docs)
    return [{
        'import_statement': f'from {config.module_name}.{normalized_module_name}.client import Client',
        'name': 'Client'
    }]


def write_import_statements(file_object, types: Set[type]):
    file_object.write('\n'.join(list(create_import_statements(types))))


def write_methods(
        methods: List[Method],
        file_object: IO,
        method_body: str = 'pass',
        first_arg: str = 'self',
        decorator: str = None,
        include_doc: bool = False
):
    for method in methods:
        write_method(method, file_object, method_body, first_arg, decorator, include_doc)


def write_method(
        method: Method,
        file_object: IO,
        method_body: str = 'pass',
        first_arg: str = 'self',
        decorator: str = None,
        include_doc: bool = False
):

    doc = ''
    if include_doc is True:
        doc = f'''        """
{add_indentation_to_docstring(clean_doc(method.docstring), 2)}
        """
'''
    def_ = 'def' if decorator is None else f'''
    {decorator}
    def'''
    arguments = f', {", ".join(format_arguments(method))}' if len(method.arguments) > 0 else ''
    file_object.write(f'''
    {def_} {method.name}({first_arg}{arguments}){f" -> {normalize_type_name(method.return_type)}" 
                                                        if method.return_type is not None 
                                                        else ''}:
{doc}        {method_body}
''')


def write_service_resource(
        service_resource: ServiceResource,
        config: Config
) -> List[Dict]:

    print(f'Writing: {service_resource.name}')
    defined_objects = []
    normalized_module_name = normalize_module_name(service_resource.name)
    if not isdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}'):
        mkdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}')
    file_path = f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}/' \
                f'service_resource.py'
    with open(file_path, 'w') as file_object:
        types = retrieve_types_from_service_resource(service_resource).union(
            {List, Dict, ResourceCollection, Optional, Union}
        )
        write_import_statements(file_object, types)
        if Boto3ServiceResource not in retrieve_types_from_service_resource(service_resource):
            file_object.write('\nfrom boto3.resources import base\n')
        write_resource(service_resource, 'ServiceResource', file_object, config.with_docs)
        defined_objects.append({
            'import_statement': f'from {config.module_name}.{normalized_module_name}'
                                f'.service_resource import ServiceResource',
            'name': 'ServiceResource'
        })
        for resource in service_resource.sub_resources:
            write_resource(resource, resource.name, file_object, config.with_docs)
            defined_objects.append({
                'import_statement': f'from {config.module_name}.{normalized_module_name}'
                                    f'.service_resource import {resource.name}',
                'name': resource.name
            })
        for collection in service_resource.collections:
            write_collection(collection, file_object, config.with_docs)
            defined_objects.append({
                'import_statement': f'from {config.module_name}.{normalized_module_name}'
                                    f'.service_resource import {collection.name}',
                'name': collection.name
            })
    return defined_objects


def write_collection(collection: Collection, file_object: IO, with_docs: bool = False):
    file_object.write(f'\n\nclass {collection.name}(ResourceCollection):')
    write_methods(collection.methods, file_object, first_arg='cls', decorator='@classmethod', include_doc=with_docs)


def write_resource(
        resource: Union[Resource, ServiceResource],
        name: str,
        file_object: IO,
        with_docs: bool = False
):

    file_object.write(f'\n\nclass {name}(base.ServiceResource):')
    attributes = resource.attributes
    attributes += [Attribute(c.name, f'\'{c.name}\'') for c in resource.collections]
    write_attributes(attributes, file_object)
    file_object.write('\n')
    write_methods(resource.methods, file_object, include_doc=with_docs)


def write_service_waiter(
        service_waiter: ServiceWaiter,
        config: Config
) -> List[Dict]:
    defined_objects = []
    print(f'Writing: {service_waiter.name}')
    normalized_module_name = normalize_module_name(service_waiter.name)
    if not isdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}'):
        mkdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}')
    file_path = f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}' \
        f'/waiter.py'
    if service_waiter.waiters:
        with open(file_path, 'w') as file_object:
            types = set()
            for waiter in service_waiter.waiters:
                types = types.union(retrieve_types_from_methods(waiter.methods))
            write_import_statements(file_object, types)
            file_object.write('\nfrom botocore.waiter import Waiter\n')
            for waiter in service_waiter.waiters:
                file_object.write(f'\n\nclass {waiter.name}(Waiter):')
                write_methods(waiter.methods, file_object, include_doc=config.with_docs)
                defined_objects.append({
                    'import_statement': f'from {config.module_name}.{normalized_module_name}.waiter '
                                        f'import {waiter.name}',
                    'name': waiter.name
                })
    return defined_objects


def write_service_paginator(
        service_paginator: ServicePaginator,
        config: Config
):
    defined_objects = []
    normalized_module_name = normalize_module_name(service_paginator.name)
    print(f'Writing: {service_paginator.name}')
    if not isdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}'):
        mkdir(f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}')
    file_path = f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/{normalized_module_name}' \
        f'/paginator.py'
    if service_paginator.paginators:
        with open(file_path, 'w') as file_object:
            types = set()
            for paginator in service_paginator.paginators:
                types = types.union(retrieve_types_from_methods(paginator.methods))
            write_import_statements(file_object, types)
            file_object.write('\nfrom botocore.paginate import Paginator\n')
            for paginator in service_paginator.paginators:
                file_object.write(f'\n\nclass {paginator.name}(Paginator):')
                write_methods(paginator.methods, file_object, include_doc=config.with_docs)
                defined_objects.append({
                    'import_statement': f'from {config.module_name}.{normalized_module_name}'
                                        f'.paginator import {paginator.name}',
                    'name': paginator.name
                })
    return defined_objects


def write_services(session: Session, config: Config):
    create_module_directory(config)
    init_files = defaultdict(list)
    if config.with_clients:
        init_files = write_clients(init_files, session, config)
    if config.with_service_resources:
        init_files = write_service_resources(init_files, session, config)
    config.with_waiters and write_service_waiters(session, config)
    config.with_paginators and write_service_paginators(session, config)
    write_init_files(init_files, config)
    write_setup(config)
    copyfile(config.license, f'{normalized_repository_path()}/{config.package_name}/LICENSE')
    copyfile(config.readme, f'{normalized_repository_path()}/{config.package_name}/README.md')


def write_init_files(init_files: Dict[str, List], config: Config):
    for module, imports in init_files.items():
        if imports:
            file_path = f'{normalized_repository_path()}/{config.package_name}/{config.module_name}/' \
                        f'{normalize_module_name(module)}/__init__.py'
            with open(file_path, 'w') as file_object:
                file_object.write('\n'.join([i.get('import_statement') for i in imports]))
                all_objects = ',\n'.join(f'    \'{i.get("name")}\'' for i in imports)
                file_object.write(f'''
    
__all__ = (
{all_objects}
)
''')


def write_setup(config: Config):
    with open(f'{normalized_repository_path()}/{config.package_name}/setup.py', 'w') as file_object:
        file_object.write(f'''
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='{config.package_name}',
    version='{config.version}',
    packages=find_packages(),
    url='https://github.com/alliefitter/boto3_type_annotations',
    license='MIT License',
    author='Allie Fitter',
    author_email='fitterj@gmail.com',
    description='Type annotations for boto3. Adds code completion in IDEs such as PyCharm.',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
)
''')


def write_service_paginators(session: Session, config: Config):
    print('\n\nWriting Clients\n\n')
    for service_paginator in parse_service_paginators(session, config):
        write_service_paginator(service_paginator, config)


def write_service_waiters(session: Session, config: Config):
    print('\n\nWriting Waiters\n\n')
    for service_waiter in parse_service_waiters(session, config):
        write_service_waiter(service_waiter, config)


def write_service_resources(init_files: Dict, session: Session, config: Config) -> Dict[str, List]:
    print('\n\nWriting Service Resources\n\n')
    for service_resource in parse_service_resources(session, config):
        init_files[service_resource.name] += write_service_resource(service_resource, config)
    return init_files


def write_clients(init_files: Dict, session: Session, config: Config) -> Dict[str, List]:
    print('\n\nWriting Clients\n\n')
    for client in parse_clients(session, config):
        init_files[client.name] += write_client(client, config)
    return init_files
