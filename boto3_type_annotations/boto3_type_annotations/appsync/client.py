from typing import Optional
from typing import Union
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_api_key(self, apiId: str, description: str = None, expires: int = None) -> Dict:
        pass

    def create_data_source(self, apiId: str, name: str, type: str, description: str = None, serviceRoleArn: str = None, dynamodbConfig: Dict = None, lambdaConfig: Dict = None, elasticsearchConfig: Dict = None, httpConfig: Dict = None) -> Dict:
        pass

    def create_graphql_api(self, name: str, authenticationType: str, logConfig: Dict = None, userPoolConfig: Dict = None, openIDConnectConfig: Dict = None) -> Dict:
        pass

    def create_resolver(self, apiId: str, typeName: str, fieldName: str, dataSourceName: str, requestMappingTemplate: str, responseMappingTemplate: str = None) -> Dict:
        pass

    def create_type(self, apiId: str, definition: str, format: str) -> Dict:
        pass

    def delete_api_key(self, apiId: str, id: str) -> Dict:
        pass

    def delete_data_source(self, apiId: str, name: str) -> Dict:
        pass

    def delete_graphql_api(self, apiId: str) -> Dict:
        pass

    def delete_resolver(self, apiId: str, typeName: str, fieldName: str) -> Dict:
        pass

    def delete_type(self, apiId: str, typeName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_data_source(self, apiId: str, name: str) -> Dict:
        pass

    def get_graphql_api(self, apiId: str) -> Dict:
        pass

    def get_introspection_schema(self, apiId: str, format: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_resolver(self, apiId: str, typeName: str, fieldName: str) -> Dict:
        pass

    def get_schema_creation_status(self, apiId: str) -> Dict:
        pass

    def get_type(self, apiId: str, typeName: str, format: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_api_keys(self, apiId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_data_sources(self, apiId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_graphql_apis(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_resolvers(self, apiId: str, typeName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_types(self, apiId: str, format: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def start_schema_creation(self, apiId: str, definition: bytes) -> Dict:
        pass

    def update_api_key(self, apiId: str, id: str, description: str = None, expires: int = None) -> Dict:
        pass

    def update_data_source(self, apiId: str, name: str, type: str, description: str = None, serviceRoleArn: str = None, dynamodbConfig: Dict = None, lambdaConfig: Dict = None, elasticsearchConfig: Dict = None, httpConfig: Dict = None) -> Dict:
        pass

    def update_graphql_api(self, apiId: str, name: str, logConfig: Dict = None, authenticationType: str = None, userPoolConfig: Dict = None, openIDConnectConfig: Dict = None) -> Dict:
        pass

    def update_resolver(self, apiId: str, typeName: str, fieldName: str, dataSourceName: str, requestMappingTemplate: str, responseMappingTemplate: str = None) -> Dict:
        pass

    def update_type(self, apiId: str, typeName: str, format: str, definition: str = None) -> Dict:
        pass
