from typing import Optional
from botocore.client import BaseClient
from botocore.waiter import Waiter
from typing import Union
from typing import Dict
from botocore.paginate import Paginator


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
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

    def execute_sql(self, awsSecretStoreArn: str, dbClusterOrInstanceArn: str, sqlStatements: str, database: str = None, schema: str = None) -> Dict:
        """
        Executes any SQL statement on the target database synchronously
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-data-2018-08-01/ExecuteSql>`_
        
        **Request Syntax**
        ::
          response = client.execute_sql(
              awsSecretStoreArn='string',
              database='string',
              dbClusterOrInstanceArn='string',
              schema='string',
              sqlStatements='string'
          )
        
        **Response Syntax**
        ::
            {
                'sqlStatementResults': [
                    {
                        'numberOfRecordsUpdated': 123,
                        'resultFrame': {
                            'records': [
                                {
                                    'values': [
                                        {
                                            'arrayValues': [
                                                {'... recursive ...'},
                                            ],
                                            'bigIntValue': 123,
                                            'bitValue': True|False,
                                            'blobValue': b'bytes',
                                            'doubleValue': 123.0,
                                            'intValue': 123,
                                            'isNull': True|False,
                                            'realValue': ...,
                                            'stringValue': 'string',
                                            'structValue': {
                                                'attributes': [
                                                    {'... recursive ...'},
                                                ]
                                            }
                                        },
                                    ]
                                },
                            ],
                            'resultSetMetadata': {
                                'columnCount': 123,
                                'columnMetadata': [
                                    {
                                        'arrayBaseColumnType': 123,
                                        'isAutoIncrement': True|False,
                                        'isCaseSensitive': True|False,
                                        'isCurrency': True|False,
                                        'isSigned': True|False,
                                        'label': 'string',
                                        'name': 'string',
                                        'nullable': 123,
                                        'precision': 123,
                                        'scale': 123,
                                        'schemaName': 'string',
                                        'tableName': 'string',
                                        'type': 123,
                                        'typeName': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* Execute SQL response
            - **sqlStatementResults** *(list) --* Results returned by executing the sql statement(s)
              - *(dict) --* SQL statement execution result
                - **numberOfRecordsUpdated** *(integer) --* Number of rows updated.
                - **resultFrame** *(dict) --* ResultFrame returned by executing the sql statement
                  - **records** *(list) --* ResultSet Metadata.
                    - *(dict) --* Row or Record
                      - **values** *(list) --* Record
                        - *(dict) --* Column value
                          - **arrayValues** *(list) --* Arbitrarily nested arrays
                            - *(dict) --* Column value
                          - **bigIntValue** *(integer) --* Long value
                          - **bitValue** *(boolean) --* Bit value
                          - **blobValue** *(bytes) --* Blob value
                          - **doubleValue** *(float) --* Double value
                          - **intValue** *(integer) --* Integer value
                          - **isNull** *(boolean) --* Is column null
                          - **realValue** *(float) --* Float value
                          - **stringValue** *(string) --* String value
                          - **structValue** *(dict) --* Struct or UDT
                            - **attributes** *(list) --* Struct or UDT
                              - *(dict) --* Column value
                  - **resultSetMetadata** *(dict) --* ResultSet Metadata.
                    - **columnCount** *(integer) --* Number of columns
                    - **columnMetadata** *(list) --* List of columns and their types
                      - *(dict) --* Column Metadata
                        - **arrayBaseColumnType** *(integer) --* Homogenous array base SQL type from java.sql.Types.
                        - **isAutoIncrement** *(boolean) --* Whether the designated column is automatically numbered
                        - **isCaseSensitive** *(boolean) --* Whether values in the designated column's case matters
                        - **isCurrency** *(boolean) --* Whether values in the designated column is a cash value
                        - **isSigned** *(boolean) --* Whether values in the designated column are signed numbers
                        - **label** *(string) --* Usually specified by the SQL AS. If not specified, return column name.
                        - **name** *(string) --* Name of the column.
                        - **nullable** *(integer) --* Indicates the nullability of values in the designated column. One of columnNoNulls (0), columnNullable (1), columnNullableUnknown (2)
                        - **precision** *(integer) --* Get the designated column's specified column size.For numeric data, this is the maximum precision. For character data, this is the length in characters. For datetime datatypes, this is the length in characters of the String representation (assuming the maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype, this is the length in bytes. 0 is returned for data types where the column size is not applicable.
                        - **scale** *(integer) --* Designated column's number of digits to right of the decimal point. 0 is returned for data types where the scale is not applicable.
                        - **schemaName** *(string) --* Designated column's table's schema
                        - **tableName** *(string) --* Designated column's table name
                        - **type** *(integer) --* SQL type from java.sql.Types.
                        - **typeName** *(string) --* Database-specific type name.
        :type awsSecretStoreArn: string
        :param awsSecretStoreArn: **[REQUIRED]** ARN of the db credentials in AWS Secret Store or the friendly secret name
        :type database: string
        :param database: Target DB name
        :type dbClusterOrInstanceArn: string
        :param dbClusterOrInstanceArn: **[REQUIRED]** ARN of the target db cluster or instance
        :type schema: string
        :param schema: Target Schema name
        :type sqlStatements: string
        :param sqlStatements: **[REQUIRED]** SQL statement(s) to be executed. Statements can be chained by using semicolons
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
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
        Create a paginator for an operation.
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass
