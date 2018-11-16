from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def add_attributes_to_findings(self, findingArns: List, attributes: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/AddAttributesToFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_attributes_to_findings(
              findingArns=[
                  \'string\',
              ],
              attributes=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type findingArns: list
        :param findingArns: **[REQUIRED]** 
        
          The ARNs that specify the findings that you want to assign attributes to.
        
          - *(string) --* 
        
        :type attributes: list
        :param attributes: **[REQUIRED]** 
        
          The array of attributes that you want to assign to specified findings.
        
          - *(dict) --* 
        
            This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The attribute key.
        
            - **value** *(string) --* 
        
              The value assigned to the attribute key.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **failedItems** *(dict) --* 
        
              Attribute details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
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

    def create_assessment_target(self, assessmentTargetName: str, resourceGroupArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/CreateAssessmentTarget>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_assessment_target(
              assessmentTargetName=\'string\',
              resourceGroupArn=\'string\'
          )
        :type assessmentTargetName: string
        :param assessmentTargetName: **[REQUIRED]** 
        
          The user-defined name that identifies the assessment target that you want to create. The name must be unique within the AWS account.
        
        :type resourceGroupArn: string
        :param resourceGroupArn: 
        
          The ARN that specifies the resource group that is used to create the assessment target. If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentTargetArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentTargetArn** *(string) --* 
        
              The ARN that specifies the assessment target that is created.
        
        """
        pass

    def create_assessment_template(self, assessmentTargetArn: str, assessmentTemplateName: str, durationInSeconds: int, rulesPackageArns: List, userAttributesForFindings: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/CreateAssessmentTemplate>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_assessment_template(
              assessmentTargetArn=\'string\',
              assessmentTemplateName=\'string\',
              durationInSeconds=123,
              rulesPackageArns=[
                  \'string\',
              ],
              userAttributesForFindings=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type assessmentTargetArn: string
        :param assessmentTargetArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment target for which you want to create the assessment template.
        
        :type assessmentTemplateName: string
        :param assessmentTemplateName: **[REQUIRED]** 
        
          The user-defined name that identifies the assessment template that you want to create. You can create several assessment templates for an assessment target. The names of the assessment templates that correspond to a particular assessment target must be unique.
        
        :type durationInSeconds: integer
        :param durationInSeconds: **[REQUIRED]** 
        
          The duration of the assessment run in seconds.
        
        :type rulesPackageArns: list
        :param rulesPackageArns: **[REQUIRED]** 
        
          The ARNs that specify the rules packages that you want to attach to the assessment template.
        
          - *(string) --* 
        
        :type userAttributesForFindings: list
        :param userAttributesForFindings: 
        
          The user-defined attributes that are assigned to every finding that is generated by the assessment run that uses this assessment template. An attribute is a key and value pair (an  Attribute object). Within an assessment template, each key must be unique.
        
          - *(dict) --* 
        
            This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The attribute key.
        
            - **value** *(string) --* 
        
              The value assigned to the attribute key.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentTemplateArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentTemplateArn** *(string) --* 
        
              The ARN that specifies the assessment template that is created.
        
        """
        pass

    def create_exclusions_preview(self, assessmentTemplateArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/CreateExclusionsPreview>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_exclusions_preview(
              assessmentTemplateArn=\'string\'
          )
        :type assessmentTemplateArn: string
        :param assessmentTemplateArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment template for which you want to create an exclusions preview.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'previewToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **previewToken** *(string) --* 
        
              Specifies the unique identifier of the requested exclusions preview. You can use the unique identifier to retrieve the exclusions preview when running the GetExclusionsPreview API.
        
        """
        pass

    def create_resource_group(self, resourceGroupTags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/CreateResourceGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_resource_group(
              resourceGroupTags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type resourceGroupTags: list
        :param resourceGroupTags: **[REQUIRED]** 
        
          A collection of keys and an array of possible values, \'[{\"key\":\"key1\",\"values\":[\"Value1\",\"Value2\"]},{\"key\":\"Key2\",\"values\":[\"Value3\"]}]\'.
        
          For example,\'[{\"key\":\"Name\",\"values\":[\"TestEC2Instance\"]}]\'.
        
          - *(dict) --* 
        
            This data type is used as one of the elements of the  ResourceGroup data type.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              A tag key.
        
            - **value** *(string) --* 
        
              The value assigned to a tag key.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'resourceGroupArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **resourceGroupArn** *(string) --* 
        
              The ARN that specifies the resource group that is created.
        
        """
        pass

    def delete_assessment_run(self, assessmentRunArn: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DeleteAssessmentRun>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_assessment_run(
              assessmentRunArn=\'string\'
          )
        :type assessmentRunArn: string
        :param assessmentRunArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment run that you want to delete.
        
        :returns: None
        """
        pass

    def delete_assessment_target(self, assessmentTargetArn: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DeleteAssessmentTarget>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_assessment_target(
              assessmentTargetArn=\'string\'
          )
        :type assessmentTargetArn: string
        :param assessmentTargetArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment target that you want to delete.
        
        :returns: None
        """
        pass

    def delete_assessment_template(self, assessmentTemplateArn: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DeleteAssessmentTemplate>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_assessment_template(
              assessmentTemplateArn=\'string\'
          )
        :type assessmentTemplateArn: string
        :param assessmentTemplateArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment template that you want to delete.
        
        :returns: None
        """
        pass

    def describe_assessment_runs(self, assessmentRunArns: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeAssessmentRuns>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_assessment_runs(
              assessmentRunArns=[
                  \'string\',
              ]
          )
        :type assessmentRunArns: list
        :param assessmentRunArns: **[REQUIRED]** 
        
          The ARN that specifies the assessment run that you want to describe.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentRuns\': [
                    {
                        \'arn\': \'string\',
                        \'name\': \'string\',
                        \'assessmentTemplateArn\': \'string\',
                        \'state\': \'CREATED\'|\'START_DATA_COLLECTION_PENDING\'|\'START_DATA_COLLECTION_IN_PROGRESS\'|\'COLLECTING_DATA\'|\'STOP_DATA_COLLECTION_PENDING\'|\'DATA_COLLECTED\'|\'START_EVALUATING_RULES_PENDING\'|\'EVALUATING_RULES\'|\'FAILED\'|\'ERROR\'|\'COMPLETED\'|\'COMPLETED_WITH_ERRORS\'|\'CANCELED\',
                        \'durationInSeconds\': 123,
                        \'rulesPackageArns\': [
                            \'string\',
                        ],
                        \'userAttributesForFindings\': [
                            {
                                \'key\': \'string\',
                                \'value\': \'string\'
                            },
                        ],
                        \'createdAt\': datetime(2015, 1, 1),
                        \'startedAt\': datetime(2015, 1, 1),
                        \'completedAt\': datetime(2015, 1, 1),
                        \'stateChangedAt\': datetime(2015, 1, 1),
                        \'dataCollected\': True|False,
                        \'stateChanges\': [
                            {
                                \'stateChangedAt\': datetime(2015, 1, 1),
                                \'state\': \'CREATED\'|\'START_DATA_COLLECTION_PENDING\'|\'START_DATA_COLLECTION_IN_PROGRESS\'|\'COLLECTING_DATA\'|\'STOP_DATA_COLLECTION_PENDING\'|\'DATA_COLLECTED\'|\'START_EVALUATING_RULES_PENDING\'|\'EVALUATING_RULES\'|\'FAILED\'|\'ERROR\'|\'COMPLETED\'|\'COMPLETED_WITH_ERRORS\'|\'CANCELED\'
                            },
                        ],
                        \'notifications\': [
                            {
                                \'date\': datetime(2015, 1, 1),
                                \'event\': \'ASSESSMENT_RUN_STARTED\'|\'ASSESSMENT_RUN_COMPLETED\'|\'ASSESSMENT_RUN_STATE_CHANGED\'|\'FINDING_REPORTED\'|\'OTHER\',
                                \'message\': \'string\',
                                \'error\': True|False,
                                \'snsTopicArn\': \'string\',
                                \'snsPublishStatusCode\': \'SUCCESS\'|\'TOPIC_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'INTERNAL_ERROR\'
                            },
                        ],
                        \'findingCounts\': {
                            \'string\': 123
                        }
                    },
                ],
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentRuns** *(list) --* 
        
              Information about the assessment run.
        
              - *(dict) --* 
        
                A snapshot of an Amazon Inspector assessment run that contains the findings of the assessment run .
        
                Used as the response element in the  DescribeAssessmentRuns action.
        
                - **arn** *(string) --* 
        
                  The ARN of the assessment run.
        
                - **name** *(string) --* 
        
                  The auto-generated name for the assessment run.
        
                - **assessmentTemplateArn** *(string) --* 
        
                  The ARN of the assessment template that is associated with the assessment run.
        
                - **state** *(string) --* 
        
                  The state of the assessment run.
        
                - **durationInSeconds** *(integer) --* 
        
                  The duration of the assessment run.
        
                - **rulesPackageArns** *(list) --* 
        
                  The rules packages selected for the assessment run.
        
                  - *(string) --* 
              
                - **userAttributesForFindings** *(list) --* 
        
                  The user-defined attributes that are assigned to every generated finding.
        
                  - *(dict) --* 
        
                    This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
                    - **key** *(string) --* 
        
                      The attribute key.
        
                    - **value** *(string) --* 
        
                      The value assigned to the attribute key.
        
                - **createdAt** *(datetime) --* 
        
                  The time when  StartAssessmentRun was called.
        
                - **startedAt** *(datetime) --* 
        
                  The time when  StartAssessmentRun was called.
        
                - **completedAt** *(datetime) --* 
        
                  The assessment run completion time that corresponds to the rules packages evaluation completion time or failure.
        
                - **stateChangedAt** *(datetime) --* 
        
                  The last time when the assessment run\'s state changed.
        
                - **dataCollected** *(boolean) --* 
        
                  A Boolean value (true or false) that specifies whether the process of collecting data from the agents is completed.
        
                - **stateChanges** *(list) --* 
        
                  A list of the assessment run state changes.
        
                  - *(dict) --* 
        
                    Used as one of the elements of the  AssessmentRun data type.
        
                    - **stateChangedAt** *(datetime) --* 
        
                      The last time the assessment run state changed.
        
                    - **state** *(string) --* 
        
                      The assessment run state.
        
                - **notifications** *(list) --* 
        
                  A list of notifications for the event subscriptions. A notification about a particular generated finding is added to this list only once.
        
                  - *(dict) --* 
        
                    Used as one of the elements of the  AssessmentRun data type.
        
                    - **date** *(datetime) --* 
        
                      The date of the notification.
        
                    - **event** *(string) --* 
        
                      The event for which a notification is sent.
        
                    - **message** *(string) --* 
        
                      The message included in the notification.
        
                    - **error** *(boolean) --* 
        
                      The Boolean value that specifies whether the notification represents an error.
        
                    - **snsTopicArn** *(string) --* 
        
                      The SNS topic to which the SNS notification is sent.
        
                    - **snsPublishStatusCode** *(string) --* 
        
                      The status code of the SNS notification.
        
                - **findingCounts** *(dict) --* 
        
                  Provides a total count of generated findings per severity.
        
                  - *(string) --* 
                    
                    - *(integer) --* 
              
            - **failedItems** *(dict) --* 
        
              Assessment run details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
        """
        pass

    def describe_assessment_targets(self, assessmentTargetArns: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeAssessmentTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_assessment_targets(
              assessmentTargetArns=[
                  \'string\',
              ]
          )
        :type assessmentTargetArns: list
        :param assessmentTargetArns: **[REQUIRED]** 
        
          The ARNs that specifies the assessment targets that you want to describe.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentTargets\': [
                    {
                        \'arn\': \'string\',
                        \'name\': \'string\',
                        \'resourceGroupArn\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'updatedAt\': datetime(2015, 1, 1)
                    },
                ],
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentTargets** *(list) --* 
        
              Information about the assessment targets.
        
              - *(dict) --* 
        
                Contains information about an Amazon Inspector application. This data type is used as the response element in the  DescribeAssessmentTargets action.
        
                - **arn** *(string) --* 
        
                  The ARN that specifies the Amazon Inspector assessment target.
        
                - **name** *(string) --* 
        
                  The name of the Amazon Inspector assessment target.
        
                - **resourceGroupArn** *(string) --* 
        
                  The ARN that specifies the resource group that is associated with the assessment target.
        
                - **createdAt** *(datetime) --* 
        
                  The time at which the assessment target is created.
        
                - **updatedAt** *(datetime) --* 
        
                  The time at which  UpdateAssessmentTarget is called.
        
            - **failedItems** *(dict) --* 
        
              Assessment target details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
        """
        pass

    def describe_assessment_templates(self, assessmentTemplateArns: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeAssessmentTemplates>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_assessment_templates(
              assessmentTemplateArns=[
                  \'string\',
              ]
          )
        :type assessmentTemplateArns: list
        :param assessmentTemplateArns: **[REQUIRED]** 
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentTemplates\': [
                    {
                        \'arn\': \'string\',
                        \'name\': \'string\',
                        \'assessmentTargetArn\': \'string\',
                        \'durationInSeconds\': 123,
                        \'rulesPackageArns\': [
                            \'string\',
                        ],
                        \'userAttributesForFindings\': [
                            {
                                \'key\': \'string\',
                                \'value\': \'string\'
                            },
                        ],
                        \'lastAssessmentRunArn\': \'string\',
                        \'assessmentRunCount\': 123,
                        \'createdAt\': datetime(2015, 1, 1)
                    },
                ],
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentTemplates** *(list) --* 
        
              Information about the assessment templates.
        
              - *(dict) --* 
        
                Contains information about an Amazon Inspector assessment template. This data type is used as the response element in the  DescribeAssessmentTemplates action.
        
                - **arn** *(string) --* 
        
                  The ARN of the assessment template.
        
                - **name** *(string) --* 
        
                  The name of the assessment template.
        
                - **assessmentTargetArn** *(string) --* 
        
                  The ARN of the assessment target that corresponds to this assessment template.
        
                - **durationInSeconds** *(integer) --* 
        
                  The duration in seconds specified for this assessment template. The default value is 3600 seconds (one hour). The maximum value is 86400 seconds (one day).
        
                - **rulesPackageArns** *(list) --* 
        
                  The rules packages that are specified for this assessment template.
        
                  - *(string) --* 
              
                - **userAttributesForFindings** *(list) --* 
        
                  The user-defined attributes that are assigned to every generated finding from the assessment run that uses this assessment template.
        
                  - *(dict) --* 
        
                    This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
                    - **key** *(string) --* 
        
                      The attribute key.
        
                    - **value** *(string) --* 
        
                      The value assigned to the attribute key.
        
                - **lastAssessmentRunArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the most recent assessment run associated with this assessment template. This value exists only when the value of assessmentRunCount is greaterpa than zero.
        
                - **assessmentRunCount** *(integer) --* 
        
                  The number of existing assessment runs associated with this assessment template. This value can be zero or a positive integer.
        
                - **createdAt** *(datetime) --* 
        
                  The time at which the assessment template is created.
        
            - **failedItems** *(dict) --* 
        
              Assessment template details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
        """
        pass

    def describe_cross_account_access_role(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeCrossAccountAccessRole>`_
        
        **Request Syntax** 
        
        ::
        
          response = client.describe_cross_account_access_role()
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'roleArn\': \'string\',
                \'valid\': True|False,
                \'registeredAt\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **roleArn** *(string) --* 
        
              The ARN that specifies the IAM role that Amazon Inspector uses to access your AWS account.
        
            - **valid** *(boolean) --* 
        
              A Boolean value that specifies whether the IAM role has the necessary policies attached to enable Amazon Inspector to access your AWS account.
        
            - **registeredAt** *(datetime) --* 
        
              The date when the cross-account access role was registered.
        
        """
        pass

    def describe_exclusions(self, exclusionArns: List, locale: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeExclusions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_exclusions(
              exclusionArns=[
                  \'string\',
              ],
              locale=\'EN_US\'
          )
        :type exclusionArns: list
        :param exclusionArns: **[REQUIRED]** 
        
          The list of ARNs that specify the exclusions that you want to describe.
        
          - *(string) --* 
        
        :type locale: string
        :param locale: 
        
          The locale into which you want to translate the exclusion\'s title, description, and recommendation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'exclusions\': {
                    \'string\': {
                        \'arn\': \'string\',
                        \'title\': \'string\',
                        \'description\': \'string\',
                        \'recommendation\': \'string\',
                        \'scopes\': [
                            {
                                \'key\': \'INSTANCE_ID\'|\'RULES_PACKAGE_ARN\',
                                \'value\': \'string\'
                            },
                        ],
                        \'attributes\': [
                            {
                                \'key\': \'string\',
                                \'value\': \'string\'
                            },
                        ]
                    }
                },
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **exclusions** *(dict) --* 
        
              Information about the exclusions.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Contains information about what was excluded from an assessment run.
        
                  - **arn** *(string) --* 
        
                    The ARN that specifies the exclusion.
        
                  - **title** *(string) --* 
        
                    The name of the exclusion.
        
                  - **description** *(string) --* 
        
                    The description of the exclusion.
        
                  - **recommendation** *(string) --* 
        
                    The recommendation for the exclusion.
        
                  - **scopes** *(list) --* 
        
                    The AWS resources for which the exclusion pertains.
        
                    - *(dict) --* 
        
                      This data type contains key-value pairs that identify various Amazon resources.
        
                      - **key** *(string) --* 
        
                        The type of the scope.
        
                      - **value** *(string) --* 
        
                        The resource identifier for the specified scope type.
        
                  - **attributes** *(list) --* 
        
                    The system-defined attributes for the exclusion.
        
                    - *(dict) --* 
        
                      This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
                      - **key** *(string) --* 
        
                        The attribute key.
        
                      - **value** *(string) --* 
        
                        The value assigned to the attribute key.
        
            - **failedItems** *(dict) --* 
        
              Exclusion details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
        """
        pass

    def describe_findings(self, findingArns: List, locale: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_findings(
              findingArns=[
                  \'string\',
              ],
              locale=\'EN_US\'
          )
        :type findingArns: list
        :param findingArns: **[REQUIRED]** 
        
          The ARN that specifies the finding that you want to describe.
        
          - *(string) --* 
        
        :type locale: string
        :param locale: 
        
          The locale into which you want to translate a finding description, recommendation, and the short description that identifies the finding.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'findings\': [
                    {
                        \'arn\': \'string\',
                        \'schemaVersion\': 123,
                        \'service\': \'string\',
                        \'serviceAttributes\': {
                            \'schemaVersion\': 123,
                            \'assessmentRunArn\': \'string\',
                            \'rulesPackageArn\': \'string\'
                        },
                        \'assetType\': \'ec2-instance\',
                        \'assetAttributes\': {
                            \'schemaVersion\': 123,
                            \'agentId\': \'string\',
                            \'autoScalingGroup\': \'string\',
                            \'amiId\': \'string\',
                            \'hostname\': \'string\',
                            \'ipv4Addresses\': [
                                \'string\',
                            ],
                            \'tags\': [
                                {
                                    \'key\': \'string\',
                                    \'value\': \'string\'
                                },
                            ],
                            \'networkInterfaces\': [
                                {
                                    \'networkInterfaceId\': \'string\',
                                    \'subnetId\': \'string\',
                                    \'vpcId\': \'string\',
                                    \'privateDnsName\': \'string\',
                                    \'privateIpAddress\': \'string\',
                                    \'privateIpAddresses\': [
                                        {
                                            \'privateDnsName\': \'string\',
                                            \'privateIpAddress\': \'string\'
                                        },
                                    ],
                                    \'publicDnsName\': \'string\',
                                    \'publicIp\': \'string\',
                                    \'ipv6Addresses\': [
                                        \'string\',
                                    ],
                                    \'securityGroups\': [
                                        {
                                            \'groupName\': \'string\',
                                            \'groupId\': \'string\'
                                        },
                                    ]
                                },
                            ]
                        },
                        \'id\': \'string\',
                        \'title\': \'string\',
                        \'description\': \'string\',
                        \'recommendation\': \'string\',
                        \'severity\': \'Low\'|\'Medium\'|\'High\'|\'Informational\'|\'Undefined\',
                        \'numericSeverity\': 123.0,
                        \'confidence\': 123,
                        \'indicatorOfCompromise\': True|False,
                        \'attributes\': [
                            {
                                \'key\': \'string\',
                                \'value\': \'string\'
                            },
                        ],
                        \'userAttributes\': [
                            {
                                \'key\': \'string\',
                                \'value\': \'string\'
                            },
                        ],
                        \'createdAt\': datetime(2015, 1, 1),
                        \'updatedAt\': datetime(2015, 1, 1)
                    },
                ],
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **findings** *(list) --* 
        
              Information about the finding.
        
              - *(dict) --* 
        
                Contains information about an Amazon Inspector finding. This data type is used as the response element in the  DescribeFindings action.
        
                - **arn** *(string) --* 
        
                  The ARN that specifies the finding.
        
                - **schemaVersion** *(integer) --* 
        
                  The schema version of this data type.
        
                - **service** *(string) --* 
        
                  The data element is set to \"Inspector\".
        
                - **serviceAttributes** *(dict) --* 
        
                  This data type is used in the  Finding data type.
        
                  - **schemaVersion** *(integer) --* 
        
                    The schema version of this data type.
        
                  - **assessmentRunArn** *(string) --* 
        
                    The ARN of the assessment run during which the finding is generated.
        
                  - **rulesPackageArn** *(string) --* 
        
                    The ARN of the rules package that is used to generate the finding.
        
                - **assetType** *(string) --* 
        
                  The type of the host from which the finding is generated.
        
                - **assetAttributes** *(dict) --* 
        
                  A collection of attributes of the host from which the finding is generated.
        
                  - **schemaVersion** *(integer) --* 
        
                    The schema version of this data type.
        
                  - **agentId** *(string) --* 
        
                    The ID of the agent that is installed on the EC2 instance where the finding is generated.
        
                  - **autoScalingGroup** *(string) --* 
        
                    The Auto Scaling group of the EC2 instance where the finding is generated.
        
                  - **amiId** *(string) --* 
        
                    The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where the finding is generated.
        
                  - **hostname** *(string) --* 
        
                    The hostname of the EC2 instance where the finding is generated.
        
                  - **ipv4Addresses** *(list) --* 
        
                    The list of IP v4 addresses of the EC2 instance where the finding is generated.
        
                    - *(string) --* 
                
                  - **tags** *(list) --* 
        
                    The tags related to the EC2 instance where the finding is generated.
        
                    - *(dict) --* 
        
                      A key and value pair. This data type is used as a request parameter in the  SetTagsForResource action and a response element in the  ListTagsForResource action.
        
                      - **key** *(string) --* 
        
                        A tag key.
        
                      - **value** *(string) --* 
        
                        A value assigned to a tag key.
        
                  - **networkInterfaces** *(list) --* 
        
                    An array of the network interfaces interacting with the EC2 instance where the finding is generated.
        
                    - *(dict) --* 
        
                      Contains information about the network interfaces interacting with an EC2 instance. This data type is used as one of the elements of the  AssetAttributes data type.
        
                      - **networkInterfaceId** *(string) --* 
        
                        The ID of the network interface.
        
                      - **subnetId** *(string) --* 
        
                        The ID of a subnet associated with the network interface.
        
                      - **vpcId** *(string) --* 
        
                        The ID of a VPC associated with the network interface.
        
                      - **privateDnsName** *(string) --* 
        
                        The name of a private DNS associated with the network interface.
        
                      - **privateIpAddress** *(string) --* 
        
                        The private IP address associated with the network interface.
        
                      - **privateIpAddresses** *(list) --* 
        
                        A list of the private IP addresses associated with the network interface. Includes the privateDnsName and privateIpAddress.
        
                        - *(dict) --* 
        
                          Contains information about a private IP address associated with a network interface. This data type is used as a response element in the  DescribeFindings action.
        
                          - **privateDnsName** *(string) --* 
        
                            The DNS name of the private IP address.
        
                          - **privateIpAddress** *(string) --* 
        
                            The full IP address of the network inteface.
        
                      - **publicDnsName** *(string) --* 
        
                        The name of a public DNS associated with the network interface.
        
                      - **publicIp** *(string) --* 
        
                        The public IP address from which the network interface is reachable.
        
                      - **ipv6Addresses** *(list) --* 
        
                        The IP addresses associated with the network interface.
        
                        - *(string) --* 
                    
                      - **securityGroups** *(list) --* 
        
                        A list of the security groups associated with the network interface. Includes the groupId and groupName.
        
                        - *(dict) --* 
        
                          Contains information about a security group associated with a network interface. This data type is used as one of the elements of the  NetworkInterface data type.
        
                          - **groupName** *(string) --* 
        
                            The name of the security group.
        
                          - **groupId** *(string) --* 
        
                            The ID of the security group.
        
                - **id** *(string) --* 
        
                  The ID of the finding.
        
                - **title** *(string) --* 
        
                  The name of the finding.
        
                - **description** *(string) --* 
        
                  The description of the finding.
        
                - **recommendation** *(string) --* 
        
                  The recommendation for the finding.
        
                - **severity** *(string) --* 
        
                  The finding severity. Values can be set to High, Medium, Low, and Informational.
        
                - **numericSeverity** *(float) --* 
        
                  The numeric value of the finding severity.
        
                - **confidence** *(integer) --* 
        
                  This data element is currently not used.
        
                - **indicatorOfCompromise** *(boolean) --* 
        
                  This data element is currently not used.
        
                - **attributes** *(list) --* 
        
                  The system-defined attributes for the finding.
        
                  - *(dict) --* 
        
                    This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
                    - **key** *(string) --* 
        
                      The attribute key.
        
                    - **value** *(string) --* 
        
                      The value assigned to the attribute key.
        
                - **userAttributes** *(list) --* 
        
                  The user-defined attributes that are assigned to the finding.
        
                  - *(dict) --* 
        
                    This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
                    - **key** *(string) --* 
        
                      The attribute key.
        
                    - **value** *(string) --* 
        
                      The value assigned to the attribute key.
        
                - **createdAt** *(datetime) --* 
        
                  The time when the finding was generated.
        
                - **updatedAt** *(datetime) --* 
        
                  The time when  AddAttributesToFindings is called.
        
            - **failedItems** *(dict) --* 
        
              Finding details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
        """
        pass

    def describe_resource_groups(self, resourceGroupArns: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeResourceGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_resource_groups(
              resourceGroupArns=[
                  \'string\',
              ]
          )
        :type resourceGroupArns: list
        :param resourceGroupArns: **[REQUIRED]** 
        
          The ARN that specifies the resource group that you want to describe.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'resourceGroups\': [
                    {
                        \'arn\': \'string\',
                        \'tags\': [
                            {
                                \'key\': \'string\',
                                \'value\': \'string\'
                            },
                        ],
                        \'createdAt\': datetime(2015, 1, 1)
                    },
                ],
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **resourceGroups** *(list) --* 
        
              Information about a resource group.
        
              - *(dict) --* 
        
                Contains information about a resource group. The resource group defines a set of tags that, when queried, identify the AWS resources that make up the assessment target. This data type is used as the response element in the  DescribeResourceGroups action.
        
                - **arn** *(string) --* 
        
                  The ARN of the resource group.
        
                - **tags** *(list) --* 
        
                  The tags (key and value pairs) of the resource group. This data type property is used in the  CreateResourceGroup action.
        
                  - *(dict) --* 
        
                    This data type is used as one of the elements of the  ResourceGroup data type.
        
                    - **key** *(string) --* 
        
                      A tag key.
        
                    - **value** *(string) --* 
        
                      The value assigned to a tag key.
        
                - **createdAt** *(datetime) --* 
        
                  The time at which resource group is created.
        
            - **failedItems** *(dict) --* 
        
              Resource group details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
        """
        pass

    def describe_rules_packages(self, rulesPackageArns: List, locale: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeRulesPackages>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_rules_packages(
              rulesPackageArns=[
                  \'string\',
              ],
              locale=\'EN_US\'
          )
        :type rulesPackageArns: list
        :param rulesPackageArns: **[REQUIRED]** 
        
          The ARN that specifies the rules package that you want to describe.
        
          - *(string) --* 
        
        :type locale: string
        :param locale: 
        
          The locale that you want to translate a rules package description into.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'rulesPackages\': [
                    {
                        \'arn\': \'string\',
                        \'name\': \'string\',
                        \'version\': \'string\',
                        \'provider\': \'string\',
                        \'description\': \'string\'
                    },
                ],
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **rulesPackages** *(list) --* 
        
              Information about the rules package.
        
              - *(dict) --* 
        
                Contains information about an Amazon Inspector rules package. This data type is used as the response element in the  DescribeRulesPackages action.
        
                - **arn** *(string) --* 
        
                  The ARN of the rules package.
        
                - **name** *(string) --* 
        
                  The name of the rules package.
        
                - **version** *(string) --* 
        
                  The version ID of the rules package.
        
                - **provider** *(string) --* 
        
                  The provider of the rules package.
        
                - **description** *(string) --* 
        
                  The description of the rules package.
        
            - **failedItems** *(dict) --* 
        
              Rules package details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
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

    def get_assessment_report(self, assessmentRunArn: str, reportFileFormat: str, reportType: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/GetAssessmentReport>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_assessment_report(
              assessmentRunArn=\'string\',
              reportFileFormat=\'HTML\'|\'PDF\',
              reportType=\'FINDING\'|\'FULL\'
          )
        :type assessmentRunArn: string
        :param assessmentRunArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment run for which you want to generate a report.
        
        :type reportFileFormat: string
        :param reportFileFormat: **[REQUIRED]** 
        
          Specifies the file format (html or pdf) of the assessment report that you want to generate.
        
        :type reportType: string
        :param reportType: **[REQUIRED]** 
        
          Specifies the type of the assessment report that you want to generate. There are two types of assessment reports: a finding report and a full report. For more information, see `Assessment Reports <http://docs.aws.amazon.com/inspector/latest/userguide/inspector_reports.html>`__ . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'status\': \'WORK_IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                \'url\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **status** *(string) --* 
        
              Specifies the status of the request to generate an assessment report. 
        
            - **url** *(string) --* 
        
              Specifies the URL where you can find the generated assessment report. This parameter is only returned if the report is successfully generated.
        
        """
        pass

    def get_exclusions_preview(self, assessmentTemplateArn: str, previewToken: str, nextToken: str = None, maxResults: int = None, locale: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/GetExclusionsPreview>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_exclusions_preview(
              assessmentTemplateArn=\'string\',
              previewToken=\'string\',
              nextToken=\'string\',
              maxResults=123,
              locale=\'EN_US\'
          )
        :type assessmentTemplateArn: string
        :param assessmentTemplateArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment template for which the exclusions preview was requested.
        
        :type previewToken: string
        :param previewToken: **[REQUIRED]** 
        
          The unique identifier associated of the exclusions preview.
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the GetExclusionsPreviewRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.
        
        :type locale: string
        :param locale: 
        
          The locale into which you want to translate the exclusion\'s title, description, and recommendation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'previewStatus\': \'WORK_IN_PROGRESS\'|\'COMPLETED\',
                \'exclusionPreviews\': [
                    {
                        \'title\': \'string\',
                        \'description\': \'string\',
                        \'recommendation\': \'string\',
                        \'scopes\': [
                            {
                                \'key\': \'INSTANCE_ID\'|\'RULES_PACKAGE_ARN\',
                                \'value\': \'string\'
                            },
                        ],
                        \'attributes\': [
                            {
                                \'key\': \'string\',
                                \'value\': \'string\'
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **previewStatus** *(string) --* 
        
              Specifies the status of the request to generate an exclusions preview.
        
            - **exclusionPreviews** *(list) --* 
        
              Information about the exclusions included in the preview.
        
              - *(dict) --* 
        
                Contains information about what is excluded from an assessment run given the current state of the assessment template.
        
                - **title** *(string) --* 
        
                  The name of the exclusion preview.
        
                - **description** *(string) --* 
        
                  The description of the exclusion preview.
        
                - **recommendation** *(string) --* 
        
                  The recommendation for the exclusion preview.
        
                - **scopes** *(list) --* 
        
                  The AWS resources for which the exclusion preview pertains.
        
                  - *(dict) --* 
        
                    This data type contains key-value pairs that identify various Amazon resources.
        
                    - **key** *(string) --* 
        
                      The type of the scope.
        
                    - **value** *(string) --* 
        
                      The resource identifier for the specified scope type.
        
                - **attributes** *(list) --* 
        
                  The system-defined attributes for the exclusion preview.
        
                  - *(dict) --* 
        
                    This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
                    - **key** *(string) --* 
        
                      The attribute key.
        
                    - **value** *(string) --* 
        
                      The value assigned to the attribute key.
        
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
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

    def get_telemetry_metadata(self, assessmentRunArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/GetTelemetryMetadata>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_telemetry_metadata(
              assessmentRunArn=\'string\'
          )
        :type assessmentRunArn: string
        :param assessmentRunArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment run that has the telemetry data that you want to obtain.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'telemetryMetadata\': [
                    {
                        \'messageType\': \'string\',
                        \'count\': 123,
                        \'dataSize\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **telemetryMetadata** *(list) --* 
        
              Telemetry details.
        
              - *(dict) --* 
        
                The metadata about the Amazon Inspector application data metrics collected by the agent. This data type is used as the response element in the  GetTelemetryMetadata action.
        
                - **messageType** *(string) --* 
        
                  A specific type of behavioral data that is collected by the agent.
        
                - **count** *(integer) --* 
        
                  The count of messages that the agent sends to the Amazon Inspector service.
        
                - **dataSize** *(integer) --* 
        
                  The data size of messages that the agent sends to the Amazon Inspector service.
        
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

    def list_assessment_run_agents(self, assessmentRunArn: str, filter: Dict = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentRunAgents>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_assessment_run_agents(
              assessmentRunArn=\'string\',
              filter={
                  \'agentHealths\': [
                      \'HEALTHY\'|\'UNHEALTHY\'|\'UNKNOWN\',
                  ],
                  \'agentHealthCodes\': [
                      \'IDLE\'|\'RUNNING\'|\'SHUTDOWN\'|\'UNHEALTHY\'|\'THROTTLED\'|\'UNKNOWN\',
                  ]
              },
              nextToken=\'string\',
              maxResults=123
          )
        :type assessmentRunArn: string
        :param assessmentRunArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment run whose agents you want to list.
        
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **agentHealths** *(list) --* **[REQUIRED]** 
        
            The current health state of the agent. Values can be set to **HEALTHY** or **UNHEALTHY** .
        
            - *(string) --* 
        
          - **agentHealthCodes** *(list) --* **[REQUIRED]** 
        
            The detailed health state of the agent. Values can be set to **IDLE** , **RUNNING** , **SHUTDOWN** , **UNHEALTHY** , **THROTTLED** , and **UNKNOWN** . 
        
            - *(string) --* 
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentRunAgents** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentRunAgents\': [
                    {
                        \'agentId\': \'string\',
                        \'assessmentRunArn\': \'string\',
                        \'agentHealth\': \'HEALTHY\'|\'UNHEALTHY\'|\'UNKNOWN\',
                        \'agentHealthCode\': \'IDLE\'|\'RUNNING\'|\'SHUTDOWN\'|\'UNHEALTHY\'|\'THROTTLED\'|\'UNKNOWN\',
                        \'agentHealthDetails\': \'string\',
                        \'autoScalingGroup\': \'string\',
                        \'telemetryMetadata\': [
                            {
                                \'messageType\': \'string\',
                                \'count\': 123,
                                \'dataSize\': 123
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentRunAgents** *(list) --* 
        
              A list of ARNs that specifies the agents returned by the action.
        
              - *(dict) --* 
        
                Contains information about an Amazon Inspector agent. This data type is used as a response element in the  ListAssessmentRunAgents action.
        
                - **agentId** *(string) --* 
        
                  The AWS account of the EC2 instance where the agent is installed.
        
                - **assessmentRunArn** *(string) --* 
        
                  The ARN of the assessment run that is associated with the agent.
        
                - **agentHealth** *(string) --* 
        
                  The current health state of the agent.
        
                - **agentHealthCode** *(string) --* 
        
                  The detailed health state of the agent.
        
                - **agentHealthDetails** *(string) --* 
        
                  The description for the agent health code.
        
                - **autoScalingGroup** *(string) --* 
        
                  The Auto Scaling group of the EC2 instance that is specified by the agent ID.
        
                - **telemetryMetadata** *(list) --* 
        
                  The Amazon Inspector application data metrics that are collected by the agent.
        
                  - *(dict) --* 
        
                    The metadata about the Amazon Inspector application data metrics collected by the agent. This data type is used as the response element in the  GetTelemetryMetadata action.
        
                    - **messageType** *(string) --* 
        
                      A specific type of behavioral data that is collected by the agent.
        
                    - **count** *(integer) --* 
        
                      The count of messages that the agent sends to the Amazon Inspector service.
        
                    - **dataSize** *(integer) --* 
        
                      The data size of messages that the agent sends to the Amazon Inspector service.
        
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def list_assessment_runs(self, assessmentTemplateArns: List = None, filter: Dict = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentRuns>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_assessment_runs(
              assessmentTemplateArns=[
                  \'string\',
              ],
              filter={
                  \'namePattern\': \'string\',
                  \'states\': [
                      \'CREATED\'|\'START_DATA_COLLECTION_PENDING\'|\'START_DATA_COLLECTION_IN_PROGRESS\'|\'COLLECTING_DATA\'|\'STOP_DATA_COLLECTION_PENDING\'|\'DATA_COLLECTED\'|\'START_EVALUATING_RULES_PENDING\'|\'EVALUATING_RULES\'|\'FAILED\'|\'ERROR\'|\'COMPLETED\'|\'COMPLETED_WITH_ERRORS\'|\'CANCELED\',
                  ],
                  \'durationRange\': {
                      \'minSeconds\': 123,
                      \'maxSeconds\': 123
                  },
                  \'rulesPackageArns\': [
                      \'string\',
                  ],
                  \'startTimeRange\': {
                      \'beginDate\': datetime(2015, 1, 1),
                      \'endDate\': datetime(2015, 1, 1)
                  },
                  \'completionTimeRange\': {
                      \'beginDate\': datetime(2015, 1, 1),
                      \'endDate\': datetime(2015, 1, 1)
                  },
                  \'stateChangeTimeRange\': {
                      \'beginDate\': datetime(2015, 1, 1),
                      \'endDate\': datetime(2015, 1, 1)
                  }
              },
              nextToken=\'string\',
              maxResults=123
          )
        :type assessmentTemplateArns: list
        :param assessmentTemplateArns: 
        
          The ARNs that specify the assessment templates whose assessment runs you want to list.
        
          - *(string) --* 
        
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **namePattern** *(string) --* 
        
            For a record to match a filter, an explicit value or a string containing a wildcard that is specified for this data type property must match the value of the **assessmentRunName** property of the  AssessmentRun data type.
        
          - **states** *(list) --* 
        
            For a record to match a filter, one of the values specified for this data type property must be the exact match of the value of the **assessmentRunState** property of the  AssessmentRun data type.
        
            - *(string) --* 
        
          - **durationRange** *(dict) --* 
        
            For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **durationInSeconds** property of the  AssessmentRun data type.
        
            - **minSeconds** *(integer) --* 
        
              The minimum value of the duration range. Must be greater than zero.
        
            - **maxSeconds** *(integer) --* 
        
              The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).
        
          - **rulesPackageArns** *(list) --* 
        
            For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the **rulesPackages** property of the  AssessmentRun data type.
        
            - *(string) --* 
        
          - **startTimeRange** *(dict) --* 
        
            For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **startTime** property of the  AssessmentRun data type.
        
            - **beginDate** *(datetime) --* 
        
              The minimum value of the timestamp range.
        
            - **endDate** *(datetime) --* 
        
              The maximum value of the timestamp range.
        
          - **completionTimeRange** *(dict) --* 
        
            For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **completedAt** property of the  AssessmentRun data type.
        
            - **beginDate** *(datetime) --* 
        
              The minimum value of the timestamp range.
        
            - **endDate** *(datetime) --* 
        
              The maximum value of the timestamp range.
        
          - **stateChangeTimeRange** *(dict) --* 
        
            For a record to match a filter, the value that is specified for this data type property must match the **stateChangedAt** property of the  AssessmentRun data type.
        
            - **beginDate** *(datetime) --* 
        
              The minimum value of the timestamp range.
        
            - **endDate** *(datetime) --* 
        
              The maximum value of the timestamp range.
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentRuns** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentRunArns\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentRunArns** *(list) --* 
        
              A list of ARNs that specifies the assessment runs that are returned by the action.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def list_assessment_targets(self, filter: Dict = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_assessment_targets(
              filter={
                  \'assessmentTargetNamePattern\': \'string\'
              },
              nextToken=\'string\',
              maxResults=123
          )
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **assessmentTargetNamePattern** *(string) --* 
        
            For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the **assessmentTargetName** property of the  AssessmentTarget data type.
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentTargets** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentTargetArns\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentTargetArns** *(list) --* 
        
              A list of ARNs that specifies the assessment targets that are returned by the action.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def list_assessment_templates(self, assessmentTargetArns: List = None, filter: Dict = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentTemplates>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_assessment_templates(
              assessmentTargetArns=[
                  \'string\',
              ],
              filter={
                  \'namePattern\': \'string\',
                  \'durationRange\': {
                      \'minSeconds\': 123,
                      \'maxSeconds\': 123
                  },
                  \'rulesPackageArns\': [
                      \'string\',
                  ]
              },
              nextToken=\'string\',
              maxResults=123
          )
        :type assessmentTargetArns: list
        :param assessmentTargetArns: 
        
          A list of ARNs that specifies the assessment targets whose assessment templates you want to list.
        
          - *(string) --* 
        
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **namePattern** *(string) --* 
        
            For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the **assessmentTemplateName** property of the  AssessmentTemplate data type.
        
          - **durationRange** *(dict) --* 
        
            For a record to match a filter, the value specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **durationInSeconds** property of the  AssessmentTemplate data type.
        
            - **minSeconds** *(integer) --* 
        
              The minimum value of the duration range. Must be greater than zero.
        
            - **maxSeconds** *(integer) --* 
        
              The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).
        
          - **rulesPackageArns** *(list) --* 
        
            For a record to match a filter, the values that are specified for this data type property must be contained in the list of values of the **rulesPackageArns** property of the  AssessmentTemplate data type.
        
            - *(string) --* 
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentTemplates** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentTemplateArns\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentTemplateArns** *(list) --* 
        
              A list of ARNs that specifies the assessment templates returned by the action.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def list_event_subscriptions(self, resourceArn: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListEventSubscriptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_event_subscriptions(
              resourceArn=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type resourceArn: string
        :param resourceArn: 
        
          The ARN of the assessment template for which you want to list the existing event subscriptions.
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListEventSubscriptions** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'subscriptions\': [
                    {
                        \'resourceArn\': \'string\',
                        \'topicArn\': \'string\',
                        \'eventSubscriptions\': [
                            {
                                \'event\': \'ASSESSMENT_RUN_STARTED\'|\'ASSESSMENT_RUN_COMPLETED\'|\'ASSESSMENT_RUN_STATE_CHANGED\'|\'FINDING_REPORTED\'|\'OTHER\',
                                \'subscribedAt\': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **subscriptions** *(list) --* 
        
              Details of the returned event subscriptions.
        
              - *(dict) --* 
        
                This data type is used as a response element in the  ListEventSubscriptions action.
        
                - **resourceArn** *(string) --* 
        
                  The ARN of the assessment template that is used during the event for which the SNS notification is sent.
        
                - **topicArn** *(string) --* 
        
                  The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS notifications are sent.
        
                - **eventSubscriptions** *(list) --* 
        
                  The list of existing event subscriptions.
        
                  - *(dict) --* 
        
                    This data type is used in the  Subscription data type.
        
                    - **event** *(string) --* 
        
                      The event for which Amazon Simple Notification Service (SNS) notifications are sent.
        
                    - **subscribedAt** *(datetime) --* 
        
                      The time at which  SubscribeToEvent is called.
        
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def list_exclusions(self, assessmentRunArn: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListExclusions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_exclusions(
              assessmentRunArn=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type assessmentRunArn: string
        :param assessmentRunArn: **[REQUIRED]** 
        
          The ARN of the assessment run that generated the exclusions that you want to list.
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListExclusionsRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'exclusionArns\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **exclusionArns** *(list) --* 
        
              A list of exclusions\' ARNs returned by the action.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def list_findings(self, assessmentRunArns: List = None, filter: Dict = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_findings(
              assessmentRunArns=[
                  \'string\',
              ],
              filter={
                  \'agentIds\': [
                      \'string\',
                  ],
                  \'autoScalingGroups\': [
                      \'string\',
                  ],
                  \'ruleNames\': [
                      \'string\',
                  ],
                  \'severities\': [
                      \'Low\'|\'Medium\'|\'High\'|\'Informational\'|\'Undefined\',
                  ],
                  \'rulesPackageArns\': [
                      \'string\',
                  ],
                  \'attributes\': [
                      {
                          \'key\': \'string\',
                          \'value\': \'string\'
                      },
                  ],
                  \'userAttributes\': [
                      {
                          \'key\': \'string\',
                          \'value\': \'string\'
                      },
                  ],
                  \'creationTimeRange\': {
                      \'beginDate\': datetime(2015, 1, 1),
                      \'endDate\': datetime(2015, 1, 1)
                  }
              },
              nextToken=\'string\',
              maxResults=123
          )
        :type assessmentRunArns: list
        :param assessmentRunArns: 
        
          The ARNs of the assessment runs that generate the findings that you want to list.
        
          - *(string) --* 
        
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **agentIds** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **agentId** property of the  Finding data type.
        
            - *(string) --* 
        
          - **autoScalingGroups** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **autoScalingGroup** property of the  Finding data type.
        
            - *(string) --* 
        
          - **ruleNames** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **ruleName** property of the  Finding data type.
        
            - *(string) --* 
        
          - **severities** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **severity** property of the  Finding data type.
        
            - *(string) --* 
        
          - **rulesPackageArns** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **rulesPackageArn** property of the  Finding data type.
        
            - *(string) --* 
        
          - **attributes** *(list) --* 
        
            For a record to match a filter, the list of values that are specified for this data type property must be contained in the list of values of the **attributes** property of the  Finding data type.
        
            - *(dict) --* 
        
              This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
              - **key** *(string) --* **[REQUIRED]** 
        
                The attribute key.
        
              - **value** *(string) --* 
        
                The value assigned to the attribute key.
        
          - **userAttributes** *(list) --* 
        
            For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the **userAttributes** property of the  Finding data type.
        
            - *(dict) --* 
        
              This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
              - **key** *(string) --* **[REQUIRED]** 
        
                The attribute key.
        
              - **value** *(string) --* 
        
                The value assigned to the attribute key.
        
          - **creationTimeRange** *(dict) --* 
        
            The time range during which the finding is generated.
        
            - **beginDate** *(datetime) --* 
        
              The minimum value of the timestamp range.
        
            - **endDate** *(datetime) --* 
        
              The maximum value of the timestamp range.
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListFindings** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'findingArns\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **findingArns** *(list) --* 
        
              A list of ARNs that specifies the findings returned by the action.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def list_rules_packages(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListRulesPackages>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_rules_packages(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListRulesPackages** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'rulesPackageArns\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **rulesPackageArns** *(list) --* 
        
              The list of ARNs that specifies the rules packages returned by the action.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def list_tags_for_resource(self, resourceArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              resourceArn=\'string\'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment template whose tags you want to list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'tags\': [
                    {
                        \'key\': \'string\',
                        \'value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **tags** *(list) --* 
        
              A collection of key and value pairs.
        
              - *(dict) --* 
        
                A key and value pair. This data type is used as a request parameter in the  SetTagsForResource action and a response element in the  ListTagsForResource action.
        
                - **key** *(string) --* 
        
                  A tag key.
        
                - **value** *(string) --* 
        
                  A value assigned to a tag key.
        
        """
        pass

    def preview_agents(self, previewAgentsArn: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/PreviewAgents>`_
        
        **Request Syntax** 
        ::
        
          response = client.preview_agents(
              previewAgentsArn=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type previewAgentsArn: string
        :param previewAgentsArn: **[REQUIRED]** 
        
          The ARN of the assessment target whose agents you want to preview.
        
        :type nextToken: string
        :param nextToken: 
        
          You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **PreviewAgents** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
        
        :type maxResults: integer
        :param maxResults: 
        
          You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'agentPreviews\': [
                    {
                        \'hostname\': \'string\',
                        \'agentId\': \'string\',
                        \'autoScalingGroup\': \'string\',
                        \'agentHealth\': \'HEALTHY\'|\'UNHEALTHY\'|\'UNKNOWN\',
                        \'agentVersion\': \'string\',
                        \'operatingSystem\': \'string\',
                        \'kernelVersion\': \'string\',
                        \'ipv4Address\': \'string\'
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **agentPreviews** *(list) --* 
        
              The resulting list of agents.
        
              - *(dict) --* 
        
                Used as a response element in the  PreviewAgents action.
        
                - **hostname** *(string) --* 
        
                  The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.
        
                - **agentId** *(string) --* 
        
                  The ID of the EC2 instance where the agent is installed.
        
                - **autoScalingGroup** *(string) --* 
        
                  The Auto Scaling group for the EC2 instance where the agent is installed.
        
                - **agentHealth** *(string) --* 
        
                  The health status of the Amazon Inspector Agent.
        
                - **agentVersion** *(string) --* 
        
                  The version of the Amazon Inspector Agent.
        
                - **operatingSystem** *(string) --* 
        
                  The operating system running on the EC2 instance on which the Amazon Inspector Agent is installed.
        
                - **kernelVersion** *(string) --* 
        
                  The kernel version of the operating system running on the EC2 instance on which the Amazon Inspector Agent is installed.
        
                - **ipv4Address** *(string) --* 
        
                  The IP address of the EC2 instance on which the Amazon Inspector Agent is installed.
        
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
        
        """
        pass

    def register_cross_account_access_role(self, roleArn: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/RegisterCrossAccountAccessRole>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_cross_account_access_role(
              roleArn=\'string\'
          )
        :type roleArn: string
        :param roleArn: **[REQUIRED]** 
        
          The ARN of the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments. 
        
        :returns: None
        """
        pass

    def remove_attributes_from_findings(self, findingArns: List, attributeKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/RemoveAttributesFromFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_attributes_from_findings(
              findingArns=[
                  \'string\',
              ],
              attributeKeys=[
                  \'string\',
              ]
          )
        :type findingArns: list
        :param findingArns: **[REQUIRED]** 
        
          The ARNs that specify the findings that you want to remove attributes from.
        
          - *(string) --* 
        
        :type attributeKeys: list
        :param attributeKeys: **[REQUIRED]** 
        
          The array of attribute keys that you want to remove from specified findings.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'failedItems\': {
                    \'string\': {
                        \'failureCode\': \'INVALID_ARN\'|\'DUPLICATE_ARN\'|\'ITEM_DOES_NOT_EXIST\'|\'ACCESS_DENIED\'|\'LIMIT_EXCEEDED\'|\'INTERNAL_ERROR\',
                        \'retryable\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **failedItems** *(dict) --* 
        
              Attributes details that cannot be described. An error code is provided for each failed item.
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Includes details about the failed items.
        
                  - **failureCode** *(string) --* 
        
                    The status code of a failed item.
        
                  - **retryable** *(boolean) --* 
        
                    Indicates whether you can immediately retry a request for this item for a specified resource.
        
        """
        pass

    def set_tags_for_resource(self, resourceArn: str, tags: List = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/SetTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_tags_for_resource(
              resourceArn=\'string\',
              tags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]** 
        
          The ARN of the assessment template that you want to set tags to.
        
        :type tags: list
        :param tags: 
        
          A collection of key and value pairs that you want to set to the assessment template.
        
          - *(dict) --* 
        
            A key and value pair. This data type is used as a request parameter in the  SetTagsForResource action and a response element in the  ListTagsForResource action.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              A tag key.
        
            - **value** *(string) --* 
        
              A value assigned to a tag key.
        
        :returns: None
        """
        pass

    def start_assessment_run(self, assessmentTemplateArn: str, assessmentRunName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/StartAssessmentRun>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_assessment_run(
              assessmentTemplateArn=\'string\',
              assessmentRunName=\'string\'
          )
        :type assessmentTemplateArn: string
        :param assessmentTemplateArn: **[REQUIRED]** 
        
          The ARN of the assessment template of the assessment run that you want to start.
        
        :type assessmentRunName: string
        :param assessmentRunName: 
        
          You can specify the name for the assessment run. The name must be unique for the assessment template whose ARN is used to start the assessment run.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'assessmentRunArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentRunArn** *(string) --* 
        
              The ARN of the assessment run that has been started.
        
        """
        pass

    def stop_assessment_run(self, assessmentRunArn: str, stopAction: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/StopAssessmentRun>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_assessment_run(
              assessmentRunArn=\'string\',
              stopAction=\'START_EVALUATION\'|\'SKIP_EVALUATION\'
          )
        :type assessmentRunArn: string
        :param assessmentRunArn: **[REQUIRED]** 
        
          The ARN of the assessment run that you want to stop.
        
        :type stopAction: string
        :param stopAction: 
        
          An input option that can be set to either START_EVALUATION or SKIP_EVALUATION. START_EVALUATION (the default value), stops the AWS agent from collecting data and begins the results evaluation and the findings generation process. SKIP_EVALUATION cancels the assessment run immediately, after which no findings are generated.
        
        :returns: None
        """
        pass

    def subscribe_to_event(self, resourceArn: str, event: str, topicArn: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/SubscribeToEvent>`_
        
        **Request Syntax** 
        ::
        
          response = client.subscribe_to_event(
              resourceArn=\'string\',
              event=\'ASSESSMENT_RUN_STARTED\'|\'ASSESSMENT_RUN_COMPLETED\'|\'ASSESSMENT_RUN_STATE_CHANGED\'|\'FINDING_REPORTED\'|\'OTHER\',
              topicArn=\'string\'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]** 
        
          The ARN of the assessment template that is used during the event for which you want to receive SNS notifications.
        
        :type event: string
        :param event: **[REQUIRED]** 
        
          The event for which you want to receive SNS notifications.
        
        :type topicArn: string
        :param topicArn: **[REQUIRED]** 
        
          The ARN of the SNS topic to which the SNS notifications are sent.
        
        :returns: None
        """
        pass

    def unsubscribe_from_event(self, resourceArn: str, event: str, topicArn: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/UnsubscribeFromEvent>`_
        
        **Request Syntax** 
        ::
        
          response = client.unsubscribe_from_event(
              resourceArn=\'string\',
              event=\'ASSESSMENT_RUN_STARTED\'|\'ASSESSMENT_RUN_COMPLETED\'|\'ASSESSMENT_RUN_STATE_CHANGED\'|\'FINDING_REPORTED\'|\'OTHER\',
              topicArn=\'string\'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]** 
        
          The ARN of the assessment template that is used during the event for which you want to stop receiving SNS notifications.
        
        :type event: string
        :param event: **[REQUIRED]** 
        
          The event for which you want to stop receiving SNS notifications.
        
        :type topicArn: string
        :param topicArn: **[REQUIRED]** 
        
          The ARN of the SNS topic to which SNS notifications are sent.
        
        :returns: None
        """
        pass

    def update_assessment_target(self, assessmentTargetArn: str, assessmentTargetName: str, resourceGroupArn: str = None):
        """
        
        If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/UpdateAssessmentTarget>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_assessment_target(
              assessmentTargetArn=\'string\',
              assessmentTargetName=\'string\',
              resourceGroupArn=\'string\'
          )
        :type assessmentTargetArn: string
        :param assessmentTargetArn: **[REQUIRED]** 
        
          The ARN of the assessment target that you want to update.
        
        :type assessmentTargetName: string
        :param assessmentTargetName: **[REQUIRED]** 
        
          The name of the assessment target that you want to update.
        
        :type resourceGroupArn: string
        :param resourceGroupArn: 
        
          The ARN of the resource group that is used to specify the new resource group to associate with the assessment target.
        
        :returns: None
        """
        pass
