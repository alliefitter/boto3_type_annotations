from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeObjects(Paginator):
    def paginate(self, pipelineId: str, objectIds: List, evaluateExpressions: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/DescribeObjects>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              pipelineId=\'string\',
              objectIds=[
                  \'string\',
              ],
              evaluateExpressions=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type pipelineId: string
        :param pipelineId: **[REQUIRED]** 
        
          The ID of the pipeline that contains the object definitions.
        
        :type objectIds: list
        :param objectIds: **[REQUIRED]** 
        
          The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to ``DescribeObjects`` .
        
          - *(string) --* 
        
        :type evaluateExpressions: boolean
        :param evaluateExpressions: 
        
          Indicates whether any expressions in the object should be evaluated when the object descriptions are returned.
        
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
                \'pipelineObjects\': [
                    {
                        \'id\': \'string\',
                        \'name\': \'string\',
                        \'fields\': [
                            {
                                \'key\': \'string\',
                                \'stringValue\': \'string\',
                                \'refValue\': \'string\'
                            },
                        ]
                    },
                ],
                \'hasMoreResults\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeObjects.
        
            - **pipelineObjects** *(list) --* 
        
              An array of object definitions.
        
              - *(dict) --* 
        
                Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
        
                - **id** *(string) --* 
        
                  The ID of the object.
        
                - **name** *(string) --* 
        
                  The name of the object.
        
                - **fields** *(list) --* 
        
                  Key-value pairs that define the properties of the object.
        
                  - *(dict) --* 
        
                    A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but not as both.
        
                    - **key** *(string) --* 
        
                      The field identifier.
        
                    - **stringValue** *(string) --* 
        
                      The field value, expressed as a String.
        
                    - **refValue** *(string) --* 
        
                      The field value, expressed as the identifier of another object.
        
            - **hasMoreResults** *(boolean) --* 
        
              Indicates whether there are more results to return.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPipelines(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/ListPipelines>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'pipelineIdList\': [
                    {
                        \'id\': \'string\',
                        \'name\': \'string\'
                    },
                ],
                \'hasMoreResults\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of ListPipelines.
        
            - **pipelineIdList** *(list) --* 
        
              The pipeline identifiers. If you require additional information about the pipelines, you can use these identifiers to call  DescribePipelines and  GetPipelineDefinition .
        
              - *(dict) --* 
        
                Contains the name and identifier of a pipeline.
        
                - **id** *(string) --* 
        
                  The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the form ``df-297EG78HU43EEXAMPLE`` .
        
                - **name** *(string) --* 
        
                  The name of the pipeline.
        
            - **hasMoreResults** *(boolean) --* 
        
              Indicates whether there are more results that can be obtained by a subsequent call.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class QueryObjects(Paginator):
    def paginate(self, pipelineId: str, sphere: str, query: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/QueryObjects>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              pipelineId=\'string\',
              query={
                  \'selectors\': [
                      {
                          \'fieldName\': \'string\',
                          \'operator\': {
                              \'type\': \'EQ\'|\'REF_EQ\'|\'LE\'|\'GE\'|\'BETWEEN\',
                              \'values\': [
                                  \'string\',
                              ]
                          }
                      },
                  ]
              },
              sphere=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type pipelineId: string
        :param pipelineId: **[REQUIRED]** 
        
          The ID of the pipeline.
        
        :type query: dict
        :param query: 
        
          The query that defines the objects to be returned. The ``Query`` object can contain a maximum of ten selectors. The conditions in the query are limited to top-level String fields in the object. These filters can be applied to components, instances, and attempts.
        
          - **selectors** *(list) --* 
        
            List of selectors that define the query. An object must satisfy all of the selectors to match the query.
        
            - *(dict) --* 
        
              A comparision that is used to determine whether a query should return this object.
        
              - **fieldName** *(string) --* 
        
                The name of the field that the operator will be applied to. The field name is the \"key\" portion of the field definition in the pipeline definition syntax that is used by the AWS Data Pipeline API. If the field is not set on the object, the condition fails.
        
              - **operator** *(dict) --* 
        
                Contains a logical operation for comparing the value of a field with a specified value.
        
                - **type** *(string) --* 
        
                  The logical operation to be performed: equal (``EQ`` ), equal reference (``REF_EQ`` ), less than or equal (``LE`` ), greater than or equal (``GE`` ), or between (``BETWEEN`` ). Equal reference (``REF_EQ`` ) can be used only with reference fields. The other comparison types can be used only with String fields. The comparison types you can use apply only to certain object fields, as detailed below. 
        
                  The comparison operators EQ and REF_EQ act on the following fields: 
        
                  * name
                   
                  * @sphere
                   
                  * parent
                   
                  * @componentParent
                   
                  * @instanceParent
                   
                  * @status
                   
                  * @scheduledStartTime
                   
                  * @scheduledEndTime
                   
                  * @actualStartTime
                   
                  * @actualEndTime
                   
                  The comparison operators ``GE`` , ``LE`` , and ``BETWEEN`` act on the following fields: 
        
                  * @scheduledStartTime
                   
                  * @scheduledEndTime
                   
                  * @actualStartTime
                   
                  * @actualEndTime
                   
                  Note that fields beginning with the at sign (@) are read-only and set by the web service. When you name fields, you should choose names containing only alpha-numeric values, as symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a pipeline should prefix their name with the string \"my\".
        
                - **values** *(list) --* 
        
                  The value that the actual field value will be compared with.
        
                  - *(string) --* 
        
        :type sphere: string
        :param sphere: **[REQUIRED]** 
        
          Indicates whether the query applies to components or instances. The possible values are: ``COMPONENT`` , ``INSTANCE`` , and ``ATTEMPT`` .
        
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
                \'ids\': [
                    \'string\',
                ],
                \'hasMoreResults\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of QueryObjects.
        
            - **ids** *(list) --* 
        
              The identifiers that match the query selectors.
        
              - *(string) --* 
          
            - **hasMoreResults** *(boolean) --* 
        
              Indicates whether there are more results that can be obtained by a subsequent call.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
