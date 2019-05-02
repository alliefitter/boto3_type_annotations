from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeActivations(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAssociationExecutionTargets(Paginator):
    def paginate(self, AssociationId: str, ExecutionId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAssociationExecutions(Paginator):
    def paginate(self, AssociationId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAutomationExecutions(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAutomationStepExecutions(Paginator):
    def paginate(self, AutomationExecutionId: str, Filters: List = None, ReverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAvailablePatches(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEffectiveInstanceAssociations(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEffectivePatchesForPatchBaseline(Paginator):
    def paginate(self, BaselineId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstanceAssociationsStatus(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstanceInformation(Paginator):
    def paginate(self, InstanceInformationFilterList: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstancePatchStates(Paginator):
    def paginate(self, InstanceIds: List, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstancePatchStatesForPatchGroup(Paginator):
    def paginate(self, PatchGroup: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstancePatches(Paginator):
    def paginate(self, InstanceId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInventoryDeletions(Paginator):
    def paginate(self, DeletionId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMaintenanceWindowExecutionTaskInvocations(Paginator):
    def paginate(self, WindowExecutionId: str, TaskId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMaintenanceWindowExecutionTasks(Paginator):
    def paginate(self, WindowExecutionId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMaintenanceWindowExecutions(Paginator):
    def paginate(self, WindowId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMaintenanceWindowSchedule(Paginator):
    def paginate(self, WindowId: str = None, Targets: List = None, ResourceType: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMaintenanceWindowTargets(Paginator):
    def paginate(self, WindowId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMaintenanceWindowTasks(Paginator):
    def paginate(self, WindowId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMaintenanceWindows(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMaintenanceWindowsForTarget(Paginator):
    def paginate(self, Targets: List, ResourceType: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeParameters(Paginator):
    def paginate(self, Filters: List = None, ParameterFilters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePatchBaselines(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePatchGroups(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSessions(Paginator):
    def paginate(self, State: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetInventory(Paginator):
    def paginate(self, Filters: List = None, Aggregators: List = None, ResultAttributes: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetInventorySchema(Paginator):
    def paginate(self, TypeName: str = None, Aggregator: bool = None, SubType: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetParameterHistory(Paginator):
    def paginate(self, Name: str, WithDecryption: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetParametersByPath(Paginator):
    def paginate(self, Path: str, Recursive: bool = None, ParameterFilters: List = None, WithDecryption: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAssociationVersions(Paginator):
    def paginate(self, AssociationId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAssociations(Paginator):
    def paginate(self, AssociationFilterList: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCommandInvocations(Paginator):
    def paginate(self, CommandId: str = None, InstanceId: str = None, Filters: List = None, Details: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCommands(Paginator):
    def paginate(self, CommandId: str = None, InstanceId: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListComplianceItems(Paginator):
    def paginate(self, Filters: List = None, ResourceIds: List = None, ResourceTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListComplianceSummaries(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDocumentVersions(Paginator):
    def paginate(self, Name: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDocuments(Paginator):
    def paginate(self, DocumentFilterList: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResourceComplianceSummaries(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResourceDataSync(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
