from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def describe_dimension_keys(self, ServiceType: str, Identifier: str, StartTime: datetime, EndTime: datetime, Metric: str, GroupBy: Dict, PeriodInSeconds: int = None, PartitionBy: Dict = None, Filter: Dict = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pi-2018-02-27/DescribeDimensionKeys>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_dimension_keys(
              ServiceType=\'RDS\',
              Identifier=\'string\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Metric=\'string\',
              PeriodInSeconds=123,
              GroupBy={
                  \'Group\': \'string\',
                  \'Dimensions\': [
                      \'string\',
                  ],
                  \'Limit\': 123
              },
              PartitionBy={
                  \'Group\': \'string\',
                  \'Dimensions\': [
                      \'string\',
                  ],
                  \'Limit\': 123
              },
              Filter={
                  \'string\': \'string\'
              },
              MaxResults=123,
              NextToken=\'string\'
          )
        :type ServiceType: string
        :param ServiceType: **[REQUIRED]** 
        
          The AWS service for which Performance Insights will return metrics. The only valid value for *ServiceType* is: ``RDS``  
        
        :type Identifier: string
        :param Identifier: **[REQUIRED]** 
        
          An immutable, AWS Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.
        
          To use an Amazon RDS instance as a data source, you specify its ``DbiResourceId`` value - for example: ``db-FAIHNTYBKTGAUSUZQYPDS2GW4A``  
        
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]** 
        
          The date and time specifying the beginning of the requested time series data. You can\'t specify a ``StartTime`` that\'s earlier than 7 days ago. The value specified is *inclusive* - data points equal to or greater than ``StartTime`` will be returned.
        
          The value for ``StartTime`` must be earlier than the value for ``EndTime`` .
        
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]** 
        
          The date and time specifying the end of the requested time series data. The value specified is *exclusive* - data points less than (but not equal to) ``EndTime`` will be returned.
        
          The value for ``EndTime`` must be later than the value for ``StartTime`` .
        
        :type Metric: string
        :param Metric: **[REQUIRED]** 
        
          The name of a Performance Insights metric to be measured.
        
          Valid values for ``Metric`` are:
        
          * ``db.load.avg`` - a scaled representation of the number of active sessions for the database engine. 
           
          * ``db.sampledload.avg`` - the raw number of active sessions for the database engine. 
           
        :type PeriodInSeconds: integer
        :param PeriodInSeconds: 
        
          The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:
        
          * ``1`` (one second) 
           
          * ``60`` (one minute) 
           
          * ``300`` (five minutes) 
           
          * ``3600`` (one hour) 
           
          * ``86400`` (twenty-four hours) 
           
          If you don\'t specify ``PeriodInSeconds`` , then Performance Insights will choose a value for you, with a goal of returning roughly 100-200 data points in the response.
        
        :type GroupBy: dict
        :param GroupBy: **[REQUIRED]** 
        
          A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.
        
          - **Group** *(string) --* **[REQUIRED]** 
        
            The name of the dimension group. Valid values are:
        
            * ``db.user``   
             
            * ``db.host``   
             
            * ``db.sql``   
             
            * ``db.sql_tokenized``   
             
            * ``db.wait_event``   
             
            * ``db.wait_event_type``   
             
          - **Dimensions** *(list) --* 
        
            A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested, or are present in the response.
        
            Valid values for elements in the ``Dimensions`` array are:
        
            * db.user.id 
             
            * db.user.name 
             
            * db.host.id 
             
            * db.host.name 
             
            * db.sql.id 
             
            * db.sql.db_id 
             
            * db.sql.statement 
             
            * db.sql.tokenized_id 
             
            * db.sql_tokenized.id 
             
            * db.sql_tokenized.db_id 
             
            * db.sql_tokenized.statement 
             
            * db.wait_event.name 
             
            * db.wait_event.type 
             
            * db.wait_event_type.name 
             
            - *(string) --* 
        
          - **Limit** *(integer) --* 
        
            The maximum number of items to fetch for this dimension group.
        
        :type PartitionBy: dict
        :param PartitionBy: 
        
          For each dimension specified in ``GroupBy`` , specify a secondary dimension to further subdivide the partition keys in the response.
        
          - **Group** *(string) --* **[REQUIRED]** 
        
            The name of the dimension group. Valid values are:
        
            * ``db.user``   
             
            * ``db.host``   
             
            * ``db.sql``   
             
            * ``db.sql_tokenized``   
             
            * ``db.wait_event``   
             
            * ``db.wait_event_type``   
             
          - **Dimensions** *(list) --* 
        
            A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested, or are present in the response.
        
            Valid values for elements in the ``Dimensions`` array are:
        
            * db.user.id 
             
            * db.user.name 
             
            * db.host.id 
             
            * db.host.name 
             
            * db.sql.id 
             
            * db.sql.db_id 
             
            * db.sql.statement 
             
            * db.sql.tokenized_id 
             
            * db.sql_tokenized.id 
             
            * db.sql_tokenized.db_id 
             
            * db.sql_tokenized.statement 
             
            * db.wait_event.name 
             
            * db.wait_event.type 
             
            * db.wait_event_type.name 
             
            - *(string) --* 
        
          - **Limit** *(integer) --* 
        
            The maximum number of items to fetch for this dimension group.
        
        :type Filter: dict
        :param Filter: 
        
          One or more filters to apply in the request. Restrictions:
        
          * Any number of filters by the same dimension, as specified in the ``GroupBy`` or ``Partition`` parameters. 
           
          * A single filter for any other dimension in this dimension group. 
           
          - *(string) --* 
        
            - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return in the response. If more items exist than the specified ``MaxRecords`` value, a pagination token is included in the response so that the remaining results can be retrieved. 
        
        :type NextToken: string
        :param NextToken: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by ``MaxRecords`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AlignedStartTime\': datetime(2015, 1, 1),
                \'AlignedEndTime\': datetime(2015, 1, 1),
                \'PartitionKeys\': [
                    {
                        \'Dimensions\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                \'Keys\': [
                    {
                        \'Dimensions\': {
                            \'string\': \'string\'
                        },
                        \'Total\': 123.0,
                        \'Partitions\': [
                            123.0,
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AlignedStartTime** *(datetime) --* 
        
              The start time for the returned dimension keys, after alignment to a granular boundary (as specified by ``PeriodInSeconds`` ). ``AlignedStartTime`` will be less than or equal to the value of the user-specified ``StartTime`` .
        
            - **AlignedEndTime** *(datetime) --* 
        
              The end time for the returned dimension keys, after alignment to a granular boundary (as specified by ``PeriodInSeconds`` ). ``AlignedEndTime`` will be greater than or equal to the value of the user-specified ``Endtime`` .
        
            - **PartitionKeys** *(list) --* 
        
              If ``PartitionBy`` was present in the request, ``PartitionKeys`` contains the breakdown of dimension keys by the specified partitions.
        
              - *(dict) --* 
        
                If ``PartitionBy`` was specified in a ``DescribeDimensionKeys`` request, the dimensions are returned in an array. Each element in the array specifies one dimension. 
        
                - **Dimensions** *(dict) --* 
        
                  A dimension map that contains the dimension(s) for this partition.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
            - **Keys** *(list) --* 
        
              The dimension keys that were requested.
        
              - *(dict) --* 
        
                An array of descriptions and aggregated values for each dimension within a dimension group.
        
                - **Dimensions** *(dict) --* 
        
                  A map of name-value pairs for the dimensions in the group.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **Total** *(float) --* 
        
                  The aggregated metric value for the dimension(s), over the requested time range.
        
                - **Partitions** *(list) --* 
        
                  If ``PartitionBy`` was specified, ``PartitionKeys`` contains the dimensions that were.
        
                  - *(float) --* 
              
            - **NextToken** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by ``MaxRecords`` .
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        
        :returns: The presigned url
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_resource_metrics(self, ServiceType: str, Identifier: str, MetricQueries: List, StartTime: datetime, EndTime: datetime, PeriodInSeconds: int = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pi-2018-02-27/GetResourceMetrics>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_resource_metrics(
              ServiceType=\'RDS\',
              Identifier=\'string\',
              MetricQueries=[
                  {
                      \'Metric\': \'string\',
                      \'GroupBy\': {
                          \'Group\': \'string\',
                          \'Dimensions\': [
                              \'string\',
                          ],
                          \'Limit\': 123
                      },
                      \'Filter\': {
                          \'string\': \'string\'
                      }
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PeriodInSeconds=123,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type ServiceType: string
        :param ServiceType: **[REQUIRED]** 
        
          The AWS service for which Performance Insights will return metrics. The only valid value for *ServiceType* is: ``RDS``  
        
        :type Identifier: string
        :param Identifier: **[REQUIRED]** 
        
          An immutable, AWS Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.
        
          To use an Amazon RDS instance as a data source, you specify its ``DbiResourceId`` value - for example: ``db-FAIHNTYBKTGAUSUZQYPDS2GW4A``  
        
        :type MetricQueries: list
        :param MetricQueries: **[REQUIRED]** 
        
          An array of one or more queries to perform. Each query must specify a Performance Insights metric, and can optionally specify aggregation and filtering criteria.
        
          - *(dict) --* 
        
            A single query to be processed. You must provide the metric to query. If no other parameters are specified, Performance Insights returns all of the data points for that metric. You can optionally request that the data points be aggregated by dimension group ( ``GroupBy`` ), and return only those data points that match your criteria (``Filter`` ).
        
            - **Metric** *(string) --* **[REQUIRED]** 
        
              The name of a Performance Insights metric to be measured.
        
              Valid values for ``Metric`` are:
        
              * ``db.load.avg`` - a scaled representation of the number of active sessions for the database engine. 
               
              * ``db.sampledload.avg`` - the raw number of active sessions for the database engine. 
               
            - **GroupBy** *(dict) --* 
        
              A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.
        
              - **Group** *(string) --* **[REQUIRED]** 
        
                The name of the dimension group. Valid values are:
        
                * ``db.user``   
                 
                * ``db.host``   
                 
                * ``db.sql``   
                 
                * ``db.sql_tokenized``   
                 
                * ``db.wait_event``   
                 
                * ``db.wait_event_type``   
                 
              - **Dimensions** *(list) --* 
        
                A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested, or are present in the response.
        
                Valid values for elements in the ``Dimensions`` array are:
        
                * db.user.id 
                 
                * db.user.name 
                 
                * db.host.id 
                 
                * db.host.name 
                 
                * db.sql.id 
                 
                * db.sql.db_id 
                 
                * db.sql.statement 
                 
                * db.sql.tokenized_id 
                 
                * db.sql_tokenized.id 
                 
                * db.sql_tokenized.db_id 
                 
                * db.sql_tokenized.statement 
                 
                * db.wait_event.name 
                 
                * db.wait_event.type 
                 
                * db.wait_event_type.name 
                 
                - *(string) --* 
        
              - **Limit** *(integer) --* 
        
                The maximum number of items to fetch for this dimension group.
        
            - **Filter** *(dict) --* 
        
              One or more filters to apply in the request. Restrictions:
        
              * Any number of filters by the same dimension, as specified in the ``GroupBy`` parameter. 
               
              * A single filter for any other dimension in this dimension group. 
               
              - *(string) --* 
        
                - *(string) --* 
        
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]** 
        
          The date and time specifying the beginning of the requested time series data. You can\'t specify a ``StartTime`` that\'s earlier than 7 days ago. The value specified is *inclusive* - data points equal to or greater than ``StartTime`` will be returned.
        
          The value for ``StartTime`` must be earlier than the value for ``EndTime`` .
        
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]** 
        
          The date and time specifiying the end of the requested time series data. The value specified is *exclusive* - data points less than (but not equal to) ``EndTime`` will be returned.
        
          The value for ``EndTime`` must be later than the value for ``StartTime`` .
        
        :type PeriodInSeconds: integer
        :param PeriodInSeconds: 
        
          The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:
        
          * ``1`` (one second) 
           
          * ``60`` (one minute) 
           
          * ``300`` (five minutes) 
           
          * ``3600`` (one hour) 
           
          * ``86400`` (twenty-four hours) 
           
          If you don\'t specify ``PeriodInSeconds`` , then Performance Insights will choose a value for you, with a goal of returning roughly 100-200 data points in the response.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return in the response. If more items exist than the specified ``MaxRecords`` value, a pagination token is included in the response so that the remaining results can be retrieved. 
        
        :type NextToken: string
        :param NextToken: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by ``MaxRecords`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AlignedStartTime\': datetime(2015, 1, 1),
                \'AlignedEndTime\': datetime(2015, 1, 1),
                \'Identifier\': \'string\',
                \'MetricList\': [
                    {
                        \'Key\': {
                            \'Metric\': \'string\',
                            \'Dimensions\': {
                                \'string\': \'string\'
                            }
                        },
                        \'DataPoints\': [
                            {
                                \'Timestamp\': datetime(2015, 1, 1),
                                \'Value\': 123.0
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AlignedStartTime** *(datetime) --* 
        
              The start time for the returned metrics, after alignment to a granular boundary (as specified by ``PeriodInSeconds`` ). ``AlignedStartTime`` will be less than or equal to the value of the user-specified ``StartTime`` .
        
            - **AlignedEndTime** *(datetime) --* 
        
              The end time for the returned metrics, after alignment to a granular boundary (as specified by ``PeriodInSeconds`` ). ``AlignedEndTime`` will be greater than or equal to the value of the user-specified ``Endtime`` .
        
            - **Identifier** *(string) --* 
        
              An immutable, AWS Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.
        
              To use an Amazon RDS instance as a data source, you specify its ``DbiResourceId`` value - for example: ``db-FAIHNTYBKTGAUSUZQYPDS2GW4A``  
        
            - **MetricList** *(list) --* 
        
              An array of metric results,, where each array element contains all of the data points for a particular dimension.
        
              - *(dict) --* 
        
                A time-ordered series of data points, correpsonding to a dimension of a Performance Insights metric.
        
                - **Key** *(dict) --* 
        
                  The dimension(s) to which the data points apply.
        
                  - **Metric** *(string) --* 
        
                    The name of a Performance Insights metric to be measured.
        
                    Valid values for ``Metric`` are:
        
                    * ``db.load.avg`` - a scaled representation of the number of active sessions for the database engine. 
                     
                    * ``db.sampledload.avg`` - the raw number of active sessions for the database engine. 
                     
                  - **Dimensions** *(dict) --* 
        
                    The valid dimensions for the metric.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                - **DataPoints** *(list) --* 
        
                  An array of timestamp-value pairs, representing measurements over a period of time.
        
                  - *(dict) --* 
        
                    A timestamp, and a single numerical value, which together represent a measurement at a particular point in time.
        
                    - **Timestamp** *(datetime) --* 
        
                      The time, in epoch format, associated with a particular ``Value`` .
        
                    - **Value** *(float) --* 
        
                      The actual value associated with a particular ``Timestamp`` .
        
            - **NextToken** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by ``MaxRecords`` .
        
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass
