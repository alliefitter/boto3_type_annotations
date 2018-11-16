from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_cloud_front_origin_access_identity(self, CloudFrontOriginAccessIdentityConfig: Dict) -> Dict:
        pass

    def create_distribution(self, DistributionConfig: Dict) -> Dict:
        pass

    def create_distribution_with_tags(self, DistributionConfigWithTags: Dict) -> Dict:
        pass

    def create_field_level_encryption_config(self, FieldLevelEncryptionConfig: Dict) -> Dict:
        pass

    def create_field_level_encryption_profile(self, FieldLevelEncryptionProfileConfig: Dict) -> Dict:
        pass

    def create_invalidation(self, DistributionId: str, InvalidationBatch: Dict) -> Dict:
        pass

    def create_public_key(self, PublicKeyConfig: Dict) -> Dict:
        pass

    def create_streaming_distribution(self, StreamingDistributionConfig: Dict) -> Dict:
        pass

    def create_streaming_distribution_with_tags(self, StreamingDistributionConfigWithTags: Dict) -> Dict:
        pass

    def delete_cloud_front_origin_access_identity(self, Id: str, IfMatch: str = None) -> NoReturn:
        pass

    def delete_distribution(self, Id: str, IfMatch: str = None) -> NoReturn:
        pass

    def delete_field_level_encryption_config(self, Id: str, IfMatch: str = None) -> NoReturn:
        pass

    def delete_field_level_encryption_profile(self, Id: str, IfMatch: str = None) -> NoReturn:
        pass

    def delete_public_key(self, Id: str, IfMatch: str = None) -> NoReturn:
        pass

    def delete_streaming_distribution(self, Id: str, IfMatch: str = None) -> NoReturn:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_cloud_front_origin_access_identity(self, Id: str) -> Dict:
        pass

    def get_cloud_front_origin_access_identity_config(self, Id: str) -> Dict:
        pass

    def get_distribution(self, Id: str) -> Dict:
        pass

    def get_distribution_config(self, Id: str) -> Dict:
        pass

    def get_field_level_encryption(self, Id: str) -> Dict:
        pass

    def get_field_level_encryption_config(self, Id: str) -> Dict:
        pass

    def get_field_level_encryption_profile(self, Id: str) -> Dict:
        pass

    def get_field_level_encryption_profile_config(self, Id: str) -> Dict:
        pass

    def get_invalidation(self, DistributionId: str, Id: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_public_key(self, Id: str) -> Dict:
        pass

    def get_public_key_config(self, Id: str) -> Dict:
        pass

    def get_streaming_distribution(self, Id: str) -> Dict:
        pass

    def get_streaming_distribution_config(self, Id: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_cloud_front_origin_access_identities(self, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_distributions(self, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_distributions_by_web_acl_id(self, WebACLId: str, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_field_level_encryption_configs(self, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_field_level_encryption_profiles(self, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_invalidations(self, DistributionId: str, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_public_keys(self, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_streaming_distributions(self, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, Resource: str) -> Dict:
        pass

    def tag_resource(self, Resource: str, Tags: Dict) -> NoReturn:
        pass

    def untag_resource(self, Resource: str, TagKeys: Dict) -> NoReturn:
        pass

    def update_cloud_front_origin_access_identity(self, CloudFrontOriginAccessIdentityConfig: Dict, Id: str, IfMatch: str = None) -> Dict:
        pass

    def update_distribution(self, DistributionConfig: Dict, Id: str, IfMatch: str = None) -> Dict:
        pass

    def update_field_level_encryption_config(self, FieldLevelEncryptionConfig: Dict, Id: str, IfMatch: str = None) -> Dict:
        pass

    def update_field_level_encryption_profile(self, FieldLevelEncryptionProfileConfig: Dict, Id: str, IfMatch: str = None) -> Dict:
        pass

    def update_public_key(self, PublicKeyConfig: Dict, Id: str, IfMatch: str = None) -> Dict:
        pass

    def update_streaming_distribution(self, StreamingDistributionConfig: Dict, Id: str, IfMatch: str = None) -> Dict:
        pass
