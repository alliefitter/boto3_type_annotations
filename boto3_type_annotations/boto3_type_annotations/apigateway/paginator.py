from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetApiKeys(Paginator):
    def paginate(self, nameQuery: str = None, customerId: str = None, includeValues: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetBasePathMappings(Paginator):
    def paginate(self, domainName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class GetClientCertificates(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDeployments(Paginator):
    def paginate(self, restApiId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDomainNames(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetModels(Paginator):
    def paginate(self, restApiId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class GetResources(Paginator):
    def paginate(self, restApiId: str, embed: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetRestApis(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetUsage(Paginator):
    def paginate(self, usagePlanId: str, startDate: str, endDate: str, keyId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetUsagePlanKeys(Paginator):
    def paginate(self, usagePlanId: str, nameQuery: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetUsagePlans(Paginator):
    def paginate(self, keyId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetVpcLinks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
