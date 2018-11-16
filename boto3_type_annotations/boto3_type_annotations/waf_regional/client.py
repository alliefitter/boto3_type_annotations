from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_web_acl(self, WebACLId: str, ResourceArn: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_byte_match_set(self, Name: str, ChangeToken: str) -> Dict:
        pass

    def create_geo_match_set(self, Name: str, ChangeToken: str) -> Dict:
        pass

    def create_ip_set(self, Name: str, ChangeToken: str) -> Dict:
        pass

    def create_rate_based_rule(self, Name: str, MetricName: str, RateKey: str, RateLimit: int, ChangeToken: str) -> Dict:
        pass

    def create_regex_match_set(self, Name: str, ChangeToken: str) -> Dict:
        pass

    def create_regex_pattern_set(self, Name: str, ChangeToken: str) -> Dict:
        pass

    def create_rule(self, Name: str, MetricName: str, ChangeToken: str) -> Dict:
        pass

    def create_rule_group(self, Name: str, MetricName: str, ChangeToken: str) -> Dict:
        pass

    def create_size_constraint_set(self, Name: str, ChangeToken: str) -> Dict:
        pass

    def create_sql_injection_match_set(self, Name: str, ChangeToken: str) -> Dict:
        pass

    def create_web_acl(self, Name: str, MetricName: str, DefaultAction: Dict, ChangeToken: str) -> Dict:
        pass

    def create_xss_match_set(self, Name: str, ChangeToken: str) -> Dict:
        pass

    def delete_byte_match_set(self, ByteMatchSetId: str, ChangeToken: str) -> Dict:
        pass

    def delete_geo_match_set(self, GeoMatchSetId: str, ChangeToken: str) -> Dict:
        pass

    def delete_ip_set(self, IPSetId: str, ChangeToken: str) -> Dict:
        pass

    def delete_logging_configuration(self, ResourceArn: str) -> Dict:
        pass

    def delete_permission_policy(self, ResourceArn: str) -> Dict:
        pass

    def delete_rate_based_rule(self, RuleId: str, ChangeToken: str) -> Dict:
        pass

    def delete_regex_match_set(self, RegexMatchSetId: str, ChangeToken: str) -> Dict:
        pass

    def delete_regex_pattern_set(self, RegexPatternSetId: str, ChangeToken: str) -> Dict:
        pass

    def delete_rule(self, RuleId: str, ChangeToken: str) -> Dict:
        pass

    def delete_rule_group(self, RuleGroupId: str, ChangeToken: str) -> Dict:
        pass

    def delete_size_constraint_set(self, SizeConstraintSetId: str, ChangeToken: str) -> Dict:
        pass

    def delete_sql_injection_match_set(self, SqlInjectionMatchSetId: str, ChangeToken: str) -> Dict:
        pass

    def delete_web_acl(self, WebACLId: str, ChangeToken: str) -> Dict:
        pass

    def delete_xss_match_set(self, XssMatchSetId: str, ChangeToken: str) -> Dict:
        pass

    def disassociate_web_acl(self, ResourceArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_byte_match_set(self, ByteMatchSetId: str) -> Dict:
        pass

    def get_change_token(self) -> Dict:
        pass

    def get_change_token_status(self, ChangeToken: str) -> Dict:
        pass

    def get_geo_match_set(self, GeoMatchSetId: str) -> Dict:
        pass

    def get_ip_set(self, IPSetId: str) -> Dict:
        pass

    def get_logging_configuration(self, ResourceArn: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_permission_policy(self, ResourceArn: str) -> Dict:
        pass

    def get_rate_based_rule(self, RuleId: str) -> Dict:
        pass

    def get_rate_based_rule_managed_keys(self, RuleId: str, NextMarker: str = None) -> Dict:
        pass

    def get_regex_match_set(self, RegexMatchSetId: str) -> Dict:
        pass

    def get_regex_pattern_set(self, RegexPatternSetId: str) -> Dict:
        pass

    def get_rule(self, RuleId: str) -> Dict:
        pass

    def get_rule_group(self, RuleGroupId: str) -> Dict:
        pass

    def get_sampled_requests(self, WebAclId: str, RuleId: str, TimeWindow: Dict, MaxItems: int) -> Dict:
        pass

    def get_size_constraint_set(self, SizeConstraintSetId: str) -> Dict:
        pass

    def get_sql_injection_match_set(self, SqlInjectionMatchSetId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def get_web_acl(self, WebACLId: str) -> Dict:
        pass

    def get_web_acl_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def get_xss_match_set(self, XssMatchSetId: str) -> Dict:
        pass

    def list_activated_rules_in_rule_group(self, RuleGroupId: str = None, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_byte_match_sets(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_geo_match_sets(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_ip_sets(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_logging_configurations(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_rate_based_rules(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_regex_match_sets(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_regex_pattern_sets(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_resources_for_web_acl(self, WebACLId: str, ResourceType: str = None) -> Dict:
        pass

    def list_rule_groups(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_rules(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_size_constraint_sets(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_sql_injection_match_sets(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_subscribed_rule_groups(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_web_acls(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def list_xss_match_sets(self, NextMarker: str = None, Limit: int = None) -> Dict:
        pass

    def put_logging_configuration(self, LoggingConfiguration: Dict) -> Dict:
        pass

    def put_permission_policy(self, ResourceArn: str, Policy: str) -> Dict:
        pass

    def update_byte_match_set(self, ByteMatchSetId: str, ChangeToken: str, Updates: List) -> Dict:
        pass

    def update_geo_match_set(self, GeoMatchSetId: str, ChangeToken: str, Updates: List) -> Dict:
        pass

    def update_ip_set(self, IPSetId: str, ChangeToken: str, Updates: List) -> Dict:
        pass

    def update_rate_based_rule(self, RuleId: str, ChangeToken: str, Updates: List, RateLimit: int) -> Dict:
        pass

    def update_regex_match_set(self, RegexMatchSetId: str, Updates: List, ChangeToken: str) -> Dict:
        pass

    def update_regex_pattern_set(self, RegexPatternSetId: str, Updates: List, ChangeToken: str) -> Dict:
        pass

    def update_rule(self, RuleId: str, ChangeToken: str, Updates: List) -> Dict:
        pass

    def update_rule_group(self, RuleGroupId: str, Updates: List, ChangeToken: str) -> Dict:
        pass

    def update_size_constraint_set(self, SizeConstraintSetId: str, ChangeToken: str, Updates: List) -> Dict:
        pass

    def update_sql_injection_match_set(self, SqlInjectionMatchSetId: str, ChangeToken: str, Updates: List) -> Dict:
        pass

    def update_web_acl(self, WebACLId: str, ChangeToken: str, Updates: List = None, DefaultAction: Dict = None) -> Dict:
        pass

    def update_xss_match_set(self, XssMatchSetId: str, ChangeToken: str, Updates: List) -> Dict:
        pass
