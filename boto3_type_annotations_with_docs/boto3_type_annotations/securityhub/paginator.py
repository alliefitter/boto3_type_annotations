from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetEnabledStandards(Paginator):
    def paginate(self, StandardsSubscriptionArns: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SecurityHub.Client.get_enabled_standards`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetEnabledStandards>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StandardsSubscriptionArns=[
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
                  .. warning::
                    In this release, Security Hub only supports the CIS AWS Foundations standard. 
                    Its ARN is arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0.
                - **StandardsInput** *(dict) --* 
                  - *(string) --* 
                    - *(string) --* 
                - **StandardsStatus** *(string) --* 
                  The standard's status.
        :type StandardsSubscriptionArns: list
        :param StandardsSubscriptionArns:
          The list of standards subscription ARNS that you want to list and describe.
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


class GetFindings(Paginator):
    def paginate(self, Filters: Dict = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SecurityHub.Client.get_findings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetFindings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
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
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                  .. note::
                    In this release, Title is a required property.
                - **Description** *(string) --* 
                  A finding's description.
                  .. note::
                    In this release, Description is a required property.
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


class GetInsights(Paginator):
    def paginate(self, InsightArns: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SecurityHub.Client.get_insights`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetInsights>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InsightArns=[
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
        :type InsightArns: list
        :param InsightArns:
          The ARNS of the insights that you want to describe.
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


class ListEnabledProductsForImport(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SecurityHub.Client.list_enabled_products_for_import`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListEnabledProductsForImport>`_
        
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
                'ProductSubscriptions': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProductSubscriptions** *(list) --* 
              A list of ARNs for the resources that represent your subscriptions to products. 
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


class ListInvitations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SecurityHub.Client.list_invitations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListInvitations>`_
        
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
                'Invitations': [
                    {
                        'AccountId': 'string',
                        'InvitationId': 'string',
                        'InvitedAt': datetime(2015, 1, 1),
                        'MemberStatus': 'string'
                    },
                ],
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


class ListMembers(Paginator):
    def paginate(self, OnlyAssociated: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SecurityHub.Client.list_members`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListMembers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              OnlyAssociated=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
        :type OnlyAssociated: boolean
        :param OnlyAssociated:
          Specifies what member accounts the response includes based on their relationship status with the master account. The default value is TRUE. If onlyAssociated is set to TRUE, the response includes member accounts whose relationship status with the master is set to ENABLED or DISABLED. If onlyAssociated is set to FALSE, the response includes all existing member accounts.
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
