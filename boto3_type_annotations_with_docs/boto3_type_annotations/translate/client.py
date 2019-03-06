from typing import Union
from botocore.paginate import Paginator
from typing import List
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from botocore.client import BaseClient


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

    def delete_terminology(self, Name: str):
        """
        A synchronous action that deletes a custom terminology.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/DeleteTerminology>`_
        
        **Request Syntax**
        ::
          response = client.delete_terminology(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the custom terminology being deleted.
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

    def get_terminology(self, Name: str, TerminologyDataFormat: str) -> Dict:
        """
        Retrieves a custom terminology.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/GetTerminology>`_
        
        **Request Syntax**
        ::
          response = client.get_terminology(
              Name='string',
              TerminologyDataFormat='CSV'|'TMX'
          )
        
        **Response Syntax**
        ::
            {
                'TerminologyProperties': {
                    'Name': 'string',
                    'Description': 'string',
                    'Arn': 'string',
                    'SourceLanguageCode': 'string',
                    'TargetLanguageCodes': [
                        'string',
                    ],
                    'EncryptionKey': {
                        'Type': 'KMS',
                        'Id': 'string'
                    },
                    'SizeBytes': 123,
                    'TermCount': 123,
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1)
                },
                'TerminologyDataLocation': {
                    'RepositoryType': 'string',
                    'Location': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TerminologyProperties** *(dict) --* 
              The properties of the custom terminology being retrieved.
              - **Name** *(string) --* 
                The name of the custom terminology.
              - **Description** *(string) --* 
                The description of the custom terminology properties.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) of the custom terminology. 
              - **SourceLanguageCode** *(string) --* 
                The language code for the source text of the translation request for which the custom terminology is being used.
              - **TargetLanguageCodes** *(list) --* 
                The language codes for the target languages available with the custom terminology file. All possible target languages are returned in array.
                - *(string) --* 
              - **EncryptionKey** *(dict) --* 
                The encryption key for the custom terminology.
                - **Type** *(string) --* 
                  The type of encryption key used by Amazon Translate to encrypt custom terminologies.
                - **Id** *(string) --* 
                  The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.
              - **SizeBytes** *(integer) --* 
                The size of the file used when importing a custom terminology.
              - **TermCount** *(integer) --* 
                The number of terms included in the custom terminology.
              - **CreatedAt** *(datetime) --* 
                The time at which the custom terminology was created, based on the timestamp.
              - **LastUpdatedAt** *(datetime) --* 
                The time at which the custom terminology was last update, based on the timestamp.
            - **TerminologyDataLocation** *(dict) --* 
              The data location of the custom terminology being retrieved. The custom terminology file is returned in a presigned url that has a 30 minute expiration.
              - **RepositoryType** *(string) --* 
                The repository type for the custom terminology data.
              - **Location** *(string) --* 
                The location of the custom terminology data.
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the custom terminology being retrieved.
        :type TerminologyDataFormat: string
        :param TerminologyDataFormat: **[REQUIRED]**
          The data format of the custom terminology being retrieved, either CSV or TMX.
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

    def import_terminology(self, Name: str, MergeStrategy: str, TerminologyData: Dict, Description: str = None, EncryptionKey: Dict = None) -> Dict:
        """
        Creates or updates a custom terminology, depending on whether or not one already exists for the given terminology name. Importing a terminology with the same name as an existing one will merge the terminologies based on the chosen merge strategy. Currently, the only supported merge strategy is OVERWRITE, and so the imported terminology will overwrite an existing terminology of the same name.
        If you import a terminology that overwrites an existing one, the new terminology take up to 10 minutes to fully propagate and be available for use in a translation due to cache policies with the DataPlane service that performs the translations.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/ImportTerminology>`_
        
        **Request Syntax**
        ::
          response = client.import_terminology(
              Name='string',
              MergeStrategy='OVERWRITE',
              Description='string',
              TerminologyData={
                  'File': b'bytes',
                  'Format': 'CSV'|'TMX'
              },
              EncryptionKey={
                  'Type': 'KMS',
                  'Id': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TerminologyProperties': {
                    'Name': 'string',
                    'Description': 'string',
                    'Arn': 'string',
                    'SourceLanguageCode': 'string',
                    'TargetLanguageCodes': [
                        'string',
                    ],
                    'EncryptionKey': {
                        'Type': 'KMS',
                        'Id': 'string'
                    },
                    'SizeBytes': 123,
                    'TermCount': 123,
                    'CreatedAt': datetime(2015, 1, 1),
                    'LastUpdatedAt': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TerminologyProperties** *(dict) --* 
              The properties of the custom terminology being imported.
              - **Name** *(string) --* 
                The name of the custom terminology.
              - **Description** *(string) --* 
                The description of the custom terminology properties.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) of the custom terminology. 
              - **SourceLanguageCode** *(string) --* 
                The language code for the source text of the translation request for which the custom terminology is being used.
              - **TargetLanguageCodes** *(list) --* 
                The language codes for the target languages available with the custom terminology file. All possible target languages are returned in array.
                - *(string) --* 
              - **EncryptionKey** *(dict) --* 
                The encryption key for the custom terminology.
                - **Type** *(string) --* 
                  The type of encryption key used by Amazon Translate to encrypt custom terminologies.
                - **Id** *(string) --* 
                  The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.
              - **SizeBytes** *(integer) --* 
                The size of the file used when importing a custom terminology.
              - **TermCount** *(integer) --* 
                The number of terms included in the custom terminology.
              - **CreatedAt** *(datetime) --* 
                The time at which the custom terminology was created, based on the timestamp.
              - **LastUpdatedAt** *(datetime) --* 
                The time at which the custom terminology was last update, based on the timestamp.
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the custom terminology being imported.
        :type MergeStrategy: string
        :param MergeStrategy: **[REQUIRED]**
          The merge strategy of the custom terminology being imported. Currently, only the OVERWRITE merge strategy is supported. In this case, the imported terminology will overwrite an existing terminology of the same name.
        :type Description: string
        :param Description:
          The description of the custom terminology being imported.
        :type TerminologyData: dict
        :param TerminologyData: **[REQUIRED]**
          The terminology data for the custom terminology being imported.
          - **File** *(bytes) --* **[REQUIRED]**
            The file containing the custom terminology data.
          - **Format** *(string) --* **[REQUIRED]**
            The data format of the custom terminology. Either CSV or TMX.
        :type EncryptionKey: dict
        :param EncryptionKey:
          The encryption key for the custom terminology being imported.
          - **Type** *(string) --* **[REQUIRED]**
            The type of encryption key used by Amazon Translate to encrypt custom terminologies.
          - **Id** *(string) --* **[REQUIRED]**
            The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.
        :rtype: dict
        :returns:
        """
        pass

    def list_terminologies(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Provides a list of custom terminologies associated with your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/ListTerminologies>`_
        
        **Request Syntax**
        ::
          response = client.list_terminologies(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'TerminologyPropertiesList': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'Arn': 'string',
                        'SourceLanguageCode': 'string',
                        'TargetLanguageCodes': [
                            'string',
                        ],
                        'EncryptionKey': {
                            'Type': 'KMS',
                            'Id': 'string'
                        },
                        'SizeBytes': 123,
                        'TermCount': 123,
                        'CreatedAt': datetime(2015, 1, 1),
                        'LastUpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TerminologyPropertiesList** *(list) --* 
              The properties list of the custom terminologies returned on the list request.
              - *(dict) --* 
                The properties of the custom terminology.
                - **Name** *(string) --* 
                  The name of the custom terminology.
                - **Description** *(string) --* 
                  The description of the custom terminology properties.
                - **Arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the custom terminology. 
                - **SourceLanguageCode** *(string) --* 
                  The language code for the source text of the translation request for which the custom terminology is being used.
                - **TargetLanguageCodes** *(list) --* 
                  The language codes for the target languages available with the custom terminology file. All possible target languages are returned in array.
                  - *(string) --* 
                - **EncryptionKey** *(dict) --* 
                  The encryption key for the custom terminology.
                  - **Type** *(string) --* 
                    The type of encryption key used by Amazon Translate to encrypt custom terminologies.
                  - **Id** *(string) --* 
                    The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.
                - **SizeBytes** *(integer) --* 
                  The size of the file used when importing a custom terminology.
                - **TermCount** *(integer) --* 
                  The number of terms included in the custom terminology.
                - **CreatedAt** *(datetime) --* 
                  The time at which the custom terminology was created, based on the timestamp.
                - **LastUpdatedAt** *(datetime) --* 
                  The time at which the custom terminology was last update, based on the timestamp.
            - **NextToken** *(string) --* 
              If the response to the ListTerminologies was truncated, the NextToken fetches the next group of custom terminologies. 
        :type NextToken: string
        :param NextToken:
          If the result of the request to ListTerminologies was truncated, include the NextToken to fetch the next group of custom terminologies.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of custom terminologies returned per list request.
        :rtype: dict
        :returns:
        """
        pass

    def translate_text(self, Text: str, SourceLanguageCode: str, TargetLanguageCode: str, TerminologyNames: List = None) -> Dict:
        """
        Translates input text from the source language to the target language. It is not necessary to use English (en) as either the source or the target language but not all language combinations are supported by Amazon Translate. For more information, see `Supported Language Pairs <http://docs.aws.amazon.com/translate/latest/dg/pairs.html>`__ .
        * Arabic (ar) 
        * Chinese (Simplified) (zh) 
        * Chinese (Traditional) (zh-TW) 
        * Czech (cs) 
        * Danish (da) 
        * Dutch (nl) 
        * English (en) 
        * Finnish (fi) 
        * French (fr) 
        * German (de) 
        * Hebrew (he) 
        * Indonesian (id) 
        * Italian (it) 
        * Japanese (ja) 
        * Korean (ko) 
        * Polish (pl) 
        * Portuguese (pt) 
        * Russian (ru) 
        * Spanish (es) 
        * Swedish (sv) 
        * Turkish (tr) 
        To have Amazon Translate determine the source language of your text, you can specify ``auto`` in the ``SourceLanguageCode`` field. If you specify ``auto`` , Amazon Translate will call Amazon Comprehend to determine the source language.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/TranslateText>`_
        
        **Request Syntax**
        ::
          response = client.translate_text(
              Text='string',
              TerminologyNames=[
                  'string',
              ],
              SourceLanguageCode='string',
              TargetLanguageCode='string'
          )
        
        **Response Syntax**
        ::
            {
                'TranslatedText': 'string',
                'SourceLanguageCode': 'string',
                'TargetLanguageCode': 'string',
                'AppliedTerminologies': [
                    {
                        'Name': 'string',
                        'Terms': [
                            {
                                'SourceText': 'string',
                                'TargetText': 'string'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TranslatedText** *(string) --* 
              The the translated text. The maximum length of this text is 5kb.
            - **SourceLanguageCode** *(string) --* 
              The language code for the language of the source text. 
            - **TargetLanguageCode** *(string) --* 
              The language code for the language of the target text. 
            - **AppliedTerminologies** *(list) --* 
              The names of the custom terminologies applied to the input text by Amazon Translate for the translated text response.
              - *(dict) --* 
                The custom terminology applied to the input text by Amazon Translate for the translated text response. This is optional in the response and will only be present if you specified terminology input in the request. Currently, only one terminology can be applied per TranslateText request.
                - **Name** *(string) --* 
                  The name of the custom terminology applied to the input text by Amazon Translate for the translated text response.
                - **Terms** *(list) --* 
                  The specific terms of the custom terminology applied to the input text by Amazon Translate for the translated text response. A maximum of 250 terms will be returned, and the specific terms applied will be the first 250 terms in the source text. 
                  - *(dict) --* 
                    The term being translated by the custom terminology.
                    - **SourceText** *(string) --* 
                      The source text of the term being translated by the custom terminology.
                    - **TargetText** *(string) --* 
                      The target text of the term being translated by the custom terminology.
        :type Text: string
        :param Text: **[REQUIRED]**
          The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters.
        :type TerminologyNames: list
        :param TerminologyNames:
          The TerminologyNames list that is taken as input to the TranslateText request. This has a minimum length of 0 and a maximum length of 1.
          - *(string) --*
        :type SourceLanguageCode: string
        :param SourceLanguageCode: **[REQUIRED]**
          The language code for the language of the source text. The language must be a language supported by Amazon Translate.
          To have Amazon Translate determine the source language of your text, you can specify ``auto`` in the ``SourceLanguageCode`` field. If you specify ``auto`` , Amazon Translate will call Amazon Comprehend to determine the source language.
        :type TargetLanguageCode: string
        :param TargetLanguageCode: **[REQUIRED]**
          The language code requested for the language of the target text. The language must be a language supported by Amazon Translate.
        :rtype: dict
        :returns:
        """
        pass
