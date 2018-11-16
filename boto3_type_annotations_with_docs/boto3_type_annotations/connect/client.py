from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
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

    def create_user(self, Username: str, PhoneConfig: Dict, SecurityProfileIds: List, RoutingProfileId: str, InstanceId: str, Password: str = None, IdentityInfo: Dict = None, DirectoryUserId: str = None, HierarchyGroupId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/CreateUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_user(
              Username=\'string\',
              Password=\'string\',
              IdentityInfo={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'Email\': \'string\'
              },
              PhoneConfig={
                  \'PhoneType\': \'SOFT_PHONE\'|\'DESK_PHONE\',
                  \'AutoAccept\': True|False,
                  \'AfterContactWorkTimeLimit\': 123,
                  \'DeskPhoneNumber\': \'string\'
              },
              DirectoryUserId=\'string\',
              SecurityProfileIds=[
                  \'string\',
              ],
              RoutingProfileId=\'string\',
              HierarchyGroupId=\'string\',
              InstanceId=\'string\'
          )
        :type Username: string
        :param Username: **[REQUIRED]** 
        
          The user name in Amazon Connect for the account to create.
        
        :type Password: string
        :param Password: 
        
          The password for the user account to create. This is required if you are using Amazon Connect for identity management. If you are using SAML for identity management and include this parameter, an ``InvalidRequestException`` is returned.
        
        :type IdentityInfo: dict
        :param IdentityInfo: 
        
          Information about the user, including email address, first name, and last name.
        
          - **FirstName** *(string) --* 
        
            The first name used in the user account. This is required if you are using Amazon Connect or SAML for identity management.
        
          - **LastName** *(string) --* 
        
            The last name used in the user account. This is required if you are using Amazon Connect or SAML for identity management.
        
          - **Email** *(string) --* 
        
            The email address added to the user account. If you are using SAML for identity management and include this parameter, an ``InvalidRequestException`` is returned.
        
        :type PhoneConfig: dict
        :param PhoneConfig: **[REQUIRED]** 
        
          Specifies the phone settings for the user, including AfterContactWorkTimeLimit, AutoAccept, DeskPhoneNumber, and PhoneType.
        
          - **PhoneType** *(string) --* **[REQUIRED]** 
        
            The phone type selected for the user, either Soft phone or Desk phone.
        
          - **AutoAccept** *(boolean) --* 
        
            The Auto accept setting for the user, Yes or No.
        
          - **AfterContactWorkTimeLimit** *(integer) --* 
        
            The After Call Work (ACW) timeout setting, in seconds, for the user.
        
          - **DeskPhoneNumber** *(string) --* 
        
            The phone number for the user\'s desk phone.
        
        :type DirectoryUserId: string
        :param DirectoryUserId: 
        
          The unique identifier for the user account in the directory service directory used for identity management. If Amazon Connect is unable to access the existing directory, you can use the ``DirectoryUserId`` to authenticate users. If you include the parameter, it is assumed that Amazon Connect cannot access the directory. If the parameter is not included, the UserIdentityInfo is used to authenticate users from your existing directory.
        
          This parameter is required if you are using an existing directory for identity management in Amazon Connect when Amazon Connect cannot access your directory to authenticate users. If you are using SAML for identity management and include this parameter, an ``InvalidRequestException`` is returned.
        
        :type SecurityProfileIds: list
        :param SecurityProfileIds: **[REQUIRED]** 
        
          The unique identifier of the security profile to assign to the user created.
        
          - *(string) --* 
        
        :type RoutingProfileId: string
        :param RoutingProfileId: **[REQUIRED]** 
        
          The unique identifier for the routing profile to assign to the user created.
        
        :type HierarchyGroupId: string
        :param HierarchyGroupId: 
        
          The unique identifier for the hierarchy group to assign to the user created.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserId\': \'string\',
                \'UserArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UserId** *(string) --* 
        
              The unique identifier for the user account in Amazon Connect
        
            - **UserArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the user account created.
        
        """
        pass

    def delete_user(self, InstanceId: str, UserId: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DeleteUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_user(
              InstanceId=\'string\',
              UserId=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The unique identifier of the user to delete.
        
        :returns: None
        """
        pass

    def describe_user(self, UserId: str, InstanceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_user(
              UserId=\'string\',
              InstanceId=\'string\'
          )
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          Unique identifier for the user account to return.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'User\': {
                    \'Id\': \'string\',
                    \'Arn\': \'string\',
                    \'Username\': \'string\',
                    \'IdentityInfo\': {
                        \'FirstName\': \'string\',
                        \'LastName\': \'string\',
                        \'Email\': \'string\'
                    },
                    \'PhoneConfig\': {
                        \'PhoneType\': \'SOFT_PHONE\'|\'DESK_PHONE\',
                        \'AutoAccept\': True|False,
                        \'AfterContactWorkTimeLimit\': 123,
                        \'DeskPhoneNumber\': \'string\'
                    },
                    \'DirectoryUserId\': \'string\',
                    \'SecurityProfileIds\': [
                        \'string\',
                    ],
                    \'RoutingProfileId\': \'string\',
                    \'HierarchyGroupId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **User** *(dict) --* 
        
              A ``User`` object that contains information about the user account and configuration settings.
        
              - **Id** *(string) --* 
        
                The identifier of the user account.
        
              - **Arn** *(string) --* 
        
                The ARN of the user account.
        
              - **Username** *(string) --* 
        
                The user name assigned to the user account.
        
              - **IdentityInfo** *(dict) --* 
        
                A ``UserIdentityInfo`` object.
        
                - **FirstName** *(string) --* 
        
                  The first name used in the user account. This is required if you are using Amazon Connect or SAML for identity management.
        
                - **LastName** *(string) --* 
        
                  The last name used in the user account. This is required if you are using Amazon Connect or SAML for identity management.
        
                - **Email** *(string) --* 
        
                  The email address added to the user account. If you are using SAML for identity management and include this parameter, an ``InvalidRequestException`` is returned.
        
              - **PhoneConfig** *(dict) --* 
        
                A ``UserPhoneConfig`` object.
        
                - **PhoneType** *(string) --* 
        
                  The phone type selected for the user, either Soft phone or Desk phone.
        
                - **AutoAccept** *(boolean) --* 
        
                  The Auto accept setting for the user, Yes or No.
        
                - **AfterContactWorkTimeLimit** *(integer) --* 
        
                  The After Call Work (ACW) timeout setting, in seconds, for the user.
        
                - **DeskPhoneNumber** *(string) --* 
        
                  The phone number for the user\'s desk phone.
        
              - **DirectoryUserId** *(string) --* 
        
                The directory Id for the user account in the existing directory used for identity management.
        
              - **SecurityProfileIds** *(list) --* 
        
                The identifier(s) for the security profile assigned to the user.
        
                - *(string) --* 
            
              - **RoutingProfileId** *(string) --* 
        
                The identifier of the routing profile assigned to the user.
        
              - **HierarchyGroupId** *(string) --* 
        
                The identifier for the hierarchy group assigned to the user.
        
        """
        pass

    def describe_user_hierarchy_group(self, HierarchyGroupId: str, InstanceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeUserHierarchyGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_user_hierarchy_group(
              HierarchyGroupId=\'string\',
              InstanceId=\'string\'
          )
        :type HierarchyGroupId: string
        :param HierarchyGroupId: **[REQUIRED]** 
        
          The identifier for the hierarchy group to return.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HierarchyGroup\': {
                    \'Id\': \'string\',
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'LevelId\': \'string\',
                    \'HierarchyPath\': {
                        \'LevelOne\': {
                            \'Id\': \'string\',
                            \'Arn\': \'string\',
                            \'Name\': \'string\'
                        },
                        \'LevelTwo\': {
                            \'Id\': \'string\',
                            \'Arn\': \'string\',
                            \'Name\': \'string\'
                        },
                        \'LevelThree\': {
                            \'Id\': \'string\',
                            \'Arn\': \'string\',
                            \'Name\': \'string\'
                        },
                        \'LevelFour\': {
                            \'Id\': \'string\',
                            \'Arn\': \'string\',
                            \'Name\': \'string\'
                        },
                        \'LevelFive\': {
                            \'Id\': \'string\',
                            \'Arn\': \'string\',
                            \'Name\': \'string\'
                        }
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **HierarchyGroup** *(dict) --* 
        
              Returns a ``HierarchyGroup`` object.
        
              - **Id** *(string) --* 
        
                The identifier for the hierarchy group.
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) for the hierarchy group.
        
              - **Name** *(string) --* 
        
                The name of the hierarchy group in your instance.
        
              - **LevelId** *(string) --* 
        
                The identifier for the level in the hierarchy group.
        
              - **HierarchyPath** *(dict) --* 
        
                A ``HierarchyPath`` object that contains information about the levels in the hierarchy group.
        
                - **LevelOne** *(dict) --* 
        
                  A ``HierarchyGroupSummary`` object that contains information about the level of the hierarchy group, including ARN, Id, and Name.
        
                  - **Id** *(string) --* 
        
                    The identifier of the hierarchy group.
        
                  - **Arn** *(string) --* 
        
                    The ARN for the hierarchy group.
        
                  - **Name** *(string) --* 
        
                    The name of the hierarchy group.
        
                - **LevelTwo** *(dict) --* 
        
                  A ``HierarchyGroupSummary`` object that contains information about the level of the hierarchy group, including ARN, Id, and Name.
        
                  - **Id** *(string) --* 
        
                    The identifier of the hierarchy group.
        
                  - **Arn** *(string) --* 
        
                    The ARN for the hierarchy group.
        
                  - **Name** *(string) --* 
        
                    The name of the hierarchy group.
        
                - **LevelThree** *(dict) --* 
        
                  A ``HierarchyGroupSummary`` object that contains information about the level of the hierarchy group, including ARN, Id, and Name.
        
                  - **Id** *(string) --* 
        
                    The identifier of the hierarchy group.
        
                  - **Arn** *(string) --* 
        
                    The ARN for the hierarchy group.
        
                  - **Name** *(string) --* 
        
                    The name of the hierarchy group.
        
                - **LevelFour** *(dict) --* 
        
                  A ``HierarchyGroupSummary`` object that contains information about the level of the hierarchy group, including ARN, Id, and Name.
        
                  - **Id** *(string) --* 
        
                    The identifier of the hierarchy group.
        
                  - **Arn** *(string) --* 
        
                    The ARN for the hierarchy group.
        
                  - **Name** *(string) --* 
        
                    The name of the hierarchy group.
        
                - **LevelFive** *(dict) --* 
        
                  A ``HierarchyGroupSummary`` object that contains information about the level of the hierarchy group, including ARN, Id, and Name.
        
                  - **Id** *(string) --* 
        
                    The identifier of the hierarchy group.
        
                  - **Arn** *(string) --* 
        
                    The ARN for the hierarchy group.
        
                  - **Name** *(string) --* 
        
                    The name of the hierarchy group.
        
        """
        pass

    def describe_user_hierarchy_structure(self, InstanceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeUserHierarchyStructure>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_user_hierarchy_structure(
              InstanceId=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HierarchyStructure\': {
                    \'LevelOne\': {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    },
                    \'LevelTwo\': {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    },
                    \'LevelThree\': {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    },
                    \'LevelFour\': {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    },
                    \'LevelFive\': {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **HierarchyStructure** *(dict) --* 
        
              A ``HierarchyStructure`` object.
        
              - **LevelOne** *(dict) --* 
        
                A ``HierarchyLevel`` object that contains information about the hierarchy group level.
        
                - **Id** *(string) --* 
        
                  The identifier for the hierarchy group level.
        
                - **Arn** *(string) --* 
        
                  The ARN for the hierarchy group level.
        
                - **Name** *(string) --* 
        
                  The name of the hierarchy group level.
        
              - **LevelTwo** *(dict) --* 
        
                A ``HierarchyLevel`` object that contains information about the hierarchy group level.
        
                - **Id** *(string) --* 
        
                  The identifier for the hierarchy group level.
        
                - **Arn** *(string) --* 
        
                  The ARN for the hierarchy group level.
        
                - **Name** *(string) --* 
        
                  The name of the hierarchy group level.
        
              - **LevelThree** *(dict) --* 
        
                A ``HierarchyLevel`` object that contains information about the hierarchy group level.
        
                - **Id** *(string) --* 
        
                  The identifier for the hierarchy group level.
        
                - **Arn** *(string) --* 
        
                  The ARN for the hierarchy group level.
        
                - **Name** *(string) --* 
        
                  The name of the hierarchy group level.
        
              - **LevelFour** *(dict) --* 
        
                A ``HierarchyLevel`` object that contains information about the hierarchy group level.
        
                - **Id** *(string) --* 
        
                  The identifier for the hierarchy group level.
        
                - **Arn** *(string) --* 
        
                  The ARN for the hierarchy group level.
        
                - **Name** *(string) --* 
        
                  The name of the hierarchy group level.
        
              - **LevelFive** *(dict) --* 
        
                A ``HierarchyLevel`` object that contains information about the hierarchy group level.
        
                - **Id** *(string) --* 
        
                  The identifier for the hierarchy group level.
        
                - **Arn** *(string) --* 
        
                  The ARN for the hierarchy group level.
        
                - **Name** *(string) --* 
        
                  The name of the hierarchy group level.
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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

    def get_current_metric_data(self, InstanceId: str, Filters: Dict, CurrentMetrics: List, Groupings: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        If you are using an IAM account, it must have permission to the ``connect:GetCurrentMetricData`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetCurrentMetricData>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_current_metric_data(
              InstanceId=\'string\',
              Filters={
                  \'Queues\': [
                      \'string\',
                  ],
                  \'Channels\': [
                      \'VOICE\',
                  ]
              },
              Groupings=[
                  \'QUEUE\'|\'CHANNEL\',
              ],
              CurrentMetrics=[
                  {
                      \'Name\': \'AGENTS_ONLINE\'|\'AGENTS_AVAILABLE\'|\'AGENTS_ON_CALL\'|\'AGENTS_NON_PRODUCTIVE\'|\'AGENTS_AFTER_CONTACT_WORK\'|\'AGENTS_ERROR\'|\'AGENTS_STAFFED\'|\'CONTACTS_IN_QUEUE\'|\'OLDEST_CONTACT_AGE\'|\'CONTACTS_SCHEDULED\',
                      \'Unit\': \'SECONDS\'|\'COUNT\'|\'PERCENT\'
                  },
              ],
              NextToken=\'string\',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type Filters: dict
        :param Filters: **[REQUIRED]** 
        
          A ``Filters`` object that contains a list of queue IDs or queue ARNs, up to 100, or list of Channels to use to filter the metrics returned in the response. Metric data is retrieved only for the resources associated with the queue IDs, ARNs, or Channels included in the filter. You can include both IDs and ARNs in the same request. To retrieve metrics for all queues, add the queue ID or ARN for each queue in your instance. Only VOICE is supported for Channels.
        
          To find the ARN for a queue, open the queue you want to use in the Amazon Connect Queue editor. The ARN for the queue is displayed in the address bar as part of the URL. For example, the queue ARN is the set of characters at the end of the URL, after \'id=\' such as ``arn:aws:connect:us-east-1:270923740243:instance/78fb859d-1b7d-44b1-8aa3-12f0835c5855/queue/1d1a4575-9618-40ab-bbeb-81e45795fe61`` . The queue ID is also included in the URL, and is the string after \'queue/\'.
        
          - **Queues** *(list) --* 
        
            A list of up to 100 queue IDs or queue ARNs to use to filter the metrics retrieved. You can include both IDs and ARNs in a request.
        
            - *(string) --* 
        
          - **Channels** *(list) --* 
        
            The Channel to use as a filter for the metrics returned. Only VOICE is supported.
        
            - *(string) --* 
        
        :type Groupings: list
        :param Groupings: 
        
          The grouping applied to the metrics returned. For example, when grouped by QUEUE, the metrics returned apply to each queue rather than aggregated for all queues. If you group by CHANNEL, you should include a Channels filter. The only supported channel is VOICE.
        
          If no ``Grouping`` is included in the request, a summary of ``CurrentMetrics`` is returned. 
        
          - *(string) --* 
        
        :type CurrentMetrics: list
        :param CurrentMetrics: **[REQUIRED]** 
        
          A list of ``CurrentMetric`` objects for the metrics to retrieve. Each ``CurrentMetric`` includes a name of a metric to retrieve and the unit to use for it.
        
          The following metrics are available:
        
            AGENTS_AVAILABLE  
        
          Unit: COUNT
        
            AGENTS_ONLINE  
        
          Unit: COUNT
        
            AGENTS_ON_CALL  
        
          Unit: COUNT
        
            AGENTS_STAFFED  
        
          Unit: COUNT
        
            AGENTS_AFTER_CONTACT_WORK  
        
          Unit: COUNT
        
            AGENTS_NON_PRODUCTIVE  
        
          Unit: COUNT
        
            AGENTS_ERROR  
        
          Unit: COUNT
        
            CONTACTS_IN_QUEUE  
        
          Unit: COUNT
        
            OLDEST_CONTACT_AGE  
        
          Unit: SECONDS
        
            CONTACTS_SCHEDULED  
        
          Unit: COUNT
        
          - *(dict) --* 
        
            A ``CurrentMetric`` object that contains the Name and Unit for the metric.
        
            - **Name** *(string) --* 
        
              The name of the metric.
        
            - **Unit** *(string) --* 
        
              The unit for the metric.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
        
          The token expires after 5 minutes from the time it is created. Subsequent requests that use the `NextToken must use the same request parameters as the request that generated the token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
           ``MaxResults`` indicates the maximum number of results to return per page in the response, between 1 and 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'MetricResults\': [
                    {
                        \'Dimensions\': {
                            \'Queue\': {
                                \'Id\': \'string\',
                                \'Arn\': \'string\'
                            },
                            \'Channel\': \'VOICE\'
                        },
                        \'Collections\': [
                            {
                                \'Metric\': {
                                    \'Name\': \'AGENTS_ONLINE\'|\'AGENTS_AVAILABLE\'|\'AGENTS_ON_CALL\'|\'AGENTS_NON_PRODUCTIVE\'|\'AGENTS_AFTER_CONTACT_WORK\'|\'AGENTS_ERROR\'|\'AGENTS_STAFFED\'|\'CONTACTS_IN_QUEUE\'|\'OLDEST_CONTACT_AGE\'|\'CONTACTS_SCHEDULED\',
                                    \'Unit\': \'SECONDS\'|\'COUNT\'|\'PERCENT\'
                                },
                                \'Value\': 123.0
                            },
                        ]
                    },
                ],
                \'DataSnapshotTime\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              A string returned in the response. Use the value returned in the response as the value of the NextToken in a subsequent request to retrieve the next set of results.
        
              The token expires after 5 minutes from the time it is created. Subsequent requests that use the NextToken must use the same request parameters as the request that generated the token. 
        
            - **MetricResults** *(list) --* 
        
              A list of ``CurrentMetricResult`` objects organized by ``Dimensions`` combining with ``CurrentMetricDataCollections`` .
        
               ``Dimensions`` is the resourceId specified in the ``Filters`` of the request. 
        
               ``Collections`` is a list of ``CurrentMetricData`` objects with corresponding values to the ``CurrentMetrics`` specified in the request.
        
              If no ``Grouping`` is specified in the request, ``Collections`` is a summary for the ``CurrentMetric`` returned.
        
              - *(dict) --* 
        
                A ``CurrentMetricResult`` object.
        
                - **Dimensions** *(dict) --* 
        
                  The ``Dimensions`` for the ``CurrentMetricResult`` object.
        
                  - **Queue** *(dict) --* 
        
                    A ``QueueReference`` object used as one part of dimension for the metrics results.
        
                    - **Id** *(string) --* 
        
                      The ID of the queue associated with the metrics returned.
        
                    - **Arn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of queue.
        
                  - **Channel** *(string) --* 
        
                    The channel used for grouping and filters. Only VOICE is supported.
        
                - **Collections** *(list) --* 
        
                  The ``Collections`` for the ``CurrentMetricResult`` object.
        
                  - *(dict) --* 
        
                    A ``CurrentMetricData`` object.
        
                    - **Metric** *(dict) --* 
        
                      The metric in a ``CurrentMetricData`` object.
        
                      - **Name** *(string) --* 
        
                        The name of the metric.
        
                      - **Unit** *(string) --* 
        
                        The unit for the metric.
        
                    - **Value** *(float) --* 
        
                      The value of the metric in the CurrentMetricData object.
        
            - **DataSnapshotTime** *(datetime) --* 
        
              The time at which ``CurrentMetricData`` was retrieved and cached for pagination.
        
        """
        pass

    def get_federation_token(self, InstanceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetFederationToken>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_federation_token(
              InstanceId=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Credentials\': {
                    \'AccessToken\': \'string\',
                    \'AccessTokenExpiration\': datetime(2015, 1, 1),
                    \'RefreshToken\': \'string\',
                    \'RefreshTokenExpiration\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Credentials** *(dict) --* 
        
              The credentials to use for federation.
        
              - **AccessToken** *(string) --* 
        
                An access token generated for a federated user to access Amazon Connect
        
              - **AccessTokenExpiration** *(datetime) --* 
        
                A token generated with an expiration time for the session a user is logged in to Amazon Connect
        
              - **RefreshToken** *(string) --* 
        
                Renews a token generated for a user to access the Amazon Connect instance.
        
              - **RefreshTokenExpiration** *(datetime) --* 
        
                Renews the expiration timer for a generated token.
        
        """
        pass

    def get_metric_data(self, InstanceId: str, StartTime: datetime, EndTime: datetime, Filters: Dict, HistoricalMetrics: List, Groupings: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        If you are using an IAM account, it must have permission to the ``connect:GetMetricData`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetMetricData>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_metric_data(
              InstanceId=\'string\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Filters={
                  \'Queues\': [
                      \'string\',
                  ],
                  \'Channels\': [
                      \'VOICE\',
                  ]
              },
              Groupings=[
                  \'QUEUE\'|\'CHANNEL\',
              ],
              HistoricalMetrics=[
                  {
                      \'Name\': \'CONTACTS_QUEUED\'|\'CONTACTS_HANDLED\'|\'CONTACTS_ABANDONED\'|\'CONTACTS_CONSULTED\'|\'CONTACTS_AGENT_HUNG_UP_FIRST\'|\'CONTACTS_HANDLED_INCOMING\'|\'CONTACTS_HANDLED_OUTBOUND\'|\'CONTACTS_HOLD_ABANDONS\'|\'CONTACTS_TRANSFERRED_IN\'|\'CONTACTS_TRANSFERRED_OUT\'|\'CONTACTS_TRANSFERRED_IN_FROM_QUEUE\'|\'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE\'|\'CONTACTS_MISSED\'|\'CALLBACK_CONTACTS_HANDLED\'|\'API_CONTACTS_HANDLED\'|\'OCCUPANCY\'|\'HANDLE_TIME\'|\'AFTER_CONTACT_WORK_TIME\'|\'QUEUED_TIME\'|\'ABANDON_TIME\'|\'QUEUE_ANSWER_TIME\'|\'HOLD_TIME\'|\'INTERACTION_TIME\'|\'INTERACTION_AND_HOLD_TIME\'|\'SERVICE_LEVEL\',
                      \'Threshold\': {
                          \'Comparison\': \'LT\',
                          \'ThresholdValue\': 123.0
                      },
                      \'Statistic\': \'SUM\'|\'MAX\'|\'AVG\',
                      \'Unit\': \'SECONDS\'|\'COUNT\'|\'PERCENT\'
                  },
              ],
              NextToken=\'string\',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]** 
        
          The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the retrieval of historical metrics data. The time must be specified using a multiple of 5 minutes, such as 10:05, 10:10, 10:15.
        
           ``StartTime`` cannot be earlier than 24 hours before the time of the request. Historical metrics are available in Amazon Connect only for 24 hours.
        
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]** 
        
          The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the retrieval of historical metrics data. The time must be specified using an interval of 5 minutes, such as 11:00, 11:05, 11:10, and must be later than the ``StartTime`` timestamp.
        
          The time range between ``StartTime`` and ``EndTime`` must be less than 24 hours.
        
        :type Filters: dict
        :param Filters: **[REQUIRED]** 
        
          A ``Filters`` object that contains a list of queue IDs or queue ARNs, up to 100, or a list of Channels to use to filter the metrics returned in the response. Metric data is retrieved only for the resources associated with the IDs, ARNs, or Channels included in the filter. You can use both IDs and ARNs together in a request. Only VOICE is supported for Channel.
        
          To find the ARN for a queue, open the queue you want to use in the Amazon Connect Queue editor. The ARN for the queue is displayed in the address bar as part of the URL. For example, the queue ARN is the set of characters at the end of the URL, after \'id=\' such as ``arn:aws:connect:us-east-1:270923740243:instance/78fb859d-1b7d-44b1-8aa3-12f0835c5855/queue/1d1a4575-9618-40ab-bbeb-81e45795fe61`` . The queue ID is also included in the URL, and is the string after \'queue/\'.
        
          - **Queues** *(list) --* 
        
            A list of up to 100 queue IDs or queue ARNs to use to filter the metrics retrieved. You can include both IDs and ARNs in a request.
        
            - *(string) --* 
        
          - **Channels** *(list) --* 
        
            The Channel to use as a filter for the metrics returned. Only VOICE is supported.
        
            - *(string) --* 
        
        :type Groupings: list
        :param Groupings: 
        
          The grouping applied to the metrics returned. For example, when results are grouped by queueId, the metrics returned are grouped by queue. The values returned apply to the metrics for each queue rather than aggregated for all queues.
        
          The current version supports grouping by Queue
        
          If no ``Grouping`` is included in the request, a summary of ``HistoricalMetrics`` for all queues is returned.
        
          - *(string) --* 
        
        :type HistoricalMetrics: list
        :param HistoricalMetrics: **[REQUIRED]** 
        
          A list of ``HistoricalMetric`` objects that contain the metrics to retrieve with the request.
        
          A ``HistoricalMetric`` object contains: ``HistoricalMetricName`` , ``Statistic`` , ``Threshold`` , and ``Unit`` .
        
          For each historical metric you include in the request, you must include a ``Unit`` and a ``Statistic`` . 
        
          The following historical metrics are available:
        
            CONTACTS_QUEUED  
        
          Unit: COUNT
        
          Statistic: SUM
        
            CONTACTS_HANDLED  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_ABANDONED  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_CONSULTED  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_AGENT_HUNG_UP_FIRST  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_HANDLED_INCOMING  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_HANDLED_OUTBOUND  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_HOLD_ABANDONS  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_TRANSFERRED_IN  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_TRANSFERRED_OUT  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_TRANSFERRED_IN_FROM_QUEUE  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_TRANSFERRED_OUT_FROM_QUEUE  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CALLBACK_CONTACTS_HANDLED  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CALLBACK_CONTACTS_HANDLED  
        
          Unit: COUNT
        
          Statistics: SUM
        
            API_CONTACTS_HANDLED  
        
          Unit: COUNT
        
          Statistics: SUM
        
            CONTACTS_MISSED  
        
          Unit: COUNT
        
          Statistics: SUM
        
            OCCUPANCY  
        
          Unit: PERCENT
        
          Statistics: AVG
        
            HANDLE_TIME  
        
          Unit: SECONDS
        
          Statistics: AVG
        
            AFTER_CONTACT_WORK_TIME  
        
          Unit: SECONDS
        
          Statistics: AVG
        
            QUEUED_TIME  
        
          Unit: SECONDS
        
          Statistics: MAX
        
            ABANDON_TIME  
        
          Unit: COUNT
        
          Statistics: SUM
        
            QUEUE_ANSWER_TIME  
        
          Unit: SECONDS
        
          Statistics: AVG
        
            HOLD_TIME  
        
          Unit: SECONDS
        
          Statistics: AVG
        
            INTERACTION_TIME  
        
          Unit: SECONDS
        
          Statistics: AVG
        
            INTERACTION_AND_HOLD_TIME  
        
          Unit: SECONDS
        
          Statistics: AVG
        
            SERVICE_LEVEL  
        
          Unit: PERCENT
        
          Statistics: AVG
        
          Threshold: Only \"Less than\" comparisons are supported, with the following service level thresholds: 15, 20, 25, 30, 45, 60, 90, 120, 180, 240, 300, 600
        
          - *(dict) --* 
        
            A ``HistoricalMetric`` object that contains the Name, Unit, Statistic, and Threshold for the metric.
        
            - **Name** *(string) --* 
        
              The name of the historical metric.
        
            - **Threshold** *(dict) --* 
        
              The threshold for the metric, used with service level metrics.
        
              - **Comparison** *(string) --* 
        
                The Threshold to use to compare service level metrics to. Only \"Less than\" (LT) comparisons are supported.
        
              - **ThresholdValue** *(float) --* 
        
                The value of the threshold to compare the metric to. Only \"Less than\" (LT) comparisons are supported.
        
            - **Statistic** *(string) --* 
        
              The statistic for the metric: SUM, MAX, or SUM.
        
            - **Unit** *(string) --* 
        
              The unit for the metric: COUNT, PERCENT, or SECONDS.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Indicates the maximum number of results to return per page in the response, between 1-100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'MetricResults\': [
                    {
                        \'Dimensions\': {
                            \'Queue\': {
                                \'Id\': \'string\',
                                \'Arn\': \'string\'
                            },
                            \'Channel\': \'VOICE\'
                        },
                        \'Collections\': [
                            {
                                \'Metric\': {
                                    \'Name\': \'CONTACTS_QUEUED\'|\'CONTACTS_HANDLED\'|\'CONTACTS_ABANDONED\'|\'CONTACTS_CONSULTED\'|\'CONTACTS_AGENT_HUNG_UP_FIRST\'|\'CONTACTS_HANDLED_INCOMING\'|\'CONTACTS_HANDLED_OUTBOUND\'|\'CONTACTS_HOLD_ABANDONS\'|\'CONTACTS_TRANSFERRED_IN\'|\'CONTACTS_TRANSFERRED_OUT\'|\'CONTACTS_TRANSFERRED_IN_FROM_QUEUE\'|\'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE\'|\'CONTACTS_MISSED\'|\'CALLBACK_CONTACTS_HANDLED\'|\'API_CONTACTS_HANDLED\'|\'OCCUPANCY\'|\'HANDLE_TIME\'|\'AFTER_CONTACT_WORK_TIME\'|\'QUEUED_TIME\'|\'ABANDON_TIME\'|\'QUEUE_ANSWER_TIME\'|\'HOLD_TIME\'|\'INTERACTION_TIME\'|\'INTERACTION_AND_HOLD_TIME\'|\'SERVICE_LEVEL\',
                                    \'Threshold\': {
                                        \'Comparison\': \'LT\',
                                        \'ThresholdValue\': 123.0
                                    },
                                    \'Statistic\': \'SUM\'|\'MAX\'|\'AVG\',
                                    \'Unit\': \'SECONDS\'|\'COUNT\'|\'PERCENT\'
                                },
                                \'Value\': 123.0
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              A string returned in the response. Use the value returned in the response as the value of the NextToken in a subsequent request to retrieve the next set of results.
        
              The token expires after 5 minutes from the time it is created. Subsequent requests that use the NextToken must use the same request parameters as the request that generated the token. 
        
            - **MetricResults** *(list) --* 
        
              A list of ``HistoricalMetricResult`` objects, organized by ``Dimensions`` , which is the ID of the resource specified in the ``Filters`` used for the request. The metrics are combined with the metrics included in ``Collections`` , which is a list of ``HisotricalMetricData`` objects.
        
              If no ``Grouping`` is specified in the request, ``Collections`` includes summary data for the ``HistoricalMetrics`` .
        
              - *(dict) --* 
        
                The metrics data returned from a ``GetMetricData`` operation.
        
                - **Dimensions** *(dict) --* 
        
                  The ``Dimensions`` for the metrics.
        
                  - **Queue** *(dict) --* 
        
                    A ``QueueReference`` object used as one part of dimension for the metrics results.
        
                    - **Id** *(string) --* 
        
                      The ID of the queue associated with the metrics returned.
        
                    - **Arn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of queue.
        
                  - **Channel** *(string) --* 
        
                    The channel used for grouping and filters. Only VOICE is supported.
        
                - **Collections** *(list) --* 
        
                  A list of ``HistoricalMetricData`` objects.
        
                  - *(dict) --* 
        
                    A ``HistoricalMetricData`` object than contains a ``Metric`` and a ``Value`` .
        
                    - **Metric** *(dict) --* 
        
                      A ``HistoricalMetric`` object.
        
                      - **Name** *(string) --* 
        
                        The name of the historical metric.
        
                      - **Threshold** *(dict) --* 
        
                        The threshold for the metric, used with service level metrics.
        
                        - **Comparison** *(string) --* 
        
                          The Threshold to use to compare service level metrics to. Only \"Less than\" (LT) comparisons are supported.
        
                        - **ThresholdValue** *(float) --* 
        
                          The value of the threshold to compare the metric to. Only \"Less than\" (LT) comparisons are supported.
        
                      - **Statistic** *(string) --* 
        
                        The statistic for the metric: SUM, MAX, or SUM.
        
                      - **Unit** *(string) --* 
        
                        The unit for the metric: COUNT, PERCENT, or SECONDS.
        
                    - **Value** *(float) --* 
        
                      The ``Value`` of the metric.
        
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_routing_profiles(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListRoutingProfiles>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_routing_profiles(
              InstanceId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of routing profiles to return in the response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RoutingProfileSummaryList\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RoutingProfileSummaryList** *(list) --* 
        
              An array of ``RoutingProfileSummary`` objects that include the ARN, Id, and Name of the routing profile.
        
              - *(dict) --* 
        
                A ``RoutingProfileSummary`` object that contains information about a routing profile, including ARN, Id, and Name.
        
                - **Id** *(string) --* 
        
                  The identifier of the routing profile.
        
                - **Arn** *(string) --* 
        
                  The ARN of the routing profile.
        
                - **Name** *(string) --* 
        
                  The name of the routing profile.
        
            - **NextToken** *(string) --* 
        
              A string returned in the response. Use the value returned in the response as the value of the NextToken in a subsequent request to retrieve the next set of results.
        
        """
        pass

    def list_security_profiles(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListSecurityProfiles>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_security_profiles(
              InstanceId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of security profiles to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SecurityProfileSummaryList\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SecurityProfileSummaryList** *(list) --* 
        
              An array of ``SecurityProfileSummary`` objects.
        
              - *(dict) --* 
        
                A ``SecurityProfileSummary`` object that contains information about a security profile, including ARN, Id, Name.
        
                - **Id** *(string) --* 
        
                  The identifier of the security profile.
        
                - **Arn** *(string) --* 
        
                  The ARN of the security profile.
        
                - **Name** *(string) --* 
        
                  The name of the security profile.
        
            - **NextToken** *(string) --* 
        
              A string returned in the response. Use the value returned in the response as the value of the NextToken in a subsequent request to retrieve the next set of results.
        
        """
        pass

    def list_user_hierarchy_groups(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListUserHierarchyGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_user_hierarchy_groups(
              InstanceId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of hierarchy groups to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserHierarchyGroupSummaryList\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UserHierarchyGroupSummaryList** *(list) --* 
        
              An array of ``HierarchyGroupSummary`` objects.
        
              - *(dict) --* 
        
                A ``HierarchyGroupSummary`` object that contains information about the hierarchy group, including ARN, Id, and Name.
        
                - **Id** *(string) --* 
        
                  The identifier of the hierarchy group.
        
                - **Arn** *(string) --* 
        
                  The ARN for the hierarchy group.
        
                - **Name** *(string) --* 
        
                  The name of the hierarchy group.
        
            - **NextToken** *(string) --* 
        
              A string returned in the response. Use the value returned in the response as the value of the NextToken in a subsequent request to retrieve the next set of results.
        
        """
        pass

    def list_users(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListUsers>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_users(
              InstanceId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in the response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserSummaryList\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Username\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UserSummaryList** *(list) --* 
        
              An array of ``UserSummary`` objects that contain information about the users in your instance.
        
              - *(dict) --* 
        
                A ``UserSummary`` object that contains Information about a user, including ARN, Id, and user name.
        
                - **Id** *(string) --* 
        
                  The identifier for the user account.
        
                - **Arn** *(string) --* 
        
                  The ARN for the user account.
        
                - **Username** *(string) --* 
        
                  The Amazon Connect user name for the user account.
        
            - **NextToken** *(string) --* 
        
              A string returned in the response. Use the value returned in the response as the value of the NextToken in a subsequent request to retrieve the next set of results.
        
        """
        pass

    def start_outbound_voice_contact(self, DestinationPhoneNumber: str, ContactFlowId: str, InstanceId: str, ClientToken: str = None, SourcePhoneNumber: str = None, QueueId: str = None, Attributes: Dict = None) -> Dict:
        """
        
        If you are using an IAM account, it must have permission to the ``connect:StartOutboundVoiceContact`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/StartOutboundVoiceContact>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_outbound_voice_contact(
              DestinationPhoneNumber=\'string\',
              ContactFlowId=\'string\',
              InstanceId=\'string\',
              ClientToken=\'string\',
              SourcePhoneNumber=\'string\',
              QueueId=\'string\',
              Attributes={
                  \'string\': \'string\'
              }
          )
        :type DestinationPhoneNumber: string
        :param DestinationPhoneNumber: **[REQUIRED]** 
        
          The phone number of the customer in E.164 format.
        
        :type ContactFlowId: string
        :param ContactFlowId: **[REQUIRED]** 
        
          The identifier for the contact flow to connect the outbound call to.
        
          To find the ``ContactFlowId`` , open the contact flow you want to use in the Amazon Connect contact flow editor. The ID for the contact flow is displayed in the address bar as part of the URL. For example, the contact flow ID is the set of characters at the end of the URL, after \'contact-flow/\' such as ``78ea8fd5-2659-4f2b-b528-699760ccfc1b`` .
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type ClientToken: string
        :param ClientToken: 
        
          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned. If the contact is disconnected, a new contact is started.
        
          This field is autopopulated if not provided.
        
        :type SourcePhoneNumber: string
        :param SourcePhoneNumber: 
        
          The phone number, in E.164 format, associated with your Amazon Connect instance to use for the outbound call.
        
        :type QueueId: string
        :param QueueId: 
        
          The queue to add the call to. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue used will be the queue defined in the contact flow.
        
          To find the ``QueueId`` , open the queue you want to use in the Amazon Connect Queue editor. The ID for the queue is displayed in the address bar as part of the URL. For example, the queue ID is the set of characters at the end of the URL, after \'queue/\' such as ``queue/aeg40574-2d01-51c3-73d6-bf8624d2168c`` .
        
        :type Attributes: dict
        :param Attributes: 
        
          Specify a custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in contact flows just like any other contact attributes.
        
          There can be up to 32,768 UTF-8 bytes across all key-value pairs. Attribute keys can include only alphanumeric, dash, and underscore characters.
        
          For example, if you want play a greeting when the customer answers the call, you can pass the customer name in attributes similar to the following:
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ContactId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ContactId** *(string) --* 
        
              The unique identifier of this contact within your Amazon Connect instance.
        
        """
        pass

    def stop_contact(self, ContactId: str, InstanceId: str) -> Dict:
        """
        
        If you are using an IAM account, it must have permission to the ``connect:StopContact`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/StopContact>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_contact(
              ContactId=\'string\',
              InstanceId=\'string\'
          )
        :type ContactId: string
        :param ContactId: **[REQUIRED]** 
        
          The unique identifier of the contact to end.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_contact_attributes(self, InitialContactId: str, InstanceId: str, Attributes: Dict) -> Dict:
        """
        
        Contact attributes are available in Amazon Connect for 24 months, and are then deleted.
        
         *Important:*  
        
        You cannot use the operation to update attributes for contacts that occurred prior to the release of the API, September 12, 2018. You can update attributes only for contacts that started after the release of the API. If you attempt to update attributes for a contact that occurred prior to the release of the API, a 400 error is returned. This applies also to queued callbacks that were initiated prior to the release of the API but are still active in your instance.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateContactAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_contact_attributes(
              InitialContactId=\'string\',
              InstanceId=\'string\',
              Attributes={
                  \'string\': \'string\'
              }
          )
        :type InitialContactId: string
        :param InitialContactId: **[REQUIRED]** 
        
          The unique identifier of the contact for which to update attributes. This is the identifier for the contact associated with the first interaction with the contact center.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :type Attributes: dict
        :param Attributes: **[REQUIRED]** 
        
          The key-value pairs for the attribute to update.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_user_hierarchy(self, UserId: str, InstanceId: str, HierarchyGroupId: str = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserHierarchy>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_user_hierarchy(
              HierarchyGroupId=\'string\',
              UserId=\'string\',
              InstanceId=\'string\'
          )
        :type HierarchyGroupId: string
        :param HierarchyGroupId: 
        
          The identifier for the hierarchy group to assign to the user.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The identifier of the user account to assign the hierarchy group to.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :returns: None
        """
        pass

    def update_user_identity_info(self, IdentityInfo: Dict, UserId: str, InstanceId: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserIdentityInfo>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_user_identity_info(
              IdentityInfo={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'Email\': \'string\'
              },
              UserId=\'string\',
              InstanceId=\'string\'
          )
        :type IdentityInfo: dict
        :param IdentityInfo: **[REQUIRED]** 
        
          A ``UserIdentityInfo`` object.
        
          - **FirstName** *(string) --* 
        
            The first name used in the user account. This is required if you are using Amazon Connect or SAML for identity management.
        
          - **LastName** *(string) --* 
        
            The last name used in the user account. This is required if you are using Amazon Connect or SAML for identity management.
        
          - **Email** *(string) --* 
        
            The email address added to the user account. If you are using SAML for identity management and include this parameter, an ``InvalidRequestException`` is returned.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The identifier for the user account to update identity information for.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :returns: None
        """
        pass

    def update_user_phone_config(self, PhoneConfig: Dict, UserId: str, InstanceId: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserPhoneConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_user_phone_config(
              PhoneConfig={
                  \'PhoneType\': \'SOFT_PHONE\'|\'DESK_PHONE\',
                  \'AutoAccept\': True|False,
                  \'AfterContactWorkTimeLimit\': 123,
                  \'DeskPhoneNumber\': \'string\'
              },
              UserId=\'string\',
              InstanceId=\'string\'
          )
        :type PhoneConfig: dict
        :param PhoneConfig: **[REQUIRED]** 
        
          A ``UserPhoneConfig`` object that contains settings for ``AfterContactWorkTimeLimit`` , ``AutoAccept`` , ``DeskPhoneNumber`` , and ``PhoneType`` to assign to the user.
        
          - **PhoneType** *(string) --* **[REQUIRED]** 
        
            The phone type selected for the user, either Soft phone or Desk phone.
        
          - **AutoAccept** *(boolean) --* 
        
            The Auto accept setting for the user, Yes or No.
        
          - **AfterContactWorkTimeLimit** *(integer) --* 
        
            The After Call Work (ACW) timeout setting, in seconds, for the user.
        
          - **DeskPhoneNumber** *(string) --* 
        
            The phone number for the user\'s desk phone.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The identifier for the user account to change phone settings for.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :returns: None
        """
        pass

    def update_user_routing_profile(self, RoutingProfileId: str, UserId: str, InstanceId: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserRoutingProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_user_routing_profile(
              RoutingProfileId=\'string\',
              UserId=\'string\',
              InstanceId=\'string\'
          )
        :type RoutingProfileId: string
        :param RoutingProfileId: **[REQUIRED]** 
        
          The identifier of the routing profile to assign to the user.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The identifier for the user account to assign the routing profile to.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :returns: None
        """
        pass

    def update_user_security_profiles(self, SecurityProfileIds: List, UserId: str, InstanceId: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserSecurityProfiles>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_user_security_profiles(
              SecurityProfileIds=[
                  \'string\',
              ],
              UserId=\'string\',
              InstanceId=\'string\'
          )
        :type SecurityProfileIds: list
        :param SecurityProfileIds: **[REQUIRED]** 
        
          The identifiers for the security profiles to assign to the user.
        
          - *(string) --* 
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The identifier of the user account to assign the security profiles.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        
        :returns: None
        """
        pass
