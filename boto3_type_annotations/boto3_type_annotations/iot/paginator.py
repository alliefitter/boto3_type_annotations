from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class ListActiveViolations(Paginator):
    def paginate(self, thingName: str = None, securityProfileName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAttachedPolicies(Paginator):
    def paginate(self, target: str, recursive: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAuditFindings(Paginator):
    def paginate(self, taskId: str = None, checkName: str = None, resourceIdentifier: Dict = None, startTime: datetime = None, endTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAuditTasks(Paginator):
    def paginate(self, startTime: datetime, endTime: datetime, taskType: str = None, taskStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAuthorizers(Paginator):
    def paginate(self, ascendingOrder: bool = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListBillingGroups(Paginator):
    def paginate(self, namePrefixFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCACertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCertificatesByCA(Paginator):
    def paginate(self, caCertificateId: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIndices(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobExecutionsForJob(Paginator):
    def paginate(self, jobId: str, status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobExecutionsForThing(Paginator):
    def paginate(self, thingName: str, status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobs(Paginator):
    def paginate(self, status: str = None, targetSelection: str = None, thingGroupName: str = None, thingGroupId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOTAUpdates(Paginator):
    def paginate(self, otaUpdateStatus: str = None, PaginationConfig: Dict = None) -> Dict:
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


class ListRoleAliases(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListScheduledAudits(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSecurityProfiles(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSecurityProfilesForTarget(Paginator):
    def paginate(self, securityProfileTargetArn: str, recursive: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStreams(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTagsForResource(Paginator):
    def paginate(self, resourceArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTargetsForPolicy(Paginator):
    def paginate(self, policyName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTargetsForSecurityProfile(Paginator):
    def paginate(self, securityProfileName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThingGroups(Paginator):
    def paginate(self, parentGroup: str = None, namePrefixFilter: str = None, recursive: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThingGroupsForThing(Paginator):
    def paginate(self, thingName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThingRegistrationTasks(Paginator):
    def paginate(self, status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThingTypes(Paginator):
    def paginate(self, thingTypeName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThings(Paginator):
    def paginate(self, attributeName: str = None, attributeValue: str = None, thingTypeName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThingsInBillingGroup(Paginator):
    def paginate(self, billingGroupName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThingsInThingGroup(Paginator):
    def paginate(self, thingGroupName: str, recursive: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTopicRules(Paginator):
    def paginate(self, topic: str = None, ruleDisabled: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListV2LoggingLevels(Paginator):
    def paginate(self, targetType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListViolationEvents(Paginator):
    def paginate(self, startTime: datetime, endTime: datetime, thingName: str = None, securityProfileName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
