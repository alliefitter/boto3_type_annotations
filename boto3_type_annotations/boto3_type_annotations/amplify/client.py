from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_app(self, name: str, repository: str, platform: str, oauthToken: str, description: str = None, iamServiceRoleArn: str = None, environmentVariables: Dict = None, enableBranchAutoBuild: bool = None, enableBasicAuth: bool = None, basicAuthCredentials: str = None, customRules: List = None, tags: Dict = None, buildSpec: str = None) -> Dict:
        pass

    def create_branch(self, appId: str, branchName: str, description: str = None, stage: str = None, framework: str = None, enableNotification: bool = None, enableAutoBuild: bool = None, environmentVariables: Dict = None, basicAuthCredentials: str = None, enableBasicAuth: bool = None, tags: Dict = None, buildSpec: str = None, ttl: str = None) -> Dict:
        pass

    def create_domain_association(self, appId: str, domainName: str, subDomainSettings: List, enableAutoSubDomain: bool = None) -> Dict:
        pass

    def delete_app(self, appId: str) -> Dict:
        pass

    def delete_branch(self, appId: str, branchName: str) -> Dict:
        pass

    def delete_domain_association(self, appId: str, domainName: str) -> Dict:
        pass

    def delete_job(self, appId: str, branchName: str, jobId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_app(self, appId: str) -> Dict:
        pass

    def get_branch(self, appId: str, branchName: str) -> Dict:
        pass

    def get_domain_association(self, appId: str, domainName: str) -> Dict:
        pass

    def get_job(self, appId: str, branchName: str, jobId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_apps(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_branches(self, appId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_domain_associations(self, appId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_jobs(self, appId: str, branchName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def start_job(self, appId: str, branchName: str, jobType: str, jobId: str = None, jobReason: str = None, commitId: str = None, commitMessage: str = None, commitTime: datetime = None) -> Dict:
        pass

    def stop_job(self, appId: str, branchName: str, jobId: str) -> Dict:
        pass

    def update_app(self, appId: str, name: str = None, description: str = None, platform: str = None, iamServiceRoleArn: str = None, environmentVariables: Dict = None, enableBranchAutoBuild: bool = None, enableBasicAuth: bool = None, basicAuthCredentials: str = None, customRules: List = None, buildSpec: str = None) -> Dict:
        pass

    def update_branch(self, appId: str, branchName: str, description: str = None, framework: str = None, stage: str = None, enableNotification: bool = None, enableAutoBuild: bool = None, environmentVariables: Dict = None, basicAuthCredentials: str = None, enableBasicAuth: bool = None, buildSpec: str = None, ttl: str = None) -> Dict:
        pass

    def update_domain_association(self, appId: str, domainName: str, subDomainSettings: List, enableAutoSubDomain: bool = None) -> Dict:
        pass
