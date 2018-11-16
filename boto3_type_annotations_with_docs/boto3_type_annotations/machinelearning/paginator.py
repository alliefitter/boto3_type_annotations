from typing import Dict
from botocore.paginate import Paginator


class DescribeBatchPredictions(Paginator):
    def paginate(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeBatchPredictions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              FilterVariable=\'CreatedAt\'|\'LastUpdatedAt\'|\'Status\'|\'Name\'|\'IAMUser\'|\'MLModelId\'|\'DataSourceId\'|\'DataURI\',
              EQ=\'string\',
              GT=\'string\',
              LT=\'string\',
              GE=\'string\',
              LE=\'string\',
              NE=\'string\',
              Prefix=\'string\',
              SortOrder=\'asc\'|\'dsc\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
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
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Results\': [
                    {
                        \'BatchPredictionId\': \'string\',
                        \'MLModelId\': \'string\',
                        \'BatchPredictionDataSourceId\': \'string\',
                        \'InputDataLocationS3\': \'string\',
                        \'CreatedByIamUser\': \'string\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'LastUpdatedAt\': datetime(2015, 1, 1),
                        \'Name\': \'string\',
                        \'Status\': \'PENDING\'|\'INPROGRESS\'|\'FAILED\'|\'COMPLETED\'|\'DELETED\',
                        \'OutputUri\': \'string\',
                        \'Message\': \'string\',
                        \'ComputeTime\': 123,
                        \'FinishedAt\': datetime(2015, 1, 1),
                        \'StartedAt\': datetime(2015, 1, 1),
                        \'TotalRecordCount\': 123,
                        \'InvalidRecordCount\': 123
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeBatchPredictions`` operation. The content is essentially a list of ``BatchPrediction`` s.
        
            - **Results** *(list) --* 
        
              A list of ``BatchPrediction`` objects that meet the search criteria. 
        
              - *(dict) --* 
        
                Represents the output of a ``GetBatchPrediction`` operation.
        
                The content consists of the detailed metadata, the status, and the data file information of a ``Batch Prediction`` .
        
                - **BatchPredictionId** *(string) --* 
        
                  The ID assigned to the ``BatchPrediction`` at creation. This value should be identical to the value of the ``BatchPredictionID`` in the request. 
        
                - **MLModelId** *(string) --* 
        
                  The ID of the ``MLModel`` that generated predictions for the ``BatchPrediction`` request.
        
                - **BatchPredictionDataSourceId** *(string) --* 
        
                  The ID of the ``DataSource`` that points to the group of observations to predict.
        
                - **InputDataLocationS3** *(string) --* 
        
                  The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
        
                - **CreatedByIamUser** *(string) --* 
        
                  The AWS user account that invoked the ``BatchPrediction`` . The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
        
                - **CreatedAt** *(datetime) --* 
        
                  The time that the ``BatchPrediction`` was created. The time is expressed in epoch time.
        
                - **LastUpdatedAt** *(datetime) --* 
        
                  The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in epoch time.
        
                - **Name** *(string) --* 
        
                  A user-supplied name or description of the ``BatchPrediction`` .
        
                - **Status** *(string) --* 
        
                  The status of the ``BatchPrediction`` . This element can have one of the following values:
        
                  * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to generate predictions for a batch of observations.
                   
                  * ``INPROGRESS`` - The process is underway.
                   
                  * ``FAILED`` - The request to perform a batch prediction did not run to completion. It is not usable.
                   
                  * ``COMPLETED`` - The batch prediction process completed successfully.
                   
                  * ``DELETED`` - The ``BatchPrediction`` is marked as deleted. It is not usable.
                   
                - **OutputUri** *(string) --* 
        
                  The location of an Amazon S3 bucket or directory to receive the operation results. The following substrings are not allowed in the ``s3 key`` portion of the ``outputURI`` field: \':\', \'//\', \'/./\', \'/../\'.
        
                - **Message** *(string) --* 
        
                  A description of the most recent details about processing the batch prediction request.
        
                - **ComputeTime** *(integer) --* 
        
                  Long integer type that is a 64-bit signed number.
        
                - **FinishedAt** *(datetime) --* 
        
                  A timestamp represented in epoch time.
        
                - **StartedAt** *(datetime) --* 
        
                  A timestamp represented in epoch time.
        
                - **TotalRecordCount** *(integer) --* 
        
                  Long integer type that is a 64-bit signed number.
        
                - **InvalidRecordCount** *(integer) --* 
        
                  Long integer type that is a 64-bit signed number.
        
        """
        pass


class DescribeDataSources(Paginator):
    def paginate(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeDataSources>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              FilterVariable=\'CreatedAt\'|\'LastUpdatedAt\'|\'Status\'|\'Name\'|\'DataLocationS3\'|\'IAMUser\',
              EQ=\'string\',
              GT=\'string\',
              LT=\'string\',
              GE=\'string\',
              LE=\'string\',
              NE=\'string\',
              Prefix=\'string\',
              SortOrder=\'asc\'|\'dsc\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
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
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Results\': [
                    {
                        \'DataSourceId\': \'string\',
                        \'DataLocationS3\': \'string\',
                        \'DataRearrangement\': \'string\',
                        \'CreatedByIamUser\': \'string\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'LastUpdatedAt\': datetime(2015, 1, 1),
                        \'DataSizeInBytes\': 123,
                        \'NumberOfFiles\': 123,
                        \'Name\': \'string\',
                        \'Status\': \'PENDING\'|\'INPROGRESS\'|\'FAILED\'|\'COMPLETED\'|\'DELETED\',
                        \'Message\': \'string\',
                        \'RedshiftMetadata\': {
                            \'RedshiftDatabase\': {
                                \'DatabaseName\': \'string\',
                                \'ClusterIdentifier\': \'string\'
                            },
                            \'DatabaseUserName\': \'string\',
                            \'SelectSqlQuery\': \'string\'
                        },
                        \'RDSMetadata\': {
                            \'Database\': {
                                \'InstanceIdentifier\': \'string\',
                                \'DatabaseName\': \'string\'
                            },
                            \'DatabaseUserName\': \'string\',
                            \'SelectSqlQuery\': \'string\',
                            \'ResourceRole\': \'string\',
                            \'ServiceRole\': \'string\',
                            \'DataPipelineId\': \'string\'
                        },
                        \'RoleARN\': \'string\',
                        \'ComputeStatistics\': True|False,
                        \'ComputeTime\': 123,
                        \'FinishedAt\': datetime(2015, 1, 1),
                        \'StartedAt\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the query results from a  DescribeDataSources operation. The content is essentially a list of ``DataSource`` .
        
            - **Results** *(list) --* 
        
              A list of ``DataSource`` that meet the search criteria. 
        
              - *(dict) --* 
        
                Represents the output of the ``GetDataSource`` operation. 
        
                The content consists of the detailed metadata and data file information and the current status of the ``DataSource`` . 
        
                - **DataSourceId** *(string) --* 
        
                  The ID that is assigned to the ``DataSource`` during creation.
        
                - **DataLocationS3** *(string) --* 
        
                  The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is used by a ``DataSource`` .
        
                - **DataRearrangement** *(string) --* 
        
                  A JSON string that represents the splitting and rearrangement requirement used when this ``DataSource`` was created.
        
                - **CreatedByIamUser** *(string) --* 
        
                  The AWS user account from which the ``DataSource`` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
        
                - **CreatedAt** *(datetime) --* 
        
                  The time that the ``DataSource`` was created. The time is expressed in epoch time.
        
                - **LastUpdatedAt** *(datetime) --* 
        
                  The time of the most recent edit to the ``BatchPrediction`` . The time is expressed in epoch time.
        
                - **DataSizeInBytes** *(integer) --* 
        
                  The total number of observations contained in the data files that the ``DataSource`` references.
        
                - **NumberOfFiles** *(integer) --* 
        
                  The number of data files referenced by the ``DataSource`` .
        
                - **Name** *(string) --* 
        
                  A user-supplied name or description of the ``DataSource`` .
        
                - **Status** *(string) --* 
        
                  The current status of the ``DataSource`` . This element can have one of the following values: 
        
                  * PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a ``DataSource`` .
                   
                  * INPROGRESS - The creation process is underway.
                   
                  * FAILED - The request to create a ``DataSource`` did not run to completion. It is not usable.
                   
                  * COMPLETED - The creation process completed successfully.
                   
                  * DELETED - The ``DataSource`` is marked as deleted. It is not usable.
                   
                - **Message** *(string) --* 
        
                  A description of the most recent details about creating the ``DataSource`` .
        
                - **RedshiftMetadata** *(dict) --* 
        
                  Describes the ``DataSource`` details specific to Amazon Redshift.
        
                  - **RedshiftDatabase** *(dict) --* 
        
                    Describes the database details required to connect to an Amazon Redshift database.
        
                    - **DatabaseName** *(string) --* 
        
                      The name of a database hosted on an Amazon Redshift cluster.
        
                    - **ClusterIdentifier** *(string) --* 
        
                      The ID of an Amazon Redshift cluster.
        
                  - **DatabaseUserName** *(string) --* 
        
                    A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the ``RedshiftSelectSqlQuery`` query. The username should be valid for an Amazon Redshift `USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ .
        
                  - **SelectSqlQuery** *(string) --* 
        
                    The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if ``Verbose`` is true in GetDataSourceInput. 
        
                - **RDSMetadata** *(dict) --* 
        
                  The datasource details that are specific to Amazon RDS.
        
                  - **Database** *(dict) --* 
        
                    The database details required to connect to an Amazon RDS.
        
                    - **InstanceIdentifier** *(string) --* 
        
                      The ID of an RDS DB instance.
        
                    - **DatabaseName** *(string) --* 
        
                      The name of a database hosted on an RDS DB instance.
        
                  - **DatabaseUserName** *(string) --* 
        
                    The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an ``RDSSelectSqlQuery`` query.
        
                  - **SelectSqlQuery** *(string) --* 
        
                    The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if ``Verbose`` is true in ``GetDataSourceInput`` . 
        
                  - **ResourceRole** *(string) --* 
        
                    The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.
        
                  - **ServiceRole** *(string) --* 
        
                    The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see `Role templates <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html>`__ for data pipelines.
        
                  - **DataPipelineId** *(string) --* 
        
                    The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to Amazon S3. You can use the ID to find details about the instance in the Data Pipeline console.
        
                - **RoleARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of an `AWS IAM Role <http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts>`__ , such as the following: arn:aws:iam::account:role/rolename. 
        
                - **ComputeStatistics** *(boolean) --* 
        
                  The parameter is ``true`` if statistics need to be generated from the observation data. 
        
                - **ComputeTime** *(integer) --* 
        
                  Long integer type that is a 64-bit signed number.
        
                - **FinishedAt** *(datetime) --* 
        
                  A timestamp represented in epoch time.
        
                - **StartedAt** *(datetime) --* 
        
                  A timestamp represented in epoch time.
        
        """
        pass


class DescribeEvaluations(Paginator):
    def paginate(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeEvaluations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              FilterVariable=\'CreatedAt\'|\'LastUpdatedAt\'|\'Status\'|\'Name\'|\'IAMUser\'|\'MLModelId\'|\'DataSourceId\'|\'DataURI\',
              EQ=\'string\',
              GT=\'string\',
              LT=\'string\',
              GE=\'string\',
              LE=\'string\',
              NE=\'string\',
              Prefix=\'string\',
              SortOrder=\'asc\'|\'dsc\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
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
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Results\': [
                    {
                        \'EvaluationId\': \'string\',
                        \'MLModelId\': \'string\',
                        \'EvaluationDataSourceId\': \'string\',
                        \'InputDataLocationS3\': \'string\',
                        \'CreatedByIamUser\': \'string\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'LastUpdatedAt\': datetime(2015, 1, 1),
                        \'Name\': \'string\',
                        \'Status\': \'PENDING\'|\'INPROGRESS\'|\'FAILED\'|\'COMPLETED\'|\'DELETED\',
                        \'PerformanceMetrics\': {
                            \'Properties\': {
                                \'string\': \'string\'
                            }
                        },
                        \'Message\': \'string\',
                        \'ComputeTime\': 123,
                        \'FinishedAt\': datetime(2015, 1, 1),
                        \'StartedAt\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the query results from a ``DescribeEvaluations`` operation. The content is essentially a list of ``Evaluation`` .
        
            - **Results** *(list) --* 
        
              A list of ``Evaluation`` that meet the search criteria. 
        
              - *(dict) --* 
        
                Represents the output of ``GetEvaluation`` operation. 
        
                The content consists of the detailed metadata and data file information and the current status of the ``Evaluation`` .
        
                - **EvaluationId** *(string) --* 
        
                  The ID that is assigned to the ``Evaluation`` at creation.
        
                - **MLModelId** *(string) --* 
        
                  The ID of the ``MLModel`` that is the focus of the evaluation.
        
                - **EvaluationDataSourceId** *(string) --* 
        
                  The ID of the ``DataSource`` that is used to evaluate the ``MLModel`` .
        
                - **InputDataLocationS3** *(string) --* 
        
                  The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is used in the evaluation.
        
                - **CreatedByIamUser** *(string) --* 
        
                  The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
        
                - **CreatedAt** *(datetime) --* 
        
                  The time that the ``Evaluation`` was created. The time is expressed in epoch time.
        
                - **LastUpdatedAt** *(datetime) --* 
        
                  The time of the most recent edit to the ``Evaluation`` . The time is expressed in epoch time.
        
                - **Name** *(string) --* 
        
                  A user-supplied name or description of the ``Evaluation`` . 
        
                - **Status** *(string) --* 
        
                  The status of the evaluation. This element can have one of the following values:
        
                  * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an ``MLModel`` .
                   
                  * ``INPROGRESS`` - The evaluation is underway.
                   
                  * ``FAILED`` - The request to evaluate an ``MLModel`` did not run to completion. It is not usable.
                   
                  * ``COMPLETED`` - The evaluation process completed successfully.
                   
                  * ``DELETED`` - The ``Evaluation`` is marked as deleted. It is not usable.
                   
                - **PerformanceMetrics** *(dict) --* 
        
                  Measurements of how well the ``MLModel`` performed, using observations referenced by the ``DataSource`` . One of the following metrics is returned, based on the type of the ``MLModel`` : 
        
                  * BinaryAUC: A binary ``MLModel`` uses the Area Under the Curve (AUC) technique to measure performance.  
                   
                  * RegressionRMSE: A regression ``MLModel`` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable. 
                   
                  * MulticlassAvgFScore: A multiclass ``MLModel`` uses the F1 score technique to measure performance.  
                   
                  For more information about performance metrics, please see the `Amazon Machine Learning Developer Guide <http://docs.aws.amazon.com/machine-learning/latest/dg>`__ . 
        
                  - **Properties** *(dict) --* 
                    
                    - *(string) --* 
                      
                      - *(string) --* 
                
                - **Message** *(string) --* 
        
                  A description of the most recent details about evaluating the ``MLModel`` .
        
                - **ComputeTime** *(integer) --* 
        
                  Long integer type that is a 64-bit signed number.
        
                - **FinishedAt** *(datetime) --* 
        
                  A timestamp represented in epoch time.
        
                - **StartedAt** *(datetime) --* 
        
                  A timestamp represented in epoch time.
        
        """
        pass


class DescribeMLModels(Paginator):
    def paginate(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeMLModels>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              FilterVariable=\'CreatedAt\'|\'LastUpdatedAt\'|\'Status\'|\'Name\'|\'IAMUser\'|\'TrainingDataSourceId\'|\'RealtimeEndpointStatus\'|\'MLModelType\'|\'Algorithm\'|\'TrainingDataURI\',
              EQ=\'string\',
              GT=\'string\',
              LT=\'string\',
              GE=\'string\',
              LE=\'string\',
              NE=\'string\',
              Prefix=\'string\',
              SortOrder=\'asc\'|\'dsc\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
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
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Results\': [
                    {
                        \'MLModelId\': \'string\',
                        \'TrainingDataSourceId\': \'string\',
                        \'CreatedByIamUser\': \'string\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'LastUpdatedAt\': datetime(2015, 1, 1),
                        \'Name\': \'string\',
                        \'Status\': \'PENDING\'|\'INPROGRESS\'|\'FAILED\'|\'COMPLETED\'|\'DELETED\',
                        \'SizeInBytes\': 123,
                        \'EndpointInfo\': {
                            \'PeakRequestsPerSecond\': 123,
                            \'CreatedAt\': datetime(2015, 1, 1),
                            \'EndpointUrl\': \'string\',
                            \'EndpointStatus\': \'NONE\'|\'READY\'|\'UPDATING\'|\'FAILED\'
                        },
                        \'TrainingParameters\': {
                            \'string\': \'string\'
                        },
                        \'InputDataLocationS3\': \'string\',
                        \'Algorithm\': \'sgd\',
                        \'MLModelType\': \'REGRESSION\'|\'BINARY\'|\'MULTICLASS\',
                        \'ScoreThreshold\': ...,
                        \'ScoreThresholdLastUpdatedAt\': datetime(2015, 1, 1),
                        \'Message\': \'string\',
                        \'ComputeTime\': 123,
                        \'FinishedAt\': datetime(2015, 1, 1),
                        \'StartedAt\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeMLModels`` operation. The content is essentially a list of ``MLModel`` .
        
            - **Results** *(list) --* 
        
              A list of ``MLModel`` that meet the search criteria.
        
              - *(dict) --* 
        
                Represents the output of a ``GetMLModel`` operation. 
        
                The content consists of the detailed metadata and the current status of the ``MLModel`` .
        
                - **MLModelId** *(string) --* 
        
                  The ID assigned to the ``MLModel`` at creation.
        
                - **TrainingDataSourceId** *(string) --* 
        
                  The ID of the training ``DataSource`` . The ``CreateMLModel`` operation uses the ``TrainingDataSourceId`` .
        
                - **CreatedByIamUser** *(string) --* 
        
                  The AWS user account from which the ``MLModel`` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
        
                - **CreatedAt** *(datetime) --* 
        
                  The time that the ``MLModel`` was created. The time is expressed in epoch time.
        
                - **LastUpdatedAt** *(datetime) --* 
        
                  The time of the most recent edit to the ``MLModel`` . The time is expressed in epoch time.
        
                - **Name** *(string) --* 
        
                  A user-supplied name or description of the ``MLModel`` .
        
                - **Status** *(string) --* 
        
                  The current status of an ``MLModel`` . This element can have one of the following values: 
        
                  * ``PENDING`` - Amazon Machine Learning (Amazon ML) submitted a request to create an ``MLModel`` .
                   
                  * ``INPROGRESS`` - The creation process is underway.
                   
                  * ``FAILED`` - The request to create an ``MLModel`` didn\'t run to completion. The model isn\'t usable.
                   
                  * ``COMPLETED`` - The creation process completed successfully.
                   
                  * ``DELETED`` - The ``MLModel`` is marked as deleted. It isn\'t usable.
                   
                - **SizeInBytes** *(integer) --* 
        
                  Long integer type that is a 64-bit signed number.
        
                - **EndpointInfo** *(dict) --* 
        
                  The current endpoint of the ``MLModel`` .
        
                  - **PeakRequestsPerSecond** *(integer) --* 
        
                    The maximum processing rate for the real-time endpoint for ``MLModel`` , measured in incoming requests per second.
        
                  - **CreatedAt** *(datetime) --* 
        
                    The time that the request to create the real-time endpoint for the ``MLModel`` was received. The time is expressed in epoch time.
        
                  - **EndpointUrl** *(string) --* 
        
                    The URI that specifies where to send real-time prediction requests for the ``MLModel`` .
        
                    .. note::
        
                      Note 
        
                      The application must wait until the real-time endpoint is ready before using this URI.
        
                  - **EndpointStatus** *(string) --* 
        
                    The current status of the real-time endpoint for the ``MLModel`` . This element can have one of the following values: 
        
                    * ``NONE`` - Endpoint does not exist or was previously deleted.
                     
                    * ``READY`` - Endpoint is ready to be used for real-time predictions.
                     
                    * ``UPDATING`` - Updating/creating the endpoint. 
                     
                - **TrainingParameters** *(dict) --* 
        
                  A list of the training parameters in the ``MLModel`` . The list is implemented as a map of key-value pairs.
        
                  The following is the current set of training parameters: 
        
                  * ``sgd.maxMLModelSizeInBytes`` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from ``100000`` to ``2147483648`` . The default value is ``33554432`` . 
                   
                  * ``sgd.maxPasses`` - The number of times that the training process traverses the observations to build the ``MLModel`` . The value is an integer that ranges from ``1`` to ``10000`` . The default value is ``10`` .
                   
                  * ``sgd.shuffleType`` - Whether Amazon ML shuffles the training data. Shuffling the data improves a model\'s ability to find the optimal solution for a variety of data types. The valid values are ``auto`` and ``none`` . The default value is ``none`` .
                   
                  * ``sgd.l1RegularizationAmount`` - The coefficient regularization L1 norm, which controls overfitting the data by penalizing large coefficients. This parameter tends to drive coefficients to zero, resulting in sparse feature set. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L1 normalization. This parameter can\'t be used when ``L2`` is specified. Use this parameter sparingly. 
                   
                  * ``sgd.l2RegularizationAmount`` - The coefficient regularization L2 norm, which controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as ``1.0E-08`` . The value is a double that ranges from ``0`` to ``MAX_DOUBLE`` . The default is to not use L2 normalization. This parameter can\'t be used when ``L1`` is specified. Use this parameter sparingly. 
                   
                  - *(string) --* 
        
                    String type.
        
                    - *(string) --* 
        
                      String type.
        
                - **InputDataLocationS3** *(string) --* 
        
                  The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
        
                - **Algorithm** *(string) --* 
        
                  The algorithm used to train the ``MLModel`` . The following algorithm is supported:
        
                  * ``SGD`` -- Stochastic gradient descent. The goal of ``SGD`` is to minimize the gradient of the loss function. 
                   
                - **MLModelType** *(string) --* 
        
                  Identifies the ``MLModel`` category. The following are the available types:
        
                  * ``REGRESSION`` - Produces a numeric result. For example, \"What price should a house be listed at?\"
                   
                  * ``BINARY`` - Produces one of two possible results. For example, \"Is this a child-friendly web site?\".
                   
                  * ``MULTICLASS`` - Produces one of several possible results. For example, \"Is this a HIGH-, LOW-, or MEDIUM-risk trade?\".
                   
                - **ScoreThreshold** *(float) --* 
                
                - **ScoreThresholdLastUpdatedAt** *(datetime) --* 
        
                  The time of the most recent edit to the ``ScoreThreshold`` . The time is expressed in epoch time.
        
                - **Message** *(string) --* 
        
                  A description of the most recent details about accessing the ``MLModel`` .
        
                - **ComputeTime** *(integer) --* 
        
                  Long integer type that is a 64-bit signed number.
        
                - **FinishedAt** *(datetime) --* 
        
                  A timestamp represented in epoch time.
        
                - **StartedAt** *(datetime) --* 
        
                  A timestamp represented in epoch time.
        
        """
        pass
