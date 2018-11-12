import builtins
from collections import defaultdict
from inspect import getmodule
from keyword import kwlist
from os import mkdir, getcwd
from os.path import isdir
from shutil import rmtree
from typing import IO, Set, Union, Tuple, List, Generator, NoReturn, Dict, Optional

import boto3
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from botocore.client import BaseClient

from parsers import parse_service_resources, parse_clients
from structures import Method, Client, ServiceResource, Resource, Attribute, Collection


def add_indentation_to_docstring(docstring: str, levels: int) -> str:
    indention = "".join(["    " for _ in range(levels)])
    return '\n'.join([f'{indention}{line}' for line in docstring.split('\n')])


def create_import_statements(types: Set[type]) -> Generator[str, None, None]:
    for _type in types:
        if getmodule(_type) != builtins and getmodule(_type) is not None:
            yield f'from {normalize_type_name(getmodule(_type))} import {normalize_type_name(_type)}'


def create_module_directory() -> NoReturn:
    isdir(f'{getcwd()}/boto3_type_annotations') and rmtree(f'{getcwd()}/boto3_type_annotations')
    mkdir(f'{getcwd()}/boto3_type_annotations')


def format_arguments(method) -> Generator[str, None, None]:
    for argument in method.arguments:
        _type = normalize_type_name(argument.type) if argument.required \
            else f'{normalize_type_name(argument.type)} = None'
        yield f'{argument.name}: {_type}'


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


def write_attributes(attributes: List[Attribute], file_object: IO) -> NoReturn:
    for attribute in attributes:
        file_object.write(f'\n    {attribute.name}: {normalize_type_name(attribute.type)}')


def write_client(client: Client) -> NoReturn:
    if not isdir(f'{getcwd()}/boto3_type_annotations/{normalize_module_name(client.name)}'):
        mkdir(f'{getcwd()}/boto3_type_annotations/{normalize_module_name(client.name)}')
    file_path = f'{getcwd()}/boto3_type_annotations/{normalize_module_name(client.name)}/client.py'
    with open(file_path, 'w') as file_object:
        types = retrieve_types_from_client(client).union({Optional, NoReturn, BaseClient})
        file_object.write('\n'.join(list(create_import_statements(types))))
        file_object.write(f'\n\n\nclass Client(BaseClient):')
        write_methods(client.methods, file_object)
    return [{
        'import_statement': f'from boto3_type_annotations.{normalize_module_name(client.name)}.client import Client',
        'name': 'Client'
    }]


def write_import_statements(file_object, types: Set[type]) -> NoReturn:
    file_object.write('\n'.join(list(create_import_statements(types))))


def write_methods(
        methods: List[Method],
        file_object: IO,
        method_body: str = 'pass',
        first_arg: str = 'self',
        decorator: str = None
) -> NoReturn:
    for method in methods:
        write_method(method, file_object, method_body, first_arg, decorator)


def write_method(
        method: Method,
        file_object: IO,
        method_body: str = 'pass',
        first_arg: str = 'self',
        decorator: str = None
) -> NoReturn:

    def_ = 'def' if decorator is None else f'''
    {decorator}
    def'''
    arguments = f', {", ".join(format_arguments(method))}' if len(method.arguments) > 0 else ''
    file_object.write(f'''
    {def_} {method.name}({first_arg}{arguments}) -> {normalize_type_name(method.return_type) 
                                                        if method.return_type is not None 
                                                        else 'NoReturn'}:
        """
{add_indentation_to_docstring(method.docstring, 2)}
        """
        {method_body}
''')


def write_service_resource(service_resource: ServiceResource):
    print('Writing: ', service_resource.name)
    objects = []
    if not isdir(f'{getcwd()}/boto3_type_annotations/{normalize_module_name(service_resource.name)}'):
        mkdir(f'{getcwd()}/boto3_type_annotations/{normalize_module_name(service_resource.name)}')
    file_path = f'{getcwd()}/boto3_type_annotations/{normalize_module_name(service_resource.name)}/service_resource.py'
    with open(file_path, 'w') as file_object:
        types = retrieve_types_from_service_resource(service_resource).union(
            {List, Dict, ResourceCollection, Optional, NoReturn}
        )
        write_import_statements(file_object, types)
        if Boto3ServiceResource not in retrieve_types_from_service_resource(service_resource):
            file_object.write('\nfrom boto3.resources import base\n')
        write_resource(service_resource, 'ServiceResource', file_object)
        objects.append({
            'import_statement': f'from boto3_type_annotations.{normalize_module_name(service_resource.name)}'
                                f'.service_resource import ServiceResource',
            'name': 'ServiceResource'
        })
        for resource in service_resource.sub_resources:
            write_resource(resource, resource.name, file_object)
            objects.append({
                'import_statement': f'from boto3_type_annotations.{normalize_module_name(service_resource.name)}'
                                    f'.service_resource import {resource.name}',
                'name': resource.name
            })
        for collection in service_resource.collections:
            write_collection(collection, file_object)
            objects.append({
                'import_statement': f'from boto3_type_annotations.{normalize_module_name(service_resource.name)}'
                                    f'.service_resource import {collection.name}',
                'name': collection.name
            })
    return objects


def write_collection(collection: Collection, file_object: IO) -> NoReturn:
    file_object.write(f'\n\nclass {collection.name}(ResourceCollection):')
    write_methods(collection.methods, file_object, first_arg='cls', decorator='@classmethod')


def write_resource(resource: Union[Resource, ServiceResource], name: str, file_object: IO) -> NoReturn:
    file_object.write(f'\n\nclass {name}(base.ServiceResource):')
    attributes = resource.attributes
    attributes += [Attribute(c.name, f'\'{c.name}\'') for c in resource.collections]
    write_attributes(attributes, file_object)
    file_object.write('\n')
    write_methods(resource.methods, file_object)


session = boto3.session.Session()
create_module_directory()
init_files = defaultdict(list)
for client in parse_clients(session):
    init_files[client.name] += write_client(client)
for service_resource in parse_service_resources(session):
    init_files[service_resource.name] += write_service_resource(service_resource)
for module, imports in init_files.items():
    file_path = f'{getcwd()}/boto3_type_annotations/{normalize_module_name(module)}/__init__.py'
    with open(file_path, 'w') as file_object:
        file_object.write('\n'.join([i.get('import_statement') for i in imports]))
        all_objects = ',\n'.join(f'    \'{i.get("name")}\'' for i in imports)
        file_object.write(f'''

__all__ = (
{all_objects}
)
''')
