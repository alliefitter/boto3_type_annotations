from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
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

    def create_stream(self, StreamName: str, DeviceName: str = None, MediaType: str = None, KmsKeyId: str = None, DataRetentionInHours: int = None) -> Dict:
        """
        
        When you create a new stream, Kinesis Video Streams assigns it a version number. When you change the stream\'s metadata, Kinesis Video Streams updates the version. 
        
         ``CreateStream`` is an asynchronous operation.
        
        For information about how the service works, see `How it Works <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html>`__ . 
        
        You must have permissions for the ``KinesisVideo:CreateStream`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/CreateStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_stream(
              DeviceName=\'string\',
              StreamName=\'string\',
              MediaType=\'string\',
              KmsKeyId=\'string\',
              DataRetentionInHours=123
          )
        :type DeviceName: string
        :param DeviceName: 
        
          The name of the device that is writing to the stream. 
        
          .. note::
        
            In the current implementation, Kinesis Video Streams does not use this name.
        
        :type StreamName: string
        :param StreamName: **[REQUIRED]** 
        
          A name for the stream that you are creating.
        
          The stream name is an identifier for the stream, and must be unique for each account and region.
        
        :type MediaType: string
        :param MediaType: 
        
          The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see `Media Types <http://www.iana.org/assignments/media-types/media-types.xhtml>`__ . If you choose to specify the ``MediaType`` , see `Naming Requirements <https://tools.ietf.org/html/rfc6838#section-4.2>`__ for guidelines.
        
          To play video on the console, the media must be H.264 encoded, and you need to specify this video type in this parameter as ``video/h264`` . 
        
          This parameter is optional; the default value is ``null`` (or empty in JSON).
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The ID of the AWS Key Management Service (AWS KMS) key that you want Kinesis Video Streams to use to encrypt stream data.
        
          If no key ID is specified, the default, Kinesis Video-managed key (``aws/kinesisvideo`` ) is used.
        
          For more information, see `DescribeKey <http://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters>`__ . 
        
        :type DataRetentionInHours: integer
        :param DataRetentionInHours: 
        
          The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.
        
          The default value is 0, indicating that the stream does not persist data.
        
          When the ``DataRetentionInHours`` value is 0, consumers can still consume the fragments that remain in the service host buffer, which has a retention time limit of 5 minutes and a retention memory limit of 200 MB. Fragments are removed from the buffer when either limit is reached.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StreamARN\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StreamARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the stream.
        
        """
        pass

    def delete_stream(self, StreamARN: str, CurrentVersion: str = None) -> Dict:
        """
        
        This method marks the stream for deletion, and makes the data in the stream inaccessible immediately.
        
        To ensure that you have the latest version of the stream before deleting it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the ``DescribeStream`` API. 
        
        This operation requires permission for the ``KinesisVideo:DeleteStream`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/DeleteStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_stream(
              StreamARN=\'string\',
              CurrentVersion=\'string\'
          )
        :type StreamARN: string
        :param StreamARN: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the stream that you want to delete. 
        
        :type CurrentVersion: string
        :param CurrentVersion: 
        
          Optional: The version of the stream that you want to delete. 
        
          Specify the version as a safeguard to ensure that your are deleting the correct stream. To get the stream version, use the ``DescribeStream`` API.
        
          If not specified, only the ``CreationTime`` is checked before deleting the stream.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_stream(self, StreamName: str = None, StreamARN: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/DescribeStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stream(
              StreamName=\'string\',
              StreamARN=\'string\'
          )
        :type StreamName: string
        :param StreamName: 
        
          The name of the stream.
        
        :type StreamARN: string
        :param StreamARN: 
        
          The Amazon Resource Name (ARN) of the stream.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StreamInfo\': {
                    \'DeviceName\': \'string\',
                    \'StreamName\': \'string\',
                    \'StreamARN\': \'string\',
                    \'MediaType\': \'string\',
                    \'KmsKeyId\': \'string\',
                    \'Version\': \'string\',
                    \'Status\': \'CREATING\'|\'ACTIVE\'|\'UPDATING\'|\'DELETING\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'DataRetentionInHours\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StreamInfo** *(dict) --* 
        
              An object that describes the stream.
        
              - **DeviceName** *(string) --* 
        
                The name of the device that is associated with the stream.
        
              - **StreamName** *(string) --* 
        
                The name of the stream.
        
              - **StreamARN** *(string) --* 
        
                The Amazon Resource Name (ARN) of the stream.
        
              - **MediaType** *(string) --* 
        
                The ``MediaType`` of the stream. 
        
              - **KmsKeyId** *(string) --* 
        
                The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to encrypt data on the stream.
        
              - **Version** *(string) --* 
        
                The version of the stream.
        
              - **Status** *(string) --* 
        
                The status of the stream.
        
              - **CreationTime** *(datetime) --* 
        
                A time stamp that indicates when the stream was created.
        
              - **DataRetentionInHours** *(integer) --* 
        
                How long the stream retains data, in hours.
        
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

    def get_data_endpoint(self, APIName: str, StreamName: str = None, StreamARN: str = None) -> Dict:
        """
        
        .. note::
        
          The returned endpoint does not have the API name appended. The client needs to add the API name to the returned endpoint.
        
        In the request, specify the stream either by ``StreamName`` or ``StreamARN`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/GetDataEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_data_endpoint(
              StreamName=\'string\',
              StreamARN=\'string\',
              APIName=\'PUT_MEDIA\'|\'GET_MEDIA\'|\'LIST_FRAGMENTS\'|\'GET_MEDIA_FOR_FRAGMENT_LIST\'|\'GET_HLS_STREAMING_SESSION_URL\'
          )
        :type StreamName: string
        :param StreamName: 
        
          The name of the stream that you want to get the endpoint for. You must specify either this parameter or a ``StreamARN`` in the request.
        
        :type StreamARN: string
        :param StreamARN: 
        
          The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for. You must specify either this parameter or a ``StreamName`` in the request. 
        
        :type APIName: string
        :param APIName: **[REQUIRED]** 
        
          The name of the API action for which to get an endpoint.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DataEndpoint\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DataEndpoint** *(string) --* 
        
              The endpoint value. To read data from the stream or to write data to it, specify this endpoint in your application.
        
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

    def list_streams(self, MaxResults: int = None, NextToken: str = None, StreamNameCondition: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/ListStreams>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_streams(
              MaxResults=123,
              NextToken=\'string\',
              StreamNameCondition={
                  \'ComparisonOperator\': \'BEGINS_WITH\',
                  \'ComparisonValue\': \'string\'
              }
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of streams to return in the response. The default is 10,000.
        
        :type NextToken: string
        :param NextToken: 
        
          If you specify this parameter, when the result of a ``ListStreams`` operation is truncated, the call returns the ``NextToken`` in the response. To get another batch of streams, provide this token in your next request.
        
        :type StreamNameCondition: dict
        :param StreamNameCondition: 
        
          Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only the prefix of a stream name as a condition. 
        
          - **ComparisonOperator** *(string) --* 
        
            A comparison operator. Currently, you can specify only the ``BEGINS_WITH`` operator, which finds streams whose names start with a given prefix.
        
          - **ComparisonValue** *(string) --* 
        
            A value to compare.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StreamInfoList\': [
                    {
                        \'DeviceName\': \'string\',
                        \'StreamName\': \'string\',
                        \'StreamARN\': \'string\',
                        \'MediaType\': \'string\',
                        \'KmsKeyId\': \'string\',
                        \'Version\': \'string\',
                        \'Status\': \'CREATING\'|\'ACTIVE\'|\'UPDATING\'|\'DELETING\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'DataRetentionInHours\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StreamInfoList** *(list) --* 
        
              An array of ``StreamInfo`` objects.
        
              - *(dict) --* 
        
                An object describing a Kinesis video stream.
        
                - **DeviceName** *(string) --* 
        
                  The name of the device that is associated with the stream.
        
                - **StreamName** *(string) --* 
        
                  The name of the stream.
        
                - **StreamARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the stream.
        
                - **MediaType** *(string) --* 
        
                  The ``MediaType`` of the stream. 
        
                - **KmsKeyId** *(string) --* 
        
                  The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to encrypt data on the stream.
        
                - **Version** *(string) --* 
        
                  The version of the stream.
        
                - **Status** *(string) --* 
        
                  The status of the stream.
        
                - **CreationTime** *(datetime) --* 
        
                  A time stamp that indicates when the stream was created.
        
                - **DataRetentionInHours** *(integer) --* 
        
                  How long the stream retains data, in hours.
        
            - **NextToken** *(string) --* 
        
              If the response is truncated, the call returns this element with a token. To get the next batch of streams, use this token in your next request. 
        
        """
        pass

    def list_tags_for_stream(self, NextToken: str = None, StreamARN: str = None, StreamName: str = None) -> Dict:
        """
        
        In the request, you must specify either the ``StreamName`` or the ``StreamARN`` . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/ListTagsForStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_stream(
              NextToken=\'string\',
              StreamARN=\'string\',
              StreamName=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          If you specify this parameter and the result of a ``ListTagsForStream`` call is truncated, the response includes a token that you can use in the next request to fetch the next batch of tags.
        
        :type StreamARN: string
        :param StreamARN: 
        
          The Amazon Resource Name (ARN) of the stream that you want to list tags for.
        
        :type StreamName: string
        :param StreamName: 
        
          The name of the stream that you want to list tags for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Tags\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              If you specify this parameter and the result of a ``ListTags`` call is truncated, the response includes a token that you can use in the next request to fetch the next set of tags.
        
            - **Tags** *(dict) --* 
        
              A map of tag keys and values associated with the specified stream.
        
              - *(string) --* 
                
                - *(string) --* 
          
        """
        pass

    def tag_stream(self, Tags: Dict, StreamARN: str = None, StreamName: str = None) -> Dict:
        """
        
        You must provide either the ``StreamName`` or the ``StreamARN`` .
        
        This operation requires permission for the ``KinesisVideo:TagStream`` action.
        
        Kinesis video streams support up to 50 tags.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/TagStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_stream(
              StreamARN=\'string\',
              StreamName=\'string\',
              Tags={
                  \'string\': \'string\'
              }
          )
        :type StreamARN: string
        :param StreamARN: 
        
          The Amazon Resource Name (ARN) of the resource that you want to add the tag or tags to.
        
        :type StreamName: string
        :param StreamName: 
        
          The name of the stream that you want to add the tag or tags to.
        
        :type Tags: dict
        :param Tags: **[REQUIRED]** 
        
          A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def untag_stream(self, TagKeyList: List, StreamARN: str = None, StreamName: str = None) -> Dict:
        """
        
        In the request, you must provide the ``StreamName`` or ``StreamARN`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/UntagStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_stream(
              StreamARN=\'string\',
              StreamName=\'string\',
              TagKeyList=[
                  \'string\',
              ]
          )
        :type StreamARN: string
        :param StreamARN: 
        
          The Amazon Resource Name (ARN) of the stream that you want to remove tags from.
        
        :type StreamName: string
        :param StreamName: 
        
          The name of the stream that you want to remove tags from.
        
        :type TagKeyList: list
        :param TagKeyList: **[REQUIRED]** 
        
          A list of the keys of the tags that you want to remove.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_data_retention(self, CurrentVersion: str, Operation: str, DataRetentionChangeInHours: int, StreamName: str = None, StreamARN: str = None) -> Dict:
        """
        
        .. note::
        
          The retention period that you specify replaces the current value.
        
        This operation requires permission for the ``KinesisVideo:UpdateDataRetention`` action.
        
        Changing the data retention period affects the data in the stream as follows:
        
        * If the data retention period is increased, existing data is retained for the new retention period. For example, if the data retention period is increased from one hour to seven hours, all existing data is retained for seven hours. 
         
        * If the data retention period is decreased, existing data is retained for the new retention period. For example, if the data retention period is decreased from seven hours to one hour, all existing data is retained for one hour, and any data older than one hour is deleted immediately. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/UpdateDataRetention>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_data_retention(
              StreamName=\'string\',
              StreamARN=\'string\',
              CurrentVersion=\'string\',
              Operation=\'INCREASE_DATA_RETENTION\'|\'DECREASE_DATA_RETENTION\',
              DataRetentionChangeInHours=123
          )
        :type StreamName: string
        :param StreamName: 
        
          The name of the stream whose retention period you want to change.
        
        :type StreamARN: string
        :param StreamARN: 
        
          The Amazon Resource Name (ARN) of the stream whose retention period you want to change.
        
        :type CurrentVersion: string
        :param CurrentVersion: **[REQUIRED]** 
        
          The version of the stream whose retention period you want to change. To get the version, call either the ``DescribeStream`` or the ``ListStreams`` API.
        
        :type Operation: string
        :param Operation: **[REQUIRED]** 
        
          Indicates whether you want to increase or decrease the retention period.
        
        :type DataRetentionChangeInHours: integer
        :param DataRetentionChangeInHours: **[REQUIRED]** 
        
          The retention period, in hours. The value you specify replaces the current value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_stream(self, CurrentVersion: str, StreamName: str = None, StreamARN: str = None, DeviceName: str = None, MediaType: str = None) -> Dict:
        """
        
        You must provide the stream name or the Amazon Resource Name (ARN) of the stream.
        
        To make sure that you have the latest version of the stream before updating it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the ``DescribeStream`` API. 
        
         ``UpdateStream`` is an asynchronous operation, and takes time to complete.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/UpdateStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_stream(
              StreamName=\'string\',
              StreamARN=\'string\',
              CurrentVersion=\'string\',
              DeviceName=\'string\',
              MediaType=\'string\'
          )
        :type StreamName: string
        :param StreamName: 
        
          The name of the stream whose metadata you want to update.
        
          The stream name is an identifier for the stream, and must be unique for each account and region.
        
        :type StreamARN: string
        :param StreamARN: 
        
          The ARN of the stream whose metadata you want to update.
        
        :type CurrentVersion: string
        :param CurrentVersion: **[REQUIRED]** 
        
          The version of the stream whose metadata you want to update.
        
        :type DeviceName: string
        :param DeviceName: 
        
          The name of the device that is writing to the stream. 
        
          .. note::
        
            In the current implementation, Kinesis Video Streams does not use this name. 
        
        :type MediaType: string
        :param MediaType: 
        
          The stream\'s media type. Use ``MediaType`` to specify the type of content that the stream contains to the consumers of the stream. For more information about media types, see `Media Types <http://www.iana.org/assignments/media-types/media-types.xhtml>`__ . If you choose to specify the ``MediaType`` , see `Naming Requirements <https://tools.ietf.org/html/rfc6838#section-4.2>`__ .
        
          To play video on the console, you must specify the correct video type. For example, if the video in the stream is H.264, specify ``video/h264`` as the ``MediaType`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
