from typing import Dict
from botocore.paginate import Paginator


class ListComplianceStatus(Paginator):
    def paginate(self, PolicyId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`FMS.Client.list_compliance_status`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListComplianceStatus>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PolicyId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PolicyComplianceStatusList': [
                    {
                        'PolicyOwner': 'string',
                        'PolicyId': 'string',
                        'PolicyName': 'string',
                        'MemberAccount': 'string',
                        'EvaluationResults': [
                            {
                                'ComplianceStatus': 'COMPLIANT'|'NON_COMPLIANT',
                                'ViolatorCount': 123,
                                'EvaluationLimitExceeded': True|False
                            },
                        ],
                        'LastUpdated': datetime(2015, 1, 1),
                        'IssueInfoMap': {
                            'string': 'string'
                        }
                    },
                ],
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
                      Describes an AWS account's compliance with the AWS Firewall Manager policy.
                    - **ViolatorCount** *(integer) --* 
                      Number of resources that are non-compliant with the specified policy. A resource is considered non-compliant if it is not associated with the specified policy.
                    - **EvaluationLimitExceeded** *(boolean) --* 
                      Indicates that over 100 resources are non-compliant with the AWS Firewall Manager policy.
                - **LastUpdated** *(datetime) --* 
                  Time stamp of the last update to the ``EvaluationResult`` objects.
                - **IssueInfoMap** *(dict) --* 
                  Details about problems with dependent services, such as AWS WAF or AWS Config, that are causing a resource to be non-compliant. The details include the name of the dependent service and the error message received that indicates the problem with the service.
                  - *(string) --* 
                    - *(string) --* 
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]**
          The ID of the AWS Firewall Manager policy that you want the details for.
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


class ListMemberAccounts(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`FMS.Client.list_member_accounts`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListMemberAccounts>`_
        
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
                'MemberAccounts': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MemberAccounts** *(list) --* 
              An array of account IDs.
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


class ListPolicies(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`FMS.Client.list_policies`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListPolicies>`_
        
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
                'PolicyList': [
                    {
                        'PolicyArn': 'string',
                        'PolicyId': 'string',
                        'PolicyName': 'string',
                        'ResourceType': 'string',
                        'SecurityServiceType': 'WAF'|'SHIELD_ADVANCED',
                        'RemediationEnabled': True|False
                    },
                ],
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
                  The type of resource to protect with the policy. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . For example: ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
                - **SecurityServiceType** *(string) --* 
                  The service that the policy is using to protect the resources. This specifies the type of policy that is created, either a WAF policy or Shield Advanced policy.
                - **RemediationEnabled** *(boolean) --* 
                  Indicates if the policy should be automatically applied to new resources.
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
