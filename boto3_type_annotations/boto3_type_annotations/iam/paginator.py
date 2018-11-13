from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetAccountAuthorizationDetails(Paginator):
    def paginate(self, Filter: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetGroup(Paginator):
    def paginate(self, GroupName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAccessKeys(Paginator):
    def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAccountAliases(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAttachedGroupPolicies(Paginator):
    def paginate(self, GroupName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAttachedRolePolicies(Paginator):
    def paginate(self, RoleName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAttachedUserPolicies(Paginator):
    def paginate(self, UserName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEntitiesForPolicy(Paginator):
    def paginate(self, PolicyArn: str, EntityFilter: str = None, PathPrefix: str = None, PolicyUsageFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroupPolicies(Paginator):
    def paginate(self, GroupName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroups(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroupsForUser(Paginator):
    def paginate(self, UserName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInstanceProfiles(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInstanceProfilesForRole(Paginator):
    def paginate(self, RoleName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListMFADevices(Paginator):
    def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPolicies(Paginator):
    def paginate(self, Scope: str = None, OnlyAttached: bool = None, PathPrefix: str = None, PolicyUsageFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPolicyVersions(Paginator):
    def paginate(self, PolicyArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRolePolicies(Paginator):
    def paginate(self, RoleName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRoles(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSSHPublicKeys(Paginator):
    def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListServerCertificates(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSigningCertificates(Paginator):
    def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUserPolicies(Paginator):
    def paginate(self, UserName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUsers(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListVirtualMFADevices(Paginator):
    def paginate(self, AssignmentStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SimulateCustomPolicy(Paginator):
    def paginate(self, PolicyInputList: List, ActionNames: List, ResourceArns: List = None, ResourcePolicy: str = None, ResourceOwner: str = None, CallerArn: str = None, ContextEntries: List = None, ResourceHandlingOption: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SimulatePrincipalPolicy(Paginator):
    def paginate(self, PolicySourceArn: str, ActionNames: List, PolicyInputList: List = None, ResourceArns: List = None, ResourcePolicy: str = None, ResourceOwner: str = None, CallerArn: str = None, ContextEntries: List = None, ResourceHandlingOption: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
