from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def accept_invitation(self, MasterId: str = None, InvitationId: str = None) -> Dict:
        """
        Accepts the invitation to be monitored by a master SecurityHub account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/AcceptInvitation>`_
        
        **Request Syntax**
        ::
          response = client.accept_invitation(
              MasterId='string',
              InvitationId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type MasterId: string
        :param MasterId:
          The account ID of the master Security Hub account whose invitation you\'re accepting.
        :type InvitationId: string
        :param InvitationId:
          The ID of the invitation that is sent to the AWS account by the Security Hub master account.
        :rtype: dict
        :returns:
        """
        pass

    def batch_disable_standards(self, StandardsSubscriptionArns: List) -> Dict:
        """
        Disables the standards specified by the standards subscription ARNs. In the context of Security Hub, supported standards (for example, CIS AWS Foundations) are automated and continuous checks that help determine your compliance status against security industry (including AWS) best practices. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchDisableStandards>`_
        
        **Request Syntax**
        ::
          response = client.batch_disable_standards(
              StandardsSubscriptionArns=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'StandardsSubscriptions': [
                    {
                        'StandardsSubscriptionArn': 'string',
                        'StandardsArn': 'string',
                        'StandardsInput': {
                            'string': 'string'
                        },
                        'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **StandardsSubscriptions** *(list) --* 
              The details of the standards subscriptions that were disabled.
              - *(dict) --* 
                A resource that represents your subscription to a supported standard.
                - **StandardsSubscriptionArn** *(string) --* 
                  The ARN of a resource that represents your subscription to a supported standard.
                - **StandardsArn** *(string) --* 
                  The ARN of a standard.
                - **StandardsInput** *(dict) --* 
                  - *(string) --* 
                    - *(string) --* 
                - **StandardsStatus** *(string) --* 
                  The standard's status.
        :type StandardsSubscriptionArns: list
        :param StandardsSubscriptionArns: **[REQUIRED]**
          The ARNS of the standards subscriptions that you want to disable.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def batch_enable_standards(self, StandardsSubscriptionRequests: List) -> Dict:
        """
        Enables the standards specified by the standards ARNs. In the context of Security Hub, supported standards (for example, CIS AWS Foundations) are automated and continuous checks that help determine your compliance status against security industry (including AWS) best practices. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchEnableStandards>`_
        
        **Request Syntax**
        ::
          response = client.batch_enable_standards(
              StandardsSubscriptionRequests=[
                  {
                      'StandardsArn': 'string',
                      'StandardsInput': {
                          'string': 'string'
                      }
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'StandardsSubscriptions': [
                    {
                        'StandardsSubscriptionArn': 'string',
                        'StandardsArn': 'string',
                        'StandardsInput': {
                            'string': 'string'
                        },
                        'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **StandardsSubscriptions** *(list) --* 
              The details of the standards subscriptions that were enabled.
              - *(dict) --* 
                A resource that represents your subscription to a supported standard.
                - **StandardsSubscriptionArn** *(string) --* 
                  The ARN of a resource that represents your subscription to a supported standard.
                - **StandardsArn** *(string) --* 
                  The ARN of a standard.
                - **StandardsInput** *(dict) --* 
                  - *(string) --* 
                    - *(string) --* 
                - **StandardsStatus** *(string) --* 
                  The standard's status.
        :type StandardsSubscriptionRequests: list
        :param StandardsSubscriptionRequests: **[REQUIRED]**
          The list of standards that you want to enable.
          - *(dict) --*
            The standard that you want to enable.
            - **StandardsArn** *(string) --* **[REQUIRED]**
              The ARN of the standard that you want to enable.
            - **StandardsInput** *(dict) --*
              - *(string) --*
                - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def batch_import_findings(self, Findings: List) -> Dict:
        """
        Imports security findings that are generated by the integrated third-party products into Security Hub.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchImportFindings>`_
        
        **Request Syntax**
        ::
          response = client.batch_import_findings(
              Findings=[
                  {
                      'SchemaVersion': 'string',
                      'Id': 'string',
                      'ProductArn': 'string',
                      'GeneratorId': 'string',
                      'AwsAccountId': 'string',
                      'Types': [
                          'string',
                      ],
                      'FirstObservedAt': 'string',
                      'LastObservedAt': 'string',
                      'CreatedAt': 'string',
                      'UpdatedAt': 'string',
                      'Severity': {
                          'Product': 123.0,
                          'Normalized': 123
                      },
                      'Confidence': 123,
                      'Criticality': 123,
                      'Title': 'string',
                      'Description': 'string',
                      'Remediation': {
                          'Recommendation': {
                              'Text': 'string',
                              'Url': 'string'
                          }
                      },
                      'SourceUrl': 'string',
                      'ProductFields': {
                          'string': 'string'
                      },
                      'UserDefinedFields': {
                          'string': 'string'
                      },
                      'Malware': [
                          {
                              'Name': 'string',
                              'Type': 'ADWARE'|'BLENDED_THREAT'|'BOTNET_AGENT'|'COIN_MINER'|'EXPLOIT_KIT'|'KEYLOGGER'|'MACRO'|'POTENTIALLY_UNWANTED'|'SPYWARE'|'RANSOMWARE'|'REMOTE_ACCESS'|'ROOTKIT'|'TROJAN'|'VIRUS'|'WORM',
                              'Path': 'string',
                              'State': 'OBSERVED'|'REMOVAL_FAILED'|'REMOVED'
                          },
                      ],
                      'Network': {
                          'Direction': 'IN'|'OUT',
                          'Protocol': 'string',
                          'SourceIpV4': 'string',
                          'SourceIpV6': 'string',
                          'SourcePort': 123,
                          'SourceDomain': 'string',
                          'SourceMac': 'string',
                          'DestinationIpV4': 'string',
                          'DestinationIpV6': 'string',
                          'DestinationPort': 123,
                          'DestinationDomain': 'string'
                      },
                      'Process': {
                          'Name': 'string',
                          'Path': 'string',
                          'Pid': 123,
                          'ParentPid': 123,
                          'LaunchedAt': 'string',
                          'TerminatedAt': 'string'
                      },
                      'ThreatIntelIndicators': [
                          {
                              'Type': 'DOMAIN'|'EMAIL_ADDRESS'|'HASH_MD5'|'HASH_SHA1'|'HASH_SHA256'|'HASH_SHA512'|'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MUTEX'|'PROCESS'|'URL',
                              'Value': 'string',
                              'Category': 'BACKDOOR'|'CARD_STEALER'|'COMMAND_AND_CONTROL'|'DROP_SITE'|'EXPLOIT_SITE'|'KEYLOGGER',
                              'LastObservedAt': 'string',
                              'Source': 'string',
                              'SourceUrl': 'string'
                          },
                      ],
                      'Resources': [
                          {
                              'Type': 'string',
                              'Id': 'string',
                              'Partition': 'aws'|'aws-cn'|'aws-us-gov',
                              'Region': 'string',
                              'Tags': {
                                  'string': 'string'
                              },
                              'Details': {
                                  'AwsEc2Instance': {
                                      'Type': 'string',
                                      'ImageId': 'string',
                                      'IpV4Addresses': [
                                          'string',
                                      ],
                                      'IpV6Addresses': [
                                          'string',
                                      ],
                                      'KeyName': 'string',
                                      'IamInstanceProfileArn': 'string',
                                      'VpcId': 'string',
                                      'SubnetId': 'string',
                                      'LaunchedAt': 'string'
                                  },
                                  'AwsS3Bucket': {
                                      'OwnerId': 'string',
                                      'OwnerName': 'string'
                                  },
                                  'AwsIamAccessKey': {
                                      'UserName': 'string',
                                      'Status': 'Active'|'Inactive',
                                      'CreatedAt': 'string'
                                  },
                                  'Container': {
                                      'Name': 'string',
                                      'ImageId': 'string',
                                      'ImageName': 'string',
                                      'LaunchedAt': 'string'
                                  },
                                  'Other': {
                                      'string': 'string'
                                  }
                              }
                          },
                      ],
                      'Compliance': {
                          'Status': 'PASSED'|'WARNING'|'FAILED'|'NOT_AVAILABLE'
                      },
                      'VerificationState': 'UNKNOWN'|'TRUE_POSITIVE'|'FALSE_POSITIVE'|'BENIGN_POSITIVE',
                      'WorkflowState': 'NEW'|'ASSIGNED'|'IN_PROGRESS'|'DEFERRED'|'RESOLVED',
                      'RecordState': 'ACTIVE'|'ARCHIVED',
                      'RelatedFindings': [
                          {
                              'ProductArn': 'string',
                              'Id': 'string'
                          },
                      ],
                      'Note': {
                          'Text': 'string',
                          'UpdatedBy': 'string',
                          'UpdatedAt': 'string'
                      }
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedCount': 123,
                'SuccessCount': 123,
                'FailedFindings': [
                    {
                        'Id': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedCount** *(integer) --* 
              The number of findings that cannot be imported.
            - **SuccessCount** *(integer) --* 
              The number of findings that were successfully imported
            - **FailedFindings** *(list) --* 
              The list of the findings that cannot be imported.
              - *(dict) --* 
                Includes details of the list of the findings that cannot be imported. 
                - **Id** *(string) --* 
                  The id of the error made during the BatchImportFindings operation.
                - **ErrorCode** *(string) --* 
                  The code of the error made during the BatchImportFindings operation. 
                - **ErrorMessage** *(string) --* 
                  The message of the error made during the BatchImportFindings operation. 
        :type Findings: list
        :param Findings: **[REQUIRED]**
          A list of findings that you want to import. Must be submitted in the AWSSecurityFinding format.
          - *(dict) --*
            Provides consistent format for the contents of the Security Hub-aggregated findings. AwsSecurityFinding format enables you to share findings between AWS security services and third-party solutions, and compliance checks.
            .. note::
              A finding is a potential security issue generated either by AWS services (GuardDuty, Inspector, Macie) or by the integrated third-party solutions and compliance checks.
            - **SchemaVersion** *(string) --* **[REQUIRED]**
              The schema version for which a finding is formatted.
            - **Id** *(string) --* **[REQUIRED]**
              The security findings provider-specific identifier for a finding.
            - **ProductArn** *(string) --* **[REQUIRED]**
              The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) once this provider\'s product (solution that generates findings) is registered with Security Hub.
            - **GeneratorId** *(string) --* **[REQUIRED]**
              This is the identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings provider\'s solutions, this generator can be called a rule, a check, a detector, a plug-in, etc.
            - **AwsAccountId** *(string) --* **[REQUIRED]**
              The AWS account ID in which a finding is generated.
            - **Types** *(list) --* **[REQUIRED]**
              One or more finding types in the format of \'namespace/category/classifier\' that classify a finding.
              Valid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual Behaviors | Sensitive Data Identifications
              - *(string) --*
            - **FirstObservedAt** *(string) --*
              An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings provider.
            - **LastObservedAt** *(string) --*
              An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings provider.
            - **CreatedAt** *(string) --* **[REQUIRED]**
              An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was created by the security findings provider.
            - **UpdatedAt** *(string) --* **[REQUIRED]**
              An ISO8601-formatted timestamp that indicates when the finding record was last updated by the security findings provider.
            - **Severity** *(dict) --* **[REQUIRED]**
              A finding\'s severity.
              - **Product** *(float) --*
                The native severity as defined by the security findings provider\'s solution that generated the finding.
              - **Normalized** *(integer) --* **[REQUIRED]**
                The normalized severity of a finding.
            - **Confidence** *(integer) --*
              A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale. 0 equates zero percent confidence and 100 equates to 100 percent confidence.
            - **Criticality** *(integer) --*
              The level of importance assigned to the resources associated with the finding. A score of 0 means the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
            - **Title** *(string) --*
              A finding\'s title.
            - **Description** *(string) --*
              A finding\'s description.
            - **Remediation** *(dict) --*
              An data type that describes the remediation options for a finding.
              - **Recommendation** *(dict) --*
                Provides a recommendation on how to remediate the issue identified within a finding.
                - **Text** *(string) --*
                  The recommendation of what to do about the issue described in a finding.
                - **Url** *(string) --*
                  A URL to link to general remediation information for the finding type of a finding.
            - **SourceUrl** *(string) --*
              A URL that links to a page about the current finding in the security findings provider\'s solution.
            - **ProductFields** *(dict) --*
              A data type where security findings providers can include additional solution-specific details that are not part of the defined AwsSecurityFinding format.
              - *(string) --*
                - *(string) --*
            - **UserDefinedFields** *(dict) --*
              A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
              - *(string) --*
                - *(string) --*
            - **Malware** *(list) --*
              A list of malware related to a finding.
              - *(dict) --*
                A list of malware related to a finding.
                - **Name** *(string) --* **[REQUIRED]**
                  The name of the malware that was observed.
                - **Type** *(string) --*
                  The type of the malware that was observed.
                - **Path** *(string) --*
                  The filesystem path of the malware that was observed.
                - **State** *(string) --*
                  The state of the malware that was observed.
            - **Network** *(dict) --*
              The details of network-related information about a finding.
              - **Direction** *(string) --*
                Indicates the direction of network traffic associated with a finding.
              - **Protocol** *(string) --*
                The protocol of network-related information about a finding.
              - **SourceIpV4** *(string) --*
                The source IPv4 address of network-related information about a finding.
              - **SourceIpV6** *(string) --*
                The source IPv6 address of network-related information about a finding.
              - **SourcePort** *(integer) --*
                The source port of network-related information about a finding.
              - **SourceDomain** *(string) --*
                The source domain of network-related information about a finding.
              - **SourceMac** *(string) --*
                The source media access control (MAC) address of network-related information about a finding.
              - **DestinationIpV4** *(string) --*
                The destination IPv4 address of network-related information about a finding.
              - **DestinationIpV6** *(string) --*
                The destination IPv6 address of network-related information about a finding.
              - **DestinationPort** *(integer) --*
                The destination port of network-related information about a finding.
              - **DestinationDomain** *(string) --*
                The destination domain of network-related information about a finding.
            - **Process** *(dict) --*
              The details of process-related information about a finding.
              - **Name** *(string) --*
                The name of the process.
              - **Path** *(string) --*
                The path to the process executable.
              - **Pid** *(integer) --*
                The process ID.
              - **ParentPid** *(integer) --*
                The parent process ID.
              - **LaunchedAt** *(string) --*
                The date/time that the process was launched.
              - **TerminatedAt** *(string) --*
                The date/time that the process was terminated.
            - **ThreatIntelIndicators** *(list) --*
              Threat intel details related to a finding.
              - *(dict) --*
                Threat intel details related to a finding.
                - **Type** *(string) --*
                  The type of a threat intel indicator.
                - **Value** *(string) --*
                  The value of a threat intel indicator.
                - **Category** *(string) --*
                  The category of a threat intel indicator.
                - **LastObservedAt** *(string) --*
                  The date/time of the last observation of a threat intel indicator.
                - **Source** *(string) --*
                  The source of the threat intel.
                - **SourceUrl** *(string) --*
                  The URL for more details from the source of the threat intel.
            - **Resources** *(list) --* **[REQUIRED]**
              A set of resource data types that describe the resources to which the finding refers.
              - *(dict) --*
                A resource data type that describes a resource to which the finding refers.
                - **Type** *(string) --* **[REQUIRED]**
                  Specifies the type of the resource for which details are provided.
                - **Id** *(string) --* **[REQUIRED]**
                  The canonical identifier for the given resource type.
                - **Partition** *(string) --*
                  The canonical AWS partition name to which the region is assigned.
                - **Region** *(string) --*
                  The canonical AWS external region name where this resource is located.
                - **Tags** *(dict) --*
                  A list of AWS tags associated with a resource at the time the finding was processed.
                  - *(string) --*
                    - *(string) --*
                - **Details** *(dict) --*
                  Provides additional details about the resource.
                  - **AwsEc2Instance** *(dict) --*
                    The details of an AWS EC2 instance.
                    - **Type** *(string) --*
                      The instance type of the instance.
                    - **ImageId** *(string) --*
                      The Amazon Machine Image (AMI) ID of the instance.
                    - **IpV4Addresses** *(list) --*
                      The IPv4 addresses associated with the instance.
                      - *(string) --*
                    - **IpV6Addresses** *(list) --*
                      The IPv6 addresses associated with the instance.
                      - *(string) --*
                    - **KeyName** *(string) --*
                      The key name associated with the instance.
                    - **IamInstanceProfileArn** *(string) --*
                      The IAM profile ARN of the instance.
                    - **VpcId** *(string) --*
                      The identifier of the VPC in which the instance was launched.
                    - **SubnetId** *(string) --*
                      The identifier of the subnet in which the instance was launched.
                    - **LaunchedAt** *(string) --*
                      The date/time the instance was launched.
                  - **AwsS3Bucket** *(dict) --*
                    The details of an AWS S3 Bucket.
                    - **OwnerId** *(string) --*
                      The canonical user ID of the owner of the S3 bucket.
                    - **OwnerName** *(string) --*
                      The display name of the owner of the S3 bucket.
                  - **AwsIamAccessKey** *(dict) --*
                    AWS IAM access key details related to a finding.
                    - **UserName** *(string) --*
                      The user associated with the IAM access key related to a finding.
                    - **Status** *(string) --*
                      The status of the IAM access key related to a finding.
                    - **CreatedAt** *(string) --*
                      The creation date/time of the IAM access key related to a finding.
                  - **Container** *(dict) --*
                    Container details related to a finding.
                    - **Name** *(string) --*
                      The name of the container related to a finding.
                    - **ImageId** *(string) --*
                      The identifier of the image related to a finding.
                    - **ImageName** *(string) --*
                      The name of the image related to a finding.
                    - **LaunchedAt** *(string) --*
                      The date/time that the container was started.
                  - **Other** *(dict) --*
                    The details of a resource that does not have a specific sub-field for the resource type defined.
                    - *(string) --*
                      - *(string) --*
            - **Compliance** *(dict) --*
              This data type is exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard (for example, AWS CIS Foundations). Contains compliance-related finding details.
              - **Status** *(string) --*
                Indicates the result of a compliance check.
            - **VerificationState** *(string) --*
              Indicates the veracity of a finding.
            - **WorkflowState** *(string) --*
              The workflow state of a finding.
            - **RecordState** *(string) --*
              The record state of a finding.
            - **RelatedFindings** *(list) --*
              A list of related findings.
              - *(dict) --*
                Related finding\'s details.
                - **ProductArn** *(string) --* **[REQUIRED]**
                  The ARN of the solution that generated a related finding.
                - **Id** *(string) --* **[REQUIRED]**
                  The solution-generated identifier for a related finding.
            - **Note** *(dict) --*
              A user-defined note added to a finding.
              - **Text** *(string) --* **[REQUIRED]**
                The text of a note.
              - **UpdatedBy** *(string) --* **[REQUIRED]**
                The principal that created a note.
              - **UpdatedAt** *(string) --* **[REQUIRED]**
                The timestamp of when the note was updated.
        :rtype: dict
        :returns:
        """
        pass

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

    def create_insight(self, Name: str, Filters: Dict, GroupByAttribute: str) -> Dict:
        """
        Creates an insight, which is a consolidation of findings that identifies a security area that requires attention or intervention.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/CreateInsight>`_
        
        **Request Syntax**
        ::
          response = client.create_insight(
              Name='string',
              Filters={
                  'ProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'AwsAccountId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Id': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'GeneratorId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Type': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'FirstObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'LastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'CreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'UpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'SeverityProduct': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityNormalized': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityLabel': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Confidence': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Criticality': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Title': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Description': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RecommendationText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'SourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProductFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ProductName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'CompanyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'UserDefinedFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'MalwareName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwareType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwarePath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwareState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkDirection': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkProtocol': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourceIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourcePort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkSourceDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceMac': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkDestinationIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationPort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkDestinationDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessPath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessParentPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ProcessTerminatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorValue': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorCategory': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorLastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorSource': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorSourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourcePartition': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceRegion': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ResourceAwsEc2InstanceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV4Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV6Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceKeyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceVpcId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceSubnetId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceAwsS3BucketOwnerId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsS3BucketOwnerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyUserName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyCreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceContainerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceDetailsOther': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ComplianceStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'VerificationState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'WorkflowState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RecordState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NoteText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NoteUpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'NoteUpdatedBy': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Keyword': [
                      {
                          'Value': 'string'
                      },
                  ]
              },
              GroupByAttribute='string'
          )
        
        **Response Syntax**
        ::
            {
                'InsightArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InsightArn** *(string) --* 
              The ARN Of the created insight.
        :type Name: string
        :param Name: **[REQUIRED]**
          The user-defined name that identifies the insight that you want to create.
        :type Filters: dict
        :param Filters: **[REQUIRED]**
          A collection of attributes that are applied to all active Security Hub-aggregated findings and that result in a subset of findings that are included in this insight.
          - **ProductArn** *(list) --*
            The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) once this provider\'s product (solution that generates findings) is registered with Security Hub.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **AwsAccountId** *(list) --*
            The AWS account ID in which a finding is generated.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Id** *(list) --*
            The security findings provider-specific identifier for a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **GeneratorId** *(list) --*
            This is the identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings provider\'s solutions, this generator can be called a rule, a check, a detector, a plug-in, etc.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Type** *(list) --*
            A finding type in the format of \'namespace/category/classifier\' that classifies a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **FirstObservedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **LastObservedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **CreatedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was created by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **UpdatedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the finding record was last updated by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **SeverityProduct** *(list) --*
            The native severity as defined by the security findings provider\'s solution that generated the finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **SeverityNormalized** *(list) --*
            The normalized severity of a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **SeverityLabel** *(list) --*
            The label of a finding\'s severity.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Confidence** *(list) --*
            A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale. 0 equates zero percent confidence and 100 equates to 100 percent confidence.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **Criticality** *(list) --*
            The level of importance assigned to the resources associated with the finding. A score of 0 means the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **Title** *(list) --*
            A finding\'s title.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Description** *(list) --*
            A finding\'s description.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RecommendationText** *(list) --*
            The recommendation of what to do about the issue described in a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **SourceUrl** *(list) --*
            A URL that links to a page about the current finding in the security findings provider\'s solution.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProductFields** *(list) --*
            A data type where security findings providers can include additional solution-specific details that are not part of the defined AwsSecurityFinding format.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ProductName** *(list) --*
            The name of the solution (product) that generates findings.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **CompanyName** *(list) --*
            The name of the findings provider (company) that owns the solution (product) that generates findings.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **UserDefinedFields** *(list) --*
            A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **MalwareName** *(list) --*
            The name of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwareType** *(list) --*
            The type of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwarePath** *(list) --*
            The filesystem path of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwareState** *(list) --*
            The state of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkDirection** *(list) --*
            Indicates the direction of network traffic associated with a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkProtocol** *(list) --*
            The protocol of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkSourceIpV4** *(list) --*
            The source IPv4 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkSourceIpV6** *(list) --*
            The source IPv6 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkSourcePort** *(list) --*
            The source port of network-related information about a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **NetworkSourceDomain** *(list) --*
            The source domain of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkSourceMac** *(list) --*
            The source media access control (MAC) address of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkDestinationIpV4** *(list) --*
            The destination IPv4 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkDestinationIpV6** *(list) --*
            The destination IPv6 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkDestinationPort** *(list) --*
            The destination port of network-related information about a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **NetworkDestinationDomain** *(list) --*
            The destination domain of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessName** *(list) --*
            The name of the process.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessPath** *(list) --*
            The path to the process executable.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessPid** *(list) --*
            The process ID.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **ProcessParentPid** *(list) --*
            The parent process ID.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **ProcessLaunchedAt** *(list) --*
            The date/time that the process was launched.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ProcessTerminatedAt** *(list) --*
            The date/time that the process was terminated.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ThreatIntelIndicatorType** *(list) --*
            The type of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorValue** *(list) --*
            The value of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorCategory** *(list) --*
            The category of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorLastObservedAt** *(list) --*
            The date/time of the last observation of a threat intel indicator.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ThreatIntelIndicatorSource** *(list) --*
            The source of the threat intel.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorSourceUrl** *(list) --*
            The URL for more details from the source of the threat intel.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceType** *(list) --*
            Specifies the type of the resource for which details are provided.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceId** *(list) --*
            The canonical identifier for the given resource type.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourcePartition** *(list) --*
            The canonical AWS partition name to which the region is assigned.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceRegion** *(list) --*
            The canonical AWS external region name where this resource is located.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceTags** *(list) --*
            A list of AWS tags associated with a resource at the time the finding was processed.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ResourceAwsEc2InstanceType** *(list) --*
            The instance type of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceImageId** *(list) --*
            The Amazon Machine Image (AMI) ID of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*
            The IPv4 addresses associated with the instance.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*
            The IPv6 addresses associated with the instance.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **ResourceAwsEc2InstanceKeyName** *(list) --*
            The key name associated with the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*
            The IAM profile ARN of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceVpcId** *(list) --*
            The identifier of the VPC in which the instance was launched.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceSubnetId** *(list) --*
            The identifier of the subnet in which the instance was launched.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*
            The date/time the instance was launched.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceAwsS3BucketOwnerId** *(list) --*
            The canonical user ID of the owner of the S3 bucket.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsS3BucketOwnerName** *(list) --*
            The display name of the owner of the S3 bucket.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyUserName** *(list) --*
            The user associated with the IAM access key related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyStatus** *(list) --*
            The status of the IAM access key related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*
            The creation date/time of the IAM access key related to a finding.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceContainerName** *(list) --*
            The name of the container related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerImageId** *(list) --*
            The identifier of the image related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerImageName** *(list) --*
            The name of the image related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerLaunchedAt** *(list) --*
            The date/time that the container was started.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceDetailsOther** *(list) --*
            The details of a resource that does not have a specific sub-field for the resource type defined.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ComplianceStatus** *(list) --*
            Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard (for example, AWS CIS Foundations). Contains compliance-related finding details.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **VerificationState** *(list) --*
            Indicates the veracity of a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **WorkflowState** *(list) --*
            The workflow state of a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RecordState** *(list) --*
            The updated record state for the finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RelatedFindingsProductArn** *(list) --*
            The ARN of the solution that generated a related finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RelatedFindingsId** *(list) --*
            The solution-generated identifier for a related finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NoteText** *(list) --*
            The text of a note.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NoteUpdatedAt** *(list) --*
            The timestamp of when the note was updated.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **NoteUpdatedBy** *(list) --*
            The principal that created a note.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Keyword** *(list) --*
            A keyword for a finding.
            - *(dict) --*
              A keyword filter for querying findings.
              - **Value** *(string) --*
                A value for the keyword.
        :type GroupByAttribute: string
        :param GroupByAttribute: **[REQUIRED]**
          The attribute by which the insight\'s findings are grouped. This attribute is used as a findings aggregator for the purposes of viewing and managing multiple related findings under a single operand.
        :rtype: dict
        :returns:
        """
        pass

    def create_members(self, AccountDetails: List = None) -> Dict:
        """
        Creates member Security Hub accounts in the current AWS account (which becomes the master Security Hub account) that has Security Hub enabled.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/CreateMembers>`_
        
        **Request Syntax**
        ::
          response = client.create_members(
              AccountDetails=[
                  {
                      'AccountId': 'string',
                      'Email': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UnprocessedAccounts** *(list) --* 
              A list of account ID and email address pairs of the AWS accounts that could not be processed.
              - *(dict) --* 
                The account details that could not be processed.
                - **AccountId** *(string) --* 
                  An ID of the AWS account that could not be processed. 
                - **ProcessingResult** *(string) --* 
                  The reason for why an account could not be processed.
        :type AccountDetails: list
        :param AccountDetails:
          A list of account ID and email address pairs of the accounts that you want to associate with the master Security Hub account.
          - *(dict) --*
            The details of an AWS account.
            - **AccountId** *(string) --*
              The ID of an AWS account.
            - **Email** *(string) --*
              The email of an AWS account.
        :rtype: dict
        :returns:
        """
        pass

    def decline_invitations(self, AccountIds: List = None) -> Dict:
        """
        Declines invitations that are sent to this AWS account (invitee) by the AWS accounts (inviters) that are specified by the account IDs. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeclineInvitations>`_
        
        **Request Syntax**
        ::
          response = client.decline_invitations(
              AccountIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UnprocessedAccounts** *(list) --* 
              A list of account ID and email address pairs of the AWS accounts that could not be processed. 
              - *(dict) --* 
                The account details that could not be processed.
                - **AccountId** *(string) --* 
                  An ID of the AWS account that could not be processed. 
                - **ProcessingResult** *(string) --* 
                  The reason for why an account could not be processed.
        :type AccountIds: list
        :param AccountIds:
          A list of account IDs specifying accounts whose invitations to Security Hub you want to decline.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def delete_insight(self, InsightArn: str) -> Dict:
        """
        Deletes an insight that is specified by the insight ARN.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeleteInsight>`_
        
        **Request Syntax**
        ::
          response = client.delete_insight(
              InsightArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'InsightArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InsightArn** *(string) --* 
              The ARN of the insight that was deleted.
        :type InsightArn: string
        :param InsightArn: **[REQUIRED]**
          The ARN of the insight that you want to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_invitations(self, AccountIds: List = None) -> Dict:
        """
        Deletes invitations that are sent to this AWS account (invitee) by the AWS accounts (inviters) that are specified by their account IDs. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeleteInvitations>`_
        
        **Request Syntax**
        ::
          response = client.delete_invitations(
              AccountIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UnprocessedAccounts** *(list) --* 
              A list of account ID and email address pairs of the AWS accounts that could not be processed. 
              - *(dict) --* 
                The account details that could not be processed.
                - **AccountId** *(string) --* 
                  An ID of the AWS account that could not be processed. 
                - **ProcessingResult** *(string) --* 
                  The reason for why an account could not be processed.
        :type AccountIds: list
        :param AccountIds:
          A list of account IDs specifying accounts whose invitations to Security Hub you want to delete.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def delete_members(self, AccountIds: List = None) -> Dict:
        """
        Deletes the Security Hub member accounts that are specified by the account IDs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DeleteMembers>`_
        
        **Request Syntax**
        ::
          response = client.delete_members(
              AccountIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UnprocessedAccounts** *(list) --* 
              A list of account ID and email address pairs of the AWS accounts that could not be processed. 
              - *(dict) --* 
                The account details that could not be processed.
                - **AccountId** *(string) --* 
                  An ID of the AWS account that could not be processed. 
                - **ProcessingResult** *(string) --* 
                  The reason for why an account could not be processed.
        :type AccountIds: list
        :param AccountIds:
          A list of account IDs of the Security Hub member accounts that you want to delete.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def disable_import_findings_for_product(self, ProductSubscriptionArn: str) -> Dict:
        """
        Stops you from being able to import findings generated by integrated third-party providers into Security Hub.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DisableImportFindingsForProduct>`_
        
        **Request Syntax**
        ::
          response = client.disable_import_findings_for_product(
              ProductSubscriptionArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ProductSubscriptionArn: string
        :param ProductSubscriptionArn: **[REQUIRED]**
          The ARN of a resource that represents your subscription to a supported product.
        :rtype: dict
        :returns:
        """
        pass

    def disable_security_hub(self) -> Dict:
        """
        Disables the AWS Security Hub Service.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DisableSecurityHub>`_
        
        **Request Syntax**
        ::
          response = client.disable_security_hub()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_from_master_account(self) -> Dict:
        """
        Disassociates the current Security Hub member account from its master account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DisassociateFromMasterAccount>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_from_master_account()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_members(self, AccountIds: List = None) -> Dict:
        """
        Disassociates the Security Hub member accounts that are specified by the account IDs from their master account. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/DisassociateMembers>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_members(
              AccountIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AccountIds: list
        :param AccountIds:
          The account IDs of the member accounts that you want to disassociate from the master account.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def enable_import_findings_for_product(self, ProductArn: str) -> Dict:
        """
        Enables you to import findings generated by integrated third-party providers into Security Hub.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/EnableImportFindingsForProduct>`_
        
        **Request Syntax**
        ::
          response = client.enable_import_findings_for_product(
              ProductArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProductSubscriptionArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProductSubscriptionArn** *(string) --* 
              The ARN of a resource that represents your subscription to the product that generates the findings that you want to import into Security Hub.
        :type ProductArn: string
        :param ProductArn: **[REQUIRED]**
          The ARN of the product that generates findings that you want to import into Security Hub.
        :rtype: dict
        :returns:
        """
        pass

    def enable_security_hub(self) -> Dict:
        """
        Enables the AWS Security Hub service.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/EnableSecurityHub>`_
        
        **Request Syntax**
        ::
          response = client.enable_security_hub()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
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

    def get_enabled_standards(self, StandardsSubscriptionArns: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists and describes enabled standards.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetEnabledStandards>`_
        
        **Request Syntax**
        ::
          response = client.get_enabled_standards(
              StandardsSubscriptionArns=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'StandardsSubscriptions': [
                    {
                        'StandardsSubscriptionArn': 'string',
                        'StandardsArn': 'string',
                        'StandardsInput': {
                            'string': 'string'
                        },
                        'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **StandardsSubscriptions** *(list) --* 
              The standards subscription details returned by the operation.
              - *(dict) --* 
                A resource that represents your subscription to a supported standard.
                - **StandardsSubscriptionArn** *(string) --* 
                  The ARN of a resource that represents your subscription to a supported standard.
                - **StandardsArn** *(string) --* 
                  The ARN of a standard.
                - **StandardsInput** *(dict) --* 
                  - *(string) --* 
                    - *(string) --* 
                - **StandardsStatus** *(string) --* 
                  The standard's status.
            - **NextToken** *(string) --* 
              The token that is required for pagination.
        :type StandardsSubscriptionArns: list
        :param StandardsSubscriptionArns:
          The list of standards subscription ARNS that you want to list and describe.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          Paginates results. Set the value of this parameter to NULL on your first call to the GetEnabledStandards operation. For subsequent calls to the operation, fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
        :type MaxResults: integer
        :param MaxResults:
          Indicates the maximum number of items that you want in the response.
        :rtype: dict
        :returns:
        """
        pass

    def get_findings(self, Filters: Dict = None, SortCriteria: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists and describes Security Hub-aggregated findings that are specified by filter attributes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetFindings>`_
        
        **Request Syntax**
        ::
          response = client.get_findings(
              Filters={
                  'ProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'AwsAccountId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Id': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'GeneratorId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Type': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'FirstObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'LastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'CreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'UpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'SeverityProduct': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityNormalized': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityLabel': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Confidence': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Criticality': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Title': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Description': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RecommendationText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'SourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProductFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ProductName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'CompanyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'UserDefinedFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'MalwareName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwareType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwarePath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwareState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkDirection': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkProtocol': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourceIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourcePort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkSourceDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceMac': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkDestinationIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationPort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkDestinationDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessPath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessParentPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ProcessTerminatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorValue': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorCategory': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorLastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorSource': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorSourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourcePartition': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceRegion': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ResourceAwsEc2InstanceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV4Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV6Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceKeyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceVpcId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceSubnetId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceAwsS3BucketOwnerId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsS3BucketOwnerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyUserName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyCreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceContainerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceDetailsOther': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ComplianceStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'VerificationState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'WorkflowState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RecordState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NoteText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NoteUpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'NoteUpdatedBy': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Keyword': [
                      {
                          'Value': 'string'
                      },
                  ]
              },
              SortCriteria=[
                  {
                      'Field': 'string',
                      'SortOrder': 'asc'|'desc'
                  },
              ],
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Findings': [
                    {
                        'SchemaVersion': 'string',
                        'Id': 'string',
                        'ProductArn': 'string',
                        'GeneratorId': 'string',
                        'AwsAccountId': 'string',
                        'Types': [
                            'string',
                        ],
                        'FirstObservedAt': 'string',
                        'LastObservedAt': 'string',
                        'CreatedAt': 'string',
                        'UpdatedAt': 'string',
                        'Severity': {
                            'Product': 123.0,
                            'Normalized': 123
                        },
                        'Confidence': 123,
                        'Criticality': 123,
                        'Title': 'string',
                        'Description': 'string',
                        'Remediation': {
                            'Recommendation': {
                                'Text': 'string',
                                'Url': 'string'
                            }
                        },
                        'SourceUrl': 'string',
                        'ProductFields': {
                            'string': 'string'
                        },
                        'UserDefinedFields': {
                            'string': 'string'
                        },
                        'Malware': [
                            {
                                'Name': 'string',
                                'Type': 'ADWARE'|'BLENDED_THREAT'|'BOTNET_AGENT'|'COIN_MINER'|'EXPLOIT_KIT'|'KEYLOGGER'|'MACRO'|'POTENTIALLY_UNWANTED'|'SPYWARE'|'RANSOMWARE'|'REMOTE_ACCESS'|'ROOTKIT'|'TROJAN'|'VIRUS'|'WORM',
                                'Path': 'string',
                                'State': 'OBSERVED'|'REMOVAL_FAILED'|'REMOVED'
                            },
                        ],
                        'Network': {
                            'Direction': 'IN'|'OUT',
                            'Protocol': 'string',
                            'SourceIpV4': 'string',
                            'SourceIpV6': 'string',
                            'SourcePort': 123,
                            'SourceDomain': 'string',
                            'SourceMac': 'string',
                            'DestinationIpV4': 'string',
                            'DestinationIpV6': 'string',
                            'DestinationPort': 123,
                            'DestinationDomain': 'string'
                        },
                        'Process': {
                            'Name': 'string',
                            'Path': 'string',
                            'Pid': 123,
                            'ParentPid': 123,
                            'LaunchedAt': 'string',
                            'TerminatedAt': 'string'
                        },
                        'ThreatIntelIndicators': [
                            {
                                'Type': 'DOMAIN'|'EMAIL_ADDRESS'|'HASH_MD5'|'HASH_SHA1'|'HASH_SHA256'|'HASH_SHA512'|'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MUTEX'|'PROCESS'|'URL',
                                'Value': 'string',
                                'Category': 'BACKDOOR'|'CARD_STEALER'|'COMMAND_AND_CONTROL'|'DROP_SITE'|'EXPLOIT_SITE'|'KEYLOGGER',
                                'LastObservedAt': 'string',
                                'Source': 'string',
                                'SourceUrl': 'string'
                            },
                        ],
                        'Resources': [
                            {
                                'Type': 'string',
                                'Id': 'string',
                                'Partition': 'aws'|'aws-cn'|'aws-us-gov',
                                'Region': 'string',
                                'Tags': {
                                    'string': 'string'
                                },
                                'Details': {
                                    'AwsEc2Instance': {
                                        'Type': 'string',
                                        'ImageId': 'string',
                                        'IpV4Addresses': [
                                            'string',
                                        ],
                                        'IpV6Addresses': [
                                            'string',
                                        ],
                                        'KeyName': 'string',
                                        'IamInstanceProfileArn': 'string',
                                        'VpcId': 'string',
                                        'SubnetId': 'string',
                                        'LaunchedAt': 'string'
                                    },
                                    'AwsS3Bucket': {
                                        'OwnerId': 'string',
                                        'OwnerName': 'string'
                                    },
                                    'AwsIamAccessKey': {
                                        'UserName': 'string',
                                        'Status': 'Active'|'Inactive',
                                        'CreatedAt': 'string'
                                    },
                                    'Container': {
                                        'Name': 'string',
                                        'ImageId': 'string',
                                        'ImageName': 'string',
                                        'LaunchedAt': 'string'
                                    },
                                    'Other': {
                                        'string': 'string'
                                    }
                                }
                            },
                        ],
                        'Compliance': {
                            'Status': 'PASSED'|'WARNING'|'FAILED'|'NOT_AVAILABLE'
                        },
                        'VerificationState': 'UNKNOWN'|'TRUE_POSITIVE'|'FALSE_POSITIVE'|'BENIGN_POSITIVE',
                        'WorkflowState': 'NEW'|'ASSIGNED'|'IN_PROGRESS'|'DEFERRED'|'RESOLVED',
                        'RecordState': 'ACTIVE'|'ARCHIVED',
                        'RelatedFindings': [
                            {
                                'ProductArn': 'string',
                                'Id': 'string'
                            },
                        ],
                        'Note': {
                            'Text': 'string',
                            'UpdatedBy': 'string',
                            'UpdatedAt': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Findings** *(list) --* 
              Findings details returned by the operation.
              - *(dict) --* 
                Provides consistent format for the contents of the Security Hub-aggregated findings. AwsSecurityFinding format enables you to share findings between AWS security services and third-party solutions, and compliance checks.
                .. note::
                  A finding is a potential security issue generated either by AWS services (GuardDuty, Inspector, Macie) or by the integrated third-party solutions and compliance checks.
                - **SchemaVersion** *(string) --* 
                  The schema version for which a finding is formatted.
                - **Id** *(string) --* 
                  The security findings provider-specific identifier for a finding.
                - **ProductArn** *(string) --* 
                  The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) once this provider's product (solution that generates findings) is registered with Security Hub. 
                - **GeneratorId** *(string) --* 
                  This is the identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings provider's solutions, this generator can be called a rule, a check, a detector, a plug-in, etc. 
                - **AwsAccountId** *(string) --* 
                  The AWS account ID in which a finding is generated.
                - **Types** *(list) --* 
                  One or more finding types in the format of 'namespace/category/classifier' that classify a finding.
                  Valid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual Behaviors | Sensitive Data Identifications
                  - *(string) --* 
                - **FirstObservedAt** *(string) --* 
                  An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings provider.
                - **LastObservedAt** *(string) --* 
                  An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings provider.
                - **CreatedAt** *(string) --* 
                  An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was created by the security findings provider.
                - **UpdatedAt** *(string) --* 
                  An ISO8601-formatted timestamp that indicates when the finding record was last updated by the security findings provider. 
                - **Severity** *(dict) --* 
                  A finding's severity.
                  - **Product** *(float) --* 
                    The native severity as defined by the security findings provider's solution that generated the finding.
                  - **Normalized** *(integer) --* 
                    The normalized severity of a finding.
                - **Confidence** *(integer) --* 
                  A finding's confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale. 0 equates zero percent confidence and 100 equates to 100 percent confidence.
                - **Criticality** *(integer) --* 
                  The level of importance assigned to the resources associated with the finding. A score of 0 means the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
                - **Title** *(string) --* 
                  A finding's title.
                - **Description** *(string) --* 
                  A finding's description.
                - **Remediation** *(dict) --* 
                  An data type that describes the remediation options for a finding.
                  - **Recommendation** *(dict) --* 
                    Provides a recommendation on how to remediate the issue identified within a finding.
                    - **Text** *(string) --* 
                      The recommendation of what to do about the issue described in a finding. 
                    - **Url** *(string) --* 
                      A URL to link to general remediation information for the finding type of a finding. 
                - **SourceUrl** *(string) --* 
                  A URL that links to a page about the current finding in the security findings provider's solution.
                - **ProductFields** *(dict) --* 
                  A data type where security findings providers can include additional solution-specific details that are not part of the defined AwsSecurityFinding format.
                  - *(string) --* 
                    - *(string) --* 
                - **UserDefinedFields** *(dict) --* 
                  A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding. 
                  - *(string) --* 
                    - *(string) --* 
                - **Malware** *(list) --* 
                  A list of malware related to a finding.
                  - *(dict) --* 
                    A list of malware related to a finding.
                    - **Name** *(string) --* 
                      The name of the malware that was observed.
                    - **Type** *(string) --* 
                      The type of the malware that was observed.
                    - **Path** *(string) --* 
                      The filesystem path of the malware that was observed.
                    - **State** *(string) --* 
                      The state of the malware that was observed.
                - **Network** *(dict) --* 
                  The details of network-related information about a finding.
                  - **Direction** *(string) --* 
                    Indicates the direction of network traffic associated with a finding.
                  - **Protocol** *(string) --* 
                    The protocol of network-related information about a finding.
                  - **SourceIpV4** *(string) --* 
                    The source IPv4 address of network-related information about a finding.
                  - **SourceIpV6** *(string) --* 
                    The source IPv6 address of network-related information about a finding.
                  - **SourcePort** *(integer) --* 
                    The source port of network-related information about a finding.
                  - **SourceDomain** *(string) --* 
                    The source domain of network-related information about a finding.
                  - **SourceMac** *(string) --* 
                    The source media access control (MAC) address of network-related information about a finding.
                  - **DestinationIpV4** *(string) --* 
                    The destination IPv4 address of network-related information about a finding.
                  - **DestinationIpV6** *(string) --* 
                    The destination IPv6 address of network-related information about a finding.
                  - **DestinationPort** *(integer) --* 
                    The destination port of network-related information about a finding.
                  - **DestinationDomain** *(string) --* 
                    The destination domain of network-related information about a finding.
                - **Process** *(dict) --* 
                  The details of process-related information about a finding.
                  - **Name** *(string) --* 
                    The name of the process.
                  - **Path** *(string) --* 
                    The path to the process executable.
                  - **Pid** *(integer) --* 
                    The process ID.
                  - **ParentPid** *(integer) --* 
                    The parent process ID.
                  - **LaunchedAt** *(string) --* 
                    The date/time that the process was launched.
                  - **TerminatedAt** *(string) --* 
                    The date/time that the process was terminated.
                - **ThreatIntelIndicators** *(list) --* 
                  Threat intel details related to a finding.
                  - *(dict) --* 
                    Threat intel details related to a finding.
                    - **Type** *(string) --* 
                      The type of a threat intel indicator.
                    - **Value** *(string) --* 
                      The value of a threat intel indicator.
                    - **Category** *(string) --* 
                      The category of a threat intel indicator.
                    - **LastObservedAt** *(string) --* 
                      The date/time of the last observation of a threat intel indicator.
                    - **Source** *(string) --* 
                      The source of the threat intel.
                    - **SourceUrl** *(string) --* 
                      The URL for more details from the source of the threat intel.
                - **Resources** *(list) --* 
                  A set of resource data types that describe the resources to which the finding refers.
                  - *(dict) --* 
                    A resource data type that describes a resource to which the finding refers.
                    - **Type** *(string) --* 
                      Specifies the type of the resource for which details are provided.
                    - **Id** *(string) --* 
                      The canonical identifier for the given resource type.
                    - **Partition** *(string) --* 
                      The canonical AWS partition name to which the region is assigned.
                    - **Region** *(string) --* 
                      The canonical AWS external region name where this resource is located.
                    - **Tags** *(dict) --* 
                      A list of AWS tags associated with a resource at the time the finding was processed.
                      - *(string) --* 
                        - *(string) --* 
                    - **Details** *(dict) --* 
                      Provides additional details about the resource.
                      - **AwsEc2Instance** *(dict) --* 
                        The details of an AWS EC2 instance.
                        - **Type** *(string) --* 
                          The instance type of the instance. 
                        - **ImageId** *(string) --* 
                          The Amazon Machine Image (AMI) ID of the instance.
                        - **IpV4Addresses** *(list) --* 
                          The IPv4 addresses associated with the instance.
                          - *(string) --* 
                        - **IpV6Addresses** *(list) --* 
                          The IPv6 addresses associated with the instance.
                          - *(string) --* 
                        - **KeyName** *(string) --* 
                          The key name associated with the instance.
                        - **IamInstanceProfileArn** *(string) --* 
                          The IAM profile ARN of the instance.
                        - **VpcId** *(string) --* 
                          The identifier of the VPC in which the instance was launched.
                        - **SubnetId** *(string) --* 
                          The identifier of the subnet in which the instance was launched.
                        - **LaunchedAt** *(string) --* 
                          The date/time the instance was launched.
                      - **AwsS3Bucket** *(dict) --* 
                        The details of an AWS S3 Bucket.
                        - **OwnerId** *(string) --* 
                          The canonical user ID of the owner of the S3 bucket.
                        - **OwnerName** *(string) --* 
                          The display name of the owner of the S3 bucket.
                      - **AwsIamAccessKey** *(dict) --* 
                        AWS IAM access key details related to a finding.
                        - **UserName** *(string) --* 
                          The user associated with the IAM access key related to a finding.
                        - **Status** *(string) --* 
                          The status of the IAM access key related to a finding.
                        - **CreatedAt** *(string) --* 
                          The creation date/time of the IAM access key related to a finding.
                      - **Container** *(dict) --* 
                        Container details related to a finding.
                        - **Name** *(string) --* 
                          The name of the container related to a finding.
                        - **ImageId** *(string) --* 
                          The identifier of the image related to a finding.
                        - **ImageName** *(string) --* 
                          The name of the image related to a finding.
                        - **LaunchedAt** *(string) --* 
                          The date/time that the container was started.
                      - **Other** *(dict) --* 
                        The details of a resource that does not have a specific sub-field for the resource type defined.
                        - *(string) --* 
                          - *(string) --* 
                - **Compliance** *(dict) --* 
                  This data type is exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard (for example, AWS CIS Foundations). Contains compliance-related finding details.
                  - **Status** *(string) --* 
                    Indicates the result of a compliance check.
                - **VerificationState** *(string) --* 
                  Indicates the veracity of a finding. 
                - **WorkflowState** *(string) --* 
                  The workflow state of a finding. 
                - **RecordState** *(string) --* 
                  The record state of a finding.
                - **RelatedFindings** *(list) --* 
                  A list of related findings.
                  - *(dict) --* 
                    Related finding's details.
                    - **ProductArn** *(string) --* 
                      The ARN of the solution that generated a related finding.
                    - **Id** *(string) --* 
                      The solution-generated identifier for a related finding.
                - **Note** *(dict) --* 
                  A user-defined note added to a finding.
                  - **Text** *(string) --* 
                    The text of a note.
                  - **UpdatedBy** *(string) --* 
                    The principal that created a note.
                  - **UpdatedAt** *(string) --* 
                    The timestamp of when the note was updated.
            - **NextToken** *(string) --* 
              The token that is required for pagination.
        :type Filters: dict
        :param Filters:
          A collection of attributes that is use for querying findings.
          - **ProductArn** *(list) --*
            The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) once this provider\'s product (solution that generates findings) is registered with Security Hub.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **AwsAccountId** *(list) --*
            The AWS account ID in which a finding is generated.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Id** *(list) --*
            The security findings provider-specific identifier for a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **GeneratorId** *(list) --*
            This is the identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings provider\'s solutions, this generator can be called a rule, a check, a detector, a plug-in, etc.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Type** *(list) --*
            A finding type in the format of \'namespace/category/classifier\' that classifies a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **FirstObservedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **LastObservedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **CreatedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was created by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **UpdatedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the finding record was last updated by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **SeverityProduct** *(list) --*
            The native severity as defined by the security findings provider\'s solution that generated the finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **SeverityNormalized** *(list) --*
            The normalized severity of a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **SeverityLabel** *(list) --*
            The label of a finding\'s severity.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Confidence** *(list) --*
            A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale. 0 equates zero percent confidence and 100 equates to 100 percent confidence.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **Criticality** *(list) --*
            The level of importance assigned to the resources associated with the finding. A score of 0 means the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **Title** *(list) --*
            A finding\'s title.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Description** *(list) --*
            A finding\'s description.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RecommendationText** *(list) --*
            The recommendation of what to do about the issue described in a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **SourceUrl** *(list) --*
            A URL that links to a page about the current finding in the security findings provider\'s solution.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProductFields** *(list) --*
            A data type where security findings providers can include additional solution-specific details that are not part of the defined AwsSecurityFinding format.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ProductName** *(list) --*
            The name of the solution (product) that generates findings.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **CompanyName** *(list) --*
            The name of the findings provider (company) that owns the solution (product) that generates findings.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **UserDefinedFields** *(list) --*
            A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **MalwareName** *(list) --*
            The name of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwareType** *(list) --*
            The type of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwarePath** *(list) --*
            The filesystem path of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwareState** *(list) --*
            The state of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkDirection** *(list) --*
            Indicates the direction of network traffic associated with a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkProtocol** *(list) --*
            The protocol of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkSourceIpV4** *(list) --*
            The source IPv4 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkSourceIpV6** *(list) --*
            The source IPv6 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkSourcePort** *(list) --*
            The source port of network-related information about a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **NetworkSourceDomain** *(list) --*
            The source domain of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkSourceMac** *(list) --*
            The source media access control (MAC) address of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkDestinationIpV4** *(list) --*
            The destination IPv4 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkDestinationIpV6** *(list) --*
            The destination IPv6 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkDestinationPort** *(list) --*
            The destination port of network-related information about a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **NetworkDestinationDomain** *(list) --*
            The destination domain of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessName** *(list) --*
            The name of the process.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessPath** *(list) --*
            The path to the process executable.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessPid** *(list) --*
            The process ID.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **ProcessParentPid** *(list) --*
            The parent process ID.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **ProcessLaunchedAt** *(list) --*
            The date/time that the process was launched.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ProcessTerminatedAt** *(list) --*
            The date/time that the process was terminated.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ThreatIntelIndicatorType** *(list) --*
            The type of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorValue** *(list) --*
            The value of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorCategory** *(list) --*
            The category of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorLastObservedAt** *(list) --*
            The date/time of the last observation of a threat intel indicator.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ThreatIntelIndicatorSource** *(list) --*
            The source of the threat intel.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorSourceUrl** *(list) --*
            The URL for more details from the source of the threat intel.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceType** *(list) --*
            Specifies the type of the resource for which details are provided.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceId** *(list) --*
            The canonical identifier for the given resource type.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourcePartition** *(list) --*
            The canonical AWS partition name to which the region is assigned.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceRegion** *(list) --*
            The canonical AWS external region name where this resource is located.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceTags** *(list) --*
            A list of AWS tags associated with a resource at the time the finding was processed.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ResourceAwsEc2InstanceType** *(list) --*
            The instance type of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceImageId** *(list) --*
            The Amazon Machine Image (AMI) ID of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*
            The IPv4 addresses associated with the instance.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*
            The IPv6 addresses associated with the instance.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **ResourceAwsEc2InstanceKeyName** *(list) --*
            The key name associated with the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*
            The IAM profile ARN of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceVpcId** *(list) --*
            The identifier of the VPC in which the instance was launched.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceSubnetId** *(list) --*
            The identifier of the subnet in which the instance was launched.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*
            The date/time the instance was launched.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceAwsS3BucketOwnerId** *(list) --*
            The canonical user ID of the owner of the S3 bucket.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsS3BucketOwnerName** *(list) --*
            The display name of the owner of the S3 bucket.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyUserName** *(list) --*
            The user associated with the IAM access key related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyStatus** *(list) --*
            The status of the IAM access key related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*
            The creation date/time of the IAM access key related to a finding.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceContainerName** *(list) --*
            The name of the container related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerImageId** *(list) --*
            The identifier of the image related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerImageName** *(list) --*
            The name of the image related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerLaunchedAt** *(list) --*
            The date/time that the container was started.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceDetailsOther** *(list) --*
            The details of a resource that does not have a specific sub-field for the resource type defined.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ComplianceStatus** *(list) --*
            Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard (for example, AWS CIS Foundations). Contains compliance-related finding details.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **VerificationState** *(list) --*
            Indicates the veracity of a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **WorkflowState** *(list) --*
            The workflow state of a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RecordState** *(list) --*
            The updated record state for the finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RelatedFindingsProductArn** *(list) --*
            The ARN of the solution that generated a related finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RelatedFindingsId** *(list) --*
            The solution-generated identifier for a related finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NoteText** *(list) --*
            The text of a note.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NoteUpdatedAt** *(list) --*
            The timestamp of when the note was updated.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **NoteUpdatedBy** *(list) --*
            The principal that created a note.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Keyword** *(list) --*
            A keyword for a finding.
            - *(dict) --*
              A keyword filter for querying findings.
              - **Value** *(string) --*
                A value for the keyword.
        :type SortCriteria: list
        :param SortCriteria:
          A collection of attributes used for sorting findings.
          - *(dict) --*
            A collection of attributes used for sorting findings.
            - **Field** *(string) --*
              The finding attribute used for sorting findings.
            - **SortOrder** *(string) --*
              The order used for sorting findings.
        :type NextToken: string
        :param NextToken:
          Paginates results. Set the value of this parameter to NULL on your first call to the GetFindings operation. For subsequent calls to the operation, fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
        :type MaxResults: integer
        :param MaxResults:
          Indicates the maximum number of items that you want in the response.
        :rtype: dict
        :returns:
        """
        pass

    def get_insight_results(self, InsightArn: str) -> Dict:
        """
        Lists the results of the Security Hub insight specified by the insight ARN.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetInsightResults>`_
        
        **Request Syntax**
        ::
          response = client.get_insight_results(
              InsightArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'InsightResults': {
                    'InsightArn': 'string',
                    'GroupByAttribute': 'string',
                    'ResultValues': [
                        {
                            'GroupByAttributeValue': 'string',
                            'Count': 123
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InsightResults** *(dict) --* 
              The insight results returned by the operation.
              - **InsightArn** *(string) --* 
                The ARN of the insight whose results are returned by the GetInsightResults operation.
              - **GroupByAttribute** *(string) --* 
                The attribute by which the findings are grouped for the insight's whose results are returned by the GetInsightResults operation.
              - **ResultValues** *(list) --* 
                The list of insight result values returned by the GetInsightResults operation.
                - *(dict) --* 
                  The insight result values returned by the GetInsightResults operation.
                  - **GroupByAttributeValue** *(string) --* 
                    The value of the attribute by which the findings are grouped for the insight's whose results are returned by the GetInsightResults operation.
                  - **Count** *(integer) --* 
                    The number of findings returned for each GroupByAttributeValue.
        :type InsightArn: string
        :param InsightArn: **[REQUIRED]**
          The ARN of the insight whose results you want to see.
        :rtype: dict
        :returns:
        """
        pass

    def get_insights(self, InsightArns: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists and describes insights that are specified by insight ARNs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetInsights>`_
        
        **Request Syntax**
        ::
          response = client.get_insights(
              InsightArns=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Insights': [
                    {
                        'InsightArn': 'string',
                        'Name': 'string',
                        'Filters': {
                            'ProductArn': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'AwsAccountId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'Id': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'GeneratorId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'Type': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'FirstObservedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'LastObservedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'CreatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'UpdatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'SeverityProduct': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'SeverityNormalized': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'SeverityLabel': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'Confidence': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'Criticality': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'Title': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'Description': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'RecommendationText': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'SourceUrl': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ProductFields': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Comparison': 'CONTAINS'
                                },
                            ],
                            'ProductName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'CompanyName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'UserDefinedFields': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Comparison': 'CONTAINS'
                                },
                            ],
                            'MalwareName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'MalwareType': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'MalwarePath': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'MalwareState': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'NetworkDirection': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'NetworkProtocol': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'NetworkSourceIpV4': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'NetworkSourceIpV6': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'NetworkSourcePort': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'NetworkSourceDomain': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'NetworkSourceMac': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'NetworkDestinationIpV4': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'NetworkDestinationIpV6': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'NetworkDestinationPort': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'NetworkDestinationDomain': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ProcessName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ProcessPath': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ProcessPid': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'ProcessParentPid': [
                                {
                                    'Gte': 123.0,
                                    'Lte': 123.0,
                                    'Eq': 123.0
                                },
                            ],
                            'ProcessLaunchedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ProcessTerminatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ThreatIntelIndicatorType': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ThreatIntelIndicatorValue': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ThreatIntelIndicatorCategory': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ThreatIntelIndicatorLastObservedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ThreatIntelIndicatorSource': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ThreatIntelIndicatorSourceUrl': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceType': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourcePartition': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceRegion': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceTags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Comparison': 'CONTAINS'
                                },
                            ],
                            'ResourceAwsEc2InstanceType': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceImageId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceIpV4Addresses': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'ResourceAwsEc2InstanceIpV6Addresses': [
                                {
                                    'Cidr': 'string'
                                },
                            ],
                            'ResourceAwsEc2InstanceKeyName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceVpcId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceSubnetId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsEc2InstanceLaunchedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ResourceAwsS3BucketOwnerId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsS3BucketOwnerName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsIamAccessKeyUserName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsIamAccessKeyStatus': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceAwsIamAccessKeyCreatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ResourceContainerName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceContainerImageId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceContainerImageName': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'ResourceContainerLaunchedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'ResourceDetailsOther': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Comparison': 'CONTAINS'
                                },
                            ],
                            'ComplianceStatus': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'VerificationState': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'WorkflowState': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'RecordState': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'RelatedFindingsProductArn': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'RelatedFindingsId': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'NoteText': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'NoteUpdatedAt': [
                                {
                                    'Start': 'string',
                                    'End': 'string',
                                    'DateRange': {
                                        'Value': 123,
                                        'Unit': 'DAYS'
                                    }
                                },
                            ],
                            'NoteUpdatedBy': [
                                {
                                    'Value': 'string',
                                    'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                                },
                            ],
                            'Keyword': [
                                {
                                    'Value': 'string'
                                },
                            ]
                        },
                        'GroupByAttribute': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Insights** *(list) --* 
              The insights returned by the operation.
              - *(dict) --* 
                Contains information about a Security Hub insight. 
                - **InsightArn** *(string) --* 
                  The ARN of a Security Hub insight.
                - **Name** *(string) --* 
                  The name of a Security Hub insight.
                - **Filters** *(dict) --* 
                  A collection of attributes that are applied to all active Security Hub-aggregated findings and that result in a subset of findings that are included in this insight. 
                  - **ProductArn** *(list) --* 
                    The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) once this provider's product (solution that generates findings) is registered with Security Hub.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **AwsAccountId** *(list) --* 
                    The AWS account ID in which a finding is generated.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **Id** *(list) --* 
                    The security findings provider-specific identifier for a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **GeneratorId** *(list) --* 
                    This is the identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings provider's solutions, this generator can be called a rule, a check, a detector, a plug-in, etc.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **Type** *(list) --* 
                    A finding type in the format of 'namespace/category/classifier' that classifies a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **FirstObservedAt** *(list) --* 
                    An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings provider.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **LastObservedAt** *(list) --* 
                    An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings provider.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **CreatedAt** *(list) --* 
                    An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was created by the security findings provider.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **UpdatedAt** *(list) --* 
                    An ISO8601-formatted timestamp that indicates when the finding record was last updated by the security findings provider. 
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **SeverityProduct** *(list) --* 
                    The native severity as defined by the security findings provider's solution that generated the finding.
                    - *(dict) --* 
                      A number filter for querying findings.
                      - **Gte** *(float) --* 
                        Represents the "greater than equal" condition to be applied to a single field when querying for findings. 
                      - **Lte** *(float) --* 
                        Represents the "less than equal" condition to be applied to a single field when querying for findings. 
                      - **Eq** *(float) --* 
                        Represents the "equal to" condition to be applied to a single field when querying for findings.
                  - **SeverityNormalized** *(list) --* 
                    The normalized severity of a finding.
                    - *(dict) --* 
                      A number filter for querying findings.
                      - **Gte** *(float) --* 
                        Represents the "greater than equal" condition to be applied to a single field when querying for findings. 
                      - **Lte** *(float) --* 
                        Represents the "less than equal" condition to be applied to a single field when querying for findings. 
                      - **Eq** *(float) --* 
                        Represents the "equal to" condition to be applied to a single field when querying for findings.
                  - **SeverityLabel** *(list) --* 
                    The label of a finding's severity.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **Confidence** *(list) --* 
                    A finding's confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale. 0 equates zero percent confidence and 100 equates to 100 percent confidence.
                    - *(dict) --* 
                      A number filter for querying findings.
                      - **Gte** *(float) --* 
                        Represents the "greater than equal" condition to be applied to a single field when querying for findings. 
                      - **Lte** *(float) --* 
                        Represents the "less than equal" condition to be applied to a single field when querying for findings. 
                      - **Eq** *(float) --* 
                        Represents the "equal to" condition to be applied to a single field when querying for findings.
                  - **Criticality** *(list) --* 
                    The level of importance assigned to the resources associated with the finding. A score of 0 means the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
                    - *(dict) --* 
                      A number filter for querying findings.
                      - **Gte** *(float) --* 
                        Represents the "greater than equal" condition to be applied to a single field when querying for findings. 
                      - **Lte** *(float) --* 
                        Represents the "less than equal" condition to be applied to a single field when querying for findings. 
                      - **Eq** *(float) --* 
                        Represents the "equal to" condition to be applied to a single field when querying for findings.
                  - **Title** *(list) --* 
                    A finding's title.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **Description** *(list) --* 
                    A finding's description.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **RecommendationText** *(list) --* 
                    The recommendation of what to do about the issue described in a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **SourceUrl** *(list) --* 
                    A URL that links to a page about the current finding in the security findings provider's solution.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ProductFields** *(list) --* 
                    A data type where security findings providers can include additional solution-specific details that are not part of the defined AwsSecurityFinding format.
                    - *(dict) --* 
                      The map filter for querying findings.
                      - **Key** *(string) --* 
                        The key of the map filter.
                      - **Value** *(string) --* 
                        The value for the key in the map filter.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a key value when querying for findings with a map filter.
                  - **ProductName** *(list) --* 
                    The name of the solution (product) that generates findings.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **CompanyName** *(list) --* 
                    The name of the findings provider (company) that owns the solution (product) that generates findings.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **UserDefinedFields** *(list) --* 
                    A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding. 
                    - *(dict) --* 
                      The map filter for querying findings.
                      - **Key** *(string) --* 
                        The key of the map filter.
                      - **Value** *(string) --* 
                        The value for the key in the map filter.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a key value when querying for findings with a map filter.
                  - **MalwareName** *(list) --* 
                    The name of the malware that was observed.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **MalwareType** *(list) --* 
                    The type of the malware that was observed.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **MalwarePath** *(list) --* 
                    The filesystem path of the malware that was observed.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **MalwareState** *(list) --* 
                    The state of the malware that was observed.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **NetworkDirection** *(list) --* 
                    Indicates the direction of network traffic associated with a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **NetworkProtocol** *(list) --* 
                    The protocol of network-related information about a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **NetworkSourceIpV4** *(list) --* 
                    The source IPv4 address of network-related information about a finding.
                    - *(dict) --* 
                      The IP filter for querying findings.>
                      - **Cidr** *(string) --* 
                        Finding's CIDR value.
                  - **NetworkSourceIpV6** *(list) --* 
                    The source IPv6 address of network-related information about a finding.
                    - *(dict) --* 
                      The IP filter for querying findings.>
                      - **Cidr** *(string) --* 
                        Finding's CIDR value.
                  - **NetworkSourcePort** *(list) --* 
                    The source port of network-related information about a finding.
                    - *(dict) --* 
                      A number filter for querying findings.
                      - **Gte** *(float) --* 
                        Represents the "greater than equal" condition to be applied to a single field when querying for findings. 
                      - **Lte** *(float) --* 
                        Represents the "less than equal" condition to be applied to a single field when querying for findings. 
                      - **Eq** *(float) --* 
                        Represents the "equal to" condition to be applied to a single field when querying for findings.
                  - **NetworkSourceDomain** *(list) --* 
                    The source domain of network-related information about a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **NetworkSourceMac** *(list) --* 
                    The source media access control (MAC) address of network-related information about a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **NetworkDestinationIpV4** *(list) --* 
                    The destination IPv4 address of network-related information about a finding.
                    - *(dict) --* 
                      The IP filter for querying findings.>
                      - **Cidr** *(string) --* 
                        Finding's CIDR value.
                  - **NetworkDestinationIpV6** *(list) --* 
                    The destination IPv6 address of network-related information about a finding.
                    - *(dict) --* 
                      The IP filter for querying findings.>
                      - **Cidr** *(string) --* 
                        Finding's CIDR value.
                  - **NetworkDestinationPort** *(list) --* 
                    The destination port of network-related information about a finding.
                    - *(dict) --* 
                      A number filter for querying findings.
                      - **Gte** *(float) --* 
                        Represents the "greater than equal" condition to be applied to a single field when querying for findings. 
                      - **Lte** *(float) --* 
                        Represents the "less than equal" condition to be applied to a single field when querying for findings. 
                      - **Eq** *(float) --* 
                        Represents the "equal to" condition to be applied to a single field when querying for findings.
                  - **NetworkDestinationDomain** *(list) --* 
                    The destination domain of network-related information about a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ProcessName** *(list) --* 
                    The name of the process.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ProcessPath** *(list) --* 
                    The path to the process executable.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ProcessPid** *(list) --* 
                    The process ID.
                    - *(dict) --* 
                      A number filter for querying findings.
                      - **Gte** *(float) --* 
                        Represents the "greater than equal" condition to be applied to a single field when querying for findings. 
                      - **Lte** *(float) --* 
                        Represents the "less than equal" condition to be applied to a single field when querying for findings. 
                      - **Eq** *(float) --* 
                        Represents the "equal to" condition to be applied to a single field when querying for findings.
                  - **ProcessParentPid** *(list) --* 
                    The parent process ID.
                    - *(dict) --* 
                      A number filter for querying findings.
                      - **Gte** *(float) --* 
                        Represents the "greater than equal" condition to be applied to a single field when querying for findings. 
                      - **Lte** *(float) --* 
                        Represents the "less than equal" condition to be applied to a single field when querying for findings. 
                      - **Eq** *(float) --* 
                        Represents the "equal to" condition to be applied to a single field when querying for findings.
                  - **ProcessLaunchedAt** *(list) --* 
                    The date/time that the process was launched.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **ProcessTerminatedAt** *(list) --* 
                    The date/time that the process was terminated.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **ThreatIntelIndicatorType** *(list) --* 
                    The type of a threat intel indicator.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ThreatIntelIndicatorValue** *(list) --* 
                    The value of a threat intel indicator.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ThreatIntelIndicatorCategory** *(list) --* 
                    The category of a threat intel indicator.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ThreatIntelIndicatorLastObservedAt** *(list) --* 
                    The date/time of the last observation of a threat intel indicator.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **ThreatIntelIndicatorSource** *(list) --* 
                    The source of the threat intel.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ThreatIntelIndicatorSourceUrl** *(list) --* 
                    The URL for more details from the source of the threat intel.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceType** *(list) --* 
                    Specifies the type of the resource for which details are provided.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceId** *(list) --* 
                    The canonical identifier for the given resource type.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourcePartition** *(list) --* 
                    The canonical AWS partition name to which the region is assigned.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceRegion** *(list) --* 
                    The canonical AWS external region name where this resource is located.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceTags** *(list) --* 
                    A list of AWS tags associated with a resource at the time the finding was processed.
                    - *(dict) --* 
                      The map filter for querying findings.
                      - **Key** *(string) --* 
                        The key of the map filter.
                      - **Value** *(string) --* 
                        The value for the key in the map filter.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a key value when querying for findings with a map filter.
                  - **ResourceAwsEc2InstanceType** *(list) --* 
                    The instance type of the instance.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsEc2InstanceImageId** *(list) --* 
                    The Amazon Machine Image (AMI) ID of the instance.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --* 
                    The IPv4 addresses associated with the instance.
                    - *(dict) --* 
                      The IP filter for querying findings.>
                      - **Cidr** *(string) --* 
                        Finding's CIDR value.
                  - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --* 
                    The IPv6 addresses associated with the instance.
                    - *(dict) --* 
                      The IP filter for querying findings.>
                      - **Cidr** *(string) --* 
                        Finding's CIDR value.
                  - **ResourceAwsEc2InstanceKeyName** *(list) --* 
                    The key name associated with the instance.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --* 
                    The IAM profile ARN of the instance.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsEc2InstanceVpcId** *(list) --* 
                    The identifier of the VPC in which the instance was launched.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsEc2InstanceSubnetId** *(list) --* 
                    The identifier of the subnet in which the instance was launched.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsEc2InstanceLaunchedAt** *(list) --* 
                    The date/time the instance was launched.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **ResourceAwsS3BucketOwnerId** *(list) --* 
                    The canonical user ID of the owner of the S3 bucket.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsS3BucketOwnerName** *(list) --* 
                    The display name of the owner of the S3 bucket.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsIamAccessKeyUserName** *(list) --* 
                    The user associated with the IAM access key related to a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsIamAccessKeyStatus** *(list) --* 
                    The status of the IAM access key related to a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceAwsIamAccessKeyCreatedAt** *(list) --* 
                    The creation date/time of the IAM access key related to a finding.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **ResourceContainerName** *(list) --* 
                    The name of the container related to a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceContainerImageId** *(list) --* 
                    The identifier of the image related to a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceContainerImageName** *(list) --* 
                    The name of the image related to a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **ResourceContainerLaunchedAt** *(list) --* 
                    The date/time that the container was started.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **ResourceDetailsOther** *(list) --* 
                    The details of a resource that does not have a specific sub-field for the resource type defined.
                    - *(dict) --* 
                      The map filter for querying findings.
                      - **Key** *(string) --* 
                        The key of the map filter.
                      - **Value** *(string) --* 
                        The value for the key in the map filter.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a key value when querying for findings with a map filter.
                  - **ComplianceStatus** *(list) --* 
                    Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard (for example, AWS CIS Foundations). Contains compliance-related finding details.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **VerificationState** *(list) --* 
                    Indicates the veracity of a finding. 
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **WorkflowState** *(list) --* 
                    The workflow state of a finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **RecordState** *(list) --* 
                    The updated record state for the finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **RelatedFindingsProductArn** *(list) --* 
                    The ARN of the solution that generated a related finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **RelatedFindingsId** *(list) --* 
                    The solution-generated identifier for a related finding.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **NoteText** *(list) --* 
                    The text of a note.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **NoteUpdatedAt** *(list) --* 
                    The timestamp of when the note was updated.
                    - *(dict) --* 
                      A date filter for querying findings.
                      - **Start** *(string) --* 
                        A start date for the date filter.
                      - **End** *(string) --* 
                        An end date for the date filter.
                      - **DateRange** *(dict) --* 
                        A date range for the date filter.
                        - **Value** *(integer) --* 
                          A date range value for the date filter.
                        - **Unit** *(string) --* 
                          A date range unit for the date filter.
                  - **NoteUpdatedBy** *(list) --* 
                    The principal that created a note.
                    - *(dict) --* 
                      A string filter for querying findings.
                      - **Value** *(string) --* 
                        The string filter value.
                      - **Comparison** *(string) --* 
                        Represents the condition to be applied to a string value when querying for findings. 
                  - **Keyword** *(list) --* 
                    A keyword for a finding.
                    - *(dict) --* 
                      A keyword filter for querying findings.
                      - **Value** *(string) --* 
                        A value for the keyword.
                - **GroupByAttribute** *(string) --* 
                  The attribute by which the insight's findings are grouped. This attribute is used as a findings aggregator for the purposes of viewing and managing multiple related findings under a single operand.
            - **NextToken** *(string) --* 
              The token that is required for pagination.
        :type InsightArns: list
        :param InsightArns:
          The ARNS of the insights that you want to describe.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          Paginates results. Set the value of this parameter to NULL on your first call to the GetInsights operation. For subsequent calls to the operation, fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
        :type MaxResults: integer
        :param MaxResults:
          Indicates the maximum number of items that you want in the response.
        :rtype: dict
        :returns:
        """
        pass

    def get_invitations_count(self) -> Dict:
        """
        Returns the count of all Security Hub membership invitations that were sent to the current member account, not including the currently accepted invitation. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetInvitationsCount>`_
        
        **Request Syntax**
        ::
          response = client.get_invitations_count()
        
        **Response Syntax**
        ::
            {
                'InvitationsCount': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InvitationsCount** *(integer) --* 
              The number of all membership invitations sent to this Security Hub member account, not including the currently accepted invitation. 
        :rtype: dict
        :returns:
        """
        pass

    def get_master_account(self) -> Dict:
        """
        Provides the details for the Security Hub master account to the current member account. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetMasterAccount>`_
        
        **Request Syntax**
        ::
          response = client.get_master_account()
        
        **Response Syntax**
        ::
            {
                'Master': {
                    'AccountId': 'string',
                    'InvitationId': 'string',
                    'InvitedAt': datetime(2015, 1, 1),
                    'MemberStatus': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Master** *(dict) --* 
              A list of details about the Security Hub master account for the current member account. 
              - **AccountId** *(string) --* 
                The account ID of the master Security Hub account who sent the invitation. 
              - **InvitationId** *(string) --* 
                The ID of the invitation sent by the master Security Hub account.
              - **InvitedAt** *(datetime) --* 
                The timestamp of when the invitation was sent.
              - **MemberStatus** *(string) --* 
                The current relationship status between the inviter and invitee accounts.
        :rtype: dict
        :returns:
        """
        pass

    def get_members(self, AccountIds: List) -> Dict:
        """
        Returns the details on the Security Hub member accounts that are specified by the account IDs. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetMembers>`_
        
        **Request Syntax**
        ::
          response = client.get_members(
              AccountIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'Members': [
                    {
                        'AccountId': 'string',
                        'Email': 'string',
                        'MasterId': 'string',
                        'MemberStatus': 'string',
                        'InvitedAt': datetime(2015, 1, 1),
                        'UpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Members** *(list) --* 
              A list of details about the Security Hub member accounts.
              - *(dict) --* 
                The details for a Security Hub member account.
                - **AccountId** *(string) --* 
                  The AWS account ID of a Security Hub member account.
                - **Email** *(string) --* 
                  The email of a Security Hub member account.
                - **MasterId** *(string) --* 
                  The AWS account ID of the master Security Hub account to this member account.
                - **MemberStatus** *(string) --* 
                  The status of the relationship between the member account and its master account. 
                - **InvitedAt** *(datetime) --* 
                  Time stamp at which the member account was invited to Security Hub.
                - **UpdatedAt** *(datetime) --* 
                  Time stamp at which this member account was updated.
            - **UnprocessedAccounts** *(list) --* 
              A list of account ID and email address pairs of the AWS accounts that could not be processed.
              - *(dict) --* 
                The account details that could not be processed.
                - **AccountId** *(string) --* 
                  An ID of the AWS account that could not be processed. 
                - **ProcessingResult** *(string) --* 
                  The reason for why an account could not be processed.
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]**
          A list of account IDs for the Security Hub member accounts on which you want to return the details.
          - *(string) --*
        :rtype: dict
        :returns:
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

    def invite_members(self, AccountIds: List = None) -> Dict:
        """
        Invites other AWS accounts to enable Security Hub and become Security Hub member accounts. When an account accepts the invitation and becomes a member account, the master account can view Security Hub findings of the member account. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/InviteMembers>`_
        
        **Request Syntax**
        ::
          response = client.invite_members(
              AccountIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'UnprocessedAccounts': [
                    {
                        'AccountId': 'string',
                        'ProcessingResult': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UnprocessedAccounts** *(list) --* 
              A list of account ID and email address pairs of the AWS accounts that could not be processed. 
              - *(dict) --* 
                The account details that could not be processed.
                - **AccountId** *(string) --* 
                  An ID of the AWS account that could not be processed. 
                - **ProcessingResult** *(string) --* 
                  The reason for why an account could not be processed.
        :type AccountIds: list
        :param AccountIds:
          A list of IDs of the AWS accounts that you want to invite to Security Hub as members.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_enabled_products_for_import(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists all Security Hub-integrated third-party findings providers.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListEnabledProductsForImport>`_
        
        **Request Syntax**
        ::
          response = client.list_enabled_products_for_import(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'ProductSubscriptions': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProductSubscriptions** *(list) --* 
              A list of ARNs for the resources that represent your subscriptions to products. 
              - *(string) --* 
            - **NextToken** *(string) --* 
              The token that is required for pagination.
        :type NextToken: string
        :param NextToken:
          Paginates results. Set the value of this parameter to NULL on your first call to the ListEnabledProductsForImport operation. For subsequent calls to the operation, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        :type MaxResults: integer
        :param MaxResults:
          Indicates the maximum number of items that you want in the response.
        :rtype: dict
        :returns:
        """
        pass

    def list_invitations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Lists all Security Hub membership invitations that were sent to the current AWS account. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListInvitations>`_
        
        **Request Syntax**
        ::
          response = client.list_invitations(
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Invitations': [
                    {
                        'AccountId': 'string',
                        'InvitationId': 'string',
                        'InvitedAt': datetime(2015, 1, 1),
                        'MemberStatus': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Invitations** *(list) --* 
              The details of the invitations returned by the operation.
              - *(dict) --* 
                The details of an invitation sent to an AWS account by the Security Hub master account. 
                - **AccountId** *(string) --* 
                  The account ID of the master Security Hub account who sent the invitation. 
                - **InvitationId** *(string) --* 
                  The ID of the invitation sent by the master Security Hub account.
                - **InvitedAt** *(datetime) --* 
                  The timestamp of when the invitation was sent.
                - **MemberStatus** *(string) --* 
                  The current relationship status between the inviter and invitee accounts.
            - **NextToken** *(string) --* 
              The token that is required for pagination.
        :type MaxResults: integer
        :param MaxResults:
          Indicates the maximum number of items that you want in the response.
        :type NextToken: string
        :param NextToken:
          Paginates results. Set the value of this parameter to NULL on your first call to the ListInvitations operation. For subsequent calls to the operation, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        :rtype: dict
        :returns:
        """
        pass

    def list_members(self, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Lists details about all member accounts for the current Security Hub master account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListMembers>`_
        
        **Request Syntax**
        ::
          response = client.list_members(
              OnlyAssociated=True|False,
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Members': [
                    {
                        'AccountId': 'string',
                        'Email': 'string',
                        'MasterId': 'string',
                        'MemberStatus': 'string',
                        'InvitedAt': datetime(2015, 1, 1),
                        'UpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Members** *(list) --* 
              Member details returned by the operation.
              - *(dict) --* 
                The details for a Security Hub member account.
                - **AccountId** *(string) --* 
                  The AWS account ID of a Security Hub member account.
                - **Email** *(string) --* 
                  The email of a Security Hub member account.
                - **MasterId** *(string) --* 
                  The AWS account ID of the master Security Hub account to this member account.
                - **MemberStatus** *(string) --* 
                  The status of the relationship between the member account and its master account. 
                - **InvitedAt** *(datetime) --* 
                  Time stamp at which the member account was invited to Security Hub.
                - **UpdatedAt** *(datetime) --* 
                  Time stamp at which this member account was updated.
            - **NextToken** *(string) --* 
              The token that is required for pagination.
        :type OnlyAssociated: boolean
        :param OnlyAssociated:
          Specifies what member accounts the response includes based on their relationship status with the master account. The default value is TRUE. If onlyAssociated is set to TRUE, the response includes member accounts whose relationship status with the master is set to ENABLED or DISABLED. If onlyAssociated is set to FALSE, the response includes all existing member accounts.
        :type MaxResults: integer
        :param MaxResults:
          Indicates the maximum number of items that you want in the response.
        :type NextToken: string
        :param NextToken:
          Paginates results. Set the value of this parameter to NULL on your first call to the ListMembers operation. For subsequent calls to the operation, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        :rtype: dict
        :returns:
        """
        pass

    def update_findings(self, Filters: Dict, Note: Dict = None, RecordState: str = None) -> Dict:
        """
        Updates the AWS Security Hub-aggregated findings specified by the filter attributes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/UpdateFindings>`_
        
        **Request Syntax**
        ::
          response = client.update_findings(
              Filters={
                  'ProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'AwsAccountId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Id': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'GeneratorId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Type': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'FirstObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'LastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'CreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'UpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'SeverityProduct': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityNormalized': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityLabel': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Confidence': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Criticality': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Title': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Description': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RecommendationText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'SourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProductFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ProductName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'CompanyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'UserDefinedFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'MalwareName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwareType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwarePath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwareState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkDirection': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkProtocol': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourceIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourcePort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkSourceDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceMac': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkDestinationIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationPort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkDestinationDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessPath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessParentPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ProcessTerminatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorValue': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorCategory': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorLastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorSource': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorSourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourcePartition': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceRegion': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ResourceAwsEc2InstanceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV4Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV6Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceKeyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceVpcId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceSubnetId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceAwsS3BucketOwnerId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsS3BucketOwnerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyUserName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyCreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceContainerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceDetailsOther': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ComplianceStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'VerificationState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'WorkflowState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RecordState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NoteText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NoteUpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'NoteUpdatedBy': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Keyword': [
                      {
                          'Value': 'string'
                      },
                  ]
              },
              Note={
                  'Text': 'string',
                  'UpdatedBy': 'string'
              },
              RecordState='ACTIVE'|'ARCHIVED'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type Filters: dict
        :param Filters: **[REQUIRED]**
          A collection of attributes that specify what findings you want to update.
          - **ProductArn** *(list) --*
            The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) once this provider\'s product (solution that generates findings) is registered with Security Hub.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **AwsAccountId** *(list) --*
            The AWS account ID in which a finding is generated.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Id** *(list) --*
            The security findings provider-specific identifier for a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **GeneratorId** *(list) --*
            This is the identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings provider\'s solutions, this generator can be called a rule, a check, a detector, a plug-in, etc.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Type** *(list) --*
            A finding type in the format of \'namespace/category/classifier\' that classifies a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **FirstObservedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **LastObservedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **CreatedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was created by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **UpdatedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the finding record was last updated by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **SeverityProduct** *(list) --*
            The native severity as defined by the security findings provider\'s solution that generated the finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **SeverityNormalized** *(list) --*
            The normalized severity of a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **SeverityLabel** *(list) --*
            The label of a finding\'s severity.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Confidence** *(list) --*
            A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale. 0 equates zero percent confidence and 100 equates to 100 percent confidence.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **Criticality** *(list) --*
            The level of importance assigned to the resources associated with the finding. A score of 0 means the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **Title** *(list) --*
            A finding\'s title.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Description** *(list) --*
            A finding\'s description.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RecommendationText** *(list) --*
            The recommendation of what to do about the issue described in a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **SourceUrl** *(list) --*
            A URL that links to a page about the current finding in the security findings provider\'s solution.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProductFields** *(list) --*
            A data type where security findings providers can include additional solution-specific details that are not part of the defined AwsSecurityFinding format.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ProductName** *(list) --*
            The name of the solution (product) that generates findings.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **CompanyName** *(list) --*
            The name of the findings provider (company) that owns the solution (product) that generates findings.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **UserDefinedFields** *(list) --*
            A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **MalwareName** *(list) --*
            The name of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwareType** *(list) --*
            The type of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwarePath** *(list) --*
            The filesystem path of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwareState** *(list) --*
            The state of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkDirection** *(list) --*
            Indicates the direction of network traffic associated with a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkProtocol** *(list) --*
            The protocol of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkSourceIpV4** *(list) --*
            The source IPv4 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkSourceIpV6** *(list) --*
            The source IPv6 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkSourcePort** *(list) --*
            The source port of network-related information about a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **NetworkSourceDomain** *(list) --*
            The source domain of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkSourceMac** *(list) --*
            The source media access control (MAC) address of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkDestinationIpV4** *(list) --*
            The destination IPv4 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkDestinationIpV6** *(list) --*
            The destination IPv6 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkDestinationPort** *(list) --*
            The destination port of network-related information about a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **NetworkDestinationDomain** *(list) --*
            The destination domain of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessName** *(list) --*
            The name of the process.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessPath** *(list) --*
            The path to the process executable.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessPid** *(list) --*
            The process ID.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **ProcessParentPid** *(list) --*
            The parent process ID.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **ProcessLaunchedAt** *(list) --*
            The date/time that the process was launched.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ProcessTerminatedAt** *(list) --*
            The date/time that the process was terminated.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ThreatIntelIndicatorType** *(list) --*
            The type of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorValue** *(list) --*
            The value of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorCategory** *(list) --*
            The category of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorLastObservedAt** *(list) --*
            The date/time of the last observation of a threat intel indicator.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ThreatIntelIndicatorSource** *(list) --*
            The source of the threat intel.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorSourceUrl** *(list) --*
            The URL for more details from the source of the threat intel.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceType** *(list) --*
            Specifies the type of the resource for which details are provided.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceId** *(list) --*
            The canonical identifier for the given resource type.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourcePartition** *(list) --*
            The canonical AWS partition name to which the region is assigned.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceRegion** *(list) --*
            The canonical AWS external region name where this resource is located.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceTags** *(list) --*
            A list of AWS tags associated with a resource at the time the finding was processed.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ResourceAwsEc2InstanceType** *(list) --*
            The instance type of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceImageId** *(list) --*
            The Amazon Machine Image (AMI) ID of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*
            The IPv4 addresses associated with the instance.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*
            The IPv6 addresses associated with the instance.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **ResourceAwsEc2InstanceKeyName** *(list) --*
            The key name associated with the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*
            The IAM profile ARN of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceVpcId** *(list) --*
            The identifier of the VPC in which the instance was launched.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceSubnetId** *(list) --*
            The identifier of the subnet in which the instance was launched.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*
            The date/time the instance was launched.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceAwsS3BucketOwnerId** *(list) --*
            The canonical user ID of the owner of the S3 bucket.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsS3BucketOwnerName** *(list) --*
            The display name of the owner of the S3 bucket.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyUserName** *(list) --*
            The user associated with the IAM access key related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyStatus** *(list) --*
            The status of the IAM access key related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*
            The creation date/time of the IAM access key related to a finding.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceContainerName** *(list) --*
            The name of the container related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerImageId** *(list) --*
            The identifier of the image related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerImageName** *(list) --*
            The name of the image related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerLaunchedAt** *(list) --*
            The date/time that the container was started.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceDetailsOther** *(list) --*
            The details of a resource that does not have a specific sub-field for the resource type defined.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ComplianceStatus** *(list) --*
            Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard (for example, AWS CIS Foundations). Contains compliance-related finding details.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **VerificationState** *(list) --*
            Indicates the veracity of a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **WorkflowState** *(list) --*
            The workflow state of a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RecordState** *(list) --*
            The updated record state for the finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RelatedFindingsProductArn** *(list) --*
            The ARN of the solution that generated a related finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RelatedFindingsId** *(list) --*
            The solution-generated identifier for a related finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NoteText** *(list) --*
            The text of a note.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NoteUpdatedAt** *(list) --*
            The timestamp of when the note was updated.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **NoteUpdatedBy** *(list) --*
            The principal that created a note.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Keyword** *(list) --*
            A keyword for a finding.
            - *(dict) --*
              A keyword filter for querying findings.
              - **Value** *(string) --*
                A value for the keyword.
        :type Note: dict
        :param Note:
          The updated note for the finding.
          - **Text** *(string) --* **[REQUIRED]**
            The updated note text.
          - **UpdatedBy** *(string) --* **[REQUIRED]**
            The principal that updated the note.
        :type RecordState: string
        :param RecordState:
          The updated record state for the finding.
        :rtype: dict
        :returns:
        """
        pass

    def update_insight(self, InsightArn: str, Name: str = None, Filters: Dict = None, GroupByAttribute: str = None) -> Dict:
        """
        Updates the AWS Security Hub insight specified by the insight ARN.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/UpdateInsight>`_
        
        **Request Syntax**
        ::
          response = client.update_insight(
              InsightArn='string',
              Name='string',
              Filters={
                  'ProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'AwsAccountId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Id': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'GeneratorId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Type': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'FirstObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'LastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'CreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'UpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'SeverityProduct': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityNormalized': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'SeverityLabel': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Confidence': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Criticality': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'Title': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Description': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RecommendationText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'SourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProductFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ProductName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'CompanyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'UserDefinedFields': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'MalwareName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwareType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwarePath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'MalwareState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkDirection': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkProtocol': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourceIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkSourcePort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkSourceDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkSourceMac': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NetworkDestinationIpV4': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationIpV6': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'NetworkDestinationPort': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'NetworkDestinationDomain': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessPath': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ProcessPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessParentPid': [
                      {
                          'Gte': 123.0,
                          'Lte': 123.0,
                          'Eq': 123.0
                      },
                  ],
                  'ProcessLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ProcessTerminatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorValue': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorCategory': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorLastObservedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ThreatIntelIndicatorSource': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ThreatIntelIndicatorSourceUrl': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourcePartition': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceRegion': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ResourceAwsEc2InstanceType': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV4Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceIpV6Addresses': [
                      {
                          'Cidr': 'string'
                      },
                  ],
                  'ResourceAwsEc2InstanceKeyName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceVpcId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceSubnetId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsEc2InstanceLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceAwsS3BucketOwnerId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsS3BucketOwnerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyUserName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceAwsIamAccessKeyCreatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceContainerName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerImageName': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'ResourceContainerLaunchedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'ResourceDetailsOther': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Comparison': 'CONTAINS'
                      },
                  ],
                  'ComplianceStatus': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'VerificationState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'WorkflowState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RecordState': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsProductArn': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'RelatedFindingsId': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NoteText': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'NoteUpdatedAt': [
                      {
                          'Start': 'string',
                          'End': 'string',
                          'DateRange': {
                              'Value': 123,
                              'Unit': 'DAYS'
                          }
                      },
                  ],
                  'NoteUpdatedBy': [
                      {
                          'Value': 'string',
                          'Comparison': 'EQUALS'|'CONTAINS'|'PREFIX'
                      },
                  ],
                  'Keyword': [
                      {
                          'Value': 'string'
                      },
                  ]
              },
              GroupByAttribute='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type InsightArn: string
        :param InsightArn: **[REQUIRED]**
          The ARN of the insight that you want to update.
        :type Name: string
        :param Name:
          The updated name for the insight.
        :type Filters: dict
        :param Filters:
          The updated filters that define this insight.
          - **ProductArn** *(list) --*
            The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) once this provider\'s product (solution that generates findings) is registered with Security Hub.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **AwsAccountId** *(list) --*
            The AWS account ID in which a finding is generated.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Id** *(list) --*
            The security findings provider-specific identifier for a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **GeneratorId** *(list) --*
            This is the identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings provider\'s solutions, this generator can be called a rule, a check, a detector, a plug-in, etc.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Type** *(list) --*
            A finding type in the format of \'namespace/category/classifier\' that classifies a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **FirstObservedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **LastObservedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **CreatedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the potential security issue captured by a finding was created by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **UpdatedAt** *(list) --*
            An ISO8601-formatted timestamp that indicates when the finding record was last updated by the security findings provider.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **SeverityProduct** *(list) --*
            The native severity as defined by the security findings provider\'s solution that generated the finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **SeverityNormalized** *(list) --*
            The normalized severity of a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **SeverityLabel** *(list) --*
            The label of a finding\'s severity.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Confidence** *(list) --*
            A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale. 0 equates zero percent confidence and 100 equates to 100 percent confidence.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **Criticality** *(list) --*
            The level of importance assigned to the resources associated with the finding. A score of 0 means the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **Title** *(list) --*
            A finding\'s title.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Description** *(list) --*
            A finding\'s description.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RecommendationText** *(list) --*
            The recommendation of what to do about the issue described in a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **SourceUrl** *(list) --*
            A URL that links to a page about the current finding in the security findings provider\'s solution.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProductFields** *(list) --*
            A data type where security findings providers can include additional solution-specific details that are not part of the defined AwsSecurityFinding format.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ProductName** *(list) --*
            The name of the solution (product) that generates findings.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **CompanyName** *(list) --*
            The name of the findings provider (company) that owns the solution (product) that generates findings.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **UserDefinedFields** *(list) --*
            A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **MalwareName** *(list) --*
            The name of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwareType** *(list) --*
            The type of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwarePath** *(list) --*
            The filesystem path of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **MalwareState** *(list) --*
            The state of the malware that was observed.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkDirection** *(list) --*
            Indicates the direction of network traffic associated with a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkProtocol** *(list) --*
            The protocol of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkSourceIpV4** *(list) --*
            The source IPv4 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkSourceIpV6** *(list) --*
            The source IPv6 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkSourcePort** *(list) --*
            The source port of network-related information about a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **NetworkSourceDomain** *(list) --*
            The source domain of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkSourceMac** *(list) --*
            The source media access control (MAC) address of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NetworkDestinationIpV4** *(list) --*
            The destination IPv4 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkDestinationIpV6** *(list) --*
            The destination IPv6 address of network-related information about a finding.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **NetworkDestinationPort** *(list) --*
            The destination port of network-related information about a finding.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **NetworkDestinationDomain** *(list) --*
            The destination domain of network-related information about a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessName** *(list) --*
            The name of the process.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessPath** *(list) --*
            The path to the process executable.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ProcessPid** *(list) --*
            The process ID.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **ProcessParentPid** *(list) --*
            The parent process ID.
            - *(dict) --*
              A number filter for querying findings.
              - **Gte** *(float) --*
                Represents the \"greater than equal\" condition to be applied to a single field when querying for findings.
              - **Lte** *(float) --*
                Represents the \"less than equal\" condition to be applied to a single field when querying for findings.
              - **Eq** *(float) --*
                Represents the \"equal to\" condition to be applied to a single field when querying for findings.
          - **ProcessLaunchedAt** *(list) --*
            The date/time that the process was launched.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ProcessTerminatedAt** *(list) --*
            The date/time that the process was terminated.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ThreatIntelIndicatorType** *(list) --*
            The type of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorValue** *(list) --*
            The value of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorCategory** *(list) --*
            The category of a threat intel indicator.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorLastObservedAt** *(list) --*
            The date/time of the last observation of a threat intel indicator.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ThreatIntelIndicatorSource** *(list) --*
            The source of the threat intel.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ThreatIntelIndicatorSourceUrl** *(list) --*
            The URL for more details from the source of the threat intel.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceType** *(list) --*
            Specifies the type of the resource for which details are provided.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceId** *(list) --*
            The canonical identifier for the given resource type.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourcePartition** *(list) --*
            The canonical AWS partition name to which the region is assigned.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceRegion** *(list) --*
            The canonical AWS external region name where this resource is located.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceTags** *(list) --*
            A list of AWS tags associated with a resource at the time the finding was processed.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ResourceAwsEc2InstanceType** *(list) --*
            The instance type of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceImageId** *(list) --*
            The Amazon Machine Image (AMI) ID of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceIpV4Addresses** *(list) --*
            The IPv4 addresses associated with the instance.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **ResourceAwsEc2InstanceIpV6Addresses** *(list) --*
            The IPv6 addresses associated with the instance.
            - *(dict) --*
              The IP filter for querying findings.>
              - **Cidr** *(string) --*
                Finding\'s CIDR value.
          - **ResourceAwsEc2InstanceKeyName** *(list) --*
            The key name associated with the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceIamInstanceProfileArn** *(list) --*
            The IAM profile ARN of the instance.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceVpcId** *(list) --*
            The identifier of the VPC in which the instance was launched.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceSubnetId** *(list) --*
            The identifier of the subnet in which the instance was launched.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsEc2InstanceLaunchedAt** *(list) --*
            The date/time the instance was launched.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceAwsS3BucketOwnerId** *(list) --*
            The canonical user ID of the owner of the S3 bucket.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsS3BucketOwnerName** *(list) --*
            The display name of the owner of the S3 bucket.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyUserName** *(list) --*
            The user associated with the IAM access key related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyStatus** *(list) --*
            The status of the IAM access key related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceAwsIamAccessKeyCreatedAt** *(list) --*
            The creation date/time of the IAM access key related to a finding.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceContainerName** *(list) --*
            The name of the container related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerImageId** *(list) --*
            The identifier of the image related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerImageName** *(list) --*
            The name of the image related to a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **ResourceContainerLaunchedAt** *(list) --*
            The date/time that the container was started.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **ResourceDetailsOther** *(list) --*
            The details of a resource that does not have a specific sub-field for the resource type defined.
            - *(dict) --*
              The map filter for querying findings.
              - **Key** *(string) --*
                The key of the map filter.
              - **Value** *(string) --*
                The value for the key in the map filter.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a key value when querying for findings with a map filter.
          - **ComplianceStatus** *(list) --*
            Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard (for example, AWS CIS Foundations). Contains compliance-related finding details.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **VerificationState** *(list) --*
            Indicates the veracity of a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **WorkflowState** *(list) --*
            The workflow state of a finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RecordState** *(list) --*
            The updated record state for the finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RelatedFindingsProductArn** *(list) --*
            The ARN of the solution that generated a related finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **RelatedFindingsId** *(list) --*
            The solution-generated identifier for a related finding.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NoteText** *(list) --*
            The text of a note.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **NoteUpdatedAt** *(list) --*
            The timestamp of when the note was updated.
            - *(dict) --*
              A date filter for querying findings.
              - **Start** *(string) --*
                A start date for the date filter.
              - **End** *(string) --*
                An end date for the date filter.
              - **DateRange** *(dict) --*
                A date range for the date filter.
                - **Value** *(integer) --*
                  A date range value for the date filter.
                - **Unit** *(string) --*
                  A date range unit for the date filter.
          - **NoteUpdatedBy** *(list) --*
            The principal that created a note.
            - *(dict) --*
              A string filter for querying findings.
              - **Value** *(string) --*
                The string filter value.
              - **Comparison** *(string) --*
                Represents the condition to be applied to a string value when querying for findings.
          - **Keyword** *(list) --*
            A keyword for a finding.
            - *(dict) --*
              A keyword filter for querying findings.
              - **Value** *(string) --*
                A value for the keyword.
        :type GroupByAttribute: string
        :param GroupByAttribute:
          The updated GroupBy attribute that defines this insight.
        :rtype: dict
        :returns:
        """
        pass
