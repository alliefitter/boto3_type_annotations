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

    def create_application(self, Author: str, Description: str, Name: str, HomePageUrl: str = None, Labels: List = None, LicenseBody: str = None, LicenseUrl: str = None, ReadmeBody: str = None, ReadmeUrl: str = None, SemanticVersion: str = None, SourceCodeUrl: str = None, SpdxLicenseId: str = None, TemplateBody: str = None, TemplateUrl: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateApplication>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_application(
              Author=\'string\',
              Description=\'string\',
              HomePageUrl=\'string\',
              Labels=[
                  \'string\',
              ],
              LicenseBody=\'string\',
              LicenseUrl=\'string\',
              Name=\'string\',
              ReadmeBody=\'string\',
              ReadmeUrl=\'string\',
              SemanticVersion=\'string\',
              SourceCodeUrl=\'string\',
              SpdxLicenseId=\'string\',
              TemplateBody=\'string\',
              TemplateUrl=\'string\'
          )
        :type Author: string
        :param Author: **[REQUIRED]** 
        
          The name of the author publishing the app.
        
          Minimum length=1. Maximum length=127.
        
          Pattern \"^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\";
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          The description of the application.
        
          Minimum length=1. Maximum length=256
        
        :type HomePageUrl: string
        :param HomePageUrl: 
        
          A URL with more information about the application, for example the location of your GitHub repository for the application.
        
        :type Labels: list
        :param Labels: 
        
          Labels to improve discovery of apps in search results.
        
          Minimum length=1. Maximum length=127. Maximum number of labels: 10
        
          Pattern: \"^[a-zA-Z0-9+\\-_:\\/@]+$\";
        
          - *(string) --* 
        
        :type LicenseBody: string
        :param LicenseBody: 
        
          A local text file that contains the license of the app that matches the spdxLicenseID value of your application. The file has the format file://<path>/<filename>.
        
          Maximum size 5 MB
        
          You can specify only one of licenseBody and licenseUrl; otherwise, an error results.
        
        :type LicenseUrl: string
        :param LicenseUrl: 
        
          A link to the S3 object that contains the license of the app that matches the spdxLicenseID value of your application.
        
          Maximum size 5 MB
        
          You can specify only one of licenseBody and licenseUrl; otherwise, an error results.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the application that you want to publish.
        
          Minimum length=1. Maximum length=140
        
          Pattern: \"[a-zA-Z0-9\\-]+\";
        
        :type ReadmeBody: string
        :param ReadmeBody: 
        
          A local text readme file in Markdown language that contains a more detailed description of the application and how it works. The file has the format file://<path>/<filename>.
        
          Maximum size 5 MB
        
          You can specify only one of readmeBody and readmeUrl; otherwise, an error results.
        
        :type ReadmeUrl: string
        :param ReadmeUrl: 
        
          A link to the S3 object in Markdown language that contains a more detailed description of the application and how it works.
        
          Maximum size 5 MB
        
          You can specify only one of readmeBody and readmeUrl; otherwise, an error results.
        
        :type SemanticVersion: string
        :param SemanticVersion: 
        
          The semantic version of the application:
        
           `https\://semver.org/ <https://semver.org/>`__  
        
        :type SourceCodeUrl: string
        :param SourceCodeUrl: 
        
          A link to a public repository for the source code of your application.
        
        :type SpdxLicenseId: string
        :param SpdxLicenseId: 
        
          A valid identifier from `https\://spdx.org/licenses/ <https://spdx.org/licenses/>`__ .
        
        :type TemplateBody: string
        :param TemplateBody: 
        
          The local raw packaged AWS SAM template file of your application. The file has the format file://<path>/<filename>.
        
          You can specify only one of templateBody and templateUrl; otherwise an error results.
        
        :type TemplateUrl: string
        :param TemplateUrl: 
        
          A link to the S3 object containing the packaged AWS SAM template of your application.
        
          You can specify only one of templateBody and templateUrl; otherwise an error results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ApplicationId\': \'string\',
                \'Author\': \'string\',
                \'CreationTime\': \'string\',
                \'Description\': \'string\',
                \'HomePageUrl\': \'string\',
                \'Labels\': [
                    \'string\',
                ],
                \'LicenseUrl\': \'string\',
                \'Name\': \'string\',
                \'ReadmeUrl\': \'string\',
                \'SpdxLicenseId\': \'string\',
                \'Version\': {
                    \'ApplicationId\': \'string\',
                    \'CreationTime\': \'string\',
                    \'ParameterDefinitions\': [
                        {
                            \'AllowedPattern\': \'string\',
                            \'AllowedValues\': [
                                \'string\',
                            ],
                            \'ConstraintDescription\': \'string\',
                            \'DefaultValue\': \'string\',
                            \'Description\': \'string\',
                            \'MaxLength\': 123,
                            \'MaxValue\': 123,
                            \'MinLength\': 123,
                            \'MinValue\': 123,
                            \'Name\': \'string\',
                            \'NoEcho\': True|False,
                            \'ReferencedByResources\': [
                                \'string\',
                            ],
                            \'Type\': \'string\'
                        },
                    ],
                    \'RequiredCapabilities\': [
                        \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\'|\'CAPABILITY_AUTO_EXPAND\'|\'CAPABILITY_RESOURCE_POLICY\',
                    ],
                    \'ResourcesSupported\': True|False,
                    \'SemanticVersion\': \'string\',
                    \'SourceCodeUrl\': \'string\',
                    \'TemplateUrl\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **ApplicationId** *(string) --* 
        
              The application Amazon Resource Name (ARN).
        
            - **Author** *(string) --* 
        
              The name of the author publishing the app.
        
              Minimum length=1. Maximum length=127.
        
              Pattern \"^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\";
        
            - **CreationTime** *(string) --* 
        
              The date and time this resource was created.
        
            - **Description** *(string) --* 
        
              The description of the application.
        
              Minimum length=1. Maximum length=256
        
            - **HomePageUrl** *(string) --* 
        
              A URL with more information about the application, for example the location of your GitHub repository for the application.
        
            - **Labels** *(list) --* 
        
              Labels to improve discovery of apps in search results.
        
              Minimum length=1. Maximum length=127. Maximum number of labels: 10
        
              Pattern: \"^[a-zA-Z0-9+\\-_:\\/@]+$\";
        
              - *(string) --* 
          
            - **LicenseUrl** *(string) --* 
        
              A link to a license file of the app that matches the spdxLicenseID value of your application.
        
              Maximum size 5 MB
        
            - **Name** *(string) --* 
        
              The name of the application.
        
              Minimum length=1. Maximum length=140
        
              Pattern: \"[a-zA-Z0-9\\-]+\";
        
            - **ReadmeUrl** *(string) --* 
        
              A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.
        
              Maximum size 5 MB
        
            - **SpdxLicenseId** *(string) --* 
        
              A valid identifier from https://spdx.org/licenses/.
        
            - **Version** *(dict) --* 
        
              Version information about the application.
        
              - **ApplicationId** *(string) --* 
        
                The application Amazon Resource Name (ARN).
        
              - **CreationTime** *(string) --* 
        
                The date and time this resource was created.
        
              - **ParameterDefinitions** *(list) --* 
        
                An array of parameter types supported by the application.
        
                - *(dict) --* 
        
                  Parameters supported by the application.
        
                  - **AllowedPattern** *(string) --* 
        
                    A regular expression that represents the patterns to allow for String types.
        
                  - **AllowedValues** *(list) --* 
        
                    An array containing the list of values allowed for the parameter.
        
                    - *(string) --* 
                
                  - **ConstraintDescription** *(string) --* 
        
                    A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:
        
                    Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ 
        
                    By adding a constraint description, such as \"must contain only uppercase and lowercase letters and numbers,\" you can display the following customized error message:
        
                    Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers. 
        
                  - **DefaultValue** *(string) --* 
        
                    A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.
        
                  - **Description** *(string) --* 
        
                    A string of up to 4,000 characters that describes the parameter.
        
                  - **MaxLength** *(integer) --* 
        
                    An integer value that determines the largest number of characters that you want to allow for String types.
        
                  - **MaxValue** *(integer) --* 
        
                    A numeric value that determines the largest numeric value that you want to allow for Number types.
        
                  - **MinLength** *(integer) --* 
        
                    An integer value that determines the smallest number of characters that you want to allow for String types.
        
                  - **MinValue** *(integer) --* 
        
                    A numeric value that determines the smallest numeric value that you want to allow for Number types.
        
                  - **Name** *(string) --* 
        
                    The name of the parameter.
        
                  - **NoEcho** *(boolean) --* 
        
                    Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*****).
        
                  - **ReferencedByResources** *(list) --* 
        
                    A list of AWS SAM resources that use this parameter.
        
                    - *(string) --* 
                
                  - **Type** *(string) --* 
        
                    The type of the parameter.
        
                    Valid values: String | Number | List<Number> | CommaDelimitedList 
        
                    String: A literal string.
        
                    For example, users can specify \"MyUserName\".
        
                    Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.
        
                    For example, users might specify \"8888\".
        
                    List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.
        
                    For example, users might specify \"80,20\", and then Ref results in [\"80\",\"20\"].
        
                    CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.
        
                    For example, users might specify \"test,dev,prod\", and then Ref results in [\"test\",\"dev\",\"prod\"].
        
              - **RequiredCapabilities** *(list) --* 
        
                A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
        
                The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, and CAPABILITY_RESOURCE_POLICY.
        
                The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: `AWS\:\:IAM\:\:Group <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__ , `AWS\:\:IAM\:\:InstanceProfile <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__ , `AWS\:\:IAM\:\:Policy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html>`__ , and `AWS\:\:IAM\:\:Role <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__ . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
        
                The following resources require you to specify CAPABILITY_RESOURCE_POLICY: `AWS\:\:ApplicationAutoScaling\:\:ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__ , `AWS\:\:S3\:\:BucketPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__ , `AWS\:\:SQS\:\:QueuePolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__ , and `AWS\:\:SNS\:TopicPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__ .
        
                If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.
        
                Valid values: CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_RESOURCE_POLICY
        
                - *(string) --* 
            
              - **ResourcesSupported** *(boolean) --* 
        
                Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.
        
              - **SemanticVersion** *(string) --* 
        
                The semantic version of the application:
        
                 `https\://semver.org/ <https://semver.org/>`__  
        
              - **SourceCodeUrl** *(string) --* 
        
                A link to a public repository for the source code of your application.
        
              - **TemplateUrl** *(string) --* 
        
                A link to the packaged AWS SAM template of your application.
        
        """
        pass

    def create_application_version(self, ApplicationId: str, SemanticVersion: str, SourceCodeUrl: str = None, TemplateBody: str = None, TemplateUrl: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateApplicationVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_application_version(
              ApplicationId=\'string\',
              SemanticVersion=\'string\',
              SourceCodeUrl=\'string\',
              TemplateBody=\'string\',
              TemplateUrl=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :type SemanticVersion: string
        :param SemanticVersion: **[REQUIRED]** 
        
          The semantic version of the new version.
        
        :type SourceCodeUrl: string
        :param SourceCodeUrl: 
        
          A link to a public repository for the source code of your application.
        
        :type TemplateBody: string
        :param TemplateBody: 
        
          The raw packaged AWS SAM template of your application.
        
        :type TemplateUrl: string
        :param TemplateUrl: 
        
          A link to the packaged AWS SAM template of your application.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ApplicationId\': \'string\',
                \'CreationTime\': \'string\',
                \'ParameterDefinitions\': [
                    {
                        \'AllowedPattern\': \'string\',
                        \'AllowedValues\': [
                            \'string\',
                        ],
                        \'ConstraintDescription\': \'string\',
                        \'DefaultValue\': \'string\',
                        \'Description\': \'string\',
                        \'MaxLength\': 123,
                        \'MaxValue\': 123,
                        \'MinLength\': 123,
                        \'MinValue\': 123,
                        \'Name\': \'string\',
                        \'NoEcho\': True|False,
                        \'ReferencedByResources\': [
                            \'string\',
                        ],
                        \'Type\': \'string\'
                    },
                ],
                \'RequiredCapabilities\': [
                    \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\'|\'CAPABILITY_AUTO_EXPAND\'|\'CAPABILITY_RESOURCE_POLICY\',
                ],
                \'ResourcesSupported\': True|False,
                \'SemanticVersion\': \'string\',
                \'SourceCodeUrl\': \'string\',
                \'TemplateUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **ApplicationId** *(string) --* 
        
              The application Amazon Resource Name (ARN).
        
            - **CreationTime** *(string) --* 
        
              The date and time this resource was created.
        
            - **ParameterDefinitions** *(list) --* 
        
              An array of parameter types supported by the application.
        
              - *(dict) --* 
        
                Parameters supported by the application.
        
                - **AllowedPattern** *(string) --* 
        
                  A regular expression that represents the patterns to allow for String types.
        
                - **AllowedValues** *(list) --* 
        
                  An array containing the list of values allowed for the parameter.
        
                  - *(string) --* 
              
                - **ConstraintDescription** *(string) --* 
        
                  A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:
        
                  Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ 
        
                  By adding a constraint description, such as \"must contain only uppercase and lowercase letters and numbers,\" you can display the following customized error message:
        
                  Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers. 
        
                - **DefaultValue** *(string) --* 
        
                  A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.
        
                - **Description** *(string) --* 
        
                  A string of up to 4,000 characters that describes the parameter.
        
                - **MaxLength** *(integer) --* 
        
                  An integer value that determines the largest number of characters that you want to allow for String types.
        
                - **MaxValue** *(integer) --* 
        
                  A numeric value that determines the largest numeric value that you want to allow for Number types.
        
                - **MinLength** *(integer) --* 
        
                  An integer value that determines the smallest number of characters that you want to allow for String types.
        
                - **MinValue** *(integer) --* 
        
                  A numeric value that determines the smallest numeric value that you want to allow for Number types.
        
                - **Name** *(string) --* 
        
                  The name of the parameter.
        
                - **NoEcho** *(boolean) --* 
        
                  Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*****).
        
                - **ReferencedByResources** *(list) --* 
        
                  A list of AWS SAM resources that use this parameter.
        
                  - *(string) --* 
              
                - **Type** *(string) --* 
        
                  The type of the parameter.
        
                  Valid values: String | Number | List<Number> | CommaDelimitedList 
        
                  String: A literal string.
        
                  For example, users can specify \"MyUserName\".
        
                  Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.
        
                  For example, users might specify \"8888\".
        
                  List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.
        
                  For example, users might specify \"80,20\", and then Ref results in [\"80\",\"20\"].
        
                  CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.
        
                  For example, users might specify \"test,dev,prod\", and then Ref results in [\"test\",\"dev\",\"prod\"].
        
            - **RequiredCapabilities** *(list) --* 
        
              A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
        
              The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, and CAPABILITY_RESOURCE_POLICY.
        
              The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: `AWS\:\:IAM\:\:Group <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__ , `AWS\:\:IAM\:\:InstanceProfile <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__ , `AWS\:\:IAM\:\:Policy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html>`__ , and `AWS\:\:IAM\:\:Role <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__ . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
        
              The following resources require you to specify CAPABILITY_RESOURCE_POLICY: `AWS\:\:ApplicationAutoScaling\:\:ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__ , `AWS\:\:S3\:\:BucketPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__ , `AWS\:\:SQS\:\:QueuePolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__ , and `AWS\:\:SNS\:TopicPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__ .
        
              If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.
        
              Valid values: CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_RESOURCE_POLICY
        
              - *(string) --* 
          
            - **ResourcesSupported** *(boolean) --* 
        
              Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.
        
            - **SemanticVersion** *(string) --* 
        
              The semantic version of the application:
        
               `https\://semver.org/ <https://semver.org/>`__  
        
            - **SourceCodeUrl** *(string) --* 
        
              A link to a public repository for the source code of your application.
        
            - **TemplateUrl** *(string) --* 
        
              A link to the packaged AWS SAM template of your application.
        
        """
        pass

    def create_cloud_formation_change_set(self, ApplicationId: str, StackName: str, Capabilities: List = None, ChangeSetName: str = None, ClientToken: str = None, Description: str = None, NotificationArns: List = None, ParameterOverrides: List = None, ResourceTypes: List = None, RollbackConfiguration: Dict = None, SemanticVersion: str = None, Tags: List = None, TemplateId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateCloudFormationChangeSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cloud_formation_change_set(
              ApplicationId=\'string\',
              Capabilities=[
                  \'string\',
              ],
              ChangeSetName=\'string\',
              ClientToken=\'string\',
              Description=\'string\',
              NotificationArns=[
                  \'string\',
              ],
              ParameterOverrides=[
                  {
                      \'Name\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              ResourceTypes=[
                  \'string\',
              ],
              RollbackConfiguration={
                  \'MonitoringTimeInMinutes\': 123,
                  \'RollbackTriggers\': [
                      {
                          \'Arn\': \'string\',
                          \'Type\': \'string\'
                      },
                  ]
              },
              SemanticVersion=\'string\',
              StackName=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              TemplateId=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :type Capabilities: list
        :param Capabilities: 
        
          A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
        
          The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, and CAPABILITY_RESOURCE_POLICY.
        
          The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: `AWS\:\:IAM\:\:Group <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__ , `AWS\:\:IAM\:\:InstanceProfile <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__ , `AWS\:\:IAM\:\:Policy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html>`__ , and `AWS\:\:IAM\:\:Role <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__ . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
        
          The following resources require you to specify CAPABILITY_RESOURCE_POLICY: `AWS\:\:ApplicationAutoScaling\:\:ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__ , `AWS\:\:S3\:\:BucketPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__ , `AWS\:\:SQS\:\:QueuePolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__ , and `AWS\:\:SNS\:TopicPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__ .
        
          If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.
        
          Valid values: CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_RESOURCE_POLICY
        
          - *(string) --* 
        
        :type ChangeSetName: string
        :param ChangeSetName: 
        
          This property corresponds to the parameter of the same name for the *AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__* API.
        
        :type ClientToken: string
        :param ClientToken: 
        
          This property corresponds to the parameter of the same name for the *AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__* API.
        
        :type Description: string
        :param Description: 
        
          This property corresponds to the parameter of the same name for the *AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__* API.
        
        :type NotificationArns: list
        :param NotificationArns: 
        
          This property corresponds to the parameter of the same name for the *AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__* API.
        
          - *(string) --* 
        
        :type ParameterOverrides: list
        :param ParameterOverrides: 
        
          A list of parameter values for the parameters of the application.
        
          - *(dict) --* 
        
            Parameter value of the application.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The input value associated with the parameter.
        
        :type ResourceTypes: list
        :param ResourceTypes: 
        
          This property corresponds to the parameter of the same name for the *AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__* API.
        
          - *(string) --* 
        
        :type RollbackConfiguration: dict
        :param RollbackConfiguration: 
        
          This property corresponds to the parameter of the same name for the *AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__* API.
        
          - **MonitoringTimeInMinutes** *(integer) --* 
        
            This property corresponds to the content of the same name for the *AWS CloudFormation `RollbackConfiguration <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration>`__* Data Type.
        
          - **RollbackTriggers** *(list) --* 
        
            This property corresponds to the content of the same name for the *AWS CloudFormation `RollbackConfiguration <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration>`__* Data Type.
        
            - *(dict) --* 
        
              This property corresponds to the *AWS CloudFormation `RollbackTrigger <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__* Data Type.
        
              - **Arn** *(string) --* **[REQUIRED]** 
        
                This property corresponds to the content of the same name for the *AWS CloudFormation `RollbackTrigger <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__* Data Type.
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                This property corresponds to the content of the same name for the *AWS CloudFormation `RollbackTrigger <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__* Data Type.
        
        :type SemanticVersion: string
        :param SemanticVersion: 
        
          The semantic version of the application:
        
           `https\://semver.org/ <https://semver.org/>`__  
        
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          This property corresponds to the parameter of the same name for the *AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__* API.
        
        :type Tags: list
        :param Tags: 
        
          This property corresponds to the parameter of the same name for the *AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__* API.
        
          - *(dict) --* 
        
            This property corresponds to the *AWS CloudFormation `Tag <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__* Data Type.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              This property corresponds to the content of the same name for the *AWS CloudFormation `Tag <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__* Data Type.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              This property corresponds to the content of the same name for the *AWS CloudFormation `Tag <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__* Data Type.
        
        :type TemplateId: string
        :param TemplateId: 
        
          The UUID returned by CreateCloudFormationTemplate.
        
          Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ApplicationId\': \'string\',
                \'ChangeSetId\': \'string\',
                \'SemanticVersion\': \'string\',
                \'StackId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **ApplicationId** *(string) --* 
        
              The application Amazon Resource Name (ARN).
        
            - **ChangeSetId** *(string) --* 
        
              The Amazon Resource Name (ARN) of the change set.
        
              Length constraints: Minimum length of 1.
        
              Pattern: ARN:[-a-zA-Z0-9:/]*
        
            - **SemanticVersion** *(string) --* 
        
              The semantic version of the application:
        
               `https\://semver.org/ <https://semver.org/>`__  
        
            - **StackId** *(string) --* 
        
              The unique ID of the stack.
        
        """
        pass

    def create_cloud_formation_template(self, ApplicationId: str, SemanticVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateCloudFormationTemplate>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cloud_formation_template(
              ApplicationId=\'string\',
              SemanticVersion=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :type SemanticVersion: string
        :param SemanticVersion: 
        
          The semantic version of the application:
        
           `https\://semver.org/ <https://semver.org/>`__  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ApplicationId\': \'string\',
                \'CreationTime\': \'string\',
                \'ExpirationTime\': \'string\',
                \'SemanticVersion\': \'string\',
                \'Status\': \'PREPARING\'|\'ACTIVE\'|\'EXPIRED\',
                \'TemplateId\': \'string\',
                \'TemplateUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **ApplicationId** *(string) --* 
        
              The application Amazon Resource Name (ARN).
        
            - **CreationTime** *(string) --* 
        
              The date and time this resource was created.
        
            - **ExpirationTime** *(string) --* 
        
              The date and time this template expires. Templates expire 1 hour after creation.
        
            - **SemanticVersion** *(string) --* 
        
              The semantic version of the application:
        
               `https\://semver.org/ <https://semver.org/>`__  
        
            - **Status** *(string) --* 
        
              Status of the template creation workflow.
        
              Possible values: PREPARING | ACTIVE | EXPIRED
        
            - **TemplateId** *(string) --* 
        
              The UUID returned by CreateCloudFormationTemplate.
        
              Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}
        
            - **TemplateUrl** *(string) --* 
        
              A link to the template that can be used to deploy the application using AWS CloudFormation.
        
        """
        pass

    def delete_application(self, ApplicationId: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/DeleteApplication>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_application(
              ApplicationId=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :returns: None
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

    def get_application(self, ApplicationId: str, SemanticVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/GetApplication>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_application(
              ApplicationId=\'string\',
              SemanticVersion=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :type SemanticVersion: string
        :param SemanticVersion: 
        
          The semantic version of the application to get.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ApplicationId\': \'string\',
                \'Author\': \'string\',
                \'CreationTime\': \'string\',
                \'Description\': \'string\',
                \'HomePageUrl\': \'string\',
                \'Labels\': [
                    \'string\',
                ],
                \'LicenseUrl\': \'string\',
                \'Name\': \'string\',
                \'ReadmeUrl\': \'string\',
                \'SpdxLicenseId\': \'string\',
                \'Version\': {
                    \'ApplicationId\': \'string\',
                    \'CreationTime\': \'string\',
                    \'ParameterDefinitions\': [
                        {
                            \'AllowedPattern\': \'string\',
                            \'AllowedValues\': [
                                \'string\',
                            ],
                            \'ConstraintDescription\': \'string\',
                            \'DefaultValue\': \'string\',
                            \'Description\': \'string\',
                            \'MaxLength\': 123,
                            \'MaxValue\': 123,
                            \'MinLength\': 123,
                            \'MinValue\': 123,
                            \'Name\': \'string\',
                            \'NoEcho\': True|False,
                            \'ReferencedByResources\': [
                                \'string\',
                            ],
                            \'Type\': \'string\'
                        },
                    ],
                    \'RequiredCapabilities\': [
                        \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\'|\'CAPABILITY_AUTO_EXPAND\'|\'CAPABILITY_RESOURCE_POLICY\',
                    ],
                    \'ResourcesSupported\': True|False,
                    \'SemanticVersion\': \'string\',
                    \'SourceCodeUrl\': \'string\',
                    \'TemplateUrl\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **ApplicationId** *(string) --* 
        
              The application Amazon Resource Name (ARN).
        
            - **Author** *(string) --* 
        
              The name of the author publishing the app.
        
              Minimum length=1. Maximum length=127.
        
              Pattern \"^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\";
        
            - **CreationTime** *(string) --* 
        
              The date and time this resource was created.
        
            - **Description** *(string) --* 
        
              The description of the application.
        
              Minimum length=1. Maximum length=256
        
            - **HomePageUrl** *(string) --* 
        
              A URL with more information about the application, for example the location of your GitHub repository for the application.
        
            - **Labels** *(list) --* 
        
              Labels to improve discovery of apps in search results.
        
              Minimum length=1. Maximum length=127. Maximum number of labels: 10
        
              Pattern: \"^[a-zA-Z0-9+\\-_:\\/@]+$\";
        
              - *(string) --* 
          
            - **LicenseUrl** *(string) --* 
        
              A link to a license file of the app that matches the spdxLicenseID value of your application.
        
              Maximum size 5 MB
        
            - **Name** *(string) --* 
        
              The name of the application.
        
              Minimum length=1. Maximum length=140
        
              Pattern: \"[a-zA-Z0-9\\-]+\";
        
            - **ReadmeUrl** *(string) --* 
        
              A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.
        
              Maximum size 5 MB
        
            - **SpdxLicenseId** *(string) --* 
        
              A valid identifier from https://spdx.org/licenses/.
        
            - **Version** *(dict) --* 
        
              Version information about the application.
        
              - **ApplicationId** *(string) --* 
        
                The application Amazon Resource Name (ARN).
        
              - **CreationTime** *(string) --* 
        
                The date and time this resource was created.
        
              - **ParameterDefinitions** *(list) --* 
        
                An array of parameter types supported by the application.
        
                - *(dict) --* 
        
                  Parameters supported by the application.
        
                  - **AllowedPattern** *(string) --* 
        
                    A regular expression that represents the patterns to allow for String types.
        
                  - **AllowedValues** *(list) --* 
        
                    An array containing the list of values allowed for the parameter.
        
                    - *(string) --* 
                
                  - **ConstraintDescription** *(string) --* 
        
                    A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:
        
                    Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ 
        
                    By adding a constraint description, such as \"must contain only uppercase and lowercase letters and numbers,\" you can display the following customized error message:
        
                    Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers. 
        
                  - **DefaultValue** *(string) --* 
        
                    A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.
        
                  - **Description** *(string) --* 
        
                    A string of up to 4,000 characters that describes the parameter.
        
                  - **MaxLength** *(integer) --* 
        
                    An integer value that determines the largest number of characters that you want to allow for String types.
        
                  - **MaxValue** *(integer) --* 
        
                    A numeric value that determines the largest numeric value that you want to allow for Number types.
        
                  - **MinLength** *(integer) --* 
        
                    An integer value that determines the smallest number of characters that you want to allow for String types.
        
                  - **MinValue** *(integer) --* 
        
                    A numeric value that determines the smallest numeric value that you want to allow for Number types.
        
                  - **Name** *(string) --* 
        
                    The name of the parameter.
        
                  - **NoEcho** *(boolean) --* 
        
                    Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*****).
        
                  - **ReferencedByResources** *(list) --* 
        
                    A list of AWS SAM resources that use this parameter.
        
                    - *(string) --* 
                
                  - **Type** *(string) --* 
        
                    The type of the parameter.
        
                    Valid values: String | Number | List<Number> | CommaDelimitedList 
        
                    String: A literal string.
        
                    For example, users can specify \"MyUserName\".
        
                    Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.
        
                    For example, users might specify \"8888\".
        
                    List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.
        
                    For example, users might specify \"80,20\", and then Ref results in [\"80\",\"20\"].
        
                    CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.
        
                    For example, users might specify \"test,dev,prod\", and then Ref results in [\"test\",\"dev\",\"prod\"].
        
              - **RequiredCapabilities** *(list) --* 
        
                A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
        
                The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, and CAPABILITY_RESOURCE_POLICY.
        
                The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: `AWS\:\:IAM\:\:Group <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__ , `AWS\:\:IAM\:\:InstanceProfile <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__ , `AWS\:\:IAM\:\:Policy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html>`__ , and `AWS\:\:IAM\:\:Role <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__ . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
        
                The following resources require you to specify CAPABILITY_RESOURCE_POLICY: `AWS\:\:ApplicationAutoScaling\:\:ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__ , `AWS\:\:S3\:\:BucketPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__ , `AWS\:\:SQS\:\:QueuePolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__ , and `AWS\:\:SNS\:TopicPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__ .
        
                If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.
        
                Valid values: CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_RESOURCE_POLICY
        
                - *(string) --* 
            
              - **ResourcesSupported** *(boolean) --* 
        
                Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.
        
              - **SemanticVersion** *(string) --* 
        
                The semantic version of the application:
        
                 `https\://semver.org/ <https://semver.org/>`__  
        
              - **SourceCodeUrl** *(string) --* 
        
                A link to a public repository for the source code of your application.
        
              - **TemplateUrl** *(string) --* 
        
                A link to the packaged AWS SAM template of your application.
        
        """
        pass

    def get_application_policy(self, ApplicationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/GetApplicationPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_application_policy(
              ApplicationId=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Statements\': [
                    {
                        \'Actions\': [
                            \'string\',
                        ],
                        \'Principals\': [
                            \'string\',
                        ],
                        \'StatementId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **Statements** *(list) --* 
        
              An array of policy statements applied to the application.
        
              - *(dict) --* 
        
                Policy statement applied to the application.
        
                - **Actions** *(list) --* 
        
                  For the list of actions supported for this operation, see `Application Permissions <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__ .
        
                  - *(string) --* 
              
                - **Principals** *(list) --* 
        
                  An AWS account ID, or * to make the application public.
        
                  - *(string) --* 
              
                - **StatementId** *(string) --* 
        
                  A unique ID for the statement.
        
        """
        pass

    def get_cloud_formation_template(self, ApplicationId: str, TemplateId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/GetCloudFormationTemplate>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_cloud_formation_template(
              ApplicationId=\'string\',
              TemplateId=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :type TemplateId: string
        :param TemplateId: **[REQUIRED]** 
        
          The UUID returned by CreateCloudFormationTemplate.
        
          Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ApplicationId\': \'string\',
                \'CreationTime\': \'string\',
                \'ExpirationTime\': \'string\',
                \'SemanticVersion\': \'string\',
                \'Status\': \'PREPARING\'|\'ACTIVE\'|\'EXPIRED\',
                \'TemplateId\': \'string\',
                \'TemplateUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **ApplicationId** *(string) --* 
        
              The application Amazon Resource Name (ARN).
        
            - **CreationTime** *(string) --* 
        
              The date and time this resource was created.
        
            - **ExpirationTime** *(string) --* 
        
              The date and time this template expires. Templates expire 1 hour after creation.
        
            - **SemanticVersion** *(string) --* 
        
              The semantic version of the application:
        
               `https\://semver.org/ <https://semver.org/>`__  
        
            - **Status** *(string) --* 
        
              Status of the template creation workflow.
        
              Possible values: PREPARING | ACTIVE | EXPIRED
        
            - **TemplateId** *(string) --* 
        
              The UUID returned by CreateCloudFormationTemplate.
        
              Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}
        
            - **TemplateUrl** *(string) --* 
        
              A link to the template that can be used to deploy the application using AWS CloudFormation.
        
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

    def list_application_versions(self, ApplicationId: str, MaxItems: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/ListApplicationVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_application_versions(
              ApplicationId=\'string\',
              MaxItems=123,
              NextToken=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :type MaxItems: integer
        :param MaxItems: 
        
          The total number of items to return.
        
        :type NextToken: string
        :param NextToken: 
        
          A token to specify where to start paginating.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Versions\': [
                    {
                        \'ApplicationId\': \'string\',
                        \'CreationTime\': \'string\',
                        \'SemanticVersion\': \'string\',
                        \'SourceCodeUrl\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **NextToken** *(string) --* 
        
              The token to request the next page of results.
        
            - **Versions** *(list) --* 
        
              An array of version summaries for the application.
        
              - *(dict) --* 
        
                An application version summary.
        
                - **ApplicationId** *(string) --* 
        
                  The application Amazon Resource Name (ARN).
        
                - **CreationTime** *(string) --* 
        
                  The date and time this resource was created.
        
                - **SemanticVersion** *(string) --* 
        
                  The semantic version of the application:
        
                   `https\://semver.org/ <https://semver.org/>`__  
        
                - **SourceCodeUrl** *(string) --* 
        
                  A link to a public repository for the source code of your application.
        
        """
        pass

    def list_applications(self, MaxItems: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/ListApplications>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_applications(
              MaxItems=123,
              NextToken=\'string\'
          )
        :type MaxItems: integer
        :param MaxItems: 
        
          The total number of items to return.
        
        :type NextToken: string
        :param NextToken: 
        
          A token to specify where to start paginating.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Applications\': [
                    {
                        \'ApplicationId\': \'string\',
                        \'Author\': \'string\',
                        \'CreationTime\': \'string\',
                        \'Description\': \'string\',
                        \'HomePageUrl\': \'string\',
                        \'Labels\': [
                            \'string\',
                        ],
                        \'Name\': \'string\',
                        \'SpdxLicenseId\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **Applications** *(list) --* 
        
              An array of application summaries.
        
              - *(dict) --* 
        
                Summary of details about the application.
        
                - **ApplicationId** *(string) --* 
        
                  The application Amazon Resource Name (ARN).
        
                - **Author** *(string) --* 
        
                  The name of the author publishing the app.
        
                  Minimum length=1. Maximum length=127.
        
                  Pattern \"^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\";
        
                - **CreationTime** *(string) --* 
        
                  The date and time this resource was created.
        
                - **Description** *(string) --* 
        
                  The description of the application.
        
                  Minimum length=1. Maximum length=256
        
                - **HomePageUrl** *(string) --* 
        
                  A URL with more information about the application, for example the location of your GitHub repository for the application.
        
                - **Labels** *(list) --* 
        
                  Labels to improve discovery of apps in search results.
        
                  Minimum length=1. Maximum length=127. Maximum number of labels: 10
        
                  Pattern: \"^[a-zA-Z0-9+\\-_:\\/@]+$\";
        
                  - *(string) --* 
              
                - **Name** *(string) --* 
        
                  The name of the application.
        
                  Minimum length=1. Maximum length=140
        
                  Pattern: \"[a-zA-Z0-9\\-]+\";
        
                - **SpdxLicenseId** *(string) --* 
        
                  A valid identifier from `https\://spdx.org/licenses/ <https://spdx.org/licenses/>`__ .
        
            - **NextToken** *(string) --* 
        
              The token to request the next page of results.
        
        """
        pass

    def put_application_policy(self, ApplicationId: str, Statements: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/PutApplicationPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_application_policy(
              ApplicationId=\'string\',
              Statements=[
                  {
                      \'Actions\': [
                          \'string\',
                      ],
                      \'Principals\': [
                          \'string\',
                      ],
                      \'StatementId\': \'string\'
                  },
              ]
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :type Statements: list
        :param Statements: **[REQUIRED]** 
        
          An array of policy statements applied to the application.
        
          - *(dict) --* 
        
            Policy statement applied to the application.
        
            - **Actions** *(list) --* **[REQUIRED]** 
        
              For the list of actions supported for this operation, see `Application Permissions <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__ .
        
              - *(string) --* 
        
            - **Principals** *(list) --* **[REQUIRED]** 
        
              An AWS account ID, or * to make the application public.
        
              - *(string) --* 
        
            - **StatementId** *(string) --* 
        
              A unique ID for the statement.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Statements\': [
                    {
                        \'Actions\': [
                            \'string\',
                        ],
                        \'Principals\': [
                            \'string\',
                        ],
                        \'StatementId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **Statements** *(list) --* 
        
              An array of policy statements applied to the application.
        
              - *(dict) --* 
        
                Policy statement applied to the application.
        
                - **Actions** *(list) --* 
        
                  For the list of actions supported for this operation, see `Application Permissions <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__ .
        
                  - *(string) --* 
              
                - **Principals** *(list) --* 
        
                  An AWS account ID, or * to make the application public.
        
                  - *(string) --* 
              
                - **StatementId** *(string) --* 
        
                  A unique ID for the statement.
        
        """
        pass

    def update_application(self, ApplicationId: str, Author: str = None, Description: str = None, HomePageUrl: str = None, Labels: List = None, ReadmeBody: str = None, ReadmeUrl: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/UpdateApplication>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_application(
              ApplicationId=\'string\',
              Author=\'string\',
              Description=\'string\',
              HomePageUrl=\'string\',
              Labels=[
                  \'string\',
              ],
              ReadmeBody=\'string\',
              ReadmeUrl=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the application.
        
        :type Author: string
        :param Author: 
        
          The name of the author publishing the app.
        
          Minimum length=1. Maximum length=127.
        
          Pattern \"^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\";
        
        :type Description: string
        :param Description: 
        
          The description of the application.
        
          Minimum length=1. Maximum length=256
        
        :type HomePageUrl: string
        :param HomePageUrl: 
        
          A URL with more information about the application, for example the location of your GitHub repository for the application.
        
        :type Labels: list
        :param Labels: 
        
          Labels to improve discovery of apps in search results.
        
          Minimum length=1. Maximum length=127. Maximum number of labels: 10
        
          Pattern: \"^[a-zA-Z0-9+\\-_:\\/@]+$\";
        
          - *(string) --* 
        
        :type ReadmeBody: string
        :param ReadmeBody: 
        
          A text readme file in Markdown language that contains a more detailed description of the application and how it works.
        
          Maximum size 5 MB
        
        :type ReadmeUrl: string
        :param ReadmeUrl: 
        
          A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.
        
          Maximum size 5 MB
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ApplicationId\': \'string\',
                \'Author\': \'string\',
                \'CreationTime\': \'string\',
                \'Description\': \'string\',
                \'HomePageUrl\': \'string\',
                \'Labels\': [
                    \'string\',
                ],
                \'LicenseUrl\': \'string\',
                \'Name\': \'string\',
                \'ReadmeUrl\': \'string\',
                \'SpdxLicenseId\': \'string\',
                \'Version\': {
                    \'ApplicationId\': \'string\',
                    \'CreationTime\': \'string\',
                    \'ParameterDefinitions\': [
                        {
                            \'AllowedPattern\': \'string\',
                            \'AllowedValues\': [
                                \'string\',
                            ],
                            \'ConstraintDescription\': \'string\',
                            \'DefaultValue\': \'string\',
                            \'Description\': \'string\',
                            \'MaxLength\': 123,
                            \'MaxValue\': 123,
                            \'MinLength\': 123,
                            \'MinValue\': 123,
                            \'Name\': \'string\',
                            \'NoEcho\': True|False,
                            \'ReferencedByResources\': [
                                \'string\',
                            ],
                            \'Type\': \'string\'
                        },
                    ],
                    \'RequiredCapabilities\': [
                        \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\'|\'CAPABILITY_AUTO_EXPAND\'|\'CAPABILITY_RESOURCE_POLICY\',
                    ],
                    \'ResourcesSupported\': True|False,
                    \'SemanticVersion\': \'string\',
                    \'SourceCodeUrl\': \'string\',
                    \'TemplateUrl\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Success
        
            - **ApplicationId** *(string) --* 
        
              The application Amazon Resource Name (ARN).
        
            - **Author** *(string) --* 
        
              The name of the author publishing the app.
        
              Minimum length=1. Maximum length=127.
        
              Pattern \"^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\";
        
            - **CreationTime** *(string) --* 
        
              The date and time this resource was created.
        
            - **Description** *(string) --* 
        
              The description of the application.
        
              Minimum length=1. Maximum length=256
        
            - **HomePageUrl** *(string) --* 
        
              A URL with more information about the application, for example the location of your GitHub repository for the application.
        
            - **Labels** *(list) --* 
        
              Labels to improve discovery of apps in search results.
        
              Minimum length=1. Maximum length=127. Maximum number of labels: 10
        
              Pattern: \"^[a-zA-Z0-9+\\-_:\\/@]+$\";
        
              - *(string) --* 
          
            - **LicenseUrl** *(string) --* 
        
              A link to a license file of the app that matches the spdxLicenseID value of your application.
        
              Maximum size 5 MB
        
            - **Name** *(string) --* 
        
              The name of the application.
        
              Minimum length=1. Maximum length=140
        
              Pattern: \"[a-zA-Z0-9\\-]+\";
        
            - **ReadmeUrl** *(string) --* 
        
              A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.
        
              Maximum size 5 MB
        
            - **SpdxLicenseId** *(string) --* 
        
              A valid identifier from https://spdx.org/licenses/.
        
            - **Version** *(dict) --* 
        
              Version information about the application.
        
              - **ApplicationId** *(string) --* 
        
                The application Amazon Resource Name (ARN).
        
              - **CreationTime** *(string) --* 
        
                The date and time this resource was created.
        
              - **ParameterDefinitions** *(list) --* 
        
                An array of parameter types supported by the application.
        
                - *(dict) --* 
        
                  Parameters supported by the application.
        
                  - **AllowedPattern** *(string) --* 
        
                    A regular expression that represents the patterns to allow for String types.
        
                  - **AllowedValues** *(list) --* 
        
                    An array containing the list of values allowed for the parameter.
        
                    - *(string) --* 
                
                  - **ConstraintDescription** *(string) --* 
        
                    A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:
        
                    Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ 
        
                    By adding a constraint description, such as \"must contain only uppercase and lowercase letters and numbers,\" you can display the following customized error message:
        
                    Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers. 
        
                  - **DefaultValue** *(string) --* 
        
                    A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.
        
                  - **Description** *(string) --* 
        
                    A string of up to 4,000 characters that describes the parameter.
        
                  - **MaxLength** *(integer) --* 
        
                    An integer value that determines the largest number of characters that you want to allow for String types.
        
                  - **MaxValue** *(integer) --* 
        
                    A numeric value that determines the largest numeric value that you want to allow for Number types.
        
                  - **MinLength** *(integer) --* 
        
                    An integer value that determines the smallest number of characters that you want to allow for String types.
        
                  - **MinValue** *(integer) --* 
        
                    A numeric value that determines the smallest numeric value that you want to allow for Number types.
        
                  - **Name** *(string) --* 
        
                    The name of the parameter.
        
                  - **NoEcho** *(boolean) --* 
        
                    Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*****).
        
                  - **ReferencedByResources** *(list) --* 
        
                    A list of AWS SAM resources that use this parameter.
        
                    - *(string) --* 
                
                  - **Type** *(string) --* 
        
                    The type of the parameter.
        
                    Valid values: String | Number | List<Number> | CommaDelimitedList 
        
                    String: A literal string.
        
                    For example, users can specify \"MyUserName\".
        
                    Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.
        
                    For example, users might specify \"8888\".
        
                    List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.
        
                    For example, users might specify \"80,20\", and then Ref results in [\"80\",\"20\"].
        
                    CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.
        
                    For example, users might specify \"test,dev,prod\", and then Ref results in [\"test\",\"dev\",\"prod\"].
        
              - **RequiredCapabilities** *(list) --* 
        
                A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
        
                The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, and CAPABILITY_RESOURCE_POLICY.
        
                The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: `AWS\:\:IAM\:\:Group <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__ , `AWS\:\:IAM\:\:InstanceProfile <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__ , `AWS\:\:IAM\:\:Policy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html>`__ , and `AWS\:\:IAM\:\:Role <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__ . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
        
                The following resources require you to specify CAPABILITY_RESOURCE_POLICY: `AWS\:\:ApplicationAutoScaling\:\:ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__ , `AWS\:\:S3\:\:BucketPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html>`__ , `AWS\:\:SQS\:\:QueuePolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html>`__ , and `AWS\:\:SNS\:TopicPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html>`__ .
        
                If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.
        
                Valid values: CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_RESOURCE_POLICY
        
                - *(string) --* 
            
              - **ResourcesSupported** *(boolean) --* 
        
                Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.
        
              - **SemanticVersion** *(string) --* 
        
                The semantic version of the application:
        
                 `https\://semver.org/ <https://semver.org/>`__  
        
              - **SourceCodeUrl** *(string) --* 
        
                A link to a public repository for the source code of your application.
        
              - **TemplateUrl** *(string) --* 
        
                A link to the packaged AWS SAM template of your application.
        
        """
        pass
