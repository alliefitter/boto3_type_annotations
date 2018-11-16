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

    def create_vocabulary(self, VocabularyName: str, LanguageCode: str, Phrases: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/CreateVocabulary>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_vocabulary(
              VocabularyName=\'string\',
              LanguageCode=\'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
              Phrases=[
                  \'string\',
              ]
          )
        :type VocabularyName: string
        :param VocabularyName: **[REQUIRED]** 
        
          The name of the vocabulary. The name must be unique within an AWS account. The name is case-sensitive.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language code of the vocabulary entries.
        
        :type Phrases: list
        :param Phrases: **[REQUIRED]** 
        
          An array of strings that contains the vocabulary entries. 
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'VocabularyName\': \'string\',
                \'LanguageCode\': \'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
                \'VocabularyState\': \'PENDING\'|\'READY\'|\'FAILED\',
                \'LastModifiedTime\': datetime(2015, 1, 1),
                \'FailureReason\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **VocabularyName** *(string) --* 
        
              The name of the vocabulary.
        
            - **LanguageCode** *(string) --* 
        
              The language code of the vocabulary entries.
        
            - **VocabularyState** *(string) --* 
        
              The processing state of the vocabulary. When the ``VocabularyState`` field contains ``READY`` the vocabulary is ready to be used in a ``StartTranscriptionJob`` request.
        
            - **LastModifiedTime** *(datetime) --* 
        
              The date and time that the vocabulary was created.
        
            - **FailureReason** *(string) --* 
        
              If the ``VocabularyState`` field is ``FAILED`` , this field contains information about why the job failed.
        
        """
        pass

    def delete_transcription_job(self, TranscriptionJobName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/DeleteTranscriptionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_transcription_job(
              TranscriptionJobName=\'string\'
          )
        :type TranscriptionJobName: string
        :param TranscriptionJobName: **[REQUIRED]** 
        
          The name of the transcription job to be deleted.
        
        :returns: None
        """
        pass

    def delete_vocabulary(self, VocabularyName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/DeleteVocabulary>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_vocabulary(
              VocabularyName=\'string\'
          )
        :type VocabularyName: string
        :param VocabularyName: **[REQUIRED]** 
        
          The name of the vocabulary to delete. 
        
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

    def get_transcription_job(self, TranscriptionJobName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/GetTranscriptionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_transcription_job(
              TranscriptionJobName=\'string\'
          )
        :type TranscriptionJobName: string
        :param TranscriptionJobName: **[REQUIRED]** 
        
          The name of the job.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TranscriptionJob\': {
                    \'TranscriptionJobName\': \'string\',
                    \'TranscriptionJobStatus\': \'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                    \'LanguageCode\': \'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
                    \'MediaSampleRateHertz\': 123,
                    \'MediaFormat\': \'mp3\'|\'mp4\'|\'wav\'|\'flac\',
                    \'Media\': {
                        \'MediaFileUri\': \'string\'
                    },
                    \'Transcript\': {
                        \'TranscriptFileUri\': \'string\'
                    },
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'CompletionTime\': datetime(2015, 1, 1),
                    \'FailureReason\': \'string\',
                    \'Settings\': {
                        \'VocabularyName\': \'string\',
                        \'ShowSpeakerLabels\': True|False,
                        \'MaxSpeakerLabels\': 123,
                        \'ChannelIdentification\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TranscriptionJob** *(dict) --* 
        
              An object that contains the results of the transcription job.
        
              - **TranscriptionJobName** *(string) --* 
        
                The name of the transcription job.
        
              - **TranscriptionJobStatus** *(string) --* 
        
                The status of the transcription job.
        
              - **LanguageCode** *(string) --* 
        
                The language code for the input speech.
        
              - **MediaSampleRateHertz** *(integer) --* 
        
                The sample rate, in Hertz, of the audio track in the input media file. 
        
              - **MediaFormat** *(string) --* 
        
                The format of the input media file.
        
              - **Media** *(dict) --* 
        
                An object that describes the input media for the transcription job.
        
                - **MediaFileUri** *(string) --* 
        
                  The S3 location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:
        
                   ``https://<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``  
        
                  For example:
        
                   ``https://s3-us-east-1.amazonaws.com/examplebucket/example.mp4``  
        
                   ``https://s3-us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``  
        
                  For more information about S3 object names, see `Object Keys <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the *Amazon S3 Developer Guide* .
        
              - **Transcript** *(dict) --* 
        
                An object that describes the output of the transcription job.
        
                - **TranscriptFileUri** *(string) --* 
        
                  The location where the transcription is stored.
        
                  Use this URI to access the transcription. If you specified an S3 bucket in the ``OutputBucketName`` field when you created the job, this is the URI of that bucket. If you chose to store the transcription in Amazon Transcribe, this is a shareable URL that provides secure access to that location.
        
              - **CreationTime** *(datetime) --* 
        
                A timestamp that shows when the job was created.
        
              - **CompletionTime** *(datetime) --* 
        
                A timestamp that shows when the job was completed.
        
              - **FailureReason** *(string) --* 
        
                If the ``TranscriptionJobStatus`` field is ``FAILED`` , this field contains information about why the job failed.
        
              - **Settings** *(dict) --* 
        
                Optional settings for the transcription job. Use these settings to turn on speaker recognition, to set the maximum number of speakers that should be identified and to specify a custom vocabulary to use when processing the transcription job.
        
                - **VocabularyName** *(string) --* 
        
                  The name of a vocabulary to use when processing the transcription job.
        
                - **ShowSpeakerLabels** *(boolean) --* 
        
                  Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recognition labels individual speakers in the audio file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum number of speaker labels ``MaxSpeakerLabels`` field.
        
                  You can\'t set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same request. If you set both, your request returns a ``BadRequestException`` .
        
                - **MaxSpeakerLabels** *(integer) --* 
        
                  The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers will be identified as a single speaker. If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels`` field to true.
        
                - **ChannelIdentification** *(boolean) --* 
        
                  Instructs Amazon Transcribe to process each audio channel separately and then merge the transcription output of each channel into a single transcription. 
        
                  Amazon Transcribe also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of the item including the confidence that Amazon Transcribe has in the transcription.
        
                  You can\'t set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same request. If you set both, your request returns a ``BadRequestException`` .
        
        """
        pass

    def get_vocabulary(self, VocabularyName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/GetVocabulary>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_vocabulary(
              VocabularyName=\'string\'
          )
        :type VocabularyName: string
        :param VocabularyName: **[REQUIRED]** 
        
          The name of the vocabulary to return information about. The name is case-sensitive.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'VocabularyName\': \'string\',
                \'LanguageCode\': \'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
                \'VocabularyState\': \'PENDING\'|\'READY\'|\'FAILED\',
                \'LastModifiedTime\': datetime(2015, 1, 1),
                \'FailureReason\': \'string\',
                \'DownloadUri\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **VocabularyName** *(string) --* 
        
              The name of the vocabulary to return.
        
            - **LanguageCode** *(string) --* 
        
              The language code of the vocabulary entries.
        
            - **VocabularyState** *(string) --* 
        
              The processing state of the vocabulary.
        
            - **LastModifiedTime** *(datetime) --* 
        
              The date and time that the vocabulary was last modified.
        
            - **FailureReason** *(string) --* 
        
              If the ``VocabularyState`` field is ``FAILED`` , this field contains information about why the job failed.
        
            - **DownloadUri** *(string) --* 
        
              The S3 location where the vocabulary is stored. Use this URI to get the contents of the vocabulary. The URI is available for a limited time.
        
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

    def list_transcription_jobs(self, Status: str = None, JobNameContains: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/ListTranscriptionJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_transcription_jobs(
              Status=\'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
              JobNameContains=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type Status: string
        :param Status: 
        
          When specified, returns only transcription jobs with the specified status.
        
        :type JobNameContains: string
        :param JobNameContains: 
        
          When specified, the jobs returned in the list are limited to jobs whose name contains the specified string.
        
        :type NextToken: string
        :param NextToken: 
        
          If the result of the previous request to ``ListTranscriptionJobs`` was truncated, include the ``NextToken`` to fetch the next set of jobs.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of jobs to return in the response. If there are fewer results in the list, this response contains only the actual results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': \'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                \'NextToken\': \'string\',
                \'TranscriptionJobSummaries\': [
                    {
                        \'TranscriptionJobName\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'CompletionTime\': datetime(2015, 1, 1),
                        \'LanguageCode\': \'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
                        \'TranscriptionJobStatus\': \'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                        \'FailureReason\': \'string\',
                        \'OutputLocationType\': \'CUSTOMER_BUCKET\'|\'SERVICE_BUCKET\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Status** *(string) --* 
        
              The requested status of the jobs returned.
        
            - **NextToken** *(string) --* 
        
              The ``ListTranscriptionJobs`` operation returns a page of jobs at a time. The maximum size of the page is set by the ``MaxResults`` parameter. If there are more jobs in the list than the page size, Amazon Transcribe returns the ``NextPage`` token. Include the token in the next request to the ``ListTranscriptionJobs`` operation to return in the next page of jobs.
        
            - **TranscriptionJobSummaries** *(list) --* 
        
              A list of objects containing summary information for a transcription job.
        
              - *(dict) --* 
        
                Provides a summary of information about a transcription job. Note that en-AU, en-UK, and fr-CA languages are in preview and are only available to whitelisted customers.
        
                - **TranscriptionJobName** *(string) --* 
        
                  The name of the transcription job.
        
                - **CreationTime** *(datetime) --* 
        
                  A timestamp that shows when the job was created.
        
                - **CompletionTime** *(datetime) --* 
        
                  A timestamp that shows when the job was completed.
        
                - **LanguageCode** *(string) --* 
        
                  The language code for the input speech.
        
                - **TranscriptionJobStatus** *(string) --* 
        
                  The status of the transcription job. When the status is ``COMPLETED`` , use the ``GetTranscriptionJob`` operation to get the results of the transcription.
        
                - **FailureReason** *(string) --* 
        
                  If the ``TranscriptionJobStatus`` field is ``FAILED`` , a description of the error.
        
                - **OutputLocationType** *(string) --* 
        
                  Indicates the location of the output of the transcription job.
        
                  If the value is ``CUSTOMER_BUCKET`` then the location is the S3 bucket specified in the ``outputBucketName`` field when the transcription job was started with the ``StartTranscriptionJob`` operation.
        
                  If the value is ``SERVICE_BUCKET`` then the output is stored by Amazon Transcribe and can be retrieved using the URI in the ``GetTranscriptionJob`` response\'s ``TranscriptFileUri`` field.
        
        """
        pass

    def list_vocabularies(self, NextToken: str = None, MaxResults: int = None, StateEquals: str = None, NameContains: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/ListVocabularies>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_vocabularies(
              NextToken=\'string\',
              MaxResults=123,
              StateEquals=\'PENDING\'|\'READY\'|\'FAILED\',
              NameContains=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          If the result of the previous request to ``ListVocabularies`` was truncated, include the ``NextToken`` to fetch the next set of jobs.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of vocabularies to return in the response. If there are fewer results in the list, this response contains only the actual results.
        
        :type StateEquals: string
        :param StateEquals: 
        
          When specified, only returns vocabularies with the ``VocabularyState`` field equal to the specified state.
        
        :type NameContains: string
        :param NameContains: 
        
          When specified, the vocabularies returned in the list are limited to vocabularies whose name contains the specified string. The search is case-insensitive, ``ListVocabularies`` will return both \"vocabularyname\" and \"VocabularyName\" in the response list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': \'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                \'NextToken\': \'string\',
                \'Vocabularies\': [
                    {
                        \'VocabularyName\': \'string\',
                        \'LanguageCode\': \'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
                        \'LastModifiedTime\': datetime(2015, 1, 1),
                        \'VocabularyState\': \'PENDING\'|\'READY\'|\'FAILED\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Status** *(string) --* 
        
              The requested vocabulary state.
        
            - **NextToken** *(string) --* 
        
              The ``ListVocabularies`` operation returns a page of vocabularies at a time. The maximum size of the page is set by the ``MaxResults`` parameter. If there are more jobs in the list than the page size, Amazon Transcribe returns the ``NextPage`` token. Include the token in the next request to the ``ListVocabularies`` operation to return in the next page of jobs.
        
            - **Vocabularies** *(list) --* 
        
              A list of objects that describe the vocabularies that match the search criteria in the request.
        
              - *(dict) --* 
        
                Provides information about a custom vocabulary. Note that vocabularies for en-AU, en-UK, and fr-CA languages that are in preview are not available. In the console, the vocabulary section will be greyed-out and SDK will return error message.
        
                - **VocabularyName** *(string) --* 
        
                  The name of the vocabulary.
        
                - **LanguageCode** *(string) --* 
        
                  The language code of the vocabulary entries.
        
                - **LastModifiedTime** *(datetime) --* 
        
                  The date and time that the vocabulary was last modified.
        
                - **VocabularyState** *(string) --* 
        
                  The processing state of the vocabulary. If the state is ``READY`` you can use the vocabulary in a ``StartTranscriptionJob`` request.
        
        """
        pass

    def start_transcription_job(self, TranscriptionJobName: str, LanguageCode: str, MediaFormat: str, Media: Dict, MediaSampleRateHertz: int = None, OutputBucketName: str = None, Settings: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/StartTranscriptionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_transcription_job(
              TranscriptionJobName=\'string\',
              LanguageCode=\'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
              MediaSampleRateHertz=123,
              MediaFormat=\'mp3\'|\'mp4\'|\'wav\'|\'flac\',
              Media={
                  \'MediaFileUri\': \'string\'
              },
              OutputBucketName=\'string\',
              Settings={
                  \'VocabularyName\': \'string\',
                  \'ShowSpeakerLabels\': True|False,
                  \'MaxSpeakerLabels\': 123,
                  \'ChannelIdentification\': True|False
              }
          )
        :type TranscriptionJobName: string
        :param TranscriptionJobName: **[REQUIRED]** 
        
          The name of the job. You can\'t use the strings \".\" or \"..\" in the job name. The name must be unique within an AWS account.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language code for the language used in the input media file.
        
        :type MediaSampleRateHertz: integer
        :param MediaSampleRateHertz: 
        
          The sample rate, in Hertz, of the audio track in the input media file. 
        
        :type MediaFormat: string
        :param MediaFormat: **[REQUIRED]** 
        
          The format of the input media file.
        
        :type Media: dict
        :param Media: **[REQUIRED]** 
        
          An object that describes the input media for a transcription job.
        
          - **MediaFileUri** *(string) --* 
        
            The S3 location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:
        
             ``https://<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``  
        
            For example:
        
             ``https://s3-us-east-1.amazonaws.com/examplebucket/example.mp4``  
        
             ``https://s3-us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``  
        
            For more information about S3 object names, see `Object Keys <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the *Amazon S3 Developer Guide* .
        
        :type OutputBucketName: string
        :param OutputBucketName: 
        
          The location where the transcription is stored.
        
          If you set the ``OutputBucketName`` , Amazon Transcribe puts the transcription in the specified S3 bucket. When you call the  GetTranscriptionJob operation, the operation returns this location in the ``TranscriptFileUri`` field. The S3 bucket must have permissions that allow Amazon Transcribe to put files in the bucket. For more information, see `Permissions Required for IAM User Roles <https://docs.aws.amazon.com/transcribe/latest/dg/access-control-managing-permissions.html#auth-role-iam-user>`__ .
        
          If you don\'t set the ``OutputBucketName`` , Amazon Transcribe generates a pre-signed URL, a shareable URL that provides secure access to your transcription, and returns it in the ``TranscriptFileUri`` field. Use this URL to download the transcription.
        
        :type Settings: dict
        :param Settings: 
        
          A ``Settings`` object that provides optional settings for a transcription job.
        
          - **VocabularyName** *(string) --* 
        
            The name of a vocabulary to use when processing the transcription job.
        
          - **ShowSpeakerLabels** *(boolean) --* 
        
            Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recognition labels individual speakers in the audio file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum number of speaker labels ``MaxSpeakerLabels`` field.
        
            You can\'t set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same request. If you set both, your request returns a ``BadRequestException`` .
        
          - **MaxSpeakerLabels** *(integer) --* 
        
            The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers will be identified as a single speaker. If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels`` field to true.
        
          - **ChannelIdentification** *(boolean) --* 
        
            Instructs Amazon Transcribe to process each audio channel separately and then merge the transcription output of each channel into a single transcription. 
        
            Amazon Transcribe also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of the item including the confidence that Amazon Transcribe has in the transcription.
        
            You can\'t set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same request. If you set both, your request returns a ``BadRequestException`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TranscriptionJob\': {
                    \'TranscriptionJobName\': \'string\',
                    \'TranscriptionJobStatus\': \'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                    \'LanguageCode\': \'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
                    \'MediaSampleRateHertz\': 123,
                    \'MediaFormat\': \'mp3\'|\'mp4\'|\'wav\'|\'flac\',
                    \'Media\': {
                        \'MediaFileUri\': \'string\'
                    },
                    \'Transcript\': {
                        \'TranscriptFileUri\': \'string\'
                    },
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'CompletionTime\': datetime(2015, 1, 1),
                    \'FailureReason\': \'string\',
                    \'Settings\': {
                        \'VocabularyName\': \'string\',
                        \'ShowSpeakerLabels\': True|False,
                        \'MaxSpeakerLabels\': 123,
                        \'ChannelIdentification\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TranscriptionJob** *(dict) --* 
        
              An object containing details of the asynchronous transcription job.
        
              - **TranscriptionJobName** *(string) --* 
        
                The name of the transcription job.
        
              - **TranscriptionJobStatus** *(string) --* 
        
                The status of the transcription job.
        
              - **LanguageCode** *(string) --* 
        
                The language code for the input speech.
        
              - **MediaSampleRateHertz** *(integer) --* 
        
                The sample rate, in Hertz, of the audio track in the input media file. 
        
              - **MediaFormat** *(string) --* 
        
                The format of the input media file.
        
              - **Media** *(dict) --* 
        
                An object that describes the input media for the transcription job.
        
                - **MediaFileUri** *(string) --* 
        
                  The S3 location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:
        
                   ``https://<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``  
        
                  For example:
        
                   ``https://s3-us-east-1.amazonaws.com/examplebucket/example.mp4``  
        
                   ``https://s3-us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``  
        
                  For more information about S3 object names, see `Object Keys <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the *Amazon S3 Developer Guide* .
        
              - **Transcript** *(dict) --* 
        
                An object that describes the output of the transcription job.
        
                - **TranscriptFileUri** *(string) --* 
        
                  The location where the transcription is stored.
        
                  Use this URI to access the transcription. If you specified an S3 bucket in the ``OutputBucketName`` field when you created the job, this is the URI of that bucket. If you chose to store the transcription in Amazon Transcribe, this is a shareable URL that provides secure access to that location.
        
              - **CreationTime** *(datetime) --* 
        
                A timestamp that shows when the job was created.
        
              - **CompletionTime** *(datetime) --* 
        
                A timestamp that shows when the job was completed.
        
              - **FailureReason** *(string) --* 
        
                If the ``TranscriptionJobStatus`` field is ``FAILED`` , this field contains information about why the job failed.
        
              - **Settings** *(dict) --* 
        
                Optional settings for the transcription job. Use these settings to turn on speaker recognition, to set the maximum number of speakers that should be identified and to specify a custom vocabulary to use when processing the transcription job.
        
                - **VocabularyName** *(string) --* 
        
                  The name of a vocabulary to use when processing the transcription job.
        
                - **ShowSpeakerLabels** *(boolean) --* 
        
                  Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recognition labels individual speakers in the audio file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum number of speaker labels ``MaxSpeakerLabels`` field.
        
                  You can\'t set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same request. If you set both, your request returns a ``BadRequestException`` .
        
                - **MaxSpeakerLabels** *(integer) --* 
        
                  The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers will be identified as a single speaker. If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels`` field to true.
        
                - **ChannelIdentification** *(boolean) --* 
        
                  Instructs Amazon Transcribe to process each audio channel separately and then merge the transcription output of each channel into a single transcription. 
        
                  Amazon Transcribe also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of the item including the confidence that Amazon Transcribe has in the transcription.
        
                  You can\'t set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same request. If you set both, your request returns a ``BadRequestException`` .
        
        """
        pass

    def update_vocabulary(self, VocabularyName: str, LanguageCode: str, Phrases: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/UpdateVocabulary>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_vocabulary(
              VocabularyName=\'string\',
              LanguageCode=\'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
              Phrases=[
                  \'string\',
              ]
          )
        :type VocabularyName: string
        :param VocabularyName: **[REQUIRED]** 
        
          The name of the vocabulary to update. The name is case-sensitive.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language code of the vocabulary entries.
        
        :type Phrases: list
        :param Phrases: **[REQUIRED]** 
        
          An array of strings containing the vocabulary entries.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'VocabularyName\': \'string\',
                \'LanguageCode\': \'en-US\'|\'es-US\'|\'en-AU\'|\'fr-CA\'|\'en-UK\',
                \'LastModifiedTime\': datetime(2015, 1, 1),
                \'VocabularyState\': \'PENDING\'|\'READY\'|\'FAILED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **VocabularyName** *(string) --* 
        
              The name of the vocabulary that was updated.
        
            - **LanguageCode** *(string) --* 
        
              The language code of the vocabulary entries.
        
            - **LastModifiedTime** *(datetime) --* 
        
              The date and time that the vocabulary was updated.
        
            - **VocabularyState** *(string) --* 
        
              The processing state of the vocabulary. When the ``VocabularyState`` field contains ``READY`` the vocabulary is ready to be used in a ``StartTranscriptionJob`` request.
        
        """
        pass
