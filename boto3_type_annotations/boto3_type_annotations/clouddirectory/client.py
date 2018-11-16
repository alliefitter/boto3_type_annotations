from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_facet_to_object(self, DirectoryArn: str, SchemaFacet: Dict, ObjectReference: Dict, ObjectAttributeList: List = None) -> Dict:
        pass

    def apply_schema(self, PublishedSchemaArn: str, DirectoryArn: str) -> Dict:
        pass

    def attach_object(self, DirectoryArn: str, ParentReference: Dict, ChildReference: Dict, LinkName: str) -> Dict:
        pass

    def attach_policy(self, DirectoryArn: str, PolicyReference: Dict, ObjectReference: Dict) -> Dict:
        pass

    def attach_to_index(self, DirectoryArn: str, IndexReference: Dict, TargetReference: Dict) -> Dict:
        pass

    def attach_typed_link(self, DirectoryArn: str, SourceObjectReference: Dict, TargetObjectReference: Dict, TypedLinkFacet: Dict, Attributes: List) -> Dict:
        pass

    def batch_read(self, DirectoryArn: str, Operations: List, ConsistencyLevel: str = None) -> Dict:
        pass

    def batch_write(self, DirectoryArn: str, Operations: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_directory(self, Name: str, SchemaArn: str) -> Dict:
        pass

    def create_facet(self, SchemaArn: str, Name: str, Attributes: List = None, ObjectType: str = None, FacetStyle: str = None) -> Dict:
        pass

    def create_index(self, DirectoryArn: str, OrderedIndexedAttributeList: List, IsUnique: bool, ParentReference: Dict = None, LinkName: str = None) -> Dict:
        pass

    def create_object(self, DirectoryArn: str, SchemaFacets: List, ObjectAttributeList: List = None, ParentReference: Dict = None, LinkName: str = None) -> Dict:
        pass

    def create_schema(self, Name: str) -> Dict:
        pass

    def create_typed_link_facet(self, SchemaArn: str, Facet: Dict) -> Dict:
        pass

    def delete_directory(self, DirectoryArn: str) -> Dict:
        pass

    def delete_facet(self, SchemaArn: str, Name: str) -> Dict:
        pass

    def delete_object(self, DirectoryArn: str, ObjectReference: Dict) -> Dict:
        pass

    def delete_schema(self, SchemaArn: str) -> Dict:
        pass

    def delete_typed_link_facet(self, SchemaArn: str, Name: str) -> Dict:
        pass

    def detach_from_index(self, DirectoryArn: str, IndexReference: Dict, TargetReference: Dict) -> Dict:
        pass

    def detach_object(self, DirectoryArn: str, ParentReference: Dict, LinkName: str) -> Dict:
        pass

    def detach_policy(self, DirectoryArn: str, PolicyReference: Dict, ObjectReference: Dict) -> Dict:
        pass

    def detach_typed_link(self, DirectoryArn: str, TypedLinkSpecifier: Dict):
        pass

    def disable_directory(self, DirectoryArn: str) -> Dict:
        pass

    def enable_directory(self, DirectoryArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_applied_schema_version(self, SchemaArn: str) -> Dict:
        pass

    def get_directory(self, DirectoryArn: str) -> Dict:
        pass

    def get_facet(self, SchemaArn: str, Name: str) -> Dict:
        pass

    def get_link_attributes(self, DirectoryArn: str, TypedLinkSpecifier: Dict, AttributeNames: List, ConsistencyLevel: str = None) -> Dict:
        pass

    def get_object_attributes(self, DirectoryArn: str, ObjectReference: Dict, SchemaFacet: Dict, AttributeNames: List, ConsistencyLevel: str = None) -> Dict:
        pass

    def get_object_information(self, DirectoryArn: str, ObjectReference: Dict, ConsistencyLevel: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_schema_as_json(self, SchemaArn: str) -> Dict:
        pass

    def get_typed_link_facet_information(self, SchemaArn: str, Name: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_applied_schema_arns(self, DirectoryArn: str, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_attached_indices(self, DirectoryArn: str, TargetReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        pass

    def list_development_schema_arns(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_directories(self, NextToken: str = None, MaxResults: int = None, state: str = None) -> Dict:
        pass

    def list_facet_attributes(self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_facet_names(self, SchemaArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_incoming_typed_links(self, DirectoryArn: str, ObjectReference: Dict, FilterAttributeRanges: List = None, FilterTypedLink: Dict = None, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        pass

    def list_index(self, DirectoryArn: str, IndexReference: Dict, RangesOnIndexedValues: List = None, MaxResults: int = None, NextToken: str = None, ConsistencyLevel: str = None) -> Dict:
        pass

    def list_managed_schema_arns(self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_object_attributes(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None, FacetFilter: Dict = None) -> Dict:
        pass

    def list_object_children(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        pass

    def list_object_parent_paths(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_object_parents(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None, IncludeAllLinksToEachParent: bool = None) -> Dict:
        pass

    def list_object_policies(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        pass

    def list_outgoing_typed_links(self, DirectoryArn: str, ObjectReference: Dict, FilterAttributeRanges: List = None, FilterTypedLink: Dict = None, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        pass

    def list_policy_attachments(self, DirectoryArn: str, PolicyReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        pass

    def list_published_schema_arns(self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_typed_link_facet_attributes(self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_typed_link_facet_names(self, SchemaArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def lookup_policy(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def publish_schema(self, DevelopmentSchemaArn: str, Version: str, MinorVersion: str = None, Name: str = None) -> Dict:
        pass

    def put_schema_from_json(self, SchemaArn: str, Document: str) -> Dict:
        pass

    def remove_facet_from_object(self, DirectoryArn: str, SchemaFacet: Dict, ObjectReference: Dict) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass

    def update_facet(self, SchemaArn: str, Name: str, AttributeUpdates: List = None, ObjectType: str = None) -> Dict:
        pass

    def update_link_attributes(self, DirectoryArn: str, TypedLinkSpecifier: Dict, AttributeUpdates: List) -> Dict:
        pass

    def update_object_attributes(self, DirectoryArn: str, ObjectReference: Dict, AttributeUpdates: List) -> Dict:
        pass

    def update_schema(self, SchemaArn: str, Name: str) -> Dict:
        pass

    def update_typed_link_facet(self, SchemaArn: str, Name: str, AttributeUpdates: List, IdentityAttributeOrder: List) -> Dict:
        pass

    def upgrade_applied_schema(self, PublishedSchemaArn: str, DirectoryArn: str, DryRun: bool = None) -> Dict:
        pass

    def upgrade_published_schema(self, DevelopmentSchemaArn: str, PublishedSchemaArn: str, MinorVersion: str, DryRun: bool = None) -> Dict:
        pass
