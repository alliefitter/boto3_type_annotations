from typing import Dict
from botocore.paginate import Paginator


class DescribeVoices(Paginator):
    def paginate(self, LanguageCode: str = None, IncludeAdditionalLanguageCodes: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Polly.Client.describe_voices`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DescribeVoices>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              LanguageCode='arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
              IncludeAdditionalLanguageCodes=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Voices': [
                    {
                        'Gender': 'Female'|'Male',
                        'Id': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
                        'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                        'LanguageName': 'string',
                        'Name': 'string',
                        'AdditionalLanguageCodes': [
                            'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                        ]
                    },
                ],
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
        :type LanguageCode: string
        :param LanguageCode:
          The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don\'t specify this optional parameter, all available voices are returned.
        :type IncludeAdditionalLanguageCodes: boolean
        :param IncludeAdditionalLanguageCodes:
          Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify ``yes`` but not if you specify ``no`` .
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
        """
        pass


class ListLexicons(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Polly.Client.list_lexicons`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/ListLexicons>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Lexicons': [
                    {
                        'Name': 'string',
                        'Attributes': {
                            'Alphabet': 'string',
                            'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                            'LastModified': datetime(2015, 1, 1),
                            'LexiconArn': 'string',
                            'LexemesCount': 123,
                            'Size': 123
                        }
                    },
                ],
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
                    Language code that the lexicon applies to. A lexicon with a language code such as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.
                  - **LastModified** *(datetime) --* 
                    Date lexicon was last modified (a timestamp value).
                  - **LexiconArn** *(string) --* 
                    Amazon Resource Name (ARN) of the lexicon.
                  - **LexemesCount** *(integer) --* 
                    Number of lexemes in the lexicon.
                  - **Size** *(integer) --* 
                    Total size of the lexicon, in characters.
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
        """
        pass


class ListSpeechSynthesisTasks(Paginator):
    def paginate(self, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Polly.Client.list_speech_synthesis_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/ListSpeechSynthesisTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Status='scheduled'|'inProgress'|'completed'|'failed',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SynthesisTasks': [
                    {
                        'TaskId': 'string',
                        'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
                        'TaskStatusReason': 'string',
                        'OutputUri': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'RequestCharacters': 123,
                        'SnsTopicArn': 'string',
                        'LexiconNames': [
                            'string',
                        ],
                        'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
                        'SampleRate': 'string',
                        'SpeechMarkTypes': [
                            'sentence'|'ssml'|'viseme'|'word',
                        ],
                        'TextType': 'ssml'|'text',
                        'VoiceId': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
                        'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
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
                  The valid values for mp3 and ogg_vorbis are "8000", "16000", and "22050". The default value is "22050".
                  Valid values for pcm are "8000" and "16000" The default value is "16000". 
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
        :type Status: string
        :param Status:
          Status of the speech synthesis tasks returned in a List operation
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
        """
        pass
