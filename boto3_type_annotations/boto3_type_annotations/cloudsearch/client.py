from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def build_suggesters(self, DomainName: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_domain(self, DomainName: str) -> Dict:
        pass

    def define_analysis_scheme(self, DomainName: str, AnalysisScheme: Dict) -> Dict:
        pass

    def define_expression(self, DomainName: str, Expression: Dict) -> Dict:
        pass

    def define_index_field(self, DomainName: str, IndexField: Dict) -> Dict:
        pass

    def define_suggester(self, DomainName: str, Suggester: Dict) -> Dict:
        pass

    def delete_analysis_scheme(self, DomainName: str, AnalysisSchemeName: str) -> Dict:
        pass

    def delete_domain(self, DomainName: str) -> Dict:
        pass

    def delete_expression(self, DomainName: str, ExpressionName: str) -> Dict:
        pass

    def delete_index_field(self, DomainName: str, IndexFieldName: str) -> Dict:
        pass

    def delete_suggester(self, DomainName: str, SuggesterName: str) -> Dict:
        pass

    def describe_analysis_schemes(self, DomainName: str, AnalysisSchemeNames: List = None, Deployed: bool = None) -> Dict:
        pass

    def describe_availability_options(self, DomainName: str, Deployed: bool = None) -> Dict:
        pass

    def describe_domains(self, DomainNames: List = None) -> Dict:
        pass

    def describe_expressions(self, DomainName: str, ExpressionNames: List = None, Deployed: bool = None) -> Dict:
        pass

    def describe_index_fields(self, DomainName: str, FieldNames: List = None, Deployed: bool = None) -> Dict:
        pass

    def describe_scaling_parameters(self, DomainName: str) -> Dict:
        pass

    def describe_service_access_policies(self, DomainName: str, Deployed: bool = None) -> Dict:
        pass

    def describe_suggesters(self, DomainName: str, SuggesterNames: List = None, Deployed: bool = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def index_documents(self, DomainName: str) -> Dict:
        pass

    def list_domain_names(self) -> Dict:
        pass

    def update_availability_options(self, DomainName: str, MultiAZ: bool) -> Dict:
        pass

    def update_scaling_parameters(self, DomainName: str, ScalingParameters: Dict) -> Dict:
        pass

    def update_service_access_policies(self, DomainName: str, AccessPolicies: str) -> Dict:
        pass
