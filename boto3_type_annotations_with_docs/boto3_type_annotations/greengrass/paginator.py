from typing import Dict
from botocore.paginate import Paginator


class ListBulkDeploymentDetailedReports(Paginator):
    def paginate(self, BulkDeploymentId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_bulk_deployment_detailed_reports`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListBulkDeploymentDetailedReports>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              BulkDeploymentId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Deployments': [
                    {
                        'CreatedAt': 'string',
                        'DeploymentArn': 'string',
                        'DeploymentId': 'string',
                        'DeploymentStatus': 'string',
                        'DeploymentType': 'NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
                        'ErrorDetails': [
                            {
                                'DetailedErrorCode': 'string',
                                'DetailedErrorMessage': 'string'
                            },
                        ],
                        'ErrorMessage': 'string',
                        'GroupArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* Success. The response body contains the list of deployments for the given group.
            - **Deployments** *(list) --* A list of the individual group deployments in the bulk deployment operation.
              - *(dict) --* Information about an individual group deployment in a bulk deployment operation.
                - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.
                - **DeploymentArn** *(string) --* The ARN of the group deployment.
                - **DeploymentId** *(string) --* The ID of the group deployment.
                - **DeploymentStatus** *(string) --* The current status of the group deployment: ''Pending'', ''InProgress'', ''Success'', or ''Failure''.
                - **DeploymentType** *(string) --* The type of the deployment.
                - **ErrorDetails** *(list) --* Details about the error.
                  - *(dict) --* Details about the error.
                    - **DetailedErrorCode** *(string) --* A detailed error code.
                    - **DetailedErrorMessage** *(string) --* A detailed error message.
                - **ErrorMessage** *(string) --* The error message for a failed deployment
                - **GroupArn** *(string) --* The ARN of the Greengrass group.
        :type BulkDeploymentId: string
        :param BulkDeploymentId: **[REQUIRED]** The ID of the bulk deployment.
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


class ListBulkDeployments(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_bulk_deployments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListBulkDeployments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'BulkDeployments': [
                    {
                        'BulkDeploymentArn': 'string',
                        'BulkDeploymentId': 'string',
                        'CreatedAt': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* Success. The response body contains the list of bulk deployments.
            - **BulkDeployments** *(list) --* A list of bulk deployments.
              - *(dict) --* Information about a bulk deployment. You cannot start a new bulk deployment while another one is still running or in a non-terminal state.
                - **BulkDeploymentArn** *(string) --* The ARN of the bulk deployment.
                - **BulkDeploymentId** *(string) --* The ID of the bulk deployment.
                - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.
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


class ListConnectorDefinitionVersions(Paginator):
    def paginate(self, ConnectorDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_connector_definition_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListConnectorDefinitionVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ConnectorDefinitionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Versions** *(list) --* Information about a version.
              - *(dict) --* Information about a version.
                - **Arn** *(string) --* The ARN of the version.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                - **Id** *(string) --* The ID of the version.
                - **Version** *(string) --* The unique ID of the version.
        :type ConnectorDefinitionId: string
        :param ConnectorDefinitionId: **[REQUIRED]** The ID of the connector definition.
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


class ListConnectorDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_connector_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListConnectorDefinitions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Definitions** *(list) --* Information about a definition.
              - *(dict) --* Information about a definition.
                - **Arn** *(string) --* The ARN of the definition.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                - **Id** *(string) --* The ID of the definition.
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                - **LatestVersion** *(string) --* The latest version of the definition.
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                - **Name** *(string) --* The name of the definition.
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


class ListCoreDefinitionVersions(Paginator):
    def paginate(self, CoreDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_core_definition_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListCoreDefinitionVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CoreDefinitionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Versions** *(list) --* Information about a version.
              - *(dict) --* Information about a version.
                - **Arn** *(string) --* The ARN of the version.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                - **Id** *(string) --* The ID of the version.
                - **Version** *(string) --* The unique ID of the version.
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.
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


class ListCoreDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_core_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListCoreDefinitions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Definitions** *(list) --* Information about a definition.
              - *(dict) --* Information about a definition.
                - **Arn** *(string) --* The ARN of the definition.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                - **Id** *(string) --* The ID of the definition.
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                - **LatestVersion** *(string) --* The latest version of the definition.
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                - **Name** *(string) --* The name of the definition.
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


class ListDeployments(Paginator):
    def paginate(self, GroupId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_deployments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeployments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              GroupId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Deployments': [
                    {
                        'CreatedAt': 'string',
                        'DeploymentArn': 'string',
                        'DeploymentId': 'string',
                        'DeploymentType': 'NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
                        'GroupArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* Success. The response body contains the list of deployments for the given group.
            - **Deployments** *(list) --* A list of deployments for the requested groups.
              - *(dict) --* Information about a deployment.
                - **CreatedAt** *(string) --* The time, in milliseconds since the epoch, when the deployment was created.
                - **DeploymentArn** *(string) --* The ARN of the deployment.
                - **DeploymentId** *(string) --* The ID of the deployment.
                - **DeploymentType** *(string) --* The type of the deployment.
                - **GroupArn** *(string) --* The ARN of the group for this deployment.
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.
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


class ListDeviceDefinitionVersions(Paginator):
    def paginate(self, DeviceDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_device_definition_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeviceDefinitionVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DeviceDefinitionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Versions** *(list) --* Information about a version.
              - *(dict) --* Information about a version.
                - **Arn** *(string) --* The ARN of the version.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                - **Id** *(string) --* The ID of the version.
                - **Version** *(string) --* The unique ID of the version.
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.
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


class ListDeviceDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_device_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeviceDefinitions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Definitions** *(list) --* Information about a definition.
              - *(dict) --* Information about a definition.
                - **Arn** *(string) --* The ARN of the definition.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                - **Id** *(string) --* The ID of the definition.
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                - **LatestVersion** *(string) --* The latest version of the definition.
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                - **Name** *(string) --* The name of the definition.
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


class ListFunctionDefinitionVersions(Paginator):
    def paginate(self, FunctionDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_function_definition_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListFunctionDefinitionVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FunctionDefinitionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* success
            - **Versions** *(list) --* Information about a version.
              - *(dict) --* Information about a version.
                - **Arn** *(string) --* The ARN of the version.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                - **Id** *(string) --* The ID of the version.
                - **Version** *(string) --* The unique ID of the version.
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.
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


class ListFunctionDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_function_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListFunctionDefinitions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* Success. The response contains the IDs of all the Greengrass Lambda function definitions in this account.
            - **Definitions** *(list) --* Information about a definition.
              - *(dict) --* Information about a definition.
                - **Arn** *(string) --* The ARN of the definition.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                - **Id** *(string) --* The ID of the definition.
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                - **LatestVersion** *(string) --* The latest version of the definition.
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                - **Name** *(string) --* The name of the definition.
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


class ListGroupVersions(Paginator):
    def paginate(self, GroupId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_group_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroupVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              GroupId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* Success. The response contains the list of versions and metadata for the given group.
            - **Versions** *(list) --* Information about a version.
              - *(dict) --* Information about a version.
                - **Arn** *(string) --* The ARN of the version.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                - **Id** *(string) --* The ID of the version.
                - **Version** *(string) --* The unique ID of the version.
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.
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


class ListGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Groups': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Groups** *(list) --* Information about a group.
              - *(dict) --* Information about a group.
                - **Arn** *(string) --* The ARN of the group.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the group was created.
                - **Id** *(string) --* The ID of the group.
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the group was last updated.
                - **LatestVersion** *(string) --* The latest version of the group.
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the group.
                - **Name** *(string) --* The name of the group.
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


class ListLoggerDefinitionVersions(Paginator):
    def paginate(self, LoggerDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_logger_definition_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListLoggerDefinitionVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              LoggerDefinitionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Versions** *(list) --* Information about a version.
              - *(dict) --* Information about a version.
                - **Arn** *(string) --* The ARN of the version.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                - **Id** *(string) --* The ID of the version.
                - **Version** *(string) --* The unique ID of the version.
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.
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


class ListLoggerDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_logger_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListLoggerDefinitions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Definitions** *(list) --* Information about a definition.
              - *(dict) --* Information about a definition.
                - **Arn** *(string) --* The ARN of the definition.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                - **Id** *(string) --* The ID of the definition.
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                - **LatestVersion** *(string) --* The latest version of the definition.
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                - **Name** *(string) --* The name of the definition.
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


class ListResourceDefinitionVersions(Paginator):
    def paginate(self, ResourceDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_resource_definition_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListResourceDefinitionVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceDefinitionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* success
            - **Versions** *(list) --* Information about a version.
              - *(dict) --* Information about a version.
                - **Arn** *(string) --* The ARN of the version.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                - **Id** *(string) --* The ID of the version.
                - **Version** *(string) --* The unique ID of the version.
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.
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


class ListResourceDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_resource_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListResourceDefinitions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* The IDs of all the Greengrass resource definitions in this account.
            - **Definitions** *(list) --* Information about a definition.
              - *(dict) --* Information about a definition.
                - **Arn** *(string) --* The ARN of the definition.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                - **Id** *(string) --* The ID of the definition.
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                - **LatestVersion** *(string) --* The latest version of the definition.
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                - **Name** *(string) --* The name of the definition.
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


class ListSubscriptionDefinitionVersions(Paginator):
    def paginate(self, SubscriptionDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_subscription_definition_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListSubscriptionDefinitionVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SubscriptionDefinitionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Versions** *(list) --* Information about a version.
              - *(dict) --* Information about a version.
                - **Arn** *(string) --* The ARN of the version.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                - **Id** *(string) --* The ID of the version.
                - **Version** *(string) --* The unique ID of the version.
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.
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


class ListSubscriptionDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Greengrass.Client.list_subscription_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListSubscriptionDefinitions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Definitions** *(list) --* Information about a definition.
              - *(dict) --* Information about a definition.
                - **Arn** *(string) --* The ARN of the definition.
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                - **Id** *(string) --* The ID of the definition.
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                - **LatestVersion** *(string) --* The latest version of the definition.
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                - **Name** *(string) --* The name of the definition.
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
