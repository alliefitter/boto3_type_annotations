from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
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

    def create_configuration_set(self, ConfigurationSetName: str = None, TrackingOptions: Dict = None, DeliveryOptions: Dict = None, ReputationOptions: Dict = None, SendingOptions: Dict = None, Tags: List = None) -> Dict:
        """
        Create a configuration set. *Configuration sets* are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateConfigurationSet>`_
        
        **Request Syntax**
        ::
          response = client.create_configuration_set(
              ConfigurationSetName='string',
              TrackingOptions={
                  'CustomRedirectDomain': 'string'
              },
              DeliveryOptions={
                  'SendingPoolName': 'string'
              },
              ReputationOptions={
                  'ReputationMetricsEnabled': True|False,
                  'LastFreshStart': datetime(2015, 1, 1)
              },
              SendingOptions={
                  'SendingEnabled': True|False
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
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
            The date and time (in Unix time) when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.
        :type SendingOptions: dict
        :param SendingOptions:
          An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
          - **SendingEnabled** *(boolean) --*
            If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.
        :type Tags: list
        :param Tags:
          An object that defines the tags (keys and values) that you want to associate with the configuration set.
          - *(dict) --*
            An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.
            Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. For example, if you have two versions of an Amazon Pinpoint project, one for internal testing and another for external use, you might assign a ``Stack`` tag key to both projects. The value of the ``Stack`` tag key might be ``Test`` for one project and ``Production`` for the other project.
            A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:
            * Tag keys and values are case sensitive.
            * For each associated resource, each tag key must be unique and it can have only one value.
            * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can\'t edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
            * You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.
            - **Key** *(string) --* **[REQUIRED]**
              One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
            - **Value** *(string) --* **[REQUIRED]**
              The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.
        :rtype: dict
        :returns:
        """
        pass

    def create_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str, EventDestination: Dict) -> Dict:
        """
        Create an event destination. In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
        A single configuration set can include more than one event destination.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateConfigurationSetEventDestination>`_
        
        **Request Syntax**
        ::
          response = client.create_configuration_set_event_destination(
              ConfigurationSetName='string',
              EventDestinationName='string',
              EventDestination={
                  'Enabled': True|False,
                  'MatchingEventTypes': [
                      'SEND'|'REJECT'|'BOUNCE'|'COMPLAINT'|'DELIVERY'|'OPEN'|'CLICK'|'RENDERING_FAILURE',
                  ],
                  'KinesisFirehoseDestination': {
                      'IamRoleArn': 'string',
                      'DeliveryStreamArn': 'string'
                  },
                  'CloudWatchDestination': {
                      'DimensionConfigurations': [
                          {
                              'DimensionName': 'string',
                              'DimensionValueSource': 'MESSAGE_TAG'|'EMAIL_HEADER'|'LINK_TAG',
                              'DefaultDimensionValue': 'string'
                          },
                      ]
                  },
                  'SnsDestination': {
                      'TopicArn': 'string'
                  },
                  'PinpointDestination': {
                      'ApplicationArn': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
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
              The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
          - **PinpointDestination** *(dict) --*
            An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
            - **ApplicationArn** *(string) --*
              The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
        :rtype: dict
        :returns:
        """
        pass

    def create_dedicated_ip_pool(self, PoolName: str, Tags: List = None) -> Dict:
        """
        Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your Amazon Pinpoint account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, Amazon Pinpoint sends it using only the IP addresses in the associated pool.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateDedicatedIpPool>`_
        
        **Request Syntax**
        ::
          response = client.create_dedicated_ip_pool(
              PoolName='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type PoolName: string
        :param PoolName: **[REQUIRED]**
          The name of the dedicated IP pool.
        :type Tags: list
        :param Tags:
          An object that defines the tags (keys and values) that you want to associate with the pool.
          - *(dict) --*
            An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.
            Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. For example, if you have two versions of an Amazon Pinpoint project, one for internal testing and another for external use, you might assign a ``Stack`` tag key to both projects. The value of the ``Stack`` tag key might be ``Test`` for one project and ``Production`` for the other project.
            A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:
            * Tag keys and values are case sensitive.
            * For each associated resource, each tag key must be unique and it can have only one value.
            * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can\'t edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
            * You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.
            - **Key** *(string) --* **[REQUIRED]**
              One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
            - **Value** *(string) --* **[REQUIRED]**
              The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.
        :rtype: dict
        :returns:
        """
        pass

    def create_deliverability_test_report(self, FromEmailAddress: str, Content: Dict, ReportName: str = None, Tags: List = None) -> Dict:
        """
        Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon Pinpoint then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the ``GetDeliverabilityTestReport`` operation to view the results of the test.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateDeliverabilityTestReport>`_
        
        **Request Syntax**
        ::
          response = client.create_deliverability_test_report(
              ReportName='string',
              FromEmailAddress='string',
              Content={
                  'Simple': {
                      'Subject': {
                          'Data': 'string',
                          'Charset': 'string'
                      },
                      'Body': {
                          'Text': {
                              'Data': 'string',
                              'Charset': 'string'
                          },
                          'Html': {
                              'Data': 'string',
                              'Charset': 'string'
                          }
                      }
                  },
                  'Raw': {
                      'Data': b'bytes'
                  }
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ReportId': 'string',
                'DeliverabilityTestStatus': 'IN_PROGRESS'|'COMPLETED'
            }
        
        **Response Structure**
          - *(dict) --* 
            Information about the predictive inbox placement test that you created.
            - **ReportId** *(string) --* 
              A unique string that identifies the predictive inbox placement test.
            - **DeliverabilityTestStatus** *(string) --* 
              The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` , then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is ``COMPLETE`` , then the test is finished, and you can use the ``GetDeliverabilityTestReport`` to view the results of the test.
        :type ReportName: string
        :param ReportName:
          A unique name that helps you to identify the predictive inbox placement test when you retrieve the results.
        :type FromEmailAddress: string
        :param FromEmailAddress: **[REQUIRED]**
          The email address that the predictive inbox placement test email was sent from.
        :type Content: dict
        :param Content: **[REQUIRED]**
          The HTML body of the message that you sent when you performed the predictive inbox placement test.
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
        :type Tags: list
        :param Tags:
          An object that defines the tags (keys and values) that you want to associate with the predictive inbox placement test.
          - *(dict) --*
            An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.
            Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. For example, if you have two versions of an Amazon Pinpoint project, one for internal testing and another for external use, you might assign a ``Stack`` tag key to both projects. The value of the ``Stack`` tag key might be ``Test`` for one project and ``Production`` for the other project.
            A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:
            * Tag keys and values are case sensitive.
            * For each associated resource, each tag key must be unique and it can have only one value.
            * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can\'t edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
            * You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.
            - **Key** *(string) --* **[REQUIRED]**
              One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
            - **Value** *(string) --* **[REQUIRED]**
              The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.
        :rtype: dict
        :returns:
        """
        pass

    def create_email_identity(self, EmailIdentity: str, Tags: List = None) -> Dict:
        """
        Verifies an email identity for use with Amazon Pinpoint. In Amazon Pinpoint, an identity is an email address or domain that you use when you send email. Before you can use an identity to send email with Amazon Pinpoint, you first have to verify it. By verifying an address, you demonstrate that you're the owner of the address, and that you've given Amazon Pinpoint permission to send email from the address.
        When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. 
        When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/CreateEmailIdentity>`_
        
        **Request Syntax**
        ::
          response = client.create_email_identity(
              EmailIdentity='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'IdentityType': 'EMAIL_ADDRESS'|'DOMAIN'|'MANAGED_DOMAIN',
                'VerifiedForSendingStatus': True|False,
                'DkimAttributes': {
                    'SigningEnabled': True|False,
                    'Status': 'PENDING'|'SUCCESS'|'FAILED'|'TEMPORARY_FAILURE'|'NOT_STARTED',
                    'Tokens': [
                        'string',
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
              Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the `Amazon Pinpoint User Guide <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html>`__ .
            - **DkimAttributes** *(dict) --* 
              An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.
              - **SigningEnabled** *(boolean) --* 
                If the value is ``true`` , then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. If the value is ``false`` , then the messages that Amazon Pinpoint sends from the identity aren't DKIM-signed.
              - **Status** *(string) --* 
                Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:
                * ``PENDING`` – Amazon Pinpoint hasn't yet located the DKIM records in the DNS configuration for the domain, but will continue to attempt to locate them. 
                * ``SUCCESS`` – Amazon Pinpoint located the DKIM records in the DNS configuration for the domain and determined that they're correct. Amazon Pinpoint can now send DKIM-signed email from the identity. 
                * ``FAILED`` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings for the domain, and won't continue to search for them. 
                * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from determining the DKIM status for the domain. 
                * ``NOT_STARTED`` – Amazon Pinpoint hasn't yet started searching for the DKIM records in the DKIM records for the domain. 
              - **Tokens** *(list) --* 
                A set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint usually detects these records within about 72 hours of adding them to the DNS configuration for your domain.
                - *(string) --* 
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]**
          The email address or domain that you want to verify.
        :type Tags: list
        :param Tags:
          An object that defines the tags (keys and values) that you want to associate with the email identity.
          - *(dict) --*
            An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.
            Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. For example, if you have two versions of an Amazon Pinpoint project, one for internal testing and another for external use, you might assign a ``Stack`` tag key to both projects. The value of the ``Stack`` tag key might be ``Test`` for one project and ``Production`` for the other project.
            A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:
            * Tag keys and values are case sensitive.
            * For each associated resource, each tag key must be unique and it can have only one value.
            * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can\'t edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
            * You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.
            - **Key** *(string) --* **[REQUIRED]**
              One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
            - **Value** *(string) --* **[REQUIRED]**
              The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.
        :rtype: dict
        :returns:
        """
        pass

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict:
        """
        Delete an existing configuration set.
        In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/DeleteConfigurationSet>`_
        
        **Request Syntax**
        ::
          response = client.delete_configuration_set(
              ConfigurationSetName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]**
          The name of the configuration set that you want to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str) -> Dict:
        """
        Delete an event destination.
        In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/DeleteConfigurationSetEventDestination>`_
        
        **Request Syntax**
        ::
          response = client.delete_configuration_set_event_destination(
              ConfigurationSetName='string',
              EventDestinationName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]**
          The name of the configuration set that contains the event destination that you want to delete.
        :type EventDestinationName: string
        :param EventDestinationName: **[REQUIRED]**
          The name of the event destination that you want to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict:
        """
        Delete a dedicated IP pool.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/DeleteDedicatedIpPool>`_
        
        **Request Syntax**
        ::
          response = client.delete_dedicated_ip_pool(
              PoolName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type PoolName: string
        :param PoolName: **[REQUIRED]**
          The name of the dedicated IP pool that you want to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_email_identity(self, EmailIdentity: str) -> Dict:
        """
        Deletes an email identity that you previously verified for use with Amazon Pinpoint. An identity can be either an email address or a domain name.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/DeleteEmailIdentity>`_
        
        **Request Syntax**
        ::
          response = client.delete_email_identity(
              EmailIdentity='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]**
          The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.
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

    def get_account(self) -> Dict:
        """
        Obtain information about the email-sending status and capabilities of your Amazon Pinpoint account in the current AWS Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetAccount>`_
        
        **Request Syntax**
        ::
          response = client.get_account()
        
        **Response Syntax**
        ::
            {
                'SendQuota': {
                    'Max24HourSend': 123.0,
                    'MaxSendRate': 123.0,
                    'SentLast24Hours': 123.0
                },
                'SendingEnabled': True|False,
                'DedicatedIpAutoWarmupEnabled': True|False,
                'EnforcementStatus': 'string',
                'ProductionAccessEnabled': True|False
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
              * ``PROBATION`` – We've identified some issues with your Amazon Pinpoint account. We're placing your account under review while you work on correcting these issues. 
              * ``SHUTDOWN`` – Your account's ability to send email is currently paused because of an issue with the email sent from your account. When you correct the issue, you can contact us and request that your account's ability to send email is resumed. 
            - **ProductionAccessEnabled** *(boolean) --* 
              Indicates whether or not your account has production access in the current AWS Region.
              If the value is ``false`` , then your account is in the *sandbox* . When your account is in the sandbox, you can only send email to verified identities. Additionally, the maximum number of emails you can send in a 24-hour period (your sending quota) is 200, and the maximum number of emails you can send per second (your maximum sending rate) is 1.
              If the value is ``true`` , then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.
        :rtype: dict
        :returns:
        """
        pass

    def get_blacklist_reports(self, BlacklistItemNames: List) -> Dict:
        """
        Retrieve a list of the blacklists that your dedicated IP addresses appear on.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetBlacklistReports>`_
        
        **Request Syntax**
        ::
          response = client.get_blacklist_reports(
              BlacklistItemNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'BlacklistReport': {
                    'string': [
                        {
                            'RblName': 'string',
                            'ListingTime': datetime(2015, 1, 1),
                            'Description': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            An object that contains information about blacklist events.
            - **BlacklistReport** *(dict) --* 
              An object that contains information about a blacklist that one of your dedicated IP addresses appears on.
              - *(string) --* 
                An IP address that you want to obtain blacklist information for.
                - *(list) --* 
                  - *(dict) --* 
                    An object that contains information about a blacklisting event that impacts one of the dedicated IP addresses that is associated with your account.
                    - **RblName** *(string) --* 
                      The name of the blacklist that the IP address appears on.
                    - **ListingTime** *(datetime) --* 
                      The time when the blacklisting event occurred, shown in Unix time format.
                    - **Description** *(string) --* 
                      Additional information about the blacklisting event, as provided by the blacklist maintainer.
        :type BlacklistItemNames: list
        :param BlacklistItemNames: **[REQUIRED]**
          A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon Pinpoint or Amazon SES.
          - *(string) --*
            An IP address that you want to obtain blacklist information for.
        :rtype: dict
        :returns:
        """
        pass

    def get_configuration_set(self, ConfigurationSetName: str) -> Dict:
        """
        Get information about an existing configuration set, including the dedicated IP pool that it's associated with, whether or not it's enabled for sending email, and more.
        In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetConfigurationSet>`_
        
        **Request Syntax**
        ::
          response = client.get_configuration_set(
              ConfigurationSetName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ConfigurationSetName': 'string',
                'TrackingOptions': {
                    'CustomRedirectDomain': 'string'
                },
                'DeliveryOptions': {
                    'SendingPoolName': 'string'
                },
                'ReputationOptions': {
                    'ReputationMetricsEnabled': True|False,
                    'LastFreshStart': datetime(2015, 1, 1)
                },
                'SendingOptions': {
                    'SendingEnabled': True|False
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
                The date and time (in Unix time) when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.
            - **SendingOptions** *(dict) --* 
              An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
              - **SendingEnabled** *(boolean) --* 
                If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]**
          The name of the configuration set that you want to obtain more information about.
        :rtype: dict
        :returns:
        """
        pass

    def get_configuration_set_event_destinations(self, ConfigurationSetName: str) -> Dict:
        """
        Retrieve a list of event destinations that are associated with a configuration set.
        In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetConfigurationSetEventDestinations>`_
        
        **Request Syntax**
        ::
          response = client.get_configuration_set_event_destinations(
              ConfigurationSetName='string'
          )
        
        **Response Syntax**
        ::
            {
                'EventDestinations': [
                    {
                        'Name': 'string',
                        'Enabled': True|False,
                        'MatchingEventTypes': [
                            'SEND'|'REJECT'|'BOUNCE'|'COMPLAINT'|'DELIVERY'|'OPEN'|'CLICK'|'RENDERING_FAILURE',
                        ],
                        'KinesisFirehoseDestination': {
                            'IamRoleArn': 'string',
                            'DeliveryStreamArn': 'string'
                        },
                        'CloudWatchDestination': {
                            'DimensionConfigurations': [
                                {
                                    'DimensionName': 'string',
                                    'DimensionValueSource': 'MESSAGE_TAG'|'EMAIL_HEADER'|'LINK_TAG',
                                    'DefaultDimensionValue': 'string'
                                },
                            ]
                        },
                        'SnsDestination': {
                            'TopicArn': 'string'
                        },
                        'PinpointDestination': {
                            'ApplicationArn': 'string'
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
                  If ``false`` , the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.
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
                        The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:
                        * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                        * It can contain no more than 256 characters. 
                - **SnsDestination** *(dict) --* 
                  An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.
                  - **TopicArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
                - **PinpointDestination** *(dict) --* 
                  An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
                  - **ApplicationArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]**
          The name of the configuration set that contains the event destination.
        :rtype: dict
        :returns:
        """
        pass

    def get_dedicated_ip(self, Ip: str) -> Dict:
        """
        Get information about a dedicated IP address, including the name of the dedicated IP pool that it's associated with, as well information about the automatic warm-up process for the address.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetDedicatedIp>`_
        
        **Request Syntax**
        ::
          response = client.get_dedicated_ip(
              Ip='string'
          )
        
        **Response Syntax**
        ::
            {
                'DedicatedIp': {
                    'Ip': 'string',
                    'WarmupStatus': 'IN_PROGRESS'|'DONE',
                    'WarmupPercentage': 123,
                    'PoolName': 'string'
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
                * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up process is ongoing. 
                * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to use. 
              - **WarmupPercentage** *(integer) --* 
                Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the address has completed the warm-up process and is ready for use.
              - **PoolName** *(string) --* 
                The name of the dedicated IP pool that the IP address is associated with.
        :type Ip: string
        :param Ip: **[REQUIRED]**
          The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that\'s assocaited with your Amazon Pinpoint account.
        :rtype: dict
        :returns:
        """
        pass

    def get_dedicated_ips(self, PoolName: str = None, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        List the dedicated IP addresses that are associated with your Amazon Pinpoint account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetDedicatedIps>`_
        
        **Request Syntax**
        ::
          response = client.get_dedicated_ips(
              PoolName='string',
              NextToken='string',
              PageSize=123
          )
        
        **Response Syntax**
        ::
            {
                'DedicatedIps': [
                    {
                        'Ip': 'string',
                        'WarmupStatus': 'IN_PROGRESS'|'DONE',
                        'WarmupPercentage': 123,
                        'PoolName': 'string'
                    },
                ],
                'NextToken': 'string'
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
                  * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up process is ongoing. 
                  * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to use. 
                - **WarmupPercentage** *(integer) --* 
                  Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the address has completed the warm-up process and is ready for use.
                - **PoolName** *(string) --* 
                  The name of the dedicated IP pool that the IP address is associated with.
            - **NextToken** *(string) --* 
              A token that indicates that there are additional dedicated IP addresses to list. To view additional addresses, issue another request to ``GetDedicatedIps`` , passing this token in the ``NextToken`` parameter.
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
        """
        pass

    def get_deliverability_dashboard_options(self) -> Dict:
        """
        Show the status of the Deliverability dashboard. When the Deliverability dashboard is enabled, you gain access to reputation metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.
        When you use the Deliverability dashboard, you pay a monthly charge of USD$1,250.00, in addition to any other fees that you accrue by using Amazon Pinpoint. If you enable the Deliverability dashboard after the first day of a calendar month, AWS prorates the monthly charge based on how many days have elapsed in the current calendar month.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetDeliverabilityDashboardOptions>`_
        
        **Request Syntax**
        ::
          response = client.get_deliverability_dashboard_options()
        
        **Response Syntax**
        ::
            {
                'DashboardEnabled': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            An object that shows the status of the Deliverability dashboard for your Amazon Pinpoint account.
            - **DashboardEnabled** *(boolean) --* 
              Indicates whether the Deliverability dashboard is enabled. If the value is ``true`` , then the dashboard is enabled.
        :rtype: dict
        :returns:
        """
        pass

    def get_deliverability_test_report(self, ReportId: str) -> Dict:
        """
        Retrieve the results of a predictive inbox placement test.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetDeliverabilityTestReport>`_
        
        **Request Syntax**
        ::
          response = client.get_deliverability_test_report(
              ReportId='string'
          )
        
        **Response Syntax**
        ::
            {
                'DeliverabilityTestReport': {
                    'ReportId': 'string',
                    'ReportName': 'string',
                    'Subject': 'string',
                    'FromEmailAddress': 'string',
                    'CreateDate': datetime(2015, 1, 1),
                    'DeliverabilityTestStatus': 'IN_PROGRESS'|'COMPLETED'
                },
                'OverallPlacement': {
                    'InboxPercentage': 123.0,
                    'SpamPercentage': 123.0,
                    'MissingPercentage': 123.0,
                    'SpfPercentage': 123.0,
                    'DkimPercentage': 123.0
                },
                'IspPlacements': [
                    {
                        'IspName': 'string',
                        'PlacementStatistics': {
                            'InboxPercentage': 123.0,
                            'SpamPercentage': 123.0,
                            'MissingPercentage': 123.0,
                            'SpfPercentage': 123.0,
                            'DkimPercentage': 123.0
                        }
                    },
                ],
                'Message': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The results of the predictive inbox placement test.
            - **DeliverabilityTestReport** *(dict) --* 
              An object that contains the results of the predictive inbox placement test.
              - **ReportId** *(string) --* 
                A unique string that identifies the predictive inbox placement test.
              - **ReportName** *(string) --* 
                A name that helps you identify a predictive inbox placement test report.
              - **Subject** *(string) --* 
                The subject line for an email that you submitted in a predictive inbox placement test.
              - **FromEmailAddress** *(string) --* 
                The sender address that you specified for the predictive inbox placement test.
              - **CreateDate** *(datetime) --* 
                The date and time when the predictive inbox placement test was created, in Unix time format.
              - **DeliverabilityTestStatus** *(string) --* 
                The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` , then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is ``COMPLETE`` , then the test is finished, and you can use the ``GetDeliverabilityTestReport`` to view the results of the test.
            - **OverallPlacement** *(dict) --* 
              An object that specifies how many test messages that were sent during the predictive inbox placement test were delivered to recipients' inboxes, how many were sent to recipients' spam folders, and how many weren't delivered.
              - **InboxPercentage** *(float) --* 
                The percentage of emails that arrived in recipients' inboxes during the predictive inbox placement test.
              - **SpamPercentage** *(float) --* 
                The percentage of emails that arrived in recipients' spam or junk mail folders during the predictive inbox placement test.
              - **MissingPercentage** *(float) --* 
                The percentage of emails that didn't arrive in recipients' inboxes at all during the predictive inbox placement test.
              - **SpfPercentage** *(float) --* 
                The percentage of emails that were authenticated by using Sender Policy Framework (SPF) during the predictive inbox placement test.
              - **DkimPercentage** *(float) --* 
                The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM) during the predictive inbox placement test.
            - **IspPlacements** *(list) --* 
              An object that describes how the test email was handled by several email providers, including Gmail, Hotmail, Yahoo, AOL, and others.
              - *(dict) --* 
                An object that describes how email sent during the predictive inbox placement test was handled by a certain email provider.
                - **IspName** *(string) --* 
                  The name of the email provider that the inbox placement data applies to.
                - **PlacementStatistics** *(dict) --* 
                  An object that contains inbox placement metrics for a specific email provider.
                  - **InboxPercentage** *(float) --* 
                    The percentage of emails that arrived in recipients' inboxes during the predictive inbox placement test.
                  - **SpamPercentage** *(float) --* 
                    The percentage of emails that arrived in recipients' spam or junk mail folders during the predictive inbox placement test.
                  - **MissingPercentage** *(float) --* 
                    The percentage of emails that didn't arrive in recipients' inboxes at all during the predictive inbox placement test.
                  - **SpfPercentage** *(float) --* 
                    The percentage of emails that were authenticated by using Sender Policy Framework (SPF) during the predictive inbox placement test.
                  - **DkimPercentage** *(float) --* 
                    The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM) during the predictive inbox placement test.
            - **Message** *(string) --* 
              An object that contains the message that you sent when you performed this predictive inbox placement test.
        :type ReportId: string
        :param ReportId: **[REQUIRED]**
          A unique string that identifies the predictive inbox placement test.
        :rtype: dict
        :returns:
        """
        pass

    def get_domain_statistics_report(self, Domain: str, StartDate: datetime, EndDate: datetime) -> Dict:
        """
        Retrieve inbox placement and engagement rates for the domains that you use to send email.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetDomainStatisticsReport>`_
        
        **Request Syntax**
        ::
          response = client.get_domain_statistics_report(
              Domain='string',
              StartDate=datetime(2015, 1, 1),
              EndDate=datetime(2015, 1, 1)
          )
        
        **Response Syntax**
        ::
            {
                'OverallVolume': {
                    'VolumeStatistics': {
                        'InboxRawCount': 123,
                        'SpamRawCount': 123,
                        'ProjectedInbox': 123,
                        'ProjectedSpam': 123
                    },
                    'ReadRatePercent': 123.0,
                    'DomainIspPlacements': [
                        {
                            'IspName': 'string',
                            'InboxRawCount': 123,
                            'SpamRawCount': 123,
                            'InboxPercentage': 123.0,
                            'SpamPercentage': 123.0
                        },
                    ]
                },
                'DailyVolumes': [
                    {
                        'StartDate': datetime(2015, 1, 1),
                        'VolumeStatistics': {
                            'InboxRawCount': 123,
                            'SpamRawCount': 123,
                            'ProjectedInbox': 123,
                            'ProjectedSpam': 123
                        },
                        'DomainIspPlacements': [
                            {
                                'IspName': 'string',
                                'InboxRawCount': 123,
                                'SpamRawCount': 123,
                                'InboxPercentage': 123.0,
                                'SpamPercentage': 123.0
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            An object that includes statistics that are related to the domain that you specified.
            - **OverallVolume** *(dict) --* 
              An object that contains deliverability metrics for the domain that you specified. The data in this object is a summary of all of the data that was collected from the ``StartDate`` to the ``EndDate`` .
              - **VolumeStatistics** *(dict) --* 
                An object that contains information about the numbers of messages that arrived in recipients' inboxes and junk mail folders.
                - **InboxRawCount** *(integer) --* 
                  The total number of emails that arrived in recipients' inboxes.
                - **SpamRawCount** *(integer) --* 
                  The total number of emails that arrived in recipients' spam or junk mail folders.
                - **ProjectedInbox** *(integer) --* 
                  An estimate of the percentage of emails sent from the current domain that will arrive in recipients' inboxes.
                - **ProjectedSpam** *(integer) --* 
                  An estimate of the percentage of emails sent from the current domain that will arrive in recipients' spam or junk mail folders.
              - **ReadRatePercent** *(float) --* 
                The percentage of emails that were sent from the domain that were read by their recipients.
              - **DomainIspPlacements** *(list) --* 
                An object that contains inbox and junk mail placement metrics for individual email providers.
                - *(dict) --* 
                  An object that contains inbox placement data for email sent from one of your email domains to a specific email provider.
                  - **IspName** *(string) --* 
                    The name of the email provider that the inbox placement data applies to.
                  - **InboxRawCount** *(integer) --* 
                    The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.
                  - **SpamRawCount** *(integer) --* 
                    The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.
                  - **InboxPercentage** *(float) --* 
                    The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.
                  - **SpamPercentage** *(float) --* 
                    The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.
            - **DailyVolumes** *(list) --* 
              An object that contains deliverability metrics for the domain that you specified. This object contains data for each day, starting on the ``StartDate`` and ending on the ``EndDate`` .
              - *(dict) --* 
                An object that contains information about the volume of email sent on each day of the analysis period.
                - **StartDate** *(datetime) --* 
                  The date that the DailyVolume metrics apply to, in Unix time.
                - **VolumeStatistics** *(dict) --* 
                  An object that contains inbox placement metrics for a specific day in the analysis period.
                  - **InboxRawCount** *(integer) --* 
                    The total number of emails that arrived in recipients' inboxes.
                  - **SpamRawCount** *(integer) --* 
                    The total number of emails that arrived in recipients' spam or junk mail folders.
                  - **ProjectedInbox** *(integer) --* 
                    An estimate of the percentage of emails sent from the current domain that will arrive in recipients' inboxes.
                  - **ProjectedSpam** *(integer) --* 
                    An estimate of the percentage of emails sent from the current domain that will arrive in recipients' spam or junk mail folders.
                - **DomainIspPlacements** *(list) --* 
                  An object that contains inbox placement metrics for a specifid day in the analysis period, broken out by the recipient's email provider.
                  - *(dict) --* 
                    An object that contains inbox placement data for email sent from one of your email domains to a specific email provider.
                    - **IspName** *(string) --* 
                      The name of the email provider that the inbox placement data applies to.
                    - **InboxRawCount** *(integer) --* 
                      The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.
                    - **SpamRawCount** *(integer) --* 
                      The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.
                    - **InboxPercentage** *(float) --* 
                      The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.
                    - **SpamPercentage** *(float) --* 
                      The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.
        :type Domain: string
        :param Domain: **[REQUIRED]**
          The domain that you want to obtain deliverability metrics for.
        :type StartDate: datetime
        :param StartDate: **[REQUIRED]**
          The first day (in Unix time) that you want to obtain domain deliverability metrics for.
        :type EndDate: datetime
        :param EndDate: **[REQUIRED]**
          The last day (in Unix time) that you want to obtain domain deliverability metrics for. The ``EndDate`` that you specify has to be less than or equal to 30 days after the ``StartDate`` .
        :rtype: dict
        :returns:
        """
        pass

    def get_email_identity(self, EmailIdentity: str) -> Dict:
        """
        Provides information about a specific identity associated with your Amazon Pinpoint account, including the identity's verification status, its DKIM authentication status, and its custom Mail-From settings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetEmailIdentity>`_
        
        **Request Syntax**
        ::
          response = client.get_email_identity(
              EmailIdentity='string'
          )
        
        **Response Syntax**
        ::
            {
                'IdentityType': 'EMAIL_ADDRESS'|'DOMAIN'|'MANAGED_DOMAIN',
                'FeedbackForwardingStatus': True|False,
                'VerifiedForSendingStatus': True|False,
                'DkimAttributes': {
                    'SigningEnabled': True|False,
                    'Status': 'PENDING'|'SUCCESS'|'FAILED'|'TEMPORARY_FAILURE'|'NOT_STARTED',
                    'Tokens': [
                        'string',
                    ]
                },
                'MailFromAttributes': {
                    'MailFromDomain': 'string',
                    'MailFromDomainStatus': 'PENDING'|'SUCCESS'|'FAILED'|'TEMPORARY_FAILURE',
                    'BehaviorOnMxFailure': 'USE_DEFAULT_VALUE'|'REJECT_MESSAGE'
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
              When you set this value to ``false`` , Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
            - **VerifiedForSendingStatus** *(boolean) --* 
              Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the `Amazon Pinpoint User Guide <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html>`__ .
            - **DkimAttributes** *(dict) --* 
              An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.
              - **SigningEnabled** *(boolean) --* 
                If the value is ``true`` , then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. If the value is ``false`` , then the messages that Amazon Pinpoint sends from the identity aren't DKIM-signed.
              - **Status** *(string) --* 
                Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:
                * ``PENDING`` – Amazon Pinpoint hasn't yet located the DKIM records in the DNS configuration for the domain, but will continue to attempt to locate them. 
                * ``SUCCESS`` – Amazon Pinpoint located the DKIM records in the DNS configuration for the domain and determined that they're correct. Amazon Pinpoint can now send DKIM-signed email from the identity. 
                * ``FAILED`` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings for the domain, and won't continue to search for them. 
                * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from determining the DKIM status for the domain. 
                * ``NOT_STARTED`` – Amazon Pinpoint hasn't yet started searching for the DKIM records in the DKIM records for the domain. 
              - **Tokens** *(list) --* 
                A set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint usually detects these records within about 72 hours of adding them to the DNS configuration for your domain.
                - *(string) --* 
            - **MailFromAttributes** *(dict) --* 
              An object that contains information about the Mail-From attributes for the email identity.
              - **MailFromDomain** *(string) --* 
                The name of a domain that an email identity uses as a custom MAIL FROM domain.
              - **MailFromDomainStatus** *(string) --* 
                The status of the MAIL FROM domain. This status can have the following values:
                * ``PENDING`` – Amazon Pinpoint hasn't started searching for the MX record yet. 
                * ``SUCCESS`` – Amazon Pinpoint detected the required MX record for the MAIL FROM domain. 
                * ``FAILED`` – Amazon Pinpoint can't find the required MX record, or the record no longer exists. 
                * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from determining the status of the MAIL FROM domain. 
              - **BehaviorOnMxFailure** *(string) --* 
                The action that Amazon Pinpoint to takes if it can't read the required MX record for a custom MAIL FROM domain. When you set this value to ``UseDefaultValue`` , Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage`` , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to deliver the email.
                These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]**
          The email identity that you want to retrieve details for.
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

    def list_configuration_sets(self, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        List all of the configuration sets associated with your Amazon Pinpoint account in the current region.
        In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListConfigurationSets>`_
        
        **Request Syntax**
        ::
          response = client.list_configuration_sets(
              NextToken='string',
              PageSize=123
          )
        
        **Response Syntax**
        ::
            {
                'ConfigurationSets': [
                    'string',
                ],
                'NextToken': 'string'
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
        :type NextToken: string
        :param NextToken:
          A token returned from a previous call to ``ListConfigurationSets`` to indicate the position in the list of configuration sets.
        :type PageSize: integer
        :param PageSize:
          The number of results to show in a single call to ``ListConfigurationSets`` . If the number of results is larger than the number you specified in this parameter, then the response includes a ``NextToken`` element, which you can use to obtain additional results.
        :rtype: dict
        :returns:
        """
        pass

    def list_dedicated_ip_pools(self, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        List all of the dedicated IP pools that exist in your Amazon Pinpoint account in the current AWS Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListDedicatedIpPools>`_
        
        **Request Syntax**
        ::
          response = client.list_dedicated_ip_pools(
              NextToken='string',
              PageSize=123
          )
        
        **Response Syntax**
        ::
            {
                'DedicatedIpPools': [
                    'string',
                ],
                'NextToken': 'string'
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
        :type NextToken: string
        :param NextToken:
          A token returned from a previous call to ``ListDedicatedIpPools`` to indicate the position in the list of dedicated IP pools.
        :type PageSize: integer
        :param PageSize:
          The number of results to show in a single call to ``ListDedicatedIpPools`` . If the number of results is larger than the number you specified in this parameter, then the response includes a ``NextToken`` element, which you can use to obtain additional results.
        :rtype: dict
        :returns:
        """
        pass

    def list_deliverability_test_reports(self, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        Show a list of the predictive inbox placement tests that you've performed, regardless of their statuses. For predictive inbox placement tests that are complete, you can use the ``GetDeliverabilityTestReport`` operation to view the results.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListDeliverabilityTestReports>`_
        
        **Request Syntax**
        ::
          response = client.list_deliverability_test_reports(
              NextToken='string',
              PageSize=123
          )
        
        **Response Syntax**
        ::
            {
                'DeliverabilityTestReports': [
                    {
                        'ReportId': 'string',
                        'ReportName': 'string',
                        'Subject': 'string',
                        'FromEmailAddress': 'string',
                        'CreateDate': datetime(2015, 1, 1),
                        'DeliverabilityTestStatus': 'IN_PROGRESS'|'COMPLETED'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of the predictive inbox placement test reports that are available for your account, regardless of whether or not those tests are complete.
            - **DeliverabilityTestReports** *(list) --* 
              An object that contains a lists of predictive inbox placement tests that you've performed.
              - *(dict) --* 
                An object that contains metadata related to a predictive inbox placement test.
                - **ReportId** *(string) --* 
                  A unique string that identifies the predictive inbox placement test.
                - **ReportName** *(string) --* 
                  A name that helps you identify a predictive inbox placement test report.
                - **Subject** *(string) --* 
                  The subject line for an email that you submitted in a predictive inbox placement test.
                - **FromEmailAddress** *(string) --* 
                  The sender address that you specified for the predictive inbox placement test.
                - **CreateDate** *(datetime) --* 
                  The date and time when the predictive inbox placement test was created, in Unix time format.
                - **DeliverabilityTestStatus** *(string) --* 
                  The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` , then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is ``COMPLETE`` , then the test is finished, and you can use the ``GetDeliverabilityTestReport`` to view the results of the test.
            - **NextToken** *(string) --* 
              A token that indicates that there are additional predictive inbox placement tests to list. To view additional predictive inbox placement tests, issue another request to ``ListDeliverabilityTestReports`` , and pass this token in the ``NextToken`` parameter.
        :type NextToken: string
        :param NextToken:
          A token returned from a previous call to ``ListDeliverabilityTestReports`` to indicate the position in the list of predictive inbox placement tests.
        :type PageSize: integer
        :param PageSize:
          The number of results to show in a single call to ``ListDeliverabilityTestReports`` . If the number of results is larger than the number you specified in this parameter, then the response includes a ``NextToken`` element, which you can use to obtain additional results.
          The value you specify has to be at least 0, and can be no more than 1000.
        :rtype: dict
        :returns:
        """
        pass

    def list_email_identities(self, NextToken: str = None, PageSize: int = None) -> Dict:
        """
        Returns a list of all of the email identities that are associated with your Amazon Pinpoint account. An identity can be either an email address or a domain. This operation returns identities that are verified as well as those that aren't.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListEmailIdentities>`_
        
        **Request Syntax**
        ::
          response = client.list_email_identities(
              NextToken='string',
              PageSize=123
          )
        
        **Response Syntax**
        ::
            {
                'EmailIdentities': [
                    {
                        'IdentityType': 'EMAIL_ADDRESS'|'DOMAIN'|'MANAGED_DOMAIN',
                        'IdentityName': 'string',
                        'SendingEnabled': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of all of the identities that you've attempted to verify for use with Amazon Pinpoint, regardless of whether or not those identities were successfully verified.
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
        :type NextToken: string
        :param NextToken:
          A token returned from a previous call to ``ListEmailIdentities`` to indicate the position in the list of identities.
        :type PageSize: integer
        :param PageSize:
          The number of results to show in a single call to ``ListEmailIdentities`` . If the number of results is larger than the number you specified in this parameter, then the response includes a ``NextToken`` element, which you can use to obtain additional results.
          The value you specify has to be at least 0, and can be no more than 1000.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        """
        Retrieve a list of the tags (keys and values) that are associated with a specific resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Each tag consists of a required *tag key* and an optional associated *tag value* . A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tags** *(list) --* 
              An array that lists all the tags that are associated with the resource. Each tag consists of a required tag key (``Key`` ) and an associated tag value (``Value`` )
              - *(dict) --* 
                An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.
                Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. For example, if you have two versions of an Amazon Pinpoint project, one for internal testing and another for external use, you might assign a ``Stack`` tag key to both projects. The value of the ``Stack`` tag key might be ``Test`` for one project and ``Production`` for the other project.
                A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:
                * Tag keys and values are case sensitive. 
                * For each associated resource, each tag key must be unique and it can have only one value. 
                * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can't edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource. 
                * You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account. 
                - **Key** *(string) --* 
                  One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
                - **Value** *(string) --* 
                  The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource that you want to retrieve tag information for.
        :rtype: dict
        :returns:
        """
        pass

    def put_account_dedicated_ip_warmup_attributes(self, AutoWarmupEnabled: bool = None) -> Dict:
        """
        Enable or disable the automatic warm-up feature for dedicated IP addresses.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutAccountDedicatedIpWarmupAttributes>`_
        
        **Request Syntax**
        ::
          response = client.put_account_dedicated_ip_warmup_attributes(
              AutoWarmupEnabled=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type AutoWarmupEnabled: boolean
        :param AutoWarmupEnabled:
          Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon Pinpoint account in the current AWS Region. Set to ``true`` to enable the automatic warm-up feature, or set to ``false`` to disable it.
        :rtype: dict
        :returns:
        """
        pass

    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict:
        """
        Enable or disable the ability of your account to send email.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutAccountSendingAttributes>`_
        
        **Request Syntax**
        ::
          response = client.put_account_sending_attributes(
              SendingEnabled=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type SendingEnabled: boolean
        :param SendingEnabled:
          Enables or disables your account\'s ability to send email. Set to ``true`` to enable email sending, or set to ``false`` to disable email sending.
          .. note::
            If AWS paused your account\'s ability to send email, you can\'t use this operation to resume your account\'s ability to send email.
        :rtype: dict
        :returns:
        """
        pass

    def put_configuration_set_delivery_options(self, ConfigurationSetName: str, SendingPoolName: str = None) -> Dict:
        """
        Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions>`_
        
        **Request Syntax**
        ::
          response = client.put_configuration_set_delivery_options(
              ConfigurationSetName='string',
              SendingPoolName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]**
          The name of the configuration set that you want to associate with a dedicated IP pool.
        :type SendingPoolName: string
        :param SendingPoolName:
          The name of the dedicated IP pool that you want to associate with the configuration set.
        :rtype: dict
        :returns:
        """
        pass

    def put_configuration_set_reputation_options(self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None) -> Dict:
        """
        Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific AWS Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutConfigurationSetReputationOptions>`_
        
        **Request Syntax**
        ::
          response = client.put_configuration_set_reputation_options(
              ConfigurationSetName='string',
              ReputationMetricsEnabled=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]**
          The name of the configuration set that you want to enable or disable reputation metric tracking for.
        :type ReputationMetricsEnabled: boolean
        :param ReputationMetricsEnabled:
          If ``true`` , tracking of reputation metrics is enabled for the configuration set. If ``false`` , tracking of reputation metrics is disabled for the configuration set.
        :rtype: dict
        :returns:
        """
        pass

    def put_configuration_set_sending_options(self, ConfigurationSetName: str, SendingEnabled: bool = None) -> Dict:
        """
        Enable or disable email sending for messages that use a particular configuration set in a specific AWS Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutConfigurationSetSendingOptions>`_
        
        **Request Syntax**
        ::
          response = client.put_configuration_set_sending_options(
              ConfigurationSetName='string',
              SendingEnabled=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]**
          The name of the configuration set that you want to enable or disable email sending for.
        :type SendingEnabled: boolean
        :param SendingEnabled:
          If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.
        :rtype: dict
        :returns:
        """
        pass

    def put_configuration_set_tracking_options(self, ConfigurationSetName: str, CustomRedirectDomain: str = None) -> Dict:
        """
        Specify a custom domain to use for open and click tracking elements in email that you send using Amazon Pinpoint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutConfigurationSetTrackingOptions>`_
        
        **Request Syntax**
        ::
          response = client.put_configuration_set_tracking_options(
              ConfigurationSetName='string',
              CustomRedirectDomain='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type ConfigurationSetName: string
        :param ConfigurationSetName: **[REQUIRED]**
          The name of the configuration set that you want to add a custom tracking domain to.
        :type CustomRedirectDomain: string
        :param CustomRedirectDomain:
          The domain that you want to use to track open and click events.
        :rtype: dict
        :returns:
        """
        pass

    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict:
        """
        Move a dedicated IP address to an existing dedicated IP pool.
        .. note::
          The dedicated IP address that you specify must already exist, and must be associated with your Amazon Pinpoint account. 
          The dedicated IP pool you specify must already exist. You can create a new pool by using the ``CreateDedicatedIpPool`` operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutDedicatedIpInPool>`_
        
        **Request Syntax**
        ::
          response = client.put_dedicated_ip_in_pool(
              Ip='string',
              DestinationPoolName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type Ip: string
        :param Ip: **[REQUIRED]**
          The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that\'s associated with your Amazon Pinpoint account.
        :type DestinationPoolName: string
        :param DestinationPoolName: **[REQUIRED]**
          The name of the IP pool that you want to add the dedicated IP address to. You have to specify an IP pool that already exists.
        :rtype: dict
        :returns:
        """
        pass

    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutDedicatedIpWarmupAttributes>`_
        
        **Request Syntax**
        ::
          response = client.put_dedicated_ip_warmup_attributes(
              Ip='string',
              WarmupPercentage=123
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type Ip: string
        :param Ip: **[REQUIRED]**
          The dedicated IP address that you want to update the warm-up attributes for.
        :type WarmupPercentage: integer
        :param WarmupPercentage: **[REQUIRED]**
          The warm-up percentage that you want to associate with the dedicated IP address.
        :rtype: dict
        :returns:
        """
        pass

    def put_deliverability_dashboard_option(self, DashboardEnabled: bool) -> Dict:
        """
        Enable or disable the Deliverability dashboard. When you enable the Deliverability dashboard, you gain access to reputation metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.
        When you use the Deliverability dashboard, you pay a monthly charge of USD$1,250.00, in addition to any other fees that you accrue by using Amazon Pinpoint. If you enable the Deliverability dashboard after the first day of a calendar month, we prorate the monthly charge based on how many days have elapsed in the current calendar month.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutDeliverabilityDashboardOption>`_
        
        **Request Syntax**
        ::
          response = client.put_deliverability_dashboard_option(
              DashboardEnabled=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            A response that indicates whether the Deliverability dashboard is enabled for your Amazon Pinpoint account.
        :type DashboardEnabled: boolean
        :param DashboardEnabled: **[REQUIRED]**
          Indicates whether the Deliverability dashboard is enabled. If the value is ``true`` , then the dashboard is enabled.
        :rtype: dict
        :returns:
        """
        pass

    def put_email_identity_dkim_attributes(self, EmailIdentity: str, SigningEnabled: bool = None) -> Dict:
        """
        Used to enable or disable DKIM authentication for an email identity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutEmailIdentityDkimAttributes>`_
        
        **Request Syntax**
        ::
          response = client.put_email_identity_dkim_attributes(
              EmailIdentity='string',
              SigningEnabled=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
        :type EmailIdentity: string
        :param EmailIdentity: **[REQUIRED]**
          The email identity that you want to change the DKIM settings for.
        :type SigningEnabled: boolean
        :param SigningEnabled:
          Sets the DKIM signing configuration for the identity.
          When you set this value ``true`` , then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. When you set this value to ``false`` , then the messages that Amazon Pinpoint sends from the identity aren\'t DKIM-signed.
        :rtype: dict
        :returns:
        """
        pass

    def put_email_identity_feedback_attributes(self, EmailIdentity: str, EmailForwardingEnabled: bool = None) -> Dict:
        """
        Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.
        When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.
        When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes>`_
        
        **Request Syntax**
        ::
          response = client.put_email_identity_feedback_attributes(
              EmailIdentity='string',
              EmailForwardingEnabled=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
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
        """
        pass

    def put_email_identity_mail_from_attributes(self, EmailIdentity: str, MailFromDomain: str = None, BehaviorOnMxFailure: str = None) -> Dict:
        """
        Used to enable or disable the custom Mail-From domain configuration for an email identity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/PutEmailIdentityMailFromAttributes>`_
        
        **Request Syntax**
        ::
          response = client.put_email_identity_mail_from_attributes(
              EmailIdentity='string',
              MailFromDomain='string',
              BehaviorOnMxFailure='USE_DEFAULT_VALUE'|'REJECT_MESSAGE'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
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
              FromEmailAddress='string',
              Destination={
                  'ToAddresses': [
                      'string',
                  ],
                  'CcAddresses': [
                      'string',
                  ],
                  'BccAddresses': [
                      'string',
                  ]
              },
              ReplyToAddresses=[
                  'string',
              ],
              FeedbackForwardingEmailAddress='string',
              Content={
                  'Simple': {
                      'Subject': {
                          'Data': 'string',
                          'Charset': 'string'
                      },
                      'Body': {
                          'Text': {
                              'Data': 'string',
                              'Charset': 'string'
                          },
                          'Html': {
                              'Data': 'string',
                              'Charset': 'string'
                          }
                      }
                  },
                  'Raw': {
                      'Data': b'bytes'
                  }
              },
              EmailTags=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              ConfigurationSetName='string'
          )
        
        **Response Syntax**
        ::
            {
                'MessageId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            A unique message ID that you receive when Amazon Pinpoint accepts an email for sending.
            - **MessageId** *(string) --* 
              A unique identifier for the message that is generated when Amazon Pinpoint accepts the message.
              .. note::
                It is possible for Amazon Pinpoint to accept a message without sending it. This can happen when the message you're trying to send has an attachment doesn't pass a virus check, or when you send a templated email that contains invalid personalization content, for example.
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
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        """
        Add one or more tags (keys and values) to one or more specified resources. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.
        Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource that you want to add one or more tags to.
        :type Tags: list
        :param Tags: **[REQUIRED]**
          A list of the tags that you want to add to the resource. A tag consists of a required tag key (``Key`` ) and an associated tag value (``Value`` ). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.
          - *(dict) --*
            An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.
            Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. For example, if you have two versions of an Amazon Pinpoint project, one for internal testing and another for external use, you might assign a ``Stack`` tag key to both projects. The value of the ``Stack`` tag key might be ``Test`` for one project and ``Production`` for the other project.
            A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:
            * Tag keys and values are case sensitive.
            * For each associated resource, each tag key must be unique and it can have only one value.
            * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can\'t edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
            * You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.
            - **Key** *(string) --* **[REQUIRED]**
              One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
            - **Value** *(string) --* **[REQUIRED]**
              The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        """
        Remove one or more tags (keys and values) from a specified resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from.
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.
          To remove more than one tag from the resource, append the ``TagKeys`` parameter and argument for each additional tag to remove, separated by an ampersand. For example: ``/v1/email/tags?ResourceArn=ResourceArn&TagKeys=Key1&TagKeys=Key2``
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str, EventDestination: Dict) -> Dict:
        """
        Update the configuration of an event destination for a configuration set.
        In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/UpdateConfigurationSetEventDestination>`_
        
        **Request Syntax**
        ::
          response = client.update_configuration_set_event_destination(
              ConfigurationSetName='string',
              EventDestinationName='string',
              EventDestination={
                  'Enabled': True|False,
                  'MatchingEventTypes': [
                      'SEND'|'REJECT'|'BOUNCE'|'COMPLAINT'|'DELIVERY'|'OPEN'|'CLICK'|'RENDERING_FAILURE',
                  ],
                  'KinesisFirehoseDestination': {
                      'IamRoleArn': 'string',
                      'DeliveryStreamArn': 'string'
                  },
                  'CloudWatchDestination': {
                      'DimensionConfigurations': [
                          {
                              'DimensionName': 'string',
                              'DimensionValueSource': 'MESSAGE_TAG'|'EMAIL_HEADER'|'LINK_TAG',
                              'DefaultDimensionValue': 'string'
                          },
                      ]
                  },
                  'SnsDestination': {
                      'TopicArn': 'string'
                  },
                  'PinpointDestination': {
                      'ApplicationArn': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            An HTTP 200 response if the request succeeds, or an error message if the request fails.
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
              The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
          - **PinpointDestination** *(dict) --*
            An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
            - **ApplicationArn** *(string) --*
              The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
        :rtype: dict
        :returns:
        """
        pass
