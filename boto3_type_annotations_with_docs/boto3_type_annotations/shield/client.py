from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_drt_log_bucket(self, LogBucket: str) -> Dict:
        """
        
        To use the services of the DRT and make an ``AssociateDRTLogBucket`` request, you must be subscribed to the `Business Support plan <https://aws.amazon.com/premiumsupport/business-support/>`__ or the `Enterprise Support plan <https://aws.amazon.com/premiumsupport/enterprise-support/>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/AssociateDRTLogBucket>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_drt_log_bucket(
              LogBucket=\'string\'
          )
        :type LogBucket: string
        :param LogBucket: **[REQUIRED]** 
        
          The Amazon S3 bucket that contains your flow logs.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def associate_drt_role(self, RoleArn: str) -> Dict:
        """
        
        You can associate only one ``RoleArn`` with your subscription. If you submit an ``AssociateDRTRole`` request for an account that already has an associated role, the new ``RoleArn`` will replace the existing ``RoleArn`` . 
        
        Prior to making the ``AssociateDRTRole`` request, you must attach the `AWSShieldDRTAccessPolicy <https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy>`__ managed policy to the role you will specify in the request. For more information see `Attaching and Detaching IAM Policies < https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`__ . The role must also trust the service principal ``drt.shield.amazonaws.com`` . For more information, see `IAM JSON Policy Elements\: Principal <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html>`__ .
        
        The DRT will have access only to your AWS WAF and Shield resources. By submitting this request, you authorize the DRT to inspect your AWS WAF and Shield configuration and create and update AWS WAF rules and web ACLs on your behalf. The DRT takes these actions only if explicitly authorized by you.
        
        You must have the ``iam:PassRole`` permission to make an ``AssociateDRTRole`` request. For more information, see `Granting a User Permissions to Pass a Role to an AWS Service <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html>`__ . 
        
        To use the services of the DRT and make an ``AssociateDRTRole`` request, you must be subscribed to the `Business Support plan <https://aws.amazon.com/premiumsupport/business-support/>`__ or the `Enterprise Support plan <https://aws.amazon.com/premiumsupport/enterprise-support/>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/AssociateDRTRole>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_drt_role(
              RoleArn=\'string\'
          )
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the role the DRT will use to access your AWS account.
        
          Prior to making the ``AssociateDRTRole`` request, you must attach the `AWSShieldDRTAccessPolicy <https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy>`__ managed policy to this role. For more information see `Attaching and Detaching IAM Policies < https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`__ .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

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

    def create_protection(self, Name: str, ResourceArn: str) -> Dict:
        """
        
        You can add protection to only a single resource with each CreateProtection request. If you want to add protection to multiple resources at once, use the `AWS WAF console <https://console.aws.amazon.com/waf/>`__ . For more information see `Getting Started with AWS Shield Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html>`__ and `Add AWS Shield Advanced Protection to more AWS Resources <https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/CreateProtection>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_protection(
              Name=\'string\',
              ResourceArn=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Friendly name for the ``Protection`` you are creating.
        
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The ARN (Amazon Resource Name) of the resource to be protected.
        
          The ARN should be in one of the following formats:
        
          * For an Application Load Balancer: ``arn:aws:elasticloadbalancing:*region* :*account-id* :loadbalancer/app/*load-balancer-name* /*load-balancer-id* ``   
           
          * For an Elastic Load Balancer (Classic Load Balancer): ``arn:aws:elasticloadbalancing:*region* :*account-id* :loadbalancer/*load-balancer-name* ``   
           
          * For AWS CloudFront distribution: ``arn:aws:cloudfront::*account-id* :distribution/*distribution-id* ``   
           
          * For Amazon Route 53: ``arn:aws:route53:::hostedzone/*hosted-zone-id* ``   
           
          * For an Elastic IP address: ``arn:aws:ec2:*region* :*account-id* :eip-allocation/*allocation-id* ``   
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ProtectionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ProtectionId** *(string) --* 
        
              The unique identifier (ID) for the  Protection object that is created.
        
        """
        pass

    def create_subscription(self) -> Dict:
        """
        
        As part of this request you can specify ``EmergencySettings`` that automaticaly grant the DDoS response team (DRT) needed permissions to assist you during a suspected DDoS attack. For more information see `Authorize the DDoS Response Team to Create Rules and Web ACLs on Your Behalf <https://docs.aws.amazon.com/waf/latest/developerguide/authorize-DRT.html>`__ .
        
        When you initally create a subscription, your subscription is set to be automatically renewed at the end of the existing subscription period. You can change this by submitting an ``UpdateSubscription`` request. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/CreateSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_subscription()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_protection(self, ProtectionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DeleteProtection>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_protection(
              ProtectionId=\'string\'
          )
        :type ProtectionId: string
        :param ProtectionId: **[REQUIRED]** 
        
          The unique identifier (ID) for the  Protection object to be deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_subscription(self) -> Dict:
        """
        
        .. danger::
        
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DeleteSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_subscription()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_attack(self, AttackId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeAttack>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_attack(
              AttackId=\'string\'
          )
        :type AttackId: string
        :param AttackId: **[REQUIRED]** 
        
          The unique identifier (ID) for the attack that to be described.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attack\': {
                    \'AttackId\': \'string\',
                    \'ResourceArn\': \'string\',
                    \'SubResources\': [
                        {
                            \'Type\': \'IP\'|\'URL\',
                            \'Id\': \'string\',
                            \'AttackVectors\': [
                                {
                                    \'VectorType\': \'string\',
                                    \'VectorCounters\': [
                                        {
                                            \'Name\': \'string\',
                                            \'Max\': 123.0,
                                            \'Average\': 123.0,
                                            \'Sum\': 123.0,
                                            \'N\': 123,
                                            \'Unit\': \'string\'
                                        },
                                    ]
                                },
                            ],
                            \'Counters\': [
                                {
                                    \'Name\': \'string\',
                                    \'Max\': 123.0,
                                    \'Average\': 123.0,
                                    \'Sum\': 123.0,
                                    \'N\': 123,
                                    \'Unit\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'StartTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'AttackCounters\': [
                        {
                            \'Name\': \'string\',
                            \'Max\': 123.0,
                            \'Average\': 123.0,
                            \'Sum\': 123.0,
                            \'N\': 123,
                            \'Unit\': \'string\'
                        },
                    ],
                    \'AttackProperties\': [
                        {
                            \'AttackLayer\': \'NETWORK\'|\'APPLICATION\',
                            \'AttackPropertyIdentifier\': \'DESTINATION_URL\'|\'REFERRER\'|\'SOURCE_ASN\'|\'SOURCE_COUNTRY\'|\'SOURCE_IP_ADDRESS\'|\'SOURCE_USER_AGENT\',
                            \'TopContributors\': [
                                {
                                    \'Name\': \'string\',
                                    \'Value\': 123
                                },
                            ],
                            \'Unit\': \'BITS\'|\'BYTES\'|\'PACKETS\'|\'REQUESTS\',
                            \'Total\': 123
                        },
                    ],
                    \'Mitigations\': [
                        {
                            \'MitigationName\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attack** *(dict) --* 
        
              The attack that is described.
        
              - **AttackId** *(string) --* 
        
                The unique identifier (ID) of the attack.
        
              - **ResourceArn** *(string) --* 
        
                The ARN (Amazon Resource Name) of the resource that was attacked.
        
              - **SubResources** *(list) --* 
        
                If applicable, additional detail about the resource being attacked, for example, IP address or URL.
        
                - *(dict) --* 
        
                  The attack information for the specified SubResource.
        
                  - **Type** *(string) --* 
        
                    The ``SubResource`` type.
        
                  - **Id** *(string) --* 
        
                    The unique identifier (ID) of the ``SubResource`` .
        
                  - **AttackVectors** *(list) --* 
        
                    The list of attack types and associated counters.
        
                    - *(dict) --* 
        
                      A summary of information about the attack.
        
                      - **VectorType** *(string) --* 
        
                        The attack type, for example, SNMP reflection or SYN flood.
        
                      - **VectorCounters** *(list) --* 
        
                        The list of counters that describe the details of the attack.
        
                        - *(dict) --* 
        
                          The counter that describes a DDoS attack.
        
                          - **Name** *(string) --* 
        
                            The counter name.
        
                          - **Max** *(float) --* 
        
                            The maximum value of the counter for a specified time period.
        
                          - **Average** *(float) --* 
        
                            The average value of the counter for a specified time period.
        
                          - **Sum** *(float) --* 
        
                            The total of counter values for a specified time period.
        
                          - **N** *(integer) --* 
        
                            The number of counters for a specified time period.
        
                          - **Unit** *(string) --* 
        
                            The unit of the counters.
        
                  - **Counters** *(list) --* 
        
                    The counters that describe the details of the attack.
        
                    - *(dict) --* 
        
                      The counter that describes a DDoS attack.
        
                      - **Name** *(string) --* 
        
                        The counter name.
        
                      - **Max** *(float) --* 
        
                        The maximum value of the counter for a specified time period.
        
                      - **Average** *(float) --* 
        
                        The average value of the counter for a specified time period.
        
                      - **Sum** *(float) --* 
        
                        The total of counter values for a specified time period.
        
                      - **N** *(integer) --* 
        
                        The number of counters for a specified time period.
        
                      - **Unit** *(string) --* 
        
                        The unit of the counters.
        
              - **StartTime** *(datetime) --* 
        
                The time the attack started, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
              - **EndTime** *(datetime) --* 
        
                The time the attack ended, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
              - **AttackCounters** *(list) --* 
        
                List of counters that describe the attack for the specified time period.
        
                - *(dict) --* 
        
                  The counter that describes a DDoS attack.
        
                  - **Name** *(string) --* 
        
                    The counter name.
        
                  - **Max** *(float) --* 
        
                    The maximum value of the counter for a specified time period.
        
                  - **Average** *(float) --* 
        
                    The average value of the counter for a specified time period.
        
                  - **Sum** *(float) --* 
        
                    The total of counter values for a specified time period.
        
                  - **N** *(integer) --* 
        
                    The number of counters for a specified time period.
        
                  - **Unit** *(string) --* 
        
                    The unit of the counters.
        
              - **AttackProperties** *(list) --* 
        
                The array of  AttackProperty objects.
        
                - *(dict) --* 
        
                  Details of the described attack.
        
                  - **AttackLayer** *(string) --* 
        
                    The type of DDoS event that was observed. ``NETWORK`` indicates layer 3 and layer 4 events and ``APPLICATION`` indicates layer 7 events.
        
                  - **AttackPropertyIdentifier** *(string) --* 
        
                    Defines the DDoS attack property information that is provided.
        
                  - **TopContributors** *(list) --* 
        
                    The array of  Contributor objects that includes the top five contributors to an attack. 
        
                    - *(dict) --* 
        
                      A contributor to the attack and their contribution.
        
                      - **Name** *(string) --* 
        
                        The name of the contributor. This is dependent on the ``AttackPropertyIdentifier`` . For example, if the ``AttackPropertyIdentifier`` is ``SOURCE_COUNTRY`` , the ``Name`` could be ``United States`` .
        
                      - **Value** *(integer) --* 
        
                        The contribution of this contributor expressed in  Protection units. For example ``10,000`` .
        
                  - **Unit** *(string) --* 
        
                    The unit of the ``Value`` of the contributions.
        
                  - **Total** *(integer) --* 
        
                    The total contributions made to this attack by all contributors, not just the five listed in the ``TopContributors`` list.
        
              - **Mitigations** *(list) --* 
        
                List of mitigation actions taken for the attack.
        
                - *(dict) --* 
        
                  The mitigation applied to a DDoS attack.
        
                  - **MitigationName** *(string) --* 
        
                    The name of the mitigation taken for this attack.
        
        """
        pass

    def describe_drt_access(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeDRTAccess>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_drt_access()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RoleArn\': \'string\',
                \'LogBucketList\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RoleArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the role the DRT used to access your AWS account.
        
            - **LogBucketList** *(list) --* 
        
              The list of Amazon S3 buckets accessed by the DRT.
        
              - *(string) --* 
          
        """
        pass

    def describe_emergency_contact_settings(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeEmergencyContactSettings>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_emergency_contact_settings()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EmergencyContactList\': [
                    {
                        \'EmailAddress\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EmergencyContactList** *(list) --* 
        
              A list of email addresses that the DRT can use to contact you during a suspected attack.
        
              - *(dict) --* 
        
                Contact information that the DRT can use to contact you during a suspected attack.
        
                - **EmailAddress** *(string) --* 
        
                  An email address that the DRT can use to contact you during a suspected attack.
        
        """
        pass

    def describe_protection(self, ProtectionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeProtection>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_protection(
              ProtectionId=\'string\'
          )
        :type ProtectionId: string
        :param ProtectionId: **[REQUIRED]** 
        
          The unique identifier (ID) for the  Protection object that is described.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Protection\': {
                    \'Id\': \'string\',
                    \'Name\': \'string\',
                    \'ResourceArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Protection** *(dict) --* 
        
              The  Protection object that is described.
        
              - **Id** *(string) --* 
        
                The unique identifier (ID) of the protection.
        
              - **Name** *(string) --* 
        
                The friendly name of the protection. For example, ``My CloudFront distributions`` .
        
              - **ResourceArn** *(string) --* 
        
                The ARN (Amazon Resource Name) of the AWS resource that is protected.
        
        """
        pass

    def describe_subscription(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_subscription()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Subscription\': {
                    \'StartTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'TimeCommitmentInSeconds\': 123,
                    \'AutoRenew\': \'ENABLED\'|\'DISABLED\',
                    \'Limits\': [
                        {
                            \'Type\': \'string\',
                            \'Max\': 123
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Subscription** *(dict) --* 
        
              The AWS Shield Advanced subscription details for an account.
        
              - **StartTime** *(datetime) --* 
        
                The start time of the subscription, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
              - **EndTime** *(datetime) --* 
        
                The date and time your subscription will end.
        
              - **TimeCommitmentInSeconds** *(integer) --* 
        
                The length, in seconds, of the AWS Shield Advanced subscription for the account.
        
              - **AutoRenew** *(string) --* 
        
                If ``ENABLED`` , the subscription will be automatically renewed at the end of the existing subscription period.
        
                When you initally create a subscription, ``AutoRenew`` is set to ``ENABLED`` . You can change this by submitting an ``UpdateSubscription`` request. If the ``UpdateSubscription`` request does not included a value for ``AutoRenew`` , the existing value for ``AutoRenew`` remains unchanged.
        
              - **Limits** *(list) --* 
        
                Specifies how many protections of a given type you can create.
        
                - *(dict) --* 
        
                  Specifies how many protections of a given type you can create.
        
                  - **Type** *(string) --* 
        
                    The type of protection.
        
                  - **Max** *(integer) --* 
        
                    The maximum number of protections that can be created for the specified ``Type`` .
        
        """
        pass

    def disassociate_drt_log_bucket(self, LogBucket: str) -> Dict:
        """
        
        To make a ``DisassociateDRTLogBucket`` request, you must be subscribed to the `Business Support plan <https://aws.amazon.com/premiumsupport/business-support/>`__ or the `Enterprise Support plan <https://aws.amazon.com/premiumsupport/enterprise-support/>`__ . However, if you are not subscribed to one of these support plans, but had been previously and had granted the DRT access to your account, you can submit a ``DisassociateDRTLogBucket`` request to remove this access.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DisassociateDRTLogBucket>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_drt_log_bucket(
              LogBucket=\'string\'
          )
        :type LogBucket: string
        :param LogBucket: **[REQUIRED]** 
        
          The Amazon S3 bucket that contains your flow logs.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_drt_role(self) -> Dict:
        """
        
        To make a ``DisassociateDRTRole`` request, you must be subscribed to the `Business Support plan <https://aws.amazon.com/premiumsupport/business-support/>`__ or the `Enterprise Support plan <https://aws.amazon.com/premiumsupport/enterprise-support/>`__ . However, if you are not subscribed to one of these support plans, but had been previously and had granted the DRT access to your account, you can submit a ``DisassociateDRTRole`` request to remove this access.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DisassociateDRTRole>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_drt_role()
          
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

    def get_subscription_state(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/GetSubscriptionState>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_subscription_state()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SubscriptionState\': \'ACTIVE\'|\'INACTIVE\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SubscriptionState** *(string) --* 
        
              The status of the subscription.
        
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

    def list_attacks(self, ResourceArns: List = None, StartTime: Dict = None, EndTime: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/ListAttacks>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_attacks(
              ResourceArns=[
                  \'string\',
              ],
              StartTime={
                  \'FromInclusive\': datetime(2015, 1, 1),
                  \'ToExclusive\': datetime(2015, 1, 1)
              },
              EndTime={
                  \'FromInclusive\': datetime(2015, 1, 1),
                  \'ToExclusive\': datetime(2015, 1, 1)
              },
              NextToken=\'string\',
              MaxResults=123
          )
        :type ResourceArns: list
        :param ResourceArns: 
        
          The ARN (Amazon Resource Name) of the resource that was attacked. If this is left blank, all applicable resources for this account will be included.
        
          - *(string) --* 
        
        :type StartTime: dict
        :param StartTime: 
        
          The start of the time period for the attacks. This is a ``timestamp`` type. The sample request above indicates a ``number`` type because the default used by WAF is Unix time in seconds. However any valid `timestamp format <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is allowed. 
        
          - **FromInclusive** *(datetime) --* 
        
            The start time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
          - **ToExclusive** *(datetime) --* 
        
            The end time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
        :type EndTime: dict
        :param EndTime: 
        
          The end of the time period for the attacks. This is a ``timestamp`` type. The sample request above indicates a ``number`` type because the default used by WAF is Unix time in seconds. However any valid `timestamp format <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is allowed. 
        
          - **FromInclusive** *(datetime) --* 
        
            The start time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
          - **ToExclusive** *(datetime) --* 
        
            The end time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
        :type NextToken: string
        :param NextToken: 
        
          The ``ListAttacksRequest.NextMarker`` value from a previous call to ``ListAttacksRequest`` . Pass null if this is the first call.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of  AttackSummary objects to be returned. If this is left blank, the first 20 results will be returned.
        
          This is a maximum value; it is possible that AWS WAF will return the results in smaller batches. That is, the number of  AttackSummary objects returned could be less than ``MaxResults`` , even if there are still more  AttackSummary objects yet to return. If there are more  AttackSummary objects to return, AWS WAF will always also return a ``NextToken`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttackSummaries\': [
                    {
                        \'AttackId\': \'string\',
                        \'ResourceArn\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'AttackVectors\': [
                            {
                                \'VectorType\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AttackSummaries** *(list) --* 
        
              The attack information for the specified time range.
        
              - *(dict) --* 
        
                Summarizes all DDoS attacks for a specified time period.
        
                - **AttackId** *(string) --* 
        
                  The unique identifier (ID) of the attack.
        
                - **ResourceArn** *(string) --* 
        
                  The ARN (Amazon Resource Name) of the resource that was attacked.
        
                - **StartTime** *(datetime) --* 
        
                  The start time of the attack, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
                - **EndTime** *(datetime) --* 
        
                  The end time of the attack, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        
                - **AttackVectors** *(list) --* 
        
                  The list of attacks for a specified time period.
        
                  - *(dict) --* 
        
                    Describes the attack.
        
                    - **VectorType** *(string) --* 
        
                      The attack type. Valid values:
        
                      * UDP_TRAFFIC 
                       
                      * UDP_FRAGMENT 
                       
                      * GENERIC_UDP_REFLECTION 
                       
                      * DNS_REFLECTION 
                       
                      * NTP_REFLECTION 
                       
                      * CHARGEN_REFLECTION 
                       
                      * SSDP_REFLECTION 
                       
                      * PORT_MAPPER 
                       
                      * RIP_REFLECTION 
                       
                      * SNMP_REFLECTION 
                       
                      * MSSQL_REFLECTION 
                       
                      * NET_BIOS_REFLECTION 
                       
                      * SYN_FLOOD 
                       
                      * ACK_FLOOD 
                       
                      * REQUEST_FLOOD 
                       
            - **NextToken** *(string) --* 
        
              The token returned by a previous call to indicate that there is more data available. If not null, more results are available. Pass this value for the ``NextMarker`` parameter in a subsequent call to ``ListAttacks`` to retrieve the next set of items.
        
              AWS WAF might return the list of  AttackSummary objects in batches smaller than the number specified by MaxResults. If there are more  AttackSummary objects to return, AWS WAF will always also return a ``NextToken`` .
        
        """
        pass

    def list_protections(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/ListProtections>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_protections(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          The ``ListProtectionsRequest.NextToken`` value from a previous call to ``ListProtections`` . Pass null if this is the first call.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of  Protection objects to be returned. If this is left blank the first 20 results will be returned.
        
          This is a maximum value; it is possible that AWS WAF will return the results in smaller batches. That is, the number of  Protection objects returned could be less than ``MaxResults`` , even if there are still more  Protection objects yet to return. If there are more  Protection objects to return, AWS WAF will always also return a ``NextToken`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Protections\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'ResourceArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Protections** *(list) --* 
        
              The array of enabled  Protection objects.
        
              - *(dict) --* 
        
                An object that represents a resource that is under DDoS protection.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of the protection.
        
                - **Name** *(string) --* 
        
                  The friendly name of the protection. For example, ``My CloudFront distributions`` .
        
                - **ResourceArn** *(string) --* 
        
                  The ARN (Amazon Resource Name) of the AWS resource that is protected.
        
            - **NextToken** *(string) --* 
        
              If you specify a value for ``MaxResults`` and you have more Protections than the value of MaxResults, AWS Shield Advanced returns a NextToken value in the response that allows you to list another group of Protections. For the second and subsequent ListProtections requests, specify the value of NextToken from the previous response to get information about another batch of Protections.
        
              AWS WAF might return the list of  Protection objects in batches smaller than the number specified by MaxResults. If there are more  Protection objects to return, AWS WAF will always also return a ``NextToken`` .
        
        """
        pass

    def update_emergency_contact_settings(self, EmergencyContactList: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/UpdateEmergencyContactSettings>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_emergency_contact_settings(
              EmergencyContactList=[
                  {
                      \'EmailAddress\': \'string\'
                  },
              ]
          )
        :type EmergencyContactList: list
        :param EmergencyContactList: 
        
          A list of email addresses that the DRT can use to contact you during a suspected attack.
        
          - *(dict) --* 
        
            Contact information that the DRT can use to contact you during a suspected attack.
        
            - **EmailAddress** *(string) --* **[REQUIRED]** 
        
              An email address that the DRT can use to contact you during a suspected attack.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_subscription(self, AutoRenew: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/UpdateSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_subscription(
              AutoRenew=\'ENABLED\'|\'DISABLED\'
          )
        :type AutoRenew: string
        :param AutoRenew: 
        
          When you initally create a subscription, ``AutoRenew`` is set to ``ENABLED`` . If ``ENABLED`` , the subscription will be automatically renewed at the end of the existing subscription period. You can change this by submitting an ``UpdateSubscription`` request. If the ``UpdateSubscription`` request does not included a value for ``AutoRenew`` , the existing value for ``AutoRenew`` remains unchanged.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
