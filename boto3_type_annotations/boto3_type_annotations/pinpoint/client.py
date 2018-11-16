from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_app(self, CreateApplicationRequest: Dict) -> Dict:
        pass

    def create_campaign(self, ApplicationId: str, WriteCampaignRequest: Dict) -> Dict:
        pass

    def create_export_job(self, ApplicationId: str, ExportJobRequest: Dict) -> Dict:
        pass

    def create_import_job(self, ApplicationId: str, ImportJobRequest: Dict) -> Dict:
        pass

    def create_segment(self, ApplicationId: str, WriteSegmentRequest: Dict) -> Dict:
        pass

    def delete_adm_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_apns_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_apns_sandbox_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_apns_voip_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_apns_voip_sandbox_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_app(self, ApplicationId: str) -> Dict:
        pass

    def delete_baidu_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_campaign(self, ApplicationId: str, CampaignId: str) -> Dict:
        pass

    def delete_email_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_endpoint(self, ApplicationId: str, EndpointId: str) -> Dict:
        pass

    def delete_event_stream(self, ApplicationId: str) -> Dict:
        pass

    def delete_gcm_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_segment(self, ApplicationId: str, SegmentId: str) -> Dict:
        pass

    def delete_sms_channel(self, ApplicationId: str) -> Dict:
        pass

    def delete_user_endpoints(self, ApplicationId: str, UserId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_adm_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_apns_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_apns_sandbox_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_apns_voip_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_apns_voip_sandbox_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_app(self, ApplicationId: str) -> Dict:
        pass

    def get_application_settings(self, ApplicationId: str) -> Dict:
        pass

    def get_apps(self, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_baidu_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_campaign(self, ApplicationId: str, CampaignId: str) -> Dict:
        pass

    def get_campaign_activities(self, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_campaign_version(self, ApplicationId: str, CampaignId: str, Version: str) -> Dict:
        pass

    def get_campaign_versions(self, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_campaigns(self, ApplicationId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_channels(self, ApplicationId: str) -> Dict:
        pass

    def get_email_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_endpoint(self, ApplicationId: str, EndpointId: str) -> Dict:
        pass

    def get_event_stream(self, ApplicationId: str) -> Dict:
        pass

    def get_export_job(self, ApplicationId: str, JobId: str) -> Dict:
        pass

    def get_export_jobs(self, ApplicationId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_gcm_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_import_job(self, ApplicationId: str, JobId: str) -> Dict:
        pass

    def get_import_jobs(self, ApplicationId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_segment(self, ApplicationId: str, SegmentId: str) -> Dict:
        pass

    def get_segment_export_jobs(self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_segment_import_jobs(self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_segment_version(self, ApplicationId: str, SegmentId: str, Version: str) -> Dict:
        pass

    def get_segment_versions(self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_segments(self, ApplicationId: str, PageSize: str = None, Token: str = None) -> Dict:
        pass

    def get_sms_channel(self, ApplicationId: str) -> Dict:
        pass

    def get_user_endpoints(self, ApplicationId: str, UserId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def phone_number_validate(self, NumberValidateRequest: Dict) -> Dict:
        pass

    def put_event_stream(self, ApplicationId: str, WriteEventStream: Dict) -> Dict:
        pass

    def put_events(self, ApplicationId: str, EventsRequest: Dict) -> Dict:
        pass

    def remove_attributes(self, ApplicationId: str, AttributeType: str, UpdateAttributesRequest: Dict) -> Dict:
        pass

    def send_messages(self, ApplicationId: str, MessageRequest: Dict) -> Dict:
        pass

    def send_users_messages(self, ApplicationId: str, SendUsersMessageRequest: Dict) -> Dict:
        pass

    def update_adm_channel(self, ADMChannelRequest: Dict, ApplicationId: str) -> Dict:
        pass

    def update_apns_channel(self, APNSChannelRequest: Dict, ApplicationId: str) -> Dict:
        pass

    def update_apns_sandbox_channel(self, APNSSandboxChannelRequest: Dict, ApplicationId: str) -> Dict:
        pass

    def update_apns_voip_channel(self, APNSVoipChannelRequest: Dict, ApplicationId: str) -> Dict:
        pass

    def update_apns_voip_sandbox_channel(self, APNSVoipSandboxChannelRequest: Dict, ApplicationId: str) -> Dict:
        pass

    def update_application_settings(self, ApplicationId: str, WriteApplicationSettingsRequest: Dict) -> Dict:
        pass

    def update_baidu_channel(self, ApplicationId: str, BaiduChannelRequest: Dict) -> Dict:
        pass

    def update_campaign(self, ApplicationId: str, CampaignId: str, WriteCampaignRequest: Dict) -> Dict:
        pass

    def update_email_channel(self, ApplicationId: str, EmailChannelRequest: Dict) -> Dict:
        pass

    def update_endpoint(self, ApplicationId: str, EndpointId: str, EndpointRequest: Dict) -> Dict:
        pass

    def update_endpoints_batch(self, ApplicationId: str, EndpointBatchRequest: Dict) -> Dict:
        pass

    def update_gcm_channel(self, ApplicationId: str, GCMChannelRequest: Dict) -> Dict:
        pass

    def update_segment(self, ApplicationId: str, SegmentId: str, WriteSegmentRequest: Dict) -> Dict:
        pass

    def update_sms_channel(self, ApplicationId: str, SMSChannelRequest: Dict) -> Dict:
        pass
