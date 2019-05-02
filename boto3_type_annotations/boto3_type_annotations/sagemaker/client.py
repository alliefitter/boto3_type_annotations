from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def add_tags(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_algorithm(self, AlgorithmName: str, TrainingSpecification: Dict, AlgorithmDescription: str = None, InferenceSpecification: Dict = None, ValidationSpecification: Dict = None, CertifyForMarketplace: bool = None) -> Dict:
        pass

    def create_code_repository(self, CodeRepositoryName: str, GitConfig: Dict) -> Dict:
        pass

    def create_compilation_job(self, CompilationJobName: str, RoleArn: str, InputConfig: Dict, OutputConfig: Dict, StoppingCondition: Dict) -> Dict:
        pass

    def create_endpoint(self, EndpointName: str, EndpointConfigName: str, Tags: List = None) -> Dict:
        pass

    def create_endpoint_config(self, EndpointConfigName: str, ProductionVariants: List, Tags: List = None, KmsKeyId: str = None) -> Dict:
        pass

    def create_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str, HyperParameterTuningJobConfig: Dict, TrainingJobDefinition: Dict, WarmStartConfig: Dict = None, Tags: List = None) -> Dict:
        pass

    def create_labeling_job(self, LabelingJobName: str, LabelAttributeName: str, InputConfig: Dict, OutputConfig: Dict, RoleArn: str, HumanTaskConfig: Dict, LabelCategoryConfigS3Uri: str = None, StoppingConditions: Dict = None, LabelingJobAlgorithmsConfig: Dict = None, Tags: List = None) -> Dict:
        pass

    def create_model(self, ModelName: str, ExecutionRoleArn: str, PrimaryContainer: Dict = None, Containers: List = None, Tags: List = None, VpcConfig: Dict = None, EnableNetworkIsolation: bool = None) -> Dict:
        pass

    def create_model_package(self, ModelPackageName: str, ModelPackageDescription: str = None, InferenceSpecification: Dict = None, ValidationSpecification: Dict = None, SourceAlgorithmSpecification: Dict = None, CertifyForMarketplace: bool = None) -> Dict:
        pass

    def create_notebook_instance(self, NotebookInstanceName: str, InstanceType: str, RoleArn: str, SubnetId: str = None, SecurityGroupIds: List = None, KmsKeyId: str = None, Tags: List = None, LifecycleConfigName: str = None, DirectInternetAccess: str = None, VolumeSizeInGB: int = None, AcceleratorTypes: List = None, DefaultCodeRepository: str = None, AdditionalCodeRepositories: List = None, RootAccess: str = None) -> Dict:
        pass

    def create_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str, OnCreate: List = None, OnStart: List = None) -> Dict:
        pass

    def create_presigned_notebook_instance_url(self, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None) -> Dict:
        pass

    def create_training_job(self, TrainingJobName: str, AlgorithmSpecification: Dict, RoleArn: str, OutputDataConfig: Dict, ResourceConfig: Dict, StoppingCondition: Dict, HyperParameters: Dict = None, InputDataConfig: List = None, VpcConfig: Dict = None, Tags: List = None, EnableNetworkIsolation: bool = None, EnableInterContainerTrafficEncryption: bool = None) -> Dict:
        pass

    def create_transform_job(self, TransformJobName: str, ModelName: str, TransformInput: Dict, TransformOutput: Dict, TransformResources: Dict, MaxConcurrentTransforms: int = None, MaxPayloadInMB: int = None, BatchStrategy: str = None, Environment: Dict = None, Tags: List = None) -> Dict:
        pass

    def create_workteam(self, WorkteamName: str, MemberDefinitions: List, Description: str, Tags: List = None) -> Dict:
        pass

    def delete_algorithm(self, AlgorithmName: str):
        pass

    def delete_code_repository(self, CodeRepositoryName: str):
        pass

    def delete_endpoint(self, EndpointName: str):
        pass

    def delete_endpoint_config(self, EndpointConfigName: str):
        pass

    def delete_model(self, ModelName: str):
        pass

    def delete_model_package(self, ModelPackageName: str):
        pass

    def delete_notebook_instance(self, NotebookInstanceName: str):
        pass

    def delete_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str):
        pass

    def delete_tags(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass

    def delete_workteam(self, WorkteamName: str) -> Dict:
        pass

    def describe_algorithm(self, AlgorithmName: str) -> Dict:
        pass

    def describe_code_repository(self, CodeRepositoryName: str) -> Dict:
        pass

    def describe_compilation_job(self, CompilationJobName: str) -> Dict:
        pass

    def describe_endpoint(self, EndpointName: str) -> Dict:
        pass

    def describe_endpoint_config(self, EndpointConfigName: str) -> Dict:
        pass

    def describe_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> Dict:
        pass

    def describe_labeling_job(self, LabelingJobName: str) -> Dict:
        pass

    def describe_model(self, ModelName: str) -> Dict:
        pass

    def describe_model_package(self, ModelPackageName: str) -> Dict:
        pass

    def describe_notebook_instance(self, NotebookInstanceName: str) -> Dict:
        pass

    def describe_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str) -> Dict:
        pass

    def describe_subscribed_workteam(self, WorkteamArn: str) -> Dict:
        pass

    def describe_training_job(self, TrainingJobName: str) -> Dict:
        pass

    def describe_transform_job(self, TransformJobName: str) -> Dict:
        pass

    def describe_workteam(self, WorkteamName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_search_suggestions(self, Resource: str, SuggestionQuery: Dict = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_algorithms(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, MaxResults: int = None, NameContains: str = None, NextToken: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_code_repositories(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, MaxResults: int = None, NameContains: str = None, NextToken: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_compilation_jobs(self, NextToken: str = None, MaxResults: int = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_endpoint_configs(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None) -> Dict:
        pass

    def list_endpoints(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None) -> Dict:
        pass

    def list_hyper_parameter_tuning_jobs(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, StatusEquals: str = None) -> Dict:
        pass

    def list_labeling_jobs(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, MaxResults: int = None, NextToken: str = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, StatusEquals: str = None) -> Dict:
        pass

    def list_labeling_jobs_for_workteam(self, WorkteamArn: str, MaxResults: int = None, NextToken: str = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, JobReferenceCodeContains: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_model_packages(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, MaxResults: int = None, NameContains: str = None, NextToken: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_models(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None) -> Dict:
        pass

    def list_notebook_instance_lifecycle_configs(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None) -> Dict:
        pass

    def list_notebook_instances(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, NotebookInstanceLifecycleConfigNameContains: str = None, DefaultCodeRepositoryContains: str = None, AdditionalCodeRepositoryEquals: str = None) -> Dict:
        pass

    def list_subscribed_workteams(self, NameContains: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_tags(self, ResourceArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_training_jobs(self, NextToken: str = None, MaxResults: int = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_training_jobs_for_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str, NextToken: str = None, MaxResults: int = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        pass

    def list_transform_jobs(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_workteams(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def render_ui_template(self, UiTemplate: Dict, Task: Dict, RoleArn: str) -> Dict:
        pass

    def search(self, Resource: str, SearchExpression: Dict = None, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def start_notebook_instance(self, NotebookInstanceName: str):
        pass

    def stop_compilation_job(self, CompilationJobName: str):
        pass

    def stop_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str):
        pass

    def stop_labeling_job(self, LabelingJobName: str):
        pass

    def stop_notebook_instance(self, NotebookInstanceName: str):
        pass

    def stop_training_job(self, TrainingJobName: str):
        pass

    def stop_transform_job(self, TransformJobName: str):
        pass

    def update_code_repository(self, CodeRepositoryName: str, GitConfig: Dict = None) -> Dict:
        pass

    def update_endpoint(self, EndpointName: str, EndpointConfigName: str) -> Dict:
        pass

    def update_endpoint_weights_and_capacities(self, EndpointName: str, DesiredWeightsAndCapacities: List) -> Dict:
        pass

    def update_notebook_instance(self, NotebookInstanceName: str, InstanceType: str = None, RoleArn: str = None, LifecycleConfigName: str = None, DisassociateLifecycleConfig: bool = None, VolumeSizeInGB: int = None, DefaultCodeRepository: str = None, AdditionalCodeRepositories: List = None, AcceleratorTypes: List = None, DisassociateAcceleratorTypes: bool = None, DisassociateDefaultCodeRepository: bool = None, DisassociateAdditionalCodeRepositories: bool = None, RootAccess: str = None) -> Dict:
        pass

    def update_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str, OnCreate: List = None, OnStart: List = None) -> Dict:
        pass

    def update_workteam(self, WorkteamName: str, MemberDefinitions: List = None, Description: str = None) -> Dict:
        pass
