from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_tags(self, Tags: List, ResourceId: str, ResourceType: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_batch_prediction(self, BatchPredictionId: str, MLModelId: str, BatchPredictionDataSourceId: str, OutputUri: str, BatchPredictionName: str = None) -> Dict:
        pass

    def create_data_source_from_rds(self, DataSourceId: str, RDSData: Dict, RoleARN: str, DataSourceName: str = None, ComputeStatistics: bool = None) -> Dict:
        pass

    def create_data_source_from_redshift(self, DataSourceId: str, DataSpec: Dict, RoleARN: str, DataSourceName: str = None, ComputeStatistics: bool = None) -> Dict:
        pass

    def create_data_source_from_s3(self, DataSourceId: str, DataSpec: Dict, DataSourceName: str = None, ComputeStatistics: bool = None) -> Dict:
        pass

    def create_evaluation(self, EvaluationId: str, MLModelId: str, EvaluationDataSourceId: str, EvaluationName: str = None) -> Dict:
        pass

    def create_ml_model(self, MLModelId: str, MLModelType: str, TrainingDataSourceId: str, MLModelName: str = None, Parameters: Dict = None, Recipe: str = None, RecipeUri: str = None) -> Dict:
        pass

    def create_realtime_endpoint(self, MLModelId: str) -> Dict:
        pass

    def delete_batch_prediction(self, BatchPredictionId: str) -> Dict:
        pass

    def delete_data_source(self, DataSourceId: str) -> Dict:
        pass

    def delete_evaluation(self, EvaluationId: str) -> Dict:
        pass

    def delete_ml_model(self, MLModelId: str) -> Dict:
        pass

    def delete_realtime_endpoint(self, MLModelId: str) -> Dict:
        pass

    def delete_tags(self, TagKeys: List, ResourceId: str, ResourceType: str) -> Dict:
        pass

    def describe_batch_predictions(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def describe_data_sources(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def describe_evaluations(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def describe_ml_models(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def describe_tags(self, ResourceId: str, ResourceType: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_batch_prediction(self, BatchPredictionId: str) -> Dict:
        pass

    def get_data_source(self, DataSourceId: str, Verbose: bool = None) -> Dict:
        pass

    def get_evaluation(self, EvaluationId: str) -> Dict:
        pass

    def get_ml_model(self, MLModelId: str, Verbose: bool = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def predict(self, MLModelId: str, Record: Dict, PredictEndpoint: str) -> Dict:
        pass

    def update_batch_prediction(self, BatchPredictionId: str, BatchPredictionName: str) -> Dict:
        pass

    def update_data_source(self, DataSourceId: str, DataSourceName: str) -> Dict:
        pass

    def update_evaluation(self, EvaluationId: str, EvaluationName: str) -> Dict:
        pass

    def update_ml_model(self, MLModelId: str, MLModelName: str = None, ScoreThreshold: float = None) -> Dict:
        pass
