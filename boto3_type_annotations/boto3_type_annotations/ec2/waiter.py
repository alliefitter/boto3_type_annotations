from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class BundleTaskComplete(Waiter):
    def wait(self, BundleIds: List = None, Filters: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ConversionTaskCancelled(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ConversionTaskCompleted(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ConversionTaskDeleted(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class CustomerGatewayAvailable(Waiter):
    def wait(self, CustomerGatewayIds: List = None, Filters: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ExportTaskCancelled(Waiter):
    def wait(self, ExportTaskIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ExportTaskCompleted(Waiter):
    def wait(self, ExportTaskIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ImageAvailable(Waiter):
    def wait(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ImageExists(Waiter):
    def wait(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceExists(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceRunning(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceStatusOk(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceStopped(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceTerminated(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class KeyPairExists(Waiter):
    def wait(self, Filters: List = None, KeyNames: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class NatGatewayAvailable(Waiter):
    def wait(self, Filters: List = None, MaxResults: int = None, NatGatewayIds: List = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class NetworkInterfaceAvailable(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class PasswordDataAvailable(Waiter):
    def wait(self, InstanceId: str, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class SnapshotCompleted(Waiter):
    def wait(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class SpotInstanceRequestFulfilled(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, SpotInstanceRequestIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class SubnetAvailable(Waiter):
    def wait(self, Filters: List = None, SubnetIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class SystemStatusOk(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VolumeAvailable(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VolumeDeleted(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VolumeInUse(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VpcAvailable(Waiter):
    def wait(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VpcExists(Waiter):
    def wait(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VpcPeeringConnectionDeleted(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VpcPeeringConnectionExists(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VpnConnectionAvailable(Waiter):
    def wait(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class VpnConnectionDeleted(Waiter):
    def wait(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
