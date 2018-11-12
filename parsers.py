import inspect
from datetime import datetime
from inspect import getdoc
from typing import IO, List, Callable, Dict, Generator, Tuple, Union, Set

import boto3
from boto3.docs.utils import is_resource_action
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.session import Session
from boto3.s3.transfer import TransferConfig
from boto3.utils import ServiceContext
from botocore.client import BaseClient
from botocore.docs.method import get_instance_public_methods
from botocore.exceptions import UnknownServiceError
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from docstring_parser import parse
from docstring_parser.parser import DocstringMeta

from structures import Argument, Method, Client, Attribute, Resource, Collection, ServiceResource
from type_map import TYPE_MAP


def get_resource_public_actions(resource_class):
    resource_class_members = inspect.getmembers(resource_class)
    resource_methods = {}
    for name, member in resource_class_members:
        if not name.startswith('_'):
            if not name[0].isupper():
                if is_resource_action(member):
                    resource_methods[name] = member
    return resource_methods


def manually_set_method(name: str) -> Method:
    methods = {
        'create_tags': Method(
            'create_tags',
            [
                Argument(
                    'DryRun',
                    bool,
                    False
                ),
                Argument(
                    'Resources',
                    'List[str]',
                    True
                ),
                Argument(
                    'Tags',
                    List,
                    True
                )
            ],
            '',
            None
        )
    }
    return methods.get(
        name,
        Method(
            name,
            [],
            None,
            None
        )
    )


def parse_argument_type(arg_name: str, meta: List) -> Union[type, Tuple, str]:
    return next(filter(lambda m: m.args[0] == 'type' and m.args[1] == arg_name, meta)).description


def parse_arguments(parsed_doc) -> Generator[Argument, None, None]:
    for arg in parsed_doc.params:
        yield Argument(
            arg.arg_name,
            parse_type_from_str(
                parse_argument_type(arg.arg_name, parsed_doc.meta)
            ),
            arg.description.startswith('**[REQUIRED]**')
        )


def parse_attributes(resource: Boto3ServiceResource) -> Generator[Attribute, None, None]:
    service_model = resource.meta.client.meta.service_model
    if resource.meta.resource_model.shape:
        shape = service_model.shape_for(resource.meta.resource_model.shape)
        attributes = resource.meta.resource_model.get_attributes(shape)
        for name, attribute in attributes.items():
            yield Attribute(
                name,
                parse_type_from_str(attribute[1].type_name)
            )


def parse_attribute_types(resource: Boto3ServiceResource) -> Set[str]:
    types = set()
    service_model = resource.meta.client.meta.service_model
    if resource.meta.resource_model.shape:
        shape = service_model.shape_for(resource.meta.resource_model.shape)
        attributes = resource.meta.resource_model.get_attributes(shape)
        for name, attribute in attributes.items():
            types.add(attribute[1].type_name)
    return types


def parse_clients(session: Session) -> Generator[Client, None, None]:
    for name in session.get_available_services():
        print(f'Parsing: {name}')
        client = session.client(name)
        yield Client(
            name,
            list(parse_methods(get_instance_public_methods(client)))
        )


def parse_client_types(session: Session) -> Set[str]:
    types = set()
    for name in session.get_available_services():
        print(f'Parsing: {name}')
        client = session.client(name)
        types = types.union(types.union(parse_method_types(get_instance_public_methods(client))))
    return types


def parse_identifiers(resource: Boto3ServiceResource) -> Generator[Attribute, None, None]:
    identifiers = resource.meta.resource_model.identifiers
    for identifier in identifiers:
        yield Attribute(
            identifier.name,
            parse_type_from_str('string')
        )


def parse_methods(public_methods: Dict) -> Generator[Method, None, None]:
    for name, method in public_methods.items():
        doc = getdoc(method)
        if doc is None:
            print('Docless method: ', name)
            yield manually_set_method(name)
        else:
            parsed_doc = parse(doc.replace('::', ''))
            yield Method(
                name,
                list(parse_arguments(parsed_doc)),
                doc,
                parse_return_type(parsed_doc.meta)
            )


