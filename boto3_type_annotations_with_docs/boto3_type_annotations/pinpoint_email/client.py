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

    def create_configuration_set(self, ConfigurationSetName: str = None, TrackingOptions: Dict = None, DeliveryOptions: Dict = None, ReputationOptions: Dict = None, SendingOptions: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateConfigurationSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_configuration_set(
              ConfigurationSetName=\'string\',
              TrackingOptions={
                  \'CustomRedirectDomain\': \'string\'
              },
              DeliveryOptions={
                  \'SendingPoolName\': \'string\'
              },
              ReputationOptions={
                  \'ReputationMetricsEnabled\': True|False,
                  \'LastFreshStart\': datetime(2015, 1, 1)
              },
              SendingOptions={
                  \'SendingEnabled\': True|False
              }
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: 
        
          The name of the configuration set.
        
        :type TrackingOptions: dict
        :param TrackingOptions: 
        
          An object that defines the open and click tracking options for emails that you send using the configuration set.
        
          - **CustomRedirectDomain** *(string) --* **[REQUIRED]** 
        
            The domain that you want to use for tracking open and click events.
        
        :type DeliveryOptions: dict
        :param DeliveryOptions: 
        
          An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
        
          - **SendingPoolName** *(string) --* 
        
            The name of the dedicated IP pool that you want to associate with the configuration set.
        
        :type ReputationOptions: dict
        :param ReputationOptions: 
        
          An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.
        
          - **ReputationMetricsEnabled** *(boolean) --* 
        
            If ``true`` , tracking of reputation metrics is enabled for the configuration set. If ``false`` , tracking of reputation metrics is disabled for the configuration set.
        
          - **LastFreshStart** *(datetime) --* 
        
            The date and time when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.
        
        :type SendingOptions: dict
        :param SendingOptions: 
        
          An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
        
          - **SendingEnabled** *(boolean) --* 
        
            If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def create_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str, EventDestination: Dict) -> Dict:
        """
        
        A single configuration set can include more than one event destination.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateConfigurationSetEventDestination>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_configuration_set_event_destination(
              ConfigurationSetName=\'string\',
              EventDestinationName=\'string\',
              EventDestination={
                  \'Enabled\': True|False,
                  \'MatchingEventTypes\': [
                      \'SEND\'|\'REJECT\'|\'BOUNCE\'|\'COMPLAINT\'|\'DELIVERY\'|\'OPEN\'|\'CLICK\'|\'RENDERING_FAILURE\',
                  ],
                  \'KinesisFirehoseDestination\': {
                      \'IamRoleArn\': \'string\',
                      \'DeliveryStreamArn\': \'string\'
                  },
                  \'CloudWatchDestination\': {
                      \'DimensionConfigurations\': [
                          {
                              \'DimensionName\': \'string\',
                              \'DimensionValueSource\': \'MESSAGE_TAG\'|\'EMAIL_HEADER\'|\'LINK_TAG\',
                              \'DefaultDimensionValue\': \'string\'
                          },
                      ]
                  },
                  \'SnsDestination\': {
                      \'TopicArn\': \'string\'
                  },
                  \'PinpointDestination\': {
                      \'ApplicationArn\': \'string\'
                  }
              }
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that you want to add an event destination to.
        
        :type EventDestinationName: string
        :param EventDestinationName: **[REQUIRED]** 
        
          A name that identifies the event destination within the configuration set.
        
        :type EventDestination: dict
        :param EventDestination: **[REQUIRED]** 
        
          An object that defines the event destination.
        
          - **Enabled** *(boolean) --* 
        
            If ``true`` , the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this ``EventDestinationDefinition`` .
        
            If ``false`` , the event destination is disabled. When the event destination is disabled, events aren\'t sent to the specified destinations.
        
          - **MatchingEventTypes** *(list) --* 
        
            An array that specifies which events Amazon Pinpoint should send to the destinations in this ``EventDestinationDefinition`` .
        
            - *(string) --* 
        
              An email sending event type. For example, email sends, opens, and bounces are all email events.
        
          - **KinesisFirehoseDestination** *(dict) --* 
        
            An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.
        
            - **IamRoleArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.
        
            - **DeliveryStreamArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.
        
          - **CloudWatchDestination** *(dict) --* 
        
            An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
        
            - **DimensionConfigurations** *(list) --* **[REQUIRED]** 
        
              An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.
        
              - *(dict) --* 
        
                An object that defines the dimension configuration to use when you send Amazon Pinpoint email events to Amazon CloudWatch.
        
                - **DimensionName** *(string) --* **[REQUIRED]** 
        
                  The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:
        
                  * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                   
                  * It can contain no more than 256 characters. 
                   
                - **DimensionValueSource** *(string) --* **[REQUIRED]** 
        
                  The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .
        
                - **DefaultDimensionValue** *(string) --* **[REQUIRED]** 
        
                  The default value of the dimension that is published to Amazon CloudWatch if you don\'t provide the value of the dimension when you send an email. This value has to meet the following criteria:
        
                  * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                   
                  * It can contain no more than 256 characters. 
                   
          - **SnsDestination** *(dict) --* 
        
            An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.
        
            - **TopicArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
        
          - **PinpointDestination** *(dict) --* 
        
            An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
        
            - **ApplicationArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def create_dedicated_ip_pool(self, PoolName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateDedicatedIpPool>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_dedicated_ip_pool(
              PoolName=\'string\'
          )
        :type PoolName: string
        :param PoolName: **[REQUIRED]** 
        
          The name of the dedicated IP pool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def create_email_identity(self, EmailIdentity: str) -> Dict:
        """
        
        When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. 
        
        When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateEmailIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_email_identity(
              EmailIdentity=\'string\'
          )
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]** 
        
          The email address or domain that you want to verify.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityType\': \'EMAIL_ADDRESS\'|\'DOMAIN\'|\'MANAGED_DOMAIN\',
                \'VerifiedForSendingStatus\': True|False,
                \'DkimAttributes\': {
                    \'SigningEnabled\': True|False,
                    \'Status\': \'PENDING\'|\'SUCCESS\'|\'FAILED\'|\'TEMPORARY_FAILURE\'|\'NOT_STARTED\',
                    \'Tokens\': [
                        \'string\',
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            If the email identity is a domain, this object contains tokens that you can use to create a set of CNAME records. To sucessfully verify your domain, you have to add these records to the DNS configuration for your domain.
        
            If the email identity is an email address, this object is empty. 
        
            - **IdentityType** *(string) --* 
        
              The email identity type.
        
            - **VerifiedForSendingStatus** *(boolean) --* 
        
              Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the `Amazon Pinpoint User Guide <http://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html>`__ .
        
            - **DkimAttributes** *(dict) --* 
        
              An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.
        
              - **SigningEnabled** *(boolean) --* 
        
                If the value is ``true`` , then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. If the value is ``false`` , then the messages that Amazon Pinpoint sends from the identity aren\'t DKIM-signed.
        
              - **Status** *(string) --* 
        
                Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:
        
                * ``PENDING`` – Amazon Pinpoint hasn\'t yet located the DKIM records in the DNS configuration for the domain, but will continue to attempt to locate them. 
                 
                * ``SUCCESS`` – Amazon Pinpoint located the DKIM records in the DNS configuration for the domain and determined that they\'re correct. Amazon Pinpoint can now send DKIM-signed email from the identity. 
                 
                * ``FAILED`` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings for the domain, and won\'t continue to search for them. 
                 
                * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from determining the DKIM status for the domain. 
                 
                * ``NOT_STARTED`` – Amazon Pinpoint hasn\'t yet started searching for the DKIM records in the DKIM records for the domain. 
                 
              - **Tokens** *(list) --* 
        
                A set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint usually detects these records within about 72 hours of adding them to the DNS configuration for your domain.
        
                - *(string) --* 
            
        """
        pass

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict:
        """
        
        In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/DeleteConfigurationSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_configuration_set(
              ConfigurationSetName=\'string\'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def delete_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str) -> Dict:
        """
        
        In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/DeleteConfigurationSetEventDestination>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_configuration_set_event_destination(
              ConfigurationSetName=\'string\',
              EventDestinationName=\'string\'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that contains the event destination that you want to delete.
        
        :type EventDestinationName: string
        :param EventDestinationName: **[REQUIRED]** 
        
          The name of the event destination that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/DeleteDedicatedIpPool>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_dedicated_ip_pool(
              PoolName=\'string\'
          )
        :type PoolName: string
        :param PoolName: **[REQUIRED]** 
        
          The name of the dedicated IP pool that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def delete_email_identity(self, EmailIdentity: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/DeleteEmailIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_email_identity(
              EmailIdentity=\'string\'
          )
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]** 
        
          The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
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

    def get_account(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_account()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SendQuota\': {
                    \'Max24HourSend\': 123.0,
                    \'MaxSendRate\': 123.0,
                    \'SentLast24Hours\': 123.0
                },
                \'SendingEnabled\': True|False,
                \'DedicatedIpAutoWarmupEnabled\': True|False,
                \'EnforcementStatus\': \'string\',
                \'ProductionAccessEnabled\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A list of details about the email-sending capabilities of your Amazon Pinpoint account in the current AWS Region.
        
            - **SendQuota** *(dict) --* 
        
              An object that contains information about the per-day and per-second sending limits for your Amazon Pinpoint account in the current AWS Region.
        
              - **Max24HourSend** *(float) --* 
        
                The maximum number of emails that you can send in the current AWS Region over a 24-hour period. This value is also called your *sending quota* .
        
              - **MaxSendRate** *(float) --* 
        
                The maximum number of emails that you can send per second in the current AWS Region. This value is also called your *maximum sending rate* or your *maximum TPS (transactions per second) rate* .
        
              - **SentLast24Hours** *(float) --* 
        
                The number of emails sent from your Amazon Pinpoint account in the current AWS Region over the past 24 hours.
        
            - **SendingEnabled** *(boolean) --* 
        
              Indicates whether or not email sending is enabled for your Amazon Pinpoint account in the current AWS Region.
        
            - **DedicatedIpAutoWarmupEnabled** *(boolean) --* 
        
              Indicates whether or not the automatic warm-up feature is enabled for dedicated IP addresses that are associated with your account.
        
            - **EnforcementStatus** *(string) --* 
        
              The reputation status of your Amazon Pinpoint account. The status can be one of the following:
        
              * ``HEALTHY`` – There are no reputation-related issues that currently impact your account. 
               
              * ``PROBATION`` – We\'ve identified some issues with your Amazon Pinpoint account. We\'re placing your account under review while you work on correcting these issues. 
               
              * ``SHUTDOWN`` – Your account\'s ability to send email is currently paused because of an issue with the email sent from your account. When you correct the issue, you can contact us and request that your account\'s ability to send email is resumed. 
               
            - **ProductionAccessEnabled** *(boolean) --* 
        
              Indicates whether or not your account has production access in the current AWS Region.
        
              If the value is ``false`` , then your account is in the *sandbox* . When your account is in the sandbox, you can only send email to verified identities. Additionally, the maximum number of emails you can send in a 24-hour period (your sending quota) is 200, and the maximum number of emails you can send per second (your maximum sending rate) is 1.
        
              If the value is ``true`` , then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.
        
        """
        pass

    def get_configuration_set(self, ConfigurationSetName: str) -> Dict:
        """
        
        In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetConfigurationSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_configuration_set(
              ConfigurationSetName=\'string\'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that you want to obtain more information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ConfigurationSetName\': \'string\',
                \'TrackingOptions\': {
                    \'CustomRedirectDomain\': \'string\'
                },
                \'DeliveryOptions\': {
                    \'SendingPoolName\': \'string\'
                },
                \'ReputationOptions\': {
                    \'ReputationMetricsEnabled\': True|False,
                    \'LastFreshStart\': datetime(2015, 1, 1)
                },
                \'SendingOptions\': {
                    \'SendingEnabled\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Information about a configuration set.
        
            - **ConfigurationSetName** *(string) --* 
        
              The name of the configuration set.
        
            - **TrackingOptions** *(dict) --* 
        
              An object that defines the open and click tracking options for emails that you send using the configuration set.
        
              - **CustomRedirectDomain** *(string) --* 
        
                The domain that you want to use for tracking open and click events.
        
            - **DeliveryOptions** *(dict) --* 
        
              An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
        
              - **SendingPoolName** *(string) --* 
        
                The name of the dedicated IP pool that you want to associate with the configuration set.
        
            - **ReputationOptions** *(dict) --* 
        
              An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.
        
              - **ReputationMetricsEnabled** *(boolean) --* 
        
                If ``true`` , tracking of reputation metrics is enabled for the configuration set. If ``false`` , tracking of reputation metrics is disabled for the configuration set.
        
              - **LastFreshStart** *(datetime) --* 
        
                The date and time when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.
        
            - **SendingOptions** *(dict) --* 
        
              An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
        
              - **SendingEnabled** *(boolean) --* 
        
                If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.
        
        """
        pass

    def get_configuration_set_event_destinations(self, ConfigurationSetName: str) -> Dict:
        """
        
        In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetConfigurationSetEventDestinations>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_configuration_set_event_destinations(
              ConfigurationSetName=\'string\'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that contains the event destination.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventDestinations\': [
                    {
                        \'Name\': \'string\',
                        \'Enabled\': True|False,
                        \'MatchingEventTypes\': [
                            \'SEND\'|\'REJECT\'|\'BOUNCE\'|\'COMPLAINT\'|\'DELIVERY\'|\'OPEN\'|\'CLICK\'|\'RENDERING_FAILURE\',
                        ],
                        \'KinesisFirehoseDestination\': {
                            \'IamRoleArn\': \'string\',
                            \'DeliveryStreamArn\': \'string\'
                        },
                        \'CloudWatchDestination\': {
                            \'DimensionConfigurations\': [
                                {
                                    \'DimensionName\': \'string\',
                                    \'DimensionValueSource\': \'MESSAGE_TAG\'|\'EMAIL_HEADER\'|\'LINK_TAG\',
                                    \'DefaultDimensionValue\': \'string\'
                                },
                            ]
                        },
                        \'SnsDestination\': {
                            \'TopicArn\': \'string\'
                        },
                        \'PinpointDestination\': {
                            \'ApplicationArn\': \'string\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Information about an event destination for a configuration set.
        
            - **EventDestinations** *(list) --* 
        
              An array that includes all of the events destinations that have been configured for the configuration set.
        
              - *(dict) --* 
        
                In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
        
                - **Name** *(string) --* 
        
                  A name that identifies the event destination.
        
                - **Enabled** *(boolean) --* 
        
                  If ``true`` , the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this ``EventDestinationDefinition`` .
        
                  If ``false`` , the event destination is disabled. When the event destination is disabled, events aren\'t sent to the specified destinations.
        
                - **MatchingEventTypes** *(list) --* 
        
                  The types of events that Amazon Pinpoint sends to the specified event destinations.
        
                  - *(string) --* 
        
                    An email sending event type. For example, email sends, opens, and bounces are all email events.
        
                - **KinesisFirehoseDestination** *(dict) --* 
        
                  An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.
        
                  - **DeliveryStreamArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.
        
                - **CloudWatchDestination** *(dict) --* 
        
                  An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
        
                  - **DimensionConfigurations** *(list) --* 
        
                    An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.
        
                    - *(dict) --* 
        
                      An object that defines the dimension configuration to use when you send Amazon Pinpoint email events to Amazon CloudWatch.
        
                      - **DimensionName** *(string) --* 
        
                        The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:
        
                        * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                         
                        * It can contain no more than 256 characters. 
                         
                      - **DimensionValueSource** *(string) --* 
        
                        The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .
        
                      - **DefaultDimensionValue** *(string) --* 
        
                        The default value of the dimension that is published to Amazon CloudWatch if you don\'t provide the value of the dimension when you send an email. This value has to meet the following criteria:
        
                        * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                         
                        * It can contain no more than 256 characters. 
                         
                - **SnsDestination** *(dict) --* 
        
                  An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.
        
                  - **TopicArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
        
                - **PinpointDestination** *(dict) --* 
        
                  An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
        
                  - **ApplicationArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
        
        """
        pass

    def get_dedicated_ip(self, Ip: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetDedicatedIp>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_dedicated_ip(
              Ip=\'string\'
          )
        :type Ip: string
        :param Ip: **[REQUIRED]** 
        
          The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that\'s assocaited with your Amazon Pinpoint account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DedicatedIp\': {
                    \'Ip\': \'string\',
                    \'WarmupStatus\': \'IN_PROGRESS\'|\'DONE\',
                    \'WarmupPercentage\': 123,
                    \'PoolName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Information about a dedicated IP address.
        
            - **DedicatedIp** *(dict) --* 
        
              An object that contains information about a dedicated IP address.
        
              - **Ip** *(string) --* 
        
                An IP address that is reserved for use by your Amazon Pinpoint account.
        
              - **WarmupStatus** *(string) --* 
        
                The warm-up status of a dedicated IP address. The status can have one of the following values:
        
                * ``IN_PROGRESS`` – The IP address isn\'t ready to use because the dedicated IP warm-up process is ongoing. 
                 
                * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to use. 
                 
              - **WarmupPercentage** *(integer) --* 
        
                Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the address has completed the warm-up process and is ready for use.
        
              - **PoolName** *(string) --* 
        
                The name of the dedicated IP pool that the IP address is associated with.
        
        """
        pass

    def get_dedicated_ips(self, PoolName: str = None, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetDedicatedIps>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_dedicated_ips(
              PoolName=\'string\',
              NextToken=\'string\',
              PageSize=123
          )
        :type PoolName: string
        :param PoolName: 
        
          The name of the IP pool that the dedicated IP address is associated with.
        
        :type NextToken: string
        :param NextToken: 
        
          A token returned from a previous call to ``GetDedicatedIps`` to indicate the position of the dedicated IP pool in the list of IP pools.
        
        :type PageSize: integer
        :param PageSize: 
        
          The number of results to show in a single call to ``GetDedicatedIpsRequest`` . If the number of results is larger than the number you specified in this parameter, then the response includes a ``NextToken`` element, which you can use to obtain additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DedicatedIps\': [
                    {
                        \'Ip\': \'string\',
                        \'WarmupStatus\': \'IN_PROGRESS\'|\'DONE\',
                        \'WarmupPercentage\': 123,
                        \'PoolName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Information about the dedicated IP addresses that are associated with your Amazon Pinpoint account.
        
            - **DedicatedIps** *(list) --* 
        
              A list of dedicated IP addresses that are reserved for use by your Amazon Pinpoint account.
        
              - *(dict) --* 
        
                Contains information about a dedicated IP address that is associated with your Amazon Pinpoint account.
        
                - **Ip** *(string) --* 
        
                  An IP address that is reserved for use by your Amazon Pinpoint account.
        
                - **WarmupStatus** *(string) --* 
        
                  The warm-up status of a dedicated IP address. The status can have one of the following values:
        
                  * ``IN_PROGRESS`` – The IP address isn\'t ready to use because the dedicated IP warm-up process is ongoing. 
                   
                  * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to use. 
                   
                - **WarmupPercentage** *(integer) --* 
        
                  Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the address has completed the warm-up process and is ready for use.
        
                - **PoolName** *(string) --* 
        
                  The name of the dedicated IP pool that the IP address is associated with.
        
            - **NextToken** *(string) --* 
        
              A token that indicates that there are additional dedicated IP addresses to list. To view additional addresses, issue another request to ``GetDedicatedIps`` , passing this token in the ``NextToken`` parameter.
        
        """
        pass

    def get_email_identity(self, EmailIdentity: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetEmailIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_email_identity(
              EmailIdentity=\'string\'
          )
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]** 
        
          The email identity that you want to retrieve details for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityType\': \'EMAIL_ADDRESS\'|\'DOMAIN\'|\'MANAGED_DOMAIN\',
                \'FeedbackForwardingStatus\': True|False,
                \'VerifiedForSendingStatus\': True|False,
                \'DkimAttributes\': {
                    \'SigningEnabled\': True|False,
                    \'Status\': \'PENDING\'|\'SUCCESS\'|\'FAILED\'|\'TEMPORARY_FAILURE\'|\'NOT_STARTED\',
                    \'Tokens\': [
                        \'string\',
                    ]
                },
                \'MailFromAttributes\': {
                    \'MailFromDomain\': \'string\',
                    \'MailFromDomainStatus\': \'PENDING\'|\'SUCCESS\'|\'FAILED\'|\'TEMPORARY_FAILURE\',
                    \'BehaviorOnMxFailure\': \'USE_DEFAULT_VALUE\'|\'REJECT_MESSAGE\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Details about an email identity.
        
            - **IdentityType** *(string) --* 
        
              The email identity type.
        
            - **FeedbackForwardingStatus** *(boolean) --* 
        
              The feedback forwarding configuration for the identity.
        
              If the value is ``true`` , Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.
        
              When you set this value to ``false`` , Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You\'re required to have a method of tracking bounces and complaints. If you haven\'t set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
        
            - **VerifiedForSendingStatus** *(boolean) --* 
        
              Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the `Amazon Pinpoint User Guide <http://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html>`__ .
        
            - **DkimAttributes** *(dict) --* 
        
              An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.
        
              - **SigningEnabled** *(boolean) --* 
        
                If the value is ``true`` , then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. If the value is ``false`` , then the messages that Amazon Pinpoint sends from the identity aren\'t DKIM-signed.
        
              - **Status** *(string) --* 
        
                Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:
        
                * ``PENDING`` – Amazon Pinpoint hasn\'t yet located the DKIM records in the DNS configuration for the domain, but will continue to attempt to locate them. 
                 
                * ``SUCCESS`` – Amazon Pinpoint located the DKIM records in the DNS configuration for the domain and determined that they\'re correct. Amazon Pinpoint can now send DKIM-signed email from the identity. 
                 
                * ``FAILED`` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings for the domain, and won\'t continue to search for them. 
                 
                * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from determining the DKIM status for the domain. 
                 
                * ``NOT_STARTED`` – Amazon Pinpoint hasn\'t yet started searching for the DKIM records in the DKIM records for the domain. 
                 
              - **Tokens** *(list) --* 
        
                A set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint usually detects these records within about 72 hours of adding them to the DNS configuration for your domain.
        
                - *(string) --* 
            
            - **MailFromAttributes** *(dict) --* 
        
              An object that contains information about the Mail-From attributes for the email identity.
        
              - **MailFromDomain** *(string) --* 
        
                The name of a domain that an email identity uses as a custom MAIL FROM domain.
        
              - **MailFromDomainStatus** *(string) --* 
        
                The status of the MAIL FROM domain. This status can have the following values:
        
                * ``PENDING`` – Amazon Pinpoint hasn\'t started searching for the MX record yet. 
                 
                * ``SUCCESS`` – Amazon Pinpoint detected the required MX record for the MAIL FROM domain. 
                 
                * ``FAILED`` – Amazon Pinpoint can\'t find the required MX record, or the record no longer exists. 
                 
                * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from determining the status of the MAIL FROM domain. 
                 
              - **BehaviorOnMxFailure** *(string) --* 
        
                The action that Amazon Pinpoint to takes if it can\'t read the required MX record for a custom MAIL FROM domain. When you set this value to ``UseDefaultValue`` , Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage`` , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn\'t attempt to deliver the email.
        
                These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.
        
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

    def list_configuration_sets(self, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        
        In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListConfigurationSets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_configuration_sets(
              NextToken=\'string\',
              PageSize=123
          )
        :type NextToken: string
        :param NextToken: 
        
          A token returned from a previous call to ``ListConfigurationSets`` to indicate the position in the list of configuration sets.
        
        :type PageSize: integer
        :param PageSize: 
        
          The number of results to show in a single call to ``ListConfigurationSets`` . If the number of results is larger than the number you specified in this parameter, then the response includes a ``NextToken`` element, which you can use to obtain additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ConfigurationSets\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A list of configuration sets in your Amazon Pinpoint account in the current AWS Region.
        
            - **ConfigurationSets** *(list) --* 
        
              An array that contains all of the configuration sets in your Amazon Pinpoint account in the current AWS Region.
        
              - *(string) --* 
        
                The name of a configuration set.
        
                In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
        
            - **NextToken** *(string) --* 
        
              A token that indicates that there are additional configuration sets to list. To view additional configuration sets, issue another request to ``ListConfigurationSets`` , and pass this token in the ``NextToken`` parameter.
        
        """
        pass

    def list_dedicated_ip_pools(self, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListDedicatedIpPools>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_dedicated_ip_pools(
              NextToken=\'string\',
              PageSize=123
          )
        :type NextToken: string
        :param NextToken: 
        
          A token returned from a previous call to ``ListDedicatedIpPools`` to indicate the position in the list of dedicated IP pools.
        
        :type PageSize: integer
        :param PageSize: 
        
          The number of results to show in a single call to ``ListDedicatedIpPools`` . If the number of results is larger than the number you specified in this parameter, then the response includes a ``NextToken`` element, which you can use to obtain additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DedicatedIpPools\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A list of dedicated IP pools.
        
            - **DedicatedIpPools** *(list) --* 
        
              A list of all of the dedicated IP pools that are associated with your Amazon Pinpoint account.
        
              - *(string) --* 
        
                The name of a dedicated IP pool.
        
            - **NextToken** *(string) --* 
        
              A token that indicates that there are additional IP pools to list. To view additional IP pools, issue another request to ``ListDedicatedIpPools`` , passing this token in the ``NextToken`` parameter.
        
        """
        pass

    def list_email_identities(self, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListEmailIdentities>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_email_identities(
              NextToken=\'string\',
              PageSize=123
          )
        :type NextToken: string
        :param NextToken: 
        
          A token returned from a previous call to ``ListEmailIdentities`` to indicate the position in the list of identities.
        
        :type PageSize: integer
        :param PageSize: 
        
          The number of results to show in a single call to ``ListEmailIdentities`` . If the number of results is larger than the number you specified in this parameter, then the response includes a ``NextToken`` element, which you can use to obtain additional results.
        
          The value you specify has to be at least 0, and can be no more than 1000.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EmailIdentities\': [
                    {
                        \'IdentityType\': \'EMAIL_ADDRESS\'|\'DOMAIN\'|\'MANAGED_DOMAIN\',
                        \'IdentityName\': \'string\',
                        \'SendingEnabled\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A list of all of the identities that you\'ve attempted to verify for use with Amazon Pinpoint, regardless of whether or not those identities were successfully verified.
        
            - **EmailIdentities** *(list) --* 
        
              An array that includes all of the identities associated with your Amazon Pinpoint account.
        
              - *(dict) --* 
        
                Information about an email identity.
        
                - **IdentityType** *(string) --* 
        
                  The email identity type. The identity type can be one of the following:
        
                  * ``EMAIL_ADDRESS`` – The identity is an email address. 
                   
                  * ``DOMAIN`` – The identity is a domain. 
                   
                  * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS. 
                   
                - **IdentityName** *(string) --* 
        
                  The address or domain of the identity.
        
                - **SendingEnabled** *(boolean) --* 
        
                  Indicates whether or not you can send email from the identity.
        
                  In Amazon Pinpoint, an identity is an email address or domain that you send email from. Before you can send email from an identity, you have to demostrate that you own the identity, and that you authorize Amazon Pinpoint to send email from that identity.
        
            - **NextToken** *(string) --* 
        
              A token that indicates that there are additional configuration sets to list. To view additional configuration sets, issue another request to ``ListEmailIdentities`` , and pass this token in the ``NextToken`` parameter.
        
        """
        pass

    def put_account_dedicated_ip_warmup_attributes(self, AutoWarmupEnabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutAccountDedicatedIpWarmupAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_account_dedicated_ip_warmup_attributes(
              AutoWarmupEnabled=True|False
          )
        :type AutoWarmupEnabled: boolean
        :param AutoWarmupEnabled: 
        
          Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon Pinpoint account in the current AWS Region. Set to ``true`` to enable the automatic warm-up feature, or set to ``false`` to disable it.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutAccountSendingAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_account_sending_attributes(
              SendingEnabled=True|False
          )
        :type SendingEnabled: boolean
        :param SendingEnabled: 
        
          Enables or disables your account\'s ability to send email. Set to ``true`` to enable email sending, or set to ``false`` to disable email sending.
        
          .. note::
        
            If AWS paused your account\'s ability to send email, you can\'t use this operation to resume your account\'s ability to send email.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_configuration_set_delivery_options(self, ConfigurationSetName: str, SendingPoolName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_configuration_set_delivery_options(
              ConfigurationSetName=\'string\',
              SendingPoolName=\'string\'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that you want to associate with a dedicated IP pool.
        
        :type SendingPoolName: string
        :param SendingPoolName: 
        
          The name of the dedicated IP pool that you want to associate with the configuration set.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_configuration_set_reputation_options(self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_configuration_set_reputation_options(
              ConfigurationSetName=\'string\',
              ReputationMetricsEnabled=True|False
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that you want to enable or disable reputation metric tracking for.
        
        :type ReputationMetricsEnabled: boolean
        :param ReputationMetricsEnabled: 
        
          If ``true`` , tracking of reputation metrics is enabled for the configuration set. If ``false`` , tracking of reputation metrics is disabled for the configuration set.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_configuration_set_sending_options(self, ConfigurationSetName: str, SendingEnabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutConfigurationSetSendingOptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_configuration_set_sending_options(
              ConfigurationSetName=\'string\',
              SendingEnabled=True|False
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that you want to enable or disable email sending for.
        
        :type SendingEnabled: boolean
        :param SendingEnabled: 
        
          If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_configuration_set_tracking_options(self, ConfigurationSetName: str, CustomRedirectDomain: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_configuration_set_tracking_options(
              ConfigurationSetName=\'string\',
              CustomRedirectDomain=\'string\'
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that you want to add a custom tracking domain to.
        
        :type CustomRedirectDomain: string
        :param CustomRedirectDomain: 
        
          The domain that you want to use to track open and click events.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict:
        """
        
        .. note::
        
          The dedicated IP address that you specify must already exist, and must be associated with your Amazon Pinpoint account. 
        
          The dedicated IP pool you specify must already exist. You can create a new pool by using the ``CreateDedicatedIpPool`` operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutDedicatedIpInPool>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_dedicated_ip_in_pool(
              Ip=\'string\',
              DestinationPoolName=\'string\'
          )
        :type Ip: string
        :param Ip: **[REQUIRED]** 
        
          The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that\'s associated with your Amazon Pinpoint account.
        
        :type DestinationPoolName: string
        :param DestinationPoolName: **[REQUIRED]** 
        
          The name of the IP pool that you want to add the dedicated IP address to. You have to specify an IP pool that already exists.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict:
        """
        
        **Request Syntax** 
        ::
        
          response = client.put_dedicated_ip_warmup_attributes(
              Ip=\'string\',
              WarmupPercentage=123
          )
        :type Ip: string
        :param Ip: **[REQUIRED]** 
        
          The dedicated IP address that you want to update the warm-up attributes for.
        
        :type WarmupPercentage: integer
        :param WarmupPercentage: **[REQUIRED]** 
        
          The warm-up percentage that you want to associate with the dedicated IP address.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_email_identity_dkim_attributes(self, EmailIdentity: str, SigningEnabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_email_identity_dkim_attributes(
              EmailIdentity=\'string\',
              SigningEnabled=True|False
          )
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]** 
        
          The email identity that you want to change the DKIM settings for.
        
        :type SigningEnabled: boolean
        :param SigningEnabled: 
        
          Sets the DKIM signing configuration for the identity.
        
          When you set this value ``true`` , then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. When you set this value to ``false`` , then the messages that Amazon Pinpoint sends from the identity aren\'t DKIM-signed.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_email_identity_feedback_attributes(self, EmailIdentity: str, EmailForwardingEnabled: bool = None) -> Dict:
        """
        
        When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.
        
        When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You\'re required to have a method of tracking bounces and complaints. If you haven\'t set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_email_identity_feedback_attributes(
              EmailIdentity=\'string\',
              EmailForwardingEnabled=True|False
          )
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]** 
        
          The email identity that you want to configure bounce and complaint feedback forwarding for.
        
        :type EmailForwardingEnabled: boolean
        :param EmailForwardingEnabled: 
        
          Sets the feedback forwarding configuration for the identity.
        
          If the value is ``true`` , Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.
        
          When you set this value to ``false`` , Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You\'re required to have a method of tracking bounces and complaints. If you haven\'t set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def put_email_identity_mail_from_attributes(self, EmailIdentity: str, MailFromDomain: str = None, BehaviorOnMxFailure: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutEmailIdentityMailFromAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_email_identity_mail_from_attributes(
              EmailIdentity=\'string\',
              MailFromDomain=\'string\',
              BehaviorOnMxFailure=\'USE_DEFAULT_VALUE\'|\'REJECT_MESSAGE\'
          )
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]** 
        
          The verified email identity that you want to set up the custom MAIL FROM domain for.
        
        :type MailFromDomain: string
        :param MailFromDomain: 
        
          The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria:
        
          * It has to be a subdomain of the verified identity. 
           
          * It can\'t be used to receive email. 
           
          * It can\'t be used in a \"From\" address if the MAIL FROM domain is a destination for feedback forwarding emails. 
           
        :type BehaviorOnMxFailure: string
        :param BehaviorOnMxFailure: 
        
          The action that you want Amazon Pinpoint to take if it can\'t read the required MX record when you send an email. When you set this value to ``UseDefaultValue`` , Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage`` , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn\'t attempt to deliver the email.
        
          These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass

    def send_email(self, Destination: Dict, Content: Dict, FromEmailAddress: str = None, ReplyToAddresses: List = None, FeedbackForwardingEmailAddress: str = None, EmailTags: List = None, ConfigurationSetName: str = None) -> Dict:
        """
        Sends an email message. You can use the Amazon Pinpoint Email API to send two types of messages:
        
        * **Simple** – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon Pinpoint assembles the message for you. 
         
        * **Raw** – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/SendEmail>`_
        
        **Request Syntax** 
        ::
        
          response = client.send_email(
              FromEmailAddress=\'string\',
              Destination={
                  \'ToAddresses\': [
                      \'string\',
                  ],
                  \'CcAddresses\': [
                      \'string\',
                  ],
                  \'BccAddresses\': [
                      \'string\',
                  ]
              },
              ReplyToAddresses=[
                  \'string\',
              ],
              FeedbackForwardingEmailAddress=\'string\',
              Content={
                  \'Simple\': {
                      \'Subject\': {
                          \'Data\': \'string\',
                          \'Charset\': \'string\'
                      },
                      \'Body\': {
                          \'Text\': {
                              \'Data\': \'string\',
                              \'Charset\': \'string\'
                          },
                          \'Html\': {
                              \'Data\': \'string\',
                              \'Charset\': \'string\'
                          }
                      }
                  },
                  \'Raw\': {
                      \'Data\': b\'bytes\'
                  }
              },
              EmailTags=[
                  {
                      \'Name\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              ConfigurationSetName=\'string\'
          )
        :type FromEmailAddress: string
        :param FromEmailAddress: 
        
          The email address that you want to use as the \"From\" address for the email. The address that you specify has to be verified. 
        
        :type Destination: dict
        :param Destination: **[REQUIRED]** 
        
          An object that contains the recipients of the email message.
        
          - **ToAddresses** *(list) --* 
        
            An array that contains the email addresses of the \"To\" recipients for the email.
        
            - *(string) --* 
        
          - **CcAddresses** *(list) --* 
        
            An array that contains the email addresses of the \"CC\" (carbon copy) recipients for the email.
        
            - *(string) --* 
        
          - **BccAddresses** *(list) --* 
        
            An array that contains the email addresses of the \"BCC\" (blind carbon copy) recipients for the email.
        
            - *(string) --* 
        
        :type ReplyToAddresses: list
        :param ReplyToAddresses: 
        
          The \"Reply-to\" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.
        
          - *(string) --* 
        
        :type FeedbackForwardingEmailAddress: string
        :param FeedbackForwardingEmailAddress: 
        
          The address that Amazon Pinpoint should send bounce and complaint notifications to.
        
        :type Content: dict
        :param Content: **[REQUIRED]** 
        
          An object that contains the body of the message. You can send either a Simple message or a Raw message.
        
          - **Simple** *(dict) --* 
        
            The simple email message. The message consists of a subject and a message body.
        
            - **Subject** *(dict) --* **[REQUIRED]** 
        
              The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .
        
              - **Data** *(string) --* **[REQUIRED]** 
        
                The content of the message itself.
        
              - **Charset** *(string) --* 
        
                The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
        
            - **Body** *(dict) --* **[REQUIRED]** 
        
              The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.
        
              - **Text** *(dict) --* 
        
                An object that represents the version of the message that is displayed in email clients that don\'t support HTML, or clients where the recipient has disabled HTML rendering.
        
                - **Data** *(string) --* **[REQUIRED]** 
        
                  The content of the message itself.
        
                - **Charset** *(string) --* 
        
                  The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
        
              - **Html** *(dict) --* 
        
                An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more. 
        
                - **Data** *(string) --* **[REQUIRED]** 
        
                  The content of the message itself.
        
                - **Charset** *(string) --* 
        
                  The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
        
          - **Raw** *(dict) --* 
        
            The raw email message. The message has to meet the following criteria:
        
            * The message has to contain a header and a body, separated by one blank line. 
             
            * All of the required header fields must be present in the message. 
             
            * Each part of a multipart MIME message must be formatted properly. 
             
            * If you include attachments, they must be in a file format that Amazon Pinpoint supports.  
             
            * The entire message must be Base64 encoded. 
             
            * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients\' email clients render the message properly. 
             
            * The length of any single line of text in the message can\'t exceed 1,000 characters. This restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ . 
             
            - **Data** *(bytes) --* **[REQUIRED]** 
        
              The raw email message. The message has to meet the following criteria:
        
              * The message has to contain a header and a body, separated by one blank line. 
               
              * All of the required header fields must be present in the message. 
               
              * Each part of a multipart MIME message must be formatted properly. 
               
              * Attachments must be in a file format that Amazon Pinpoint supports.  
               
              * The entire message must be Base64 encoded. 
               
              * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients\' email clients render the message properly. 
               
              * The length of any single line of text in the message can\'t exceed 1,000 characters. This restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ . 
               
        :type EmailTags: list
        :param EmailTags: 
        
          A list of tags, in the form of name/value pairs, to apply to an email that you send using the ``SendEmail`` operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. 
        
          - *(dict) --* 
        
            Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events. 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the message tag. The message tag name has to meet the following criteria:
        
              * It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-). 
               
              * It can contain no more than 256 characters. 
               
            - **Value** *(string) --* **[REQUIRED]** 
        
              The value of the message tag. The message tag value has to meet the following criteria:
        
              * It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-). 
               
              * It can contain no more than 256 characters. 
               
        :type ConfigurationSetName: string
        :param ConfigurationSetName: 
        
          The name of the configuration set that you want to use when sending the email.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'MessageId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A unique message ID that you receive when Amazon Pinpoint accepts an email for sending.
        
            - **MessageId** *(string) --* 
        
              A unique identifier for the message that is generated when Amazon Pinpoint accepts the message.
        
              .. note::
        
                It is possible for Amazon Pinpoint to accept a message without sending it. This can happen when the message you\'re trying to send has an attachment doesn\'t pass a virus check, or when you send a templated email that contains invalid personalization content, for example.
        
        """
        pass

    def update_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str, EventDestination: Dict) -> Dict:
        """
        
        In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_configuration_set_event_destination(
              ConfigurationSetName=\'string\',
              EventDestinationName=\'string\',
              EventDestination={
                  \'Enabled\': True|False,
                  \'MatchingEventTypes\': [
                      \'SEND\'|\'REJECT\'|\'BOUNCE\'|\'COMPLAINT\'|\'DELIVERY\'|\'OPEN\'|\'CLICK\'|\'RENDERING_FAILURE\',
                  ],
                  \'KinesisFirehoseDestination\': {
                      \'IamRoleArn\': \'string\',
                      \'DeliveryStreamArn\': \'string\'
                  },
                  \'CloudWatchDestination\': {
                      \'DimensionConfigurations\': [
                          {
                              \'DimensionName\': \'string\',
                              \'DimensionValueSource\': \'MESSAGE_TAG\'|\'EMAIL_HEADER\'|\'LINK_TAG\',
                              \'DefaultDimensionValue\': \'string\'
                          },
                      ]
                  },
                  \'SnsDestination\': {
                      \'TopicArn\': \'string\'
                  },
                  \'PinpointDestination\': {
                      \'ApplicationArn\': \'string\'
                  }
              }
          )
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]** 
        
          The name of the configuration set that contains the event destination that you want to modify.
        
        :type EventDestinationName: string
        :param EventDestinationName: **[REQUIRED]** 
        
          The name of the event destination that you want to modify.
        
        :type EventDestination: dict
        :param EventDestination: **[REQUIRED]** 
        
          An object that defines the event destination.
        
          - **Enabled** *(boolean) --* 
        
            If ``true`` , the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this ``EventDestinationDefinition`` .
        
            If ``false`` , the event destination is disabled. When the event destination is disabled, events aren\'t sent to the specified destinations.
        
          - **MatchingEventTypes** *(list) --* 
        
            An array that specifies which events Amazon Pinpoint should send to the destinations in this ``EventDestinationDefinition`` .
        
            - *(string) --* 
        
              An email sending event type. For example, email sends, opens, and bounces are all email events.
        
          - **KinesisFirehoseDestination** *(dict) --* 
        
            An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.
        
            - **IamRoleArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.
        
            - **DeliveryStreamArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.
        
          - **CloudWatchDestination** *(dict) --* 
        
            An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
        
            - **DimensionConfigurations** *(list) --* **[REQUIRED]** 
        
              An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.
        
              - *(dict) --* 
        
                An object that defines the dimension configuration to use when you send Amazon Pinpoint email events to Amazon CloudWatch.
        
                - **DimensionName** *(string) --* **[REQUIRED]** 
        
                  The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:
        
                  * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                   
                  * It can contain no more than 256 characters. 
                   
                - **DimensionValueSource** *(string) --* **[REQUIRED]** 
        
                  The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .
        
                - **DefaultDimensionValue** *(string) --* **[REQUIRED]** 
        
                  The default value of the dimension that is published to Amazon CloudWatch if you don\'t provide the value of the dimension when you send an email. This value has to meet the following criteria:
        
                  * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                   
                  * It can contain no more than 256 characters. 
                   
          - **SnsDestination** *(dict) --* 
        
            An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.
        
            - **TopicArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
        
          - **PinpointDestination** *(dict) --* 
        
            An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
        
            - **ApplicationArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        
        """
        pass
