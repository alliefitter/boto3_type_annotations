from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_device_pool(self, projectArn: str, name: str, rules: List, description: str = None) -> Dict:
        pass

    def create_instance_profile(self, name: str, description: str = None, packageCleanup: bool = None, excludeAppPackagesFromCleanup: List = None, rebootAfterUse: bool = None) -> Dict:
        pass

    def create_network_profile(self, projectArn: str, name: str, description: str = None, type: str = None, uplinkBandwidthBits: int = None, downlinkBandwidthBits: int = None, uplinkDelayMs: int = None, downlinkDelayMs: int = None, uplinkJitterMs: int = None, downlinkJitterMs: int = None, uplinkLossPercent: int = None, downlinkLossPercent: int = None) -> Dict:
        pass

    def create_project(self, name: str, defaultJobTimeoutMinutes: int = None) -> Dict:
        pass

    def create_remote_access_session(self, projectArn: str, deviceArn: str, instanceArn: str = None, sshPublicKey: str = None, remoteDebugEnabled: bool = None, remoteRecordEnabled: bool = None, remoteRecordAppArn: str = None, name: str = None, clientId: str = None, configuration: Dict = None, interactionMode: str = None, skipAppResign: bool = None) -> Dict:
        pass

    def create_upload(self, projectArn: str, name: str, type: str, contentType: str = None) -> Dict:
        pass

    def create_vpce_configuration(self, vpceConfigurationName: str, vpceServiceName: str, serviceDnsName: str, vpceConfigurationDescription: str = None) -> Dict:
        pass

    def delete_device_pool(self, arn: str) -> Dict:
        pass

    def delete_instance_profile(self, arn: str) -> Dict:
        pass

    def delete_network_profile(self, arn: str) -> Dict:
        pass

    def delete_project(self, arn: str) -> Dict:
        pass

    def delete_remote_access_session(self, arn: str) -> Dict:
        pass

    def delete_run(self, arn: str) -> Dict:
        pass

    def delete_upload(self, arn: str) -> Dict:
        pass

    def delete_vpce_configuration(self, arn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_account_settings(self) -> Dict:
        pass

    def get_device(self, arn: str) -> Dict:
        pass

    def get_device_instance(self, arn: str) -> Dict:
        pass

    def get_device_pool(self, arn: str) -> Dict:
        pass

    def get_device_pool_compatibility(self, devicePoolArn: str, appArn: str = None, testType: str = None, test: Dict = None, configuration: Dict = None) -> Dict:
        pass

    def get_instance_profile(self, arn: str) -> Dict:
        pass

    def get_job(self, arn: str) -> Dict:
        pass

    def get_network_profile(self, arn: str) -> Dict:
        pass

    def get_offering_status(self, nextToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_project(self, arn: str) -> Dict:
        pass

    def get_remote_access_session(self, arn: str) -> Dict:
        pass

    def get_run(self, arn: str) -> Dict:
        pass

    def get_suite(self, arn: str) -> Dict:
        pass

    def get_test(self, arn: str) -> Dict:
        pass

    def get_upload(self, arn: str) -> Dict:
        pass

    def get_vpce_configuration(self, arn: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def install_to_remote_access_session(self, remoteAccessSessionArn: str, appArn: str) -> Dict:
        pass

    def list_artifacts(self, arn: str, type: str, nextToken: str = None) -> Dict:
        pass

    def list_device_instances(self, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_device_pools(self, arn: str, type: str = None, nextToken: str = None) -> Dict:
        pass

    def list_devices(self, arn: str = None, nextToken: str = None) -> Dict:
        pass

    def list_instance_profiles(self, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_jobs(self, arn: str, nextToken: str = None) -> Dict:
        pass

    def list_network_profiles(self, arn: str, type: str = None, nextToken: str = None) -> Dict:
        pass

    def list_offering_promotions(self, nextToken: str = None) -> Dict:
        pass

    def list_offering_transactions(self, nextToken: str = None) -> Dict:
        pass

    def list_offerings(self, nextToken: str = None) -> Dict:
        pass

    def list_projects(self, arn: str = None, nextToken: str = None) -> Dict:
        pass

    def list_remote_access_sessions(self, arn: str, nextToken: str = None) -> Dict:
        pass

    def list_runs(self, arn: str, nextToken: str = None) -> Dict:
        pass

    def list_samples(self, arn: str, nextToken: str = None) -> Dict:
        pass

    def list_suites(self, arn: str, nextToken: str = None) -> Dict:
        pass

    def list_tests(self, arn: str, nextToken: str = None) -> Dict:
        pass

    def list_unique_problems(self, arn: str, nextToken: str = None) -> Dict:
        pass

    def list_uploads(self, arn: str, type: str = None, nextToken: str = None) -> Dict:
        pass

    def list_vpce_configurations(self, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def purchase_offering(self, offeringId: str = None, quantity: int = None, offeringPromotionId: str = None) -> Dict:
        pass

    def renew_offering(self, offeringId: str = None, quantity: int = None) -> Dict:
        pass

    def schedule_run(self, projectArn: str, devicePoolArn: str, test: Dict, appArn: str = None, name: str = None, configuration: Dict = None, executionConfiguration: Dict = None) -> Dict:
        pass

    def stop_job(self, arn: str) -> Dict:
        pass

    def stop_remote_access_session(self, arn: str) -> Dict:
        pass

    def stop_run(self, arn: str) -> Dict:
        pass

    def update_device_instance(self, arn: str, profileArn: str = None, labels: List = None) -> Dict:
        pass

    def update_device_pool(self, arn: str, name: str = None, description: str = None, rules: List = None) -> Dict:
        pass

    def update_instance_profile(self, arn: str, name: str = None, description: str = None, packageCleanup: bool = None, excludeAppPackagesFromCleanup: List = None, rebootAfterUse: bool = None) -> Dict:
        pass

    def update_network_profile(self, arn: str, name: str = None, description: str = None, type: str = None, uplinkBandwidthBits: int = None, downlinkBandwidthBits: int = None, uplinkDelayMs: int = None, downlinkDelayMs: int = None, uplinkJitterMs: int = None, downlinkJitterMs: int = None, uplinkLossPercent: int = None, downlinkLossPercent: int = None) -> Dict:
        pass

    def update_project(self, arn: str, name: str = None, defaultJobTimeoutMinutes: int = None) -> Dict:
        pass

    def update_upload(self, arn: str, name: str = None, contentType: str = None, editContent: bool = None) -> Dict:
        pass

    def update_vpce_configuration(self, arn: str, vpceConfigurationName: str = None, vpceServiceName: str = None, serviceDnsName: str = None, vpceConfigurationDescription: str = None) -> Dict:
        pass
