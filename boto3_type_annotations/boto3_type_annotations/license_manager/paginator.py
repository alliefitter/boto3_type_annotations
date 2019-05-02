from typing import Dict
from typing import List
from botocore.paginate import Paginator


class ListAssociationsForLicenseConfiguration(Paginator):
    def paginate(self, LicenseConfigurationArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLicenseConfigurations(Paginator):
    def paginate(self, LicenseConfigurationArns: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLicenseSpecificationsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResourceInventory(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUsageForLicenseConfiguration(Paginator):
    def paginate(self, LicenseConfigurationArn: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
