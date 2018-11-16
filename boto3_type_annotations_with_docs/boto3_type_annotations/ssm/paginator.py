from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeActivations(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeActivations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'FilterKey\': \'ActivationIds\'|\'DefaultInstanceName\'|\'IamRole\',
                      \'FilterValues\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          A filter to view information about your activations.
        
          - *(dict) --* 
        
            Filter for the DescribeActivation API.
        
            - **FilterKey** *(string) --* 
        
              The name of the filter.
        
            - **FilterValues** *(list) --* 
        
              The filter values.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'ActivationList\': [
                    {
                        \'ActivationId\': \'string\',
                        \'Description\': \'string\',
                        \'DefaultInstanceName\': \'string\',
                        \'IamRole\': \'string\',
                        \'RegistrationLimit\': 123,
                        \'RegistrationsCount\': 123,
                        \'ExpirationDate\': datetime(2015, 1, 1),
                        \'Expired\': True|False,
                        \'CreatedDate\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ActivationList** *(list) --* 
        
              A list of activations for your AWS account.
        
              - *(dict) --* 
        
                An activation registers one or more on-premises servers or virtual machines (VMs) with AWS so that you can configure those servers or VMs using Run Command. A server or VM that has been registered with AWS is called a managed instance.
        
                - **ActivationId** *(string) --* 
        
                  The ID created by Systems Manager when you submitted the activation.
        
                - **Description** *(string) --* 
        
                  A user defined description of the activation.
        
                - **DefaultInstanceName** *(string) --* 
        
                  A name for the managed instance when it is created.
        
                - **IamRole** *(string) --* 
        
                  The Amazon Identity and Access Management (IAM) role to assign to the managed instance.
        
                - **RegistrationLimit** *(integer) --* 
        
                  The maximum number of managed instances that can be registered using this activation.
        
                - **RegistrationsCount** *(integer) --* 
        
                  The number of managed instances already registered with this activation.
        
                - **ExpirationDate** *(datetime) --* 
        
                  The date when this activation can no longer be used to register managed instances.
        
                - **Expired** *(boolean) --* 
        
                  Whether or not the activation is expired.
        
                - **CreatedDate** *(datetime) --* 
        
                  The date the activation was created.
        
        """
        pass


class DescribeInstanceInformation(Paginator):
    def paginate(self, InstanceInformationFilterList: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceInformation>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              InstanceInformationFilterList=[
                  {
                      \'key\': \'InstanceIds\'|\'AgentVersion\'|\'PingStatus\'|\'PlatformTypes\'|\'ActivationIds\'|\'IamRole\'|\'ResourceType\'|\'AssociationStatus\',
                      \'valueSet\': [
                          \'string\',
                      ]
                  },
              ],
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type InstanceInformationFilterList: list
        :param InstanceInformationFilterList: 
        
          This is a legacy method. We recommend that you don\'t use this method. Instead, use the  InstanceInformationFilter action. The ``InstanceInformationFilter`` action enables you to return instance information by using tags that are specified as a key-value mapping. 
        
          If you do use this method, then you can\'t use the ``InstanceInformationFilter`` action. Using this method and the ``InstanceInformationFilter`` action causes an exception error. 
        
          - *(dict) --* 
        
            Describes a filter for a specific list of instances. You can filter instances information by using tags. You specify tags by using a key-value mapping.
        
            Use this action instead of the  DescribeInstanceInformationRequest$InstanceInformationFilterList method. The ``InstanceInformationFilterList`` method is a legacy method and does not support tags. 
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The name of the filter. 
        
            - **valueSet** *(list) --* **[REQUIRED]** 
        
              The filter values.
        
              - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          One or more filters. Use a filter to return a more specific list of instances. You can filter on Amazon EC2 tag. Specify tags by using a key-value mapping.
        
          - *(dict) --* 
        
            The filters to describe or get information about your managed instances.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The filter key name to describe your instances. For example:
        
              \"InstanceIds\"|\"AgentVersion\"|\"PingStatus\"|\"PlatformTypes\"|\"ActivationIds\"|\"IamRole\"|\"ResourceType\"|\"AssociationStatus\"|\"Tag Key\"
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter values.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceInformationList\': [
                    {
                        \'InstanceId\': \'string\',
                        \'PingStatus\': \'Online\'|\'ConnectionLost\'|\'Inactive\',
                        \'LastPingDateTime\': datetime(2015, 1, 1),
                        \'AgentVersion\': \'string\',
                        \'IsLatestVersion\': True|False,
                        \'PlatformType\': \'Windows\'|\'Linux\',
                        \'PlatformName\': \'string\',
                        \'PlatformVersion\': \'string\',
                        \'ActivationId\': \'string\',
                        \'IamRole\': \'string\',
                        \'RegistrationDate\': datetime(2015, 1, 1),
                        \'ResourceType\': \'ManagedInstance\'|\'Document\'|\'EC2Instance\',
                        \'Name\': \'string\',
                        \'IPAddress\': \'string\',
                        \'ComputerName\': \'string\',
                        \'AssociationStatus\': \'string\',
                        \'LastAssociationExecutionDate\': datetime(2015, 1, 1),
                        \'LastSuccessfulAssociationExecutionDate\': datetime(2015, 1, 1),
                        \'AssociationOverview\': {
                            \'DetailedStatus\': \'string\',
                            \'InstanceAssociationStatusAggregatedCount\': {
                                \'string\': 123
                            }
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **InstanceInformationList** *(list) --* 
        
              The instance information list.
        
              - *(dict) --* 
        
                Describes a filter for a specific list of instances. 
        
                - **InstanceId** *(string) --* 
        
                  The instance ID. 
        
                - **PingStatus** *(string) --* 
        
                  Connection status of SSM Agent. 
        
                - **LastPingDateTime** *(datetime) --* 
        
                  The date and time when agent last pinged Systems Manager service. 
        
                - **AgentVersion** *(string) --* 
        
                  The version of SSM Agent running on your Linux instance. 
        
                - **IsLatestVersion** *(boolean) --* 
        
                  Indicates whether latest version of SSM Agent is running on your instance. Some older versions of Windows Server use the EC2Config service to process SSM requests. For this reason, this field does not indicate whether or not the latest version is installed on Windows managed instances.
        
                - **PlatformType** *(string) --* 
        
                  The operating system platform type. 
        
                - **PlatformName** *(string) --* 
        
                  The name of the operating system platform running on your instance. 
        
                - **PlatformVersion** *(string) --* 
        
                  The version of the OS platform running on your instance. 
        
                - **ActivationId** *(string) --* 
        
                  The activation ID created by Systems Manager when the server or VM was registered.
        
                - **IamRole** *(string) --* 
        
                  The Amazon Identity and Access Management (IAM) role assigned to the on-premises Systems Manager managed instances. This call does not return the IAM role for Amazon EC2 instances. 
        
                - **RegistrationDate** *(datetime) --* 
        
                  The date the server or VM was registered with AWS as a managed instance.
        
                - **ResourceType** *(string) --* 
        
                  The type of instance. Instances are either EC2 instances or managed instances. 
        
                - **Name** *(string) --* 
        
                  The name of the managed instance.
        
                - **IPAddress** *(string) --* 
        
                  The IP address of the managed instance.
        
                - **ComputerName** *(string) --* 
        
                  The fully qualified host name of the managed instance.
        
                - **AssociationStatus** *(string) --* 
        
                  The status of the association.
        
                - **LastAssociationExecutionDate** *(datetime) --* 
        
                  The date the association was last executed.
        
                - **LastSuccessfulAssociationExecutionDate** *(datetime) --* 
        
                  The last date the association was successfully run.
        
                - **AssociationOverview** *(dict) --* 
        
                  Information about the association.
        
                  - **DetailedStatus** *(string) --* 
        
                    Detailed status information about the aggregated associations.
        
                  - **InstanceAssociationStatusAggregatedCount** *(dict) --* 
        
                    The number of associations for the instance(s).
        
                    - *(string) --* 
                      
                      - *(integer) --* 
                
        """
        pass


class DescribeParameters(Paginator):
    def paginate(self, Filters: List = None, ParameterFilters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeParameters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Key\': \'Name\'|\'Type\'|\'KeyId\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ParameterFilters=[
                  {
                      \'Key\': \'string\',
                      \'Option\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters. Use a filter to return a more specific list of results.
        
          - *(dict) --* 
        
            This data type is deprecated. Instead, use  ParameterStringFilter .
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter values.
        
              - *(string) --* 
        
        :type ParameterFilters: list
        :param ParameterFilters: 
        
          Filters to limit the request results.
        
          - *(dict) --* 
        
            One or more filters. Use a filter to return a more specific list of results.
        
            .. note::
        
              The ``Name`` field can\'t be used with the  GetParametersByPath API action.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Option** *(string) --* 
        
              Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
        
            - **Values** *(list) --* 
        
              The value you want to search for.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameters\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'String\'|\'StringList\'|\'SecureString\',
                        \'KeyId\': \'string\',
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'LastModifiedUser\': \'string\',
                        \'Description\': \'string\',
                        \'AllowedPattern\': \'string\',
                        \'Version\': 123
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Parameters** *(list) --* 
        
              Parameters returned by the request.
        
              - *(dict) --* 
        
                Metada includes information like the ARN of the last user and the date/time the parameter was last used.
        
                - **Name** *(string) --* 
        
                  The parameter name.
        
                - **Type** *(string) --* 
        
                  The type of parameter. Valid parameter types include the following: String, String list, Secure string.
        
                - **KeyId** *(string) --* 
        
                  The ID of the query key used for this parameter.
        
                - **LastModifiedDate** *(datetime) --* 
        
                  Date the parameter was last changed or updated.
        
                - **LastModifiedUser** *(string) --* 
        
                  Amazon Resource Name (ARN) of the AWS user who last changed the parameter.
        
                - **Description** *(string) --* 
        
                  Description of the parameter actions.
        
                - **AllowedPattern** *(string) --* 
        
                  A parameter name can include only the following letters and symbols.
        
                  a-zA-Z0-9_.-
        
                - **Version** *(integer) --* 
        
                  The parameter version.
        
        """
        pass


class GetParameterHistory(Paginator):
    def paginate(self, Name: str, WithDecryption: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParameterHistory>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Name=\'string\',
              WithDecryption=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of a parameter you want to query.
        
        :type WithDecryption: boolean
        :param WithDecryption: 
        
          Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.
        
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
                \'Parameters\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'String\'|\'StringList\'|\'SecureString\',
                        \'KeyId\': \'string\',
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'LastModifiedUser\': \'string\',
                        \'Description\': \'string\',
                        \'Value\': \'string\',
                        \'AllowedPattern\': \'string\',
                        \'Version\': 123,
                        \'Labels\': [
                            \'string\',
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Parameters** *(list) --* 
        
              A list of parameters returned by the request.
        
              - *(dict) --* 
        
                Information about parameter usage.
        
                - **Name** *(string) --* 
        
                  The name of the parameter.
        
                - **Type** *(string) --* 
        
                  The type of parameter used.
        
                - **KeyId** *(string) --* 
        
                  The ID of the query key used for this parameter.
        
                - **LastModifiedDate** *(datetime) --* 
        
                  Date the parameter was last changed or updated.
        
                - **LastModifiedUser** *(string) --* 
        
                  Amazon Resource Name (ARN) of the AWS user who last changed the parameter.
        
                - **Description** *(string) --* 
        
                  Information about the parameter.
        
                - **Value** *(string) --* 
        
                  The parameter value.
        
                - **AllowedPattern** *(string) --* 
        
                  Parameter names can include the following letters and symbols.
        
                  a-zA-Z0-9_.-
        
                - **Version** *(integer) --* 
        
                  The parameter version.
        
                - **Labels** *(list) --* 
        
                  Labels assigned to the parameter version.
        
                  - *(string) --* 
              
        """
        pass


class GetParametersByPath(Paginator):
    def paginate(self, Path: str, Recursive: bool = None, ParameterFilters: List = None, WithDecryption: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParametersByPath>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Path=\'string\',
              Recursive=True|False,
              ParameterFilters=[
                  {
                      \'Key\': \'string\',
                      \'Option\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              WithDecryption=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Path: string
        :param Path: **[REQUIRED]** 
        
          The hierarchy for the parameter. Hierarchies start with a forward slash (/) and end with the parameter name. A parameter name hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: ``/Finance/Prod/IAD/WinServ2016/license33``  
        
        :type Recursive: boolean
        :param Recursive: 
        
          Retrieve all parameters within a hierarchy.
        
          .. warning::
        
            If a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path /a, then the user can also access /a/b. Even if a user has explicitly been denied access in IAM for parameter /a, they can still call the GetParametersByPath API action recursively and view /a/b.
        
        :type ParameterFilters: list
        :param ParameterFilters: 
        
          Filters to limit the request results.
        
          .. note::
        
            You can\'t filter using the parameter name.
        
          - *(dict) --* 
        
            One or more filters. Use a filter to return a more specific list of results.
        
            .. note::
        
              The ``Name`` field can\'t be used with the  GetParametersByPath API action.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Option** *(string) --* 
        
              Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
        
            - **Values** *(list) --* 
        
              The value you want to search for.
        
              - *(string) --* 
        
        :type WithDecryption: boolean
        :param WithDecryption: 
        
          Retrieve all parameters in a hierarchy with their value decrypted.
        
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
                \'Parameters\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'String\'|\'StringList\'|\'SecureString\',
                        \'Value\': \'string\',
                        \'Version\': 123,
                        \'Selector\': \'string\',
                        \'SourceResult\': \'string\',
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'ARN\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Parameters** *(list) --* 
        
              A list of parameters found in the specified hierarchy.
        
              - *(dict) --* 
        
                An Amazon EC2 Systems Manager parameter in Parameter Store.
        
                - **Name** *(string) --* 
        
                  The name of the parameter.
        
                - **Type** *(string) --* 
        
                  The type of parameter. Valid values include the following: String, String list, Secure string.
        
                - **Value** *(string) --* 
        
                  The parameter value.
        
                - **Version** *(integer) --* 
        
                  The parameter version.
        
                - **Selector** *(string) --* 
        
                  Either the version number or the label used to retrieve the parameter value. Specify selectors by using one of the following formats:
        
                  parameter_name:version
        
                  parameter_name:label
        
                - **SourceResult** *(string) --* 
        
                  Applies to parameters that reference information in other AWS services. SourceResult is the raw result or response from the source.
        
                - **LastModifiedDate** *(datetime) --* 
        
                  Date the parameter was last changed or updated and the parameter version was created.
        
                - **ARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the parameter.
        
        """
        pass


class ListAssociations(Paginator):
    def paginate(self, AssociationFilterList: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListAssociations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AssociationFilterList=[
                  {
                      \'key\': \'InstanceId\'|\'Name\'|\'AssociationId\'|\'AssociationStatusName\'|\'LastExecutedBefore\'|\'LastExecutedAfter\'|\'AssociationName\',
                      \'value\': \'string\'
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AssociationFilterList: list
        :param AssociationFilterList: 
        
          One or more filters. Use a filter to return a more specific list of results.
        
          - *(dict) --* 
        
            Describes a filter.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'Associations\': [
                    {
                        \'Name\': \'string\',
                        \'InstanceId\': \'string\',
                        \'AssociationId\': \'string\',
                        \'AssociationVersion\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'LastExecutionDate\': datetime(2015, 1, 1),
                        \'Overview\': {
                            \'Status\': \'string\',
                            \'DetailedStatus\': \'string\',
                            \'AssociationStatusAggregatedCount\': {
                                \'string\': 123
                            }
                        },
                        \'ScheduleExpression\': \'string\',
                        \'AssociationName\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Associations** *(list) --* 
        
              The associations.
        
              - *(dict) --* 
        
                Describes an association of a Systems Manager document and an instance.
        
                - **Name** *(string) --* 
        
                  The name of the Systems Manager document.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **AssociationId** *(string) --* 
        
                  The ID created by the system when you create an association. An association is a binding between a document and a set of targets with a schedule.
        
                - **AssociationVersion** *(string) --* 
        
                  The association version.
        
                - **DocumentVersion** *(string) --* 
        
                  The version of the document used in the association.
        
                - **Targets** *(list) --* 
        
                  The instances targeted by the request to create an association. 
        
                  - *(dict) --* 
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                      - *(string) --* 
                  
                - **LastExecutionDate** *(datetime) --* 
        
                  The date on which the association was last run.
        
                - **Overview** *(dict) --* 
        
                  Information about the association.
        
                  - **Status** *(string) --* 
        
                    The status of the association. Status can be: Pending, Success, or Failed.
        
                  - **DetailedStatus** *(string) --* 
        
                    A detailed status of the association.
        
                  - **AssociationStatusAggregatedCount** *(dict) --* 
        
                    Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.
        
                    - *(string) --* 
                      
                      - *(integer) --* 
                
                - **ScheduleExpression** *(string) --* 
        
                  A cron expression that specifies a schedule when the association runs.
        
                - **AssociationName** *(string) --* 
        
                  The association name.
        
        """
        pass


class ListCommandInvocations(Paginator):
    def paginate(self, CommandId: str = None, InstanceId: str = None, Filters: List = None, Details: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommandInvocations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CommandId=\'string\',
              InstanceId=\'string\',
              Filters=[
                  {
                      \'key\': \'InvokedAfter\'|\'InvokedBefore\'|\'Status\'|\'ExecutionStage\'|\'DocumentName\',
                      \'value\': \'string\'
                  },
              ],
              Details=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CommandId: string
        :param CommandId: 
        
          (Optional) The invocations for a specific command ID.
        
        :type InstanceId: string
        :param InstanceId: 
        
          (Optional) The command execution details for a specific instance ID.
        
        :type Filters: list
        :param Filters: 
        
          (Optional) One or more filters. Use a filter to return a more specific list of results.
        
          - *(dict) --* 
        
            Describes a command filter.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The filter value. Valid values for each filter key are as follows:
        
              * InvokedAfter: A timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see results occurring July 7, 2018, and later. 
               
              * InvokedBefore: A timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see results before July 7, 2018. 
               
              * Status: Specify a valid command status to see a list of all command executions with that status. Status values you can specify include: 
        
                * Pending 
                 
                * InProgress 
                 
                * Success 
                 
                * Cancelled 
                 
                * Failed 
                 
                * TimedOut 
                 
                * Cancelling  
                 
              * DocumentName: The name of the SSM document for which you want to see command results. For example, specify ``AWS-RunPatchBaseline`` to see command executions that used this SSM document to perform security patching operations on instances.  
               
              * ExecutionStage: An enum whose value can be either ``Executing`` or ``Complete`` . 
        
                * Specify ``Executing`` to see a list of command executions that are currently still running. 
                 
                * Specify ``Complete`` to see a list of command exeuctions that have already completed. 
                 
        :type Details: boolean
        :param Details: 
        
          (Optional) If set this returns the response of the command executions and any command output. By default this is set to False. 
        
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
                \'CommandInvocations\': [
                    {
                        \'CommandId\': \'string\',
                        \'InstanceId\': \'string\',
                        \'InstanceName\': \'string\',
                        \'Comment\': \'string\',
                        \'DocumentName\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'RequestedDateTime\': datetime(2015, 1, 1),
                        \'Status\': \'Pending\'|\'InProgress\'|\'Delayed\'|\'Success\'|\'Cancelled\'|\'TimedOut\'|\'Failed\'|\'Cancelling\',
                        \'StatusDetails\': \'string\',
                        \'TraceOutput\': \'string\',
                        \'StandardOutputUrl\': \'string\',
                        \'StandardErrorUrl\': \'string\',
                        \'CommandPlugins\': [
                            {
                                \'Name\': \'string\',
                                \'Status\': \'Pending\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                                \'StatusDetails\': \'string\',
                                \'ResponseCode\': 123,
                                \'ResponseStartDateTime\': datetime(2015, 1, 1),
                                \'ResponseFinishDateTime\': datetime(2015, 1, 1),
                                \'Output\': \'string\',
                                \'StandardOutputUrl\': \'string\',
                                \'StandardErrorUrl\': \'string\',
                                \'OutputS3Region\': \'string\',
                                \'OutputS3BucketName\': \'string\',
                                \'OutputS3KeyPrefix\': \'string\'
                            },
                        ],
                        \'ServiceRole\': \'string\',
                        \'NotificationConfig\': {
                            \'NotificationArn\': \'string\',
                            \'NotificationEvents\': [
                                \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                            ],
                            \'NotificationType\': \'Command\'|\'Invocation\'
                        },
                        \'CloudWatchOutputConfig\': {
                            \'CloudWatchLogGroupName\': \'string\',
                            \'CloudWatchOutputEnabled\': True|False
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CommandInvocations** *(list) --* 
        
              (Optional) A list of all invocations. 
        
              - *(dict) --* 
        
                An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user executes SendCommand against three instances, then a command invocation is created for each requested instance ID. A command invocation returns status and detail information about a command you executed. 
        
                - **CommandId** *(string) --* 
        
                  The command against which this invocation was requested.
        
                - **InstanceId** *(string) --* 
        
                  The instance ID in which this invocation was requested.
        
                - **InstanceName** *(string) --* 
        
                  The name of the invocation target. For Amazon EC2 instances this is the value for the aws:Name tag. For on-premises instances, this is the name of the instance.
        
                - **Comment** *(string) --* 
        
                  User-specified information about the command, such as a brief description of what the command should do.
        
                - **DocumentName** *(string) --* 
        
                  The document name that was requested for execution.
        
                - **DocumentVersion** *(string) --* 
        
                  The SSM document version.
        
                - **RequestedDateTime** *(datetime) --* 
        
                  The time and date the request was sent to this instance.
        
                - **Status** *(string) --* 
        
                  Whether or not the invocation succeeded, failed, or is pending.
        
                - **StatusDetails** *(string) --* 
        
                  A detailed status of the command execution for each invocation (each instance targeted by the command). StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
        
                  * Pending: The command has not been sent to the instance. 
                   
                  * In Progress: The command has been sent to the instance but has not reached a terminal state. 
                   
                  * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
                   
                  * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                   
                  * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
                   
                  * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
                   
                  * Canceled: The command was terminated before it was completed. This is a terminal state. 
                   
                  * Undeliverable: The command can\'t be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit and don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                   
                  * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
                   
                - **TraceOutput** *(string) --* 
        
                  Gets the trace output sent by the agent. 
        
                - **StandardOutputUrl** *(string) --* 
        
                  The URL to the plugin\'s StdOut file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardOutputUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.
        
                - **StandardErrorUrl** *(string) --* 
        
                  The URL to the plugin\'s StdErr file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardErrorUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.
        
                - **CommandPlugins** *(list) --* 
                  
                  - *(dict) --* 
        
                    Describes plugin details.
        
                    - **Name** *(string) --* 
        
                      The name of the plugin. Must be one of the following: aws:updateAgent, aws:domainjoin, aws:applications, aws:runPowerShellScript, aws:psmodule, aws:cloudWatch, aws:runShellScript, or aws:updateSSMAgent. 
        
                    - **Status** *(string) --* 
        
                      The status of this plugin. You can execute a document with multiple plugins.
        
                    - **StatusDetails** *(string) --* 
        
                      A detailed status of the plugin execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
        
                      * Pending: The command has not been sent to the instance. 
                       
                      * In Progress: The command has been sent to the instance but has not reached a terminal state. 
                       
                      * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
                       
                      * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                       
                      * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
                       
                      * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
                       
                      * Canceled: The command was terminated before it was completed. This is a terminal state. 
                       
                      * Undeliverable: The command can\'t be delivered to the instance. The instance might not exist, or it might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit, and they don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                       
                      * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
                       
                    - **ResponseCode** *(integer) --* 
        
                      A numeric response code generated after executing the plugin. 
        
                    - **ResponseStartDateTime** *(datetime) --* 
        
                      The time the plugin started executing. 
        
                    - **ResponseFinishDateTime** *(datetime) --* 
        
                      The time the plugin stopped executing. Could stop prematurely if, for example, a cancel command was sent. 
        
                    - **Output** *(string) --* 
        
                      Output of the plugin execution.
        
                    - **StandardOutputUrl** *(string) --* 
        
                      The URL for the complete text written by the plugin to stdout in Amazon S3. If the Amazon S3 bucket for the command was not specified, then this string is empty.
        
                    - **StandardErrorUrl** *(string) --* 
        
                      The URL for the complete text written by the plugin to stderr. If execution is not yet complete, then this string is empty.
        
                    - **OutputS3Region** *(string) --* 
        
                      (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                    - **OutputS3BucketName** *(string) --* 
        
                      The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:
        
                      test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript 
        
                      test_folder is the name of the Amazon S3 bucket;
        
                      ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;
        
                      i-1234567876543 is the instance ID;
        
                      awsrunShellScript is the name of the plugin.
        
                    - **OutputS3KeyPrefix** *(string) --* 
        
                      The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:
        
                      test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript 
        
                      test_folder is the name of the Amazon S3 bucket;
        
                      ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;
        
                      i-1234567876543 is the instance ID;
        
                      awsrunShellScript is the name of the plugin.
        
                - **ServiceRole** *(string) --* 
        
                  The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes on a per instance basis.
        
                - **NotificationConfig** *(dict) --* 
        
                  Configurations for sending notifications about command status changes on a per instance basis.
        
                  - **NotificationArn** *(string) --* 
        
                    An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        
                  - **NotificationEvents** *(list) --* 
        
                    The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
                  - **NotificationType** *(string) --* 
        
                    Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
        
                - **CloudWatchOutputConfig** *(dict) --* 
        
                  CloudWatch Logs information where you want Systems Manager to send the command output.
        
                  - **CloudWatchLogGroupName** *(string) --* 
        
                    The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
        
                  - **CloudWatchOutputEnabled** *(boolean) --* 
        
                    Enables Systems Manager to send command output to CloudWatch Logs.
        
        """
        pass


class ListCommands(Paginator):
    def paginate(self, CommandId: str = None, InstanceId: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommands>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CommandId=\'string\',
              InstanceId=\'string\',
              Filters=[
                  {
                      \'key\': \'InvokedAfter\'|\'InvokedBefore\'|\'Status\'|\'ExecutionStage\'|\'DocumentName\',
                      \'value\': \'string\'
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CommandId: string
        :param CommandId: 
        
          (Optional) If provided, lists only the specified command.
        
        :type InstanceId: string
        :param InstanceId: 
        
          (Optional) Lists commands issued against this instance ID.
        
        :type Filters: list
        :param Filters: 
        
          (Optional) One or more filters. Use a filter to return a more specific list of results. 
        
          - *(dict) --* 
        
            Describes a command filter.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The filter value. Valid values for each filter key are as follows:
        
              * InvokedAfter: A timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see results occurring July 7, 2018, and later. 
               
              * InvokedBefore: A timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see results before July 7, 2018. 
               
              * Status: Specify a valid command status to see a list of all command executions with that status. Status values you can specify include: 
        
                * Pending 
                 
                * InProgress 
                 
                * Success 
                 
                * Cancelled 
                 
                * Failed 
                 
                * TimedOut 
                 
                * Cancelling  
                 
              * DocumentName: The name of the SSM document for which you want to see command results. For example, specify ``AWS-RunPatchBaseline`` to see command executions that used this SSM document to perform security patching operations on instances.  
               
              * ExecutionStage: An enum whose value can be either ``Executing`` or ``Complete`` . 
        
                * Specify ``Executing`` to see a list of command executions that are currently still running. 
                 
                * Specify ``Complete`` to see a list of command exeuctions that have already completed. 
                 
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
                \'Commands\': [
                    {
                        \'CommandId\': \'string\',
                        \'DocumentName\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'Comment\': \'string\',
                        \'ExpiresAfter\': datetime(2015, 1, 1),
                        \'Parameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'InstanceIds\': [
                            \'string\',
                        ],
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'RequestedDateTime\': datetime(2015, 1, 1),
                        \'Status\': \'Pending\'|\'InProgress\'|\'Success\'|\'Cancelled\'|\'Failed\'|\'TimedOut\'|\'Cancelling\',
                        \'StatusDetails\': \'string\',
                        \'OutputS3Region\': \'string\',
                        \'OutputS3BucketName\': \'string\',
                        \'OutputS3KeyPrefix\': \'string\',
                        \'MaxConcurrency\': \'string\',
                        \'MaxErrors\': \'string\',
                        \'TargetCount\': 123,
                        \'CompletedCount\': 123,
                        \'ErrorCount\': 123,
                        \'DeliveryTimedOutCount\': 123,
                        \'ServiceRole\': \'string\',
                        \'NotificationConfig\': {
                            \'NotificationArn\': \'string\',
                            \'NotificationEvents\': [
                                \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                            ],
                            \'NotificationType\': \'Command\'|\'Invocation\'
                        },
                        \'CloudWatchOutputConfig\': {
                            \'CloudWatchLogGroupName\': \'string\',
                            \'CloudWatchOutputEnabled\': True|False
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Commands** *(list) --* 
        
              (Optional) The list of commands requested by the user. 
        
              - *(dict) --* 
        
                Describes a command request.
        
                - **CommandId** *(string) --* 
        
                  A unique identifier for this command.
        
                - **DocumentName** *(string) --* 
        
                  The name of the document requested for execution.
        
                - **DocumentVersion** *(string) --* 
        
                  The SSM document version.
        
                - **Comment** *(string) --* 
        
                  User-specified information about the command, such as a brief description of what the command should do.
        
                - **ExpiresAfter** *(datetime) --* 
        
                  If this time is reached and the command has not already started executing, it will not run. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.
        
                - **Parameters** *(dict) --* 
        
                  The parameter values to be inserted in the document when executing the command.
        
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
                - **InstanceIds** *(list) --* 
        
                  The instance IDs against which this command was requested.
        
                  - *(string) --* 
              
                - **Targets** *(list) --* 
        
                  An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don\'t provide one or more instance IDs in the call.
        
                  - *(dict) --* 
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                      - *(string) --* 
                  
                - **RequestedDateTime** *(datetime) --* 
        
                  The date and time the command was requested.
        
                - **Status** *(string) --* 
        
                  The status of the command.
        
                - **StatusDetails** *(string) --* 
        
                  A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
        
                  * Pending: The command has not been sent to any instances. 
                   
                  * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances. 
                   
                  * Success: The command successfully executed on all invocations. This is a terminal state. 
                   
                  * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state. 
                   
                  * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state. 
                   
                  * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state. 
                   
                  * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state. 
                   
                  * Canceled: The command was terminated before it was completed. This is a terminal state. 
                   
                  * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before executing it on any instance. This is a terminal state. 
                   
                - **OutputS3Region** *(string) --* 
        
                  (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                - **OutputS3BucketName** *(string) --* 
        
                  The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.
        
                - **OutputS3KeyPrefix** *(string) --* 
        
                  The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.
        
                - **MaxConcurrency** *(string) --* 
        
                  The maximum number of instances that are allowed to execute the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Executing Commands Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ in the *AWS Systems Manager User Guide* .
        
                - **MaxErrors** *(string) --* 
        
                  The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 0. For more information about how to use MaxErrors, see `Executing Commands Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ in the *AWS Systems Manager User Guide* .
        
                - **TargetCount** *(integer) --* 
        
                  The number of targets for the command.
        
                - **CompletedCount** *(integer) --* 
        
                  The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.
        
                - **ErrorCount** *(integer) --* 
        
                  The number of targets for which the status is Failed or Execution Timed Out.
        
                - **DeliveryTimedOutCount** *(integer) --* 
        
                  The number of targets for which the status is Delivery Timed Out.
        
                - **ServiceRole** *(string) --* 
        
                  The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes. 
        
                - **NotificationConfig** *(dict) --* 
        
                  Configurations for sending notifications about command status changes. 
        
                  - **NotificationArn** *(string) --* 
        
                    An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        
                  - **NotificationEvents** *(list) --* 
        
                    The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
                  - **NotificationType** *(string) --* 
        
                    Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
        
                - **CloudWatchOutputConfig** *(dict) --* 
        
                  CloudWatch Logs information where you want Systems Manager to send the command output.
        
                  - **CloudWatchLogGroupName** *(string) --* 
        
                    The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
        
                  - **CloudWatchOutputEnabled** *(boolean) --* 
        
                    Enables Systems Manager to send command output to CloudWatch Logs.
        
        """
        pass


class ListDocuments(Paginator):
    def paginate(self, DocumentFilterList: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocuments>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DocumentFilterList=[
                  {
                      \'key\': \'Name\'|\'Owner\'|\'PlatformTypes\'|\'DocumentType\',
                      \'value\': \'string\'
                  },
              ],
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DocumentFilterList: list
        :param DocumentFilterList: 
        
          One or more filters. Use a filter to return a more specific list of results.
        
          - *(dict) --* 
        
            Describes a filter.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The value of the filter.
        
        :type Filters: list
        :param Filters: 
        
          One or more filters. Use a filter to return a more specific list of results.
        
          - *(dict) --* 
        
            One or more filters. Use a filter to return a more specific list of documents.
        
            For keys, you can specify one or more tags that have been applied to a document. 
        
            Other valid values include Owner, Name, PlatformTypes, and DocumentType.
        
            Note that only one Owner can be specified in a request. For example: ``Key=Owner,Values=Self`` .
        
            If you use Name as a key, you can use a name prefix to return a list of documents. For example, in the AWS CLI, to return a list of all documents that begin with ``Te`` , run the following command:
        
             ``aws ssm list-documents --filters Key=Name,Values=Te``  
        
            If you specify more than two keys, only documents that are identified by all the tags are returned in the results. If you specify more than two values for a key, documents that are identified by any of the values are returned in the results.
        
            To specify a custom key and value pair, use the format ``Key=tag:[tagName],Values=[valueName]`` .
        
            For example, if you created a Key called region and are using the AWS CLI to call the ``list-documents`` command: 
        
             ``aws ssm list-documents --filters Key=tag:region,Values=east,west Key=Owner,Values=Self``  
        
            - **Key** *(string) --* 
        
              The name of the filter key.
        
            - **Values** *(list) --* 
        
              The value for the filter key.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'DocumentIdentifiers\': [
                    {
                        \'Name\': \'string\',
                        \'Owner\': \'string\',
                        \'PlatformTypes\': [
                            \'Windows\'|\'Linux\',
                        ],
                        \'DocumentVersion\': \'string\',
                        \'DocumentType\': \'Command\'|\'Policy\'|\'Automation\'|\'Session\',
                        \'SchemaVersion\': \'string\',
                        \'DocumentFormat\': \'YAML\'|\'JSON\',
                        \'TargetType\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DocumentIdentifiers** *(list) --* 
        
              The names of the Systems Manager documents.
        
              - *(dict) --* 
        
                Describes the name of a Systems Manager document.
        
                - **Name** *(string) --* 
        
                  The name of the Systems Manager document.
        
                - **Owner** *(string) --* 
        
                  The AWS user account that created the document.
        
                - **PlatformTypes** *(list) --* 
        
                  The operating system platform. 
        
                  - *(string) --* 
              
                - **DocumentVersion** *(string) --* 
        
                  The document version.
        
                - **DocumentType** *(string) --* 
        
                  The document type.
        
                - **SchemaVersion** *(string) --* 
        
                  The schema version.
        
                - **DocumentFormat** *(string) --* 
        
                  The document format, either JSON or YAML.
        
                - **TargetType** *(string) --* 
        
                  The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 
        
                - **Tags** *(list) --* 
        
                  The tags, or metadata, that have been applied to the document.
        
                  - *(dict) --* 
        
                    Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.
        
                    - **Key** *(string) --* 
        
                      The name of the tag.
        
                    - **Value** *(string) --* 
        
                      The value of the tag.
        
        """
        pass
