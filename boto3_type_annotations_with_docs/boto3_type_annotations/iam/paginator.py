from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetAccountAuthorizationDetails(Paginator):
    def paginate(self, Filter: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetAccountAuthorizationDetails>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filter=[
                  \'User\'|\'Role\'|\'Group\'|\'LocalManagedPolicy\'|\'AWSManagedPolicy\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filter: list
        :param Filter: 
        
          A list of entity types used to filter the results. Only the entities that match the types you specify are included in the output. Use the value ``LocalManagedPolicy`` to include customer managed policies.
        
          The format for this parameter is a comma-separated (if more than one) list of strings. Each string value in the list must be one of the valid values listed below.
        
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
                \'UserDetailList\': [
                    {
                        \'Path\': \'string\',
                        \'UserName\': \'string\',
                        \'UserId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'UserPolicyList\': [
                            {
                                \'PolicyName\': \'string\',
                                \'PolicyDocument\': \'string\'
                            },
                        ],
                        \'GroupList\': [
                            \'string\',
                        ],
                        \'AttachedManagedPolicies\': [
                            {
                                \'PolicyName\': \'string\',
                                \'PolicyArn\': \'string\'
                            },
                        ],
                        \'PermissionsBoundary\': {
                            \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                            \'PermissionsBoundaryArn\': \'string\'
                        }
                    },
                ],
                \'GroupDetailList\': [
                    {
                        \'Path\': \'string\',
                        \'GroupName\': \'string\',
                        \'GroupId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'GroupPolicyList\': [
                            {
                                \'PolicyName\': \'string\',
                                \'PolicyDocument\': \'string\'
                            },
                        ],
                        \'AttachedManagedPolicies\': [
                            {
                                \'PolicyName\': \'string\',
                                \'PolicyArn\': \'string\'
                            },
                        ]
                    },
                ],
                \'RoleDetailList\': [
                    {
                        \'Path\': \'string\',
                        \'RoleName\': \'string\',
                        \'RoleId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'AssumeRolePolicyDocument\': \'string\',
                        \'InstanceProfileList\': [
                            {
                                \'Path\': \'string\',
                                \'InstanceProfileName\': \'string\',
                                \'InstanceProfileId\': \'string\',
                                \'Arn\': \'string\',
                                \'CreateDate\': datetime(2015, 1, 1),
                                \'Roles\': [
                                    {
                                        \'Path\': \'string\',
                                        \'RoleName\': \'string\',
                                        \'RoleId\': \'string\',
                                        \'Arn\': \'string\',
                                        \'CreateDate\': datetime(2015, 1, 1),
                                        \'AssumeRolePolicyDocument\': \'string\',
                                        \'Description\': \'string\',
                                        \'MaxSessionDuration\': 123,
                                        \'PermissionsBoundary\': {
                                            \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                                            \'PermissionsBoundaryArn\': \'string\'
                                        }
                                    },
                                ]
                            },
                        ],
                        \'RolePolicyList\': [
                            {
                                \'PolicyName\': \'string\',
                                \'PolicyDocument\': \'string\'
                            },
                        ],
                        \'AttachedManagedPolicies\': [
                            {
                                \'PolicyName\': \'string\',
                                \'PolicyArn\': \'string\'
                            },
                        ],
                        \'PermissionsBoundary\': {
                            \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                            \'PermissionsBoundaryArn\': \'string\'
                        }
                    },
                ],
                \'Policies\': [
                    {
                        \'PolicyName\': \'string\',
                        \'PolicyId\': \'string\',
                        \'Arn\': \'string\',
                        \'Path\': \'string\',
                        \'DefaultVersionId\': \'string\',
                        \'AttachmentCount\': 123,
                        \'PermissionsBoundaryUsageCount\': 123,
                        \'IsAttachable\': True|False,
                        \'Description\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'UpdateDate\': datetime(2015, 1, 1),
                        \'PolicyVersionList\': [
                            {
                                \'Document\': \'string\',
                                \'VersionId\': \'string\',
                                \'IsDefaultVersion\': True|False,
                                \'CreateDate\': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  GetAccountAuthorizationDetails request. 
        
            - **UserDetailList** *(list) --* 
        
              A list containing information about IAM users.
        
              - *(dict) --* 
        
                Contains information about an IAM user, including all the user\'s policies and all the IAM groups the user is in.
        
                This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
        
                - **Path** *(string) --* 
        
                  The path to the user. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **UserName** *(string) --* 
        
                  The friendly name identifying the user.
        
                - **UserId** *(string) --* 
        
                  The stable and unique string identifying the user. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                  For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the user was created.
        
                - **UserPolicyList** *(list) --* 
        
                  A list of the inline policies embedded in the user.
        
                  - *(dict) --* 
        
                    Contains information about an IAM policy, including the policy document.
        
                    This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
        
                    - **PolicyName** *(string) --* 
        
                      The name of the policy.
        
                    - **PolicyDocument** *(string) --* 
        
                      The policy document.
        
                - **GroupList** *(list) --* 
        
                  A list of IAM groups that the user is in.
        
                  - *(string) --* 
              
                - **AttachedManagedPolicies** *(list) --* 
        
                  A list of the managed policies attached to the user.
        
                  - *(dict) --* 
        
                    Contains information about an attached policy.
        
                    An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations. 
        
                    For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                    - **PolicyName** *(string) --* 
        
                      The friendly name of the attached policy.
        
                    - **PolicyArn** *(string) --* 
        
                      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
                - **PermissionsBoundary** *(dict) --* 
        
                  The ARN of the policy used to set the permissions boundary for the user.
        
                  For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                  - **PermissionsBoundaryType** *(string) --* 
        
                    The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                  - **PermissionsBoundaryArn** *(string) --* 
        
                    The ARN of the policy used to set the permissions boundary for the user or role.
        
            - **GroupDetailList** *(list) --* 
        
              A list containing information about IAM groups.
        
              - *(dict) --* 
        
                Contains information about an IAM group, including all of the group\'s policies.
        
                This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
        
                - **Path** *(string) --* 
        
                  The path to the group. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **GroupName** *(string) --* 
        
                  The friendly name that identifies the group.
        
                - **GroupId** *(string) --* 
        
                  The stable and unique string identifying the group. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                  For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the group was created.
        
                - **GroupPolicyList** *(list) --* 
        
                  A list of the inline policies embedded in the group.
        
                  - *(dict) --* 
        
                    Contains information about an IAM policy, including the policy document.
        
                    This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
        
                    - **PolicyName** *(string) --* 
        
                      The name of the policy.
        
                    - **PolicyDocument** *(string) --* 
        
                      The policy document.
        
                - **AttachedManagedPolicies** *(list) --* 
        
                  A list of the managed policies attached to the group.
        
                  - *(dict) --* 
        
                    Contains information about an attached policy.
        
                    An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations. 
        
                    For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                    - **PolicyName** *(string) --* 
        
                      The friendly name of the attached policy.
        
                    - **PolicyArn** *(string) --* 
        
                      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
            - **RoleDetailList** *(list) --* 
        
              A list containing information about IAM roles.
        
              - *(dict) --* 
        
                Contains information about an IAM role, including all of the role\'s policies.
        
                This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
        
                - **Path** *(string) --* 
        
                  The path to the role. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **RoleName** *(string) --* 
        
                  The friendly name that identifies the role.
        
                - **RoleId** *(string) --* 
        
                  The stable and unique string identifying the role. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                  For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the role was created.
        
                - **AssumeRolePolicyDocument** *(string) --* 
        
                  The trust policy that grants permission to assume the role.
        
                - **InstanceProfileList** *(list) --* 
        
                  A list of instance profiles that contain this role.
        
                  - *(dict) --* 
        
                    Contains information about an instance profile.
        
                    This data type is used as a response element in the following operations:
        
                    *  CreateInstanceProfile   
                     
                    *  GetInstanceProfile   
                     
                    *  ListInstanceProfiles   
                     
                    *  ListInstanceProfilesForRole   
                     
                    - **Path** *(string) --* 
        
                      The path to the instance profile. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                    - **InstanceProfileName** *(string) --* 
        
                      The name identifying the instance profile.
        
                    - **InstanceProfileId** *(string) --* 
        
                      The stable and unique string identifying the instance profile. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                    - **Arn** *(string) --* 
        
                      The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                    - **CreateDate** *(datetime) --* 
        
                      The date when the instance profile was created.
        
                    - **Roles** *(list) --* 
        
                      The role associated with the instance profile.
        
                      - *(dict) --* 
        
                        Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.
        
                        - **Path** *(string) --* 
        
                          The path to the role. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                        - **RoleName** *(string) --* 
        
                          The friendly name that identifies the role.
        
                        - **RoleId** *(string) --* 
        
                          The stable and unique string identifying the role. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                        - **Arn** *(string) --* 
        
                          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM User Guide* guide. 
        
                        - **CreateDate** *(datetime) --* 
        
                          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the role was created.
        
                        - **AssumeRolePolicyDocument** *(string) --* 
        
                          The policy that grants an entity permission to assume the role.
        
                        - **Description** *(string) --* 
        
                          A description of the role that you provide.
        
                        - **MaxSessionDuration** *(integer) --* 
        
                          The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI or API to assume the role can specify the duration using the optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.
        
                        - **PermissionsBoundary** *(dict) --* 
        
                          The ARN of the policy used to set the permissions boundary for the role.
        
                          For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                          - **PermissionsBoundaryType** *(string) --* 
        
                            The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                          - **PermissionsBoundaryArn** *(string) --* 
        
                            The ARN of the policy used to set the permissions boundary for the user or role.
        
                - **RolePolicyList** *(list) --* 
        
                  A list of inline policies embedded in the role. These policies are the role\'s access (permissions) policies.
        
                  - *(dict) --* 
        
                    Contains information about an IAM policy, including the policy document.
        
                    This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
        
                    - **PolicyName** *(string) --* 
        
                      The name of the policy.
        
                    - **PolicyDocument** *(string) --* 
        
                      The policy document.
        
                - **AttachedManagedPolicies** *(list) --* 
        
                  A list of managed policies attached to the role. These policies are the role\'s access (permissions) policies.
        
                  - *(dict) --* 
        
                    Contains information about an attached policy.
        
                    An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations. 
        
                    For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                    - **PolicyName** *(string) --* 
        
                      The friendly name of the attached policy.
        
                    - **PolicyArn** *(string) --* 
        
                      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
                - **PermissionsBoundary** *(dict) --* 
        
                  The ARN of the policy used to set the permissions boundary for the role.
        
                  For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                  - **PermissionsBoundaryType** *(string) --* 
        
                    The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                  - **PermissionsBoundaryArn** *(string) --* 
        
                    The ARN of the policy used to set the permissions boundary for the user or role.
        
            - **Policies** *(list) --* 
        
              A list containing information about managed policies.
        
              - *(dict) --* 
        
                Contains information about a managed policy, including the policy\'s ARN, versions, and the number of principal entities (users, groups, and roles) that the policy is attached to.
        
                This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
        
                For more information about managed policies, see `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **PolicyName** *(string) --* 
        
                  The friendly name (not ARN) identifying the policy.
        
                - **PolicyId** *(string) --* 
        
                  The stable and unique string identifying the policy.
        
                  For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                  For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
                - **Path** *(string) --* 
        
                  The path to the policy.
        
                  For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **DefaultVersionId** *(string) --* 
        
                  The identifier for the version of the policy that is set as the default (operative) version.
        
                  For more information about policy versions, see `Versioning for Managed Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the *Using IAM* guide. 
        
                - **AttachmentCount** *(integer) --* 
        
                  The number of principal entities (users, groups, and roles) that the policy is attached to.
        
                - **PermissionsBoundaryUsageCount** *(integer) --* 
        
                  The number of entities (users and roles) for which the policy is used as the permissions boundary. 
        
                  For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                - **IsAttachable** *(boolean) --* 
        
                  Specifies whether the policy can be attached to an IAM user, group, or role.
        
                - **Description** *(string) --* 
        
                  A friendly description of the policy.
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the policy was created.
        
                - **UpdateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the policy was last updated.
        
                  When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.
        
                - **PolicyVersionList** *(list) --* 
        
                  A list containing information about the versions of the policy.
        
                  - *(dict) --* 
        
                    Contains information about a version of a managed policy.
        
                    This data type is used as a response element in the  CreatePolicyVersion ,  GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations. 
        
                    For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                    - **Document** *(string) --* 
        
                      The policy document.
        
                      The policy document is returned in the response to the  GetPolicyVersion and  GetAccountAuthorizationDetails operations. It is not returned in the response to the  CreatePolicyVersion or  ListPolicyVersions operations. 
        
                      The policy document returned in this structure is URL-encoded compliant with `RFC 3986 <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and SDKs provide similar functionality.
        
                    - **VersionId** *(string) --* 
        
                      The identifier for the policy version.
        
                      Policy version identifiers always begin with ``v`` (always lowercase). When a policy is created, the first policy version is ``v1`` . 
        
                    - **IsDefaultVersion** *(boolean) --* 
        
                      Specifies whether the policy version is set as the policy\'s default version.
        
                    - **CreateDate** *(datetime) --* 
        
                      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the policy version was created.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetGroup(Paginator):
    def paginate(self, GroupName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetGroup>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              GroupName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the group.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'Group\': {
                    \'Path\': \'string\',
                    \'GroupName\': \'string\',
                    \'GroupId\': \'string\',
                    \'Arn\': \'string\',
                    \'CreateDate\': datetime(2015, 1, 1)
                },
                \'Users\': [
                    {
                        \'Path\': \'string\',
                        \'UserName\': \'string\',
                        \'UserId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'PasswordLastUsed\': datetime(2015, 1, 1),
                        \'PermissionsBoundary\': {
                            \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                            \'PermissionsBoundaryArn\': \'string\'
                        }
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  GetGroup request. 
        
            - **Group** *(dict) --* 
        
              A structure that contains details about the group.
        
              - **Path** *(string) --* 
        
                The path to the group. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
              - **GroupName** *(string) --* 
        
                The friendly name that identifies the group.
        
              - **GroupId** *(string) --* 
        
                The stable and unique string identifying the group. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
              - **CreateDate** *(datetime) --* 
        
                The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the group was created.
        
            - **Users** *(list) --* 
        
              A list of users in the group.
        
              - *(dict) --* 
        
                Contains information about an IAM user entity.
        
                This data type is used as a response element in the following operations:
        
                *  CreateUser   
                 
                *  GetUser   
                 
                *  ListUsers   
                 
                - **Path** *(string) --* 
        
                  The path to the user. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **UserName** *(string) --* 
        
                  The friendly name identifying the user.
        
                - **UserId** *(string) --* 
        
                  The stable and unique string identifying the user. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the user was created.
        
                - **PasswordLastUsed** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the `Credential Reports <http://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in the *Using IAM* guide. If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value) then it indicates that they never signed in with a password. This can be because:
        
                  * The user never had a password. 
                   
                  * A password exists but has not been used since IAM started tracking this information on October 20th, 2014. 
                   
                  A null does not mean that the user *never* had a password. Also, if the user does not currently have a password, but had one in the past, then this field contains the date and time the most recent password was used.
        
                  This value is returned only in the  GetUser and  ListUsers operations. 
        
                - **PermissionsBoundary** *(dict) --* 
        
                  The ARN of the policy used to set the permissions boundary for the user.
        
                  For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                  - **PermissionsBoundaryType** *(string) --* 
        
                    The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                  - **PermissionsBoundaryArn** *(string) --* 
        
                    The ARN of the policy used to set the permissions boundary for the user or role.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListAccessKeys(Paginator):
    def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              UserName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type UserName: string
        :param UserName: 
        
          The name of the user.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'AccessKeyMetadata\': [
                    {
                        \'UserName\': \'string\',
                        \'AccessKeyId\': \'string\',
                        \'Status\': \'Active\'|\'Inactive\',
                        \'CreateDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListAccessKeys request. 
        
            - **AccessKeyMetadata** *(list) --* 
        
              A list of objects containing metadata about the access keys.
        
              - *(dict) --* 
        
                Contains information about an AWS access key, without its secret key.
        
                This data type is used as a response element in the  ListAccessKeys operation.
        
                - **UserName** *(string) --* 
        
                  The name of the IAM user that the key is associated with.
        
                - **AccessKeyId** *(string) --* 
        
                  The ID for this access key.
        
                - **Status** *(string) --* 
        
                  The status of the access key. ``Active`` means the key is valid for API calls; ``Inactive`` means it is not.
        
                - **CreateDate** *(datetime) --* 
        
                  The date when the access key was created.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListAccountAliases(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccountAliases>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'AccountAliases\': [
                    \'string\',
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListAccountAliases request. 
        
            - **AccountAliases** *(list) --* 
        
              A list of aliases associated with the account. AWS supports only one alias per account.
        
              - *(string) --* 
          
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListAttachedGroupPolicies(Paginator):
    def paginate(self, GroupName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedGroupPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              GroupName=\'string\',
              PathPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name (friendly name, not ARN) of the group to list attached policies for.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
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
                \'AttachedPolicies\': [
                    {
                        \'PolicyName\': \'string\',
                        \'PolicyArn\': \'string\'
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListAttachedGroupPolicies request. 
        
            - **AttachedPolicies** *(list) --* 
        
              A list of the attached policies.
        
              - *(dict) --* 
        
                Contains information about an attached policy.
        
                An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations. 
        
                For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **PolicyName** *(string) --* 
        
                  The friendly name of the attached policy.
        
                - **PolicyArn** *(string) --* 
        
                  The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                  For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListAttachedRolePolicies(Paginator):
    def paginate(self, RoleName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedRolePolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              RoleName=\'string\',
              PathPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type RoleName: string
        :param RoleName: **[REQUIRED]** 
        
          The name (friendly name, not ARN) of the role to list attached policies for.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
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
                \'AttachedPolicies\': [
                    {
                        \'PolicyName\': \'string\',
                        \'PolicyArn\': \'string\'
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListAttachedRolePolicies request. 
        
            - **AttachedPolicies** *(list) --* 
        
              A list of the attached policies.
        
              - *(dict) --* 
        
                Contains information about an attached policy.
        
                An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations. 
        
                For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **PolicyName** *(string) --* 
        
                  The friendly name of the attached policy.
        
                - **PolicyArn** *(string) --* 
        
                  The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                  For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListAttachedUserPolicies(Paginator):
    def paginate(self, UserName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedUserPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              UserName=\'string\',
              PathPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type UserName: string
        :param UserName: **[REQUIRED]** 
        
          The name (friendly name, not ARN) of the user to list attached policies for.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
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
                \'AttachedPolicies\': [
                    {
                        \'PolicyName\': \'string\',
                        \'PolicyArn\': \'string\'
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListAttachedUserPolicies request. 
        
            - **AttachedPolicies** *(list) --* 
        
              A list of the attached policies.
        
              - *(dict) --* 
        
                Contains information about an attached policy.
        
                An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations. 
        
                For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **PolicyName** *(string) --* 
        
                  The friendly name of the attached policy.
        
                - **PolicyArn** *(string) --* 
        
                  The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                  For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListEntitiesForPolicy(Paginator):
    def paginate(self, PolicyArn: str, EntityFilter: str = None, PathPrefix: str = None, PolicyUsageFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PolicyArn=\'string\',
              EntityFilter=\'User\'|\'Role\'|\'Group\'|\'LocalManagedPolicy\'|\'AWSManagedPolicy\',
              PathPrefix=\'string\',
              PolicyUsageFilter=\'PermissionsPolicy\'|\'PermissionsBoundary\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.
        
          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .
        
        :type EntityFilter: string
        :param EntityFilter: 
        
          The entity type to use for filtering the results.
        
          For example, when ``EntityFilter`` is ``Role`` , only the roles that are attached to the specified policy are returned. This parameter is optional. If it is not included, all attached entities (users, groups, and roles) are returned. The argument for this parameter must be one of the valid values listed below.
        
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all entities.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
        :type PolicyUsageFilter: string
        :param PolicyUsageFilter: 
        
          The policy usage method to use for filtering the results.
        
          To list only permissions policies, set ``PolicyUsageFilter`` to ``PermissionsPolicy`` . To list only the policies used to set permissions boundaries, set the value to ``PermissionsBoundary`` .
        
          This parameter is optional. If it is not included, all policies are returned. 
        
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
                \'PolicyGroups\': [
                    {
                        \'GroupName\': \'string\',
                        \'GroupId\': \'string\'
                    },
                ],
                \'PolicyUsers\': [
                    {
                        \'UserName\': \'string\',
                        \'UserId\': \'string\'
                    },
                ],
                \'PolicyRoles\': [
                    {
                        \'RoleName\': \'string\',
                        \'RoleId\': \'string\'
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListEntitiesForPolicy request. 
        
            - **PolicyGroups** *(list) --* 
        
              A list of IAM groups that the policy is attached to.
        
              - *(dict) --* 
        
                Contains information about a group that a managed policy is attached to.
        
                This data type is used as a response element in the  ListEntitiesForPolicy operation. 
        
                For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **GroupName** *(string) --* 
        
                  The name (friendly name, not ARN) identifying the group.
        
                - **GroupId** *(string) --* 
        
                  The stable and unique string identifying the group. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the *IAM User Guide* .
        
            - **PolicyUsers** *(list) --* 
        
              A list of IAM users that the policy is attached to.
        
              - *(dict) --* 
        
                Contains information about a user that a managed policy is attached to.
        
                This data type is used as a response element in the  ListEntitiesForPolicy operation. 
        
                For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **UserName** *(string) --* 
        
                  The name (friendly name, not ARN) identifying the user.
        
                - **UserId** *(string) --* 
        
                  The stable and unique string identifying the user. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the *IAM User Guide* .
        
            - **PolicyRoles** *(list) --* 
        
              A list of IAM roles that the policy is attached to.
        
              - *(dict) --* 
        
                Contains information about a role that a managed policy is attached to.
        
                This data type is used as a response element in the  ListEntitiesForPolicy operation. 
        
                For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **RoleName** *(string) --* 
        
                  The name (friendly name, not ARN) identifying the role.
        
                - **RoleId** *(string) --* 
        
                  The stable and unique string identifying the role. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the *IAM User Guide* .
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListGroupPolicies(Paginator):
    def paginate(self, GroupName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              GroupName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the group to list policies for.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'PolicyNames\': [
                    \'string\',
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListGroupPolicies request. 
        
            - **PolicyNames** *(list) --* 
        
              A list of policy names.
        
              This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
              - *(string) --* 
          
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListGroups(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PathPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. For example, the prefix ``/division_abc/subdivision_xyz/`` gets all groups whose path starts with ``/division_abc/subdivision_xyz/`` .
        
          This parameter is optional. If it is not included, it defaults to a slash (/), listing all groups. This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
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
                \'Groups\': [
                    {
                        \'Path\': \'string\',
                        \'GroupName\': \'string\',
                        \'GroupId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListGroups request. 
        
            - **Groups** *(list) --* 
        
              A list of groups.
        
              - *(dict) --* 
        
                Contains information about an IAM group entity.
        
                This data type is used as a response element in the following operations:
        
                *  CreateGroup   
                 
                *  GetGroup   
                 
                *  ListGroups   
                 
                - **Path** *(string) --* 
        
                  The path to the group. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **GroupName** *(string) --* 
        
                  The friendly name that identifies the group.
        
                - **GroupId** *(string) --* 
        
                  The stable and unique string identifying the group. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the group was created.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListGroupsForUser(Paginator):
    def paginate(self, UserName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupsForUser>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              UserName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type UserName: string
        :param UserName: **[REQUIRED]** 
        
          The name of the user to list groups for.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'Groups\': [
                    {
                        \'Path\': \'string\',
                        \'GroupName\': \'string\',
                        \'GroupId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListGroupsForUser request. 
        
            - **Groups** *(list) --* 
        
              A list of groups.
        
              - *(dict) --* 
        
                Contains information about an IAM group entity.
        
                This data type is used as a response element in the following operations:
        
                *  CreateGroup   
                 
                *  GetGroup   
                 
                *  ListGroups   
                 
                - **Path** *(string) --* 
        
                  The path to the group. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **GroupName** *(string) --* 
        
                  The friendly name that identifies the group.
        
                - **GroupId** *(string) --* 
        
                  The stable and unique string identifying the group. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the group was created.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListInstanceProfiles(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfiles>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PathPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. For example, the prefix ``/application_abc/component_xyz/`` gets all instance profiles whose path starts with ``/application_abc/component_xyz/`` .
        
          This parameter is optional. If it is not included, it defaults to a slash (/), listing all instance profiles. This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
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
                \'InstanceProfiles\': [
                    {
                        \'Path\': \'string\',
                        \'InstanceProfileName\': \'string\',
                        \'InstanceProfileId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'Roles\': [
                            {
                                \'Path\': \'string\',
                                \'RoleName\': \'string\',
                                \'RoleId\': \'string\',
                                \'Arn\': \'string\',
                                \'CreateDate\': datetime(2015, 1, 1),
                                \'AssumeRolePolicyDocument\': \'string\',
                                \'Description\': \'string\',
                                \'MaxSessionDuration\': 123,
                                \'PermissionsBoundary\': {
                                    \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                                    \'PermissionsBoundaryArn\': \'string\'
                                }
                            },
                        ]
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListInstanceProfiles request. 
        
            - **InstanceProfiles** *(list) --* 
        
              A list of instance profiles.
        
              - *(dict) --* 
        
                Contains information about an instance profile.
        
                This data type is used as a response element in the following operations:
        
                *  CreateInstanceProfile   
                 
                *  GetInstanceProfile   
                 
                *  ListInstanceProfiles   
                 
                *  ListInstanceProfilesForRole   
                 
                - **Path** *(string) --* 
        
                  The path to the instance profile. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **InstanceProfileName** *(string) --* 
        
                  The name identifying the instance profile.
        
                - **InstanceProfileId** *(string) --* 
        
                  The stable and unique string identifying the instance profile. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **CreateDate** *(datetime) --* 
        
                  The date when the instance profile was created.
        
                - **Roles** *(list) --* 
        
                  The role associated with the instance profile.
        
                  - *(dict) --* 
        
                    Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.
        
                    - **Path** *(string) --* 
        
                      The path to the role. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                    - **RoleName** *(string) --* 
        
                      The friendly name that identifies the role.
        
                    - **RoleId** *(string) --* 
        
                      The stable and unique string identifying the role. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                    - **Arn** *(string) --* 
        
                      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM User Guide* guide. 
        
                    - **CreateDate** *(datetime) --* 
        
                      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the role was created.
        
                    - **AssumeRolePolicyDocument** *(string) --* 
        
                      The policy that grants an entity permission to assume the role.
        
                    - **Description** *(string) --* 
        
                      A description of the role that you provide.
        
                    - **MaxSessionDuration** *(integer) --* 
        
                      The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI or API to assume the role can specify the duration using the optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.
        
                    - **PermissionsBoundary** *(dict) --* 
        
                      The ARN of the policy used to set the permissions boundary for the role.
        
                      For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                      - **PermissionsBoundaryType** *(string) --* 
        
                        The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                      - **PermissionsBoundaryArn** *(string) --* 
        
                        The ARN of the policy used to set the permissions boundary for the user or role.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListInstanceProfilesForRole(Paginator):
    def paginate(self, RoleName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfilesForRole>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              RoleName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type RoleName: string
        :param RoleName: **[REQUIRED]** 
        
          The name of the role to list instance profiles for.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'InstanceProfiles\': [
                    {
                        \'Path\': \'string\',
                        \'InstanceProfileName\': \'string\',
                        \'InstanceProfileId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'Roles\': [
                            {
                                \'Path\': \'string\',
                                \'RoleName\': \'string\',
                                \'RoleId\': \'string\',
                                \'Arn\': \'string\',
                                \'CreateDate\': datetime(2015, 1, 1),
                                \'AssumeRolePolicyDocument\': \'string\',
                                \'Description\': \'string\',
                                \'MaxSessionDuration\': 123,
                                \'PermissionsBoundary\': {
                                    \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                                    \'PermissionsBoundaryArn\': \'string\'
                                }
                            },
                        ]
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListInstanceProfilesForRole request. 
        
            - **InstanceProfiles** *(list) --* 
        
              A list of instance profiles.
        
              - *(dict) --* 
        
                Contains information about an instance profile.
        
                This data type is used as a response element in the following operations:
        
                *  CreateInstanceProfile   
                 
                *  GetInstanceProfile   
                 
                *  ListInstanceProfiles   
                 
                *  ListInstanceProfilesForRole   
                 
                - **Path** *(string) --* 
        
                  The path to the instance profile. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **InstanceProfileName** *(string) --* 
        
                  The name identifying the instance profile.
        
                - **InstanceProfileId** *(string) --* 
        
                  The stable and unique string identifying the instance profile. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **CreateDate** *(datetime) --* 
        
                  The date when the instance profile was created.
        
                - **Roles** *(list) --* 
        
                  The role associated with the instance profile.
        
                  - *(dict) --* 
        
                    Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.
        
                    - **Path** *(string) --* 
        
                      The path to the role. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                    - **RoleName** *(string) --* 
        
                      The friendly name that identifies the role.
        
                    - **RoleId** *(string) --* 
        
                      The stable and unique string identifying the role. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                    - **Arn** *(string) --* 
        
                      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM User Guide* guide. 
        
                    - **CreateDate** *(datetime) --* 
        
                      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the role was created.
        
                    - **AssumeRolePolicyDocument** *(string) --* 
        
                      The policy that grants an entity permission to assume the role.
        
                    - **Description** *(string) --* 
        
                      A description of the role that you provide.
        
                    - **MaxSessionDuration** *(integer) --* 
        
                      The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI or API to assume the role can specify the duration using the optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.
        
                    - **PermissionsBoundary** *(dict) --* 
        
                      The ARN of the policy used to set the permissions boundary for the role.
        
                      For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                      - **PermissionsBoundaryType** *(string) --* 
        
                        The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                      - **PermissionsBoundaryArn** *(string) --* 
        
                        The ARN of the policy used to set the permissions boundary for the user or role.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListMFADevices(Paginator):
    def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              UserName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type UserName: string
        :param UserName: 
        
          The name of the user whose MFA devices you want to list.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'MFADevices\': [
                    {
                        \'UserName\': \'string\',
                        \'SerialNumber\': \'string\',
                        \'EnableDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListMFADevices request. 
        
            - **MFADevices** *(list) --* 
        
              A list of MFA devices.
        
              - *(dict) --* 
        
                Contains information about an MFA device.
        
                This data type is used as a response element in the  ListMFADevices operation.
        
                - **UserName** *(string) --* 
        
                  The user with whom the MFA device is associated.
        
                - **SerialNumber** *(string) --* 
        
                  The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.
        
                - **EnableDate** *(datetime) --* 
        
                  The date when the MFA device was enabled for the user.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPolicies(Paginator):
    def paginate(self, Scope: str = None, OnlyAttached: bool = None, PathPrefix: str = None, PolicyUsageFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Scope=\'All\'|\'AWS\'|\'Local\',
              OnlyAttached=True|False,
              PathPrefix=\'string\',
              PolicyUsageFilter=\'PermissionsPolicy\'|\'PermissionsBoundary\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Scope: string
        :param Scope: 
        
          The scope to use for filtering the results.
        
          To list only AWS managed policies, set ``Scope`` to ``AWS`` . To list only the customer managed policies in your AWS account, set ``Scope`` to ``Local`` .
        
          This parameter is optional. If it is not included, or if it is set to ``All`` , all policies are returned.
        
        :type OnlyAttached: boolean
        :param OnlyAttached: 
        
          A flag to filter the results to only the attached policies.
        
          When ``OnlyAttached`` is ``true`` , the returned list contains only the policies that are attached to an IAM user, group, or role. When ``OnlyAttached`` is ``false`` , or when the parameter is not included, all policies are returned.
        
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies. This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
        :type PolicyUsageFilter: string
        :param PolicyUsageFilter: 
        
          The policy usage method to use for filtering the results.
        
          To list only permissions policies, set ``PolicyUsageFilter`` to ``PermissionsPolicy`` . To list only the policies used to set permissions boundaries, set the value to ``PermissionsBoundary`` .
        
          This parameter is optional. If it is not included, all policies are returned. 
        
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
                \'Policies\': [
                    {
                        \'PolicyName\': \'string\',
                        \'PolicyId\': \'string\',
                        \'Arn\': \'string\',
                        \'Path\': \'string\',
                        \'DefaultVersionId\': \'string\',
                        \'AttachmentCount\': 123,
                        \'PermissionsBoundaryUsageCount\': 123,
                        \'IsAttachable\': True|False,
                        \'Description\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'UpdateDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListPolicies request. 
        
            - **Policies** *(list) --* 
        
              A list of policies.
        
              - *(dict) --* 
        
                Contains information about a managed policy.
        
                This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and  ListPolicies operations. 
        
                For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **PolicyName** *(string) --* 
        
                  The friendly name (not ARN) identifying the policy.
        
                - **PolicyId** *(string) --* 
        
                  The stable and unique string identifying the policy.
        
                  For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        
                  For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* . 
        
                - **Path** *(string) --* 
        
                  The path to the policy.
        
                  For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **DefaultVersionId** *(string) --* 
        
                  The identifier for the version of the policy that is set as the default version.
        
                - **AttachmentCount** *(integer) --* 
        
                  The number of entities (users, groups, and roles) that the policy is attached to.
        
                - **PermissionsBoundaryUsageCount** *(integer) --* 
        
                  The number of entities (users and roles) for which the policy is used to set the permissions boundary. 
        
                  For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                - **IsAttachable** *(boolean) --* 
        
                  Specifies whether the policy can be attached to an IAM user, group, or role.
        
                - **Description** *(string) --* 
        
                  A friendly description of the policy.
        
                  This element is included in the response to the  GetPolicy operation. It is not included in the response to the  ListPolicies operation. 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the policy was created.
        
                - **UpdateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the policy was last updated.
        
                  When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPolicyVersions(Paginator):
    def paginate(self, PolicyArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicyVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PolicyArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.
        
          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .
        
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
                \'Versions\': [
                    {
                        \'Document\': \'string\',
                        \'VersionId\': \'string\',
                        \'IsDefaultVersion\': True|False,
                        \'CreateDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListPolicyVersions request. 
        
            - **Versions** *(list) --* 
        
              A list of policy versions.
        
              For more information about managed policy versions, see `Versioning for Managed Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the *IAM User Guide* .
        
              - *(dict) --* 
        
                Contains information about a version of a managed policy.
        
                This data type is used as a response element in the  CreatePolicyVersion ,  GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations. 
        
                For more information about managed policies, refer to `Managed Policies and Inline Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the *Using IAM* guide. 
        
                - **Document** *(string) --* 
        
                  The policy document.
        
                  The policy document is returned in the response to the  GetPolicyVersion and  GetAccountAuthorizationDetails operations. It is not returned in the response to the  CreatePolicyVersion or  ListPolicyVersions operations. 
        
                  The policy document returned in this structure is URL-encoded compliant with `RFC 3986 <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and SDKs provide similar functionality.
        
                - **VersionId** *(string) --* 
        
                  The identifier for the policy version.
        
                  Policy version identifiers always begin with ``v`` (always lowercase). When a policy is created, the first policy version is ``v1`` . 
        
                - **IsDefaultVersion** *(boolean) --* 
        
                  Specifies whether the policy version is set as the policy\'s default version.
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the policy version was created.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListRolePolicies(Paginator):
    def paginate(self, RoleName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRolePolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              RoleName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type RoleName: string
        :param RoleName: **[REQUIRED]** 
        
          The name of the role to list policies for.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'PolicyNames\': [
                    \'string\',
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListRolePolicies request. 
        
            - **PolicyNames** *(list) --* 
        
              A list of policy names.
        
              - *(string) --* 
          
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListRoles(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRoles>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PathPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. For example, the prefix ``/application_abc/component_xyz/`` gets all roles whose path starts with ``/application_abc/component_xyz/`` .
        
          This parameter is optional. If it is not included, it defaults to a slash (/), listing all roles. This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
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
                \'Roles\': [
                    {
                        \'Path\': \'string\',
                        \'RoleName\': \'string\',
                        \'RoleId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'AssumeRolePolicyDocument\': \'string\',
                        \'Description\': \'string\',
                        \'MaxSessionDuration\': 123,
                        \'PermissionsBoundary\': {
                            \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                            \'PermissionsBoundaryArn\': \'string\'
                        }
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListRoles request. 
        
            - **Roles** *(list) --* 
        
              A list of roles.
        
              - *(dict) --* 
        
                Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.
        
                - **Path** *(string) --* 
        
                  The path to the role. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **RoleName** *(string) --* 
        
                  The friendly name that identifies the role.
        
                - **RoleId** *(string) --* 
        
                  The stable and unique string identifying the role. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM User Guide* guide. 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the role was created.
        
                - **AssumeRolePolicyDocument** *(string) --* 
        
                  The policy that grants an entity permission to assume the role.
        
                - **Description** *(string) --* 
        
                  A description of the role that you provide.
        
                - **MaxSessionDuration** *(integer) --* 
        
                  The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI or API to assume the role can specify the duration using the optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.
        
                - **PermissionsBoundary** *(dict) --* 
        
                  The ARN of the policy used to set the permissions boundary for the role.
        
                  For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                  - **PermissionsBoundaryType** *(string) --* 
        
                    The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                  - **PermissionsBoundaryArn** *(string) --* 
        
                    The ARN of the policy used to set the permissions boundary for the user or role.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListSSHPublicKeys(Paginator):
    def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSSHPublicKeys>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              UserName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type UserName: string
        :param UserName: 
        
          The name of the IAM user to list SSH public keys for. If none is specified, the ``UserName`` field is determined implicitly based on the AWS access key used to sign the request.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'SSHPublicKeys\': [
                    {
                        \'UserName\': \'string\',
                        \'SSHPublicKeyId\': \'string\',
                        \'Status\': \'Active\'|\'Inactive\',
                        \'UploadDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListSSHPublicKeys request.
        
            - **SSHPublicKeys** *(list) --* 
        
              A list of the SSH public keys assigned to IAM user.
        
              - *(dict) --* 
        
                Contains information about an SSH public key, without the key\'s body or fingerprint.
        
                This data type is used as a response element in the  ListSSHPublicKeys operation.
        
                - **UserName** *(string) --* 
        
                  The name of the IAM user associated with the SSH public key.
        
                - **SSHPublicKeyId** *(string) --* 
        
                  The unique identifier for the SSH public key.
        
                - **Status** *(string) --* 
        
                  The status of the SSH public key. ``Active`` means that the key can be used for authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot be used.
        
                - **UploadDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the SSH public key was uploaded.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListServerCertificates(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListServerCertificates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PathPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. For example: ``/company/servercerts`` would get all server certificates for which the path starts with ``/company/servercerts`` .
        
          This parameter is optional. If it is not included, it defaults to a slash (/), listing all server certificates. This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
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
                \'ServerCertificateMetadataList\': [
                    {
                        \'Path\': \'string\',
                        \'ServerCertificateName\': \'string\',
                        \'ServerCertificateId\': \'string\',
                        \'Arn\': \'string\',
                        \'UploadDate\': datetime(2015, 1, 1),
                        \'Expiration\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListServerCertificates request. 
        
            - **ServerCertificateMetadataList** *(list) --* 
        
              A list of server certificates.
        
              - *(dict) --* 
        
                Contains information about a server certificate without its certificate body, certificate chain, and private key.
        
                This data type is used as a response element in the  UploadServerCertificate and  ListServerCertificates operations. 
        
                - **Path** *(string) --* 
        
                  The path to the server certificate. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **ServerCertificateName** *(string) --* 
        
                  The name that identifies the server certificate.
        
                - **ServerCertificateId** *(string) --* 
        
                  The stable and unique string identifying the server certificate. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) specifying the server certificate. For more information about ARNs and how to use them in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **UploadDate** *(datetime) --* 
        
                  The date when the server certificate was uploaded.
        
                - **Expiration** *(datetime) --* 
        
                  The date on which the certificate is set to expire.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListSigningCertificates(Paginator):
    def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              UserName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type UserName: string
        :param UserName: 
        
          The name of the IAM user whose signing certificates you want to examine.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'Certificates\': [
                    {
                        \'UserName\': \'string\',
                        \'CertificateId\': \'string\',
                        \'CertificateBody\': \'string\',
                        \'Status\': \'Active\'|\'Inactive\',
                        \'UploadDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListSigningCertificates request. 
        
            - **Certificates** *(list) --* 
        
              A list of the user\'s signing certificate information.
        
              - *(dict) --* 
        
                Contains information about an X.509 signing certificate.
        
                This data type is used as a response element in the  UploadSigningCertificate and  ListSigningCertificates operations. 
        
                - **UserName** *(string) --* 
        
                  The name of the user the signing certificate is associated with.
        
                - **CertificateId** *(string) --* 
        
                  The ID for the signing certificate.
        
                - **CertificateBody** *(string) --* 
        
                  The contents of the signing certificate.
        
                - **Status** *(string) --* 
        
                  The status of the signing certificate. ``Active`` means that the key is valid for API calls, while ``Inactive`` means it is not.
        
                - **UploadDate** *(datetime) --* 
        
                  The date when the signing certificate was uploaded.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListUserPolicies(Paginator):
    def paginate(self, UserName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUserPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              UserName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type UserName: string
        :param UserName: **[REQUIRED]** 
        
          The name of the user to list policies for.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
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
                \'PolicyNames\': [
                    \'string\',
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListUserPolicies request. 
        
            - **PolicyNames** *(list) --* 
        
              A list of policy names.
        
              - *(string) --* 
          
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListUsers(Paginator):
    def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUsers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PathPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PathPrefix: string
        :param PathPrefix: 
        
          The path prefix for filtering the results. For example: ``/division_abc/subdivision_xyz/`` , which would get all user names whose path starts with ``/division_abc/subdivision_xyz/`` .
        
          This parameter is optional. If it is not included, it defaults to a slash (/), listing all user names. This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\u0021) through the DEL character (\u007F), including most punctuation characters, digits, and upper and lowercased letters.
        
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
                \'Users\': [
                    {
                        \'Path\': \'string\',
                        \'UserName\': \'string\',
                        \'UserId\': \'string\',
                        \'Arn\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'PasswordLastUsed\': datetime(2015, 1, 1),
                        \'PermissionsBoundary\': {
                            \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                            \'PermissionsBoundaryArn\': \'string\'
                        }
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListUsers request. 
        
            - **Users** *(list) --* 
        
              A list of users.
        
              - *(dict) --* 
        
                Contains information about an IAM user entity.
        
                This data type is used as a response element in the following operations:
        
                *  CreateUser   
                 
                *  GetUser   
                 
                *  ListUsers   
                 
                - **Path** *(string) --* 
        
                  The path to the user. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **UserName** *(string) --* 
        
                  The friendly name identifying the user.
        
                - **UserId** *(string) --* 
        
                  The stable and unique string identifying the user. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                - **CreateDate** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the user was created.
        
                - **PasswordLastUsed** *(datetime) --* 
        
                  The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the `Credential Reports <http://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in the *Using IAM* guide. If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value) then it indicates that they never signed in with a password. This can be because:
        
                  * The user never had a password. 
                   
                  * A password exists but has not been used since IAM started tracking this information on October 20th, 2014. 
                   
                  A null does not mean that the user *never* had a password. Also, if the user does not currently have a password, but had one in the past, then this field contains the date and time the most recent password was used.
        
                  This value is returned only in the  GetUser and  ListUsers operations. 
        
                - **PermissionsBoundary** *(dict) --* 
        
                  The ARN of the policy used to set the permissions boundary for the user.
        
                  For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                  - **PermissionsBoundaryType** *(string) --* 
        
                    The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                  - **PermissionsBoundaryArn** *(string) --* 
        
                    The ARN of the policy used to set the permissions boundary for the user or role.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListVirtualMFADevices(Paginator):
    def paginate(self, AssignmentStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListVirtualMFADevices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AssignmentStatus=\'Assigned\'|\'Unassigned\'|\'Any\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AssignmentStatus: string
        :param AssignmentStatus: 
        
          The status (``Unassigned`` or ``Assigned`` ) of the devices to list. If you do not specify an ``AssignmentStatus`` , the operation defaults to ``Any`` which lists both assigned and unassigned virtual MFA devices.
        
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
                \'VirtualMFADevices\': [
                    {
                        \'SerialNumber\': \'string\',
                        \'Base32StringSeed\': b\'bytes\',
                        \'QRCodePNG\': b\'bytes\',
                        \'User\': {
                            \'Path\': \'string\',
                            \'UserName\': \'string\',
                            \'UserId\': \'string\',
                            \'Arn\': \'string\',
                            \'CreateDate\': datetime(2015, 1, 1),
                            \'PasswordLastUsed\': datetime(2015, 1, 1),
                            \'PermissionsBoundary\': {
                                \'PermissionsBoundaryType\': \'PermissionsBoundaryPolicy\',
                                \'PermissionsBoundaryArn\': \'string\'
                            }
                        },
                        \'EnableDate\': datetime(2015, 1, 1)
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  ListVirtualMFADevices request. 
        
            - **VirtualMFADevices** *(list) --* 
        
              The list of virtual MFA devices in the current account that match the ``AssignmentStatus`` value that was passed in the request.
        
              - *(dict) --* 
        
                Contains information about a virtual MFA device.
        
                - **SerialNumber** *(string) --* 
        
                  The serial number associated with ``VirtualMFADevice`` .
        
                - **Base32StringSeed** *(bytes) --* 
        
                  The Base32 seed defined as specified in `RFC3548 <https://tools.ietf.org/html/rfc3548.txt>`__ . The ``Base32StringSeed`` is Base64-encoded. 
        
                - **QRCodePNG** *(bytes) --* 
        
                  A QR code PNG image that encodes ``otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String`` where ``$virtualMFADeviceName`` is one of the create call arguments, ``AccountName`` is the user name if set (otherwise, the account ID otherwise), and ``Base32String`` is the seed in Base32 format. The ``Base32String`` value is Base64-encoded. 
        
                - **User** *(dict) --* 
        
                  The IAM user associated with this virtual MFA device.
        
                  - **Path** *(string) --* 
        
                    The path to the user. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                  - **UserName** *(string) --* 
        
                    The friendly name identifying the user.
        
                  - **UserId** *(string) --* 
        
                    The stable and unique string identifying the user. For more information about IDs, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide.
        
                  - **Arn** *(string) --* 
        
                    The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *Using IAM* guide. 
        
                  - **CreateDate** *(datetime) --* 
        
                    The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the user was created.
        
                  - **PasswordLastUsed** *(datetime) --* 
        
                    The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the `Credential Reports <http://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in the *Using IAM* guide. If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value) then it indicates that they never signed in with a password. This can be because:
        
                    * The user never had a password. 
                     
                    * A password exists but has not been used since IAM started tracking this information on October 20th, 2014. 
                     
                    A null does not mean that the user *never* had a password. Also, if the user does not currently have a password, but had one in the past, then this field contains the date and time the most recent password was used.
        
                    This value is returned only in the  GetUser and  ListUsers operations. 
        
                  - **PermissionsBoundary** *(dict) --* 
        
                    The ARN of the policy used to set the permissions boundary for the user.
        
                    For more information about permissions boundaries, see `Permissions Boundaries for IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in the *IAM User Guide* .
        
                    - **PermissionsBoundaryType** *(string) --* 
        
                      The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of ``Policy`` .
        
                    - **PermissionsBoundaryArn** *(string) --* 
        
                      The ARN of the policy used to set the permissions boundary for the user or role.
        
                - **EnableDate** *(datetime) --* 
        
                  The date and time on which the virtual MFA device was enabled.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class SimulateCustomPolicy(Paginator):
    def paginate(self, PolicyInputList: List, ActionNames: List, ResourceArns: List = None, ResourcePolicy: str = None, ResourceOwner: str = None, CallerArn: str = None, ContextEntries: List = None, ResourceHandlingOption: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/SimulateCustomPolicy>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PolicyInputList=[
                  \'string\',
              ],
              ActionNames=[
                  \'string\',
              ],
              ResourceArns=[
                  \'string\',
              ],
              ResourcePolicy=\'string\',
              ResourceOwner=\'string\',
              CallerArn=\'string\',
              ContextEntries=[
                  {
                      \'ContextKeyName\': \'string\',
                      \'ContextKeyValues\': [
                          \'string\',
                      ],
                      \'ContextKeyType\': \'string\'|\'stringList\'|\'numeric\'|\'numericList\'|\'boolean\'|\'booleanList\'|\'ip\'|\'ipList\'|\'binary\'|\'binaryList\'|\'date\'|\'dateList\'
                  },
              ],
              ResourceHandlingOption=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PolicyInputList: list
        :param PolicyInputList: **[REQUIRED]** 
        
          A list of policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy. Do not include any resource-based policies in this parameter. Any resource-based policy must be submitted with the ``ResourcePolicy`` parameter. The policies cannot be \"scope-down\" policies, such as you could include in a call to `GetFederationToken <http://docs.aws.amazon.com/IAM/latest/APIReference/API_GetFederationToken.html>`__ or one of the `AssumeRole <http://docs.aws.amazon.com/IAM/latest/APIReference/API_AssumeRole.html>`__ API operations. In other words, do not use policies designed to restrict what a user can do while using the temporary credentials.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is a string of characters consisting of the following:
        
          * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range 
           
          * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF) 
           
          * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D) 
           
          - *(string) --* 
        
        :type ActionNames: list
        :param ActionNames: **[REQUIRED]** 
        
          A list of names of API operations to evaluate in the simulation. Each operation is evaluated against each resource. Each operation must include the service identifier, such as ``iam:CreateUser`` .
        
          - *(string) --* 
        
        :type ResourceArns: list
        :param ResourceArns: 
        
          A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided then the value defaults to ``*`` (all resources). Each API in the ``ActionNames`` parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response.
        
          The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the ``ResourcePolicy`` parameter.
        
          If you include a ``ResourcePolicy`` , then it must be applicable to all of the resources included in the simulation or you receive an invalid input error.
        
          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .
        
          - *(string) --* 
        
        :type ResourcePolicy: string
        :param ResourcePolicy: 
        
          A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is a string of characters consisting of the following:
        
          * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range 
           
          * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF) 
           
          * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D) 
           
        :type ResourceOwner: string
        :param ResourceOwner: 
        
          An ARN representing the AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN, such as an S3 bucket or object. If ``ResourceOwner`` is specified, it is also used as the account owner of any ``ResourcePolicy`` included in the simulation. If the ``ResourceOwner`` parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in ``CallerArn`` . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user ``CallerArn`` .
        
          The ARN for an account uses the following syntax: ``arn:aws:iam::*AWS-account-ID* :root`` . For example, to represent the account with the 112233445566 ID, use the following ARN: ``arn:aws:iam::112233445566-ID:root`` . 
        
        :type CallerArn: string
        :param CallerArn: 
        
          The ARN of the IAM user that you want to use as the simulated caller of the API operations. ``CallerArn`` is required if you include a ``ResourcePolicy`` so that the policy\'s ``Principal`` element has a value to use in evaluating the policy.
        
          You can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.
        
        :type ContextEntries: list
        :param ContextEntries: 
        
          A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permission policies, the corresponding value is supplied.
        
          - *(dict) --* 
        
            Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the ``Condition`` elements of the input policies.
        
            This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``  SimulateCustomPolicy `` .
        
            - **ContextKeyName** *(string) --* 
        
              The full name of a condition context key, including the service prefix. For example, ``aws:SourceIp`` or ``s3:VersionId`` .
        
            - **ContextKeyValues** *(list) --* 
        
              The value (or values, if the condition context key supports multiple values) to provide to the simulation when the key is referenced by a ``Condition`` element in an input policy.
        
              - *(string) --* 
        
            - **ContextKeyType** *(string) --* 
        
              The data type of the value (or values) specified in the ``ContextKeyValues`` parameter.
        
        :type ResourceHandlingOption: string
        :param ResourceHandlingOption: 
        
          Specifies the type of simulation to run. Different API operations that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.
        
          Each of the EC2 scenarios requires that you specify instance, image, and security-group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the EC2 scenario includes VPC, then you must supply the network-interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the EC2 scenario options, see `Supported Platforms <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`__ in the *Amazon EC2 User Guide* .
        
          * **EC2-Classic-InstanceStore**   instance, image, security-group 
           
          * **EC2-Classic-EBS**   instance, image, security-group, volume 
           
          * **EC2-VPC-InstanceStore**   instance, image, security-group, network-interface 
           
          * **EC2-VPC-InstanceStore-Subnet**   instance, image, security-group, network-interface, subnet 
           
          * **EC2-VPC-EBS**   instance, image, security-group, network-interface, volume 
           
          * **EC2-VPC-EBS-Subnet**   instance, image, security-group, network-interface, subnet, volume 
           
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
                        \'EvalActionName\': \'string\',
                        \'EvalResourceName\': \'string\',
                        \'EvalDecision\': \'allowed\'|\'explicitDeny\'|\'implicitDeny\',
                        \'MatchedStatements\': [
                            {
                                \'SourcePolicyId\': \'string\',
                                \'SourcePolicyType\': \'user\'|\'group\'|\'role\'|\'aws-managed\'|\'user-managed\'|\'resource\'|\'none\',
                                \'StartPosition\': {
                                    \'Line\': 123,
                                    \'Column\': 123
                                },
                                \'EndPosition\': {
                                    \'Line\': 123,
                                    \'Column\': 123
                                }
                            },
                        ],
                        \'MissingContextValues\': [
                            \'string\',
                        ],
                        \'OrganizationsDecisionDetail\': {
                            \'AllowedByOrganizations\': True|False
                        },
                        \'EvalDecisionDetails\': {
                            \'string\': \'allowed\'|\'explicitDeny\'|\'implicitDeny\'
                        },
                        \'ResourceSpecificResults\': [
                            {
                                \'EvalResourceName\': \'string\',
                                \'EvalResourceDecision\': \'allowed\'|\'explicitDeny\'|\'implicitDeny\',
                                \'MatchedStatements\': [
                                    {
                                        \'SourcePolicyId\': \'string\',
                                        \'SourcePolicyType\': \'user\'|\'group\'|\'role\'|\'aws-managed\'|\'user-managed\'|\'resource\'|\'none\',
                                        \'StartPosition\': {
                                            \'Line\': 123,
                                            \'Column\': 123
                                        },
                                        \'EndPosition\': {
                                            \'Line\': 123,
                                            \'Column\': 123
                                        }
                                    },
                                ],
                                \'MissingContextValues\': [
                                    \'string\',
                                ],
                                \'EvalDecisionDetails\': {
                                    \'string\': \'allowed\'|\'explicitDeny\'|\'implicitDeny\'
                                }
                            },
                        ]
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  SimulatePrincipalPolicy or  SimulateCustomPolicy request.
        
            - **EvaluationResults** *(list) --* 
        
              The results of the simulation.
        
              - *(dict) --* 
        
                Contains the results of a simulation.
        
                This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``  SimulatePrincipalPolicy `` .
        
                - **EvalActionName** *(string) --* 
        
                  The name of the API operation tested on the indicated resource.
        
                - **EvalResourceName** *(string) --* 
        
                  The ARN of the resource that the indicated API operation was tested on.
        
                - **EvalDecision** *(string) --* 
        
                  The result of the simulation.
        
                - **MatchedStatements** *(list) --* 
        
                  A list of the statements in the input policies that determine the result for this scenario. Remember that even if multiple statements allow the operation on the resource, if only one statement denies that operation, then the explicit deny overrides any allow, and the deny statement is the only entry included in the result.
        
                  - *(dict) --* 
        
                    Contains a reference to a ``Statement`` element in a policy document that determines the result of the simulation.
        
                    This data type is used by the ``MatchedStatements`` member of the ``  EvaluationResult `` type.
        
                    - **SourcePolicyId** *(string) --* 
        
                      The identifier of the policy that was provided as an input.
        
                    - **SourcePolicyType** *(string) --* 
        
                      The type of the policy.
        
                    - **StartPosition** *(dict) --* 
        
                      The row and column of the beginning of the ``Statement`` in an IAM policy.
        
                      - **Line** *(integer) --* 
        
                        The line containing the specified position in the document.
        
                      - **Column** *(integer) --* 
        
                        The column in the line containing the specified position in the document.
        
                    - **EndPosition** *(dict) --* 
        
                      The row and column of the end of a ``Statement`` in an IAM policy.
        
                      - **Line** *(integer) --* 
        
                        The line containing the specified position in the document.
        
                      - **Column** *(integer) --* 
        
                        The column in the line containing the specified position in the document.
        
                - **MissingContextValues** *(list) --* 
        
                  A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when the resource in a simulation is \"*\", either explicitly, or when the ``ResourceArns`` parameter blank. If you include a list of resources, then any missing context values are instead included under the ``ResourceSpecificResults`` section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .
        
                  - *(string) --* 
              
                - **OrganizationsDecisionDetail** *(dict) --* 
        
                  A structure that details how AWS Organizations and its service control policies affect the results of the simulation. Only applies if the simulated user\'s account is part of an organization.
        
                  - **AllowedByOrganizations** *(boolean) --* 
        
                    Specifies whether the simulated operation is allowed by the AWS Organizations service control policies that impact the simulated user\'s account.
        
                - **EvalDecisionDetails** *(dict) --* 
        
                  Additional details about the results of the evaluation decision. When there are both IAM policies and resource policies, this parameter explains how each set of policies contributes to the final evaluation decision. When simulating cross-account access to a resource, both the resource-based policy and the caller\'s IAM policy must grant access. See `How IAM Roles Differ from Resource-based Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html>`__  
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **ResourceSpecificResults** *(list) --* 
        
                  The individual results of the simulation of the API operation specified in EvalActionName on each resource.
        
                  - *(dict) --* 
        
                    Contains the result of the simulation of a single API operation call on a single resource.
        
                    This data type is used by a member of the  EvaluationResult data type.
        
                    - **EvalResourceName** *(string) --* 
        
                      The name of the simulated resource, in Amazon Resource Name (ARN) format.
        
                    - **EvalResourceDecision** *(string) --* 
        
                      The result of the simulation of the simulated API operation on the resource specified in ``EvalResourceName`` .
        
                    - **MatchedStatements** *(list) --* 
        
                      A list of the statements in the input policies that determine the result for this part of the simulation. Remember that even if multiple statements allow the operation on the resource, if *any* statement denies that operation, then the explicit deny overrides any allow, and the deny statement is the only entry included in the result.
        
                      - *(dict) --* 
        
                        Contains a reference to a ``Statement`` element in a policy document that determines the result of the simulation.
        
                        This data type is used by the ``MatchedStatements`` member of the ``  EvaluationResult `` type.
        
                        - **SourcePolicyId** *(string) --* 
        
                          The identifier of the policy that was provided as an input.
        
                        - **SourcePolicyType** *(string) --* 
        
                          The type of the policy.
        
                        - **StartPosition** *(dict) --* 
        
                          The row and column of the beginning of the ``Statement`` in an IAM policy.
        
                          - **Line** *(integer) --* 
        
                            The line containing the specified position in the document.
        
                          - **Column** *(integer) --* 
        
                            The column in the line containing the specified position in the document.
        
                        - **EndPosition** *(dict) --* 
        
                          The row and column of the end of a ``Statement`` in an IAM policy.
        
                          - **Line** *(integer) --* 
        
                            The line containing the specified position in the document.
        
                          - **Column** *(integer) --* 
        
                            The column in the line containing the specified position in the document.
        
                    - **MissingContextValues** *(list) --* 
        
                      A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when a list of ARNs is included in the ``ResourceArns`` parameter instead of \"*\". If you do not specify individual resources, by setting ``ResourceArns`` to \"*\" or by not including the ``ResourceArns`` parameter, then any missing context values are instead included under the ``EvaluationResults`` section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .
        
                      - *(string) --* 
                  
                    - **EvalDecisionDetails** *(dict) --* 
        
                      Additional details about the results of the evaluation decision. When there are both IAM policies and resource policies, this parameter explains how each set of policies contributes to the final evaluation decision. When simulating cross-account access to a resource, both the resource-based policy and the caller\'s IAM policy must grant access.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class SimulatePrincipalPolicy(Paginator):
    def paginate(self, PolicySourceArn: str, ActionNames: List, PolicyInputList: List = None, ResourceArns: List = None, ResourcePolicy: str = None, ResourceOwner: str = None, CallerArn: str = None, ContextEntries: List = None, ResourceHandlingOption: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/SimulatePrincipalPolicy>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PolicySourceArn=\'string\',
              PolicyInputList=[
                  \'string\',
              ],
              ActionNames=[
                  \'string\',
              ],
              ResourceArns=[
                  \'string\',
              ],
              ResourcePolicy=\'string\',
              ResourceOwner=\'string\',
              CallerArn=\'string\',
              ContextEntries=[
                  {
                      \'ContextKeyName\': \'string\',
                      \'ContextKeyValues\': [
                          \'string\',
                      ],
                      \'ContextKeyType\': \'string\'|\'stringList\'|\'numeric\'|\'numericList\'|\'boolean\'|\'booleanList\'|\'ip\'|\'ipList\'|\'binary\'|\'binaryList\'|\'date\'|\'dateList\'
                  },
              ],
              ResourceHandlingOption=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PolicySourceArn: string
        :param PolicySourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of a user, group, or role whose policies you want to include in the simulation. If you specify a user, group, or role, the simulation includes all policies that are associated with that entity. If you specify a user, the simulation also includes all policies that are attached to any groups the user belongs to.
        
          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .
        
        :type PolicyInputList: list
        :param PolicyInputList: 
        
          An optional list of additional policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is a string of characters consisting of the following:
        
          * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range 
           
          * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF) 
           
          * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D) 
           
          - *(string) --* 
        
        :type ActionNames: list
        :param ActionNames: **[REQUIRED]** 
        
          A list of names of API operations to evaluate in the simulation. Each operation is evaluated for each resource. Each operation must include the service identifier, such as ``iam:CreateUser`` .
        
          - *(string) --* 
        
        :type ResourceArns: list
        :param ResourceArns: 
        
          A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided, then the value defaults to ``*`` (all resources). Each API in the ``ActionNames`` parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response.
        
          The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the ``ResourcePolicy`` parameter.
        
          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .
        
          - *(string) --* 
        
        :type ResourcePolicy: string
        :param ResourcePolicy: 
        
          A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is a string of characters consisting of the following:
        
          * Any printable ASCII character ranging from the space character (\u0020) through the end of the ASCII character range 
           
          * The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF) 
           
          * The special characters tab (\u0009), line feed (\u000A), and carriage return (\u000D) 
           
        :type ResourceOwner: string
        :param ResourceOwner: 
        
          An AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN, such as an S3 bucket or object. If ``ResourceOwner`` is specified, it is also used as the account owner of any ``ResourcePolicy`` included in the simulation. If the ``ResourceOwner`` parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in ``CallerArn`` . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user ``CallerArn`` .
        
        :type CallerArn: string
        :param CallerArn: 
        
          The ARN of the IAM user that you want to specify as the simulated caller of the API operations. If you do not specify a ``CallerArn`` , it defaults to the ARN of the user that you specify in ``PolicySourceArn`` , if you specified a user. If you include both a ``PolicySourceArn`` (for example, ``arn:aws:iam::123456789012:user/David`` ) and a ``CallerArn`` (for example, ``arn:aws:iam::123456789012:user/Bob`` ), the result is that you simulate calling the API operations as Bob, as if Bob had David\'s policies.
        
          You can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.
        
           ``CallerArn`` is required if you include a ``ResourcePolicy`` and the ``PolicySourceArn`` is not the ARN for an IAM user. This is required so that the resource-based policy\'s ``Principal`` element has a value to use in evaluating the policy.
        
          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .
        
        :type ContextEntries: list
        :param ContextEntries: 
        
          A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permission policies, the corresponding value is supplied.
        
          - *(dict) --* 
        
            Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the ``Condition`` elements of the input policies.
        
            This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``  SimulateCustomPolicy `` .
        
            - **ContextKeyName** *(string) --* 
        
              The full name of a condition context key, including the service prefix. For example, ``aws:SourceIp`` or ``s3:VersionId`` .
        
            - **ContextKeyValues** *(list) --* 
        
              The value (or values, if the condition context key supports multiple values) to provide to the simulation when the key is referenced by a ``Condition`` element in an input policy.
        
              - *(string) --* 
        
            - **ContextKeyType** *(string) --* 
        
              The data type of the value (or values) specified in the ``ContextKeyValues`` parameter.
        
        :type ResourceHandlingOption: string
        :param ResourceHandlingOption: 
        
          Specifies the type of simulation to run. Different API operations that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.
        
          Each of the EC2 scenarios requires that you specify instance, image, and security-group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the EC2 scenario includes VPC, then you must supply the network-interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the EC2 scenario options, see `Supported Platforms <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`__ in the *Amazon EC2 User Guide* .
        
          * **EC2-Classic-InstanceStore**   instance, image, security-group 
           
          * **EC2-Classic-EBS**   instance, image, security-group, volume 
           
          * **EC2-VPC-InstanceStore**   instance, image, security-group, network-interface 
           
          * **EC2-VPC-InstanceStore-Subnet**   instance, image, security-group, network-interface, subnet 
           
          * **EC2-VPC-EBS**   instance, image, security-group, network-interface, volume 
           
          * **EC2-VPC-EBS-Subnet**   instance, image, security-group, network-interface, subnet, volume 
           
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
                        \'EvalActionName\': \'string\',
                        \'EvalResourceName\': \'string\',
                        \'EvalDecision\': \'allowed\'|\'explicitDeny\'|\'implicitDeny\',
                        \'MatchedStatements\': [
                            {
                                \'SourcePolicyId\': \'string\',
                                \'SourcePolicyType\': \'user\'|\'group\'|\'role\'|\'aws-managed\'|\'user-managed\'|\'resource\'|\'none\',
                                \'StartPosition\': {
                                    \'Line\': 123,
                                    \'Column\': 123
                                },
                                \'EndPosition\': {
                                    \'Line\': 123,
                                    \'Column\': 123
                                }
                            },
                        ],
                        \'MissingContextValues\': [
                            \'string\',
                        ],
                        \'OrganizationsDecisionDetail\': {
                            \'AllowedByOrganizations\': True|False
                        },
                        \'EvalDecisionDetails\': {
                            \'string\': \'allowed\'|\'explicitDeny\'|\'implicitDeny\'
                        },
                        \'ResourceSpecificResults\': [
                            {
                                \'EvalResourceName\': \'string\',
                                \'EvalResourceDecision\': \'allowed\'|\'explicitDeny\'|\'implicitDeny\',
                                \'MatchedStatements\': [
                                    {
                                        \'SourcePolicyId\': \'string\',
                                        \'SourcePolicyType\': \'user\'|\'group\'|\'role\'|\'aws-managed\'|\'user-managed\'|\'resource\'|\'none\',
                                        \'StartPosition\': {
                                            \'Line\': 123,
                                            \'Column\': 123
                                        },
                                        \'EndPosition\': {
                                            \'Line\': 123,
                                            \'Column\': 123
                                        }
                                    },
                                ],
                                \'MissingContextValues\': [
                                    \'string\',
                                ],
                                \'EvalDecisionDetails\': {
                                    \'string\': \'allowed\'|\'explicitDeny\'|\'implicitDeny\'
                                }
                            },
                        ]
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a successful  SimulatePrincipalPolicy or  SimulateCustomPolicy request.
        
            - **EvaluationResults** *(list) --* 
        
              The results of the simulation.
        
              - *(dict) --* 
        
                Contains the results of a simulation.
        
                This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``  SimulatePrincipalPolicy `` .
        
                - **EvalActionName** *(string) --* 
        
                  The name of the API operation tested on the indicated resource.
        
                - **EvalResourceName** *(string) --* 
        
                  The ARN of the resource that the indicated API operation was tested on.
        
                - **EvalDecision** *(string) --* 
        
                  The result of the simulation.
        
                - **MatchedStatements** *(list) --* 
        
                  A list of the statements in the input policies that determine the result for this scenario. Remember that even if multiple statements allow the operation on the resource, if only one statement denies that operation, then the explicit deny overrides any allow, and the deny statement is the only entry included in the result.
        
                  - *(dict) --* 
        
                    Contains a reference to a ``Statement`` element in a policy document that determines the result of the simulation.
        
                    This data type is used by the ``MatchedStatements`` member of the ``  EvaluationResult `` type.
        
                    - **SourcePolicyId** *(string) --* 
        
                      The identifier of the policy that was provided as an input.
        
                    - **SourcePolicyType** *(string) --* 
        
                      The type of the policy.
        
                    - **StartPosition** *(dict) --* 
        
                      The row and column of the beginning of the ``Statement`` in an IAM policy.
        
                      - **Line** *(integer) --* 
        
                        The line containing the specified position in the document.
        
                      - **Column** *(integer) --* 
        
                        The column in the line containing the specified position in the document.
        
                    - **EndPosition** *(dict) --* 
        
                      The row and column of the end of a ``Statement`` in an IAM policy.
        
                      - **Line** *(integer) --* 
        
                        The line containing the specified position in the document.
        
                      - **Column** *(integer) --* 
        
                        The column in the line containing the specified position in the document.
        
                - **MissingContextValues** *(list) --* 
        
                  A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when the resource in a simulation is \"*\", either explicitly, or when the ``ResourceArns`` parameter blank. If you include a list of resources, then any missing context values are instead included under the ``ResourceSpecificResults`` section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .
        
                  - *(string) --* 
              
                - **OrganizationsDecisionDetail** *(dict) --* 
        
                  A structure that details how AWS Organizations and its service control policies affect the results of the simulation. Only applies if the simulated user\'s account is part of an organization.
        
                  - **AllowedByOrganizations** *(boolean) --* 
        
                    Specifies whether the simulated operation is allowed by the AWS Organizations service control policies that impact the simulated user\'s account.
        
                - **EvalDecisionDetails** *(dict) --* 
        
                  Additional details about the results of the evaluation decision. When there are both IAM policies and resource policies, this parameter explains how each set of policies contributes to the final evaluation decision. When simulating cross-account access to a resource, both the resource-based policy and the caller\'s IAM policy must grant access. See `How IAM Roles Differ from Resource-based Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html>`__  
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **ResourceSpecificResults** *(list) --* 
        
                  The individual results of the simulation of the API operation specified in EvalActionName on each resource.
        
                  - *(dict) --* 
        
                    Contains the result of the simulation of a single API operation call on a single resource.
        
                    This data type is used by a member of the  EvaluationResult data type.
        
                    - **EvalResourceName** *(string) --* 
        
                      The name of the simulated resource, in Amazon Resource Name (ARN) format.
        
                    - **EvalResourceDecision** *(string) --* 
        
                      The result of the simulation of the simulated API operation on the resource specified in ``EvalResourceName`` .
        
                    - **MatchedStatements** *(list) --* 
        
                      A list of the statements in the input policies that determine the result for this part of the simulation. Remember that even if multiple statements allow the operation on the resource, if *any* statement denies that operation, then the explicit deny overrides any allow, and the deny statement is the only entry included in the result.
        
                      - *(dict) --* 
        
                        Contains a reference to a ``Statement`` element in a policy document that determines the result of the simulation.
        
                        This data type is used by the ``MatchedStatements`` member of the ``  EvaluationResult `` type.
        
                        - **SourcePolicyId** *(string) --* 
        
                          The identifier of the policy that was provided as an input.
        
                        - **SourcePolicyType** *(string) --* 
        
                          The type of the policy.
        
                        - **StartPosition** *(dict) --* 
        
                          The row and column of the beginning of the ``Statement`` in an IAM policy.
        
                          - **Line** *(integer) --* 
        
                            The line containing the specified position in the document.
        
                          - **Column** *(integer) --* 
        
                            The column in the line containing the specified position in the document.
        
                        - **EndPosition** *(dict) --* 
        
                          The row and column of the end of a ``Statement`` in an IAM policy.
        
                          - **Line** *(integer) --* 
        
                            The line containing the specified position in the document.
        
                          - **Column** *(integer) --* 
        
                            The column in the line containing the specified position in the document.
        
                    - **MissingContextValues** *(list) --* 
        
                      A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when a list of ARNs is included in the ``ResourceArns`` parameter instead of \"*\". If you do not specify individual resources, by setting ``ResourceArns`` to \"*\" or by not including the ``ResourceArns`` parameter, then any missing context values are instead included under the ``EvaluationResults`` section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .
        
                      - *(string) --* 
                  
                    - **EvalDecisionDetails** *(dict) --* 
        
                      Additional details about the results of the evaluation decision. When there are both IAM policies and resource policies, this parameter explains how each set of policies contributes to the final evaluation decision. When simulating cross-account access to a resource, both the resource-based policy and the caller\'s IAM policy must grant access.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the ``Marker`` request parameter to retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results even when there are more results available. We recommend that you check ``IsTruncated`` after every call to ensure that you receive all of your results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
