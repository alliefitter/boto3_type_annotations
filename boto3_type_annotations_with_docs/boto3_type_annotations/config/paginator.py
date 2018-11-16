from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeComplianceByConfigRule(Paginator):
    def paginate(self, ConfigRuleNames: List = None, ComplianceTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByConfigRule>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ConfigRuleNames=[
                  \'string\',
              ],
              ComplianceTypes=[
                  \'COMPLIANT\'|\'NON_COMPLIANT\'|\'NOT_APPLICABLE\'|\'INSUFFICIENT_DATA\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ConfigRuleNames: list
        :param ConfigRuleNames: 
        
          Specify one or more AWS Config rule names to filter the results by rule.
        
          - *(string) --* 
        
        :type ComplianceTypes: list
        :param ComplianceTypes: 
        
          Filters the results by compliance.
        
          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` .
        
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
                \'ComplianceByConfigRules\': [
                    {
                        \'ConfigRuleName\': \'string\',
                        \'Compliance\': {
                            \'ComplianceType\': \'COMPLIANT\'|\'NON_COMPLIANT\'|\'NOT_APPLICABLE\'|\'INSUFFICIENT_DATA\',
                            \'ComplianceContributorCount\': {
                                \'CappedCount\': 123,
                                \'CapExceeded\': True|False
                            }
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ComplianceByConfigRules** *(list) --* 
        
              Indicates whether each of the specified AWS Config rules is compliant.
        
              - *(dict) --* 
        
                Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the resources that the rule evaluated comply with it. A rule is noncompliant if any of these resources do not comply.
        
                - **ConfigRuleName** *(string) --* 
        
                  The name of the AWS Config rule.
        
                - **Compliance** *(dict) --* 
        
                  Indicates whether the AWS Config rule is compliant.
        
                  - **ComplianceType** *(string) --* 
        
                    Indicates whether an AWS resource or AWS Config rule is compliant.
        
                    A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
        
                    A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
        
                    AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or AWS Config rule.
        
                    For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.
        
                  - **ComplianceContributorCount** *(dict) --* 
        
                    The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.
        
                    - **CappedCount** *(integer) --* 
        
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
        
                    - **CapExceeded** *(boolean) --* 
        
                      Indicates whether the maximum count is reached.
        
        """
        pass


class DescribeComplianceByResource(Paginator):
    def paginate(self, ResourceType: str = None, ResourceId: str = None, ComplianceTypes: List = None, Limit: int = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByResource>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ResourceType=\'string\',
              ResourceId=\'string\',
              ComplianceTypes=[
                  \'COMPLIANT\'|\'NON_COMPLIANT\'|\'NOT_APPLICABLE\'|\'INSUFFICIENT_DATA\',
              ],
              Limit=123,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ResourceType: string
        :param ResourceType: 
        
          The types of AWS resources for which you want compliance information (for example, ``AWS::EC2::Instance`` ). For this action, you can specify that the resource type is an AWS account by specifying ``AWS::::Account`` .
        
        :type ResourceId: string
        :param ResourceId: 
        
          The ID of the AWS resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for ``ResourceType`` .
        
        :type ComplianceTypes: list
        :param ComplianceTypes: 
        
          Filters the results by compliance.
        
          The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .
        
          - *(string) --* 
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        
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
                \'ComplianceByResources\': [
                    {
                        \'ResourceType\': \'string\',
                        \'ResourceId\': \'string\',
                        \'Compliance\': {
                            \'ComplianceType\': \'COMPLIANT\'|\'NON_COMPLIANT\'|\'NOT_APPLICABLE\'|\'INSUFFICIENT_DATA\',
                            \'ComplianceContributorCount\': {
                                \'CappedCount\': 123,
                                \'CapExceeded\': True|False
                            }
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ComplianceByResources** *(list) --* 
        
              Indicates whether the specified AWS resource complies with all of the AWS Config rules that evaluate it.
        
              - *(dict) --* 
        
                Indicates whether an AWS resource that is evaluated according to one or more AWS Config rules is compliant. A resource is compliant if it complies with all of the rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
        
                - **ResourceType** *(string) --* 
        
                  The type of the AWS resource that was evaluated.
        
                - **ResourceId** *(string) --* 
        
                  The ID of the AWS resource that was evaluated.
        
                - **Compliance** *(dict) --* 
        
                  Indicates whether the AWS resource complies with all of the AWS Config rules that evaluated it.
        
                  - **ComplianceType** *(string) --* 
        
                    Indicates whether an AWS resource or AWS Config rule is compliant.
        
                    A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
        
                    A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
        
                    AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or AWS Config rule.
        
                    For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.
        
                  - **ComplianceContributorCount** *(dict) --* 
        
                    The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.
        
                    - **CappedCount** *(integer) --* 
        
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
        
                    - **CapExceeded** *(boolean) --* 
        
                      Indicates whether the maximum count is reached.
        
        """
        pass


class DescribeConfigRules(Paginator):
    def paginate(self, ConfigRuleNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRules>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ConfigRuleNames=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ConfigRuleNames: list
        :param ConfigRuleNames: 
        
          The names of the AWS Config rules for which you want details. If you do not specify any names, AWS Config returns details for all your rules.
        
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
                \'ConfigRules\': [
                    {
                        \'ConfigRuleName\': \'string\',
                        \'ConfigRuleArn\': \'string\',
                        \'ConfigRuleId\': \'string\',
                        \'Description\': \'string\',
                        \'Scope\': {
                            \'ComplianceResourceTypes\': [
                                \'string\',
                            ],
                            \'TagKey\': \'string\',
                            \'TagValue\': \'string\',
                            \'ComplianceResourceId\': \'string\'
                        },
                        \'Source\': {
                            \'Owner\': \'CUSTOM_LAMBDA\'|\'AWS\',
                            \'SourceIdentifier\': \'string\',
                            \'SourceDetails\': [
                                {
                                    \'EventSource\': \'aws.config\',
                                    \'MessageType\': \'ConfigurationItemChangeNotification\'|\'ConfigurationSnapshotDeliveryCompleted\'|\'ScheduledNotification\'|\'OversizedConfigurationItemChangeNotification\',
                                    \'MaximumExecutionFrequency\': \'One_Hour\'|\'Three_Hours\'|\'Six_Hours\'|\'Twelve_Hours\'|\'TwentyFour_Hours\'
                                },
                            ]
                        },
                        \'InputParameters\': \'string\',
                        \'MaximumExecutionFrequency\': \'One_Hour\'|\'Three_Hours\'|\'Six_Hours\'|\'Twelve_Hours\'|\'TwentyFour_Hours\',
                        \'ConfigRuleState\': \'ACTIVE\'|\'DELETING\'|\'DELETING_RESULTS\'|\'EVALUATING\',
                        \'CreatedBy\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ConfigRules** *(list) --* 
        
              The details about your AWS Config rules.
        
              - *(dict) --* 
        
                An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a predefined function for an AWS managed rule. The function evaluates configuration items to assess whether your AWS resources comply with your desired configurations. This function can run when AWS Config detects a configuration change to an AWS resource and at a periodic frequency that you choose (for example, every 24 hours).
        
                .. note::
        
                  You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .
        
                For more information about developing and using AWS Config rules, see `Evaluating AWS Resource Configurations with AWS Config <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the *AWS Config Developer Guide* .
        
                - **ConfigRuleName** *(string) --* 
        
                  The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.
        
                - **ConfigRuleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the AWS Config rule.
        
                - **ConfigRuleId** *(string) --* 
        
                  The ID of the AWS Config rule.
        
                - **Description** *(string) --* 
        
                  The description that you provide for the AWS Config rule.
        
                - **Scope** *(dict) --* 
        
                  Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
        
                  - **ComplianceResourceTypes** *(list) --* 
        
                    The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .
        
                    - *(string) --* 
                
                  - **TagKey** *(string) --* 
        
                    The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
        
                  - **TagValue** *(string) --* 
        
                    The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .
        
                  - **ComplianceResourceId** *(string) --* 
        
                    The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .
        
                - **Source** *(dict) --* 
        
                  Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
        
                  - **Owner** *(string) --* 
        
                    Indicates whether AWS or the customer owns and manages the AWS Config rule.
        
                  - **SourceIdentifier** *(string) --* 
        
                    For AWS Config managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Managed Config Rules <http://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__ .
        
                    For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule\'s AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .
        
                  - **SourceDetails** *(list) --* 
        
                    Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.
        
                    - *(dict) --* 
        
                      Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for ``SourceDetail`` only for custom rules. 
        
                      - **EventSource** *(string) --* 
        
                        The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.
        
                      - **MessageType** *(string) --* 
        
                        The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
        
                        * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. 
                         
                        * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. 
                         
                        * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` . 
                         
                        * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot. 
                         
                        If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for ``OversizedConfigurationItemChangeNotification`` .
        
                      - **MaximumExecutionFrequency** *(string) --* 
        
                        The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value.
        
                        .. note::
        
                          By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
        
                          Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once every three hours. In this case, ``Three_Hours`` is the frequency of this rule. 
        
                - **InputParameters** *(string) --* 
        
                  A string, in JSON format, that is passed to the AWS Config rule Lambda function.
        
                - **MaximumExecutionFrequency** *(string) --* 
        
                  The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when:
        
                  * You are using an AWS managed rule that is triggered at a periodic frequency. 
                   
                  * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties . 
                   
                  .. note::
        
                    By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
        
                - **ConfigRuleState** *(string) --* 
        
                  Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the AWS Config rule.
        
                  AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the ``StartConfigRulesEvaluation`` request to evaluate your resources against the AWS Config rule.
        
                  AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use the ``DeleteEvaluationResults`` request to delete the current evaluation results for the AWS Config rule.
        
                  AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.
        
                - **CreatedBy** *(string) --* 
        
                  Service principal name of the service that created the rule.
        
                  .. note::
        
                    The field is populated only if the service linked rule is created by a service. The field is empty if you create your own rule.
        
        """
        pass


class GetComplianceDetailsByConfigRule(Paginator):
    def paginate(self, ConfigRuleName: str, ComplianceTypes: List = None, Limit: int = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByConfigRule>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ConfigRuleName=\'string\',
              ComplianceTypes=[
                  \'COMPLIANT\'|\'NON_COMPLIANT\'|\'NOT_APPLICABLE\'|\'INSUFFICIENT_DATA\',
              ],
              Limit=123,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]** 
        
          The name of the AWS Config rule for which you want compliance information.
        
        :type ComplianceTypes: list
        :param ComplianceTypes: 
        
          Filters the results by compliance.
        
          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .
        
          - *(string) --* 
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        
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
                \'EvaluationResults\': [
                    {
                        \'EvaluationResultIdentifier\': {
                            \'EvaluationResultQualifier\': {
                                \'ConfigRuleName\': \'string\',
                                \'ResourceType\': \'string\',
                                \'ResourceId\': \'string\'
                            },
                            \'OrderingTimestamp\': datetime(2015, 1, 1)
                        },
                        \'ComplianceType\': \'COMPLIANT\'|\'NON_COMPLIANT\'|\'NOT_APPLICABLE\'|\'INSUFFICIENT_DATA\',
                        \'ResultRecordedTime\': datetime(2015, 1, 1),
                        \'ConfigRuleInvokedTime\': datetime(2015, 1, 1),
                        \'Annotation\': \'string\',
                        \'ResultToken\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **EvaluationResults** *(list) --* 
        
              Indicates whether the AWS resource complies with the specified AWS Config rule.
        
              - *(dict) --* 
        
                The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.
        
                - **EvaluationResultIdentifier** *(dict) --* 
        
                  Uniquely identifies the evaluation result.
        
                  - **EvaluationResultQualifier** *(dict) --* 
        
                    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.
        
                    - **ConfigRuleName** *(string) --* 
        
                      The name of the AWS Config rule that was used in the evaluation.
        
                    - **ResourceType** *(string) --* 
        
                      The type of AWS resource that was evaluated.
        
                    - **ResourceId** *(string) --* 
        
                      The ID of the evaluated AWS resource.
        
                  - **OrderingTimestamp** *(datetime) --* 
        
                    The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.
        
                - **ComplianceType** *(string) --* 
        
                  Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.
        
                  For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.
        
                - **ResultRecordedTime** *(datetime) --* 
        
                  The time when AWS Config recorded the evaluation result.
        
                - **ConfigRuleInvokedTime** *(datetime) --* 
        
                  The time when the AWS Config rule evaluated the AWS resource.
        
                - **Annotation** *(string) --* 
        
                  Supplementary information about how the evaluation determined the compliance.
        
                - **ResultToken** *(string) --* 
        
                  An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.
        
        """
        pass


class GetComplianceDetailsByResource(Paginator):
    def paginate(self, ResourceType: str, ResourceId: str, ComplianceTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByResource>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ResourceType=\'string\',
              ResourceId=\'string\',
              ComplianceTypes=[
                  \'COMPLIANT\'|\'NON_COMPLIANT\'|\'NOT_APPLICABLE\'|\'INSUFFICIENT_DATA\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]** 
        
          The type of the AWS resource for which you want compliance information.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The ID of the AWS resource for which you want compliance information.
        
        :type ComplianceTypes: list
        :param ComplianceTypes: 
        
          Filters the results by compliance.
        
          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .
        
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
                \'EvaluationResults\': [
                    {
                        \'EvaluationResultIdentifier\': {
                            \'EvaluationResultQualifier\': {
                                \'ConfigRuleName\': \'string\',
                                \'ResourceType\': \'string\',
                                \'ResourceId\': \'string\'
                            },
                            \'OrderingTimestamp\': datetime(2015, 1, 1)
                        },
                        \'ComplianceType\': \'COMPLIANT\'|\'NON_COMPLIANT\'|\'NOT_APPLICABLE\'|\'INSUFFICIENT_DATA\',
                        \'ResultRecordedTime\': datetime(2015, 1, 1),
                        \'ConfigRuleInvokedTime\': datetime(2015, 1, 1),
                        \'Annotation\': \'string\',
                        \'ResultToken\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **EvaluationResults** *(list) --* 
        
              Indicates whether the specified AWS resource complies each AWS Config rule.
        
              - *(dict) --* 
        
                The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.
        
                - **EvaluationResultIdentifier** *(dict) --* 
        
                  Uniquely identifies the evaluation result.
        
                  - **EvaluationResultQualifier** *(dict) --* 
        
                    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.
        
                    - **ConfigRuleName** *(string) --* 
        
                      The name of the AWS Config rule that was used in the evaluation.
        
                    - **ResourceType** *(string) --* 
        
                      The type of AWS resource that was evaluated.
        
                    - **ResourceId** *(string) --* 
        
                      The ID of the evaluated AWS resource.
        
                  - **OrderingTimestamp** *(datetime) --* 
        
                    The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.
        
                - **ComplianceType** *(string) --* 
        
                  Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.
        
                  For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.
        
                - **ResultRecordedTime** *(datetime) --* 
        
                  The time when AWS Config recorded the evaluation result.
        
                - **ConfigRuleInvokedTime** *(datetime) --* 
        
                  The time when the AWS Config rule evaluated the AWS resource.
        
                - **Annotation** *(string) --* 
        
                  Supplementary information about how the evaluation determined the compliance.
        
                - **ResultToken** *(string) --* 
        
                  An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.
        
        """
        pass


class GetResourceConfigHistory(Paginator):
    def paginate(self, resourceType: str, resourceId: str, laterTime: datetime = None, earlierTime: datetime = None, chronologicalOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetResourceConfigHistory>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              resourceType=\'AWS::EC2::CustomerGateway\'|\'AWS::EC2::EIP\'|\'AWS::EC2::Host\'|\'AWS::EC2::Instance\'|\'AWS::EC2::InternetGateway\'|\'AWS::EC2::NetworkAcl\'|\'AWS::EC2::NetworkInterface\'|\'AWS::EC2::RouteTable\'|\'AWS::EC2::SecurityGroup\'|\'AWS::EC2::Subnet\'|\'AWS::CloudTrail::Trail\'|\'AWS::EC2::Volume\'|\'AWS::EC2::VPC\'|\'AWS::EC2::VPNConnection\'|\'AWS::EC2::VPNGateway\'|\'AWS::IAM::Group\'|\'AWS::IAM::Policy\'|\'AWS::IAM::Role\'|\'AWS::IAM::User\'|\'AWS::ACM::Certificate\'|\'AWS::RDS::DBInstance\'|\'AWS::RDS::DBSubnetGroup\'|\'AWS::RDS::DBSecurityGroup\'|\'AWS::RDS::DBSnapshot\'|\'AWS::RDS::EventSubscription\'|\'AWS::ElasticLoadBalancingV2::LoadBalancer\'|\'AWS::S3::Bucket\'|\'AWS::SSM::ManagedInstanceInventory\'|\'AWS::Redshift::Cluster\'|\'AWS::Redshift::ClusterSnapshot\'|\'AWS::Redshift::ClusterParameterGroup\'|\'AWS::Redshift::ClusterSecurityGroup\'|\'AWS::Redshift::ClusterSubnetGroup\'|\'AWS::Redshift::EventSubscription\'|\'AWS::CloudWatch::Alarm\'|\'AWS::CloudFormation::Stack\'|\'AWS::DynamoDB::Table\'|\'AWS::AutoScaling::AutoScalingGroup\'|\'AWS::AutoScaling::LaunchConfiguration\'|\'AWS::AutoScaling::ScalingPolicy\'|\'AWS::AutoScaling::ScheduledAction\'|\'AWS::CodeBuild::Project\'|\'AWS::WAF::RateBasedRule\'|\'AWS::WAF::Rule\'|\'AWS::WAF::WebACL\'|\'AWS::WAFRegional::RateBasedRule\'|\'AWS::WAFRegional::Rule\'|\'AWS::WAFRegional::WebACL\'|\'AWS::CloudFront::Distribution\'|\'AWS::CloudFront::StreamingDistribution\'|\'AWS::WAF::RuleGroup\'|\'AWS::WAFRegional::RuleGroup\'|\'AWS::Lambda::Function\'|\'AWS::ElasticBeanstalk::Application\'|\'AWS::ElasticBeanstalk::ApplicationVersion\'|\'AWS::ElasticBeanstalk::Environment\'|\'AWS::ElasticLoadBalancing::LoadBalancer\'|\'AWS::XRay::EncryptionConfig\'|\'AWS::SSM::AssociationCompliance\'|\'AWS::SSM::PatchCompliance\'|\'AWS::Shield::Protection\'|\'AWS::ShieldRegional::Protection\'|\'AWS::Config::ResourceCompliance\'|\'AWS::CodePipeline::Pipeline\',
              resourceId=\'string\',
              laterTime=datetime(2015, 1, 1),
              earlierTime=datetime(2015, 1, 1),
              chronologicalOrder=\'Reverse\'|\'Forward\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type resourceType: string
        :param resourceType: **[REQUIRED]** 
        
          The resource type.
        
        :type resourceId: string
        :param resourceId: **[REQUIRED]** 
        
          The ID of the resource (for example., ``sg-xxxxxx`` ).
        
        :type laterTime: datetime
        :param laterTime: 
        
          The time stamp that indicates a later time. If not specified, current time is taken.
        
        :type earlierTime: datetime
        :param earlierTime: 
        
          The time stamp that indicates an earlier time. If not specified, the action returns paginated results that contain configuration items that start when the first configuration item was recorded.
        
        :type chronologicalOrder: string
        :param chronologicalOrder: 
        
          The chronological order for configuration items listed. By default, the results are listed in reverse chronological order.
        
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
                \'configurationItems\': [
                    {
                        \'version\': \'string\',
                        \'accountId\': \'string\',
                        \'configurationItemCaptureTime\': datetime(2015, 1, 1),
                        \'configurationItemStatus\': \'OK\'|\'ResourceDiscovered\'|\'ResourceNotRecorded\'|\'ResourceDeleted\'|\'ResourceDeletedNotRecorded\',
                        \'configurationStateId\': \'string\',
                        \'configurationItemMD5Hash\': \'string\',
                        \'arn\': \'string\',
                        \'resourceType\': \'AWS::EC2::CustomerGateway\'|\'AWS::EC2::EIP\'|\'AWS::EC2::Host\'|\'AWS::EC2::Instance\'|\'AWS::EC2::InternetGateway\'|\'AWS::EC2::NetworkAcl\'|\'AWS::EC2::NetworkInterface\'|\'AWS::EC2::RouteTable\'|\'AWS::EC2::SecurityGroup\'|\'AWS::EC2::Subnet\'|\'AWS::CloudTrail::Trail\'|\'AWS::EC2::Volume\'|\'AWS::EC2::VPC\'|\'AWS::EC2::VPNConnection\'|\'AWS::EC2::VPNGateway\'|\'AWS::IAM::Group\'|\'AWS::IAM::Policy\'|\'AWS::IAM::Role\'|\'AWS::IAM::User\'|\'AWS::ACM::Certificate\'|\'AWS::RDS::DBInstance\'|\'AWS::RDS::DBSubnetGroup\'|\'AWS::RDS::DBSecurityGroup\'|\'AWS::RDS::DBSnapshot\'|\'AWS::RDS::EventSubscription\'|\'AWS::ElasticLoadBalancingV2::LoadBalancer\'|\'AWS::S3::Bucket\'|\'AWS::SSM::ManagedInstanceInventory\'|\'AWS::Redshift::Cluster\'|\'AWS::Redshift::ClusterSnapshot\'|\'AWS::Redshift::ClusterParameterGroup\'|\'AWS::Redshift::ClusterSecurityGroup\'|\'AWS::Redshift::ClusterSubnetGroup\'|\'AWS::Redshift::EventSubscription\'|\'AWS::CloudWatch::Alarm\'|\'AWS::CloudFormation::Stack\'|\'AWS::DynamoDB::Table\'|\'AWS::AutoScaling::AutoScalingGroup\'|\'AWS::AutoScaling::LaunchConfiguration\'|\'AWS::AutoScaling::ScalingPolicy\'|\'AWS::AutoScaling::ScheduledAction\'|\'AWS::CodeBuild::Project\'|\'AWS::WAF::RateBasedRule\'|\'AWS::WAF::Rule\'|\'AWS::WAF::WebACL\'|\'AWS::WAFRegional::RateBasedRule\'|\'AWS::WAFRegional::Rule\'|\'AWS::WAFRegional::WebACL\'|\'AWS::CloudFront::Distribution\'|\'AWS::CloudFront::StreamingDistribution\'|\'AWS::WAF::RuleGroup\'|\'AWS::WAFRegional::RuleGroup\'|\'AWS::Lambda::Function\'|\'AWS::ElasticBeanstalk::Application\'|\'AWS::ElasticBeanstalk::ApplicationVersion\'|\'AWS::ElasticBeanstalk::Environment\'|\'AWS::ElasticLoadBalancing::LoadBalancer\'|\'AWS::XRay::EncryptionConfig\'|\'AWS::SSM::AssociationCompliance\'|\'AWS::SSM::PatchCompliance\'|\'AWS::Shield::Protection\'|\'AWS::ShieldRegional::Protection\'|\'AWS::Config::ResourceCompliance\'|\'AWS::CodePipeline::Pipeline\',
                        \'resourceId\': \'string\',
                        \'resourceName\': \'string\',
                        \'awsRegion\': \'string\',
                        \'availabilityZone\': \'string\',
                        \'resourceCreationTime\': datetime(2015, 1, 1),
                        \'tags\': {
                            \'string\': \'string\'
                        },
                        \'relatedEvents\': [
                            \'string\',
                        ],
                        \'relationships\': [
                            {
                                \'resourceType\': \'AWS::EC2::CustomerGateway\'|\'AWS::EC2::EIP\'|\'AWS::EC2::Host\'|\'AWS::EC2::Instance\'|\'AWS::EC2::InternetGateway\'|\'AWS::EC2::NetworkAcl\'|\'AWS::EC2::NetworkInterface\'|\'AWS::EC2::RouteTable\'|\'AWS::EC2::SecurityGroup\'|\'AWS::EC2::Subnet\'|\'AWS::CloudTrail::Trail\'|\'AWS::EC2::Volume\'|\'AWS::EC2::VPC\'|\'AWS::EC2::VPNConnection\'|\'AWS::EC2::VPNGateway\'|\'AWS::IAM::Group\'|\'AWS::IAM::Policy\'|\'AWS::IAM::Role\'|\'AWS::IAM::User\'|\'AWS::ACM::Certificate\'|\'AWS::RDS::DBInstance\'|\'AWS::RDS::DBSubnetGroup\'|\'AWS::RDS::DBSecurityGroup\'|\'AWS::RDS::DBSnapshot\'|\'AWS::RDS::EventSubscription\'|\'AWS::ElasticLoadBalancingV2::LoadBalancer\'|\'AWS::S3::Bucket\'|\'AWS::SSM::ManagedInstanceInventory\'|\'AWS::Redshift::Cluster\'|\'AWS::Redshift::ClusterSnapshot\'|\'AWS::Redshift::ClusterParameterGroup\'|\'AWS::Redshift::ClusterSecurityGroup\'|\'AWS::Redshift::ClusterSubnetGroup\'|\'AWS::Redshift::EventSubscription\'|\'AWS::CloudWatch::Alarm\'|\'AWS::CloudFormation::Stack\'|\'AWS::DynamoDB::Table\'|\'AWS::AutoScaling::AutoScalingGroup\'|\'AWS::AutoScaling::LaunchConfiguration\'|\'AWS::AutoScaling::ScalingPolicy\'|\'AWS::AutoScaling::ScheduledAction\'|\'AWS::CodeBuild::Project\'|\'AWS::WAF::RateBasedRule\'|\'AWS::WAF::Rule\'|\'AWS::WAF::WebACL\'|\'AWS::WAFRegional::RateBasedRule\'|\'AWS::WAFRegional::Rule\'|\'AWS::WAFRegional::WebACL\'|\'AWS::CloudFront::Distribution\'|\'AWS::CloudFront::StreamingDistribution\'|\'AWS::WAF::RuleGroup\'|\'AWS::WAFRegional::RuleGroup\'|\'AWS::Lambda::Function\'|\'AWS::ElasticBeanstalk::Application\'|\'AWS::ElasticBeanstalk::ApplicationVersion\'|\'AWS::ElasticBeanstalk::Environment\'|\'AWS::ElasticLoadBalancing::LoadBalancer\'|\'AWS::XRay::EncryptionConfig\'|\'AWS::SSM::AssociationCompliance\'|\'AWS::SSM::PatchCompliance\'|\'AWS::Shield::Protection\'|\'AWS::ShieldRegional::Protection\'|\'AWS::Config::ResourceCompliance\'|\'AWS::CodePipeline::Pipeline\',
                                \'resourceId\': \'string\',
                                \'resourceName\': \'string\',
                                \'relationshipName\': \'string\'
                            },
                        ],
                        \'configuration\': \'string\',
                        \'supplementaryConfiguration\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the  GetResourceConfigHistory action.
        
            - **configurationItems** *(list) --* 
        
              A list that contains the configuration history of one or more resources.
        
              - *(dict) --* 
        
                A list that contains detailed configurations of a specified resource.
        
                - **version** *(string) --* 
        
                  The version number of the resource configuration.
        
                - **accountId** *(string) --* 
        
                  The 12-digit AWS account ID associated with the resource.
        
                - **configurationItemCaptureTime** *(datetime) --* 
        
                  The time when the configuration recording was initiated.
        
                - **configurationItemStatus** *(string) --* 
        
                  The configuration item status.
        
                - **configurationStateId** *(string) --* 
        
                  An identifier that indicates the ordering of the configuration items of a resource.
        
                - **configurationItemMD5Hash** *(string) --* 
        
                  Unique MD5 hash that represents the configuration item\'s state.
        
                  You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the resource.
        
                - **resourceType** *(string) --* 
        
                  The type of AWS resource.
        
                - **resourceId** *(string) --* 
        
                  The ID of the resource (for example, ``sg-xxxxxx`` ).
        
                - **resourceName** *(string) --* 
        
                  The custom name of the resource, if available.
        
                - **awsRegion** *(string) --* 
        
                  The region where the resource resides.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone associated with the resource.
        
                - **resourceCreationTime** *(datetime) --* 
        
                  The time stamp when the resource was created.
        
                - **tags** *(dict) --* 
        
                  A mapping of key value tags associated with the resource.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **relatedEvents** *(list) --* 
        
                  A list of CloudTrail event IDs.
        
                  A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS CloudTrail <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__ .
        
                  An empty field indicates that the current configuration was not initiated by any event.
        
                  - *(string) --* 
              
                - **relationships** *(list) --* 
        
                  A list of related AWS resources.
        
                  - *(dict) --* 
        
                    The relationship of the related resource to the main resource.
        
                    - **resourceType** *(string) --* 
        
                      The resource type of the related resource.
        
                    - **resourceId** *(string) --* 
        
                      The ID of the related resource (for example, ``sg-xxxxxx`` ).
        
                    - **resourceName** *(string) --* 
        
                      The custom name of the related resource, if available.
        
                    - **relationshipName** *(string) --* 
        
                      The type of relationship with the related resource.
        
                - **configuration** *(string) --* 
        
                  The description of the resource configuration.
        
                - **supplementaryConfiguration** *(dict) --* 
        
                  Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the ``configuration`` parameter.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListDiscoveredResources(Paginator):
    def paginate(self, resourceType: str, resourceIds: List = None, resourceName: str = None, limit: int = None, includeDeletedResources: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/ListDiscoveredResources>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              resourceType=\'AWS::EC2::CustomerGateway\'|\'AWS::EC2::EIP\'|\'AWS::EC2::Host\'|\'AWS::EC2::Instance\'|\'AWS::EC2::InternetGateway\'|\'AWS::EC2::NetworkAcl\'|\'AWS::EC2::NetworkInterface\'|\'AWS::EC2::RouteTable\'|\'AWS::EC2::SecurityGroup\'|\'AWS::EC2::Subnet\'|\'AWS::CloudTrail::Trail\'|\'AWS::EC2::Volume\'|\'AWS::EC2::VPC\'|\'AWS::EC2::VPNConnection\'|\'AWS::EC2::VPNGateway\'|\'AWS::IAM::Group\'|\'AWS::IAM::Policy\'|\'AWS::IAM::Role\'|\'AWS::IAM::User\'|\'AWS::ACM::Certificate\'|\'AWS::RDS::DBInstance\'|\'AWS::RDS::DBSubnetGroup\'|\'AWS::RDS::DBSecurityGroup\'|\'AWS::RDS::DBSnapshot\'|\'AWS::RDS::EventSubscription\'|\'AWS::ElasticLoadBalancingV2::LoadBalancer\'|\'AWS::S3::Bucket\'|\'AWS::SSM::ManagedInstanceInventory\'|\'AWS::Redshift::Cluster\'|\'AWS::Redshift::ClusterSnapshot\'|\'AWS::Redshift::ClusterParameterGroup\'|\'AWS::Redshift::ClusterSecurityGroup\'|\'AWS::Redshift::ClusterSubnetGroup\'|\'AWS::Redshift::EventSubscription\'|\'AWS::CloudWatch::Alarm\'|\'AWS::CloudFormation::Stack\'|\'AWS::DynamoDB::Table\'|\'AWS::AutoScaling::AutoScalingGroup\'|\'AWS::AutoScaling::LaunchConfiguration\'|\'AWS::AutoScaling::ScalingPolicy\'|\'AWS::AutoScaling::ScheduledAction\'|\'AWS::CodeBuild::Project\'|\'AWS::WAF::RateBasedRule\'|\'AWS::WAF::Rule\'|\'AWS::WAF::WebACL\'|\'AWS::WAFRegional::RateBasedRule\'|\'AWS::WAFRegional::Rule\'|\'AWS::WAFRegional::WebACL\'|\'AWS::CloudFront::Distribution\'|\'AWS::CloudFront::StreamingDistribution\'|\'AWS::WAF::RuleGroup\'|\'AWS::WAFRegional::RuleGroup\'|\'AWS::Lambda::Function\'|\'AWS::ElasticBeanstalk::Application\'|\'AWS::ElasticBeanstalk::ApplicationVersion\'|\'AWS::ElasticBeanstalk::Environment\'|\'AWS::ElasticLoadBalancing::LoadBalancer\'|\'AWS::XRay::EncryptionConfig\'|\'AWS::SSM::AssociationCompliance\'|\'AWS::SSM::PatchCompliance\'|\'AWS::Shield::Protection\'|\'AWS::ShieldRegional::Protection\'|\'AWS::Config::ResourceCompliance\'|\'AWS::CodePipeline::Pipeline\',
              resourceIds=[
                  \'string\',
              ],
              resourceName=\'string\',
              limit=123,
              includeDeletedResources=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type resourceType: string
        :param resourceType: **[REQUIRED]** 
        
          The type of resources that you want AWS Config to list in the response.
        
        :type resourceIds: list
        :param resourceIds: 
        
          The IDs of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.
        
          - *(string) --* 
        
        :type resourceName: string
        :param resourceName: 
        
          The custom name of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.
        
        :type limit: integer
        :param limit: 
        
          The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        
        :type includeDeletedResources: boolean
        :param includeDeletedResources: 
        
          Specifies whether AWS Config includes deleted resources in the results. By default, deleted resources are not included.
        
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
                \'resourceIdentifiers\': [
                    {
                        \'resourceType\': \'AWS::EC2::CustomerGateway\'|\'AWS::EC2::EIP\'|\'AWS::EC2::Host\'|\'AWS::EC2::Instance\'|\'AWS::EC2::InternetGateway\'|\'AWS::EC2::NetworkAcl\'|\'AWS::EC2::NetworkInterface\'|\'AWS::EC2::RouteTable\'|\'AWS::EC2::SecurityGroup\'|\'AWS::EC2::Subnet\'|\'AWS::CloudTrail::Trail\'|\'AWS::EC2::Volume\'|\'AWS::EC2::VPC\'|\'AWS::EC2::VPNConnection\'|\'AWS::EC2::VPNGateway\'|\'AWS::IAM::Group\'|\'AWS::IAM::Policy\'|\'AWS::IAM::Role\'|\'AWS::IAM::User\'|\'AWS::ACM::Certificate\'|\'AWS::RDS::DBInstance\'|\'AWS::RDS::DBSubnetGroup\'|\'AWS::RDS::DBSecurityGroup\'|\'AWS::RDS::DBSnapshot\'|\'AWS::RDS::EventSubscription\'|\'AWS::ElasticLoadBalancingV2::LoadBalancer\'|\'AWS::S3::Bucket\'|\'AWS::SSM::ManagedInstanceInventory\'|\'AWS::Redshift::Cluster\'|\'AWS::Redshift::ClusterSnapshot\'|\'AWS::Redshift::ClusterParameterGroup\'|\'AWS::Redshift::ClusterSecurityGroup\'|\'AWS::Redshift::ClusterSubnetGroup\'|\'AWS::Redshift::EventSubscription\'|\'AWS::CloudWatch::Alarm\'|\'AWS::CloudFormation::Stack\'|\'AWS::DynamoDB::Table\'|\'AWS::AutoScaling::AutoScalingGroup\'|\'AWS::AutoScaling::LaunchConfiguration\'|\'AWS::AutoScaling::ScalingPolicy\'|\'AWS::AutoScaling::ScheduledAction\'|\'AWS::CodeBuild::Project\'|\'AWS::WAF::RateBasedRule\'|\'AWS::WAF::Rule\'|\'AWS::WAF::WebACL\'|\'AWS::WAFRegional::RateBasedRule\'|\'AWS::WAFRegional::Rule\'|\'AWS::WAFRegional::WebACL\'|\'AWS::CloudFront::Distribution\'|\'AWS::CloudFront::StreamingDistribution\'|\'AWS::WAF::RuleGroup\'|\'AWS::WAFRegional::RuleGroup\'|\'AWS::Lambda::Function\'|\'AWS::ElasticBeanstalk::Application\'|\'AWS::ElasticBeanstalk::ApplicationVersion\'|\'AWS::ElasticBeanstalk::Environment\'|\'AWS::ElasticLoadBalancing::LoadBalancer\'|\'AWS::XRay::EncryptionConfig\'|\'AWS::SSM::AssociationCompliance\'|\'AWS::SSM::PatchCompliance\'|\'AWS::Shield::Protection\'|\'AWS::ShieldRegional::Protection\'|\'AWS::Config::ResourceCompliance\'|\'AWS::CodePipeline::Pipeline\',
                        \'resourceId\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceDeletionTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **resourceIdentifiers** *(list) --* 
        
              The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.
        
              - *(dict) --* 
        
                The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.
        
                - **resourceType** *(string) --* 
        
                  The type of resource.
        
                - **resourceId** *(string) --* 
        
                  The ID of the resource (for example, ``sg-xxxxxx`` ).
        
                - **resourceName** *(string) --* 
        
                  The custom name of the resource (if available).
        
                - **resourceDeletionTime** *(datetime) --* 
        
                  The time that the resource was deleted.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
