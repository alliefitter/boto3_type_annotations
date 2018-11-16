from typing import Dict
from botocore.paginate import Paginator


class DescribeVoices(Paginator):
    def paginate(self, LanguageCode: str = None, IncludeAdditionalLanguageCodes: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DescribeVoices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              LanguageCode=\'cmn-CN\'|\'cy-GB\'|\'da-DK\'|\'de-DE\'|\'en-AU\'|\'en-GB\'|\'en-GB-WLS\'|\'en-IN\'|\'en-US\'|\'es-ES\'|\'es-MX\'|\'es-US\'|\'fr-CA\'|\'fr-FR\'|\'is-IS\'|\'it-IT\'|\'ja-JP\'|\'hi-IN\'|\'ko-KR\'|\'nb-NO\'|\'nl-NL\'|\'pl-PL\'|\'pt-BR\'|\'pt-PT\'|\'ro-RO\'|\'ru-RU\'|\'sv-SE\'|\'tr-TR\',
              IncludeAdditionalLanguageCodes=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
              
        """
        pass
