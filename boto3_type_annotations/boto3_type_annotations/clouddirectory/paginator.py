from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAppliedSchemaArns(Paginator):
    def paginate(self, DirectoryArn: str, SchemaArn: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAttachedIndices(Paginator):
    def paginate(self, DirectoryArn: str, TargetReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDevelopmentSchemaArns(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDirectories(Paginator):
    def paginate(self, state: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFacetAttributes(Paginator):
    def paginate(self, SchemaArn: str, Name: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFacetNames(Paginator):
    def paginate(self, SchemaArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIndex(Paginator):
    def paginate(self, DirectoryArn: str, IndexReference: Dict, RangesOnIndexedValues: List = None, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListObjectAttributes(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, ConsistencyLevel: str = None, FacetFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListObjectParentPaths(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, PaginationConfig: Dict = None) -> Dict:
        pass


class ListObjectPolicies(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPolicyAttachments(Paginator):
    def paginate(self, DirectoryArn: str, PolicyReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPublishedSchemaArns(Paginator):
    def paginate(self, SchemaArn: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTagsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTypedLinkFacetAttributes(Paginator):
    def paginate(self, SchemaArn: str, Name: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTypedLinkFacetNames(Paginator):
    def paginate(self, SchemaArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class LookupPolicy(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, PaginationConfig: Dict = None) -> Dict:
        pass
