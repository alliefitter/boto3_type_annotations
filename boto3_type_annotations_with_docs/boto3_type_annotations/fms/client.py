from typing import Optional
from typing import Union
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_admin_account(self, AdminAccount: str):
        """
        
        The account that you associate with AWS Firewall Manager is called the AWS Firewall Manager administrator account. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/AssociateAdminAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_admin_account(
              AdminAccount=\'string\'
          )
        :type AdminAccount: string
        :param AdminAccount: **[REQUIRED]** 
        
          The AWS account ID to associate with AWS Firewall Manager as the AWS Firewall Manager administrator account. This can be an AWS Organizations master account or a member account. For more information about AWS Organizations and master accounts, see `Managing the AWS Accounts in Your Organization <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html>`__ .
        
        :returns: None
        """
        pass

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

    def delete_notification_channel(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DeleteNotificationChannel>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_notification_channel()
          
        :returns: None
        """
        pass

    def delete_policy(self, PolicyId: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DeletePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_policy(
              PolicyId=\'string\'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The ID of the policy that you want to delete. ``PolicyId`` is returned by ``PutPolicy`` and by ``ListPolicies`` .
        
        :returns: None
        """
        pass

    def disassociate_admin_account(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DisassociateAdminAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_admin_account()
          
        :returns: None
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

    def get_admin_account(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetAdminAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_admin_account()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AdminAccount\': \'string\',
                \'RoleStatus\': \'READY\'|\'CREATING\'|\'PENDING_DELETION\'|\'DELETING\'|\'DELETED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AdminAccount** *(string) --* 
        
              The AWS account that is set as the AWS Firewall Manager administrator.
        
            - **RoleStatus** *(string) --* 
        
              The status of the AWS account that you set as the AWS Firewall Manager administrator.
        
        """
        pass

    def get_compliance_detail(self, PolicyId: str, MemberAccount: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetComplianceDetail>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_compliance_detail(
              PolicyId=\'string\',
              MemberAccount=\'string\'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The ID of the policy that you want to get the details for. ``PolicyId`` is returned by ``PutPolicy`` and by ``ListPolicies`` .
        
        :type MemberAccount: string
        :param MemberAccount: **[REQUIRED]** 
        
          The AWS account that owns the resources that you want to get the details for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PolicyComplianceDetail\': {
                    \'PolicyOwner\': \'string\',
                    \'PolicyId\': \'string\',
                    \'MemberAccount\': \'string\',
                    \'Violators\': [
                        {
                            \'ResourceId\': \'string\',
                            \'ViolationReason\': \'WEB_ACL_MISSING_RULE_GROUP\'|\'RESOURCE_MISSING_WEB_ACL\'|\'RESOURCE_INCORRECT_WEB_ACL\',
                            \'ResourceType\': \'string\'
                        },
                    ],
                    \'EvaluationLimitExceeded\': True|False,
                    \'ExpiredAt\': datetime(2015, 1, 1),
                    \'IssueInfoMap\': {
                        \'string\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PolicyComplianceDetail** *(dict) --* 
        
              Information about the resources and the policy that you specified in the ``GetComplianceDetail`` request.
        
              - **PolicyOwner** *(string) --* 
        
                The AWS account that created the AWS Firewall Manager policy.
        
              - **PolicyId** *(string) --* 
        
                The ID of the AWS Firewall Manager policy.
        
              - **MemberAccount** *(string) --* 
        
                The AWS account ID.
        
              - **Violators** *(list) --* 
        
                An array of resources that are not protected by the policy.
        
                - *(dict) --* 
        
                  Details of the resource that is not protected by the policy.
        
                  - **ResourceId** *(string) --* 
        
                    The resource ID.
        
                  - **ViolationReason** *(string) --* 
        
                    The reason that the resource is not protected by the policy.
        
                  - **ResourceType** *(string) --* 
        
                    The resource type. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
              - **EvaluationLimitExceeded** *(boolean) --* 
        
                Indicates if over 100 resources are non-compliant with the AWS Firewall Manager policy.
        
              - **ExpiredAt** *(datetime) --* 
        
                A time stamp that indicates when the returned information should be considered out-of-date.
        
              - **IssueInfoMap** *(dict) --* 
        
                Details about problems with dependent services, such as AWS WAF or AWS Config, that are causing a resource to be non-compliant. The details include the name of the dependent service and the error message recieved indicating the problem with the service.
        
                - *(string) --* 
                  
                  - *(string) --* 
            
        """
        pass

    def get_notification_channel(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetNotificationChannel>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_notification_channel()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SnsTopicArn\': \'string\',
                \'SnsRoleName\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SnsTopicArn** *(string) --* 
        
              The SNS topic that records AWS Firewall Manager activity. 
        
            - **SnsRoleName** *(string) --* 
        
              The IAM role that is used by AWS Firewall Manager to record activity to SNS.
        
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

    def get_policy(self, PolicyId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_policy(
              PolicyId=\'string\'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The ID of the AWS Firewall Manager policy that you want the details for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policy\': {
                    \'PolicyId\': \'string\',
                    \'PolicyName\': \'string\',
                    \'PolicyUpdateToken\': \'string\',
                    \'SecurityServicePolicyData\': {
                        \'Type\': \'WAF\',
                        \'ManagedServiceData\': \'string\'
                    },
                    \'ResourceType\': \'string\',
                    \'ResourceTags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'ExcludeResourceTags\': True|False,
                    \'RemediationEnabled\': True|False,
                    \'IncludeMap\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'ExcludeMap\': {
                        \'string\': [
                            \'string\',
                        ]
                    }
                },
                \'PolicyArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policy** *(dict) --* 
        
              Information about the specified AWS Firewall Manager policy.
        
              - **PolicyId** *(string) --* 
        
                The ID of the AWS Firewall Manager policy.
        
              - **PolicyName** *(string) --* 
        
                The friendly name of the AWS Firewall Manager policy.
        
              - **PolicyUpdateToken** *(string) --* 
        
                A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request, the ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the current policy version. To get the ``PolicyUpdateToken`` of the current policy version, use a ``GetPolicy`` request.
        
              - **SecurityServicePolicyData** *(dict) --* 
        
                Details about the security service that is being used to protect the resources.
        
                - **Type** *(string) --* 
        
                  The service that the policy is using to protect the resources. This value is ``WAF`` .
        
                - **ManagedServiceData** *(string) --* 
        
                  Details about the service. This contains ``WAF`` data in JSON format, as shown in the following example:
        
                   ``ManagedServiceData\": \"{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\": \\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}``  
        
              - **ResourceType** *(string) --* 
        
                The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
              - **ResourceTags** *(list) --* 
        
                An array of ``ResourceTag`` objects.
        
                - *(dict) --* 
        
                  The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from protection by the AWS Firewall Manager policy. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. Tags are combined with an \"OR.\" That is, if you add more than one tag, if any of the tags matches, the resource is considered a match for the include or exclude. `Working with Tag Editor <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .
        
                  - **Key** *(string) --* 
        
                    The resource tag key.
        
                  - **Value** *(string) --* 
        
                    The resource tag value.
        
              - **ExcludeResourceTags** *(boolean) --* 
        
                If set to ``True`` , resources with the tags that are specified in the ``ResourceTag`` array are not protected by the policy. If set to ``False`` , and the ``ResourceTag`` array is not null, only resources with the specified tags are associated with the policy.
        
              - **RemediationEnabled** *(boolean) --* 
        
                Indicates if the policy should be automatically applied to new resources.
        
              - **IncludeMap** *(dict) --* 
        
                Specifies the AWS account IDs to include in the policy. If ``IncludeMap`` is null, all accounts in the AWS Organization are included in the policy. If ``IncludeMap`` is not null, only values listed in ``IncludeMap`` will be included in the policy.
        
                The key to the map is ``ACCOUNT`` . For example, a valid ``IncludeMap`` would be ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **ExcludeMap** *(dict) --* 
        
                Specifies the AWS account IDs to exclude from the policy. The ``IncludeMap`` values are evaluated first, with all of the appropriate account IDs added to the policy. Then the accounts listed in ``ExcludeMap`` are removed, resulting in the final list of accounts to add to the policy.
        
                The key to the map is ``ACCOUNT`` . For example, a valid ``ExcludeMap`` would be ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
            - **PolicyArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the specified policy.
        
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

    def list_compliance_status(self, PolicyId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListComplianceStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_compliance_status(
              PolicyId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The ID of the AWS Firewall Manager policy that you want the details for.
        
        :type NextToken: string
        :param NextToken: 
        
          If you specify a value for ``MaxResults`` and you have more ``PolicyComplianceStatus`` objects than the number that you specify for ``MaxResults`` , AWS Firewall Manager returns a ``NextToken`` value in the response that allows you to list another group of ``PolicyComplianceStatus`` objects. For the second and subsequent ``ListComplianceStatus`` requests, specify the value of ``NextToken`` from the previous response to get information about another batch of ``PolicyComplianceStatus`` objects.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Specifies the number of ``PolicyComplianceStatus`` objects that you want AWS Firewall Manager to return for this request. If you have more ``PolicyComplianceStatus`` objects than the number that you specify for ``MaxResults`` , the response includes a ``NextToken`` value that you can use to get another batch of ``PolicyComplianceStatus`` objects.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PolicyComplianceStatusList\': [
                    {
                        \'PolicyOwner\': \'string\',
                        \'PolicyId\': \'string\',
                        \'PolicyName\': \'string\',
                        \'MemberAccount\': \'string\',
                        \'EvaluationResults\': [
                            {
                                \'ComplianceStatus\': \'COMPLIANT\'|\'NON_COMPLIANT\',
                                \'ViolatorCount\': 123,
                                \'EvaluationLimitExceeded\': True|False
                            },
                        ],
                        \'LastUpdated\': datetime(2015, 1, 1),
                        \'IssueInfoMap\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PolicyComplianceStatusList** *(list) --* 
        
              An array of ``PolicyComplianceStatus`` objects.
        
              - *(dict) --* 
        
                Indicates whether the account is compliant with the specified policy. An account is considered non-compliant if it includes resources that are not protected by the policy.
        
                - **PolicyOwner** *(string) --* 
        
                  The AWS account that created the AWS Firewall Manager policy.
        
                - **PolicyId** *(string) --* 
        
                  The ID of the AWS Firewall Manager policy.
        
                - **PolicyName** *(string) --* 
        
                  The friendly name of the AWS Firewall Manager policy.
        
                - **MemberAccount** *(string) --* 
        
                  The member account ID.
        
                - **EvaluationResults** *(list) --* 
        
                  An array of ``EvaluationResult`` objects.
        
                  - *(dict) --* 
        
                    Describes the compliance status for the account. An account is considered non-compliant if it includes resources that are not protected by the specified policy.
        
                    - **ComplianceStatus** *(string) --* 
        
                      Describes an AWS account\'s compliance with the AWS Firewall Manager policy.
        
                    - **ViolatorCount** *(integer) --* 
        
                      Number of resources that are non-compliant with the specified policy. A resource is considered non-compliant if it is not associated with the specified policy.
        
                    - **EvaluationLimitExceeded** *(boolean) --* 
        
                      Indicates that over 100 resources are non-compliant with the AWS Firewall Manager policy.
        
                - **LastUpdated** *(datetime) --* 
        
                  Time stamp of the last update to the ``EvaluationResult`` objects.
        
                - **IssueInfoMap** *(dict) --* 
        
                  Details about problems with dependent services, such as AWS WAF or AWS Config, that are causing a resource to be non-compliant. The details include the name of the dependent service and the error message recieved indicating the problem with the service.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              If you have more ``PolicyComplianceStatus`` objects than the number that you specified for ``MaxResults`` in the request, the response includes a ``NextToken`` value. To list more ``PolicyComplianceStatus`` objects, submit another ``ListComplianceStatus`` request, and specify the ``NextToken`` value from the response in the ``NextToken`` value in the next request.
        
        """
        pass

    def list_member_accounts(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        The ``ListMemberAccounts`` must be submitted by the account that is set as the AWS Firewall Manager administrator.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListMemberAccounts>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_member_accounts(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          If you specify a value for ``MaxResults`` and you have more account IDs than the number that you specify for ``MaxResults`` , AWS Firewall Manager returns a ``NextToken`` value in the response that allows you to list another group of IDs. For the second and subsequent ``ListMemberAccountsRequest`` requests, specify the value of ``NextToken`` from the previous response to get information about another batch of member account IDs.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Specifies the number of member account IDs that you want AWS Firewall Manager to return for this request. If you have more IDs than the number that you specify for ``MaxResults`` , the response includes a ``NextToken`` value that you can use to get another batch of member account IDs. The maximum value for ``MaxResults`` is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'MemberAccounts\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **MemberAccounts** *(list) --* 
        
              An array of account IDs.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              If you have more member account IDs than the number that you specified for ``MaxResults`` in the request, the response includes a ``NextToken`` value. To list more IDs, submit another ``ListMemberAccounts`` request, and specify the ``NextToken`` value from the response in the ``NextToken`` value in the next request.
        
        """
        pass

    def list_policies(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListPolicies>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_policies(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          If you specify a value for ``MaxResults`` and you have more ``PolicySummary`` objects than the number that you specify for ``MaxResults`` , AWS Firewall Manager returns a ``NextToken`` value in the response that allows you to list another group of ``PolicySummary`` objects. For the second and subsequent ``ListPolicies`` requests, specify the value of ``NextToken`` from the previous response to get information about another batch of ``PolicySummary`` objects.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Specifies the number of ``PolicySummary`` objects that you want AWS Firewall Manager to return for this request. If you have more ``PolicySummary`` objects than the number that you specify for ``MaxResults`` , the response includes a ``NextToken`` value that you can use to get another batch of ``PolicySummary`` objects.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PolicyList\': [
                    {
                        \'PolicyArn\': \'string\',
                        \'PolicyId\': \'string\',
                        \'PolicyName\': \'string\',
                        \'ResourceType\': \'string\',
                        \'SecurityServiceType\': \'WAF\',
                        \'RemediationEnabled\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PolicyList** *(list) --* 
        
              An array of ``PolicySummary`` objects.
        
              - *(dict) --* 
        
                Details of the AWS Firewall Manager policy. 
        
                - **PolicyArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the specified policy.
        
                - **PolicyId** *(string) --* 
        
                  The ID of the specified policy.
        
                - **PolicyName** *(string) --* 
        
                  The friendly name of the specified policy.
        
                - **ResourceType** *(string) --* 
        
                  The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
                - **SecurityServiceType** *(string) --* 
        
                  The service that the policy is using to protect the resources. This value is ``WAF`` .
        
                - **RemediationEnabled** *(boolean) --* 
        
                  Indicates if the policy should be automatically applied to new resources.
        
            - **NextToken** *(string) --* 
        
              If you have more ``PolicySummary`` objects than the number that you specified for ``MaxResults`` in the request, the response includes a ``NextToken`` value. To list more ``PolicySummary`` objects, submit another ``ListPolicies`` request, and specify the ``NextToken`` value from the response in the ``NextToken`` value in the next request.
        
        """
        pass

    def put_notification_channel(self, SnsTopicArn: str, SnsRoleName: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/PutNotificationChannel>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_notification_channel(
              SnsTopicArn=\'string\',
              SnsRoleName=\'string\'
          )
        :type SnsTopicArn: string
        :param SnsTopicArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager.
        
        :type SnsRoleName: string
        :param SnsRoleName: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity. 
        
        :returns: None
        """
        pass

    def put_policy(self, Policy: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/PutPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_policy(
              Policy={
                  \'PolicyId\': \'string\',
                  \'PolicyName\': \'string\',
                  \'PolicyUpdateToken\': \'string\',
                  \'SecurityServicePolicyData\': {
                      \'Type\': \'WAF\',
                      \'ManagedServiceData\': \'string\'
                  },
                  \'ResourceType\': \'string\',
                  \'ResourceTags\': [
                      {
                          \'Key\': \'string\',
                          \'Value\': \'string\'
                      },
                  ],
                  \'ExcludeResourceTags\': True|False,
                  \'RemediationEnabled\': True|False,
                  \'IncludeMap\': {
                      \'string\': [
                          \'string\',
                      ]
                  },
                  \'ExcludeMap\': {
                      \'string\': [
                          \'string\',
                      ]
                  }
              }
          )
        :type Policy: dict
        :param Policy: **[REQUIRED]** 
        
          The details of the AWS Firewall Manager policy to be created.
        
          - **PolicyId** *(string) --* 
        
            The ID of the AWS Firewall Manager policy.
        
          - **PolicyName** *(string) --* **[REQUIRED]** 
        
            The friendly name of the AWS Firewall Manager policy.
        
          - **PolicyUpdateToken** *(string) --* 
        
            A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request, the ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the current policy version. To get the ``PolicyUpdateToken`` of the current policy version, use a ``GetPolicy`` request.
        
          - **SecurityServicePolicyData** *(dict) --* **[REQUIRED]** 
        
            Details about the security service that is being used to protect the resources.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              The service that the policy is using to protect the resources. This value is ``WAF`` .
        
            - **ManagedServiceData** *(string) --* 
        
              Details about the service. This contains ``WAF`` data in JSON format, as shown in the following example:
        
               ``ManagedServiceData\": \"{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\": \\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}``  
        
          - **ResourceType** *(string) --* **[REQUIRED]** 
        
            The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
          - **ResourceTags** *(list) --* 
        
            An array of ``ResourceTag`` objects.
        
            - *(dict) --* 
        
              The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from protection by the AWS Firewall Manager policy. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. Tags are combined with an \"OR.\" That is, if you add more than one tag, if any of the tags matches, the resource is considered a match for the include or exclude. `Working with Tag Editor <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .
        
              - **Key** *(string) --* **[REQUIRED]** 
        
                The resource tag key.
        
              - **Value** *(string) --* 
        
                The resource tag value.
        
          - **ExcludeResourceTags** *(boolean) --* **[REQUIRED]** 
        
            If set to ``True`` , resources with the tags that are specified in the ``ResourceTag`` array are not protected by the policy. If set to ``False`` , and the ``ResourceTag`` array is not null, only resources with the specified tags are associated with the policy.
        
          - **RemediationEnabled** *(boolean) --* **[REQUIRED]** 
        
            Indicates if the policy should be automatically applied to new resources.
        
          - **IncludeMap** *(dict) --* 
        
            Specifies the AWS account IDs to include in the policy. If ``IncludeMap`` is null, all accounts in the AWS Organization are included in the policy. If ``IncludeMap`` is not null, only values listed in ``IncludeMap`` will be included in the policy.
        
            The key to the map is ``ACCOUNT`` . For example, a valid ``IncludeMap`` would be ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        
            - *(string) --* 
        
              - *(list) --* 
        
                - *(string) --* 
        
          - **ExcludeMap** *(dict) --* 
        
            Specifies the AWS account IDs to exclude from the policy. The ``IncludeMap`` values are evaluated first, with all of the appropriate account IDs added to the policy. Then the accounts listed in ``ExcludeMap`` are removed, resulting in the final list of accounts to add to the policy.
        
            The key to the map is ``ACCOUNT`` . For example, a valid ``ExcludeMap`` would be ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        
            - *(string) --* 
        
              - *(list) --* 
        
                - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policy\': {
                    \'PolicyId\': \'string\',
                    \'PolicyName\': \'string\',
                    \'PolicyUpdateToken\': \'string\',
                    \'SecurityServicePolicyData\': {
                        \'Type\': \'WAF\',
                        \'ManagedServiceData\': \'string\'
                    },
                    \'ResourceType\': \'string\',
                    \'ResourceTags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'ExcludeResourceTags\': True|False,
                    \'RemediationEnabled\': True|False,
                    \'IncludeMap\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'ExcludeMap\': {
                        \'string\': [
                            \'string\',
                        ]
                    }
                },
                \'PolicyArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policy** *(dict) --* 
        
              The details of the AWS Firewall Manager policy that was created.
        
              - **PolicyId** *(string) --* 
        
                The ID of the AWS Firewall Manager policy.
        
              - **PolicyName** *(string) --* 
        
                The friendly name of the AWS Firewall Manager policy.
        
              - **PolicyUpdateToken** *(string) --* 
        
                A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request, the ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the current policy version. To get the ``PolicyUpdateToken`` of the current policy version, use a ``GetPolicy`` request.
        
              - **SecurityServicePolicyData** *(dict) --* 
        
                Details about the security service that is being used to protect the resources.
        
                - **Type** *(string) --* 
        
                  The service that the policy is using to protect the resources. This value is ``WAF`` .
        
                - **ManagedServiceData** *(string) --* 
        
                  Details about the service. This contains ``WAF`` data in JSON format, as shown in the following example:
        
                   ``ManagedServiceData\": \"{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\": \\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}``  
        
              - **ResourceType** *(string) --* 
        
                The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
              - **ResourceTags** *(list) --* 
        
                An array of ``ResourceTag`` objects.
        
                - *(dict) --* 
        
                  The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from protection by the AWS Firewall Manager policy. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. Tags are combined with an \"OR.\" That is, if you add more than one tag, if any of the tags matches, the resource is considered a match for the include or exclude. `Working with Tag Editor <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .
        
                  - **Key** *(string) --* 
        
                    The resource tag key.
        
                  - **Value** *(string) --* 
        
                    The resource tag value.
        
              - **ExcludeResourceTags** *(boolean) --* 
        
                If set to ``True`` , resources with the tags that are specified in the ``ResourceTag`` array are not protected by the policy. If set to ``False`` , and the ``ResourceTag`` array is not null, only resources with the specified tags are associated with the policy.
        
              - **RemediationEnabled** *(boolean) --* 
        
                Indicates if the policy should be automatically applied to new resources.
        
              - **IncludeMap** *(dict) --* 
        
                Specifies the AWS account IDs to include in the policy. If ``IncludeMap`` is null, all accounts in the AWS Organization are included in the policy. If ``IncludeMap`` is not null, only values listed in ``IncludeMap`` will be included in the policy.
        
                The key to the map is ``ACCOUNT`` . For example, a valid ``IncludeMap`` would be ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **ExcludeMap** *(dict) --* 
        
                Specifies the AWS account IDs to exclude from the policy. The ``IncludeMap`` values are evaluated first, with all of the appropriate account IDs added to the policy. Then the accounts listed in ``ExcludeMap`` are removed, resulting in the final list of accounts to add to the policy.
        
                The key to the map is ``ACCOUNT`` . For example, a valid ``ExcludeMap`` would be ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
            - **PolicyArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the policy that was created.
        
        """
        pass
