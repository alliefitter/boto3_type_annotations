from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class BatchPredictionAvailable(Waiter):
    def wait(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class DataSourceAvailable(Waiter):
    def wait(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class EvaluationAvailable(Waiter):
    def wait(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class MLModelAvailable(Waiter):
    def wait(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
