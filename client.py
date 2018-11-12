import builtins
from datetime import datetime
from inspect import getdoc, getmodule
from keyword import kwlist
from os import getcwd, mkdir
from shutil import rmtree
from typing import List, Dict, IO, Union, Callable, NamedTuple, Set, Generator, Tuple

import boto3
from boto3.session import Session
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.docs.method import get_instance_public_methods
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from docstring_parser import parse
from docstring_parser.parser import DocstringMeta


def add_indentation_to_docstring(docstring: str, levels: int):
    indention = "".join(["    " for _ in range(levels)])
    return '\n'.join([f'{indention}{line}' for line in docstring.split('\n')])


def create_import_statements(types: Set[type]):
    for _type in types:
        if getmodule(_type) != builtins and getmodule(_type) is not None:
            yield f'from {normalize_type_name(getmodule(_type))} import {normalize_type_name(_type)}'


def format_arguments(method):
    for argument in method.arguments:
        _type = normalize_type_name(argument.type) if argument.required \
            else f'Optional[{normalize_type_name(argument.type)}]'
        yield f'{argument.name}: {_type}'


def normalize_module_name(name: str):
    name = name.replace('-', '_')
    if name in kwlist:
        name = f'{name}_'
    return name


def normalize_type_name(_type: Union[type, Tuple]):
    if isinstance(_type, tuple):
        return f'Union[{", ".join([normalize_type_name(t) for t in _type])}]'
    return _type._name if hasattr(_type, '_name') and not hasattr(_type, '__name__') else _type.__name__


def retrieve_argument_types(method: Method) -> Set[type]:
    types = set()
    for arg in method.arguments:
        types.add(arg.type) if not isinstance(arg.type, tuple) else [types.add(t) for t in arg.type]
    return types


def retrieve_types(client: Client) -> Set[type]:
    types = set()
    for method_types in retrieve_method_types(client.methods):
        types = types.union(method_types)
    return types


def retrieve_method_types(methods: List[Method]) -> Generator[Set, None, None]:
    for m in methods:
        argument_types = retrieve_argument_types(m)
        argument_types.add(m.return_type)
        yield argument_types


def write_clients(clients: List[Client]):
    rmtree(f'{getcwd()}/client')
    mkdir(f'{getcwd()}/client')
    write_init(clients)
    for client in clients:
        print(f'Writing: {client.name}')
        write_client(client)


def write_client(client: Client):
    with open(f'{getcwd()}/client/{normalize_module_name(client.name)}.py', 'w') as file_object:
        file_object.write('\n'.join(list(create_import_statements(retrieve_types(client)))))
        file_object.write('\nfrom typing import Optional, NoReturn\n')
        BaseClient in retrieve_types(client) or file_object.write('\nfrom botocore import BaseClient\n')
        file_object.write(f'\n\nclass {normalize_module_name(client.name)}(BaseClient):')
        write_methods(client, file_object)


def write_init(clients: List[Client]):
    with open(f'{getcwd()}/client/__init__.py', 'w') as file_object:
        file_object.write(
            '\n'.join(
                [
                    f'from client.{normalize_module_name(client.name)}'
                    f' import {normalize_module_name(client.name)}'
                    for client in clients
                ]
            )
        )
        modules = ',\n'.join([f'    \'{normalize_module_name(client.name)}\'' for client in clients])
        file_object.write(
            f'''
__all__ = [
{modules}
]
'''
        )


def write_methods(client, file_object: IO):
    for method in client.methods:
        write_method(method, file_object)


def write_method(method: Method, file_object: IO, method_body: str = 'pass'):
    file_object.write(f'''
    def {method.name}(self, {', '.join(format_arguments(method))}) -> {normalize_type_name(method.return_type) 
                                                                           if method.return_type is not None 
                                                                           else 'NoReturn'}:
        """
{add_indentation_to_docstring(method.docstring, 2)}
        """
        {method_body}
''')


if __name__ == '__main__':
    write_clients(list(parse_clients(boto3.session.Session())))
