from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class BatchPredictionAvailable(Waiter):
    def wait(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeBatchPredictions>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              FilterVariable=\'CreatedAt\'|\'LastUpdatedAt\'|\'Status\'|\'Name\'|\'IAMUser\'|\'MLModelId\'|\'DataSourceId\'|\'DataURI\',
              EQ=\'string\',
              GT=\'string\',
              LT=\'string\',
              GE=\'string\',
              LE=\'string\',
              NE=\'string\',
              Prefix=\'string\',
              SortOrder=\'asc\'|\'dsc\',
              NextToken=\'string\',
              Limit=123,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type FilterVariable: string
        :param FilterVariable: 
        
          Use one of the following variables to filter a list of ``BatchPrediction`` :
        
          * ``CreatedAt`` - Sets the search criteria to the ``BatchPrediction`` creation date.
           
          * ``Status`` - Sets the search criteria to the ``BatchPrediction`` status.
           
          * ``Name`` - Sets the search criteria to the contents of the ``BatchPrediction`` ****  ``Name`` .
           
          * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``BatchPrediction`` creation.
           
          * ``MLModelId`` - Sets the search criteria to the ``MLModel`` used in the ``BatchPrediction`` .
           
          * ``DataSourceId`` - Sets the search criteria to the ``DataSource`` used in the ``BatchPrediction`` .
           
          * ``DataURI`` - Sets the search criteria to the data file(s) used in the ``BatchPrediction`` . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
           
        :type EQ: string
        :param EQ: 
        
          The equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .
        
        :type GT: string
        :param GT: 
        
          The greater than operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .
        
        :type LT: string
        :param LT: 
        
          The less than operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .
        
        :type GE: string
        :param GE: 
        
          The greater than or equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 
        
        :type LE: string
        :param LE: 
        
          The less than or equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .
        
        :type NE: string
        :param NE: 
        
          The not equal to operator. The ``BatchPrediction`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .
        
        :type Prefix: string
        :param Prefix: 
        
          A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .
        
          For example, a ``Batch Prediction`` operation could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``BatchPrediction`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 
        
          * 2014-09
           
          * 2014-09-09
           
          * 2014-09-09-Holiday
           
        :type SortOrder: string
        :param SortOrder: 
        
          A two-value parameter that determines the sequence of the resulting list of ``MLModel`` s.
        
          * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
           
          * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
           
          Results are sorted by ``FilterVariable`` .
        
        :type NextToken: string
        :param NextToken: 
        
          An ID of the page in the paginated results.
        
        :type Limit: integer
        :param Limit: 
        
          The number of pages of information to include in the result. The range of acceptable values is ``1`` through ``100`` . The default value is ``100`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass


class DataSourceAvailable(Waiter):
    def wait(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeDataSources>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              FilterVariable=\'CreatedAt\'|\'LastUpdatedAt\'|\'Status\'|\'Name\'|\'DataLocationS3\'|\'IAMUser\',
              EQ=\'string\',
              GT=\'string\',
              LT=\'string\',
              GE=\'string\',
              LE=\'string\',
              NE=\'string\',
              Prefix=\'string\',
              SortOrder=\'asc\'|\'dsc\',
              NextToken=\'string\',
              Limit=123,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type FilterVariable: string
        :param FilterVariable: 
        
          Use one of the following variables to filter a list of ``DataSource`` :
        
          * ``CreatedAt`` - Sets the search criteria to ``DataSource`` creation dates.
           
          * ``Status`` - Sets the search criteria to ``DataSource`` statuses.
           
          * ``Name`` - Sets the search criteria to the contents of ``DataSource``  ****  ``Name`` .
           
          * ``DataUri`` - Sets the search criteria to the URI of data files used to create the ``DataSource`` . The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
           
          * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``DataSource`` creation.
           
        :type EQ: string
        :param EQ: 
        
          The equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .
        
        :type GT: string
        :param GT: 
        
          The greater than operator. The ``DataSource`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .
        
        :type LT: string
        :param LT: 
        
          The less than operator. The ``DataSource`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .
        
        :type GE: string
        :param GE: 
        
          The greater than or equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 
        
        :type LE: string
        :param LE: 
        
          The less than or equal to operator. The ``DataSource`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .
        
        :type NE: string
        :param NE: 
        
          The not equal to operator. The ``DataSource`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .
        
        :type Prefix: string
        :param Prefix: 
        
          A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .
        
          For example, a ``DataSource`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``DataSource`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 
        
          * 2014-09
           
          * 2014-09-09
           
          * 2014-09-09-Holiday
           
        :type SortOrder: string
        :param SortOrder: 
        
          A two-value parameter that determines the sequence of the resulting list of ``DataSource`` .
        
          * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
           
          * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
           
          Results are sorted by ``FilterVariable`` .
        
        :type NextToken: string
        :param NextToken: 
        
          The ID of the page in the paginated results.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of ``DataSource`` to include in the result.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass


class EvaluationAvailable(Waiter):
    def wait(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeEvaluations>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              FilterVariable=\'CreatedAt\'|\'LastUpdatedAt\'|\'Status\'|\'Name\'|\'IAMUser\'|\'MLModelId\'|\'DataSourceId\'|\'DataURI\',
              EQ=\'string\',
              GT=\'string\',
              LT=\'string\',
              GE=\'string\',
              LE=\'string\',
              NE=\'string\',
              Prefix=\'string\',
              SortOrder=\'asc\'|\'dsc\',
              NextToken=\'string\',
              Limit=123,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type FilterVariable: string
        :param FilterVariable: 
        
          Use one of the following variable to filter a list of ``Evaluation`` objects:
        
          * ``CreatedAt`` - Sets the search criteria to the ``Evaluation`` creation date.
           
          * ``Status`` - Sets the search criteria to the ``Evaluation`` status.
           
          * ``Name`` - Sets the search criteria to the contents of ``Evaluation``  ****  ``Name`` .
           
          * ``IAMUser`` - Sets the search criteria to the user account that invoked an ``Evaluation`` .
           
          * ``MLModelId`` - Sets the search criteria to the ``MLModel`` that was evaluated.
           
          * ``DataSourceId`` - Sets the search criteria to the ``DataSource`` used in ``Evaluation`` .
           
          * ``DataUri`` - Sets the search criteria to the data file(s) used in ``Evaluation`` . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
           
        :type EQ: string
        :param EQ: 
        
          The equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .
        
        :type GT: string
        :param GT: 
        
          The greater than operator. The ``Evaluation`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .
        
        :type LT: string
        :param LT: 
        
          The less than operator. The ``Evaluation`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .
        
        :type GE: string
        :param GE: 
        
          The greater than or equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 
        
        :type LE: string
        :param LE: 
        
          The less than or equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .
        
        :type NE: string
        :param NE: 
        
          The not equal to operator. The ``Evaluation`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .
        
        :type Prefix: string
        :param Prefix: 
        
          A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .
        
          For example, an ``Evaluation`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``Evaluation`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 
        
          * 2014-09
           
          * 2014-09-09
           
          * 2014-09-09-Holiday
           
        :type SortOrder: string
        :param SortOrder: 
        
          A two-value parameter that determines the sequence of the resulting list of ``Evaluation`` .
        
          * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
           
          * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
           
          Results are sorted by ``FilterVariable`` .
        
        :type NextToken: string
        :param NextToken: 
        
          The ID of the page in the paginated results.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of ``Evaluation`` to include in the result.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass


class MLModelAvailable(Waiter):
    def wait(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, NextToken: str = None, Limit: int = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeMLModels>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              FilterVariable=\'CreatedAt\'|\'LastUpdatedAt\'|\'Status\'|\'Name\'|\'IAMUser\'|\'TrainingDataSourceId\'|\'RealtimeEndpointStatus\'|\'MLModelType\'|\'Algorithm\'|\'TrainingDataURI\',
              EQ=\'string\',
              GT=\'string\',
              LT=\'string\',
              GE=\'string\',
              LE=\'string\',
              NE=\'string\',
              Prefix=\'string\',
              SortOrder=\'asc\'|\'dsc\',
              NextToken=\'string\',
              Limit=123,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type FilterVariable: string
        :param FilterVariable: 
        
          Use one of the following variables to filter a list of ``MLModel`` :
        
          * ``CreatedAt`` - Sets the search criteria to ``MLModel`` creation date.
           
          * ``Status`` - Sets the search criteria to ``MLModel`` status.
           
          * ``Name`` - Sets the search criteria to the contents of ``MLModel`` ****  ``Name`` .
           
          * ``IAMUser`` - Sets the search criteria to the user account that invoked the ``MLModel`` creation.
           
          * ``TrainingDataSourceId`` - Sets the search criteria to the ``DataSource`` used to train one or more ``MLModel`` .
           
          * ``RealtimeEndpointStatus`` - Sets the search criteria to the ``MLModel`` real-time endpoint status.
           
          * ``MLModelType`` - Sets the search criteria to ``MLModel`` type: binary, regression, or multi-class.
           
          * ``Algorithm`` - Sets the search criteria to the algorithm that the ``MLModel`` uses.
           
          * ``TrainingDataURI`` - Sets the search criteria to the data file(s) used in training a ``MLModel`` . The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
           
        :type EQ: string
        :param EQ: 
        
          The equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that exactly match the value specified with ``EQ`` .
        
        :type GT: string
        :param GT: 
        
          The greater than operator. The ``MLModel`` results will have ``FilterVariable`` values that are greater than the value specified with ``GT`` .
        
        :type LT: string
        :param LT: 
        
          The less than operator. The ``MLModel`` results will have ``FilterVariable`` values that are less than the value specified with ``LT`` .
        
        :type GE: string
        :param GE: 
        
          The greater than or equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that are greater than or equal to the value specified with ``GE`` . 
        
        :type LE: string
        :param LE: 
        
          The less than or equal to operator. The ``MLModel`` results will have ``FilterVariable`` values that are less than or equal to the value specified with ``LE`` .
        
        :type NE: string
        :param NE: 
        
          The not equal to operator. The ``MLModel`` results will have ``FilterVariable`` values not equal to the value specified with ``NE`` .
        
        :type Prefix: string
        :param Prefix: 
        
          A string that is found at the beginning of a variable, such as ``Name`` or ``Id`` .
        
          For example, an ``MLModel`` could have the ``Name``  ``2014-09-09-HolidayGiftMailer`` . To search for this ``MLModel`` , select ``Name`` for the ``FilterVariable`` and any of the following strings for the ``Prefix`` : 
        
          * 2014-09
           
          * 2014-09-09
           
          * 2014-09-09-Holiday
           
        :type SortOrder: string
        :param SortOrder: 
        
          A two-value parameter that determines the sequence of the resulting list of ``MLModel`` .
        
          * ``asc`` - Arranges the list in ascending order (A-Z, 0-9).
           
          * ``dsc`` - Arranges the list in descending order (Z-A, 9-0).
           
          Results are sorted by ``FilterVariable`` .
        
        :type NextToken: string
        :param NextToken: 
        
          The ID of the page in the paginated results.
        
        :type Limit: integer
        :param Limit: 
        
          The number of pages of information to include in the result. The range of acceptable values is ``1`` through ``100`` . The default value is ``100`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass
