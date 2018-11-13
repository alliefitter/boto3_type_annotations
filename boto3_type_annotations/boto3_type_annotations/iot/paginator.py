from typing import Dict
from botocore.paginate import Paginator


class ListCACertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCertificatesByCA(Paginator):
    def paginate(self, caCertificateId: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOutgoingCertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPolicies(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPolicyPrincipals(Paginator):
    def paginate(self, policyName: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPrincipalPolicies(Paginator):
    def paginate(self, principal: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPrincipalThings(Paginator):
    def paginate(self, principal: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThingTypes(Paginator):
    def paginate(self, thingTypeName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThings(Paginator):
    def paginate(self, attributeName: str = None, attributeValue: str = None, thingTypeName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTopicRules(Paginator):
    def paginate(self, topic: str = None, ruleDisabled: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
