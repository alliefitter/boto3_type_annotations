from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
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

    def delete_lexicon(self, Name: str) -> Dict:
        """
        
        For more information, see `Managing Lexicons <http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DeleteLexicon>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_lexicon(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the lexicon to delete. Must be an existing lexicon in the region.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_voices(self, LanguageCode: str = None, IncludeAdditionalLanguageCodes: bool = None, NextToken: str = None) -> Dict:
        """
        
        When synthesizing speech ( ``SynthesizeSpeech`` ), you provide the voice ID for the voice you want from the list of voices returned by ``DescribeVoices`` .
        
        For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the ``DescribeVoices`` operation you can provide the user with a list of available voices to select from.
        
        You can optionally specify a language code to filter the available voices. For example, if you specify ``en-US`` , the operation returns a list of all available US English voices. 
        
        This operation requires permissions to perform the ``polly:DescribeVoices`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DescribeVoices>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_voices(
              LanguageCode=\'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\',
              IncludeAdditionalLanguageCodes=True|False,
              NextToken=\'string\'
          )
        :type LanguageCode: string
        :param LanguageCode: 
        
          The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don\'t specify this optional parameter, all available voices are returned. 
        
        :type IncludeAdditionalLanguageCodes: boolean
        :param IncludeAdditionalLanguageCodes: 
        
          Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify ``yes`` but not if you specify ``no`` .
        
        :type NextToken: string
        :param NextToken: 
        
          An opaque pagination token returned from the previous ``DescribeVoices`` operation. If present, this indicates where to continue the listing.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Voices\': [
                    {
                        \'Gender\': \'Female\'|\'Male\',
                        \'Id\': \'Geraint\'|\'Gwyneth\'|\'Mads\'|\'Naja\'|\'Hans\'|\'Marlene\'|\'Nicole\'|\'Russell\'|\'Amy\'|\'Brian\'|\'Emma\'|\'Raveena\'|\'Ivy\'|\'Joanna\'|\'Joey\'|\'Justin\'|\'Kendra\'|\'Kimberly\'|\'Matthew\'|\'Salli\'|\'Conchita\'|\'Enrique\'|\'Miguel\'|\'Penelope\'|\'Chantal\'|\'Celine\'|\'Lea\'|\'Mathieu\'|\'Dora\'|\'Karl\'|\'Carla\'|\'Giorgio\'|\'Mizuki\'|\'Liv\'|\'Lotte\'|\'Ruben\'|\'Ewa\'|\'Jacek\'|\'Jan\'|\'Maja\'|\'Ricardo\'|\'Vitoria\'|\'Cristiano\'|\'Ines\'|\'Carmen\'|\'Maxim\'|\'Tatyana\'|\'Astrid\'|\'Filiz\'|\'Vicki\'|\'Takumi\'|\'Seoyeon\'|\'Aditi\'|\'Zhiyu\'|\'Bianca\'|\'Lucia\'|\'Mia\',
                        \'LanguageCode\': \'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\',
                        \'LanguageName\': \'string\',
                        \'Name\': \'string\',
                        \'AdditionalLanguageCodes\': [
                            \'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Voices** *(list) --* 
        
              A list of voices with their properties.
        
              - *(dict) --* 
        
                Description of the voice.
        
                - **Gender** *(string) --* 
        
                  Gender of the voice.
        
                - **Id** *(string) --* 
        
                  Amazon Polly assigned voice ID. This is the ID that you specify when calling the ``SynthesizeSpeech`` operation.
        
                - **LanguageCode** *(string) --* 
        
                  Language code of the voice.
        
                - **LanguageName** *(string) --* 
        
                  Human readable name of the language in English.
        
                - **Name** *(string) --* 
        
                  Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable voice name that you might display in your application.
        
                - **AdditionalLanguageCodes** *(list) --* 
        
                  Additional codes for languages available for the specified voice in addition to its default language. 
        
                  For example, the default language for Aditi is Indian English (en-IN) because it was first used for that language. Since Aditi is bilingual and fluent in both Indian English and Hindi, this parameter would show the code ``hi-IN`` .
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              The pagination token to use in the next request to continue the listing of voices. ``NextToken`` is returned only if the response is truncated.
        
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

    def get_lexicon(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/GetLexicon>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_lexicon(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Name of the lexicon.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Lexicon\': {
                    \'Content\': \'string\',
                    \'Name\': \'string\'
                },
                \'LexiconAttributes\': {
                    \'Alphabet\': \'string\',
                    \'LanguageCode\': \'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\',
                    \'LastModified\': datetime(2015, 1, 1),
                    \'LexiconArn\': \'string\',
                    \'LexemesCount\': 123,
                    \'Size\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Lexicon** *(dict) --* 
        
              Lexicon object that provides name and the string content of the lexicon. 
        
              - **Content** *(string) --* 
        
                Lexicon content in string format. The content of a lexicon must be in PLS format.
        
              - **Name** *(string) --* 
        
                Name of the lexicon.
        
            - **LexiconAttributes** *(dict) --* 
        
              Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon in bytes.
        
              - **Alphabet** *(string) --* 
        
                Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .
        
              - **LanguageCode** *(string) --* 
        
                Language code that the lexicon applies to. A lexicon with a language code such as \"en\" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.
        
              - **LastModified** *(datetime) --* 
        
                Date lexicon was last modified (a timestamp value).
        
              - **LexiconArn** *(string) --* 
        
                Amazon Resource Name (ARN) of the lexicon.
        
              - **LexemesCount** *(integer) --* 
        
                Number of lexemes in the lexicon.
        
              - **Size** *(integer) --* 
        
                Total size of the lexicon, in characters.
        
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

    def get_speech_synthesis_task(self, TaskId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/GetSpeechSynthesisTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_speech_synthesis_task(
              TaskId=\'string\'
          )
        :type TaskId: string
        :param TaskId: **[REQUIRED]** 
        
          The Amazon Polly generated identifier for a speech synthesis task.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SynthesisTask\': {
                    \'TaskId\': \'string\',
                    \'TaskStatus\': \'scheduled\'|\'inProgress\'|\'completed\'|\'failed\',
                    \'TaskStatusReason\': \'string\',
                    \'OutputUri\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'RequestCharacters\': 123,
                    \'SnsTopicArn\': \'string\',
                    \'LexiconNames\': [
                        \'string\',
                    ],
                    \'OutputFormat\': \'json\'|\'mp3\'|\'ogg_vorbis\'|\'pcm\',
                    \'SampleRate\': \'string\',
                    \'SpeechMarkTypes\': [
                        \'sentence\'|\'ssml\'|\'viseme\'|\'word\',
                    ],
                    \'TextType\': \'ssml\'|\'text\',
                    \'VoiceId\': \'Geraint\'|\'Gwyneth\'|\'Mads\'|\'Naja\'|\'Hans\'|\'Marlene\'|\'Nicole\'|\'Russell\'|\'Amy\'|\'Brian\'|\'Emma\'|\'Raveena\'|\'Ivy\'|\'Joanna\'|\'Joey\'|\'Justin\'|\'Kendra\'|\'Kimberly\'|\'Matthew\'|\'Salli\'|\'Conchita\'|\'Enrique\'|\'Miguel\'|\'Penelope\'|\'Chantal\'|\'Celine\'|\'Lea\'|\'Mathieu\'|\'Dora\'|\'Karl\'|\'Carla\'|\'Giorgio\'|\'Mizuki\'|\'Liv\'|\'Lotte\'|\'Ruben\'|\'Ewa\'|\'Jacek\'|\'Jan\'|\'Maja\'|\'Ricardo\'|\'Vitoria\'|\'Cristiano\'|\'Ines\'|\'Carmen\'|\'Maxim\'|\'Tatyana\'|\'Astrid\'|\'Filiz\'|\'Vicki\'|\'Takumi\'|\'Seoyeon\'|\'Aditi\'|\'Zhiyu\'|\'Bianca\'|\'Lucia\'|\'Mia\',
                    \'LanguageCode\': \'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SynthesisTask** *(dict) --* 
        
              SynthesisTask object that provides information from the requested task, including output format, creation time, task status, and so on.
        
              - **TaskId** *(string) --* 
        
                The Amazon Polly generated identifier for a speech synthesis task.
        
              - **TaskStatus** *(string) --* 
        
                Current status of the individual speech synthesis task.
        
              - **TaskStatusReason** *(string) --* 
        
                Reason for the current status of a specific speech synthesis task, including errors if the task has failed.
        
              - **OutputUri** *(string) --* 
        
                Pathway for the output speech file.
        
              - **CreationTime** *(datetime) --* 
        
                Timestamp for the time the synthesis task was started.
        
              - **RequestCharacters** *(integer) --* 
        
                Number of billable characters synthesized.
        
              - **SnsTopicArn** *(string) --* 
        
                ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.
        
              - **LexiconNames** *(list) --* 
        
                List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. 
        
                - *(string) --* 
            
              - **OutputFormat** *(string) --* 
        
                The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json. 
        
              - **SampleRate** *(string) --* 
        
                The audio frequency specified in Hz.
        
                The valid values for mp3 and ogg_vorbis are \"8000\", \"16000\", and \"22050\". The default value is \"22050\".
        
                Valid values for pcm are \"8000\" and \"16000\" The default value is \"16000\". 
        
              - **SpeechMarkTypes** *(list) --* 
        
                The type of speech marks returned for the input text.
        
                - *(string) --* 
            
              - **TextType** *(string) --* 
        
                Specifies whether the input text is plain text or SSML. The default value is plain text. 
        
              - **VoiceId** *(string) --* 
        
                Voice ID to use for the synthesis. 
        
              - **LanguageCode** *(string) --* 
        
                Optional language code for a synthesis task. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). 
        
                If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the `DescribeVoices <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.
        
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

    def list_lexicons(self, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/ListLexicons>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_lexicons(
              NextToken=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          An opaque pagination token returned from previous ``ListLexicons`` operation. If present, indicates where to continue the list of lexicons.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Lexicons\': [
                    {
                        \'Name\': \'string\',
                        \'Attributes\': {
                            \'Alphabet\': \'string\',
                            \'LanguageCode\': \'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\',
                            \'LastModified\': datetime(2015, 1, 1),
                            \'LexiconArn\': \'string\',
                            \'LexemesCount\': 123,
                            \'Size\': 123
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Lexicons** *(list) --* 
        
              A list of lexicon names and attributes.
        
              - *(dict) --* 
        
                Describes the content of the lexicon.
        
                - **Name** *(string) --* 
        
                  Name of the lexicon.
        
                - **Attributes** *(dict) --* 
        
                  Provides lexicon metadata.
        
                  - **Alphabet** *(string) --* 
        
                    Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .
        
                  - **LanguageCode** *(string) --* 
        
                    Language code that the lexicon applies to. A lexicon with a language code such as \"en\" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.
        
                  - **LastModified** *(datetime) --* 
        
                    Date lexicon was last modified (a timestamp value).
        
                  - **LexiconArn** *(string) --* 
        
                    Amazon Resource Name (ARN) of the lexicon.
        
                  - **LexemesCount** *(integer) --* 
        
                    Number of lexemes in the lexicon.
        
                  - **Size** *(integer) --* 
        
                    Total size of the lexicon, in characters.
        
            - **NextToken** *(string) --* 
        
              The pagination token to use in the next request to continue the listing of lexicons. ``NextToken`` is returned only if the response is truncated.
        
        """
        pass

    def list_speech_synthesis_tasks(self, MaxResults: int = None, NextToken: str = None, Status: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/ListSpeechSynthesisTasks>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_speech_synthesis_tasks(
              MaxResults=123,
              NextToken=\'string\',
              Status=\'scheduled\'|\'inProgress\'|\'completed\'|\'failed\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          Maximum number of speech synthesis tasks returned in a List operation.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use in the next request to continue the listing of speech synthesis tasks. 
        
        :type Status: string
        :param Status: 
        
          Status of the speech synthesis tasks returned in a List operation
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'SynthesisTasks\': [
                    {
                        \'TaskId\': \'string\',
                        \'TaskStatus\': \'scheduled\'|\'inProgress\'|\'completed\'|\'failed\',
                        \'TaskStatusReason\': \'string\',
                        \'OutputUri\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'RequestCharacters\': 123,
                        \'SnsTopicArn\': \'string\',
                        \'LexiconNames\': [
                            \'string\',
                        ],
                        \'OutputFormat\': \'json\'|\'mp3\'|\'ogg_vorbis\'|\'pcm\',
                        \'SampleRate\': \'string\',
                        \'SpeechMarkTypes\': [
                            \'sentence\'|\'ssml\'|\'viseme\'|\'word\',
                        ],
                        \'TextType\': \'ssml\'|\'text\',
                        \'VoiceId\': \'Geraint\'|\'Gwyneth\'|\'Mads\'|\'Naja\'|\'Hans\'|\'Marlene\'|\'Nicole\'|\'Russell\'|\'Amy\'|\'Brian\'|\'Emma\'|\'Raveena\'|\'Ivy\'|\'Joanna\'|\'Joey\'|\'Justin\'|\'Kendra\'|\'Kimberly\'|\'Matthew\'|\'Salli\'|\'Conchita\'|\'Enrique\'|\'Miguel\'|\'Penelope\'|\'Chantal\'|\'Celine\'|\'Lea\'|\'Mathieu\'|\'Dora\'|\'Karl\'|\'Carla\'|\'Giorgio\'|\'Mizuki\'|\'Liv\'|\'Lotte\'|\'Ruben\'|\'Ewa\'|\'Jacek\'|\'Jan\'|\'Maja\'|\'Ricardo\'|\'Vitoria\'|\'Cristiano\'|\'Ines\'|\'Carmen\'|\'Maxim\'|\'Tatyana\'|\'Astrid\'|\'Filiz\'|\'Vicki\'|\'Takumi\'|\'Seoyeon\'|\'Aditi\'|\'Zhiyu\'|\'Bianca\'|\'Lucia\'|\'Mia\',
                        \'LanguageCode\': \'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              An opaque pagination token returned from the previous List operation in this request. If present, this indicates where to continue the listing.
        
            - **SynthesisTasks** *(list) --* 
        
              List of SynthesisTask objects that provides information from the specified task in the list request, including output format, creation time, task status, and so on.
        
              - *(dict) --* 
        
                SynthesisTask object that provides information about a speech synthesis task.
        
                - **TaskId** *(string) --* 
        
                  The Amazon Polly generated identifier for a speech synthesis task.
        
                - **TaskStatus** *(string) --* 
        
                  Current status of the individual speech synthesis task.
        
                - **TaskStatusReason** *(string) --* 
        
                  Reason for the current status of a specific speech synthesis task, including errors if the task has failed.
        
                - **OutputUri** *(string) --* 
        
                  Pathway for the output speech file.
        
                - **CreationTime** *(datetime) --* 
        
                  Timestamp for the time the synthesis task was started.
        
                - **RequestCharacters** *(integer) --* 
        
                  Number of billable characters synthesized.
        
                - **SnsTopicArn** *(string) --* 
        
                  ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.
        
                - **LexiconNames** *(list) --* 
        
                  List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. 
        
                  - *(string) --* 
              
                - **OutputFormat** *(string) --* 
        
                  The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json. 
        
                - **SampleRate** *(string) --* 
        
                  The audio frequency specified in Hz.
        
                  The valid values for mp3 and ogg_vorbis are \"8000\", \"16000\", and \"22050\". The default value is \"22050\".
        
                  Valid values for pcm are \"8000\" and \"16000\" The default value is \"16000\". 
        
                - **SpeechMarkTypes** *(list) --* 
        
                  The type of speech marks returned for the input text.
        
                  - *(string) --* 
              
                - **TextType** *(string) --* 
        
                  Specifies whether the input text is plain text or SSML. The default value is plain text. 
        
                - **VoiceId** *(string) --* 
        
                  Voice ID to use for the synthesis. 
        
                - **LanguageCode** *(string) --* 
        
                  Optional language code for a synthesis task. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). 
        
                  If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the `DescribeVoices <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.
        
        """
        pass

    def put_lexicon(self, Name: str, Content: str) -> Dict:
        """
        
        For more information, see `Managing Lexicons <http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/PutLexicon>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_lexicon(
              Name=\'string\',
              Content=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. 
        
        :type Content: string
        :param Content: **[REQUIRED]** 
        
          Content of the PLS lexicon as string data.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def start_speech_synthesis_task(self, OutputFormat: str, OutputS3BucketName: str, Text: str, VoiceId: str, LexiconNames: List = None, OutputS3KeyPrefix: str = None, SampleRate: str = None, SnsTopicArn: str = None, SpeechMarkTypes: List = None, TextType: str = None, LanguageCode: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/StartSpeechSynthesisTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_speech_synthesis_task(
              LexiconNames=[
                  \'string\',
              ],
              OutputFormat=\'json\'|\'mp3\'|\'ogg_vorbis\'|\'pcm\',
              OutputS3BucketName=\'string\',
              OutputS3KeyPrefix=\'string\',
              SampleRate=\'string\',
              SnsTopicArn=\'string\',
              SpeechMarkTypes=[
                  \'sentence\'|\'ssml\'|\'viseme\'|\'word\',
              ],
              Text=\'string\',
              TextType=\'ssml\'|\'text\',
              VoiceId=\'Geraint\'|\'Gwyneth\'|\'Mads\'|\'Naja\'|\'Hans\'|\'Marlene\'|\'Nicole\'|\'Russell\'|\'Amy\'|\'Brian\'|\'Emma\'|\'Raveena\'|\'Ivy\'|\'Joanna\'|\'Joey\'|\'Justin\'|\'Kendra\'|\'Kimberly\'|\'Matthew\'|\'Salli\'|\'Conchita\'|\'Enrique\'|\'Miguel\'|\'Penelope\'|\'Chantal\'|\'Celine\'|\'Lea\'|\'Mathieu\'|\'Dora\'|\'Karl\'|\'Carla\'|\'Giorgio\'|\'Mizuki\'|\'Liv\'|\'Lotte\'|\'Ruben\'|\'Ewa\'|\'Jacek\'|\'Jan\'|\'Maja\'|\'Ricardo\'|\'Vitoria\'|\'Cristiano\'|\'Ines\'|\'Carmen\'|\'Maxim\'|\'Tatyana\'|\'Astrid\'|\'Filiz\'|\'Vicki\'|\'Takumi\'|\'Seoyeon\'|\'Aditi\'|\'Zhiyu\'|\'Bianca\'|\'Lucia\'|\'Mia\',
              LanguageCode=\'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\'
          )
        :type LexiconNames: list
        :param LexiconNames: 
        
          List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. 
        
          - *(string) --* 
        
        :type OutputFormat: string
        :param OutputFormat: **[REQUIRED]** 
        
          The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json. 
        
        :type OutputS3BucketName: string
        :param OutputS3BucketName: **[REQUIRED]** 
        
          Amazon S3 bucket name to which the output file will be saved.
        
        :type OutputS3KeyPrefix: string
        :param OutputS3KeyPrefix: 
        
          The Amazon S3 key prefix for the output speech file.
        
        :type SampleRate: string
        :param SampleRate: 
        
          The audio frequency specified in Hz.
        
          The valid values for mp3 and ogg_vorbis are \"8000\", \"16000\", and \"22050\". The default value is \"22050\".
        
          Valid values for pcm are \"8000\" and \"16000\" The default value is \"16000\". 
        
        :type SnsTopicArn: string
        :param SnsTopicArn: 
        
          ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.
        
        :type SpeechMarkTypes: list
        :param SpeechMarkTypes: 
        
          The type of speech marks returned for the input text.
        
          - *(string) --* 
        
        :type Text: string
        :param Text: **[REQUIRED]** 
        
          The input text to synthesize. If you specify ssml as the TextType, follow the SSML format for the input text. 
        
        :type TextType: string
        :param TextType: 
        
          Specifies whether the input text is plain text or SSML. The default value is plain text. 
        
        :type VoiceId: string
        :param VoiceId: **[REQUIRED]** 
        
          Voice ID to use for the synthesis. 
        
        :type LanguageCode: string
        :param LanguageCode: 
        
          Optional language code for the Speech Synthesis request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). 
        
          If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the `DescribeVoices <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SynthesisTask\': {
                    \'TaskId\': \'string\',
                    \'TaskStatus\': \'scheduled\'|\'inProgress\'|\'completed\'|\'failed\',
                    \'TaskStatusReason\': \'string\',
                    \'OutputUri\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'RequestCharacters\': 123,
                    \'SnsTopicArn\': \'string\',
                    \'LexiconNames\': [
                        \'string\',
                    ],
                    \'OutputFormat\': \'json\'|\'mp3\'|\'ogg_vorbis\'|\'pcm\',
                    \'SampleRate\': \'string\',
                    \'SpeechMarkTypes\': [
                        \'sentence\'|\'ssml\'|\'viseme\'|\'word\',
                    ],
                    \'TextType\': \'ssml\'|\'text\',
                    \'VoiceId\': \'Geraint\'|\'Gwyneth\'|\'Mads\'|\'Naja\'|\'Hans\'|\'Marlene\'|\'Nicole\'|\'Russell\'|\'Amy\'|\'Brian\'|\'Emma\'|\'Raveena\'|\'Ivy\'|\'Joanna\'|\'Joey\'|\'Justin\'|\'Kendra\'|\'Kimberly\'|\'Matthew\'|\'Salli\'|\'Conchita\'|\'Enrique\'|\'Miguel\'|\'Penelope\'|\'Chantal\'|\'Celine\'|\'Lea\'|\'Mathieu\'|\'Dora\'|\'Karl\'|\'Carla\'|\'Giorgio\'|\'Mizuki\'|\'Liv\'|\'Lotte\'|\'Ruben\'|\'Ewa\'|\'Jacek\'|\'Jan\'|\'Maja\'|\'Ricardo\'|\'Vitoria\'|\'Cristiano\'|\'Ines\'|\'Carmen\'|\'Maxim\'|\'Tatyana\'|\'Astrid\'|\'Filiz\'|\'Vicki\'|\'Takumi\'|\'Seoyeon\'|\'Aditi\'|\'Zhiyu\'|\'Bianca\'|\'Lucia\'|\'Mia\',
                    \'LanguageCode\': \'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SynthesisTask** *(dict) --* 
        
              SynthesisTask object that provides information and attributes about a newly submitted speech synthesis task.
        
              - **TaskId** *(string) --* 
        
                The Amazon Polly generated identifier for a speech synthesis task.
        
              - **TaskStatus** *(string) --* 
        
                Current status of the individual speech synthesis task.
        
              - **TaskStatusReason** *(string) --* 
        
                Reason for the current status of a specific speech synthesis task, including errors if the task has failed.
        
              - **OutputUri** *(string) --* 
        
                Pathway for the output speech file.
        
              - **CreationTime** *(datetime) --* 
        
                Timestamp for the time the synthesis task was started.
        
              - **RequestCharacters** *(integer) --* 
        
                Number of billable characters synthesized.
        
              - **SnsTopicArn** *(string) --* 
        
                ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.
        
              - **LexiconNames** *(list) --* 
        
                List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. 
        
                - *(string) --* 
            
              - **OutputFormat** *(string) --* 
        
                The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json. 
        
              - **SampleRate** *(string) --* 
        
                The audio frequency specified in Hz.
        
                The valid values for mp3 and ogg_vorbis are \"8000\", \"16000\", and \"22050\". The default value is \"22050\".
        
                Valid values for pcm are \"8000\" and \"16000\" The default value is \"16000\". 
        
              - **SpeechMarkTypes** *(list) --* 
        
                The type of speech marks returned for the input text.
        
                - *(string) --* 
            
              - **TextType** *(string) --* 
        
                Specifies whether the input text is plain text or SSML. The default value is plain text. 
        
              - **VoiceId** *(string) --* 
        
                Voice ID to use for the synthesis. 
        
              - **LanguageCode** *(string) --* 
        
                Optional language code for a synthesis task. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). 
        
                If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the `DescribeVoices <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.
        
        """
        pass

    def synthesize_speech(self, OutputFormat: str, Text: str, VoiceId: str, LexiconNames: List = None, SampleRate: str = None, SpeechMarkTypes: List = None, TextType: str = None, LanguageCode: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/SynthesizeSpeech>`_
        
        **Request Syntax** 
        ::
        
          response = client.synthesize_speech(
              LexiconNames=[
                  \'string\',
              ],
              OutputFormat=\'json\'|\'mp3\'|\'ogg_vorbis\'|\'pcm\',
              SampleRate=\'string\',
              SpeechMarkTypes=[
                  \'sentence\'|\'ssml\'|\'viseme\'|\'word\',
              ],
              Text=\'string\',
              TextType=\'ssml\'|\'text\',
              VoiceId=\'Geraint\'|\'Gwyneth\'|\'Mads\'|\'Naja\'|\'Hans\'|\'Marlene\'|\'Nicole\'|\'Russell\'|\'Amy\'|\'Brian\'|\'Emma\'|\'Raveena\'|\'Ivy\'|\'Joanna\'|\'Joey\'|\'Justin\'|\'Kendra\'|\'Kimberly\'|\'Matthew\'|\'Salli\'|\'Conchita\'|\'Enrique\'|\'Miguel\'|\'Penelope\'|\'Chantal\'|\'Celine\'|\'Lea\'|\'Mathieu\'|\'Dora\'|\'Karl\'|\'Carla\'|\'Giorgio\'|\'Mizuki\'|\'Liv\'|\'Lotte\'|\'Ruben\'|\'Ewa\'|\'Jacek\'|\'Jan\'|\'Maja\'|\'Ricardo\'|\'Vitoria\'|\'Cristiano\'|\'Ines\'|\'Carmen\'|\'Maxim\'|\'Tatyana\'|\'Astrid\'|\'Filiz\'|\'Vicki\'|\'Takumi\'|\'Seoyeon\'|\'Aditi\'|\'Zhiyu\'|\'Bianca\'|\'Lucia\'|\'Mia\',
              LanguageCode=\'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\'
          )
        :type LexiconNames: list
        :param LexiconNames: 
        
          List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see `PutLexicon <http://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html>`__ .
        
          - *(string) --* 
        
        :type OutputFormat: string
        :param OutputFormat: **[REQUIRED]** 
        
          The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json. 
        
          When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format. 
        
        :type SampleRate: string
        :param SampleRate: 
        
          The audio frequency specified in Hz. 
        
          The valid values for ``mp3`` and ``ogg_vorbis`` are \"8000\", \"16000\", and \"22050\". The default value is \"22050\". 
        
          Valid values for ``pcm`` are \"8000\" and \"16000\" The default value is \"16000\". 
        
        :type SpeechMarkTypes: list
        :param SpeechMarkTypes: 
        
          The type of speech marks returned for the input text.
        
          - *(string) --* 
        
        :type Text: string
        :param Text: **[REQUIRED]** 
        
          Input text to synthesize. If you specify ``ssml`` as the ``TextType`` , follow the SSML format for the input text. 
        
        :type TextType: string
        :param TextType: 
        
          Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see `Using SSML <http://docs.aws.amazon.com/polly/latest/dg/ssml.html>`__ .
        
        :type VoiceId: string
        :param VoiceId: **[REQUIRED]** 
        
          Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the `DescribeVoices <http://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation. 
        
        :type LanguageCode: string
        :param LanguageCode: 
        
          Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). 
        
          If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the `DescribeVoices <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AudioStream\': StreamingBody(),
                \'ContentType\': \'string\',
                \'RequestCharacters\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AudioStream** (:class:`.StreamingBody`) -- 
        
              Stream containing the synthesized speech. 
        
            - **ContentType** *(string) --* 
        
              Specifies the type audio stream. This should reflect the ``OutputFormat`` parameter in your request. 
        
              * If you request ``mp3`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/mpeg.  
               
              * If you request ``ogg_vorbis`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/ogg.  
               
              * If you request ``pcm`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.  
               
              * If you request ``json`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/json. 
               
            - **RequestCharacters** *(integer) --* 
        
              Number of characters synthesized.
        
        """
        pass
