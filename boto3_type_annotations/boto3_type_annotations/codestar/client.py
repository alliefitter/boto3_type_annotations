from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_team_member(self, projectId: str, userArn: str, projectRole: str, clientRequestToken: str = None, remoteAccessAllowed: bool = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_project(self, name: str, id: str, description: str = None, clientRequestToken: str = None, sourceCode: List = None, toolchain: Dict = None, tags: Dict = None) -> Dict:
        pass

    def create_user_profile(self, userArn: str, displayName: str, emailAddress: str, sshPublicKey: str = None) -> Dict:
        pass

    def delete_project(self, id: str, clientRequestToken: str = None, deleteStack: bool = None) -> Dict:
        pass

    def delete_user_profile(self, userArn: str) -> Dict:
        pass

    def describe_project(self, id: str) -> Dict:
        pass

    def describe_user_profile(self, userArn: str) -> Dict:
        pass

    def disassociate_team_member(self, projectId: str, userArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_projects(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_resources(self, projectId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_tags_for_project(self, id: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_team_members(self, projectId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_user_profiles(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def tag_project(self, id: str, tags: Dict) -> Dict:
        pass

    def untag_project(self, id: str, tags: List) -> Dict:
        pass

    def update_project(self, id: str, name: str = None, description: str = None) -> Dict:
        pass

    def update_team_member(self, projectId: str, userArn: str, projectRole: str = None, remoteAccessAllowed: bool = None) -> Dict:
        pass

    def update_user_profile(self, userArn: str, displayName: str = None, emailAddress: str = None, sshPublicKey: str = None) -> Dict:
        pass
