from typing import Dict
from botocore.paginate import Paginator


class ListAcceptedPortfolioShares(Paginator):
    def paginate(self, AcceptLanguage: str = None, PortfolioShareType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListConstraintsForPortfolio(Paginator):
    def paginate(self, PortfolioId: str, AcceptLanguage: str = None, ProductId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLaunchPaths(Paginator):
    def paginate(self, ProductId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOrganizationPortfolioAccess(Paginator):
    def paginate(self, PortfolioId: str, OrganizationNodeType: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPortfolios(Paginator):
    def paginate(self, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPortfoliosForProduct(Paginator):
    def paginate(self, ProductId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPrincipalsForPortfolio(Paginator):
    def paginate(self, PortfolioId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListProvisionedProductPlans(Paginator):
    def paginate(self, AcceptLanguage: str = None, ProvisionProductId: str = None, AccessLevelFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListProvisioningArtifactsForServiceAction(Paginator):
    def paginate(self, ServiceActionId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRecordHistory(Paginator):
    def paginate(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, SearchFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResourcesForTagOption(Paginator):
    def paginate(self, TagOptionId: str, ResourceType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListServiceActions(Paginator):
    def paginate(self, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListServiceActionsForProvisioningArtifact(Paginator):
    def paginate(self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTagOptions(Paginator):
    def paginate(self, Filters: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ScanProvisionedProducts(Paginator):
    def paginate(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SearchProductsAsAdmin(Paginator):
    def paginate(self, AcceptLanguage: str = None, PortfolioId: str = None, Filters: Dict = None, SortBy: str = None, SortOrder: str = None, ProductSource: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
