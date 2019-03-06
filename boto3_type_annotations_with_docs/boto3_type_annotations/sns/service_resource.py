from typing import Union
from typing import List
from typing import Optional
from boto3.resources.collection import ResourceCollection
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    platform_applications: 'platform_applications'
    subscriptions: 'subscriptions'
    topics: 'topics'

    def PlatformApplication(self, arn: str = None) -> 'PlatformApplication':
        """
        Creates a PlatformApplication resource.::
          platform_application = sns.PlatformApplication('arn')
        :type arn: string
        :param arn: The PlatformApplication\'s arn identifier. This **must** be set.
        :rtype: :py:class:`SNS.PlatformApplication`
        :returns: A PlatformApplication resource
        """
        pass

    def PlatformEndpoint(self, arn: str = None) -> 'PlatformEndpoint':
        """
        Creates a PlatformEndpoint resource.::
          platform_endpoint = sns.PlatformEndpoint('arn')
        :type arn: string
        :param arn: The PlatformEndpoint\'s arn identifier. This **must** be set.
        :rtype: :py:class:`SNS.PlatformEndpoint`
        :returns: A PlatformEndpoint resource
        """
        pass

    def Subscription(self, arn: str = None) -> 'Subscription':
        """
        Creates a Subscription resource.::
          subscription = sns.Subscription('arn')
        :type arn: string
        :param arn: The Subscription\'s arn identifier. This **must** be set.
        :rtype: :py:class:`SNS.Subscription`
        :returns: A Subscription resource
        """
        pass

    def Topic(self, arn: str = None) -> 'Topic':
        """
        Creates a Topic resource.::
          topic = sns.Topic('arn')
        :type arn: string
        :param arn: The Topic\'s arn identifier. This **must** be set.
        :rtype: :py:class:`SNS.Topic`
        :returns: A Topic resource
        """
        pass

    def create_platform_application(self, Name: str, Platform: str, Attributes: Dict) -> 'PlatformApplication':
        """
        Creates a platform application object for one of the supported push notification services, such as APNS and GCM, to which devices and mobile apps may register. You must specify PlatformPrincipal and PlatformCredential attributes when using the ``CreatePlatformApplication`` action. The PlatformPrincipal is received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is "SSL certificate". For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". The PlatformCredential is also received from the notification service. For WNS, PlatformPrincipal is "Package Security Identifier". For MPNS, PlatformPrincipal is "TLS certificate". For Baidu, PlatformPrincipal is "API key".
        For APNS/APNS_SANDBOX, PlatformCredential is "private key". For GCM, PlatformCredential is "API key". For ADM, PlatformCredential is "client secret". For WNS, PlatformCredential is "secret key". For MPNS, PlatformCredential is "private key". For Baidu, PlatformCredential is "secret key". The PlatformApplicationArn that is returned when using ``CreatePlatformApplication`` is then used as an attribute for the ``CreatePlatformEndpoint`` action. For more information, see `Using Amazon SNS Mobile Push Notifications <http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ . For more information about obtaining the PlatformPrincipal and PlatformCredential for each of the supported push notification services, see `Getting Started with Apple Push Notification Service <http://docs.aws.amazon.com/sns/latest/dg/mobile-push-apns.html>`__ , `Getting Started with Amazon Device Messaging <http://docs.aws.amazon.com/sns/latest/dg/mobile-push-adm.html>`__ , `Getting Started with Baidu Cloud Push <http://docs.aws.amazon.com/sns/latest/dg/mobile-push-baidu.html>`__ , `Getting Started with Google Cloud Messaging for Android <http://docs.aws.amazon.com/sns/latest/dg/mobile-push-gcm.html>`__ , `Getting Started with MPNS <http://docs.aws.amazon.com/sns/latest/dg/mobile-push-mpns.html>`__ , or `Getting Started with WNS <http://docs.aws.amazon.com/sns/latest/dg/mobile-push-wns.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/CreatePlatformApplication>`_
        
        **Request Syntax**
        ::
          platform_application = sns.create_platform_application(
              Name='string',
              Platform='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**
          Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.
        :type Platform: string
        :param Platform: **[REQUIRED]**
          The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Google Cloud Messaging).
        :type Attributes: dict
        :param Attributes: **[REQUIRED]**
          For a list of attributes, see `SetPlatformApplicationAttributes <http://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html>`__
          - *(string) --*
            - *(string) --*
        :rtype: :py:class:`sns.PlatformApplication`
        :returns: PlatformApplication resource
        """
        pass

    def create_topic(self, Name: str, Attributes: Dict = None) -> 'Topic':
        """
        Creates a topic to which notifications can be published. Users can create at most 100,000 topics. For more information, see `http\://aws.amazon.com/sns <http://aws.amazon.com/sns/>`__ . This action is idempotent, so if the requester already owns a topic with the specified name, that topic's ARN is returned without creating a new topic.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/CreateTopic>`_
        
        **Request Syntax**
        ::
          topic = sns.create_topic(
              Name='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the topic you want to create.
          Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.
        :type Attributes: dict
        :param Attributes:
          A map of attributes with their corresponding values.
          The following lists the names, descriptions, and values of the special request parameters that the ``CreateTopic`` action uses:
          * ``DeliveryPolicy`` – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
          * ``DisplayName`` – The display name to use for a topic with SMS subscriptions.
          * ``Policy`` – The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.
          - *(string) --*
            - *(string) --*
        :rtype: :py:class:`sns.Topic`
        :returns: Topic resource
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass


class PlatformApplication(base.ServiceResource):
    attributes: Dict
    arn: str
    endpoints: 'endpoints'

    def create_platform_endpoint(self, Token: str, CustomUserData: str = None, Attributes: Dict = None) -> 'PlatformEndpoint':
        """
        Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM and APNS. ``CreatePlatformEndpoint`` requires the PlatformApplicationArn that is returned from ``CreatePlatformApplication`` . The EndpointArn that is returned when using ``CreatePlatformEndpoint`` can then be used by the ``Publish`` action to send a message to a mobile app or by the ``Subscribe`` action for subscription to a topic. The ``CreatePlatformEndpoint`` action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint's ARN is returned without creating a new endpoint. For more information, see `Using Amazon SNS Mobile Push Notifications <http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ . 
        When using ``CreatePlatformEndpoint`` with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see `Creating an Amazon SNS Endpoint for Baidu <http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePushBaiduEndpoint.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/CreatePlatformEndpoint>`_
        
        **Request Syntax**
        ::
          platform_endpoint = platform_application.create_platform_endpoint(
              Token='string',
              CustomUserData='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type Token: string
        :param Token: **[REQUIRED]**
          Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM or ADM, the device token equivalent is called the registration ID.
        :type CustomUserData: string
        :param CustomUserData:
          Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
        :type Attributes: dict
        :param Attributes:
          For a list of attributes, see `SetEndpointAttributes <http://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html>`__ .
          - *(string) --*
            - *(string) --*
        :rtype: :py:class:`sns.PlatformEndpoint`
        :returns: PlatformEndpoint resource
        """
        pass

    def delete(self):
        """
        Deletes a platform application object for one of the supported push notification services, such as APNS and GCM. For more information, see `Using Amazon SNS Mobile Push Notifications <http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/DeletePlatformApplication>`_
        
        **Request Syntax**
        ::
          response = platform_application.delete()
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        Calls :py:meth:`SNS.Client.get_platform_application_attributes` to update the attributes of the PlatformApplication resource. Note that the load and reload methods are the same method and can be used interchangeably.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/None>`_
        
        **Request Syntax**
        ::
          platform_application.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        Calls :py:meth:`SNS.Client.get_platform_application_attributes` to update the attributes of the PlatformApplication resource. Note that the load and reload methods are the same method and can be used interchangeably.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/None>`_
        
        **Request Syntax**
        ::
          platform_application.load()
        :returns: None
        """
        pass

    def set_attributes(self, Attributes: Dict):
        """
        Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see `Using Amazon SNS Mobile Push Notifications <http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ . For information on configuring attributes for message delivery status, see `Using Amazon SNS Application Attributes for Message Delivery Status <http://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetPlatformApplicationAttributes>`_
        
        **Request Syntax**
        ::
          response = platform_application.set_attributes(
              Attributes={
                  'string': 'string'
              }
          )
        :type Attributes: dict
        :param Attributes: **[REQUIRED]**
          A map of the platform application attributes. Attributes in this map include the following:
          * ``PlatformCredential`` – The credential received from the notification service. For APNS/APNS_SANDBOX, PlatformCredential is private key. For GCM, PlatformCredential is \"API key\". For ADM, PlatformCredential is \"client secret\".
          * ``PlatformPrincipal`` – The principal received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is SSL certificate. For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is \"client id\".
          * ``EventEndpointCreated`` – Topic ARN to which EndpointCreated event notifications should be sent.
          * ``EventEndpointDeleted`` – Topic ARN to which EndpointDeleted event notifications should be sent.
          * ``EventEndpointUpdated`` – Topic ARN to which EndpointUpdate event notifications should be sent.
          * ``EventDeliveryFailure`` – Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application\'s endpoints.
          * ``SuccessFeedbackRoleArn`` – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
          * ``FailureFeedbackRoleArn`` – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
          * ``SuccessFeedbackSampleRate`` – Sample rate percentage (0-100) of successfully delivered messages.
          - *(string) --*
            - *(string) --*
        :returns: None
        """
        pass


class PlatformEndpoint(base.ServiceResource):
    attributes: Dict
    arn: str

    def delete(self):
        """
        Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see `Using Amazon SNS Mobile Push Notifications <http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ . 
        When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/DeleteEndpoint>`_
        
        **Request Syntax**
        ::
          response = platform_endpoint.delete()
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        Calls :py:meth:`SNS.Client.get_endpoint_attributes` to update the attributes of the PlatformEndpoint resource. Note that the load and reload methods are the same method and can be used interchangeably.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/None>`_
        
        **Request Syntax**
        ::
          platform_endpoint.load()
        :returns: None
        """
        pass

    def publish(self, Message: str, TopicArn: str = None, PhoneNumber: str = None, Subject: str = None, MessageStructure: str = None, MessageAttributes: Dict = None) -> Dict:
        """
        Sends a message to an Amazon SNS topic or sends a text message (SMS message) directly to a phone number. 
        If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.
        When a ``messageId`` is returned, the message has been saved and Amazon SNS will attempt to deliver it shortly.
        To use the ``Publish`` action for sending a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the ``CreatePlatformEndpoint`` action. 
        For more information about formatting messages, see `Send Custom Platform-Specific Payloads in Messages to Mobile Devices <http://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-custommessage.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Publish>`_
        
        **Request Syntax**
        ::
          response = platform_endpoint.publish(
              TopicArn='string',
              PhoneNumber='string',
              Message='string',
              Subject='string',
              MessageStructure='string',
              MessageAttributes={
                  'string': {
                      'DataType': 'string',
                      'StringValue': 'string',
                      'BinaryValue': b'bytes'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'MessageId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Response for Publish action.
            - **MessageId** *(string) --* 
              Unique identifier assigned to the published message.
              Length Constraint: Maximum 100 characters
        :type TopicArn: string
        :param TopicArn:
          The topic you want to publish to.
          If you don\'t specify a value for the ``TopicArn`` parameter, you must specify a value for the ``PhoneNumber`` or ``TargetArn`` parameters.
        :type PhoneNumber: string
        :param PhoneNumber:
          The phone number to which you want to deliver an SMS message. Use E.164 format.
          If you don\'t specify a value for the ``PhoneNumber`` parameter, you must specify a value for the ``TargetArn`` or ``TopicArn`` parameters.
        :type Message: string
        :param Message: **[REQUIRED]**
          The message you want to send.
          .. warning::
            The ``Message`` parameter is always a string. If you set ``MessageStructure`` to ``json`` , you must string-encode the ``Message`` parameter.
          If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the ``MessageStructure`` parameter to ``json`` and use a JSON object for the ``Message`` parameter.
          Constraints:
          * With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262,144 bytes, not 262,144 characters).
          * For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters. If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages aren\'t truncated mid-word but are cut off at whole-word boundaries. The total size limit for a single SMS ``Publish`` action is 1,600 characters.
          JSON-specific constraints:
          * Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.
          * The values will be parsed (unescaped) before they are used in outgoing messages.
          * Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).
          * Values have a minimum length of 0 (the empty string, \"\", is allowed).
          * Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).
          * Non-string values will cause the key to be ignored.
          * Keys that do not correspond to supported transport protocols are ignored.
          * Duplicate keys are not allowed.
          * Failure to parse or validate any key or value in the message will cause the ``Publish`` call to return an error (no partial delivery).
        :type Subject: string
        :param Subject:
          Optional parameter to be used as the \"Subject\" line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.
          Constraints: Subjects must be ASCII text that begins with a letter, number, or punctuation mark; must not include line breaks or control characters; and must be less than 100 characters long.
        :type MessageStructure: string
        :param MessageStructure:
          Set ``MessageStructure`` to ``json`` if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set ``MessageStructure`` to ``json`` , the value of the ``Message`` parameter must:
          * be a syntactically valid JSON object; and
          * contain at least a top-level JSON key of \"default\" with a value that is a string.
          You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., \"http\").
          For information about sending different messages for each protocol using the AWS Management Console, go to `Create Different Messages for Each Protocol <http://docs.aws.amazon.com/sns/latest/gsg/Publish.html#sns-message-formatting-by-protocol>`__ in the *Amazon Simple Notification Service Getting Started Guide* .
          Valid value: ``json``
        :type MessageAttributes: dict
        :param MessageAttributes:
          Message attributes for Publish action.
          - *(string) --*
            - *(dict) --*
              The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see `Publish <http://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`__ .
              Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes). For more information, see `Using Amazon SNS Message Attributes <http://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html>`__ .
              - **DataType** *(string) --* **[REQUIRED]**
                Amazon SNS supports the following logical data types: String, String.Array, Number, and Binary. For more information, see `Message Attribute Data Types <http://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes>`__ .
              - **StringValue** *(string) --*
                Strings are Unicode with UTF8 binary encoding. For a list of code values, see `http\://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .
              - **BinaryValue** *(bytes) --*
                Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.
        :rtype: dict
        :returns:
        """
        pass

    def reload(self):
        """
        Calls :py:meth:`SNS.Client.get_endpoint_attributes` to update the attributes of the PlatformEndpoint resource. Note that the load and reload methods are the same method and can be used interchangeably.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/None>`_
        
        **Request Syntax**
        ::
          platform_endpoint.load()
        :returns: None
        """
        pass

    def set_attributes(self, Attributes: Dict):
        """
        Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM and APNS. For more information, see `Using Amazon SNS Mobile Push Notifications <http://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetEndpointAttributes>`_
        
        **Request Syntax**
        ::
          response = platform_endpoint.set_attributes(
              Attributes={
                  'string': 'string'
              }
          )
        :type Attributes: dict
        :param Attributes: **[REQUIRED]**
          A map of the endpoint attributes. Attributes in this map include the following:
          * ``CustomUserData`` – arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
          * ``Enabled`` – flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.
          * ``Token`` – device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.
          - *(string) --*
            - *(string) --*
        :returns: None
        """
        pass


class Subscription(base.ServiceResource):
    attributes: Dict
    arn: str

    def delete(self):
        """
        Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic's owner can unsubscribe, and an AWS signature is required. If the ``Unsubscribe`` call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the ``Unsubscribe`` request was unintended.
        This action is throttled at 100 transactions per second (TPS).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Unsubscribe>`_
        
        **Request Syntax**
        ::
          response = subscription.delete()
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        Calls :py:meth:`SNS.Client.get_subscription_attributes` to update the attributes of the Subscription resource. Note that the load and reload methods are the same method and can be used interchangeably.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/None>`_
        
        **Request Syntax**
        ::
          subscription.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        Calls :py:meth:`SNS.Client.get_subscription_attributes` to update the attributes of the Subscription resource. Note that the load and reload methods are the same method and can be used interchangeably.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/None>`_
        
        **Request Syntax**
        ::
          subscription.load()
        :returns: None
        """
        pass

    def set_attributes(self, AttributeName: str, AttributeValue: str = None):
        """
        Allows a subscription owner to set an attribute of the subscription to a new value.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetSubscriptionAttributes>`_
        
        **Request Syntax**
        ::
          response = subscription.set_attributes(
              AttributeName='string',
              AttributeValue='string'
          )
        :type AttributeName: string
        :param AttributeName: **[REQUIRED]**
          A map of attributes with their corresponding values.
          The following lists the names, descriptions, and values of the special request parameters that the ``SetTopicAttributes`` action uses:
          * ``DeliveryPolicy`` – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
          * ``FilterPolicy`` – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.
          * ``RawMessageDelivery`` – When set to ``true`` , enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.
        :type AttributeValue: string
        :param AttributeValue:
          The new value for the attribute in JSON format.
        :returns: None
        """
        pass


class Topic(base.ServiceResource):
    attributes: Dict
    arn: str
    subscriptions: 'subscriptions'

    def add_permission(self, Label: str, AWSAccountId: List, ActionName: List):
        """
        Adds a statement to a topic's access control policy, granting access for the specified AWS accounts to the specified actions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/AddPermission>`_
        
        **Request Syntax**
        ::
          response = topic.add_permission(
              Label='string',
              AWSAccountId=[
                  'string',
              ],
              ActionName=[
                  'string',
              ]
          )
        :type Label: string
        :param Label: **[REQUIRED]**
          A unique identifier for the new policy statement.
        :type AWSAccountId: list
        :param AWSAccountId: **[REQUIRED]**
          The AWS account IDs of the users (principals) who will be given access to the specified actions. The users must have AWS accounts, but do not need to be signed up for this service.
          - *(string) --*
        :type ActionName: list
        :param ActionName: **[REQUIRED]**
          The action you want to allow for the specified principal(s).
          Valid values: any Amazon SNS action name.
          - *(string) --*
        :returns: None
        """
        pass

    def confirm_subscription(self, Token: str, AuthenticateOnUnsubscribe: str = None) -> 'Subscription':
        """
        Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier ``Subscribe`` action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the ``AuthenticateOnUnsubscribe`` flag is set to "true".
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ConfirmSubscription>`_
        
        **Request Syntax**
        ::
          subscription = topic.confirm_subscription(
              Token='string',
              AuthenticateOnUnsubscribe='string'
          )
        :type Token: string
        :param Token: **[REQUIRED]**
          Short-lived token sent to an endpoint during the ``Subscribe`` action.
        :type AuthenticateOnUnsubscribe: string
        :param AuthenticateOnUnsubscribe:
          Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is ``true`` and the request has an AWS signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires AWS authentication.
        :rtype: :py:class:`sns.Subscription`
        :returns: Subscription resource
        """
        pass

    def delete(self):
        """
        Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/DeleteTopic>`_
        
        **Request Syntax**
        ::
          response = topic.delete()
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        Calls :py:meth:`SNS.Client.get_topic_attributes` to update the attributes of the Topic resource. Note that the load and reload methods are the same method and can be used interchangeably.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/None>`_
        
        **Request Syntax**
        ::
          topic.load()
        :returns: None
        """
        pass

    def publish(self, Message: str, TargetArn: str = None, PhoneNumber: str = None, Subject: str = None, MessageStructure: str = None, MessageAttributes: Dict = None) -> Dict:
        """
        Sends a message to an Amazon SNS topic or sends a text message (SMS message) directly to a phone number. 
        If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.
        When a ``messageId`` is returned, the message has been saved and Amazon SNS will attempt to deliver it shortly.
        To use the ``Publish`` action for sending a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the ``CreatePlatformEndpoint`` action. 
        For more information about formatting messages, see `Send Custom Platform-Specific Payloads in Messages to Mobile Devices <http://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-custommessage.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Publish>`_
        
        **Request Syntax**
        ::
          response = topic.publish(
              TargetArn='string',
              PhoneNumber='string',
              Message='string',
              Subject='string',
              MessageStructure='string',
              MessageAttributes={
                  'string': {
                      'DataType': 'string',
                      'StringValue': 'string',
                      'BinaryValue': b'bytes'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'MessageId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Response for Publish action.
            - **MessageId** *(string) --* 
              Unique identifier assigned to the published message.
              Length Constraint: Maximum 100 characters
        :type TargetArn: string
        :param TargetArn:
          Either TopicArn or EndpointArn, but not both.
          If you don\'t specify a value for the ``TargetArn`` parameter, you must specify a value for the ``PhoneNumber`` or ``TopicArn`` parameters.
        :type PhoneNumber: string
        :param PhoneNumber:
          The phone number to which you want to deliver an SMS message. Use E.164 format.
          If you don\'t specify a value for the ``PhoneNumber`` parameter, you must specify a value for the ``TargetArn`` or ``TopicArn`` parameters.
        :type Message: string
        :param Message: **[REQUIRED]**
          The message you want to send.
          .. warning::
            The ``Message`` parameter is always a string. If you set ``MessageStructure`` to ``json`` , you must string-encode the ``Message`` parameter.
          If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the ``MessageStructure`` parameter to ``json`` and use a JSON object for the ``Message`` parameter.
          Constraints:
          * With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262,144 bytes, not 262,144 characters).
          * For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters. If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages aren\'t truncated mid-word but are cut off at whole-word boundaries. The total size limit for a single SMS ``Publish`` action is 1,600 characters.
          JSON-specific constraints:
          * Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.
          * The values will be parsed (unescaped) before they are used in outgoing messages.
          * Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).
          * Values have a minimum length of 0 (the empty string, \"\", is allowed).
          * Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).
          * Non-string values will cause the key to be ignored.
          * Keys that do not correspond to supported transport protocols are ignored.
          * Duplicate keys are not allowed.
          * Failure to parse or validate any key or value in the message will cause the ``Publish`` call to return an error (no partial delivery).
        :type Subject: string
        :param Subject:
          Optional parameter to be used as the \"Subject\" line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.
          Constraints: Subjects must be ASCII text that begins with a letter, number, or punctuation mark; must not include line breaks or control characters; and must be less than 100 characters long.
        :type MessageStructure: string
        :param MessageStructure:
          Set ``MessageStructure`` to ``json`` if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set ``MessageStructure`` to ``json`` , the value of the ``Message`` parameter must:
          * be a syntactically valid JSON object; and
          * contain at least a top-level JSON key of \"default\" with a value that is a string.
          You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., \"http\").
          For information about sending different messages for each protocol using the AWS Management Console, go to `Create Different Messages for Each Protocol <http://docs.aws.amazon.com/sns/latest/gsg/Publish.html#sns-message-formatting-by-protocol>`__ in the *Amazon Simple Notification Service Getting Started Guide* .
          Valid value: ``json``
        :type MessageAttributes: dict
        :param MessageAttributes:
          Message attributes for Publish action.
          - *(string) --*
            - *(dict) --*
              The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see `Publish <http://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`__ .
              Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes). For more information, see `Using Amazon SNS Message Attributes <http://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html>`__ .
              - **DataType** *(string) --* **[REQUIRED]**
                Amazon SNS supports the following logical data types: String, String.Array, Number, and Binary. For more information, see `Message Attribute Data Types <http://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes>`__ .
              - **StringValue** *(string) --*
                Strings are Unicode with UTF8 binary encoding. For a list of code values, see `http\://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .
              - **BinaryValue** *(bytes) --*
                Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.
        :rtype: dict
        :returns:
        """
        pass

    def reload(self):
        """
        Calls :py:meth:`SNS.Client.get_topic_attributes` to update the attributes of the Topic resource. Note that the load and reload methods are the same method and can be used interchangeably.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/None>`_
        
        **Request Syntax**
        ::
          topic.load()
        :returns: None
        """
        pass

    def remove_permission(self, Label: str):
        """
        Removes a statement from a topic's access control policy.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/RemovePermission>`_
        
        **Request Syntax**
        ::
          response = topic.remove_permission(
              Label='string'
          )
        :type Label: string
        :param Label: **[REQUIRED]**
          The unique label of the statement you want to remove.
        :returns: None
        """
        pass

    def set_attributes(self, AttributeName: str, AttributeValue: str = None):
        """
        Allows a topic owner to set an attribute of the topic to a new value.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetTopicAttributes>`_
        
        **Request Syntax**
        ::
          response = topic.set_attributes(
              AttributeName='string',
              AttributeValue='string'
          )
        :type AttributeName: string
        :param AttributeName: **[REQUIRED]**
          A map of attributes with their corresponding values.
          The following lists the names, descriptions, and values of the special request parameters that the ``SetTopicAttributes`` action uses:
          * ``DeliveryPolicy`` – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
          * ``DisplayName`` – The display name to use for a topic with SMS subscriptions.
          * ``Policy`` – The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.
        :type AttributeValue: string
        :param AttributeValue:
          The new value for the attribute.
        :returns: None
        """
        pass

    def subscribe(self, Protocol: str, Endpoint: str = None, Attributes: Dict = None, ReturnSubscriptionArn: bool = None) -> 'Subscription':
        """
        Prepares to subscribe an endpoint by sending the endpoint a confirmation message. To actually create a subscription, the endpoint owner must call the ``ConfirmSubscription`` action with the token from the confirmation message. Confirmation tokens are valid for three days.
        This action is throttled at 100 transactions per second (TPS).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Subscribe>`_
        
        **Request Syntax**
        ::
          subscription = topic.subscribe(
              Protocol='string',
              Endpoint='string',
              Attributes={
                  'string': 'string'
              },
              ReturnSubscriptionArn=True|False
          )
        :type Protocol: string
        :param Protocol: **[REQUIRED]**
          The protocol you want to use. Supported protocols include:
          * ``http`` – delivery of JSON-encoded message via HTTP POST
          * ``https`` – delivery of JSON-encoded message via HTTPS POST
          * ``email`` – delivery of message via SMTP
          * ``email-json`` – delivery of JSON-encoded message via SMTP
          * ``sms`` – delivery of message via SMS
          * ``sqs`` – delivery of JSON-encoded message to an Amazon SQS queue
          * ``application`` – delivery of JSON-encoded message to an EndpointArn for a mobile app and device.
          * ``lambda`` – delivery of JSON-encoded message to an AWS Lambda function.
        :type Endpoint: string
        :param Endpoint:
          The endpoint that you want to receive notifications. Endpoints vary by protocol:
          * For the ``http`` protocol, the endpoint is an URL beginning with \"http://\"
          * For the ``https`` protocol, the endpoint is a URL beginning with \"https://\"
          * For the ``email`` protocol, the endpoint is an email address
          * For the ``email-json`` protocol, the endpoint is an email address
          * For the ``sms`` protocol, the endpoint is a phone number of an SMS-enabled device
          * For the ``sqs`` protocol, the endpoint is the ARN of an Amazon SQS queue
          * For the ``application`` protocol, the endpoint is the EndpointArn of a mobile app and device.
          * For the ``lambda`` protocol, the endpoint is the ARN of an AWS Lambda function.
        :type Attributes: dict
        :param Attributes:
          A map of attributes with their corresponding values.
          The following lists the names, descriptions, and values of the special request parameters that the ``SetTopicAttributes`` action uses:
          * ``DeliveryPolicy`` – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
          * ``FilterPolicy`` – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.
          * ``RawMessageDelivery`` – When set to ``true`` , enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.
          - *(string) --*
            - *(string) --*
        :type ReturnSubscriptionArn: boolean
        :param ReturnSubscriptionArn:
          Sets whether the response from the ``Subscribe`` request includes the subscription ARN, even if the subscription is not yet confirmed.
          If you set this parameter to ``false`` , the response includes the ARN for confirmed subscriptions, but it includes an ARN value of \"pending subscription\" for subscriptions that are not yet confirmed. A subscription becomes confirmed when the subscriber calls the ``ConfirmSubscription`` action with a confirmation token.
          If you set this parameter to ``true`` , the response includes the ARN in all cases, even if the subscription is not yet confirmed.
          The default value is ``false`` .
        :rtype: :py:class:`sns.Subscription`
        :returns: Subscription resource
        """
        pass


class platform_applications(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['PlatformApplication']:
        """
        Creates an iterable of all PlatformApplication resources in the collection.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPlatformApplications>`_
        
        **Request Syntax**
        ::
          platform_application_iterator = sns.platform_applications.all()
        :rtype: list(:py:class:`sns.PlatformApplication`)
        :returns: A list of PlatformApplication resources
        """
        pass

    
    @classmethod
    def filter(cls, NextToken: str = None) -> List['PlatformApplication']:
        """
        Creates an iterable of all PlatformApplication resources in the collection filtered by kwargs passed to method.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPlatformApplications>`_
        
        **Request Syntax**
        ::
          platform_application_iterator = sns.platform_applications.filter(
              NextToken='string'
          )
        :type NextToken: string
        :param NextToken:
          NextToken string is used when calling ListPlatformApplications action to retrieve additional records that are available after the first page results.
        :rtype: list(:py:class:`sns.PlatformApplication`)
        :returns: A list of PlatformApplication resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['PlatformApplication']:
        """
        Creates an iterable up to a specified amount of PlatformApplication resources in the collection.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPlatformApplications>`_
        
        **Request Syntax**
        ::
          platform_application_iterator = sns.platform_applications.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        :rtype: list(:py:class:`sns.PlatformApplication`)
        :returns: A list of PlatformApplication resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['PlatformApplication']:
        """
        Creates an iterable of all PlatformApplication resources in the collection, but limits the number of items returned by each service call by the specified amount.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPlatformApplications>`_
        
        **Request Syntax**
        ::
          platform_application_iterator = sns.platform_applications.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        :rtype: list(:py:class:`sns.PlatformApplication`)
        :returns: A list of PlatformApplication resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class subscriptions(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Subscription']:
        """
        Creates an iterable of all Subscription resources in the collection.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptions>`_
        
        **Request Syntax**
        ::
          subscription_iterator = sns.subscriptions.all()
        :rtype: list(:py:class:`sns.Subscription`)
        :returns: A list of Subscription resources
        """
        pass

    
    @classmethod
    def filter(cls, NextToken: str = None) -> List['Subscription']:
        """
        Creates an iterable of all Subscription resources in the collection filtered by kwargs passed to method.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptions>`_
        
        **Request Syntax**
        ::
          subscription_iterator = sns.subscriptions.filter(
              NextToken='string'
          )
        :type NextToken: string
        :param NextToken:
          Token returned by the previous ``ListSubscriptions`` request.
        :rtype: list(:py:class:`sns.Subscription`)
        :returns: A list of Subscription resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Subscription']:
        """
        Creates an iterable up to a specified amount of Subscription resources in the collection.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptions>`_
        
        **Request Syntax**
        ::
          subscription_iterator = sns.subscriptions.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        :rtype: list(:py:class:`sns.Subscription`)
        :returns: A list of Subscription resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Subscription']:
        """
        Creates an iterable of all Subscription resources in the collection, but limits the number of items returned by each service call by the specified amount.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptions>`_
        
        **Request Syntax**
        ::
          subscription_iterator = sns.subscriptions.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        :rtype: list(:py:class:`sns.Subscription`)
        :returns: A list of Subscription resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class topics(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Topic']:
        """
        Creates an iterable of all Topic resources in the collection.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListTopics>`_
        
        **Request Syntax**
        ::
          topic_iterator = sns.topics.all()
        :rtype: list(:py:class:`sns.Topic`)
        :returns: A list of Topic resources
        """
        pass

    
    @classmethod
    def filter(cls, NextToken: str = None) -> List['Topic']:
        """
        Creates an iterable of all Topic resources in the collection filtered by kwargs passed to method.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListTopics>`_
        
        **Request Syntax**
        ::
          topic_iterator = sns.topics.filter(
              NextToken='string'
          )
        :type NextToken: string
        :param NextToken:
          Token returned by the previous ``ListTopics`` request.
        :rtype: list(:py:class:`sns.Topic`)
        :returns: A list of Topic resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Topic']:
        """
        Creates an iterable up to a specified amount of Topic resources in the collection.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListTopics>`_
        
        **Request Syntax**
        ::
          topic_iterator = sns.topics.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        :rtype: list(:py:class:`sns.Topic`)
        :returns: A list of Topic resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Topic']:
        """
        Creates an iterable of all Topic resources in the collection, but limits the number of items returned by each service call by the specified amount.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListTopics>`_
        
        **Request Syntax**
        ::
          topic_iterator = sns.topics.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        :rtype: list(:py:class:`sns.Topic`)
        :returns: A list of Topic resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass
