from typing import NamedTuple, List, Union, Tuple


class Attribute(NamedTuple):
    name: str
    type: Union[type, Tuple, str]


class Argument(NamedTuple):
    name: str
    type: Union[type, Tuple, str]
    required: bool


class Method(NamedTuple):
    name: str
    arguments: List[Argument]
    docstring: str
    return_type: Union[type, Tuple, str]


class Collection(NamedTuple):
    name: str
    methods: List[Method]


class Resource(NamedTuple):
    name: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]


class Waiter(NamedTuple):
    name: str
    methods: List[Method]


class Paginator(NamedTuple):
    name: str
    methods: List[Method]


class ServiceResource(NamedTuple):
    name: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]
    sub_resources: List[Resource]


class Client(NamedTuple):
    name: str
    methods: List[Method]


class ServiceWaiter(NamedTuple):
    name: str
    waiters: List[Waiter]


class ServicePaginator(NamedTuple):
    name: str
    paginators: List[Paginator]


class Config(NamedTuple):
    services: List
    with_docs: bool
    with_clients: bool
    with_service_resources: bool
    with_paginators: bool
    with_waiters: bool
    package_name: str
    module_name: str
    version: str
    readme: str
    license: str
