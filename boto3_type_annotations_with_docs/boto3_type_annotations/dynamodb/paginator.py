from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListBackups(Paginator):
    def paginate(self, TableName: str = None, TimeRangeLowerBound: datetime = None, TimeRangeUpperBound: datetime = None, BackupType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/ListBackups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              TableName=\'string\',
              TimeRangeLowerBound=datetime(2015, 1, 1),
              TimeRangeUpperBound=datetime(2015, 1, 1),
              BackupType=\'USER\'|\'SYSTEM\'|\'ALL\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type TableName: string
        :param TableName: 
        
          The backups from the table specified by ``TableName`` are listed. 
        
        :type TimeRangeLowerBound: datetime
        :param TimeRangeLowerBound: 
        
          Only backups created after this time are listed. ``TimeRangeLowerBound`` is inclusive.
        
        :type TimeRangeUpperBound: datetime
        :param TimeRangeUpperBound: 
        
          Only backups created before this time are listed. ``TimeRangeUpperBound`` is exclusive. 
        
        :type BackupType: string
        :param BackupType: 
        
          The backups from the table specified by ``BackupType`` are listed.
        
          Where ``BackupType`` can be:
        
          * ``USER`` - On-demand backup created by you. 
           
          * ``SYSTEM`` - On-demand backup automatically created by DynamoDB. 
           
          * ``ALL`` - All types of on-demand backups (USER and SYSTEM). 
           
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
                \'BackupSummaries\': [
                    {
                        \'TableName\': \'string\',
                        \'TableId\': \'string\',
                        \'TableArn\': \'string\',
                        \'BackupArn\': \'string\',
                        \'BackupName\': \'string\',
                        \'BackupCreationDateTime\': datetime(2015, 1, 1),
                        \'BackupExpiryDateTime\': datetime(2015, 1, 1),
                        \'BackupStatus\': \'CREATING\'|\'DELETED\'|\'AVAILABLE\',
                        \'BackupType\': \'USER\'|\'SYSTEM\',
                        \'BackupSizeBytes\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BackupSummaries** *(list) --* 
        
              List of ``BackupSummary`` objects.
        
              - *(dict) --* 
        
                Contains details for the backup.
        
                - **TableName** *(string) --* 
        
                  Name of the table.
        
                - **TableId** *(string) --* 
        
                  Unique identifier for the table.
        
                - **TableArn** *(string) --* 
        
                  ARN associated with the table.
        
                - **BackupArn** *(string) --* 
        
                  ARN associated with the backup.
        
                - **BackupName** *(string) --* 
        
                  Name of the specified backup.
        
                - **BackupCreationDateTime** *(datetime) --* 
        
                  Time at which the backup was created.
        
                - **BackupExpiryDateTime** *(datetime) --* 
        
                  Time at which the automatic on-demand backup created by DynamoDB will expire. This ``SYSTEM`` on-demand backup expires automatically 35 days after its creation.
        
                - **BackupStatus** *(string) --* 
        
                  Backup can be in one of the following states: CREATING, ACTIVE, DELETED.
        
                - **BackupType** *(string) --* 
        
                  BackupType:
        
                  * ``USER`` - On-demand backup created by you. 
                   
                  * ``SYSTEM`` - On-demand backup automatically created by DynamoDB. 
                   
                - **BackupSizeBytes** *(integer) --* 
        
                  Size of the backup in bytes.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListTables(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/ListTables>`_
        
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
                \'TableNames\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``ListTables`` operation.
        
            - **TableNames** *(list) --* 
        
              The names of the tables associated with the current account at the current endpoint. The maximum size of this array is 100.
        
              If ``LastEvaluatedTableName`` also appears in the output, you can use this value as the ``ExclusiveStartTableName`` parameter in a subsequent ``ListTables`` request and obtain the next page of results.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class Query(Paginator):
    def paginate(self, TableName: str, IndexName: str = None, Select: str = None, AttributesToGet: List = None, ConsistentRead: bool = None, KeyConditions: Dict = None, QueryFilter: Dict = None, ConditionalOperator: str = None, ScanIndexForward: bool = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, FilterExpression: str = None, KeyConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/Query>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              TableName=\'string\',
              IndexName=\'string\',
              Select=\'ALL_ATTRIBUTES\'|\'ALL_PROJECTED_ATTRIBUTES\'|\'SPECIFIC_ATTRIBUTES\'|\'COUNT\',
              AttributesToGet=[
                  \'string\',
              ],
              ConsistentRead=True|False,
              KeyConditions={
                  \'string\': {
                      \'AttributeValueList\': [
                          {
                              \'S\': \'string\',
                              \'N\': \'string\',
                              \'B\': b\'bytes\',
                              \'SS\': [
                                  \'string\',
                              ],
                              \'NS\': [
                                  \'string\',
                              ],
                              \'BS\': [
                                  b\'bytes\',
                              ],
                              \'M\': {
                                  \'string\': {\'... recursive ...\'}
                              },
                              \'L\': [
                                  {\'... recursive ...\'},
                              ],
                              \'NULL\': True|False,
                              \'BOOL\': True|False
                          },
                      ],
                      \'ComparisonOperator\': \'EQ\'|\'NE\'|\'IN\'|\'LE\'|\'LT\'|\'GE\'|\'GT\'|\'BETWEEN\'|\'NOT_NULL\'|\'NULL\'|\'CONTAINS\'|\'NOT_CONTAINS\'|\'BEGINS_WITH\'
                  }
              },
              QueryFilter={
                  \'string\': {
                      \'AttributeValueList\': [
                          {
                              \'S\': \'string\',
                              \'N\': \'string\',
                              \'B\': b\'bytes\',
                              \'SS\': [
                                  \'string\',
                              ],
                              \'NS\': [
                                  \'string\',
                              ],
                              \'BS\': [
                                  b\'bytes\',
                              ],
                              \'M\': {
                                  \'string\': {\'... recursive ...\'}
                              },
                              \'L\': [
                                  {\'... recursive ...\'},
                              ],
                              \'NULL\': True|False,
                              \'BOOL\': True|False
                          },
                      ],
                      \'ComparisonOperator\': \'EQ\'|\'NE\'|\'IN\'|\'LE\'|\'LT\'|\'GE\'|\'GT\'|\'BETWEEN\'|\'NOT_NULL\'|\'NULL\'|\'CONTAINS\'|\'NOT_CONTAINS\'|\'BEGINS_WITH\'
                  }
              },
              ConditionalOperator=\'AND\'|\'OR\',
              ScanIndexForward=True|False,
              ReturnConsumedCapacity=\'INDEXES\'|\'TOTAL\'|\'NONE\',
              ProjectionExpression=\'string\',
              FilterExpression=\'string\',
              KeyConditionExpression=\'string\',
              ExpressionAttributeNames={
                  \'string\': \'string\'
              },
              ExpressionAttributeValues={
                  \'string\': {
                      \'S\': \'string\',
                      \'N\': \'string\',
                      \'B\': b\'bytes\',
                      \'SS\': [
                          \'string\',
                      ],
                      \'NS\': [
                          \'string\',
                      ],
                      \'BS\': [
                          b\'bytes\',
                      ],
                      \'M\': {
                          \'string\': {\'... recursive ...\'}
                      },
                      \'L\': [
                          {\'... recursive ...\'},
                      ],
                      \'NULL\': True|False,
                      \'BOOL\': True|False
                  }
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type TableName: string
        :param TableName: **[REQUIRED]** 
        
          The name of the table containing the requested items.
        
        :type IndexName: string
        :param IndexName: 
        
          The name of an index to query. This index can be any local secondary index or global secondary index on the table. Note that if you use the ``IndexName`` parameter, you must also provide ``TableName.``  
        
        :type Select: string
        :param Select: 
        
          The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.
        
          * ``ALL_ATTRIBUTES`` - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required. 
           
          * ``ALL_PROJECTED_ATTRIBUTES`` - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying ``ALL_ATTRIBUTES`` . 
           
          * ``COUNT`` - Returns the number of matching items, rather than the matching items themselves. 
           
          * ``SPECIFIC_ATTRIBUTES`` - Returns only the attributes listed in ``AttributesToGet`` . This return value is equivalent to specifying ``AttributesToGet`` without specifying any value for ``Select`` . If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB will fetch each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table. 
           
          If neither ``Select`` nor ``AttributesToGet`` are specified, DynamoDB defaults to ``ALL_ATTRIBUTES`` when accessing a table, and ``ALL_PROJECTED_ATTRIBUTES`` when accessing an index. You cannot use both ``Select`` and ``AttributesToGet`` together in a single request, unless the value for ``Select`` is ``SPECIFIC_ATTRIBUTES`` . (This usage is equivalent to specifying ``AttributesToGet`` without any value for ``Select`` .)
        
          .. note::
        
            If you use the ``ProjectionExpression`` parameter, then the value for ``Select`` can only be ``SPECIFIC_ATTRIBUTES`` . Any other value for ``Select`` will return an error.
        
        :type AttributesToGet: list
        :param AttributesToGet: 
        
          This is a legacy parameter. Use ``ProjectionExpression`` instead. For more information, see `AttributesToGet <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
        :type ConsistentRead: boolean
        :param ConsistentRead: 
        
          Determines the read consistency model: If set to ``true`` , then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.
        
          Strongly consistent reads are not supported on global secondary indexes. If you query a global secondary index with ``ConsistentRead`` set to ``true`` , you will receive a ``ValidationException`` .
        
        :type KeyConditions: dict
        :param KeyConditions: 
        
          This is a legacy parameter. Use ``KeyConditionExpression`` instead. For more information, see `KeyConditions <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.KeyConditions.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
            - *(dict) --* 
        
              Represents the selection criteria for a ``Query`` or ``Scan`` operation:
        
              * For a ``Query`` operation, ``Condition`` is used for specifying the ``KeyConditions`` to use when querying a table or an index. For ``KeyConditions`` , only the following comparison operators are supported:  ``EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN``    ``Condition`` is also used in a ``QueryFilter`` , which evaluates the query results and returns only the desired values. 
               
              * For a ``Scan`` operation, ``Condition`` is used in a ``ScanFilter`` , which evaluates the scan results and returns only the desired values. 
               
              - **AttributeValueList** *(list) --* 
        
                One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ``ComparisonOperator`` being used.
        
                For type Number, value comparisons are numeric.
        
                String value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, ``a`` is greater than ``A`` , and ``a`` is greater than ``B`` . For a list of code values, see `http\://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .
        
                For Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.
        
                - *(dict) --* 
        
                  Represents the data for an attribute.
        
                  Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                  For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **S** *(string) --* 
        
                    An attribute of type String. For example:
        
                     ``\"S\": \"Hello\"``  
        
                  - **N** *(string) --* 
        
                    An attribute of type Number. For example:
        
                     ``\"N\": \"123.45\"``  
        
                    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                  - **B** *(bytes) --* 
        
                    An attribute of type Binary. For example:
        
                     ``\"B\": \"dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk\"``  
        
                  - **SS** *(list) --* 
        
                    An attribute of type String Set. For example:
        
                     ``\"SS\": [\"Giraffe\", \"Hippo\" ,\"Zebra\"]``  
        
                    - *(string) --* 
        
                  - **NS** *(list) --* 
        
                    An attribute of type Number Set. For example:
        
                     ``\"NS\": [\"42.2\", \"-19\", \"7.5\", \"3.14\"]``  
        
                    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                    - *(string) --* 
        
                  - **BS** *(list) --* 
        
                    An attribute of type Binary Set. For example:
        
                     ``\"BS\": [\"U3Vubnk=\", \"UmFpbnk=\", \"U25vd3k=\"]``  
        
                    - *(bytes) --* 
        
                  - **M** *(dict) --* 
        
                    An attribute of type Map. For example:
        
                     ``\"M\": {\"Name\": {\"S\": \"Joe\"}, \"Age\": {\"N\": \"35\"}}``  
        
                    - *(string) --* 
        
                      - *(dict) --* 
        
                        Represents the data for an attribute.
        
                        Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                        For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **L** *(list) --* 
        
                    An attribute of type List. For example:
        
                     ``\"L\": [\"Cookies\", \"Coffee\", 3.14159]``  
        
                    - *(dict) --* 
        
                      Represents the data for an attribute.
        
                      Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                      For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **NULL** *(boolean) --* 
        
                    An attribute of type Null. For example:
        
                     ``\"NULL\": true``  
        
                  - **BOOL** *(boolean) --* 
        
                    An attribute of type Boolean. For example:
        
                     ``\"BOOL\": true``  
        
              - **ComparisonOperator** *(string) --* **[REQUIRED]** 
        
                A comparator for evaluating attributes. For example, equals, greater than, less than, etc.
        
                The following comparison operators are available:
        
                 ``EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN``  
        
                The following are descriptions of each comparison operator.
        
                * ``EQ`` : Equal. ``EQ`` is supported for all data types, including lists and maps.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not equal ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``NE`` : Not equal. ``NE`` is supported for all data types, including lists and maps.  ``AttributeValueList`` can contain only one ``AttributeValue`` of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an ``AttributeValue`` of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not equal ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``LE`` : Less than or equal.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``LT`` : Less than.   ``AttributeValueList`` can contain only one ``AttributeValue`` of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``GE`` : Greater than or equal.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``GT`` : Greater than.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``NOT_NULL`` : The attribute exists. ``NOT_NULL`` is supported for all data types, including lists and maps. 
        
                .. note::
        
                   This operator tests for the existence of an attribute, not its data type. If the data type of attribute \"``a`` \" is null, and you evaluate it using ``NOT_NULL`` , the result is a Boolean ``true`` . This result is because the attribute \"``a`` \" exists; its data type is not relevant to the ``NOT_NULL`` comparison operator. 
        
                * ``NULL`` : The attribute does not exist. ``NULL`` is supported for all data types, including lists and maps. 
        
                .. note::
        
                   This operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute \"``a`` \" is null, and you evaluate it using ``NULL`` , the result is a Boolean ``false`` . This is because the attribute \"``a`` \" exists; its data type is not relevant to the ``NULL`` comparison operator. 
        
                * ``CONTAINS`` : Checks for a subsequence, or value in a set.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set (\"``SS`` \", \"``NS`` \", or \"``BS`` \"), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating \"``a CONTAINS b`` \", \"``a`` \" can be a list; however, \"``b`` \" cannot be a set, a map, or a list. 
                 
                * ``NOT_CONTAINS`` : Checks for absence of a subsequence, or absence of a value in a set.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set (\"``SS`` \", \"``NS`` \", or \"``BS`` \"), then the operator evaluates to true if it *does not* find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating \"``a NOT CONTAINS b`` \", \"``a`` \" can be a list; however, \"``b`` \" cannot be a set, a map, or a list. 
                 
                * ``BEGINS_WITH`` : Checks for a prefix.   ``AttributeValueList`` can contain only one ``AttributeValue`` of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).  
                 
                * ``IN`` : Checks for matching elements in a list.  ``AttributeValueList`` can contain one or more ``AttributeValue`` elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true. 
                 
                * ``BETWEEN`` : Greater than or equal to the first value, and less than or equal to the second value.   ``AttributeValueList`` must contain two ``AttributeValue`` elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not compare to ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}``   
                 
                For usage examples of ``AttributeValueList`` and ``ComparisonOperator`` , see `Legacy Conditional Parameters <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type QueryFilter: dict
        :param QueryFilter: 
        
          This is a legacy parameter. Use ``FilterExpression`` instead. For more information, see `QueryFilter <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.QueryFilter.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
            - *(dict) --* 
        
              Represents the selection criteria for a ``Query`` or ``Scan`` operation:
        
              * For a ``Query`` operation, ``Condition`` is used for specifying the ``KeyConditions`` to use when querying a table or an index. For ``KeyConditions`` , only the following comparison operators are supported:  ``EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN``    ``Condition`` is also used in a ``QueryFilter`` , which evaluates the query results and returns only the desired values. 
               
              * For a ``Scan`` operation, ``Condition`` is used in a ``ScanFilter`` , which evaluates the scan results and returns only the desired values. 
               
              - **AttributeValueList** *(list) --* 
        
                One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ``ComparisonOperator`` being used.
        
                For type Number, value comparisons are numeric.
        
                String value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, ``a`` is greater than ``A`` , and ``a`` is greater than ``B`` . For a list of code values, see `http\://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .
        
                For Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.
        
                - *(dict) --* 
        
                  Represents the data for an attribute.
        
                  Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                  For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **S** *(string) --* 
        
                    An attribute of type String. For example:
        
                     ``\"S\": \"Hello\"``  
        
                  - **N** *(string) --* 
        
                    An attribute of type Number. For example:
        
                     ``\"N\": \"123.45\"``  
        
                    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                  - **B** *(bytes) --* 
        
                    An attribute of type Binary. For example:
        
                     ``\"B\": \"dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk\"``  
        
                  - **SS** *(list) --* 
        
                    An attribute of type String Set. For example:
        
                     ``\"SS\": [\"Giraffe\", \"Hippo\" ,\"Zebra\"]``  
        
                    - *(string) --* 
        
                  - **NS** *(list) --* 
        
                    An attribute of type Number Set. For example:
        
                     ``\"NS\": [\"42.2\", \"-19\", \"7.5\", \"3.14\"]``  
        
                    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                    - *(string) --* 
        
                  - **BS** *(list) --* 
        
                    An attribute of type Binary Set. For example:
        
                     ``\"BS\": [\"U3Vubnk=\", \"UmFpbnk=\", \"U25vd3k=\"]``  
        
                    - *(bytes) --* 
        
                  - **M** *(dict) --* 
        
                    An attribute of type Map. For example:
        
                     ``\"M\": {\"Name\": {\"S\": \"Joe\"}, \"Age\": {\"N\": \"35\"}}``  
        
                    - *(string) --* 
        
                      - *(dict) --* 
        
                        Represents the data for an attribute.
        
                        Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                        For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **L** *(list) --* 
        
                    An attribute of type List. For example:
        
                     ``\"L\": [\"Cookies\", \"Coffee\", 3.14159]``  
        
                    - *(dict) --* 
        
                      Represents the data for an attribute.
        
                      Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                      For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **NULL** *(boolean) --* 
        
                    An attribute of type Null. For example:
        
                     ``\"NULL\": true``  
        
                  - **BOOL** *(boolean) --* 
        
                    An attribute of type Boolean. For example:
        
                     ``\"BOOL\": true``  
        
              - **ComparisonOperator** *(string) --* **[REQUIRED]** 
        
                A comparator for evaluating attributes. For example, equals, greater than, less than, etc.
        
                The following comparison operators are available:
        
                 ``EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN``  
        
                The following are descriptions of each comparison operator.
        
                * ``EQ`` : Equal. ``EQ`` is supported for all data types, including lists and maps.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not equal ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``NE`` : Not equal. ``NE`` is supported for all data types, including lists and maps.  ``AttributeValueList`` can contain only one ``AttributeValue`` of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an ``AttributeValue`` of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not equal ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``LE`` : Less than or equal.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``LT`` : Less than.   ``AttributeValueList`` can contain only one ``AttributeValue`` of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``GE`` : Greater than or equal.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``GT`` : Greater than.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``NOT_NULL`` : The attribute exists. ``NOT_NULL`` is supported for all data types, including lists and maps. 
        
                .. note::
        
                   This operator tests for the existence of an attribute, not its data type. If the data type of attribute \"``a`` \" is null, and you evaluate it using ``NOT_NULL`` , the result is a Boolean ``true`` . This result is because the attribute \"``a`` \" exists; its data type is not relevant to the ``NOT_NULL`` comparison operator. 
        
                * ``NULL`` : The attribute does not exist. ``NULL`` is supported for all data types, including lists and maps. 
        
                .. note::
        
                   This operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute \"``a`` \" is null, and you evaluate it using ``NULL`` , the result is a Boolean ``false`` . This is because the attribute \"``a`` \" exists; its data type is not relevant to the ``NULL`` comparison operator. 
        
                * ``CONTAINS`` : Checks for a subsequence, or value in a set.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set (\"``SS`` \", \"``NS`` \", or \"``BS`` \"), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating \"``a CONTAINS b`` \", \"``a`` \" can be a list; however, \"``b`` \" cannot be a set, a map, or a list. 
                 
                * ``NOT_CONTAINS`` : Checks for absence of a subsequence, or absence of a value in a set.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set (\"``SS`` \", \"``NS`` \", or \"``BS`` \"), then the operator evaluates to true if it *does not* find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating \"``a NOT CONTAINS b`` \", \"``a`` \" can be a list; however, \"``b`` \" cannot be a set, a map, or a list. 
                 
                * ``BEGINS_WITH`` : Checks for a prefix.   ``AttributeValueList`` can contain only one ``AttributeValue`` of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).  
                 
                * ``IN`` : Checks for matching elements in a list.  ``AttributeValueList`` can contain one or more ``AttributeValue`` elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true. 
                 
                * ``BETWEEN`` : Greater than or equal to the first value, and less than or equal to the second value.   ``AttributeValueList`` must contain two ``AttributeValue`` elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not compare to ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}``   
                 
                For usage examples of ``AttributeValueList`` and ``ComparisonOperator`` , see `Legacy Conditional Parameters <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type ConditionalOperator: string
        :param ConditionalOperator: 
        
          This is a legacy parameter. Use ``FilterExpression`` instead. For more information, see `ConditionalOperator <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type ScanIndexForward: boolean
        :param ScanIndexForward: 
        
          Specifies the order for index traversal: If ``true`` (default), the traversal is performed in ascending order; if ``false`` , the traversal is performed in descending order. 
        
          Items with the same partition key value are stored in sorted order by sort key. If the sort key data type is Number, the results are stored in numeric order. For type String, the results are stored in order of UTF-8 bytes. For type Binary, DynamoDB treats each byte of the binary data as unsigned.
        
          If ``ScanIndexForward`` is ``true`` , DynamoDB returns the results in the order in which they are stored (by sort key value). This is the default behavior. If ``ScanIndexForward`` is ``false`` , DynamoDB reads the results in reverse order by sort key value, and then returns the results to the client.
        
        :type ReturnConsumedCapacity: string
        :param ReturnConsumedCapacity: 
        
          Determines the level of detail about provisioned throughput consumption that is returned in the response:
        
          * ``INDEXES`` - The response includes the aggregate ``ConsumedCapacity`` for the operation, together with ``ConsumedCapacity`` for each table and secondary index that was accessed. Note that some operations, such as ``GetItem`` and ``BatchGetItem`` , do not access any indexes at all. In these cases, specifying ``INDEXES`` will only return ``ConsumedCapacity`` information for table(s). 
           
          * ``TOTAL`` - The response includes only the aggregate ``ConsumedCapacity`` for the operation. 
           
          * ``NONE`` - No ``ConsumedCapacity`` details are included in the response. 
           
        :type ProjectionExpression: string
        :param ProjectionExpression: 
        
          A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.
        
          If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.
        
          For more information, see `Accessing Item Attributes <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type FilterExpression: string
        :param FilterExpression: 
        
          A string that contains conditions that DynamoDB applies after the ``Query`` operation, but before the data is returned to you. Items that do not satisfy the ``FilterExpression`` criteria are not returned.
        
          A ``FilterExpression`` does not allow key attributes. You cannot define a filter expression based on a partition key or a sort key.
        
          .. note::
        
            A ``FilterExpression`` is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.
        
          For more information, see `Filter Expressions <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#FilteringResults>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type KeyConditionExpression: string
        :param KeyConditionExpression: 
        
          The condition that specifies the key value(s) for items to be retrieved by the ``Query`` action.
        
          The condition must perform an equality test on a single partition key value.
        
          The condition can optionally perform one of several comparison tests on a single sort key value. This allows ``Query`` to retrieve one item with a given partition key value and sort key value, or several items that have the same partition key value but different sort key values.
        
          The partition key equality test is required, and must be specified in the following format:
        
           ``partitionKeyName``  *=*  ``:partitionkeyval``  
        
          If you also want to provide a condition for the sort key, it must be combined using ``AND`` with the condition for the sort key. Following is an example, using the **=** comparison operator for the sort key:
        
           ``partitionKeyName``  ``=``  ``:partitionkeyval``  ``AND``  ``sortKeyName``  ``=``  ``:sortkeyval``  
        
          Valid comparisons for the sort key condition are as follows:
        
          * ``sortKeyName``  ``=``  ``:sortkeyval`` - true if the sort key value is equal to ``:sortkeyval`` . 
           
          * ``sortKeyName``  ``<``  ``:sortkeyval`` - true if the sort key value is less than ``:sortkeyval`` . 
           
          * ``sortKeyName``  ``<=``  ``:sortkeyval`` - true if the sort key value is less than or equal to ``:sortkeyval`` . 
           
          * ``sortKeyName``  ``>``  ``:sortkeyval`` - true if the sort key value is greater than ``:sortkeyval`` . 
           
          * ``sortKeyName``  ``>=``  ``:sortkeyval`` - true if the sort key value is greater than or equal to ``:sortkeyval`` . 
           
          * ``sortKeyName``  ``BETWEEN``  ``:sortkeyval1``  ``AND``  ``:sortkeyval2`` - true if the sort key value is greater than or equal to ``:sortkeyval1`` , and less than or equal to ``:sortkeyval2`` . 
           
          * ``begins_with (``  ``sortKeyName`` , ``:sortkeyval``  ``)`` - true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.) Note that the function name ``begins_with`` is case-sensitive. 
           
          Use the ``ExpressionAttributeValues`` parameter to replace tokens such as ``:partitionval`` and ``:sortval`` with actual values at runtime.
        
          You can optionally use the ``ExpressionAttributeNames`` parameter to replace the names of the partition key and sort key with placeholder tokens. This option might be necessary if an attribute name conflicts with a DynamoDB reserved word. For example, the following ``KeyConditionExpression`` parameter causes an error because *Size* is a reserved word:
        
          * ``Size = :myval``   
           
          To work around this, define a placeholder (such a ``#S`` ) to represent the attribute name *Size* . ``KeyConditionExpression`` then is as follows:
        
          * ``#S = :myval``   
           
          For a list of reserved words, see `Reserved Words <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          For more information on ``ExpressionAttributeNames`` and ``ExpressionAttributeValues`` , see `Using Placeholders for Attribute Names and Values <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ExpressionPlaceholders.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type ExpressionAttributeNames: dict
        :param ExpressionAttributeNames: 
        
          One or more substitution tokens for attribute names in an expression. The following are some use cases for using ``ExpressionAttributeNames`` :
        
          * To access an attribute whose name conflicts with a DynamoDB reserved word. 
           
          * To create a placeholder for repeating occurrences of an attribute name in an expression. 
           
          * To prevent special characters in an attribute name from being misinterpreted in an expression. 
           
          Use the **#** character in an expression to dereference an attribute name. For example, consider the following attribute name:
        
          * ``Percentile``   
           
          The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see `Reserved Words <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html>`__ in the *Amazon DynamoDB Developer Guide* ). To work around this, you could specify the following for ``ExpressionAttributeNames`` :
        
          * ``{\"#P\":\"Percentile\"}``   
           
          You could then use this substitution in an expression, as in this example:
        
          * ``#P = :val``   
           
          .. note::
        
            Tokens that begin with the **:** character are *expression attribute values* , which are placeholders for the actual value at runtime.
        
          For more information on expression attribute names, see `Accessing Item Attributes <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type ExpressionAttributeValues: dict
        :param ExpressionAttributeValues: 
        
          One or more values that can be substituted in an expression.
        
          Use the **:** (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the *ProductStatus* attribute was one of the following: 
        
           ``Available | Backordered | Discontinued``  
        
          You would first need to specify ``ExpressionAttributeValues`` as follows:
        
           ``{ \":avail\":{\"S\":\"Available\"}, \":back\":{\"S\":\"Backordered\"}, \":disc\":{\"S\":\"Discontinued\"} }``  
        
          You could then use these values in an expression, such as this:
        
           ``ProductStatus IN (:avail, :back, :disc)``  
        
          For more information on expression attribute values, see `Specifying Conditions <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
            - *(dict) --* 
        
              Represents the data for an attribute.
        
              Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
              For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
              - **S** *(string) --* 
        
                An attribute of type String. For example:
        
                 ``\"S\": \"Hello\"``  
        
              - **N** *(string) --* 
        
                An attribute of type Number. For example:
        
                 ``\"N\": \"123.45\"``  
        
                Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
              - **B** *(bytes) --* 
        
                An attribute of type Binary. For example:
        
                 ``\"B\": \"dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk\"``  
        
              - **SS** *(list) --* 
        
                An attribute of type String Set. For example:
        
                 ``\"SS\": [\"Giraffe\", \"Hippo\" ,\"Zebra\"]``  
        
                - *(string) --* 
        
              - **NS** *(list) --* 
        
                An attribute of type Number Set. For example:
        
                 ``\"NS\": [\"42.2\", \"-19\", \"7.5\", \"3.14\"]``  
        
                Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                - *(string) --* 
        
              - **BS** *(list) --* 
        
                An attribute of type Binary Set. For example:
        
                 ``\"BS\": [\"U3Vubnk=\", \"UmFpbnk=\", \"U25vd3k=\"]``  
        
                - *(bytes) --* 
        
              - **M** *(dict) --* 
        
                An attribute of type Map. For example:
        
                 ``\"M\": {\"Name\": {\"S\": \"Joe\"}, \"Age\": {\"N\": \"35\"}}``  
        
                - *(string) --* 
        
                  - *(dict) --* 
        
                    Represents the data for an attribute.
        
                    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                    For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
              - **L** *(list) --* 
        
                An attribute of type List. For example:
        
                 ``\"L\": [\"Cookies\", \"Coffee\", 3.14159]``  
        
                - *(dict) --* 
        
                  Represents the data for an attribute.
        
                  Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                  For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
              - **NULL** *(boolean) --* 
        
                An attribute of type Null. For example:
        
                 ``\"NULL\": true``  
        
              - **BOOL** *(boolean) --* 
        
                An attribute of type Boolean. For example:
        
                 ``\"BOOL\": true``  
        
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
                \'Items\': [
                    {
                        \'string\': {
                            \'S\': \'string\',
                            \'N\': \'string\',
                            \'B\': b\'bytes\',
                            \'SS\': [
                                \'string\',
                            ],
                            \'NS\': [
                                \'string\',
                            ],
                            \'BS\': [
                                b\'bytes\',
                            ],
                            \'M\': {
                                \'string\': {\'... recursive ...\'}
                            },
                            \'L\': [
                                {\'... recursive ...\'},
                            ],
                            \'NULL\': True|False,
                            \'BOOL\': True|False
                        }
                    },
                ],
                \'Count\': 123,
                \'ScannedCount\': 123,
                \'ConsumedCapacity\': {
                    \'TableName\': \'string\',
                    \'CapacityUnits\': 123.0,
                    \'Table\': {
                        \'CapacityUnits\': 123.0
                    },
                    \'LocalSecondaryIndexes\': {
                        \'string\': {
                            \'CapacityUnits\': 123.0
                        }
                    },
                    \'GlobalSecondaryIndexes\': {
                        \'string\': {
                            \'CapacityUnits\': 123.0
                        }
                    }
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``Query`` operation.
        
            - **Items** *(list) --* 
        
              An array of item attributes that match the query criteria. Each element in this array consists of an attribute name and the value for that attribute.
        
              - *(dict) --* 
                
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    Represents the data for an attribute.
        
                    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                    For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                    - **S** *(string) --* 
        
                      An attribute of type String. For example:
        
                       ``\"S\": \"Hello\"``  
        
                    - **N** *(string) --* 
        
                      An attribute of type Number. For example:
        
                       ``\"N\": \"123.45\"``  
        
                      Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                    - **B** *(bytes) --* 
        
                      An attribute of type Binary. For example:
        
                       ``\"B\": \"dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk\"``  
        
                    - **SS** *(list) --* 
        
                      An attribute of type String Set. For example:
        
                       ``\"SS\": [\"Giraffe\", \"Hippo\" ,\"Zebra\"]``  
        
                      - *(string) --* 
                  
                    - **NS** *(list) --* 
        
                      An attribute of type Number Set. For example:
        
                       ``\"NS\": [\"42.2\", \"-19\", \"7.5\", \"3.14\"]``  
        
                      Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                      - *(string) --* 
                  
                    - **BS** *(list) --* 
        
                      An attribute of type Binary Set. For example:
        
                       ``\"BS\": [\"U3Vubnk=\", \"UmFpbnk=\", \"U25vd3k=\"]``  
        
                      - *(bytes) --* 
                  
                    - **M** *(dict) --* 
        
                      An attribute of type Map. For example:
        
                       ``\"M\": {\"Name\": {\"S\": \"Joe\"}, \"Age\": {\"N\": \"35\"}}``  
        
                      - *(string) --* 
                        
                        - *(dict) --* 
        
                          Represents the data for an attribute.
        
                          Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                          For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                    - **L** *(list) --* 
        
                      An attribute of type List. For example:
        
                       ``\"L\": [\"Cookies\", \"Coffee\", 3.14159]``  
        
                      - *(dict) --* 
        
                        Represents the data for an attribute.
        
                        Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                        For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                    - **NULL** *(boolean) --* 
        
                      An attribute of type Null. For example:
        
                       ``\"NULL\": true``  
        
                    - **BOOL** *(boolean) --* 
        
                      An attribute of type Boolean. For example:
        
                       ``\"BOOL\": true``  
        
            - **Count** *(integer) --* 
        
              The number of items in the response.
        
              If you used a ``QueryFilter`` in the request, then ``Count`` is the number of items returned after the filter was applied, and ``ScannedCount`` is the number of matching items before the filter was applied.
        
              If you did not use a filter in the request, then ``Count`` and ``ScannedCount`` are the same.
        
            - **ScannedCount** *(integer) --* 
        
              The number of items evaluated, before any ``QueryFilter`` is applied. A high ``ScannedCount`` value with few, or no, ``Count`` results indicates an inefficient ``Query`` operation. For more information, see `Count and ScannedCount <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#Count>`__ in the *Amazon DynamoDB Developer Guide* .
        
              If you did not use a filter in the request, then ``ScannedCount`` is the same as ``Count`` .
        
            - **ConsumedCapacity** *(dict) --* 
        
              The capacity units consumed by the ``Query`` operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ``ConsumedCapacity`` is only returned if the ``ReturnConsumedCapacity`` parameter was specified For more information, see `Provisioned Throughput <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
              - **TableName** *(string) --* 
        
                The name of the table that was affected by the operation.
        
              - **CapacityUnits** *(float) --* 
        
                The total number of capacity units consumed by the operation.
        
              - **Table** *(dict) --* 
        
                The amount of throughput consumed on the table affected by the operation.
        
                - **CapacityUnits** *(float) --* 
        
                  The total number of capacity units consumed on a table or an index.
        
              - **LocalSecondaryIndexes** *(dict) --* 
        
                The amount of throughput consumed on each local index affected by the operation.
        
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    Represents the amount of provisioned throughput capacity consumed on a table or an index.
        
                    - **CapacityUnits** *(float) --* 
        
                      The total number of capacity units consumed on a table or an index.
        
              - **GlobalSecondaryIndexes** *(dict) --* 
        
                The amount of throughput consumed on each global index affected by the operation.
        
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    Represents the amount of provisioned throughput capacity consumed on a table or an index.
        
                    - **CapacityUnits** *(float) --* 
        
                      The total number of capacity units consumed on a table or an index.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class Scan(Paginator):
    def paginate(self, TableName: str, IndexName: str = None, AttributesToGet: List = None, Select: str = None, ScanFilter: Dict = None, ConditionalOperator: str = None, ReturnConsumedCapacity: str = None, TotalSegments: int = None, Segment: int = None, ProjectionExpression: str = None, FilterExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, ConsistentRead: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/Scan>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              TableName=\'string\',
              IndexName=\'string\',
              AttributesToGet=[
                  \'string\',
              ],
              Select=\'ALL_ATTRIBUTES\'|\'ALL_PROJECTED_ATTRIBUTES\'|\'SPECIFIC_ATTRIBUTES\'|\'COUNT\',
              ScanFilter={
                  \'string\': {
                      \'AttributeValueList\': [
                          {
                              \'S\': \'string\',
                              \'N\': \'string\',
                              \'B\': b\'bytes\',
                              \'SS\': [
                                  \'string\',
                              ],
                              \'NS\': [
                                  \'string\',
                              ],
                              \'BS\': [
                                  b\'bytes\',
                              ],
                              \'M\': {
                                  \'string\': {\'... recursive ...\'}
                              },
                              \'L\': [
                                  {\'... recursive ...\'},
                              ],
                              \'NULL\': True|False,
                              \'BOOL\': True|False
                          },
                      ],
                      \'ComparisonOperator\': \'EQ\'|\'NE\'|\'IN\'|\'LE\'|\'LT\'|\'GE\'|\'GT\'|\'BETWEEN\'|\'NOT_NULL\'|\'NULL\'|\'CONTAINS\'|\'NOT_CONTAINS\'|\'BEGINS_WITH\'
                  }
              },
              ConditionalOperator=\'AND\'|\'OR\',
              ReturnConsumedCapacity=\'INDEXES\'|\'TOTAL\'|\'NONE\',
              TotalSegments=123,
              Segment=123,
              ProjectionExpression=\'string\',
              FilterExpression=\'string\',
              ExpressionAttributeNames={
                  \'string\': \'string\'
              },
              ExpressionAttributeValues={
                  \'string\': {
                      \'S\': \'string\',
                      \'N\': \'string\',
                      \'B\': b\'bytes\',
                      \'SS\': [
                          \'string\',
                      ],
                      \'NS\': [
                          \'string\',
                      ],
                      \'BS\': [
                          b\'bytes\',
                      ],
                      \'M\': {
                          \'string\': {\'... recursive ...\'}
                      },
                      \'L\': [
                          {\'... recursive ...\'},
                      ],
                      \'NULL\': True|False,
                      \'BOOL\': True|False
                  }
              },
              ConsistentRead=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type TableName: string
        :param TableName: **[REQUIRED]** 
        
          The name of the table containing the requested items; or, if you provide ``IndexName`` , the name of the table to which that index belongs.
        
        :type IndexName: string
        :param IndexName: 
        
          The name of a secondary index to scan. This index can be any local secondary index or global secondary index. Note that if you use the ``IndexName`` parameter, you must also provide ``TableName`` .
        
        :type AttributesToGet: list
        :param AttributesToGet: 
        
          This is a legacy parameter. Use ``ProjectionExpression`` instead. For more information, see `AttributesToGet <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
        :type Select: string
        :param Select: 
        
          The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.
        
          * ``ALL_ATTRIBUTES`` - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required. 
           
          * ``ALL_PROJECTED_ATTRIBUTES`` - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying ``ALL_ATTRIBUTES`` . 
           
          * ``COUNT`` - Returns the number of matching items, rather than the matching items themselves. 
           
          * ``SPECIFIC_ATTRIBUTES`` - Returns only the attributes listed in ``AttributesToGet`` . This return value is equivalent to specifying ``AttributesToGet`` without specifying any value for ``Select`` . If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB will fetch each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table. 
           
          If neither ``Select`` nor ``AttributesToGet`` are specified, DynamoDB defaults to ``ALL_ATTRIBUTES`` when accessing a table, and ``ALL_PROJECTED_ATTRIBUTES`` when accessing an index. You cannot use both ``Select`` and ``AttributesToGet`` together in a single request, unless the value for ``Select`` is ``SPECIFIC_ATTRIBUTES`` . (This usage is equivalent to specifying ``AttributesToGet`` without any value for ``Select`` .)
        
          .. note::
        
            If you use the ``ProjectionExpression`` parameter, then the value for ``Select`` can only be ``SPECIFIC_ATTRIBUTES`` . Any other value for ``Select`` will return an error.
        
        :type ScanFilter: dict
        :param ScanFilter: 
        
          This is a legacy parameter. Use ``FilterExpression`` instead. For more information, see `ScanFilter <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ScanFilter.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
            - *(dict) --* 
        
              Represents the selection criteria for a ``Query`` or ``Scan`` operation:
        
              * For a ``Query`` operation, ``Condition`` is used for specifying the ``KeyConditions`` to use when querying a table or an index. For ``KeyConditions`` , only the following comparison operators are supported:  ``EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN``    ``Condition`` is also used in a ``QueryFilter`` , which evaluates the query results and returns only the desired values. 
               
              * For a ``Scan`` operation, ``Condition`` is used in a ``ScanFilter`` , which evaluates the scan results and returns only the desired values. 
               
              - **AttributeValueList** *(list) --* 
        
                One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ``ComparisonOperator`` being used.
        
                For type Number, value comparisons are numeric.
        
                String value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, ``a`` is greater than ``A`` , and ``a`` is greater than ``B`` . For a list of code values, see `http\://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .
        
                For Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.
        
                - *(dict) --* 
        
                  Represents the data for an attribute.
        
                  Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                  For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **S** *(string) --* 
        
                    An attribute of type String. For example:
        
                     ``\"S\": \"Hello\"``  
        
                  - **N** *(string) --* 
        
                    An attribute of type Number. For example:
        
                     ``\"N\": \"123.45\"``  
        
                    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                  - **B** *(bytes) --* 
        
                    An attribute of type Binary. For example:
        
                     ``\"B\": \"dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk\"``  
        
                  - **SS** *(list) --* 
        
                    An attribute of type String Set. For example:
        
                     ``\"SS\": [\"Giraffe\", \"Hippo\" ,\"Zebra\"]``  
        
                    - *(string) --* 
        
                  - **NS** *(list) --* 
        
                    An attribute of type Number Set. For example:
        
                     ``\"NS\": [\"42.2\", \"-19\", \"7.5\", \"3.14\"]``  
        
                    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                    - *(string) --* 
        
                  - **BS** *(list) --* 
        
                    An attribute of type Binary Set. For example:
        
                     ``\"BS\": [\"U3Vubnk=\", \"UmFpbnk=\", \"U25vd3k=\"]``  
        
                    - *(bytes) --* 
        
                  - **M** *(dict) --* 
        
                    An attribute of type Map. For example:
        
                     ``\"M\": {\"Name\": {\"S\": \"Joe\"}, \"Age\": {\"N\": \"35\"}}``  
        
                    - *(string) --* 
        
                      - *(dict) --* 
        
                        Represents the data for an attribute.
        
                        Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                        For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **L** *(list) --* 
        
                    An attribute of type List. For example:
        
                     ``\"L\": [\"Cookies\", \"Coffee\", 3.14159]``  
        
                    - *(dict) --* 
        
                      Represents the data for an attribute.
        
                      Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                      For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                  - **NULL** *(boolean) --* 
        
                    An attribute of type Null. For example:
        
                     ``\"NULL\": true``  
        
                  - **BOOL** *(boolean) --* 
        
                    An attribute of type Boolean. For example:
        
                     ``\"BOOL\": true``  
        
              - **ComparisonOperator** *(string) --* **[REQUIRED]** 
        
                A comparator for evaluating attributes. For example, equals, greater than, less than, etc.
        
                The following comparison operators are available:
        
                 ``EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN``  
        
                The following are descriptions of each comparison operator.
        
                * ``EQ`` : Equal. ``EQ`` is supported for all data types, including lists and maps.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not equal ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``NE`` : Not equal. ``NE`` is supported for all data types, including lists and maps.  ``AttributeValueList`` can contain only one ``AttributeValue`` of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an ``AttributeValue`` of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not equal ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``LE`` : Less than or equal.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``LT`` : Less than.   ``AttributeValueList`` can contain only one ``AttributeValue`` of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``GE`` : Greater than or equal.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``GT`` : Greater than.   ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not equal ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}`` .  
                 
                * ``NOT_NULL`` : The attribute exists. ``NOT_NULL`` is supported for all data types, including lists and maps. 
        
                .. note::
        
                   This operator tests for the existence of an attribute, not its data type. If the data type of attribute \"``a`` \" is null, and you evaluate it using ``NOT_NULL`` , the result is a Boolean ``true`` . This result is because the attribute \"``a`` \" exists; its data type is not relevant to the ``NOT_NULL`` comparison operator. 
        
                * ``NULL`` : The attribute does not exist. ``NULL`` is supported for all data types, including lists and maps. 
        
                .. note::
        
                   This operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute \"``a`` \" is null, and you evaluate it using ``NULL`` , the result is a Boolean ``false`` . This is because the attribute \"``a`` \" exists; its data type is not relevant to the ``NULL`` comparison operator. 
        
                * ``CONTAINS`` : Checks for a subsequence, or value in a set.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set (\"``SS`` \", \"``NS`` \", or \"``BS`` \"), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating \"``a CONTAINS b`` \", \"``a`` \" can be a list; however, \"``b`` \" cannot be a set, a map, or a list. 
                 
                * ``NOT_CONTAINS`` : Checks for absence of a subsequence, or absence of a value in a set.  ``AttributeValueList`` can contain only one ``AttributeValue`` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set (\"``SS`` \", \"``NS`` \", or \"``BS`` \"), then the operator evaluates to true if it *does not* find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating \"``a NOT CONTAINS b`` \", \"``a`` \" can be a list; however, \"``b`` \" cannot be a set, a map, or a list. 
                 
                * ``BEGINS_WITH`` : Checks for a prefix.   ``AttributeValueList`` can contain only one ``AttributeValue`` of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).  
                 
                * ``IN`` : Checks for matching elements in a list.  ``AttributeValueList`` can contain one or more ``AttributeValue`` elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true. 
                 
                * ``BETWEEN`` : Greater than or equal to the first value, and less than or equal to the second value.   ``AttributeValueList`` must contain two ``AttributeValue`` elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an ``AttributeValue`` element of a different type than the one provided in the request, the value does not match. For example, ``{\"S\":\"6\"}`` does not compare to ``{\"N\":\"6\"}`` . Also, ``{\"N\":\"6\"}`` does not compare to ``{\"NS\":[\"6\", \"2\", \"1\"]}``   
                 
                For usage examples of ``AttributeValueList`` and ``ComparisonOperator`` , see `Legacy Conditional Parameters <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type ConditionalOperator: string
        :param ConditionalOperator: 
        
          This is a legacy parameter. Use ``FilterExpression`` instead. For more information, see `ConditionalOperator <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type ReturnConsumedCapacity: string
        :param ReturnConsumedCapacity: 
        
          Determines the level of detail about provisioned throughput consumption that is returned in the response:
        
          * ``INDEXES`` - The response includes the aggregate ``ConsumedCapacity`` for the operation, together with ``ConsumedCapacity`` for each table and secondary index that was accessed. Note that some operations, such as ``GetItem`` and ``BatchGetItem`` , do not access any indexes at all. In these cases, specifying ``INDEXES`` will only return ``ConsumedCapacity`` information for table(s). 
           
          * ``TOTAL`` - The response includes only the aggregate ``ConsumedCapacity`` for the operation. 
           
          * ``NONE`` - No ``ConsumedCapacity`` details are included in the response. 
           
        :type TotalSegments: integer
        :param TotalSegments: 
        
          For a parallel ``Scan`` request, ``TotalSegments`` represents the total number of segments into which the ``Scan`` operation will be divided. The value of ``TotalSegments`` corresponds to the number of application workers that will perform the parallel scan. For example, if you want to use four application threads to scan a table or an index, specify a ``TotalSegments`` value of 4.
        
          The value for ``TotalSegments`` must be greater than or equal to 1, and less than or equal to 1000000. If you specify a ``TotalSegments`` value of 1, the ``Scan`` operation will be sequential rather than parallel.
        
          If you specify ``TotalSegments`` , you must also specify ``Segment`` .
        
        :type Segment: integer
        :param Segment: 
        
          For a parallel ``Scan`` request, ``Segment`` identifies an individual segment to be scanned by an application worker.
        
          Segment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to scan a table or an index, then the first thread specifies a ``Segment`` value of 0, the second thread specifies 1, and so on.
        
          The value of ``LastEvaluatedKey`` returned from a parallel ``Scan`` request must be used as ``ExclusiveStartKey`` with the same segment ID in a subsequent ``Scan`` operation.
        
          The value for ``Segment`` must be greater than or equal to 0, and less than the value provided for ``TotalSegments`` .
        
          If you provide ``Segment`` , you must also provide ``TotalSegments`` .
        
        :type ProjectionExpression: string
        :param ProjectionExpression: 
        
          A string that identifies one or more attributes to retrieve from the specified table or index. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.
        
          If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.
        
          For more information, see `Accessing Item Attributes <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type FilterExpression: string
        :param FilterExpression: 
        
          A string that contains conditions that DynamoDB applies after the ``Scan`` operation, but before the data is returned to you. Items that do not satisfy the ``FilterExpression`` criteria are not returned.
        
          .. note::
        
            A ``FilterExpression`` is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.
        
          For more information, see `Filter Expressions <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#FilteringResults>`__ in the *Amazon DynamoDB Developer Guide* .
        
        :type ExpressionAttributeNames: dict
        :param ExpressionAttributeNames: 
        
          One or more substitution tokens for attribute names in an expression. The following are some use cases for using ``ExpressionAttributeNames`` :
        
          * To access an attribute whose name conflicts with a DynamoDB reserved word. 
           
          * To create a placeholder for repeating occurrences of an attribute name in an expression. 
           
          * To prevent special characters in an attribute name from being misinterpreted in an expression. 
           
          Use the **#** character in an expression to dereference an attribute name. For example, consider the following attribute name:
        
          * ``Percentile``   
           
          The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see `Reserved Words <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html>`__ in the *Amazon DynamoDB Developer Guide* ). To work around this, you could specify the following for ``ExpressionAttributeNames`` :
        
          * ``{\"#P\":\"Percentile\"}``   
           
          You could then use this substitution in an expression, as in this example:
        
          * ``#P = :val``   
           
          .. note::
        
            Tokens that begin with the **:** character are *expression attribute values* , which are placeholders for the actual value at runtime.
        
          For more information on expression attribute names, see `Accessing Item Attributes <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type ExpressionAttributeValues: dict
        :param ExpressionAttributeValues: 
        
          One or more values that can be substituted in an expression.
        
          Use the **:** (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the *ProductStatus* attribute was one of the following: 
        
           ``Available | Backordered | Discontinued``  
        
          You would first need to specify ``ExpressionAttributeValues`` as follows:
        
           ``{ \":avail\":{\"S\":\"Available\"}, \":back\":{\"S\":\"Backordered\"}, \":disc\":{\"S\":\"Discontinued\"} }``  
        
          You could then use these values in an expression, such as this:
        
           ``ProductStatus IN (:avail, :back, :disc)``  
        
          For more information on expression attribute values, see `Specifying Conditions <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
          - *(string) --* 
        
            - *(dict) --* 
        
              Represents the data for an attribute.
        
              Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
              For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
              - **S** *(string) --* 
        
                An attribute of type String. For example:
        
                 ``\"S\": \"Hello\"``  
        
              - **N** *(string) --* 
        
                An attribute of type Number. For example:
        
                 ``\"N\": \"123.45\"``  
        
                Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
              - **B** *(bytes) --* 
        
                An attribute of type Binary. For example:
        
                 ``\"B\": \"dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk\"``  
        
              - **SS** *(list) --* 
        
                An attribute of type String Set. For example:
        
                 ``\"SS\": [\"Giraffe\", \"Hippo\" ,\"Zebra\"]``  
        
                - *(string) --* 
        
              - **NS** *(list) --* 
        
                An attribute of type Number Set. For example:
        
                 ``\"NS\": [\"42.2\", \"-19\", \"7.5\", \"3.14\"]``  
        
                Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                - *(string) --* 
        
              - **BS** *(list) --* 
        
                An attribute of type Binary Set. For example:
        
                 ``\"BS\": [\"U3Vubnk=\", \"UmFpbnk=\", \"U25vd3k=\"]``  
        
                - *(bytes) --* 
        
              - **M** *(dict) --* 
        
                An attribute of type Map. For example:
        
                 ``\"M\": {\"Name\": {\"S\": \"Joe\"}, \"Age\": {\"N\": \"35\"}}``  
        
                - *(string) --* 
        
                  - *(dict) --* 
        
                    Represents the data for an attribute.
        
                    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                    For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
              - **L** *(list) --* 
        
                An attribute of type List. For example:
        
                 ``\"L\": [\"Cookies\", \"Coffee\", 3.14159]``  
        
                - *(dict) --* 
        
                  Represents the data for an attribute.
        
                  Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                  For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
              - **NULL** *(boolean) --* 
        
                An attribute of type Null. For example:
        
                 ``\"NULL\": true``  
        
              - **BOOL** *(boolean) --* 
        
                An attribute of type Boolean. For example:
        
                 ``\"BOOL\": true``  
        
        :type ConsistentRead: boolean
        :param ConsistentRead: 
        
          A Boolean value that determines the read consistency model during the scan:
        
          * If ``ConsistentRead`` is ``false`` , then the data returned from ``Scan`` might not contain the results from other recently completed write operations (PutItem, UpdateItem or DeleteItem). 
           
          * If ``ConsistentRead`` is ``true`` , then all of the write operations that completed before the ``Scan`` began are guaranteed to be contained in the ``Scan`` response. 
           
          The default setting for ``ConsistentRead`` is ``false`` .
        
          The ``ConsistentRead`` parameter is not supported on global secondary indexes. If you scan a global secondary index with ``ConsistentRead`` set to true, you will receive a ``ValidationException`` .
        
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
                \'Items\': [
                    {
                        \'string\': {
                            \'S\': \'string\',
                            \'N\': \'string\',
                            \'B\': b\'bytes\',
                            \'SS\': [
                                \'string\',
                            ],
                            \'NS\': [
                                \'string\',
                            ],
                            \'BS\': [
                                b\'bytes\',
                            ],
                            \'M\': {
                                \'string\': {\'... recursive ...\'}
                            },
                            \'L\': [
                                {\'... recursive ...\'},
                            ],
                            \'NULL\': True|False,
                            \'BOOL\': True|False
                        }
                    },
                ],
                \'Count\': 123,
                \'ScannedCount\': 123,
                \'ConsumedCapacity\': {
                    \'TableName\': \'string\',
                    \'CapacityUnits\': 123.0,
                    \'Table\': {
                        \'CapacityUnits\': 123.0
                    },
                    \'LocalSecondaryIndexes\': {
                        \'string\': {
                            \'CapacityUnits\': 123.0
                        }
                    },
                    \'GlobalSecondaryIndexes\': {
                        \'string\': {
                            \'CapacityUnits\': 123.0
                        }
                    }
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``Scan`` operation.
        
            - **Items** *(list) --* 
        
              An array of item attributes that match the scan criteria. Each element in this array consists of an attribute name and the value for that attribute.
        
              - *(dict) --* 
                
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    Represents the data for an attribute.
        
                    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                    For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                    - **S** *(string) --* 
        
                      An attribute of type String. For example:
        
                       ``\"S\": \"Hello\"``  
        
                    - **N** *(string) --* 
        
                      An attribute of type Number. For example:
        
                       ``\"N\": \"123.45\"``  
        
                      Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                    - **B** *(bytes) --* 
        
                      An attribute of type Binary. For example:
        
                       ``\"B\": \"dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk\"``  
        
                    - **SS** *(list) --* 
        
                      An attribute of type String Set. For example:
        
                       ``\"SS\": [\"Giraffe\", \"Hippo\" ,\"Zebra\"]``  
        
                      - *(string) --* 
                  
                    - **NS** *(list) --* 
        
                      An attribute of type Number Set. For example:
        
                       ``\"NS\": [\"42.2\", \"-19\", \"7.5\", \"3.14\"]``  
        
                      Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
        
                      - *(string) --* 
                  
                    - **BS** *(list) --* 
        
                      An attribute of type Binary Set. For example:
        
                       ``\"BS\": [\"U3Vubnk=\", \"UmFpbnk=\", \"U25vd3k=\"]``  
        
                      - *(bytes) --* 
                  
                    - **M** *(dict) --* 
        
                      An attribute of type Map. For example:
        
                       ``\"M\": {\"Name\": {\"S\": \"Joe\"}, \"Age\": {\"N\": \"35\"}}``  
        
                      - *(string) --* 
                        
                        - *(dict) --* 
        
                          Represents the data for an attribute.
        
                          Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                          For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                    - **L** *(list) --* 
        
                      An attribute of type List. For example:
        
                       ``\"L\": [\"Cookies\", \"Coffee\", 3.14159]``  
        
                      - *(dict) --* 
        
                        Represents the data for an attribute.
        
                        Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
        
                        For more information, see `Data Types <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>`__ in the *Amazon DynamoDB Developer Guide* .
        
                    - **NULL** *(boolean) --* 
        
                      An attribute of type Null. For example:
        
                       ``\"NULL\": true``  
        
                    - **BOOL** *(boolean) --* 
        
                      An attribute of type Boolean. For example:
        
                       ``\"BOOL\": true``  
        
            - **Count** *(integer) --* 
        
              The number of items in the response.
        
              If you set ``ScanFilter`` in the request, then ``Count`` is the number of items returned after the filter was applied, and ``ScannedCount`` is the number of matching items before the filter was applied.
        
              If you did not use a filter in the request, then ``Count`` is the same as ``ScannedCount`` .
        
            - **ScannedCount** *(integer) --* 
        
              The number of items evaluated, before any ``ScanFilter`` is applied. A high ``ScannedCount`` value with few, or no, ``Count`` results indicates an inefficient ``Scan`` operation. For more information, see `Count and ScannedCount <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#Count>`__ in the *Amazon DynamoDB Developer Guide* .
        
              If you did not use a filter in the request, then ``ScannedCount`` is the same as ``Count`` .
        
            - **ConsumedCapacity** *(dict) --* 
        
              The capacity units consumed by the ``Scan`` operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ``ConsumedCapacity`` is only returned if the ``ReturnConsumedCapacity`` parameter was specified. For more information, see `Provisioned Throughput <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html>`__ in the *Amazon DynamoDB Developer Guide* .
        
              - **TableName** *(string) --* 
        
                The name of the table that was affected by the operation.
        
              - **CapacityUnits** *(float) --* 
        
                The total number of capacity units consumed by the operation.
        
              - **Table** *(dict) --* 
        
                The amount of throughput consumed on the table affected by the operation.
        
                - **CapacityUnits** *(float) --* 
        
                  The total number of capacity units consumed on a table or an index.
        
              - **LocalSecondaryIndexes** *(dict) --* 
        
                The amount of throughput consumed on each local index affected by the operation.
        
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    Represents the amount of provisioned throughput capacity consumed on a table or an index.
        
                    - **CapacityUnits** *(float) --* 
        
                      The total number of capacity units consumed on a table or an index.
        
              - **GlobalSecondaryIndexes** *(dict) --* 
        
                The amount of throughput consumed on each global index affected by the operation.
        
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    Represents the amount of provisioned throughput capacity consumed on a table or an index.
        
                    - **CapacityUnits** *(float) --* 
        
                      The total number of capacity units consumed on a table or an index.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
