from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def acknowledge_job(self, jobId: str, nonce: str) -> Dict:
        pass

    def acknowledge_third_party_job(self, jobId: str, nonce: str, clientToken: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_custom_action_type(self, category: str, provider: str, version: str, inputArtifactDetails: Dict, outputArtifactDetails: Dict, settings: Dict = None, configurationProperties: List = None) -> Dict:
        pass

    def create_pipeline(self, pipeline: Dict) -> Dict:
        pass

    def delete_custom_action_type(self, category: str, provider: str, version: str):
        pass

    def delete_pipeline(self, name: str):
        pass

    def delete_webhook(self, name: str) -> Dict:
        pass

    def deregister_webhook_with_third_party(self, webhookName: str = None) -> Dict:
        pass

    def disable_stage_transition(self, pipelineName: str, stageName: str, transitionType: str, reason: str):
        pass

    def enable_stage_transition(self, pipelineName: str, stageName: str, transitionType: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_job_details(self, jobId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_pipeline(self, name: str, version: int = None) -> Dict:
        pass

    def get_pipeline_execution(self, pipelineName: str, pipelineExecutionId: str) -> Dict:
        pass

    def get_pipeline_state(self, name: str) -> Dict:
        pass

    def get_third_party_job_details(self, jobId: str, clientToken: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_action_types(self, actionOwnerFilter: str = None, nextToken: str = None) -> Dict:
        pass

    def list_pipeline_executions(self, pipelineName: str, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_pipelines(self, nextToken: str = None) -> Dict:
        pass

    def list_webhooks(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def poll_for_jobs(self, actionTypeId: Dict, maxBatchSize: int = None, queryParam: Dict = None) -> Dict:
        pass

    def poll_for_third_party_jobs(self, actionTypeId: Dict, maxBatchSize: int = None) -> Dict:
        pass

    def put_action_revision(self, pipelineName: str, stageName: str, actionName: str, actionRevision: Dict) -> Dict:
        pass

    def put_approval_result(self, pipelineName: str, stageName: str, actionName: str, result: Dict, token: str) -> Dict:
        pass

    def put_job_failure_result(self, jobId: str, failureDetails: Dict):
        pass

    def put_job_success_result(self, jobId: str, currentRevision: Dict = None, continuationToken: str = None, executionDetails: Dict = None):
        pass

    def put_third_party_job_failure_result(self, jobId: str, clientToken: str, failureDetails: Dict):
        pass

    def put_third_party_job_success_result(self, jobId: str, clientToken: str, currentRevision: Dict = None, continuationToken: str = None, executionDetails: Dict = None):
        pass

    def put_webhook(self, webhook: Dict) -> Dict:
        pass

    def register_webhook_with_third_party(self, webhookName: str = None) -> Dict:
        pass

    def retry_stage_execution(self, pipelineName: str, stageName: str, pipelineExecutionId: str, retryMode: str) -> Dict:
        pass

    def start_pipeline_execution(self, name: str, clientRequestToken: str = None) -> Dict:
        pass

    def update_pipeline(self, pipeline: Dict) -> Dict:
        pass
