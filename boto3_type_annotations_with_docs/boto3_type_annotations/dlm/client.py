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

    def create_lifecycle_policy(self, ExecutionRoleArn: str, Description: str, State: str, PolicyDetails: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dlm-2018-01-12/CreateLifecyclePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_lifecycle_policy(
              ExecutionRoleArn=\'string\',
              Description=\'string\',
              State=\'ENABLED\'|\'DISABLED\',
              PolicyDetails={
                  \'ResourceTypes\': [
                      \'VOLUME\',
                  ],
                  \'TargetTags\': [
                      {
                          \'Key\': \'string\',
                          \'Value\': \'string\'
                      },
                  ],
                  \'Schedules\': [
                      {
                          \'Name\': \'string\',
                          \'CopyTags\': True|False,
                          \'TagsToAdd\': [
                              {
                                  \'Key\': \'string\',
                                  \'Value\': \'string\'
                              },
                          ],
                          \'CreateRule\': {
                              \'Interval\': 123,
                              \'IntervalUnit\': \'HOURS\',
                              \'Times\': [
                                  \'string\',
                              ]
                          },
                          \'RetainRule\': {
                              \'Count\': 123
                          }
                      },
                  ]
              }
          )
        :type ExecutionRoleArn: string
        :param ExecutionRoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported.
        
        :type State: string
        :param State: **[REQUIRED]** 
        
          The desired activation state of the lifecycle policy after creation.
        
        :type PolicyDetails: dict
        :param PolicyDetails: **[REQUIRED]** 
        
          The configuration details of the lifecycle policy.
        
          Target tags cannot be re-used across lifecycle policies.
        
          - **ResourceTypes** *(list) --* 
        
            The resource type.
        
            - *(string) --* 
        
          - **TargetTags** *(list) --* 
        
            The single tag that identifies targeted resources for this policy.
        
            - *(dict) --* 
        
              Specifies a tag for a resource.
        
              - **Key** *(string) --* **[REQUIRED]** 
        
                The tag key.
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                The tag value.
        
          - **Schedules** *(list) --* 
        
            The schedule of policy-defined actions.
        
            - *(dict) --* 
        
              Specifies a schedule.
        
              - **Name** *(string) --* 
        
                The name of the schedule.
        
              - **CopyTags** *(boolean) --* 
        
              - **TagsToAdd** *(list) --* 
        
                The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.
        
                - *(dict) --* 
        
                  Specifies a tag for a resource.
        
                  - **Key** *(string) --* **[REQUIRED]** 
        
                    The tag key.
        
                  - **Value** *(string) --* **[REQUIRED]** 
        
                    The tag value.
        
              - **CreateRule** *(dict) --* 
        
                The create rule.
        
                - **Interval** *(integer) --* **[REQUIRED]** 
        
                  The interval. The supported values are 12 and 24.
        
                - **IntervalUnit** *(string) --* **[REQUIRED]** 
        
                  The interval unit.
        
                - **Times** *(list) --* 
        
                  The time, in UTC, to start the operation.
        
                  The operation occurs within a one-hour window following the specified time.
        
                  - *(string) --* 
        
              - **RetainRule** *(dict) --* 
        
                The retain rule.
        
                - **Count** *(integer) --* **[REQUIRED]** 
        
                  The number of snapshots to keep for each volume, up to a maximum of 1000.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PolicyId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PolicyId** *(string) --* 
        
              The identifier of the lifecycle policy.
        
        """
        pass

    def delete_lifecycle_policy(self, PolicyId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dlm-2018-01-12/DeleteLifecyclePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_lifecycle_policy(
              PolicyId=\'string\'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The identifier of the lifecycle policy.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
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

    def get_lifecycle_policies(self, PolicyIds: List = None, State: str = None, ResourceTypes: List = None, TargetTags: List = None, TagsToAdd: List = None) -> Dict:
        """
        
        To get complete information about a policy, use  GetLifecyclePolicy .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dlm-2018-01-12/GetLifecyclePolicies>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_lifecycle_policies(
              PolicyIds=[
                  \'string\',
              ],
              State=\'ENABLED\'|\'DISABLED\'|\'ERROR\',
              ResourceTypes=[
                  \'VOLUME\',
              ],
              TargetTags=[
                  \'string\',
              ],
              TagsToAdd=[
                  \'string\',
              ]
          )
        :type PolicyIds: list
        :param PolicyIds: 
        
          The identifiers of the data lifecycle policies.
        
          - *(string) --* 
        
        :type State: string
        :param State: 
        
          The activation state.
        
        :type ResourceTypes: list
        :param ResourceTypes: 
        
          The resource type.
        
          - *(string) --* 
        
        :type TargetTags: list
        :param TargetTags: 
        
          The target tag for a policy.
        
          Tags are strings in the format ``key=value`` .
        
          - *(string) --* 
        
        :type TagsToAdd: list
        :param TagsToAdd: 
        
          The tags to add to objects created by the policy.
        
          Tags are strings in the format ``key=value`` .
        
          These user-defined tags are added in addition to the AWS-added lifecycle tags.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policies\': [
                    {
                        \'PolicyId\': \'string\',
                        \'Description\': \'string\',
                        \'State\': \'ENABLED\'|\'DISABLED\'|\'ERROR\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policies** *(list) --* 
        
              Summary information about the lifecycle policies.
        
              - *(dict) --* 
        
                Summary information about a lifecycle policy.
        
                - **PolicyId** *(string) --* 
        
                  The identifier of the lifecycle policy.
        
                - **Description** *(string) --* 
        
                  The description of the lifecycle policy.
        
                - **State** *(string) --* 
        
                  The activation state of the lifecycle policy.
        
        """
        pass

    def get_lifecycle_policy(self, PolicyId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dlm-2018-01-12/GetLifecyclePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_lifecycle_policy(
              PolicyId=\'string\'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The identifier of the lifecycle policy.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policy\': {
                    \'PolicyId\': \'string\',
                    \'Description\': \'string\',
                    \'State\': \'ENABLED\'|\'DISABLED\'|\'ERROR\',
                    \'ExecutionRoleArn\': \'string\',
                    \'DateCreated\': datetime(2015, 1, 1),
                    \'DateModified\': datetime(2015, 1, 1),
                    \'PolicyDetails\': {
                        \'ResourceTypes\': [
                            \'VOLUME\',
                        ],
                        \'TargetTags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'Schedules\': [
                            {
                                \'Name\': \'string\',
                                \'CopyTags\': True|False,
                                \'TagsToAdd\': [
                                    {
                                        \'Key\': \'string\',
                                        \'Value\': \'string\'
                                    },
                                ],
                                \'CreateRule\': {
                                    \'Interval\': 123,
                                    \'IntervalUnit\': \'HOURS\',
                                    \'Times\': [
                                        \'string\',
                                    ]
                                },
                                \'RetainRule\': {
                                    \'Count\': 123
                                }
                            },
                        ]
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policy** *(dict) --* 
        
              Detailed information about the lifecycle policy.
        
              - **PolicyId** *(string) --* 
        
                The identifier of the lifecycle policy.
        
              - **Description** *(string) --* 
        
                The description of the lifecycle policy.
        
              - **State** *(string) --* 
        
                The activation state of the lifecycle policy.
        
              - **ExecutionRoleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
        
              - **DateCreated** *(datetime) --* 
        
                The local date and time when the lifecycle policy was created.
        
              - **DateModified** *(datetime) --* 
        
                The local date and time when the lifecycle policy was last modified.
        
              - **PolicyDetails** *(dict) --* 
        
                The configuration of the lifecycle policy
        
                - **ResourceTypes** *(list) --* 
        
                  The resource type.
        
                  - *(string) --* 
              
                - **TargetTags** *(list) --* 
        
                  The single tag that identifies targeted resources for this policy.
        
                  - *(dict) --* 
        
                    Specifies a tag for a resource.
        
                    - **Key** *(string) --* 
        
                      The tag key.
        
                    - **Value** *(string) --* 
        
                      The tag value.
        
                - **Schedules** *(list) --* 
        
                  The schedule of policy-defined actions.
        
                  - *(dict) --* 
        
                    Specifies a schedule.
        
                    - **Name** *(string) --* 
        
                      The name of the schedule.
        
                    - **CopyTags** *(boolean) --* 
                    
                    - **TagsToAdd** *(list) --* 
        
                      The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.
        
                      - *(dict) --* 
        
                        Specifies a tag for a resource.
        
                        - **Key** *(string) --* 
        
                          The tag key.
        
                        - **Value** *(string) --* 
        
                          The tag value.
        
                    - **CreateRule** *(dict) --* 
        
                      The create rule.
        
                      - **Interval** *(integer) --* 
        
                        The interval. The supported values are 12 and 24.
        
                      - **IntervalUnit** *(string) --* 
        
                        The interval unit.
        
                      - **Times** *(list) --* 
        
                        The time, in UTC, to start the operation.
        
                        The operation occurs within a one-hour window following the specified time.
        
                        - *(string) --* 
                    
                    - **RetainRule** *(dict) --* 
        
                      The retain rule.
        
                      - **Count** *(integer) --* 
        
                        The number of snapshots to keep for each volume, up to a maximum of 1000.
        
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

    def update_lifecycle_policy(self, PolicyId: str, ExecutionRoleArn: str = None, State: str = None, Description: str = None, PolicyDetails: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dlm-2018-01-12/UpdateLifecyclePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_lifecycle_policy(
              PolicyId=\'string\',
              ExecutionRoleArn=\'string\',
              State=\'ENABLED\'|\'DISABLED\',
              Description=\'string\',
              PolicyDetails={
                  \'ResourceTypes\': [
                      \'VOLUME\',
                  ],
                  \'TargetTags\': [
                      {
                          \'Key\': \'string\',
                          \'Value\': \'string\'
                      },
                  ],
                  \'Schedules\': [
                      {
                          \'Name\': \'string\',
                          \'CopyTags\': True|False,
                          \'TagsToAdd\': [
                              {
                                  \'Key\': \'string\',
                                  \'Value\': \'string\'
                              },
                          ],
                          \'CreateRule\': {
                              \'Interval\': 123,
                              \'IntervalUnit\': \'HOURS\',
                              \'Times\': [
                                  \'string\',
                              ]
                          },
                          \'RetainRule\': {
                              \'Count\': 123
                          }
                      },
                  ]
              }
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The identifier of the lifecycle policy.
        
        :type ExecutionRoleArn: string
        :param ExecutionRoleArn: 
        
          The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
        
        :type State: string
        :param State: 
        
          The desired activation state of the lifecycle policy after creation.
        
        :type Description: string
        :param Description: 
        
          A description of the lifecycle policy.
        
        :type PolicyDetails: dict
        :param PolicyDetails: 
        
          The configuration of the lifecycle policy.
        
          Target tags cannot be re-used across policies.
        
          - **ResourceTypes** *(list) --* 
        
            The resource type.
        
            - *(string) --* 
        
          - **TargetTags** *(list) --* 
        
            The single tag that identifies targeted resources for this policy.
        
            - *(dict) --* 
        
              Specifies a tag for a resource.
        
              - **Key** *(string) --* **[REQUIRED]** 
        
                The tag key.
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                The tag value.
        
          - **Schedules** *(list) --* 
        
            The schedule of policy-defined actions.
        
            - *(dict) --* 
        
              Specifies a schedule.
        
              - **Name** *(string) --* 
        
                The name of the schedule.
        
              - **CopyTags** *(boolean) --* 
        
              - **TagsToAdd** *(list) --* 
        
                The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.
        
                - *(dict) --* 
        
                  Specifies a tag for a resource.
        
                  - **Key** *(string) --* **[REQUIRED]** 
        
                    The tag key.
        
                  - **Value** *(string) --* **[REQUIRED]** 
        
                    The tag value.
        
              - **CreateRule** *(dict) --* 
        
                The create rule.
        
                - **Interval** *(integer) --* **[REQUIRED]** 
        
                  The interval. The supported values are 12 and 24.
        
                - **IntervalUnit** *(string) --* **[REQUIRED]** 
        
                  The interval unit.
        
                - **Times** *(list) --* 
        
                  The time, in UTC, to start the operation.
        
                  The operation occurs within a one-hour window following the specified time.
        
                  - *(string) --* 
        
              - **RetainRule** *(dict) --* 
        
                The retain rule.
        
                - **Count** *(integer) --* **[REQUIRED]** 
        
                  The number of snapshots to keep for each volume, up to a maximum of 1000.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
