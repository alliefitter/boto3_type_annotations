from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def add_permission(self, QueueUrl: str, Label: str, AWSAccountIds: List, Actions: List):
        """
        Adds a permission to a queue for a specific `principal <http://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P>`__ . This allows sharing access to the queue.
        When you create a queue, you have full control access rights for the queue. Only you, the owner of the queue, can grant or deny permissions to the queue. For more information about these permissions, see `Allow Developers to Write Messages to a Shared Queue <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-writing-an-sqs-policy.html#write-messages-to-shared-queue>`__ in the *Amazon Simple Queue Service Developer Guide* .
        .. note::
           ``AddPermission`` writes an Amazon-SQS-generated policy. If you want to write your own policy, use ``  SetQueueAttributes `` to upload your policy. For more information about writing your own policy, see `Using Custom Policies with the Amazon SQS Access Policy Language <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
          An Amazon SQS policy can have a maximum of 7 actions.
        Some actions take lists of parameters. These lists are specified using the ``param.n`` notation. Values of ``n`` are integers starting from 1. For example, a parameter list with two elements looks like this:
         ``&Attribute.1=first``  
         ``&Attribute.2=second``  
        .. note::
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/AddPermission>`_
        
        **Request Syntax**
        ::
          response = client.add_permission(
              QueueUrl='string',
              Label='string',
              AWSAccountIds=[
                  'string',
              ],
              Actions=[
                  'string',
              ]
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue to which permissions are added.
          Queue URLs and names are case-sensitive.
        :type Label: string
        :param Label: **[REQUIRED]**
          The unique identification of the permission you\'re setting (for example, ``AliceSendMessage`` ). Maximum 80 characters. Allowed characters include alphanumeric characters, hyphens (``-`` ), and underscores (``_`` ).
        :type AWSAccountIds: list
        :param AWSAccountIds: **[REQUIRED]**
          The AWS account number of the `principal <http://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P>`__ who is given permission. The principal must have an AWS account, but does not need to be signed up for Amazon SQS. For information about locating the AWS account identification, see `Your AWS Identifiers <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests.html#sqs-api-request-authentication>`__ in the *Amazon Simple Queue Service Developer Guide* .
          - *(string) --*
        :type Actions: list
        :param Actions: **[REQUIRED]**
          The action the client wants to allow for the specified principal. Valid values: the name of any action or ``*`` .
          For more information about these actions, see `Overview of Managing Access Permissions to Your Amazon Simple Queue Service Resource <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
          Specifying ``SendMessage`` , ``DeleteMessage`` , or ``ChangeMessageVisibility`` for ``ActionName.n`` also grants permissions for the corresponding batch versions of those actions: ``SendMessageBatch`` , ``DeleteMessageBatch`` , and ``ChangeMessageVisibilityBatch`` .
          - *(string) --*
        :returns: None
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

    def change_message_visibility(self, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int):
        """
        Changes the visibility timeout of a specified message in a queue to a new value. The maximum allowed timeout value is 12 hours. For more information, see `Visibility Timeout <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        For example, you have a message with a visibility timeout of 5 minutes. After 3 minutes, you call ``ChangeMessageVisibility`` with a timeout of 10 minutes. You can continue to call ``ChangeMessageVisibility`` to extend the visibility timeout to a maximum of 12 hours. If you try to extend the visibility timeout beyond 12 hours, your request is rejected.
        A message is considered to be *in flight* after it's received from a queue by a consumer, but not yet deleted from the queue.
        For standard queues, there can be a maximum of 120,000 inflight messages per queue. If you reach this limit, Amazon SQS returns the ``OverLimit`` error message. To avoid reaching the limit, you should delete messages from the queue after they're processed. You can also increase the number of queues you use to process your messages.
        For FIFO queues, there can be a maximum of 20,000 inflight messages per queue. If you reach this limit, Amazon SQS returns no error messages.
        .. warning::
          If you attempt to set the ``VisibilityTimeout`` to a value greater than the maximum time left, Amazon SQS returns an error. Amazon SQS doesn't automatically recalculate and increase the timeout to the maximum remaining time.
          Unlike with a queue, when you change the visibility timeout for a specific message the timeout value is applied immediately but isn't saved in memory for that message. If you don't delete a message after it is received, the visibility timeout for the message reverts to the original timeout value (not to the value you set using the ``ChangeMessageVisibility`` action) the next time the message is received.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/ChangeMessageVisibility>`_
        
        **Request Syntax**
        ::
          response = client.change_message_visibility(
              QueueUrl='string',
              ReceiptHandle='string',
              VisibilityTimeout=123
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue whose message\'s visibility is changed.
          Queue URLs and names are case-sensitive.
        :type ReceiptHandle: string
        :param ReceiptHandle: **[REQUIRED]**
          The receipt handle associated with the message whose visibility timeout is changed. This parameter is returned by the ``  ReceiveMessage `` action.
        :type VisibilityTimeout: integer
        :param VisibilityTimeout: **[REQUIRED]**
          The new value for the message\'s visibility timeout (in seconds). Values values: ``0`` to ``43200`` . Maximum: 12 hours.
        :returns: None
        """
        pass

    def change_message_visibility_batch(self, QueueUrl: str, Entries: List) -> Dict:
        """
        Changes the visibility timeout of multiple messages. This is a batch version of ``  ChangeMessageVisibility .`` The result of the action on each message is reported individually in the response. You can send up to 10 ``  ChangeMessageVisibility `` requests with each ``ChangeMessageVisibilityBatch`` action.
        .. warning::
          Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of ``200`` .
        Some actions take lists of parameters. These lists are specified using the ``param.n`` notation. Values of ``n`` are integers starting from 1. For example, a parameter list with two elements looks like this:
         ``&Attribute.1=first``  
         ``&Attribute.2=second``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/ChangeMessageVisibilityBatch>`_
        
        **Request Syntax**
        ::
          response = client.change_message_visibility_batch(
              QueueUrl='string',
              Entries=[
                  {
                      'Id': 'string',
                      'ReceiptHandle': 'string',
                      'VisibilityTimeout': 123
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'Successful': [
                    {
                        'Id': 'string'
                    },
                ],
                'Failed': [
                    {
                        'Id': 'string',
                        'SenderFault': True|False,
                        'Code': 'string',
                        'Message': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            For each message in the batch, the response contains a ``  ChangeMessageVisibilityBatchResultEntry `` tag if the message succeeds or a ``  BatchResultErrorEntry `` tag if the message fails.
            - **Successful** *(list) --* 
              A list of ``  ChangeMessageVisibilityBatchResultEntry `` items.
              - *(dict) --* 
                Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``  
                - **Id** *(string) --* 
                  Represents a message whose visibility timeout has been changed successfully.
            - **Failed** *(list) --* 
              A list of ``  BatchResultErrorEntry `` items.
              - *(dict) --* 
                Gives a detailed description of the result of an action on each entry in the request.
                - **Id** *(string) --* 
                  The ``Id`` of an entry in a batch request.
                - **SenderFault** *(boolean) --* 
                  Specifies whether the error happened due to the producer.
                - **Code** *(string) --* 
                  An error code representing why the action failed on this entry.
                - **Message** *(string) --* 
                  A message explaining why the action failed on this entry.
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue whose messages\' visibility is changed.
          Queue URLs and names are case-sensitive.
        :type Entries: list
        :param Entries: **[REQUIRED]**
          A list of receipt handles of the messages for which the visibility timeout must be changed.
          - *(dict) --*
            Encloses a receipt handle and an entry id for each message in ``  ChangeMessageVisibilityBatch .``
            .. warning::
              All of the following list parameters must be prefixed with ``ChangeMessageVisibilityBatchRequestEntry.n`` , where ``n`` is an integer value starting with ``1`` . For example, a parameter list for this action might look like this:
             ``&ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2``
             ``&ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=your_receipt_handle``
             ``&ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45``
            - **Id** *(string) --* **[REQUIRED]**
              An identifier for this particular receipt handle used to communicate the result.
              .. note::
                The ``Id`` s of a batch request need to be unique within a request
            - **ReceiptHandle** *(string) --* **[REQUIRED]**
              A receipt handle.
            - **VisibilityTimeout** *(integer) --*
              The new value (in seconds) for the message\'s visibility timeout.
        :rtype: dict
        :returns:
        """
        pass

    def create_queue(self, QueueName: str, Attributes: Dict = None) -> Dict:
        """
        Creates a new standard or FIFO queue. You can pass one or more attributes in the request. Keep the following caveats in mind:
        * If you don't specify the ``FifoQueue`` attribute, Amazon SQS creates a standard queue. 
        .. note::
           You can't change the queue type after you create it and you can't convert an existing standard queue into a FIFO queue. You must either create a new FIFO queue for your application or delete your existing standard queue and recreate it as a FIFO queue. For more information, see `Moving From a Standard Queue to a FIFO Queue <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-moving>`__ in the *Amazon Simple Queue Service Developer Guide* .  
        * If you don't provide a value for an attribute, the queue is created with the default value for the attribute. 
        * If you delete a queue, you must wait at least 60 seconds before creating a queue with the same name. 
        To successfully create a new queue, you must provide a queue name that adheres to the `limits related to queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-queues.html>`__ and is unique within the scope of your queues.
        To get the queue URL, use the ``  GetQueueUrl `` action. ``  GetQueueUrl `` requires only the ``QueueName`` parameter. be aware of existing queue names:
        * If you provide the name of an existing queue along with the exact names and values of all the queue's attributes, ``CreateQueue`` returns the queue URL for the existing queue. 
        * If the queue name, attribute names, or attribute values don't match an existing queue, ``CreateQueue`` returns an error. 
        Some actions take lists of parameters. These lists are specified using the ``param.n`` notation. Values of ``n`` are integers starting from 1. For example, a parameter list with two elements looks like this:
         ``&Attribute.1=first``  
         ``&Attribute.2=second``  
        .. note::
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/CreateQueue>`_
        
        **Request Syntax**
        ::
          response = client.create_queue(
              QueueName='string',
              Attributes={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'QueueUrl': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Returns the ``QueueUrl`` attribute of the created queue.
            - **QueueUrl** *(string) --* 
              The URL of the created Amazon SQS queue.
        :type QueueName: string
        :param QueueName: **[REQUIRED]**
          The name of the new queue. The following limits apply to this name:
          * A queue name can have up to 80 characters.
          * Valid values: alphanumeric characters, hyphens (``-`` ), and underscores (``_`` ).
          * A FIFO queue name must end with the ``.fifo`` suffix.
          Queue URLs and names are case-sensitive.
        :type Attributes: dict
        :param Attributes:
          A map of attributes with their corresponding values.
          The following lists the names, descriptions, and values of the special request parameters that the ``CreateQueue`` action uses:
          * ``DelaySeconds`` - The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 seconds (15 minutes). Default: 0.
          * ``MaximumMessageSize`` - The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). Default: 262,144 (256 KiB).
          * ``MessageRetentionPeriod`` - The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer from 60 seconds (1 minute) to 1,209,600 seconds (14 days). Default: 345,600 (4 days).
          * ``Policy`` - The queue\'s policy. A valid AWS policy. For more information about policy structure, see `Overview of AWS IAM Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html>`__ in the *Amazon IAM User Guide* .
          * ``ReceiveMessageWaitTimeSeconds`` - The length of time, in seconds, for which a ``  ReceiveMessage `` action waits for a message to arrive. Valid values: An integer from 0 to 20 (seconds). Default: 0.
          * ``RedrivePolicy`` - The string that includes the parameters for the dead-letter queue functionality of the source queue. For more information about the redrive policy and dead-letter queues, see `Using Amazon SQS Dead-Letter Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
            * ``deadLetterTargetArn`` - The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of ``maxReceiveCount`` is exceeded.
            * ``maxReceiveCount`` - The number of times a message is delivered to the source queue before being moved to the dead-letter queue. When the ``ReceiveCount`` for a message exceeds the ``maxReceiveCount`` for a queue, Amazon SQS moves the message to the dead-letter-queue.
          .. note::
            The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a standard queue must also be a standard queue.
          * ``VisibilityTimeout`` - The visibility timeout for the queue, in seconds. Valid values: An integer from 0 to 43,200 (12 hours). Default: 30. For more information about the visibility timeout, see `Visibility Timeout <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
          The following attributes apply only to `server-side-encryption <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html>`__ :
          * ``KmsMasterKeyId`` - The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see `Key Terms <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms>`__ . While the alias of the AWS-managed CMK for Amazon SQS is always ``alias/aws/sqs`` , the alias of a custom CMK can, for example, be ``alias/*MyAlias* `` . For more examples, see `KeyId <http://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters>`__ in the *AWS Key Management Service API Reference* .
          * ``KmsDataKeyReusePeriodSeconds`` - The length of time, in seconds, for which Amazon SQS can reuse a `data key <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys>`__ to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). Default: 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which might incur charges after Free Tier. For more information, see `How Does the Data Key Reuse Period Work? <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work>`__ .
          The following attributes apply only to `FIFO (first-in-first-out) queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html>`__ :
          * ``FifoQueue`` - Designates a queue as FIFO. Valid values: ``true`` , ``false`` . You can provide this attribute only during queue creation. You can\'t change it for an existing queue. When you set this attribute, you must also provide the ``MessageGroupId`` for your messages explicitly. For more information, see `FIFO Queue Logic <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-understanding-logic>`__ in the *Amazon Simple Queue Service Developer Guide* .
          * ``ContentBasedDeduplication`` - Enables content-based deduplication. Valid values: ``true`` , ``false`` . For more information, see `Exactly-Once Processing <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing>`__ in the *Amazon Simple Queue Service Developer Guide* .
            * Every message must have a unique ``MessageDeduplicationId`` ,
              * You may provide a ``MessageDeduplicationId`` explicitly.
              * If you aren\'t able to provide a ``MessageDeduplicationId`` and you enable ``ContentBasedDeduplication`` for your queue, Amazon SQS uses a SHA-256 hash to generate the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the message).
              * If you don\'t provide a ``MessageDeduplicationId`` and the queue doesn\'t have ``ContentBasedDeduplication`` set, the action fails with an error.
              * If the queue has ``ContentBasedDeduplication`` set, your ``MessageDeduplicationId`` overrides the generated one.
            * When ``ContentBasedDeduplication`` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
            * If you send one message with ``ContentBasedDeduplication`` enabled and then another message with a ``MessageDeduplicationId`` that is the same as the one generated for the first ``MessageDeduplicationId`` , the two messages are treated as duplicates and only one copy of the message is delivered.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def delete_message(self, QueueUrl: str, ReceiptHandle: str):
        """
        Deletes the specified message from the specified queue. To select the message to delete, use the ``ReceiptHandle`` of the message (*not* the ``MessageId`` which you receive when you send the message). Amazon SQS can delete a message from a queue even if a visibility timeout setting causes the message to be locked by another consumer. Amazon SQS automatically deletes messages left in a queue longer than the retention period configured for the queue. 
        .. note::
          The ``ReceiptHandle`` is associated with a *specific instance* of receiving a message. If you receive a message more than once, the ``ReceiptHandle`` is different each time you receive a message. When you use the ``DeleteMessage`` action, you must provide the most recently received ``ReceiptHandle`` for the message (otherwise, the request succeeds, but the message might not be deleted).
          For standard queues, it is possible to receive a message even after you delete it. This might happen on rare occasions if one of the servers which stores a copy of the message is unavailable when you send the request to delete the message. The copy remains on the server and might be returned to you during a subsequent receive request. You should ensure that your application is idempotent, so that receiving a message more than once does not cause issues.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/DeleteMessage>`_
        
        **Request Syntax**
        ::
          response = client.delete_message(
              QueueUrl='string',
              ReceiptHandle='string'
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue from which messages are deleted.
          Queue URLs and names are case-sensitive.
        :type ReceiptHandle: string
        :param ReceiptHandle: **[REQUIRED]**
          The receipt handle associated with the message to delete.
        :returns: None
        """
        pass

    def delete_message_batch(self, QueueUrl: str, Entries: List) -> Dict:
        """
        Deletes up to ten messages from the specified queue. This is a batch version of ``  DeleteMessage .`` The result of the action on each message is reported individually in the response.
        .. warning::
          Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of ``200`` .
        Some actions take lists of parameters. These lists are specified using the ``param.n`` notation. Values of ``n`` are integers starting from 1. For example, a parameter list with two elements looks like this:
         ``&Attribute.1=first``  
         ``&Attribute.2=second``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/DeleteMessageBatch>`_
        
        **Request Syntax**
        ::
          response = client.delete_message_batch(
              QueueUrl='string',
              Entries=[
                  {
                      'Id': 'string',
                      'ReceiptHandle': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'Successful': [
                    {
                        'Id': 'string'
                    },
                ],
                'Failed': [
                    {
                        'Id': 'string',
                        'SenderFault': True|False,
                        'Code': 'string',
                        'Message': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            For each message in the batch, the response contains a ``  DeleteMessageBatchResultEntry `` tag if the message is deleted or a ``  BatchResultErrorEntry `` tag if the message can't be deleted.
            - **Successful** *(list) --* 
              A list of ``  DeleteMessageBatchResultEntry `` items.
              - *(dict) --* 
                Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``  
                - **Id** *(string) --* 
                  Represents a successfully deleted message.
            - **Failed** *(list) --* 
              A list of ``  BatchResultErrorEntry `` items.
              - *(dict) --* 
                Gives a detailed description of the result of an action on each entry in the request.
                - **Id** *(string) --* 
                  The ``Id`` of an entry in a batch request.
                - **SenderFault** *(boolean) --* 
                  Specifies whether the error happened due to the producer.
                - **Code** *(string) --* 
                  An error code representing why the action failed on this entry.
                - **Message** *(string) --* 
                  A message explaining why the action failed on this entry.
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue from which messages are deleted.
          Queue URLs and names are case-sensitive.
        :type Entries: list
        :param Entries: **[REQUIRED]**
          A list of receipt handles for the messages to be deleted.
          - *(dict) --*
            Encloses a receipt handle and an identifier for it.
            - **Id** *(string) --* **[REQUIRED]**
              An identifier for this particular receipt handle. This is used to communicate the result.
              .. note::
                The ``Id`` s of a batch request need to be unique within a request
            - **ReceiptHandle** *(string) --* **[REQUIRED]**
              A receipt handle.
        :rtype: dict
        :returns:
        """
        pass

    def delete_queue(self, QueueUrl: str):
        """
        Deletes the queue specified by the ``QueueUrl`` , regardless of the queue's contents. If the specified queue doesn't exist, Amazon SQS returns a successful response.
        .. warning::
          Be careful with the ``DeleteQueue`` action: When you delete a queue, any messages in the queue are no longer available. 
        When you delete a queue, the deletion process takes up to 60 seconds. Requests you send involving that queue during the 60 seconds might succeed. For example, a ``  SendMessage `` request might succeed, but after 60 seconds the queue and the message you sent no longer exist.
        When you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.
        .. note::
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/DeleteQueue>`_
        
        **Request Syntax**
        ::
          response = client.delete_queue(
              QueueUrl='string'
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue to delete.
          Queue URLs and names are case-sensitive.
        :returns: None
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

    def get_queue_attributes(self, QueueUrl: str, AttributeNames: List = None) -> Dict:
        """
        Gets attributes for the specified queue.
        .. note::
          To determine whether a queue is `FIFO <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html>`__ , you can check whether ``QueueName`` ends with the ``.fifo`` suffix.
        Some actions take lists of parameters. These lists are specified using the ``param.n`` notation. Values of ``n`` are integers starting from 1. For example, a parameter list with two elements looks like this:
         ``&Attribute.1=first``  
         ``&Attribute.2=second``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/GetQueueAttributes>`_
        
        **Request Syntax**
        ::
          response = client.get_queue_attributes(
              QueueUrl='string',
              AttributeNames=[
                  'All'|'Policy'|'VisibilityTimeout'|'MaximumMessageSize'|'MessageRetentionPeriod'|'ApproximateNumberOfMessages'|'ApproximateNumberOfMessagesNotVisible'|'CreatedTimestamp'|'LastModifiedTimestamp'|'QueueArn'|'ApproximateNumberOfMessagesDelayed'|'DelaySeconds'|'ReceiveMessageWaitTimeSeconds'|'RedrivePolicy'|'FifoQueue'|'ContentBasedDeduplication'|'KmsMasterKeyId'|'KmsDataKeyReusePeriodSeconds',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'Attributes': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of returned queue attributes.
            - **Attributes** *(dict) --* 
              A map of attributes to their respective values.
              - *(string) --* 
                - *(string) --* 
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue whose attribute information is retrieved.
          Queue URLs and names are case-sensitive.
        :type AttributeNames: list
        :param AttributeNames:
          A list of attributes for which to retrieve information.
          .. note::
            In the future, new attributes might be added. If you write code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.
          The following attributes are supported:
          * ``All`` - Returns all values.
          * ``ApproximateNumberOfMessages`` - Returns the approximate number of messages available for retrieval from the queue.
          * ``ApproximateNumberOfMessagesDelayed`` - Returns the approximate number of messages in the queue that are delayed and not available for reading immediately. This can happen when the queue is configured as a delay queue or when a message has been sent with a delay parameter.
          * ``ApproximateNumberOfMessagesNotVisible`` - Returns the approximate number of messages that are in flight. Messages are considered to be *in flight* if they have been sent to a client but have not yet been deleted or have not yet reached the end of their visibility window.
          * ``CreatedTimestamp`` - Returns the time when the queue was created in seconds (`epoch time <http://en.wikipedia.org/wiki/Unix_time>`__ ).
          * ``DelaySeconds`` - Returns the default delay on the queue in seconds.
          * ``LastModifiedTimestamp`` - Returns the time when the queue was last changed in seconds (`epoch time <http://en.wikipedia.org/wiki/Unix_time>`__ ).
          * ``MaximumMessageSize`` - Returns the limit of how many bytes a message can contain before Amazon SQS rejects it.
          * ``MessageRetentionPeriod`` - Returns the length of time, in seconds, for which Amazon SQS retains a message.
          * ``Policy`` - Returns the policy of the queue.
          * ``QueueArn`` - Returns the Amazon resource name (ARN) of the queue.
          * ``ReceiveMessageWaitTimeSeconds`` - Returns the length of time, in seconds, for which the ``ReceiveMessage`` action waits for a message to arrive.
          * ``RedrivePolicy`` - Returns the string that includes the parameters for dead-letter queue functionality of the source queue. For more information about the redrive policy and dead-letter queues, see `Using Amazon SQS Dead-Letter Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
            * ``deadLetterTargetArn`` - The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of ``maxReceiveCount`` is exceeded.
            * ``maxReceiveCount`` - The number of times a message is delivered to the source queue before being moved to the dead-letter queue. When the ``ReceiveCount`` for a message exceeds the ``maxReceiveCount`` for a queue, Amazon SQS moves the message to the dead-letter-queue.
          * ``VisibilityTimeout`` - Returns the visibility timeout for the queue. For more information about the visibility timeout, see `Visibility Timeout <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
          The following attributes apply only to `server-side-encryption <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html>`__ :
          * ``KmsMasterKeyId`` - Returns the ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see `Key Terms <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms>`__ .
          * ``KmsDataKeyReusePeriodSeconds`` - Returns the length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. For more information, see `How Does the Data Key Reuse Period Work? <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work>`__ .
          The following attributes apply only to `FIFO (first-in-first-out) queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html>`__ :
          * ``FifoQueue`` - Returns whether the queue is FIFO. For more information, see `FIFO Queue Logic <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-understanding-logic>`__ in the *Amazon Simple Queue Service Developer Guide* .
          .. note::
             To determine whether a queue is `FIFO <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html>`__ , you can check whether ``QueueName`` ends with the ``.fifo`` suffix.
          * ``ContentBasedDeduplication`` - Returns whether content-based deduplication is enabled for the queue. For more information, see `Exactly-Once Processing <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing>`__ in the *Amazon Simple Queue Service Developer Guide* .
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def get_queue_url(self, QueueName: str, QueueOwnerAWSAccountId: str = None) -> Dict:
        """
        Returns the URL of an existing Amazon SQS queue.
        To access a queue that belongs to another AWS account, use the ``QueueOwnerAWSAccountId`` parameter to specify the account ID of the queue's owner. The queue's owner must grant you permission to access the queue. For more information about shared queue access, see ``  AddPermission `` or see `Allow Developers to Write Messages to a Shared Queue <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-writing-an-sqs-policy.html#write-messages-to-shared-queue>`__ in the *Amazon Simple Queue Service Developer Guide* . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/GetQueueUrl>`_
        
        **Request Syntax**
        ::
          response = client.get_queue_url(
              QueueName='string',
              QueueOwnerAWSAccountId='string'
          )
        
        **Response Syntax**
        ::
            {
                'QueueUrl': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            For more information, see `Interpreting Responses <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-api-responses.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
            - **QueueUrl** *(string) --* 
              The URL of the queue.
        :type QueueName: string
        :param QueueName: **[REQUIRED]**
          The name of the queue whose URL must be fetched. Maximum 80 characters. Valid values: alphanumeric characters, hyphens (``-`` ), and underscores (``_`` ).
          Queue URLs and names are case-sensitive.
        :type QueueOwnerAWSAccountId: string
        :param QueueOwnerAWSAccountId:
          The AWS account ID of the account that created the queue.
        :rtype: dict
        :returns:
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

    def list_dead_letter_source_queues(self, QueueUrl: str) -> Dict:
        """
        Returns a list of your queues that have the ``RedrivePolicy`` queue attribute configured with a dead-letter queue.
        For more information about using dead-letter queues, see `Using Amazon SQS Dead-Letter Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/ListDeadLetterSourceQueues>`_
        
        **Request Syntax**
        ::
          response = client.list_dead_letter_source_queues(
              QueueUrl='string'
          )
        
        **Response Syntax**
        ::
            {
                'queueUrls': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of your dead letter source queues.
            - **queueUrls** *(list) --* 
              A list of source queue URLs that have the ``RedrivePolicy`` queue attribute configured with a dead-letter queue.
              - *(string) --* 
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of a dead-letter queue.
          Queue URLs and names are case-sensitive.
        :rtype: dict
        :returns:
        """
        pass

    def list_queue_tags(self, QueueUrl: str) -> Dict:
        """
        List all cost allocation tags added to the specified Amazon SQS queue. For an overview, see `Tagging Your Amazon SQS Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        When you use queue tags, keep the following guidelines in mind:
        * Adding more than 50 tags to a queue isn't recommended. 
        * Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings. 
        * Tags are case-sensitive. 
        * A new tag with a key identical to that of an existing tag overwrites the existing tag. 
        * Tagging actions are limited to 5 TPS per AWS account. If your application requires a higher throughput, file a `technical support request <https://console.aws.amazon.com/support/home#/case/create?issueType=technical>`__ . 
        For a full list of tag restrictions, see `Limits Related to Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html#limits-queues>`__ in the *Amazon Simple Queue Service Developer Guide* .
        .. note::
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/ListQueueTags>`_
        
        **Request Syntax**
        ::
          response = client.list_queue_tags(
              QueueUrl='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tags** *(dict) --* 
              The list of all tags added to the specified queue.
              - *(string) --* 
                - *(string) --* 
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the queue.
        :rtype: dict
        :returns:
        """
        pass

    def list_queues(self, QueueNamePrefix: str = None) -> Dict:
        """
        Returns a list of your queues. The maximum number of queues that can be returned is 1,000. If you specify a value for the optional ``QueueNamePrefix`` parameter, only queues with a name that begins with the specified value are returned.
        .. note::
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/ListQueues>`_
        
        **Request Syntax**
        ::
          response = client.list_queues(
              QueueNamePrefix='string'
          )
        
        **Response Syntax**
        ::
            {
                'QueueUrls': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of your queues.
            - **QueueUrls** *(list) --* 
              A list of queue URLs, up to 1,000 entries.
              - *(string) --* 
        :type QueueNamePrefix: string
        :param QueueNamePrefix:
          A string to use for filtering the list results. Only those queues whose name begins with the specified string are returned.
          Queue URLs and names are case-sensitive.
        :rtype: dict
        :returns:
        """
        pass

    def purge_queue(self, QueueUrl: str):
        """
        Deletes the messages in a queue specified by the ``QueueURL`` parameter.
        .. warning::
          When you use the ``PurgeQueue`` action, you can't retrieve any messages deleted from a queue.
          The message deletion process takes up to 60 seconds. We recommend waiting for 60 seconds regardless of your queue's size. 
        Messages sent to the queue *before* you call ``PurgeQueue`` might be received but are deleted within the next minute.
        Messages sent to the queue *after* you call ``PurgeQueue`` might be deleted while the queue is being purged.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/PurgeQueue>`_
        
        **Request Syntax**
        ::
          response = client.purge_queue(
              QueueUrl='string'
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the queue from which the ``PurgeQueue`` action deletes messages.
          Queue URLs and names are case-sensitive.
        :returns: None
        """
        pass

    def receive_message(self, QueueUrl: str, AttributeNames: List = None, MessageAttributeNames: List = None, MaxNumberOfMessages: int = None, VisibilityTimeout: int = None, WaitTimeSeconds: int = None, ReceiveRequestAttemptId: str = None) -> Dict:
        """
        Retrieves one or more messages (up to 10), from the specified queue. Using the ``WaitTimeSeconds`` parameter enables long-poll support. For more information, see `Amazon SQS Long Polling <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html>`__ in the *Amazon Simple Queue Service Developer Guide* . 
        Short poll is the default behavior where a weighted random set of machines is sampled on a ``ReceiveMessage`` call. Thus, only the messages on the sampled machines are returned. If the number of messages in the queue is small (fewer than 1,000), you most likely get fewer messages than you requested per ``ReceiveMessage`` call. If the number of messages in the queue is extremely small, you might not receive any messages in a particular ``ReceiveMessage`` response. If this happens, repeat the request. 
        For each message returned, the response includes the following:
        * The message body. 
        * An MD5 digest of the message body. For information about MD5, see `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ . 
        * The ``MessageId`` you received when you sent the message to the queue. 
        * The receipt handle. 
        * The message attributes. 
        * An MD5 digest of the message attributes. 
        The receipt handle is the identifier you must provide when deleting the message. For more information, see `Queue and Message Identifiers <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        You can provide the ``VisibilityTimeout`` parameter in your request. The parameter is applied to the messages that Amazon SQS returns in the response. If you don't include the parameter, the overall visibility timeout for the queue is used for the returned messages. For more information, see `Visibility Timeout <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        A message that isn't deleted or a message whose visibility isn't extended before the visibility timeout expires counts as a failed receive. Depending on the configuration of the queue, the message might be sent to the dead-letter queue.
        .. note::
          In the future, new attributes might be added. If you write code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/ReceiveMessage>`_
        
        **Request Syntax**
        ::
          response = client.receive_message(
              QueueUrl='string',
              AttributeNames=[
                  'All'|'Policy'|'VisibilityTimeout'|'MaximumMessageSize'|'MessageRetentionPeriod'|'ApproximateNumberOfMessages'|'ApproximateNumberOfMessagesNotVisible'|'CreatedTimestamp'|'LastModifiedTimestamp'|'QueueArn'|'ApproximateNumberOfMessagesDelayed'|'DelaySeconds'|'ReceiveMessageWaitTimeSeconds'|'RedrivePolicy'|'FifoQueue'|'ContentBasedDeduplication'|'KmsMasterKeyId'|'KmsDataKeyReusePeriodSeconds',
              ],
              MessageAttributeNames=[
                  'string',
              ],
              MaxNumberOfMessages=123,
              VisibilityTimeout=123,
              WaitTimeSeconds=123,
              ReceiveRequestAttemptId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Messages': [
                    {
                        'MessageId': 'string',
                        'ReceiptHandle': 'string',
                        'MD5OfBody': 'string',
                        'Body': 'string',
                        'Attributes': {
                            'string': 'string'
                        },
                        'MD5OfMessageAttributes': 'string',
                        'MessageAttributes': {
                            'string': {
                                'StringValue': 'string',
                                'BinaryValue': b'bytes',
                                'StringListValues': [
                                    'string',
                                ],
                                'BinaryListValues': [
                                    b'bytes',
                                ],
                                'DataType': 'string'
                            }
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of received messages.
            - **Messages** *(list) --* 
              A list of messages.
              - *(dict) --* 
                An Amazon SQS message.
                - **MessageId** *(string) --* 
                  A unique identifier for the message. A ``MessageId`` is considered unique across all AWS accounts for an extended period of time.
                - **ReceiptHandle** *(string) --* 
                  An identifier associated with the act of receiving the message. A new receipt handle is returned every time you receive a message. When deleting a message, you provide the last received receipt handle to delete the message.
                - **MD5OfBody** *(string) --* 
                  An MD5 digest of the non-URL-encoded message body string.
                - **Body** *(string) --* 
                  The message's contents (not URL-encoded).
                - **Attributes** *(dict) --* 
                  A map of the attributes requested in ``  ReceiveMessage `` to their respective values. Supported attributes:
                  * ``ApproximateReceiveCount``   
                  * ``ApproximateFirstReceiveTimestamp``   
                  * ``MessageDeduplicationId``   
                  * ``MessageGroupId``   
                  * ``SenderId``   
                  * ``SentTimestamp``   
                  * ``SequenceNumber``   
                   ``ApproximateFirstReceiveTimestamp`` and ``SentTimestamp`` are each returned as an integer representing the `epoch time <http://en.wikipedia.org/wiki/Unix_time>`__ in milliseconds.
                  - *(string) --* 
                    - *(string) --* 
                - **MD5OfMessageAttributes** *(string) --* 
                  An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .
                - **MessageAttributes** *(dict) --* 
                  Each message attribute consists of a ``Name`` , ``Type`` , and ``Value`` . For more information, see `Amazon SQS Message Attributes <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
                  - *(string) --* 
                    - *(dict) --* 
                      The user-specified message attribute value. For string data types, the ``Value`` attribute has the same restrictions on the content as the message body. For more information, see ``  SendMessage .``  
                       ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part of the message size restriction (256 KB or 262,144 bytes).
                      - **StringValue** *(string) --* 
                        Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .
                      - **BinaryValue** *(bytes) --* 
                        Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.
                      - **StringListValues** *(list) --* 
                        Not implemented. Reserved for future use.
                        - *(string) --* 
                      - **BinaryListValues** *(list) --* 
                        Not implemented. Reserved for future use.
                        - *(bytes) --* 
                      - **DataType** *(string) --* 
                        Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .
                        You can also append custom labels. For more information, see `Amazon SQS Message Attributes <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue from which messages are received.
          Queue URLs and names are case-sensitive.
        :type AttributeNames: list
        :param AttributeNames:
          A list of s that need to be returned along with each message. These attributes include:
          * ``All`` - Returns all values.
          * ``ApproximateFirstReceiveTimestamp`` - Returns the time the message was first received from the queue (`epoch time <http://en.wikipedia.org/wiki/Unix_time>`__ in milliseconds).
          * ``ApproximateReceiveCount`` - Returns the number of times a message has been received from the queue but not deleted.
          * ``SenderId``
            * For an IAM user, returns the IAM user ID, for example ``ABCDEFGHI1JKLMNOPQ23R`` .
            * For an IAM role, returns the IAM role ID, for example ``ABCDE1F2GH3I4JK5LMNOP:i-a123b456`` .
          * ``SentTimestamp`` - Returns the time the message was sent to the queue (`epoch time <http://en.wikipedia.org/wiki/Unix_time>`__ in milliseconds).
          * ``MessageDeduplicationId`` - Returns the value provided by the producer that calls the ``  SendMessage `` action.
          * ``MessageGroupId`` - Returns the value provided by the producer that calls the ``  SendMessage `` action. Messages with the same ``MessageGroupId`` are returned in sequence.
          * ``SequenceNumber`` - Returns the value provided by Amazon SQS.
          - *(string) --*
        :type MessageAttributeNames: list
        :param MessageAttributeNames:
          The name of the message attribute, where *N* is the index.
          * The name can contain alphanumeric characters and the underscore (``_`` ), hyphen (``-`` ), and period (``.`` ).
          * The name is case-sensitive and must be unique among all attribute names for the message.
          * The name must not start with AWS-reserved prefixes such as ``AWS.`` or ``Amazon.`` (or any casing variants).
          * The name must not start or end with a period (``.`` ), and it should not have periods in succession (``..`` ).
          * The name can be up to 256 characters long.
          When using ``ReceiveMessage`` , you can send a list of attribute names to receive, or you can return all of the attributes by specifying ``All`` or ``.*`` in your request. You can also use all message attributes starting with a prefix, for example ``bar.*`` .
          - *(string) --*
        :type MaxNumberOfMessages: integer
        :param MaxNumberOfMessages:
          The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1.
        :type VisibilityTimeout: integer
        :param VisibilityTimeout:
          The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ``ReceiveMessage`` request.
        :type WaitTimeSeconds: integer
        :param WaitTimeSeconds:
          The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than ``WaitTimeSeconds`` . If no messages are available and the wait time expires, the call returns successfully with an empty list of messages.
        :type ReceiveRequestAttemptId: string
        :param ReceiveRequestAttemptId:
          This parameter applies only to FIFO (first-in-first-out) queues.
          The token used for deduplication of ``ReceiveMessage`` calls. If a networking issue occurs after a ``ReceiveMessage`` action, and instead of a response you receive a generic error, you can retry the same action with an identical ``ReceiveRequestAttemptId`` to retrieve the same set of messages, even if their visibility timeout has not yet expired.
          * You can use ``ReceiveRequestAttemptId`` only for 5 minutes after a ``ReceiveMessage`` action.
          * When you set ``FifoQueue`` , a caller of the ``ReceiveMessage`` action can provide a ``ReceiveRequestAttemptId`` explicitly.
          * If a caller of the ``ReceiveMessage`` action doesn\'t provide a ``ReceiveRequestAttemptId`` , Amazon SQS generates a ``ReceiveRequestAttemptId`` .
          * You can retry the ``ReceiveMessage`` action with the same ``ReceiveRequestAttemptId`` if none of the messages have been modified (deleted or had their visibility changes).
          * During a visibility timeout, subsequent calls with the same ``ReceiveRequestAttemptId`` return the same messages and receipt handles. If a retry occurs within the deduplication interval, it resets the visibility timeout. For more information, see `Visibility Timeout <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
          .. warning::
             If a caller of the ``ReceiveMessage`` action still processes messages when the visibility timeout expires and messages become visible, another worker consuming from the same queue can receive the same messages and therefore process duplicates. Also, if a consumer whose message processing time is longer than the visibility timeout tries to delete the processed messages, the action fails with an error. To mitigate this effect, ensure that your application observes a safe threshold before the visibility timeout expires and extend the visibility timeout as necessary.
          * While messages with a particular ``MessageGroupId`` are invisible, no more messages belonging to the same ``MessageGroupId`` are returned until the visibility timeout expires. You can still receive messages with another ``MessageGroupId`` as long as it is also visible.
          * If a caller of ``ReceiveMessage`` can\'t track the ``ReceiveRequestAttemptId`` , no retries work until the original visibility timeout expires. As a result, delays might occur but the messages in the queue remain in a strict order.
          The length of ``ReceiveRequestAttemptId`` is 128 characters. ``ReceiveRequestAttemptId`` can contain alphanumeric characters (``a-z`` , ``A-Z`` , ``0-9`` ) and punctuation (``!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~`` ).
          For best practices of using ``ReceiveRequestAttemptId`` , see `Using the ReceiveRequestAttemptId Request Parameter <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-receiverequestattemptid-request-parameter.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        :rtype: dict
        :returns:
        """
        pass

    def remove_permission(self, QueueUrl: str, Label: str):
        """
        Revokes any permissions in the queue policy that matches the specified ``Label`` parameter.
        .. note::
          Only the owner of a queue can remove permissions from it.
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/RemovePermission>`_
        
        **Request Syntax**
        ::
          response = client.remove_permission(
              QueueUrl='string',
              Label='string'
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue from which permissions are removed.
          Queue URLs and names are case-sensitive.
        :type Label: string
        :param Label: **[REQUIRED]**
          The identification of the permission to remove. This is the label added using the ``  AddPermission `` action.
        :returns: None
        """
        pass

    def send_message(self, QueueUrl: str, MessageBody: str, DelaySeconds: int = None, MessageAttributes: Dict = None, MessageDeduplicationId: str = None, MessageGroupId: str = None) -> Dict:
        """
        Delivers a message to the specified queue.
        .. warning::
          A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed:
           ``#x9`` | ``#xA`` | ``#xD`` | ``#x20`` to ``#xD7FF`` | ``#xE000`` to ``#xFFFD`` | ``#x10000`` to ``#x10FFFF``  
          Any characters not included in this list will be rejected. For more information, see the `W3C specification for characters <http://www.w3.org/TR/REC-xml/#charsets>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/SendMessage>`_
        
        **Request Syntax**
        ::
          response = client.send_message(
              QueueUrl='string',
              MessageBody='string',
              DelaySeconds=123,
              MessageAttributes={
                  'string': {
                      'StringValue': 'string',
                      'BinaryValue': b'bytes',
                      'StringListValues': [
                          'string',
                      ],
                      'BinaryListValues': [
                          b'bytes',
                      ],
                      'DataType': 'string'
                  }
              },
              MessageDeduplicationId='string',
              MessageGroupId='string'
          )
        
        **Response Syntax**
        ::
            {
                'MD5OfMessageBody': 'string',
                'MD5OfMessageAttributes': 'string',
                'MessageId': 'string',
                'SequenceNumber': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The ``MD5OfMessageBody`` and ``MessageId`` elements.
            - **MD5OfMessageBody** *(string) --* 
              An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .
            - **MD5OfMessageAttributes** *(string) --* 
              An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .
            - **MessageId** *(string) --* 
              An attribute containing the ``MessageId`` of the message sent to the queue. For more information, see `Queue and Message Identifiers <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html>`__ in the *Amazon Simple Queue Service Developer Guide* . 
            - **SequenceNumber** *(string) --* 
              This parameter applies only to FIFO (first-in-first-out) queues.
              The large, non-consecutive number that Amazon SQS assigns to each message.
              The length of ``SequenceNumber`` is 128 bits. ``SequenceNumber`` continues to increase for a particular ``MessageGroupId`` .
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue to which a message is sent.
          Queue URLs and names are case-sensitive.
        :type MessageBody: string
        :param MessageBody: **[REQUIRED]**
          The message to send. The maximum string size is 256 KB.
          .. warning::
            A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed:
             ``#x9`` | ``#xA`` | ``#xD`` | ``#x20`` to ``#xD7FF`` | ``#xE000`` to ``#xFFFD`` | ``#x10000`` to ``#x10FFFF``
            Any characters not included in this list will be rejected. For more information, see the `W3C specification for characters <http://www.w3.org/TR/REC-xml/#charsets>`__ .
        :type DelaySeconds: integer
        :param DelaySeconds:
          The length of time, in seconds, for which to delay a specific message. Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive ``DelaySeconds`` value become available for processing after the delay period is finished. If you don\'t specify a value, the default value for the queue applies.
          .. note::
            When you set ``FifoQueue`` , you can\'t set ``DelaySeconds`` per message. You can set this parameter only on a queue level.
        :type MessageAttributes: dict
        :param MessageAttributes:
          Each message attribute consists of a ``Name`` , ``Type`` , and ``Value`` . For more information, see `Amazon SQS Message Attributes <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
          - *(string) --*
            - *(dict) --*
              The user-specified message attribute value. For string data types, the ``Value`` attribute has the same restrictions on the content as the message body. For more information, see ``  SendMessage .``
               ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part of the message size restriction (256 KB or 262,144 bytes).
              - **StringValue** *(string) --*
                Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .
              - **BinaryValue** *(bytes) --*
                Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.
              - **StringListValues** *(list) --*
                Not implemented. Reserved for future use.
                - *(string) --*
              - **BinaryListValues** *(list) --*
                Not implemented. Reserved for future use.
                - *(bytes) --*
              - **DataType** *(string) --* **[REQUIRED]**
                Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .
                You can also append custom labels. For more information, see `Amazon SQS Message Attributes <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        :type MessageDeduplicationId: string
        :param MessageDeduplicationId:
          This parameter applies only to FIFO (first-in-first-out) queues.
          The token used for deduplication of sent messages. If a message with a particular ``MessageDeduplicationId`` is sent successfully, any messages sent with the same ``MessageDeduplicationId`` are accepted successfully but aren\'t delivered during the 5-minute deduplication interval. For more information, see `Exactly-Once Processing <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing>`__ in the *Amazon Simple Queue Service Developer Guide* .
          * Every message must have a unique ``MessageDeduplicationId`` ,
            * You may provide a ``MessageDeduplicationId`` explicitly.
            * If you aren\'t able to provide a ``MessageDeduplicationId`` and you enable ``ContentBasedDeduplication`` for your queue, Amazon SQS uses a SHA-256 hash to generate the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the message).
            * If you don\'t provide a ``MessageDeduplicationId`` and the queue doesn\'t have ``ContentBasedDeduplication`` set, the action fails with an error.
            * If the queue has ``ContentBasedDeduplication`` set, your ``MessageDeduplicationId`` overrides the generated one.
          * When ``ContentBasedDeduplication`` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
          * If you send one message with ``ContentBasedDeduplication`` enabled and then another message with a ``MessageDeduplicationId`` that is the same as the one generated for the first ``MessageDeduplicationId`` , the two messages are treated as duplicates and only one copy of the message is delivered.
          .. note::
            The ``MessageDeduplicationId`` is available to the consumer of the message (this can be useful for troubleshooting delivery issues).
            If a message is sent successfully but the acknowledgement is lost and the message is resent with the same ``MessageDeduplicationId`` after the deduplication interval, Amazon SQS can\'t detect duplicate messages.
            Amazon SQS continues to keep track of the message deduplication ID even after the message is received and deleted.
          The length of ``MessageDeduplicationId`` is 128 characters. ``MessageDeduplicationId`` can contain alphanumeric characters (``a-z`` , ``A-Z`` , ``0-9`` ) and punctuation (``!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~`` ).
          For best practices of using ``MessageDeduplicationId`` , see `Using the MessageDeduplicationId Property <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        :type MessageGroupId: string
        :param MessageGroupId:
          This parameter applies only to FIFO (first-in-first-out) queues.
          The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use ``MessageGroupId`` values (for example, session data for multiple users). In this scenario, multiple consumers can process the queue, but the session data of each user is processed in a FIFO fashion.
          * You must associate a non-empty ``MessageGroupId`` with a message. If you don\'t provide a ``MessageGroupId`` , the action fails.
          * ``ReceiveMessage`` might return messages with multiple ``MessageGroupId`` values. For each ``MessageGroupId`` , the messages are sorted by time sent. The caller can\'t specify a ``MessageGroupId`` .
          The length of ``MessageGroupId`` is 128 characters. Valid values: alphanumeric characters and punctuation ``(!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~)`` .
          For best practices of using ``MessageGroupId`` , see `Using the MessageGroupId Property <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
          .. warning::
             ``MessageGroupId`` is required for FIFO queues. You can\'t use it for Standard queues.
        :rtype: dict
        :returns:
        """
        pass

    def send_message_batch(self, QueueUrl: str, Entries: List) -> Dict:
        """
        Delivers up to ten messages to the specified queue. This is a batch version of ``  SendMessage .`` For a FIFO queue, multiple messages within a single batch are enqueued in the order they are sent.
        The result of sending each message is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of ``200`` .
        The maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 256 KB (262,144 bytes).
        .. warning::
          A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed:
           ``#x9`` | ``#xA`` | ``#xD`` | ``#x20`` to ``#xD7FF`` | ``#xE000`` to ``#xFFFD`` | ``#x10000`` to ``#x10FFFF``  
          Any characters not included in this list will be rejected. For more information, see the `W3C specification for characters <http://www.w3.org/TR/REC-xml/#charsets>`__ .
        If you don't specify the ``DelaySeconds`` parameter for an entry, Amazon SQS uses the default value for the queue.
        Some actions take lists of parameters. These lists are specified using the ``param.n`` notation. Values of ``n`` are integers starting from 1. For example, a parameter list with two elements looks like this:
         ``&Attribute.1=first``  
         ``&Attribute.2=second``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/SendMessageBatch>`_
        
        **Request Syntax**
        ::
          response = client.send_message_batch(
              QueueUrl='string',
              Entries=[
                  {
                      'Id': 'string',
                      'MessageBody': 'string',
                      'DelaySeconds': 123,
                      'MessageAttributes': {
                          'string': {
                              'StringValue': 'string',
                              'BinaryValue': b'bytes',
                              'StringListValues': [
                                  'string',
                              ],
                              'BinaryListValues': [
                                  b'bytes',
                              ],
                              'DataType': 'string'
                          }
                      },
                      'MessageDeduplicationId': 'string',
                      'MessageGroupId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'Successful': [
                    {
                        'Id': 'string',
                        'MessageId': 'string',
                        'MD5OfMessageBody': 'string',
                        'MD5OfMessageAttributes': 'string',
                        'SequenceNumber': 'string'
                    },
                ],
                'Failed': [
                    {
                        'Id': 'string',
                        'SenderFault': True|False,
                        'Code': 'string',
                        'Message': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            For each message in the batch, the response contains a ``  SendMessageBatchResultEntry `` tag if the message succeeds or a ``  BatchResultErrorEntry `` tag if the message fails.
            - **Successful** *(list) --* 
              A list of ``  SendMessageBatchResultEntry `` items.
              - *(dict) --* 
                Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``  
                - **Id** *(string) --* 
                  An identifier for the message in this batch.
                - **MessageId** *(string) --* 
                  An identifier for the message.
                - **MD5OfMessageBody** *(string) --* 
                  An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .
                - **MD5OfMessageAttributes** *(string) --* 
                  An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .
                - **SequenceNumber** *(string) --* 
                  This parameter applies only to FIFO (first-in-first-out) queues.
                  The large, non-consecutive number that Amazon SQS assigns to each message.
                  The length of ``SequenceNumber`` is 128 bits. As ``SequenceNumber`` continues to increase for a particular ``MessageGroupId`` .
            - **Failed** *(list) --* 
              A list of ``  BatchResultErrorEntry `` items with error details about each message that can't be enqueued.
              - *(dict) --* 
                Gives a detailed description of the result of an action on each entry in the request.
                - **Id** *(string) --* 
                  The ``Id`` of an entry in a batch request.
                - **SenderFault** *(boolean) --* 
                  Specifies whether the error happened due to the producer.
                - **Code** *(string) --* 
                  An error code representing why the action failed on this entry.
                - **Message** *(string) --* 
                  A message explaining why the action failed on this entry.
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue to which batched messages are sent.
          Queue URLs and names are case-sensitive.
        :type Entries: list
        :param Entries: **[REQUIRED]**
          A list of ``  SendMessageBatchRequestEntry `` items.
          - *(dict) --*
            Contains the details of a single Amazon SQS message along with an ``Id`` .
            - **Id** *(string) --* **[REQUIRED]**
              An identifier for a message in this batch used to communicate the result.
              .. note::
                The ``Id`` s of a batch request need to be unique within a request
                This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (_).
            - **MessageBody** *(string) --* **[REQUIRED]**
              The body of the message.
            - **DelaySeconds** *(integer) --*
              The length of time, in seconds, for which a specific message is delayed. Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive ``DelaySeconds`` value become available for processing after the delay period is finished. If you don\'t specify a value, the default value for the queue is applied.
              .. note::
                When you set ``FifoQueue`` , you can\'t set ``DelaySeconds`` per message. You can set this parameter only on a queue level.
            - **MessageAttributes** *(dict) --*
              Each message attribute consists of a ``Name`` , ``Type`` , and ``Value`` . For more information, see `Amazon SQS Message Attributes <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
              - *(string) --*
                - *(dict) --*
                  The user-specified message attribute value. For string data types, the ``Value`` attribute has the same restrictions on the content as the message body. For more information, see ``  SendMessage .``
                   ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part of the message size restriction (256 KB or 262,144 bytes).
                  - **StringValue** *(string) --*
                    Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .
                  - **BinaryValue** *(bytes) --*
                    Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.
                  - **StringListValues** *(list) --*
                    Not implemented. Reserved for future use.
                    - *(string) --*
                  - **BinaryListValues** *(list) --*
                    Not implemented. Reserved for future use.
                    - *(bytes) --*
                  - **DataType** *(string) --* **[REQUIRED]**
                    Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .
                    You can also append custom labels. For more information, see `Amazon SQS Message Attributes <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
            - **MessageDeduplicationId** *(string) --*
              This parameter applies only to FIFO (first-in-first-out) queues.
              The token used for deduplication of messages within a 5-minute minimum deduplication interval. If a message with a particular ``MessageDeduplicationId`` is sent successfully, subsequent messages with the same ``MessageDeduplicationId`` are accepted successfully but aren\'t delivered. For more information, see `Exactly-Once Processing <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing>`__ in the *Amazon Simple Queue Service Developer Guide* .
              * Every message must have a unique ``MessageDeduplicationId`` ,
                * You may provide a ``MessageDeduplicationId`` explicitly.
                * If you aren\'t able to provide a ``MessageDeduplicationId`` and you enable ``ContentBasedDeduplication`` for your queue, Amazon SQS uses a SHA-256 hash to generate the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the message).
                * If you don\'t provide a ``MessageDeduplicationId`` and the queue doesn\'t have ``ContentBasedDeduplication`` set, the action fails with an error.
                * If the queue has ``ContentBasedDeduplication`` set, your ``MessageDeduplicationId`` overrides the generated one.
              * When ``ContentBasedDeduplication`` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
              * If you send one message with ``ContentBasedDeduplication`` enabled and then another message with a ``MessageDeduplicationId`` that is the same as the one generated for the first ``MessageDeduplicationId`` , the two messages are treated as duplicates and only one copy of the message is delivered.
              .. note::
                The ``MessageDeduplicationId`` is available to the consumer of the message (this can be useful for troubleshooting delivery issues).
                If a message is sent successfully but the acknowledgement is lost and the message is resent with the same ``MessageDeduplicationId`` after the deduplication interval, Amazon SQS can\'t detect duplicate messages.
                Amazon SQS continues to keep track of the message deduplication ID even after the message is received and deleted.
              The length of ``MessageDeduplicationId`` is 128 characters. ``MessageDeduplicationId`` can contain alphanumeric characters (``a-z`` , ``A-Z`` , ``0-9`` ) and punctuation (``!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~`` ).
              For best practices of using ``MessageDeduplicationId`` , see `Using the MessageDeduplicationId Property <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
            - **MessageGroupId** *(string) --*
              This parameter applies only to FIFO (first-in-first-out) queues.
              The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use ``MessageGroupId`` values (for example, session data for multiple users). In this scenario, multiple consumers can process the queue, but the session data of each user is processed in a FIFO fashion.
              * You must associate a non-empty ``MessageGroupId`` with a message. If you don\'t provide a ``MessageGroupId`` , the action fails.
              * ``ReceiveMessage`` might return messages with multiple ``MessageGroupId`` values. For each ``MessageGroupId`` , the messages are sorted by time sent. The caller can\'t specify a ``MessageGroupId`` .
              The length of ``MessageGroupId`` is 128 characters. Valid values: alphanumeric characters and punctuation ``(!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~)`` .
              For best practices of using ``MessageGroupId`` , see `Using the MessageGroupId Property <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
              .. warning::
                 ``MessageGroupId`` is required for FIFO queues. You can\'t use it for Standard queues.
        :rtype: dict
        :returns:
        """
        pass

    def set_queue_attributes(self, QueueUrl: str, Attributes: Dict):
        """
        Sets the value of one or more queue attributes. When you change a queue's attributes, the change can take up to 60 seconds for most of the attributes to propagate throughout the Amazon SQS system. Changes made to the ``MessageRetentionPeriod`` attribute can take up to 15 minutes.
        .. note::
          In the future, new attributes might be added. If you write code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/SetQueueAttributes>`_
        
        **Request Syntax**
        ::
          response = client.set_queue_attributes(
              QueueUrl='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the Amazon SQS queue whose attributes are set.
          Queue URLs and names are case-sensitive.
        :type Attributes: dict
        :param Attributes: **[REQUIRED]**
          A map of attributes to set.
          The following lists the names, descriptions, and values of the special request parameters that the ``SetQueueAttributes`` action uses:
          * ``DelaySeconds`` - The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 (15 minutes). Default: 0.
          * ``MaximumMessageSize`` - The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) up to 262,144 bytes (256 KiB). Default: 262,144 (256 KiB).
          * ``MessageRetentionPeriod`` - The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer representing seconds, from 60 (1 minute) to 1,209,600 (14 days). Default: 345,600 (4 days).
          * ``Policy`` - The queue\'s policy. A valid AWS policy. For more information about policy structure, see `Overview of AWS IAM Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html>`__ in the *Amazon IAM User Guide* .
          * ``ReceiveMessageWaitTimeSeconds`` - The length of time, in seconds, for which a ``  ReceiveMessage `` action waits for a message to arrive. Valid values: an integer from 0 to 20 (seconds). Default: 0.
          * ``RedrivePolicy`` - The string that includes the parameters for the dead-letter queue functionality of the source queue. For more information about the redrive policy and dead-letter queues, see `Using Amazon SQS Dead-Letter Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
            * ``deadLetterTargetArn`` - The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of ``maxReceiveCount`` is exceeded.
            * ``maxReceiveCount`` - The number of times a message is delivered to the source queue before being moved to the dead-letter queue. When the ``ReceiveCount`` for a message exceeds the ``maxReceiveCount`` for a queue, Amazon SQS moves the message to the dead-letter-queue.
          .. note::
            The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a standard queue must also be a standard queue.
          * ``VisibilityTimeout`` - The visibility timeout for the queue, in seconds. Valid values: an integer from 0 to 43,200 (12 hours). Default: 30. For more information about the visibility timeout, see `Visibility Timeout <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
          The following attributes apply only to `server-side-encryption <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html>`__ :
          * ``KmsMasterKeyId`` - The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see `Key Terms <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms>`__ . While the alias of the AWS-managed CMK for Amazon SQS is always ``alias/aws/sqs`` , the alias of a custom CMK can, for example, be ``alias/*MyAlias* `` . For more examples, see `KeyId <http://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters>`__ in the *AWS Key Management Service API Reference* .
          * ``KmsDataKeyReusePeriodSeconds`` - The length of time, in seconds, for which Amazon SQS can reuse a `data key <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys>`__ to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). Default: 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which might incur charges after Free Tier. For more information, see `How Does the Data Key Reuse Period Work? <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work>`__ .
          The following attribute applies only to `FIFO (first-in-first-out) queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html>`__ :
          * ``ContentBasedDeduplication`` - Enables content-based deduplication. For more information, see `Exactly-Once Processing <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing>`__ in the *Amazon Simple Queue Service Developer Guide* .
            * Every message must have a unique ``MessageDeduplicationId`` ,
              * You may provide a ``MessageDeduplicationId`` explicitly.
              * If you aren\'t able to provide a ``MessageDeduplicationId`` and you enable ``ContentBasedDeduplication`` for your queue, Amazon SQS uses a SHA-256 hash to generate the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the message).
              * If you don\'t provide a ``MessageDeduplicationId`` and the queue doesn\'t have ``ContentBasedDeduplication`` set, the action fails with an error.
              * If the queue has ``ContentBasedDeduplication`` set, your ``MessageDeduplicationId`` overrides the generated one.
            * When ``ContentBasedDeduplication`` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
            * If you send one message with ``ContentBasedDeduplication`` enabled and then another message with a ``MessageDeduplicationId`` that is the same as the one generated for the first ``MessageDeduplicationId`` , the two messages are treated as duplicates and only one copy of the message is delivered.
          - *(string) --*
            - *(string) --*
        :returns: None
        """
        pass

    def tag_queue(self, QueueUrl: str, Tags: Dict):
        """
        Add cost allocation tags to the specified Amazon SQS queue. For an overview, see `Tagging Your Amazon SQS Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        When you use queue tags, keep the following guidelines in mind:
        * Adding more than 50 tags to a queue isn't recommended. 
        * Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings. 
        * Tags are case-sensitive. 
        * A new tag with a key identical to that of an existing tag overwrites the existing tag. 
        * Tagging actions are limited to 5 TPS per AWS account. If your application requires a higher throughput, file a `technical support request <https://console.aws.amazon.com/support/home#/case/create?issueType=technical>`__ . 
        For a full list of tag restrictions, see `Limits Related to Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html#limits-queues>`__ in the *Amazon Simple Queue Service Developer Guide* .
        .. note::
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/TagQueue>`_
        
        **Request Syntax**
        ::
          response = client.tag_queue(
              QueueUrl='string',
              Tags={
                  'string': 'string'
              }
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the queue.
        :type Tags: dict
        :param Tags: **[REQUIRED]**
          The list of tags to be added to the specified queue.
          - *(string) --*
            - *(string) --*
        :returns: None
        """
        pass

    def untag_queue(self, QueueUrl: str, TagKeys: List):
        """
        Remove cost allocation tags from the specified Amazon SQS queue. For an overview, see `Tagging Your Amazon SQS Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html>`__ in the *Amazon Simple Queue Service Developer Guide* .
        When you use queue tags, keep the following guidelines in mind:
        * Adding more than 50 tags to a queue isn't recommended. 
        * Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings. 
        * Tags are case-sensitive. 
        * A new tag with a key identical to that of an existing tag overwrites the existing tag. 
        * Tagging actions are limited to 5 TPS per AWS account. If your application requires a higher throughput, file a `technical support request <https://console.aws.amazon.com/support/home#/case/create?issueType=technical>`__ . 
        For a full list of tag restrictions, see `Limits Related to Queues <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html#limits-queues>`__ in the *Amazon Simple Queue Service Developer Guide* .
        .. note::
          Cross-account permissions don't apply to this action. For more information, see see `Grant Cross-Account Permissions to a Role and a User Name <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name>`__ in the *Amazon Simple Queue Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/UntagQueue>`_
        
        **Request Syntax**
        ::
          response = client.untag_queue(
              QueueUrl='string',
              TagKeys=[
                  'string',
              ]
          )
        :type QueueUrl: string
        :param QueueUrl: **[REQUIRED]**
          The URL of the queue.
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          The list of tags to be removed from the specified queue.
          - *(string) --*
        :returns: None
        """
        pass
