from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def allocate_static_ip(self, staticIpName: str) -> Dict:
        pass

    def attach_disk(self, diskName: str, instanceName: str, diskPath: str) -> Dict:
        pass

    def attach_instances_to_load_balancer(self, loadBalancerName: str, instanceNames: List) -> Dict:
        pass

    def attach_load_balancer_tls_certificate(self, loadBalancerName: str, certificateName: str) -> Dict:
        pass

    def attach_static_ip(self, staticIpName: str, instanceName: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def close_instance_public_ports(self, portInfo: Dict, instanceName: str) -> Dict:
        pass

    def create_disk(self, diskName: str, availabilityZone: str, sizeInGb: int) -> Dict:
        pass

    def create_disk_from_snapshot(self, diskName: str, diskSnapshotName: str, availabilityZone: str, sizeInGb: int) -> Dict:
        pass

    def create_disk_snapshot(self, diskName: str, diskSnapshotName: str) -> Dict:
        pass

    def create_domain(self, domainName: str) -> Dict:
        pass

    def create_domain_entry(self, domainName: str, domainEntry: Dict) -> Dict:
        pass

    def create_instance_snapshot(self, instanceSnapshotName: str, instanceName: str) -> Dict:
        pass

    def create_instances(self, instanceNames: List, availabilityZone: str, blueprintId: str, bundleId: str, customImageName: str = None, userData: str = None, keyPairName: str = None) -> Dict:
        pass

    def create_instances_from_snapshot(self, instanceNames: List, availabilityZone: str, instanceSnapshotName: str, bundleId: str, attachedDiskMapping: Dict = None, userData: str = None, keyPairName: str = None) -> Dict:
        pass

    def create_key_pair(self, keyPairName: str) -> Dict:
        pass

    def create_load_balancer(self, loadBalancerName: str, instancePort: int, healthCheckPath: str = None, certificateName: str = None, certificateDomainName: str = None, certificateAlternativeNames: List = None) -> Dict:
        pass

    def create_load_balancer_tls_certificate(self, loadBalancerName: str, certificateName: str, certificateDomainName: str, certificateAlternativeNames: List = None) -> Dict:
        pass

    def create_relational_database(self, relationalDatabaseName: str, relationalDatabaseBlueprintId: str, relationalDatabaseBundleId: str, masterDatabaseName: str, masterUsername: str, availabilityZone: str = None, masterUserPassword: str = None, preferredBackupWindow: str = None, preferredMaintenanceWindow: str = None, publiclyAccessible: bool = None) -> Dict:
        pass

    def create_relational_database_from_snapshot(self, relationalDatabaseName: str, availabilityZone: str = None, publiclyAccessible: bool = None, relationalDatabaseSnapshotName: str = None, relationalDatabaseBundleId: str = None, sourceRelationalDatabaseName: str = None, restoreTime: datetime = None, useLatestRestorableTime: bool = None) -> Dict:
        pass

    def create_relational_database_snapshot(self, relationalDatabaseName: str, relationalDatabaseSnapshotName: str) -> Dict:
        pass

    def delete_disk(self, diskName: str) -> Dict:
        pass

    def delete_disk_snapshot(self, diskSnapshotName: str) -> Dict:
        pass

    def delete_domain(self, domainName: str) -> Dict:
        pass

    def delete_domain_entry(self, domainName: str, domainEntry: Dict) -> Dict:
        pass

    def delete_instance(self, instanceName: str) -> Dict:
        pass

    def delete_instance_snapshot(self, instanceSnapshotName: str) -> Dict:
        pass

    def delete_key_pair(self, keyPairName: str) -> Dict:
        pass

    def delete_load_balancer(self, loadBalancerName: str) -> Dict:
        pass

    def delete_load_balancer_tls_certificate(self, loadBalancerName: str, certificateName: str, force: bool = None) -> Dict:
        pass

    def delete_relational_database(self, relationalDatabaseName: str, skipFinalSnapshot: bool = None, finalRelationalDatabaseSnapshotName: str = None) -> Dict:
        pass

    def delete_relational_database_snapshot(self, relationalDatabaseSnapshotName: str) -> Dict:
        pass

    def detach_disk(self, diskName: str) -> Dict:
        pass

    def detach_instances_from_load_balancer(self, loadBalancerName: str, instanceNames: List) -> Dict:
        pass

    def detach_static_ip(self, staticIpName: str) -> Dict:
        pass

    def download_default_key_pair(self) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_active_names(self, pageToken: str = None) -> Dict:
        pass

    def get_blueprints(self, includeInactive: bool = None, pageToken: str = None) -> Dict:
        pass

    def get_bundles(self, includeInactive: bool = None, pageToken: str = None) -> Dict:
        pass

    def get_disk(self, diskName: str) -> Dict:
        pass

    def get_disk_snapshot(self, diskSnapshotName: str) -> Dict:
        pass

    def get_disk_snapshots(self, pageToken: str = None) -> Dict:
        pass

    def get_disks(self, pageToken: str = None) -> Dict:
        pass

    def get_domain(self, domainName: str) -> Dict:
        pass

    def get_domains(self, pageToken: str = None) -> Dict:
        pass

    def get_instance(self, instanceName: str) -> Dict:
        pass

    def get_instance_access_details(self, instanceName: str, protocol: str = None) -> Dict:
        pass

    def get_instance_metric_data(self, instanceName: str, metricName: str, period: int, startTime: datetime, endTime: datetime, unit: str, statistics: List) -> Dict:
        pass

    def get_instance_port_states(self, instanceName: str) -> Dict:
        pass

    def get_instance_snapshot(self, instanceSnapshotName: str) -> Dict:
        pass

    def get_instance_snapshots(self, pageToken: str = None) -> Dict:
        pass

    def get_instance_state(self, instanceName: str) -> Dict:
        pass

    def get_instances(self, pageToken: str = None) -> Dict:
        pass

    def get_key_pair(self, keyPairName: str) -> Dict:
        pass

    def get_key_pairs(self, pageToken: str = None) -> Dict:
        pass

    def get_load_balancer(self, loadBalancerName: str) -> Dict:
        pass

    def get_load_balancer_metric_data(self, loadBalancerName: str, metricName: str, period: int, startTime: datetime, endTime: datetime, unit: str, statistics: List) -> Dict:
        pass

    def get_load_balancer_tls_certificates(self, loadBalancerName: str) -> Dict:
        pass

    def get_load_balancers(self, pageToken: str = None) -> Dict:
        pass

    def get_operation(self, operationId: str) -> Dict:
        pass

    def get_operations(self, pageToken: str = None) -> Dict:
        pass

    def get_operations_for_resource(self, resourceName: str, pageToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_regions(self, includeAvailabilityZones: bool = None, includeRelationalDatabaseAvailabilityZones: bool = None) -> Dict:
        pass

    def get_relational_database(self, relationalDatabaseName: str) -> Dict:
        pass

    def get_relational_database_blueprints(self, pageToken: str = None) -> Dict:
        pass

    def get_relational_database_bundles(self, pageToken: str = None) -> Dict:
        pass

    def get_relational_database_events(self, relationalDatabaseName: str, durationInMinutes: int = None, pageToken: str = None) -> Dict:
        pass

    def get_relational_database_log_events(self, relationalDatabaseName: str, logStreamName: str, startTime: datetime = None, endTime: datetime = None, startFromHead: bool = None, pageToken: str = None) -> Dict:
        pass

    def get_relational_database_log_streams(self, relationalDatabaseName: str) -> Dict:
        pass

    def get_relational_database_master_user_password(self, relationalDatabaseName: str, passwordVersion: str = None) -> Dict:
        pass

    def get_relational_database_metric_data(self, relationalDatabaseName: str, metricName: str, period: int, startTime: datetime, endTime: datetime, unit: str, statistics: List) -> Dict:
        pass

    def get_relational_database_parameters(self, relationalDatabaseName: str, pageToken: str = None) -> Dict:
        pass

    def get_relational_database_snapshot(self, relationalDatabaseSnapshotName: str) -> Dict:
        pass

    def get_relational_database_snapshots(self, pageToken: str = None) -> Dict:
        pass

    def get_relational_databases(self, pageToken: str = None) -> Dict:
        pass

    def get_static_ip(self, staticIpName: str) -> Dict:
        pass

    def get_static_ips(self, pageToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_key_pair(self, keyPairName: str, publicKeyBase64: str) -> Dict:
        pass

    def is_vpc_peered(self) -> Dict:
        pass

    def open_instance_public_ports(self, portInfo: Dict, instanceName: str) -> Dict:
        pass

    def peer_vpc(self) -> Dict:
        pass

    def put_instance_public_ports(self, portInfos: List, instanceName: str) -> Dict:
        pass

    def reboot_instance(self, instanceName: str) -> Dict:
        pass

    def reboot_relational_database(self, relationalDatabaseName: str) -> Dict:
        pass

    def release_static_ip(self, staticIpName: str) -> Dict:
        pass

    def start_instance(self, instanceName: str) -> Dict:
        pass

    def start_relational_database(self, relationalDatabaseName: str) -> Dict:
        pass

    def stop_instance(self, instanceName: str, force: bool = None) -> Dict:
        pass

    def stop_relational_database(self, relationalDatabaseName: str, relationalDatabaseSnapshotName: str = None) -> Dict:
        pass

    def unpeer_vpc(self) -> Dict:
        pass

    def update_domain_entry(self, domainName: str, domainEntry: Dict) -> Dict:
        pass

    def update_load_balancer_attribute(self, loadBalancerName: str, attributeName: str, attributeValue: str) -> Dict:
        pass

    def update_relational_database(self, relationalDatabaseName: str, masterUserPassword: str = None, rotateMasterUserPassword: bool = None, preferredBackupWindow: str = None, preferredMaintenanceWindow: str = None, enableBackupRetention: bool = None, disableBackupRetention: bool = None, publiclyAccessible: bool = None, applyImmediately: bool = None) -> Dict:
        pass

    def update_relational_database_parameters(self, relationalDatabaseName: str, parameters: List) -> Dict:
        pass
