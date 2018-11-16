from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_application(self, Author: str, Description: str, Name: str, HomePageUrl: str = None, Labels: List = None, LicenseBody: str = None, LicenseUrl: str = None, ReadmeBody: str = None, ReadmeUrl: str = None, SemanticVersion: str = None, SourceCodeUrl: str = None, SpdxLicenseId: str = None, TemplateBody: str = None, TemplateUrl: str = None) -> Dict:
        pass

    def create_application_version(self, ApplicationId: str, SemanticVersion: str, SourceCodeUrl: str = None, TemplateBody: str = None, TemplateUrl: str = None) -> Dict:
        pass

    def create_cloud_formation_change_set(self, ApplicationId: str, StackName: str, Capabilities: List = None, ChangeSetName: str = None, ClientToken: str = None, Description: str = None, NotificationArns: List = None, ParameterOverrides: List = None, ResourceTypes: List = None, RollbackConfiguration: Dict = None, SemanticVersion: str = None, Tags: List = None, TemplateId: str = None) -> Dict:
        pass

    def create_cloud_formation_template(self, ApplicationId: str, SemanticVersion: str = None) -> Dict:
        pass

    def delete_application(self, ApplicationId: str) -> NoReturn:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_application(self, ApplicationId: str, SemanticVersion: str = None) -> Dict:
        pass

    def get_application_policy(self, ApplicationId: str) -> Dict:
        pass

    def get_cloud_formation_template(self, ApplicationId: str, TemplateId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_application_versions(self, ApplicationId: str, MaxItems: int = None, NextToken: str = None) -> Dict:
        pass

    def list_applications(self, MaxItems: int = None, NextToken: str = None) -> Dict:
        pass

    def put_application_policy(self, ApplicationId: str, Statements: List) -> Dict:
        pass

    def update_application(self, ApplicationId: str, Author: str = None, Description: str = None, HomePageUrl: str = None, Labels: List = None, ReadmeBody: str = None, ReadmeUrl: str = None) -> Dict:
        pass
