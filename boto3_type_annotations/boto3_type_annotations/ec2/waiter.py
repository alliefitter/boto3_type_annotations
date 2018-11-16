from typing import List
from typing import Dict
from botocore.waiter import Waiter


class BundleTaskComplete(Waiter):
    def wait(self, BundleIds: List = None, Filters: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ConversionTaskCancelled(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ConversionTaskCompleted(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ConversionTaskDeleted(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class CustomerGatewayAvailable(Waiter):
    def wait(self, CustomerGatewayIds: List = None, Filters: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ExportTaskCancelled(Waiter):
    def wait(self, ExportTaskIds: List = None, WaiterConfig: Dict = None):
        pass


class ExportTaskCompleted(Waiter):
    def wait(self, ExportTaskIds: List = None, WaiterConfig: Dict = None):
        pass


class ImageAvailable(Waiter):
    def wait(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ImageExists(Waiter):
    def wait(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class InstanceExists(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class InstanceRunning(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class InstanceStatusOk(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None, WaiterConfig: Dict = None):
        pass


class InstanceStopped(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class InstanceTerminated(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class KeyPairExists(Waiter):
    def wait(self, Filters: List = None, KeyNames: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class NatGatewayAvailable(Waiter):
    def wait(self, Filters: List = None, MaxResults: int = None, NatGatewayIds: List = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class NetworkInterfaceAvailable(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None):
        pass


class PasswordDataAvailable(Waiter):
    def wait(self, InstanceId: str, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class SnapshotCompleted(Waiter):
    def wait(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class SpotInstanceRequestFulfilled(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, SpotInstanceRequestIds: List = None, WaiterConfig: Dict = None):
        pass


class SubnetAvailable(Waiter):
    def wait(self, Filters: List = None, SubnetIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class SystemStatusOk(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None, WaiterConfig: Dict = None):
        pass


class VolumeAvailable(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class VolumeDeleted(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class VolumeInUse(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class VpcAvailable(Waiter):
    def wait(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class VpcExists(Waiter):
    def wait(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class VpcPeeringConnectionDeleted(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, WaiterConfig: Dict = None):
        pass


class VpcPeeringConnectionExists(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, WaiterConfig: Dict = None):
        pass


class VpnConnectionAvailable(Waiter):
    def wait(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class VpnConnectionDeleted(Waiter):
    def wait(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass
