from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeAgents(Paginator):
    def paginate(self, agentIds: List = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ApplicationDiscoveryService.Client.describe_agents`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeAgents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              agentIds=[
                  'string',
              ],
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ],
                      'condition': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'agentsInfo': [
                    {
                        'agentId': 'string',
                        'hostName': 'string',
                        'agentNetworkInfoList': [
                            {
                                'ipAddress': 'string',
                                'macAddress': 'string'
                            },
                        ],
                        'connectorId': 'string',
                        'version': 'string',
                        'health': 'HEALTHY'|'UNHEALTHY'|'RUNNING'|'UNKNOWN'|'BLACKLISTED'|'SHUTDOWN',
                        'lastHealthPingTime': 'string',
                        'collectionStatus': 'string',
                        'agentType': 'string',
                        'registeredTime': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **agentsInfo** *(list) --* 
              Lists agents or the Connector by ID or lists all agents/Connectors associated with your user account if you did not specify an agent/Connector ID. The output includes agent/Connector IDs, IP addresses, media access control (MAC) addresses, agent/Connector health, host name where the agent/Connector resides, and the version number of each agent/Connector.
              - *(dict) --* 
                Information about agents or connectors associated with the user’s AWS account. Information includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent or connector health, hostname where the agent or connector resides, and agent version for each agent.
                - **agentId** *(string) --* 
                  The agent or connector ID.
                - **hostName** *(string) --* 
                  The name of the host where the agent or connector resides. The host can be a server or virtual machine.
                - **agentNetworkInfoList** *(list) --* 
                  Network details about the host where the agent or connector resides.
                  - *(dict) --* 
                    Network details about the host where the agent/connector resides.
                    - **ipAddress** *(string) --* 
                      The IP address for the host where the agent/connector resides.
                    - **macAddress** *(string) --* 
                      The MAC address for the host where the agent/connector resides.
                - **connectorId** *(string) --* 
                  The ID of the connector.
                - **version** *(string) --* 
                  The agent or connector version.
                - **health** *(string) --* 
                  The health of the agent or connector.
                - **lastHealthPingTime** *(string) --* 
                  Time since agent or connector health was reported.
                - **collectionStatus** *(string) --* 
                  Status of the collection process for an agent or connector.
                - **agentType** *(string) --* 
                  Type of agent.
                - **registeredTime** *(string) --* 
                  Agent's first registration timestamp in UTC.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type agentIds: list
        :param agentIds:
          The agent or the Connector IDs for which you want information. If you specify no IDs, the system returns information about all agents/Connectors associated with your AWS user account.
          - *(string) --*
        :type filters: list
        :param filters:
          You can filter the request using various logical operators and a *key* -*value* format. For example:
           ``{\"key\": \"collectionStatus\", \"value\": \"STARTED\"}``
          - *(dict) --*
            A filter that can use conditional operators.
            For more information about filters, see `Querying Discovered Configuration Items <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html>`__ .
            - **name** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **values** *(list) --* **[REQUIRED]**
              A string value on which to filter. For example, if you choose the ``destinationServer.osVersion`` filter name, you could specify ``Ubuntu`` for the value.
              - *(string) --*
            - **condition** *(string) --* **[REQUIRED]**
              A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by *AND* . If you specify multiple values for a particular filter, the system differentiates the values using *OR* . Calling either *DescribeConfigurations* or *ListConfigurations* returns attributes of matching configuration items.
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
        """
        pass


class DescribeContinuousExports(Paginator):
    def paginate(self, exportIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ApplicationDiscoveryService.Client.describe_continuous_exports`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeContinuousExports>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              exportIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'descriptions': [
                    {
                        'exportId': 'string',
                        'status': 'START_IN_PROGRESS'|'START_FAILED'|'ACTIVE'|'ERROR'|'STOP_IN_PROGRESS'|'STOP_FAILED'|'INACTIVE',
                        'statusDetail': 'string',
                        's3Bucket': 'string',
                        'startTime': datetime(2015, 1, 1),
                        'stopTime': datetime(2015, 1, 1),
                        'dataSource': 'AGENT',
                        'schemaStorageConfig': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **descriptions** *(list) --* 
              A list of continuous export descriptions.
              - *(dict) --* 
                A list of continuous export descriptions.
                - **exportId** *(string) --* 
                  The unique ID assigned to this export.
                - **status** *(string) --* 
                  Describes the status of the export. Can be one of the following values:
                  * START_IN_PROGRESS - setting up resources to start continuous export. 
                  * START_FAILED - an error occurred setting up continuous export. To recover, call start-continuous-export again. 
                  * ACTIVE - data is being exported to the customer bucket. 
                  * ERROR - an error occurred during export. To fix the issue, call stop-continuous-export and start-continuous-export. 
                  * STOP_IN_PROGRESS - stopping the export. 
                  * STOP_FAILED - an error occurred stopping the export. To recover, call stop-continuous-export again. 
                  * INACTIVE - the continuous export has been stopped. Data is no longer being exported to the customer bucket. 
                - **statusDetail** *(string) --* 
                  Contains information about any errors that have occurred. This data type can have the following values:
                  * ACCESS_DENIED - You don’t have permission to start Data Exploration in Amazon Athena. Contact your AWS administrator for help. For more information, see `Setting Up AWS Application Discovery Service <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html>`__ in the Application Discovery Service User Guide. 
                  * DELIVERY_STREAM_LIMIT_FAILURE - You reached the limit for Amazon Kinesis Data Firehose delivery streams. Reduce the number of streams or request a limit increase and try again. For more information, see `Kinesis Data Streams Limits <http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html>`__ in the Amazon Kinesis Data Streams Developer Guide. 
                  * FIREHOSE_ROLE_MISSING - The Data Exploration feature is in an error state because your IAM User is missing the AWSApplicationDiscoveryServiceFirehose role. Turn on Data Exploration in Amazon Athena and try again. For more information, see `Step 3\: Provide Application Discovery Service Access to Non-Administrator Users by Attaching Policies <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html#setting-up-user-policy>`__ in the Application Discovery Service User Guide. 
                  * FIREHOSE_STREAM_DOES_NOT_EXIST - The Data Exploration feature is in an error state because your IAM User is missing one or more of the Kinesis data delivery streams. 
                  * INTERNAL_FAILURE - The Data Exploration feature is in an error state because of an internal failure. Try again later. If this problem persists, contact AWS Support. 
                  * S3_BUCKET_LIMIT_FAILURE - You reached the limit for Amazon S3 buckets. Reduce the number of Amazon S3 buckets or request a limit increase and try again. For more information, see `Bucket Restrictions and Limitations <http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the Amazon Simple Storage Service Developer Guide. 
                  * S3_NOT_SIGNED_UP - Your account is not signed up for the Amazon S3 service. You must sign up before you can use Amazon S3. You can sign up at the following URL: `https\://aws.amazon.com/s3 <https://aws.amazon.com/s3>`__ . 
                - **s3Bucket** *(string) --* 
                  The name of the s3 bucket where the export data parquet files are stored.
                - **startTime** *(datetime) --* 
                  The timestamp representing when the continuous export was started.
                - **stopTime** *(datetime) --* 
                  The timestamp that represents when this continuous export was stopped.
                - **dataSource** *(string) --* 
                  The type of data collector used to gather this data (currently only offered for AGENT).
                - **schemaStorageConfig** *(dict) --* 
                  An object which describes how the data is stored.
                  * ``databaseName`` - the name of the Glue database used to store the schema. 
                  - *(string) --* 
                    - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type exportIds: list
        :param exportIds:
          The unique IDs assigned to the exports.
          - *(string) --*
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
        """
        pass


class DescribeExportConfigurations(Paginator):
    def paginate(self, exportIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ApplicationDiscoveryService.Client.describe_export_configurations`.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeExportConfigurations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              exportIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'exportsInfo': [
                    {
                        'exportId': 'string',
                        'exportStatus': 'FAILED'|'SUCCEEDED'|'IN_PROGRESS',
                        'statusMessage': 'string',
                        'configurationsDownloadUrl': 'string',
                        'exportRequestTime': datetime(2015, 1, 1),
                        'isTruncated': True|False,
                        'requestedStartTime': datetime(2015, 1, 1),
                        'requestedEndTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **exportsInfo** *(list) --* 
              - *(dict) --* 
                Information regarding the export status of discovered data. The value is an array of objects.
                - **exportId** *(string) --* 
                  A unique identifier used to query an export.
                - **exportStatus** *(string) --* 
                  The status of the data export job.
                - **statusMessage** *(string) --* 
                  A status message provided for API callers.
                - **configurationsDownloadUrl** *(string) --* 
                  A URL for an Amazon S3 bucket where you can review the exported data. The URL is displayed only if the export succeeded.
                - **exportRequestTime** *(datetime) --* 
                  The time that the data export was initiated.
                - **isTruncated** *(boolean) --* 
                  If true, the export of agent information exceeded the size limit for a single export and the exported data is incomplete for the requested time range. To address this, select a smaller time range for the export by using ``startDate`` and ``endDate`` .
                - **requestedStartTime** *(datetime) --* 
                  The value of ``startTime`` parameter in the ``StartExportTask`` request. If no ``startTime`` was requested, this result does not appear in ``ExportInfo`` .
                - **requestedEndTime** *(datetime) --* 
                  The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested, this result does not appear in ``ExportInfo`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type exportIds: list
        :param exportIds:
          A list of continuous export ids to search for.
          - *(string) --*
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
        """
        pass


class DescribeExportTasks(Paginator):
    def paginate(self, exportIds: List = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ApplicationDiscoveryService.Client.describe_export_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeExportTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              exportIds=[
                  'string',
              ],
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ],
                      'condition': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'exportsInfo': [
                    {
                        'exportId': 'string',
                        'exportStatus': 'FAILED'|'SUCCEEDED'|'IN_PROGRESS',
                        'statusMessage': 'string',
                        'configurationsDownloadUrl': 'string',
                        'exportRequestTime': datetime(2015, 1, 1),
                        'isTruncated': True|False,
                        'requestedStartTime': datetime(2015, 1, 1),
                        'requestedEndTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **exportsInfo** *(list) --* 
              Contains one or more sets of export request details. When the status of a request is ``SUCCEEDED`` , the response includes a URL for an Amazon S3 bucket where you can view the data in a CSV file.
              - *(dict) --* 
                Information regarding the export status of discovered data. The value is an array of objects.
                - **exportId** *(string) --* 
                  A unique identifier used to query an export.
                - **exportStatus** *(string) --* 
                  The status of the data export job.
                - **statusMessage** *(string) --* 
                  A status message provided for API callers.
                - **configurationsDownloadUrl** *(string) --* 
                  A URL for an Amazon S3 bucket where you can review the exported data. The URL is displayed only if the export succeeded.
                - **exportRequestTime** *(datetime) --* 
                  The time that the data export was initiated.
                - **isTruncated** *(boolean) --* 
                  If true, the export of agent information exceeded the size limit for a single export and the exported data is incomplete for the requested time range. To address this, select a smaller time range for the export by using ``startDate`` and ``endDate`` .
                - **requestedStartTime** *(datetime) --* 
                  The value of ``startTime`` parameter in the ``StartExportTask`` request. If no ``startTime`` was requested, this result does not appear in ``ExportInfo`` .
                - **requestedEndTime** *(datetime) --* 
                  The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested, this result does not appear in ``ExportInfo`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type exportIds: list
        :param exportIds:
          One or more unique identifiers used to query the status of an export request.
          - *(string) --*
        :type filters: list
        :param filters:
          One or more filters.
          * ``AgentId`` - ID of the agent whose collected data will be exported
          - *(dict) --*
            Used to select which agent\'s data is to be exported. A single agent ID may be selected for export using the `StartExportTask <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__ action.
            - **name** *(string) --* **[REQUIRED]**
              A single ``ExportFilter`` name. Supported filters: ``agentId`` .
            - **values** *(list) --* **[REQUIRED]**
              A single ``agentId`` for a Discovery Agent. An ``agentId`` can be found using the `DescribeAgents <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html>`__ action. Typically an ADS ``agentId`` is in the form ``o-0123456789abcdef0`` .
              - *(string) --*
            - **condition** *(string) --* **[REQUIRED]**
              Supported condition: ``EQUALS``
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
        """
        pass


class DescribeTags(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ApplicationDiscoveryService.Client.describe_tags`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeTags>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'tags': [
                    {
                        'configurationType': 'SERVER'|'PROCESS'|'CONNECTION'|'APPLICATION',
                        'configurationId': 'string',
                        'key': 'string',
                        'value': 'string',
                        'timeOfCreation': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tags** *(list) --* 
              Depending on the input, this is a list of configuration items tagged with a specific tag, or a list of tags for a specific configuration item.
              - *(dict) --* 
                Tags for a configuration item. Tags are metadata that help you categorize IT assets.
                - **configurationType** *(string) --* 
                  A type of IT asset to tag.
                - **configurationId** *(string) --* 
                  The configuration ID for the item to tag. You can specify a list of keys and values.
                - **key** *(string) --* 
                  A type of tag on which to filter. For example, *serverType* .
                - **value** *(string) --* 
                  A value on which to filter. For example *key = serverType* and *value = web server* .
                - **timeOfCreation** *(datetime) --* 
                  The time the configuration tag was created in Coordinated Universal Time (UTC).
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type filters: list
        :param filters:
          You can filter the list using a *key* -*value* format. You can separate these items by using logical operators. Allowed filters include ``tagKey`` , ``tagValue`` , and ``configurationId`` .
          - *(dict) --*
            The tag filter. Valid names are: ``tagKey`` , ``tagValue`` , ``configurationId`` .
            - **name** *(string) --* **[REQUIRED]**
              A name of the tag filter.
            - **values** *(list) --* **[REQUIRED]**
              Values for the tag filter.
              - *(string) --*
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
        """
        pass


class ListConfigurations(Paginator):
    def paginate(self, configurationType: str, filters: List = None, orderBy: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ApplicationDiscoveryService.Client.list_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/ListConfigurations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              configurationType='SERVER'|'PROCESS'|'CONNECTION'|'APPLICATION',
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ],
                      'condition': 'string'
                  },
              ],
              orderBy=[
                  {
                      'fieldName': 'string',
                      'sortOrder': 'ASC'|'DESC'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'configurations': [
                    {
                        'string': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **configurations** *(list) --* 
              Returns configuration details, including the configuration ID, attribute names, and attribute values.
              - *(dict) --* 
                - *(string) --* 
                  - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type configurationType: string
        :param configurationType: **[REQUIRED]**
          A valid configuration identified by Application Discovery Service.
        :type filters: list
        :param filters:
          You can filter the request using various logical operators and a *key* -*value* format. For example:
           ``{\"key\": \"serverType\", \"value\": \"webServer\"}``
          For a complete list of filter options and guidance about using them with this action, see `Querying Discovered Configuration Items <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html#ListConfigurations>`__ .
          - *(dict) --*
            A filter that can use conditional operators.
            For more information about filters, see `Querying Discovered Configuration Items <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html>`__ .
            - **name** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **values** *(list) --* **[REQUIRED]**
              A string value on which to filter. For example, if you choose the ``destinationServer.osVersion`` filter name, you could specify ``Ubuntu`` for the value.
              - *(string) --*
            - **condition** *(string) --* **[REQUIRED]**
              A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by *AND* . If you specify multiple values for a particular filter, the system differentiates the values using *OR* . Calling either *DescribeConfigurations* or *ListConfigurations* returns attributes of matching configuration items.
        :type orderBy: list
        :param orderBy:
          Certain filter criteria return output that can be sorted in ascending or descending order. For a list of output characteristics for each filter, see `Using the ListConfigurations Action <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html#ListConfigurations>`__ .
          - *(dict) --*
            A field and direction for ordered output.
            - **fieldName** *(string) --* **[REQUIRED]**
              The field on which to order.
            - **sortOrder** *(string) --*
              Ordering direction.
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
        """
        pass