def parse_method_types(public_methods: Dict) -> Set[str]:
    types = set()
    for name, method in public_methods.items():
        doc = getdoc(method)
        parsed_doc = parse(doc.replace('::', ''))
        for arg in parsed_doc.params:
            types.add(parse_argument_type(arg.arg_name, parsed_doc.meta))
        types.add(parse_return_type(parsed_doc.meta))
    return types


def parse_collections(resource: Boto3ServiceResource) -> Generator[Collection, None, None]:
    for collection in resource.meta.resource_model.collections:
        yield Collection(
            collection.name,
            list(parse_methods(get_instance_public_methods(getattr(resource, collection.name))))
        )


def parse_resource(resource: Boto3ServiceResource):
    return Resource(
        resource.__class__.__name__.split('.')[1],
        list(parse_methods(get_resource_public_actions(resource.__class__))),
        list(parse_attributes(resource)) + list(parse_identifiers(resource)),
        list(parse_collections(resource))
    )


def parse_service_resources(session: Session) -> Generator[ServiceResource, None, None]:
    for resource_name in session.get_available_resources():
        service_resource = session.resource(resource_name)
        print('Parsing: ', resource_name)
        yield ServiceResource(
            resource_name,
            list(parse_methods(get_instance_public_methods(service_resource))),
            list(parse_attributes(service_resource)) + list(parse_identifiers(service_resource)),
            list(parse_collections(service_resource)),
            [parse_resource(resource) for resource in retrieve_sub_resources(session, service_resource)]
        )


def parse_return_type(meta: List[DocstringMeta]) -> Union[str, None]:
    return_type = None
    if any([m.args[0] == 'rtype' for m in meta]):
        try:
            return_type = parse_type_from_str(next(filter(lambda m: m.args[0] == 'rtype', meta)).description)
        except StopIteration:
            print(next(filter(lambda m: m.args[0] == 'rtype', meta)).description)
    return return_type


def parse_service_resource_types(session: Session) -> Set[str]:
    types = set()
    for resource_name in session.get_available_resources():
        service_resource = session.resource(resource_name)
        types = types.union(parse_method_types(get_resource_public_actions(service_resource)))
        types = types.union(parse_attribute_types(service_resource))
        for collection in service_resource.meta.resource_model.collections:
            types = types.union(parse_method_types(get_instance_public_methods(getattr(service_resource, collection.name))))
        for resource in retrieve_sub_resources(session, service_resource):
            types = types.union(parse_method_types(get_resource_public_actions(resource.__class__)))
            types = types.union(parse_attribute_types(resource))
            for collection in resource.meta.resource_model.collections:
                types = types.union(parse_method_types(get_instance_public_methods(getattr(resource, collection.name))))
    return types


def parse_type_from_str(type_str: str) -> Union[type, Tuple, str]:
    return next(filter(lambda item: type_str in item[1], TYPE_MAP.items()))[0]


def retrieve_sub_resources(session, resource) -> Generator[Boto3ServiceResource, None, None]:
    loader = session._session.get_component('data_loader')
    json_resource_model = loader.load_service_model(
        resource.meta.service_name,
        'resources-1'
    )
    service_model = resource.meta.client.meta.service_model
    try:
        service_waiter_model = session._session.get_waiter_model(service_model.service_name)
    except UnknownServiceError:
        service_waiter_model = None
    for name in json_resource_model['resources']:
        resource_model = json_resource_model['resources'][name]
        cls = session.resource_factory.load_from_definition(
            resource_name=name,
            single_resource_json_definition=resource_model,
            service_context=ServiceContext(
                service_name=resource.meta.service_name,
                resource_json_definitions=json_resource_model['resources'],
                service_model=service_model,
                service_waiter_model=service_waiter_model
            )
        )
        identifiers = cls.meta.resource_model.identifiers
        args = []
        for _ in identifiers:
            args.append('foo')
        yield cls(*args, client=boto3.client(resource.meta.service_name))
