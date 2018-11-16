import builtins
from collections import defaultdict
from inspect import getmodule
from keyword import kwlist
from os import mkdir, getcwd
from os.path import isdir, dirname
from shutil import rmtree
from typing import IO, Set, Union, Tuple, List, Generator, Dict, Optional

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.session import Session
from botocore.client import BaseClient

from build_scripts.parsers import parse_service_resources, parse_clients, parse_service_waiters, parse_service_paginators
from build_scripts.structures import Method, Client, ServiceResource, Resource, Attribute, Collection, ServiceWaiter, \
    ServicePaginator


def add_indentation_to_docstring(docstring: str, levels: int) -> str:
    indention = "".join(["    " for _ in range(levels)])
    return '\n'.join([f'{indention}{line}' for line in docstring.split('\n')])


def clean_doc(doc: str) -> str:

    def append_line(next_line: str):
        cleaned_doc.append(next_line.replace('\'', '\\\'').replace('"', '\\\"'))

    cleaned_doc = []
    previous_line = None
    for line in doc.split('\n'):
        if isinstance(previous_line, str) and previous_line.endswith(':'):
            append_line(previous_line)
            append_line(line)
        elif isinstance(previous_line, str) and previous_line.strip() == '' and line.strip() == '':
            previous_line = line
            continue
        elif isinstance(previous_line, str) and not line.endswith(':'):
            append_line(line)
        previous_line = line
    return '\n'.join(cleaned_doc)


def create_import_statements(types: Set[type]) -> Generator[str, None, None]:
    for _type in types:
        if getmodule(_type) != builtins and getmodule(_type) is not None:
            yield f'from {normalize_type_name(getmodule(_type))} import {normalize_type_name(_type)}'


def create_module_directory(package_name: str = 'boto3_type_annotations'):
    if isdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations'):
        rmtree(f'{dirname(getcwd())}/{package_name}')
    mkdir(f'{dirname(getcwd())}/{package_name}')
    mkdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations')
    with open(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/__init__.py', 'w') as file_object:
        file_object.write('\n')


def format_arguments(method) -> Generator[str, None, None]:
    for argument in sorted(method.arguments, key=lambda m: m.required, reverse=True):
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


def write_attributes(attributes: List[Attribute], file_object: IO):
    for attribute in attributes:
        file_object.write(f'\n    {attribute.name}: {normalize_type_name(attribute.type)}')


def write_client(client: Client, with_docs: bool = False, package_name: str = 'boto3_type_annotations'):
    print(f'Writing: {client.name}')
    normalized_module_name = normalize_module_name(client.name)
    if not isdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}'):
        mkdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}')
    file_path = f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}/client.py'
    with open(file_path, 'w') as file_object:
        types = retrieve_types_from_client(client).union({Optional, BaseClient, Union})
        file_object.write('\n'.join(list(create_import_statements(types))))
        file_object.write(f'\n\n\nclass Client(BaseClient):')
        write_methods(client.methods, file_object, include_doc=with_docs)
    return [{
        'import_statement': f'from boto3_type_annotations.{normalized_module_name}.client import Client',
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
        with_docs: bool = False,
        package_name: str = 'boto3_type_annotations'
) -> List[Dict]:

    print(f'Writing: {service_resource.name}')
    defined_objects = []
    normalized_module_name = normalize_module_name(service_resource.name)
    if not isdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}'):
        mkdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}')
    file_path = f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}/' \
                f'service_resource.py'
    with open(file_path, 'w') as file_object:
        types = retrieve_types_from_service_resource(service_resource).union(
            {List, Dict, ResourceCollection, Optional, Union}
        )
        write_import_statements(file_object, types)
        if Boto3ServiceResource not in retrieve_types_from_service_resource(service_resource):
            file_object.write('\nfrom boto3.resources import base\n')
        write_resource(service_resource, 'ServiceResource', file_object, with_docs)
        defined_objects.append({
            'import_statement': f'from boto3_type_annotations.{normalized_module_name}'
                                f'.service_resource import ServiceResource',
            'name': 'ServiceResource'
        })
        for resource in service_resource.sub_resources:
            write_resource(resource, resource.name, file_object, with_docs)
            defined_objects.append({
                'import_statement': f'from boto3_type_annotations.{normalized_module_name}'
                                    f'.service_resource import {resource.name}',
                'name': resource.name
            })
        for collection in service_resource.collections:
            write_collection(collection, file_object, with_docs)
            defined_objects.append({
                'import_statement': f'from boto3_type_annotations.{normalized_module_name}'
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
        with_docs: bool = False,
        package_name: str = 'boto3_type_annotations'
) -> List[Dict]:
    defined_objects = []
    print(f'Writing: {service_waiter.name}')
    normalized_module_name = normalize_module_name(service_waiter.name)
    if not isdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}'):
        mkdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}')
    file_path = f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}/waiter.py'
    if service_waiter.waiters:
        with open(file_path, 'w') as file_object:
            types = set()
            for waiter in service_waiter.waiters:
                types = types.union(retrieve_types_from_methods(waiter.methods))
            write_import_statements(file_object, types)
            file_object.write('\nfrom botocore.waiter import Waiter\n')
            for waiter in service_waiter.waiters:
                file_object.write(f'\n\nclass {waiter.name}(Waiter):')
                write_methods(waiter.methods, file_object, include_doc=with_docs)
                defined_objects.append({
                    'import_statement': f'from boto3_type_annotations.{normalized_module_name}.waiter '
                                        f'import {waiter.name}',
                    'name': waiter.name
                })
    return defined_objects


