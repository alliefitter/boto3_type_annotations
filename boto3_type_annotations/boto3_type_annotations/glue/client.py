from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_create_partition(self, DatabaseName: str, TableName: str, PartitionInputList: List, CatalogId: str = None) -> Dict:
        pass

    def batch_delete_connection(self, ConnectionNameList: List, CatalogId: str = None) -> Dict:
        pass

    def batch_delete_partition(self, DatabaseName: str, TableName: str, PartitionsToDelete: List, CatalogId: str = None) -> Dict:
        pass

    def batch_delete_table(self, DatabaseName: str, TablesToDelete: List, CatalogId: str = None) -> Dict:
        pass

    def batch_delete_table_version(self, DatabaseName: str, TableName: str, VersionIds: List, CatalogId: str = None) -> Dict:
        pass

    def batch_get_partition(self, DatabaseName: str, TableName: str, PartitionsToGet: List, CatalogId: str = None) -> Dict:
        pass

    def batch_stop_job_run(self, JobName: str, JobRunIds: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_classifier(self, GrokClassifier: Dict = None, XMLClassifier: Dict = None, JsonClassifier: Dict = None) -> Dict:
        pass

    def create_connection(self, ConnectionInput: Dict, CatalogId: str = None) -> Dict:
        pass

    def create_crawler(self, Name: str, Role: str, DatabaseName: str, Targets: Dict, Description: str = None, Schedule: str = None, Classifiers: List = None, TablePrefix: str = None, SchemaChangePolicy: Dict = None, Configuration: str = None, CrawlerSecurityConfiguration: str = None) -> Dict:
        pass

    def create_database(self, DatabaseInput: Dict, CatalogId: str = None) -> Dict:
        pass

    def create_dev_endpoint(self, EndpointName: str, RoleArn: str, SecurityGroupIds: List = None, SubnetId: str = None, PublicKey: str = None, PublicKeys: List = None, NumberOfNodes: int = None, ExtraPythonLibsS3Path: str = None, ExtraJarsS3Path: str = None, SecurityConfiguration: str = None) -> Dict:
        pass

    def create_job(self, Name: str, Role: str, Command: Dict, Description: str = None, LogUri: str = None, ExecutionProperty: Dict = None, DefaultArguments: Dict = None, Connections: Dict = None, MaxRetries: int = None, AllocatedCapacity: int = None, Timeout: int = None, NotificationProperty: Dict = None, SecurityConfiguration: str = None) -> Dict:
        pass

    def create_partition(self, DatabaseName: str, TableName: str, PartitionInput: Dict, CatalogId: str = None) -> Dict:
        pass

    def create_script(self, DagNodes: List = None, DagEdges: List = None, Language: str = None) -> Dict:
        pass

    def create_security_configuration(self, Name: str, EncryptionConfiguration: Dict) -> Dict:
        pass

    def create_table(self, DatabaseName: str, TableInput: Dict, CatalogId: str = None) -> Dict:
        pass

    def create_trigger(self, Name: str, Type: str, Actions: List, Schedule: str = None, Predicate: Dict = None, Description: str = None, StartOnCreation: bool = None) -> Dict:
        pass

    def create_user_defined_function(self, DatabaseName: str, FunctionInput: Dict, CatalogId: str = None) -> Dict:
        pass

    def delete_classifier(self, Name: str) -> Dict:
        pass

    def delete_connection(self, ConnectionName: str, CatalogId: str = None) -> Dict:
        pass

    def delete_crawler(self, Name: str) -> Dict:
        pass

    def delete_database(self, Name: str, CatalogId: str = None) -> Dict:
        pass

    def delete_dev_endpoint(self, EndpointName: str) -> Dict:
        pass

    def delete_job(self, JobName: str) -> Dict:
        pass

    def delete_partition(self, DatabaseName: str, TableName: str, PartitionValues: List, CatalogId: str = None) -> Dict:
        pass

    def delete_resource_policy(self, PolicyHashCondition: str = None) -> Dict:
        pass

    def delete_security_configuration(self, Name: str) -> Dict:
        pass

    def delete_table(self, DatabaseName: str, Name: str, CatalogId: str = None) -> Dict:
        pass

    def delete_table_version(self, DatabaseName: str, TableName: str, VersionId: str, CatalogId: str = None) -> Dict:
        pass

    def delete_trigger(self, Name: str) -> Dict:
        pass

    def delete_user_defined_function(self, DatabaseName: str, FunctionName: str, CatalogId: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_catalog_import_status(self, CatalogId: str = None) -> Dict:
        pass

    def get_classifier(self, Name: str) -> Dict:
        pass

    def get_classifiers(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_connection(self, Name: str, CatalogId: str = None) -> Dict:
        pass

    def get_connections(self, CatalogId: str = None, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_crawler(self, Name: str) -> Dict:
        pass

    def get_crawler_metrics(self, CrawlerNameList: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_crawlers(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_data_catalog_encryption_settings(self, CatalogId: str = None) -> Dict:
        pass

    def get_database(self, Name: str, CatalogId: str = None) -> Dict:
        pass

    def get_databases(self, CatalogId: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_dataflow_graph(self, PythonScript: str = None) -> Dict:
        pass

    def get_dev_endpoint(self, EndpointName: str) -> Dict:
        pass

    def get_dev_endpoints(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_job(self, JobName: str) -> Dict:
        pass

    def get_job_run(self, JobName: str, RunId: str, PredecessorsIncluded: bool = None) -> Dict:
        pass

    def get_job_runs(self, JobName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_jobs(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_mapping(self, Source: Dict, Sinks: List = None, Location: Dict = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_partition(self, DatabaseName: str, TableName: str, PartitionValues: List, CatalogId: str = None) -> Dict:
        pass

    def get_partitions(self, DatabaseName: str, TableName: str, CatalogId: str = None, Expression: str = None, NextToken: str = None, Segment: Dict = None, MaxResults: int = None) -> Dict:
        pass

    def get_plan(self, Mapping: List, Source: Dict, Sinks: List = None, Location: Dict = None, Language: str = None) -> Dict:
        pass

    def get_resource_policy(self) -> Dict:
        pass

    def get_security_configuration(self, Name: str) -> Dict:
        pass

    def get_security_configurations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_table(self, DatabaseName: str, Name: str, CatalogId: str = None) -> Dict:
        pass

    def get_table_version(self, DatabaseName: str, TableName: str, CatalogId: str = None, VersionId: str = None) -> Dict:
        pass

    def get_table_versions(self, DatabaseName: str, TableName: str, CatalogId: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_tables(self, DatabaseName: str, CatalogId: str = None, Expression: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_trigger(self, Name: str) -> Dict:
        pass

    def get_triggers(self, NextToken: str = None, DependentJobName: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_user_defined_function(self, DatabaseName: str, FunctionName: str, CatalogId: str = None) -> Dict:
        pass

    def get_user_defined_functions(self, DatabaseName: str, Pattern: str, CatalogId: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_catalog_to_glue(self, CatalogId: str = None) -> Dict:
        pass

    def put_data_catalog_encryption_settings(self, DataCatalogEncryptionSettings: Dict, CatalogId: str = None) -> Dict:
        pass

    def put_resource_policy(self, PolicyInJson: str, PolicyHashCondition: str = None, PolicyExistsCondition: str = None) -> Dict:
        pass

    def reset_job_bookmark(self, JobName: str) -> Dict:
        pass

    def start_crawler(self, Name: str) -> Dict:
        pass

    def start_crawler_schedule(self, CrawlerName: str) -> Dict:
        pass

    def start_job_run(self, JobName: str, JobRunId: str = None, Arguments: Dict = None, AllocatedCapacity: int = None, Timeout: int = None, NotificationProperty: Dict = None, SecurityConfiguration: str = None) -> Dict:
        pass

    def start_trigger(self, Name: str) -> Dict:
        pass

    def stop_crawler(self, Name: str) -> Dict:
        pass

    def stop_crawler_schedule(self, CrawlerName: str) -> Dict:
        pass

    def stop_trigger(self, Name: str) -> Dict:
        pass

    def update_classifier(self, GrokClassifier: Dict = None, XMLClassifier: Dict = None, JsonClassifier: Dict = None) -> Dict:
        pass

    def update_connection(self, Name: str, ConnectionInput: Dict, CatalogId: str = None) -> Dict:
        pass

    def update_crawler(self, Name: str, Role: str = None, DatabaseName: str = None, Description: str = None, Targets: Dict = None, Schedule: str = None, Classifiers: List = None, TablePrefix: str = None, SchemaChangePolicy: Dict = None, Configuration: str = None, CrawlerSecurityConfiguration: str = None) -> Dict:
        pass

    def update_crawler_schedule(self, CrawlerName: str, Schedule: str = None) -> Dict:
        pass

    def update_database(self, Name: str, DatabaseInput: Dict, CatalogId: str = None) -> Dict:
        pass

    def update_dev_endpoint(self, EndpointName: str, PublicKey: str = None, AddPublicKeys: List = None, DeletePublicKeys: List = None, CustomLibraries: Dict = None, UpdateEtlLibraries: bool = None) -> Dict:
        pass

    def update_job(self, JobName: str, JobUpdate: Dict) -> Dict:
        pass

    def update_partition(self, DatabaseName: str, TableName: str, PartitionValueList: List, PartitionInput: Dict, CatalogId: str = None) -> Dict:
        pass

    def update_table(self, DatabaseName: str, TableInput: Dict, CatalogId: str = None, SkipArchive: bool = None) -> Dict:
        pass

    def update_trigger(self, Name: str, TriggerUpdate: Dict) -> Dict:
        pass

    def update_user_defined_function(self, DatabaseName: str, FunctionName: str, FunctionInput: Dict, CatalogId: str = None) -> Dict:
        pass
