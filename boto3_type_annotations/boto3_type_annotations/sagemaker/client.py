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
    def add_tags(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_endpoint(self, EndpointName: str, EndpointConfigName: str, Tags: List = None) -> Dict:
        pass

    def create_endpoint_config(self, EndpointConfigName: str, ProductionVariants: List, Tags: List = None, KmsKeyId: str = None) -> Dict:
        pass

    def create_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str, HyperParameterTuningJobConfig: Dict, TrainingJobDefinition: Dict, Tags: List = None) -> Dict:
        pass

    def create_model(self, ModelName: str, PrimaryContainer: Dict, ExecutionRoleArn: str, Tags: List = None, VpcConfig: Dict = None) -> Dict:
        pass

    def create_notebook_instance(self, NotebookInstanceName: str, InstanceType: str, RoleArn: str, SubnetId: str = None, SecurityGroupIds: List = None, KmsKeyId: str = None, Tags: List = None, LifecycleConfigName: str = None, DirectInternetAccess: str = None, VolumeSizeInGB: int = None) -> Dict:
        pass

    def create_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str, OnCreate: List = None, OnStart: List = None) -> Dict:
        pass

    def create_presigned_notebook_instance_url(self, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None) -> Dict:
        pass

    def create_training_job(self, TrainingJobName: str, AlgorithmSpecification: Dict, RoleArn: str, OutputDataConfig: Dict, ResourceConfig: Dict, StoppingCondition: Dict, HyperParameters: Dict = None, InputDataConfig: List = None, VpcConfig: Dict = None, Tags: List = None) -> Dict:
        pass

    def create_transform_job(self, TransformJobName: str, ModelName: str, TransformInput: Dict, TransformOutput: Dict, TransformResources: Dict, MaxConcurrentTransforms: int = None, MaxPayloadInMB: int = None, BatchStrategy: str = None, Environment: Dict = None, Tags: List = None) -> Dict:
        pass

    def delete_endpoint(self, EndpointName: str) -> NoReturn:
        pass

    def delete_endpoint_config(self, EndpointConfigName: str) -> NoReturn:
        pass

    def delete_model(self, ModelName: str) -> NoReturn:
        pass

    def delete_notebook_instance(self, NotebookInstanceName: str) -> NoReturn:
        pass

    def delete_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str) -> NoReturn:
        pass

    def delete_tags(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass

    def describe_endpoint(self, EndpointName: str) -> Dict:
        pass

    def describe_endpoint_config(self, EndpointConfigName: str) -> Dict:
        pass

    def describe_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> Dict:
        pass

    def describe_model(self, ModelName: str) -> Dict:
        pass

    def describe_notebook_instance(self, NotebookInstanceName: str) -> Dict:
        pass

    def describe_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str) -> Dict:
        pass

    def describe_training_job(self, TrainingJobName: str) -> Dict:
        pass

    def describe_transform_job(self, TransformJobName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_endpoint_configs(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None) -> Dict:
        pass

    def list_endpoints(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None) -> Dict:
        pass

    def list_hyper_parameter_tuning_jobs(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, StatusEquals: str = None) -> Dict:
        pass

    def list_models(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None) -> Dict:
        pass

    def list_notebook_instance_lifecycle_configs(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None) -> Dict:
        pass

    def list_notebook_instances(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, NotebookInstanceLifecycleConfigNameContains: str = None) -> Dict:
        pass

    def list_tags(self, ResourceArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_training_jobs(self, NextToken: str = None, MaxResults: int = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_training_jobs_for_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str, NextToken: str = None, MaxResults: int = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_transform_jobs(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def start_notebook_instance(self, NotebookInstanceName: str) -> NoReturn:
        pass

    def stop_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> NoReturn:
        pass

    def stop_notebook_instance(self, NotebookInstanceName: str) -> NoReturn:
        pass

    def stop_training_job(self, TrainingJobName: str) -> NoReturn:
        pass

    def stop_transform_job(self, TransformJobName: str) -> NoReturn:
        pass

    def update_endpoint(self, EndpointName: str, EndpointConfigName: str) -> Dict:
        pass

    def update_endpoint_weights_and_capacities(self, EndpointName: str, DesiredWeightsAndCapacities: List) -> Dict:
        pass

    def update_notebook_instance(self, NotebookInstanceName: str, InstanceType: str = None, RoleArn: str = None, LifecycleConfigName: str = None, DisassociateLifecycleConfig: bool = None, VolumeSizeInGB: int = None) -> Dict:
        pass

    def update_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str, OnCreate: List = None, OnStart: List = None) -> Dict:
        pass