def write_service_paginator(
        service_paginator: ServicePaginator,
        with_docs: bool = False,
        package_name: str = 'boto3_type_annotations'
):
    defined_objects = []
    normalized_module_name = normalize_module_name(service_paginator.name)
    print(f'Writing: {service_paginator.name}')
    if not isdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}'):
        mkdir(f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}')
    file_path = f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalized_module_name}/paginator.py'
    if service_paginator.paginators:
        with open(file_path, 'w') as file_object:
            types = set()
            for paginator in service_paginator.paginators:
                types = types.union(retrieve_types_from_methods(paginator.methods))
            write_import_statements(file_object, types)
            file_object.write('\nfrom botocore.paginate import Paginator\n')
            for paginator in service_paginator.paginators:
                file_object.write(f'\n\nclass {paginator.name}(Paginator):')
                write_methods(paginator.methods, file_object, include_doc=with_docs)
                defined_objects.append({
                    'import_statement': f'from boto3_type_annotations.{normalized_module_name}'
                                        f'.paginator import {paginator.name}',
                    'name': paginator.name
                })
    return defined_objects


def write_services(session: Session, with_docs: bool = False, package_name: str = 'boto3_type_annotations'):
    create_module_directory(package_name)
    init_files = defaultdict(list)
    init_files = write_clients(init_files, session, with_docs, package_name)
    init_files = write_service_resources(init_files, session, with_docs, package_name)
    write_service_waiters(session, with_docs, package_name)
    write_service_paginators(session, with_docs, package_name)
    write_init_files(init_files, package_name)


def write_init_files(init_files: Dict[str, List], package_name: str = 'boto3_type_annotations'):
    for module, imports in init_files.items():
        if imports:
            file_path = f'{dirname(getcwd())}/{package_name}/boto3_type_annotations/{normalize_module_name(module)}/' \
                        f'__init__.py'
            with open(file_path, 'w') as file_object:
                file_object.write('\n'.join([i.get('import_statement') for i in imports]))
                all_objects = ',\n'.join(f'    \'{i.get("name")}\'' for i in imports)
                file_object.write(f'''
    
__all__ = (
{all_objects}
)
''')


def write_service_paginators(
        session: Session,
        with_docs: bool = False,
        package_name: str = 'boto3_type_annotations'
):
    for service_paginator in parse_service_paginators(session):
        write_service_paginator(service_paginator, with_docs, package_name)


def write_service_waiters(
        session: Session,
        with_docs: bool = False,
        package_name: str = 'boto3_type_annotations'
):
    for service_waiter in parse_service_waiters(session):
        write_service_waiter(service_waiter, with_docs, package_name)


def write_service_resources(
        init_files: Dict,
        session: Session,
        with_docs: bool = False,
        package_name: str = 'boto3_type_annotations'
) -> Dict[str, List]:
    for service_resource in parse_service_resources(session):
        init_files[service_resource.name] += write_service_resource(service_resource, with_docs, package_name)
    return init_files


def write_clients(
        init_files: Dict,
        session: Session,
        with_docs: bool = False,
        package_name: str = 'boto3_type_annotations'
) -> Dict[str, List]:
    for client in parse_clients(session):
        init_files[client.name] += write_client(client, with_docs, package_name)
    return init_files
