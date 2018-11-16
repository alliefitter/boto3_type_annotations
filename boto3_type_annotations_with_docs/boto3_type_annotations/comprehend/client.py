from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_detect_dominant_language(self, TextList: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectDominantLanguage>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_detect_dominant_language(
              TextList=[
                  \'string\',
              ]
          )
        :type TextList: list
        :param TextList: **[REQUIRED]** 
        
          A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document should contain at least 20 characters and must contain fewer than 5,000 bytes of UTF-8 encoded characters.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResultList\': [
                    {
                        \'Index\': 123,
                        \'Languages\': [
                            {
                                \'LanguageCode\': \'string\',
                                \'Score\': ...
                            },
                        ]
                    },
                ],
                \'ErrorList\': [
                    {
                        \'Index\': 123,
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResultList** *(list) --* 
        
              A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.
        
              - *(dict) --* 
        
                The result of calling the operation. The operation returns one object for each document that is successfully processed by the operation.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **Languages** *(list) --* 
        
                  One or more  DominantLanguage objects describing the dominant languages in the document.
        
                  - *(dict) --* 
        
                    Returns the code for the dominant language in the input text and the level of confidence that Amazon Comprehend has in the accuracy of the detection.
        
                    - **LanguageCode** *(string) --* 
        
                      The RFC 5646 language code for the dominant language. For more information about RFC 5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site.
        
                    - **Score** *(float) --* 
        
                      The level of confidence that Amazon Comprehend has in the accuracy of the detection.
        
            - **ErrorList** *(list) --* 
        
              A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.
        
              - *(dict) --* 
        
                Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **ErrorCode** *(string) --* 
        
                  The numeric error code of the error.
        
                - **ErrorMessage** *(string) --* 
        
                  A text description of the error.
        
        """
        pass

    def batch_detect_entities(self, TextList: List, LanguageCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectEntities>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_detect_entities(
              TextList=[
                  \'string\',
              ],
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\'
          )
        :type TextList: list
        :param TextList: **[REQUIRED]** 
        
          A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer than 5,000 bytes of UTF-8 encoded characters.
        
          - *(string) --* 
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResultList\': [
                    {
                        \'Index\': 123,
                        \'Entities\': [
                            {
                                \'Score\': ...,
                                \'Type\': \'PERSON\'|\'LOCATION\'|\'ORGANIZATION\'|\'COMMERCIAL_ITEM\'|\'EVENT\'|\'DATE\'|\'QUANTITY\'|\'TITLE\'|\'OTHER\',
                                \'Text\': \'string\',
                                \'BeginOffset\': 123,
                                \'EndOffset\': 123
                            },
                        ]
                    },
                ],
                \'ErrorList\': [
                    {
                        \'Index\': 123,
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResultList** *(list) --* 
        
              A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.
        
              - *(dict) --* 
        
                The result of calling the operation. The operation returns one object for each document that is successfully processed by the operation.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **Entities** *(list) --* 
        
                  One or more  Entity objects, one for each entity detected in the document.
        
                  - *(dict) --* 
        
                    Provides information about an entity. 
        
                    - **Score** *(float) --* 
        
                      The level of confidence that Amazon Comprehend has in the accuracy of the detection.
        
                    - **Type** *(string) --* 
        
                      The entity\'s type.
        
                    - **Text** *(string) --* 
        
                      The text of the entity.
        
                    - **BeginOffset** *(integer) --* 
        
                      A character offset in the input text that shows where the entity begins (the first character is at position 0). The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.
        
                    - **EndOffset** *(integer) --* 
        
                      A character offset in the input text that shows where the entity ends. The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point. 
        
            - **ErrorList** *(list) --* 
        
              A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.
        
              - *(dict) --* 
        
                Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **ErrorCode** *(string) --* 
        
                  The numeric error code of the error.
        
                - **ErrorMessage** *(string) --* 
        
                  A text description of the error.
        
        """
        pass

    def batch_detect_key_phrases(self, TextList: List, LanguageCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectKeyPhrases>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_detect_key_phrases(
              TextList=[
                  \'string\',
              ],
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\'
          )
        :type TextList: list
        :param TextList: **[REQUIRED]** 
        
          A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.
        
          - *(string) --* 
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResultList\': [
                    {
                        \'Index\': 123,
                        \'KeyPhrases\': [
                            {
                                \'Score\': ...,
                                \'Text\': \'string\',
                                \'BeginOffset\': 123,
                                \'EndOffset\': 123
                            },
                        ]
                    },
                ],
                \'ErrorList\': [
                    {
                        \'Index\': 123,
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResultList** *(list) --* 
        
              A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.
        
              - *(dict) --* 
        
                The result of calling the operation. The operation returns one object for each document that is successfully processed by the operation.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **KeyPhrases** *(list) --* 
        
                  One or more  KeyPhrase objects, one for each key phrase detected in the document.
        
                  - *(dict) --* 
        
                    Describes a key noun phrase.
        
                    - **Score** *(float) --* 
        
                      The level of confidence that Amazon Comprehend has in the accuracy of the detection.
        
                    - **Text** *(string) --* 
        
                      The text of a key noun phrase.
        
                    - **BeginOffset** *(integer) --* 
        
                      A character offset in the input text that shows where the key phrase begins (the first character is at position 0). The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.
        
                    - **EndOffset** *(integer) --* 
        
                      A character offset in the input text where the key phrase ends. The offset returns the position of each UTF-8 code point in the string. A ``code point`` is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.
        
            - **ErrorList** *(list) --* 
        
              A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.
        
              - *(dict) --* 
        
                Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **ErrorCode** *(string) --* 
        
                  The numeric error code of the error.
        
                - **ErrorMessage** *(string) --* 
        
                  A text description of the error.
        
        """
        pass

    def batch_detect_sentiment(self, TextList: List, LanguageCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectSentiment>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_detect_sentiment(
              TextList=[
                  \'string\',
              ],
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\'
          )
        :type TextList: list
        :param TextList: **[REQUIRED]** 
        
          A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.
        
          - *(string) --* 
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResultList\': [
                    {
                        \'Index\': 123,
                        \'Sentiment\': \'POSITIVE\'|\'NEGATIVE\'|\'NEUTRAL\'|\'MIXED\',
                        \'SentimentScore\': {
                            \'Positive\': ...,
                            \'Negative\': ...,
                            \'Neutral\': ...,
                            \'Mixed\': ...
                        }
                    },
                ],
                \'ErrorList\': [
                    {
                        \'Index\': 123,
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResultList** *(list) --* 
        
              A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.
        
              - *(dict) --* 
        
                The result of calling the operation. The operation returns one object for each document that is successfully processed by the operation.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **Sentiment** *(string) --* 
        
                  The sentiment detected in the document.
        
                - **SentimentScore** *(dict) --* 
        
                  The level of confidence that Amazon Comprehend has in the accuracy of its sentiment detection.
        
                  - **Positive** *(float) --* 
        
                    The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``POSITIVE`` sentiment.
        
                  - **Negative** *(float) --* 
        
                    The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``NEGATIVE`` sentiment.
        
                  - **Neutral** *(float) --* 
        
                    The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``NEUTRAL`` sentiment.
        
                  - **Mixed** *(float) --* 
        
                    The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``MIXED`` sentiment.
        
            - **ErrorList** *(list) --* 
        
              A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.
        
              - *(dict) --* 
        
                Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **ErrorCode** *(string) --* 
        
                  The numeric error code of the error.
        
                - **ErrorMessage** *(string) --* 
        
                  A text description of the error.
        
        """
        pass

    def batch_detect_syntax(self, TextList: List, LanguageCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectSyntax>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_detect_syntax(
              TextList=[
                  \'string\',
              ],
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\'
          )
        :type TextList: list
        :param TextList: **[REQUIRED]** 
        
          A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.
        
          - *(string) --* 
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResultList\': [
                    {
                        \'Index\': 123,
                        \'SyntaxTokens\': [
                            {
                                \'TokenId\': 123,
                                \'Text\': \'string\',
                                \'BeginOffset\': 123,
                                \'EndOffset\': 123,
                                \'PartOfSpeech\': {
                                    \'Tag\': \'ADJ\'|\'ADP\'|\'ADV\'|\'AUX\'|\'CONJ\'|\'DET\'|\'INTJ\'|\'NOUN\'|\'NUM\'|\'O\'|\'PART\'|\'PRON\'|\'PROPN\'|\'PUNCT\'|\'SCONJ\'|\'SYM\'|\'VERB\',
                                    \'Score\': ...
                                }
                            },
                        ]
                    },
                ],
                \'ErrorList\': [
                    {
                        \'Index\': 123,
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResultList** *(list) --* 
        
              A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.
        
              - *(dict) --* 
        
                The result of calling the operation. The operation returns one object that is successfully processed by the operation.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **SyntaxTokens** *(list) --* 
        
                  The syntax tokens for the words in the document, one token for each word.
        
                  - *(dict) --* 
        
                    Represents a work in the input text that was recognized and assigned a part of speech. There is one syntax token record for each word in the source text.
        
                    - **TokenId** *(integer) --* 
        
                      A unique identifier for a token.
        
                    - **Text** *(string) --* 
        
                      The word that was recognized in the source text.
        
                    - **BeginOffset** *(integer) --* 
        
                      The zero-based offset from the beginning of the source text to the first character in the word.
        
                    - **EndOffset** *(integer) --* 
        
                      The zero-based offset from the beginning of the source text to the last character in the word.
        
                    - **PartOfSpeech** *(dict) --* 
        
                      Provides the part of speech label and the confidence level that Amazon Comprehend has that the part of speech was correctly identified. For more information, see  how-syntax .
        
                      - **Tag** *(string) --* 
        
                        Identifies the part of speech that the token represents.
        
                      - **Score** *(float) --* 
        
                        The confidence that Amazon Comprehend has that the part of speech was correctly identified.
        
            - **ErrorList** *(list) --* 
        
              A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.
        
              - *(dict) --* 
        
                Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.
        
                - **Index** *(integer) --* 
        
                  The zero-based index of the document in the input list.
        
                - **ErrorCode** *(string) --* 
        
                  The numeric error code of the error.
        
                - **ErrorMessage** *(string) --* 
        
                  A text description of the error.
        
        """
        pass

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

    def describe_dominant_language_detection_job(self, JobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeDominantLanguageDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_dominant_language_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DominantLanguageDetectionJobProperties\': {
                    \'JobId\': \'string\',
                    \'JobName\': \'string\',
                    \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                    \'Message\': \'string\',
                    \'SubmitTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'InputDataConfig\': {
                        \'S3Uri\': \'string\',
                        \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                    },
                    \'OutputDataConfig\': {
                        \'S3Uri\': \'string\'
                    },
                    \'DataAccessRoleArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DominantLanguageDetectionJobProperties** *(dict) --* 
        
              An object that contains the properties associated with a dominant language detection job.
        
              - **JobId** *(string) --* 
        
                The identifier assigned to the dominant language detection job.
        
              - **JobName** *(string) --* 
        
                The name that you assigned to the dominant language detection job.
        
              - **JobStatus** *(string) --* 
        
                The current status of the dominant language detection job. If the status is ``FAILED`` , the ``Message`` field shows the reason for the failure.
        
              - **Message** *(string) --* 
        
                A description for the status of a job.
        
              - **SubmitTime** *(datetime) --* 
        
                The time that the dominant language detection job was submitted for processing.
        
              - **EndTime** *(datetime) --* 
        
                The time that the dominant language detection job completed.
        
              - **InputDataConfig** *(dict) --* 
        
                The input data configuration that you supplied when you created the dominant language detection job.
        
                - **S3Uri** *(string) --* 
        
                  The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                - **InputFormat** *(string) --* 
        
                  Specifies how the text in an input file should be processed:
        
                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                   
                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                   
              - **OutputDataConfig** *(dict) --* 
        
                The output data configuration that you supplied when you created the dominant language detection job.
        
                - **S3Uri** *(string) --* 
        
                  When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                  When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
              - **DataAccessRoleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.
        
        """
        pass

    def describe_entities_detection_job(self, JobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeEntitiesDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_entities_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EntitiesDetectionJobProperties\': {
                    \'JobId\': \'string\',
                    \'JobName\': \'string\',
                    \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                    \'Message\': \'string\',
                    \'SubmitTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'InputDataConfig\': {
                        \'S3Uri\': \'string\',
                        \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                    },
                    \'OutputDataConfig\': {
                        \'S3Uri\': \'string\'
                    },
                    \'LanguageCode\': \'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
                    \'DataAccessRoleArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EntitiesDetectionJobProperties** *(dict) --* 
        
              An object that contains the properties associated with an entities detection job.
        
              - **JobId** *(string) --* 
        
                The identifier assigned to the entities detection job.
        
              - **JobName** *(string) --* 
        
                The name that you assigned the entities detection job.
        
              - **JobStatus** *(string) --* 
        
                The current status of the entities detection job. If the status is ``FAILED`` , the ``Message`` field shows the reason for the failure.
        
              - **Message** *(string) --* 
        
                A description of the status of a job.
        
              - **SubmitTime** *(datetime) --* 
        
                The time that the entities detection job was submitted for processing.
        
              - **EndTime** *(datetime) --* 
        
                The time that the entities detection job completed
        
              - **InputDataConfig** *(dict) --* 
        
                The input data configuration that you supplied when you created the entities detection job.
        
                - **S3Uri** *(string) --* 
        
                  The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                - **InputFormat** *(string) --* 
        
                  Specifies how the text in an input file should be processed:
        
                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                   
                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                   
              - **OutputDataConfig** *(dict) --* 
        
                The output data configuration that you supplied when you created the entities detection job. 
        
                - **S3Uri** *(string) --* 
        
                  When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                  When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
              - **LanguageCode** *(string) --* 
        
                The language code of the input documents.
        
              - **DataAccessRoleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.
        
        """
        pass

    def describe_key_phrases_detection_job(self, JobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeKeyPhrasesDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_key_phrases_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyPhrasesDetectionJobProperties\': {
                    \'JobId\': \'string\',
                    \'JobName\': \'string\',
                    \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                    \'Message\': \'string\',
                    \'SubmitTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'InputDataConfig\': {
                        \'S3Uri\': \'string\',
                        \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                    },
                    \'OutputDataConfig\': {
                        \'S3Uri\': \'string\'
                    },
                    \'LanguageCode\': \'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
                    \'DataAccessRoleArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyPhrasesDetectionJobProperties** *(dict) --* 
        
              An object that contains the properties associated with a key phrases detection job. 
        
              - **JobId** *(string) --* 
        
                The identifier assigned to the key phrases detection job.
        
              - **JobName** *(string) --* 
        
                The name that you assigned the key phrases detection job.
        
              - **JobStatus** *(string) --* 
        
                The current status of the key phrases detection job. If the status is ``FAILED`` , the ``Message`` field shows the reason for the failure.
        
              - **Message** *(string) --* 
        
                A description of the status of a job.
        
              - **SubmitTime** *(datetime) --* 
        
                The time that the key phrases detection job was submitted for processing.
        
              - **EndTime** *(datetime) --* 
        
                The time that the key phrases detection job completed.
        
              - **InputDataConfig** *(dict) --* 
        
                The input data configuration that you supplied when you created the key phrases detection job.
        
                - **S3Uri** *(string) --* 
        
                  The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                - **InputFormat** *(string) --* 
        
                  Specifies how the text in an input file should be processed:
        
                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                   
                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                   
              - **OutputDataConfig** *(dict) --* 
        
                The output data configuration that you supplied when you created the key phrases detection job.
        
                - **S3Uri** *(string) --* 
        
                  When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                  When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
              - **LanguageCode** *(string) --* 
        
                The language code of the input documents.
        
              - **DataAccessRoleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.
        
        """
        pass

    def describe_sentiment_detection_job(self, JobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeSentimentDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_sentiment_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SentimentDetectionJobProperties\': {
                    \'JobId\': \'string\',
                    \'JobName\': \'string\',
                    \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                    \'Message\': \'string\',
                    \'SubmitTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'InputDataConfig\': {
                        \'S3Uri\': \'string\',
                        \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                    },
                    \'OutputDataConfig\': {
                        \'S3Uri\': \'string\'
                    },
                    \'LanguageCode\': \'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
                    \'DataAccessRoleArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SentimentDetectionJobProperties** *(dict) --* 
        
              An object that contains the properties associated with a sentiment detection job.
        
              - **JobId** *(string) --* 
        
                The identifier assigned to the sentiment detection job.
        
              - **JobName** *(string) --* 
        
                The name that you assigned to the sentiment detection job
        
              - **JobStatus** *(string) --* 
        
                The current status of the sentiment detection job. If the status is ``FAILED`` , the ``Messages`` field shows the reason for the failure.
        
              - **Message** *(string) --* 
        
                A description of the status of a job.
        
              - **SubmitTime** *(datetime) --* 
        
                The time that the sentiment detection job was submitted for processing.
        
              - **EndTime** *(datetime) --* 
        
                The time that the sentiment detection job ended.
        
              - **InputDataConfig** *(dict) --* 
        
                The input data configuration that you supplied when you created the sentiment detection job.
        
                - **S3Uri** *(string) --* 
        
                  The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                - **InputFormat** *(string) --* 
        
                  Specifies how the text in an input file should be processed:
        
                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                   
                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                   
              - **OutputDataConfig** *(dict) --* 
        
                The output data configuration that you supplied when you created the sentiment detection job.
        
                - **S3Uri** *(string) --* 
        
                  When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                  When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
              - **LanguageCode** *(string) --* 
        
                The language code of the input documents.
        
              - **DataAccessRoleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.
        
        """
        pass

    def describe_topics_detection_job(self, JobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeTopicsDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_topics_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier assigned by the user to the detection job.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TopicsDetectionJobProperties\': {
                    \'JobId\': \'string\',
                    \'JobName\': \'string\',
                    \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                    \'Message\': \'string\',
                    \'SubmitTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'InputDataConfig\': {
                        \'S3Uri\': \'string\',
                        \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                    },
                    \'OutputDataConfig\': {
                        \'S3Uri\': \'string\'
                    },
                    \'NumberOfTopics\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TopicsDetectionJobProperties** *(dict) --* 
        
              The list of properties for the requested job.
        
              - **JobId** *(string) --* 
        
                The identifier assigned to the topic detection job.
        
              - **JobName** *(string) --* 
        
                The name of the topic detection job.
        
              - **JobStatus** *(string) --* 
        
                The current status of the topic detection job. If the status is ``Failed`` , the reason for the failure is shown in the ``Message`` field.
        
              - **Message** *(string) --* 
        
                A description for the status of a job.
        
              - **SubmitTime** *(datetime) --* 
        
                The time that the topic detection job was submitted for processing.
        
              - **EndTime** *(datetime) --* 
        
                The time that the topic detection job was completed.
        
              - **InputDataConfig** *(dict) --* 
        
                The input data configuration supplied when you created the topic detection job.
        
                - **S3Uri** *(string) --* 
        
                  The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                - **InputFormat** *(string) --* 
        
                  Specifies how the text in an input file should be processed:
        
                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                   
                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                   
              - **OutputDataConfig** *(dict) --* 
        
                The output data configuration supplied when you created the topic detection job.
        
                - **S3Uri** *(string) --* 
        
                  When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                  When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
              - **NumberOfTopics** *(integer) --* 
        
                The number of topics to detect supplied when you created the topic detection job. The default is 10. 
        
        """
        pass

    def detect_dominant_language(self, Text: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectDominantLanguage>`_
        
        **Request Syntax** 
        ::
        
          response = client.detect_dominant_language(
              Text=\'string\'
          )
        :type Text: string
        :param Text: **[REQUIRED]** 
        
          A UTF-8 text string. Each string should contain at least 20 characters and must contain fewer that 5,000 bytes of UTF-8 encoded characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Languages\': [
                    {
                        \'LanguageCode\': \'string\',
                        \'Score\': ...
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Languages** *(list) --* 
        
              The languages that Amazon Comprehend detected in the input text. For each language, the response returns the RFC 5646 language code and the level of confidence that Amazon Comprehend has in the accuracy of its inference. For more information about RFC 5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site.
        
              - *(dict) --* 
        
                Returns the code for the dominant language in the input text and the level of confidence that Amazon Comprehend has in the accuracy of the detection.
        
                - **LanguageCode** *(string) --* 
        
                  The RFC 5646 language code for the dominant language. For more information about RFC 5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site.
        
                - **Score** *(float) --* 
        
                  The level of confidence that Amazon Comprehend has in the accuracy of the detection.
        
        """
        pass

    def detect_entities(self, Text: str, LanguageCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectEntities>`_
        
        **Request Syntax** 
        ::
        
          response = client.detect_entities(
              Text=\'string\',
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\'
          )
        :type Text: string
        :param Text: **[REQUIRED]** 
        
          A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Entities\': [
                    {
                        \'Score\': ...,
                        \'Type\': \'PERSON\'|\'LOCATION\'|\'ORGANIZATION\'|\'COMMERCIAL_ITEM\'|\'EVENT\'|\'DATE\'|\'QUANTITY\'|\'TITLE\'|\'OTHER\',
                        \'Text\': \'string\',
                        \'BeginOffset\': 123,
                        \'EndOffset\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Entities** *(list) --* 
        
              A collection of entities identified in the input text. For each entity, the response provides the entity text, entity type, where the entity text begins and ends, and the level of confidence that Amazon Comprehend has in the detection. For a list of entity types, see  how-entities . 
        
              - *(dict) --* 
        
                Provides information about an entity. 
        
                - **Score** *(float) --* 
        
                  The level of confidence that Amazon Comprehend has in the accuracy of the detection.
        
                - **Type** *(string) --* 
        
                  The entity\'s type.
        
                - **Text** *(string) --* 
        
                  The text of the entity.
        
                - **BeginOffset** *(integer) --* 
        
                  A character offset in the input text that shows where the entity begins (the first character is at position 0). The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.
        
                - **EndOffset** *(integer) --* 
        
                  A character offset in the input text that shows where the entity ends. The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point. 
        
        """
        pass

    def detect_key_phrases(self, Text: str, LanguageCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectKeyPhrases>`_
        
        **Request Syntax** 
        ::
        
          response = client.detect_key_phrases(
              Text=\'string\',
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\'
          )
        :type Text: string
        :param Text: **[REQUIRED]** 
        
          A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyPhrases\': [
                    {
                        \'Score\': ...,
                        \'Text\': \'string\',
                        \'BeginOffset\': 123,
                        \'EndOffset\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyPhrases** *(list) --* 
        
              A collection of key phrases that Amazon Comprehend identified in the input text. For each key phrase, the response provides the text of the key phrase, where the key phrase begins and ends, and the level of confidence that Amazon Comprehend has in the accuracy of the detection. 
        
              - *(dict) --* 
        
                Describes a key noun phrase.
        
                - **Score** *(float) --* 
        
                  The level of confidence that Amazon Comprehend has in the accuracy of the detection.
        
                - **Text** *(string) --* 
        
                  The text of a key noun phrase.
        
                - **BeginOffset** *(integer) --* 
        
                  A character offset in the input text that shows where the key phrase begins (the first character is at position 0). The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.
        
                - **EndOffset** *(integer) --* 
        
                  A character offset in the input text where the key phrase ends. The offset returns the position of each UTF-8 code point in the string. A ``code point`` is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.
        
        """
        pass

    def detect_sentiment(self, Text: str, LanguageCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectSentiment>`_
        
        **Request Syntax** 
        ::
        
          response = client.detect_sentiment(
              Text=\'string\',
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\'
          )
        :type Text: string
        :param Text: **[REQUIRED]** 
        
          A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Sentiment\': \'POSITIVE\'|\'NEGATIVE\'|\'NEUTRAL\'|\'MIXED\',
                \'SentimentScore\': {
                    \'Positive\': ...,
                    \'Negative\': ...,
                    \'Neutral\': ...,
                    \'Mixed\': ...
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Sentiment** *(string) --* 
        
              The inferred sentiment that Amazon Comprehend has the highest level of confidence in.
        
            - **SentimentScore** *(dict) --* 
        
              An object that lists the sentiments, and their corresponding confidence levels.
        
              - **Positive** *(float) --* 
        
                The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``POSITIVE`` sentiment.
        
              - **Negative** *(float) --* 
        
                The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``NEGATIVE`` sentiment.
        
              - **Neutral** *(float) --* 
        
                The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``NEUTRAL`` sentiment.
        
              - **Mixed** *(float) --* 
        
                The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``MIXED`` sentiment.
        
        """
        pass

    def detect_syntax(self, Text: str, LanguageCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectSyntax>`_
        
        **Request Syntax** 
        ::
        
          response = client.detect_syntax(
              Text=\'string\',
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\'
          )
        :type Text: string
        :param Text: **[REQUIRED]** 
        
          A UTF-8 string. Each string must contain fewer that 5,000 bytes of UTF encoded characters.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language code of the input documents. You can specify English (\"en\") or Spanish (\"es\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SyntaxTokens\': [
                    {
                        \'TokenId\': 123,
                        \'Text\': \'string\',
                        \'BeginOffset\': 123,
                        \'EndOffset\': 123,
                        \'PartOfSpeech\': {
                            \'Tag\': \'ADJ\'|\'ADP\'|\'ADV\'|\'AUX\'|\'CONJ\'|\'DET\'|\'INTJ\'|\'NOUN\'|\'NUM\'|\'O\'|\'PART\'|\'PRON\'|\'PROPN\'|\'PUNCT\'|\'SCONJ\'|\'SYM\'|\'VERB\',
                            \'Score\': ...
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SyntaxTokens** *(list) --* 
        
              A collection of syntax tokens describing the text. For each token, the response provides the text, the token type, where the text begins and ends, and the level of confidence that Amazon Comprehend has that the token is correct. For a list of token types, see  how-syntax .
        
              - *(dict) --* 
        
                Represents a work in the input text that was recognized and assigned a part of speech. There is one syntax token record for each word in the source text.
        
                - **TokenId** *(integer) --* 
        
                  A unique identifier for a token.
        
                - **Text** *(string) --* 
        
                  The word that was recognized in the source text.
        
                - **BeginOffset** *(integer) --* 
        
                  The zero-based offset from the beginning of the source text to the first character in the word.
        
                - **EndOffset** *(integer) --* 
        
                  The zero-based offset from the beginning of the source text to the last character in the word.
        
                - **PartOfSpeech** *(dict) --* 
        
                  Provides the part of speech label and the confidence level that Amazon Comprehend has that the part of speech was correctly identified. For more information, see  how-syntax .
        
                  - **Tag** *(string) --* 
        
                    Identifies the part of speech that the token represents.
        
                  - **Score** *(float) --* 
        
                    The confidence that Amazon Comprehend has that the part of speech was correctly identified.
        
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

    def list_dominant_language_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListDominantLanguageDetectionJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_dominant_language_detection_jobs(
              Filter={
                  \'JobName\': \'string\',
                  \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                  \'SubmitTimeBefore\': datetime(2015, 1, 1),
                  \'SubmitTimeAfter\': datetime(2015, 1, 1)
              },
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter: 
        
          Filters that jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
        
          - **JobName** *(string) --* 
        
            Filters on the name of the job.
        
          - **JobStatus** *(string) --* 
        
            Filters the list of jobs based on job status. Returns only jobs with the specified status.
        
          - **SubmitTimeBefore** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
        
          - **SubmitTimeAfter** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
        
        :type NextToken: string
        :param NextToken: 
        
          Identifies the next page of results to return.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in each page. The default is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DominantLanguageDetectionJobPropertiesList\': [
                    {
                        \'JobId\': \'string\',
                        \'JobName\': \'string\',
                        \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                        \'Message\': \'string\',
                        \'SubmitTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'InputDataConfig\': {
                            \'S3Uri\': \'string\',
                            \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                        },
                        \'OutputDataConfig\': {
                            \'S3Uri\': \'string\'
                        },
                        \'DataAccessRoleArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DominantLanguageDetectionJobPropertiesList** *(list) --* 
        
              A list containing the properties of each job that is returned.
        
              - *(dict) --* 
        
                Provides information about a dominant language detection job.
        
                - **JobId** *(string) --* 
        
                  The identifier assigned to the dominant language detection job.
        
                - **JobName** *(string) --* 
        
                  The name that you assigned to the dominant language detection job.
        
                - **JobStatus** *(string) --* 
        
                  The current status of the dominant language detection job. If the status is ``FAILED`` , the ``Message`` field shows the reason for the failure.
        
                - **Message** *(string) --* 
        
                  A description for the status of a job.
        
                - **SubmitTime** *(datetime) --* 
        
                  The time that the dominant language detection job was submitted for processing.
        
                - **EndTime** *(datetime) --* 
        
                  The time that the dominant language detection job completed.
        
                - **InputDataConfig** *(dict) --* 
        
                  The input data configuration that you supplied when you created the dominant language detection job.
        
                  - **S3Uri** *(string) --* 
        
                    The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                  - **InputFormat** *(string) --* 
        
                    Specifies how the text in an input file should be processed:
        
                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                     
                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                     
                - **OutputDataConfig** *(dict) --* 
        
                  The output data configuration that you supplied when you created the dominant language detection job.
        
                  - **S3Uri** *(string) --* 
        
                    When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                    When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
                - **DataAccessRoleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.
        
            - **NextToken** *(string) --* 
        
              Identifies the next page of results to return.
        
        """
        pass

    def list_entities_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListEntitiesDetectionJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_entities_detection_jobs(
              Filter={
                  \'JobName\': \'string\',
                  \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                  \'SubmitTimeBefore\': datetime(2015, 1, 1),
                  \'SubmitTimeAfter\': datetime(2015, 1, 1)
              },
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter: 
        
          Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
        
          - **JobName** *(string) --* 
        
            Filters on the name of the job.
        
          - **JobStatus** *(string) --* 
        
            Filters the list of jobs based on job status. Returns only jobs with the specified status.
        
          - **SubmitTimeBefore** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
        
          - **SubmitTimeAfter** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
        
        :type NextToken: string
        :param NextToken: 
        
          Identifies the next page of results to return.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in each page. The default is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EntitiesDetectionJobPropertiesList\': [
                    {
                        \'JobId\': \'string\',
                        \'JobName\': \'string\',
                        \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                        \'Message\': \'string\',
                        \'SubmitTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'InputDataConfig\': {
                            \'S3Uri\': \'string\',
                            \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                        },
                        \'OutputDataConfig\': {
                            \'S3Uri\': \'string\'
                        },
                        \'LanguageCode\': \'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
                        \'DataAccessRoleArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EntitiesDetectionJobPropertiesList** *(list) --* 
        
              A list containing the properties of each job that is returned.
        
              - *(dict) --* 
        
                Provides information about an entities detection job.
        
                - **JobId** *(string) --* 
        
                  The identifier assigned to the entities detection job.
        
                - **JobName** *(string) --* 
        
                  The name that you assigned the entities detection job.
        
                - **JobStatus** *(string) --* 
        
                  The current status of the entities detection job. If the status is ``FAILED`` , the ``Message`` field shows the reason for the failure.
        
                - **Message** *(string) --* 
        
                  A description of the status of a job.
        
                - **SubmitTime** *(datetime) --* 
        
                  The time that the entities detection job was submitted for processing.
        
                - **EndTime** *(datetime) --* 
        
                  The time that the entities detection job completed
        
                - **InputDataConfig** *(dict) --* 
        
                  The input data configuration that you supplied when you created the entities detection job.
        
                  - **S3Uri** *(string) --* 
        
                    The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                  - **InputFormat** *(string) --* 
        
                    Specifies how the text in an input file should be processed:
        
                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                     
                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                     
                - **OutputDataConfig** *(dict) --* 
        
                  The output data configuration that you supplied when you created the entities detection job. 
        
                  - **S3Uri** *(string) --* 
        
                    When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                    When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
                - **LanguageCode** *(string) --* 
        
                  The language code of the input documents.
        
                - **DataAccessRoleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.
        
            - **NextToken** *(string) --* 
        
              Identifies the next page of results to return.
        
        """
        pass

    def list_key_phrases_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListKeyPhrasesDetectionJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_key_phrases_detection_jobs(
              Filter={
                  \'JobName\': \'string\',
                  \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                  \'SubmitTimeBefore\': datetime(2015, 1, 1),
                  \'SubmitTimeAfter\': datetime(2015, 1, 1)
              },
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter: 
        
          Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
        
          - **JobName** *(string) --* 
        
            Filters on the name of the job.
        
          - **JobStatus** *(string) --* 
        
            Filters the list of jobs based on job status. Returns only jobs with the specified status.
        
          - **SubmitTimeBefore** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
        
          - **SubmitTimeAfter** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
        
        :type NextToken: string
        :param NextToken: 
        
          Identifies the next page of results to return.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in each page. The default is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyPhrasesDetectionJobPropertiesList\': [
                    {
                        \'JobId\': \'string\',
                        \'JobName\': \'string\',
                        \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                        \'Message\': \'string\',
                        \'SubmitTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'InputDataConfig\': {
                            \'S3Uri\': \'string\',
                            \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                        },
                        \'OutputDataConfig\': {
                            \'S3Uri\': \'string\'
                        },
                        \'LanguageCode\': \'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
                        \'DataAccessRoleArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyPhrasesDetectionJobPropertiesList** *(list) --* 
        
              A list containing the properties of each job that is returned.
        
              - *(dict) --* 
        
                Provides information about a key phrases detection job.
        
                - **JobId** *(string) --* 
        
                  The identifier assigned to the key phrases detection job.
        
                - **JobName** *(string) --* 
        
                  The name that you assigned the key phrases detection job.
        
                - **JobStatus** *(string) --* 
        
                  The current status of the key phrases detection job. If the status is ``FAILED`` , the ``Message`` field shows the reason for the failure.
        
                - **Message** *(string) --* 
        
                  A description of the status of a job.
        
                - **SubmitTime** *(datetime) --* 
        
                  The time that the key phrases detection job was submitted for processing.
        
                - **EndTime** *(datetime) --* 
        
                  The time that the key phrases detection job completed.
        
                - **InputDataConfig** *(dict) --* 
        
                  The input data configuration that you supplied when you created the key phrases detection job.
        
                  - **S3Uri** *(string) --* 
        
                    The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                  - **InputFormat** *(string) --* 
        
                    Specifies how the text in an input file should be processed:
        
                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                     
                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                     
                - **OutputDataConfig** *(dict) --* 
        
                  The output data configuration that you supplied when you created the key phrases detection job.
        
                  - **S3Uri** *(string) --* 
        
                    When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                    When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
                - **LanguageCode** *(string) --* 
        
                  The language code of the input documents.
        
                - **DataAccessRoleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.
        
            - **NextToken** *(string) --* 
        
              Identifies the next page of results to return.
        
        """
        pass

    def list_sentiment_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListSentimentDetectionJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_sentiment_detection_jobs(
              Filter={
                  \'JobName\': \'string\',
                  \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                  \'SubmitTimeBefore\': datetime(2015, 1, 1),
                  \'SubmitTimeAfter\': datetime(2015, 1, 1)
              },
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter: 
        
          Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
        
          - **JobName** *(string) --* 
        
            Filters on the name of the job.
        
          - **JobStatus** *(string) --* 
        
            Filters the list of jobs based on job status. Returns only jobs with the specified status.
        
          - **SubmitTimeBefore** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
        
          - **SubmitTimeAfter** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
        
        :type NextToken: string
        :param NextToken: 
        
          Identifies the next page of results to return.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in each page. The default is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SentimentDetectionJobPropertiesList\': [
                    {
                        \'JobId\': \'string\',
                        \'JobName\': \'string\',
                        \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                        \'Message\': \'string\',
                        \'SubmitTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'InputDataConfig\': {
                            \'S3Uri\': \'string\',
                            \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                        },
                        \'OutputDataConfig\': {
                            \'S3Uri\': \'string\'
                        },
                        \'LanguageCode\': \'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
                        \'DataAccessRoleArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SentimentDetectionJobPropertiesList** *(list) --* 
        
              A list containing the properties of each job that is returned.
        
              - *(dict) --* 
        
                Provides information about a sentiment detection job.
        
                - **JobId** *(string) --* 
        
                  The identifier assigned to the sentiment detection job.
        
                - **JobName** *(string) --* 
        
                  The name that you assigned to the sentiment detection job
        
                - **JobStatus** *(string) --* 
        
                  The current status of the sentiment detection job. If the status is ``FAILED`` , the ``Messages`` field shows the reason for the failure.
        
                - **Message** *(string) --* 
        
                  A description of the status of a job.
        
                - **SubmitTime** *(datetime) --* 
        
                  The time that the sentiment detection job was submitted for processing.
        
                - **EndTime** *(datetime) --* 
        
                  The time that the sentiment detection job ended.
        
                - **InputDataConfig** *(dict) --* 
        
                  The input data configuration that you supplied when you created the sentiment detection job.
        
                  - **S3Uri** *(string) --* 
        
                    The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                  - **InputFormat** *(string) --* 
        
                    Specifies how the text in an input file should be processed:
        
                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                     
                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                     
                - **OutputDataConfig** *(dict) --* 
        
                  The output data configuration that you supplied when you created the sentiment detection job.
        
                  - **S3Uri** *(string) --* 
        
                    When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                    When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
                - **LanguageCode** *(string) --* 
        
                  The language code of the input documents.
        
                - **DataAccessRoleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.
        
            - **NextToken** *(string) --* 
        
              Identifies the next page of results to return.
        
        """
        pass

    def list_topics_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListTopicsDetectionJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_topics_detection_jobs(
              Filter={
                  \'JobName\': \'string\',
                  \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                  \'SubmitTimeBefore\': datetime(2015, 1, 1),
                  \'SubmitTimeAfter\': datetime(2015, 1, 1)
              },
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter: 
        
          Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and time that they were submitted. You can set only one filter at a time.
        
          - **JobName** *(string) --* 
        
          - **JobStatus** *(string) --* 
        
            Filters the list of topic detection jobs based on job status. Returns only jobs with the specified status.
        
          - **SubmitTimeBefore** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.
        
          - **SubmitTimeAfter** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.
        
        :type NextToken: string
        :param NextToken: 
        
          Identifies the next page of results to return.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in each page. The default is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TopicsDetectionJobPropertiesList\': [
                    {
                        \'JobId\': \'string\',
                        \'JobName\': \'string\',
                        \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                        \'Message\': \'string\',
                        \'SubmitTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'InputDataConfig\': {
                            \'S3Uri\': \'string\',
                            \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                        },
                        \'OutputDataConfig\': {
                            \'S3Uri\': \'string\'
                        },
                        \'NumberOfTopics\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TopicsDetectionJobPropertiesList** *(list) --* 
        
              A list containing the properties of each job that is returned.
        
              - *(dict) --* 
        
                Provides information about a topic detection job.
        
                - **JobId** *(string) --* 
        
                  The identifier assigned to the topic detection job.
        
                - **JobName** *(string) --* 
        
                  The name of the topic detection job.
        
                - **JobStatus** *(string) --* 
        
                  The current status of the topic detection job. If the status is ``Failed`` , the reason for the failure is shown in the ``Message`` field.
        
                - **Message** *(string) --* 
        
                  A description for the status of a job.
        
                - **SubmitTime** *(datetime) --* 
        
                  The time that the topic detection job was submitted for processing.
        
                - **EndTime** *(datetime) --* 
        
                  The time that the topic detection job was completed.
        
                - **InputDataConfig** *(dict) --* 
        
                  The input data configuration supplied when you created the topic detection job.
        
                  - **S3Uri** *(string) --* 
        
                    The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                  - **InputFormat** *(string) --* 
        
                    Specifies how the text in an input file should be processed:
        
                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                     
                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                     
                - **OutputDataConfig** *(dict) --* 
        
                  The output data configuration supplied when you created the topic detection job.
        
                  - **S3Uri** *(string) --* 
        
                    When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                    When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
                - **NumberOfTopics** *(integer) --* 
        
                  The number of topics to detect supplied when you created the topic detection job. The default is 10. 
        
            - **NextToken** *(string) --* 
        
              Identifies the next page of results to return.
        
        """
        pass

    def start_dominant_language_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, JobName: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartDominantLanguageDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_dominant_language_detection_job(
              InputDataConfig={
                  \'S3Uri\': \'string\',
                  \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
              },
              OutputDataConfig={
                  \'S3Uri\': \'string\'
              },
              DataAccessRoleArn=\'string\',
              JobName=\'string\',
              ClientRequestToken=\'string\'
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]** 
        
          Specifies the format and location of the input data for the job.
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
          - **InputFormat** *(string) --* 
        
            Specifies how the text in an input file should be processed:
        
            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
             
            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
             
        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]** 
        
          Specifies where to send the output files.
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see `https\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__ .
        
        :type JobName: string
        :param JobName: 
        
          An identifier for the job.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier generated for the job. To get the status of a job, use this identifier with the operation.
        
            - **JobStatus** *(string) --* 
        
              The status of the job. 
        
              * SUBMITTED - The job has been received and is queued for processing. 
               
              * IN_PROGRESS - Amazon Comprehend is processing the job. 
               
              * COMPLETED - The job was successfully completed and the output is available. 
               
              * FAILED - The job did not complete. To get details, use the operation. 
               
        """
        pass

    def start_entities_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, LanguageCode: str, JobName: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartEntitiesDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_entities_detection_job(
              InputDataConfig={
                  \'S3Uri\': \'string\',
                  \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
              },
              OutputDataConfig={
                  \'S3Uri\': \'string\'
              },
              DataAccessRoleArn=\'string\',
              JobName=\'string\',
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
              ClientRequestToken=\'string\'
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]** 
        
          Specifies the format and location of the input data for the job.
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
          - **InputFormat** *(string) --* 
        
            Specifies how the text in an input file should be processed:
        
            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
             
            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
             
        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]** 
        
          Specifies where to send the output files.
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see `https\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__ .
        
        :type JobName: string
        :param JobName: 
        
          The identifier of the job.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for the request. If you don\'t set the client request token, Amazon Comprehend generates one.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier generated for the job. To get the status of job, use this identifier with the operation.
        
            - **JobStatus** *(string) --* 
        
              The status of the job. 
        
              * SUBMITTED - The job has been received and is queued for processing. 
               
              * IN_PROGRESS - Amazon Comprehend is processing the job. 
               
              * COMPLETED - The job was successfully completed and the output is available. 
               
              * FAILED - The job did not complete. To get details, use the operation. 
               
        """
        pass

    def start_key_phrases_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, LanguageCode: str, JobName: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartKeyPhrasesDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_key_phrases_detection_job(
              InputDataConfig={
                  \'S3Uri\': \'string\',
                  \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
              },
              OutputDataConfig={
                  \'S3Uri\': \'string\'
              },
              DataAccessRoleArn=\'string\',
              JobName=\'string\',
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
              ClientRequestToken=\'string\'
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]** 
        
          Specifies the format and location of the input data for the job.
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
          - **InputFormat** *(string) --* 
        
            Specifies how the text in an input file should be processed:
        
            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
             
            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
             
        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]** 
        
          Specifies where to send the output files.
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see `https\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__ .
        
        :type JobName: string
        :param JobName: 
        
          The identifier of the job.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for the request. If you don\'t set the client request token, Amazon Comprehend generates one.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier generated for the job. To get the status of a job, use this identifier with the operation.
        
            - **JobStatus** *(string) --* 
        
              The status of the job. 
        
              * SUBMITTED - The job has been received and is queued for processing. 
               
              * IN_PROGRESS - Amazon Comprehend is processing the job. 
               
              * COMPLETED - The job was successfully completed and the output is available. 
               
              * FAILED - The job did not complete. To get details, use the operation. 
               
        """
        pass

    def start_sentiment_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, LanguageCode: str, JobName: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartSentimentDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_sentiment_detection_job(
              InputDataConfig={
                  \'S3Uri\': \'string\',
                  \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
              },
              OutputDataConfig={
                  \'S3Uri\': \'string\'
              },
              DataAccessRoleArn=\'string\',
              JobName=\'string\',
              LanguageCode=\'en\'|\'es\'|\'fr\'|\'de\'|\'it\'|\'pt\',
              ClientRequestToken=\'string\'
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]** 
        
          Specifies the format and location of the input data for the job.
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
          - **InputFormat** *(string) --* 
        
            Specifies how the text in an input file should be processed:
        
            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
             
            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
             
        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]** 
        
          Specifies where to send the output files. 
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see `https\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__ .
        
        :type JobName: string
        :param JobName: 
        
          The identifier of the job.
        
        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]** 
        
          The language of the input documents. You can specify English (\"en\") or Spanish (\"es\"). All documents must be in the same language.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for the request. If you don\'t set the client request token, Amazon Comprehend generates one.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier generated for the job. To get the status of a job, use this identifier with the operation.
        
            - **JobStatus** *(string) --* 
        
              The status of the job. 
        
              * SUBMITTED - The job has been received and is queued for processing. 
               
              * IN_PROGRESS - Amazon Comprehend is processing the job. 
               
              * COMPLETED - The job was successfully completed and the output is available. 
               
              * FAILED - The job did not complete. To get details, use the operation. 
               
        """
        pass

    def start_topics_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, JobName: str = None, NumberOfTopics: int = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartTopicsDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_topics_detection_job(
              InputDataConfig={
                  \'S3Uri\': \'string\',
                  \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
              },
              OutputDataConfig={
                  \'S3Uri\': \'string\'
              },
              DataAccessRoleArn=\'string\',
              JobName=\'string\',
              NumberOfTopics=123,
              ClientRequestToken=\'string\'
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]** 
        
          Specifies the format and location of the input data for the job.
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
          - **InputFormat** *(string) --* 
        
            Specifies how the text in an input file should be processed:
        
            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
             
            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
             
        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]** 
        
          Specifies where to send the output files. The output is a compressed archive with two files, ``topic-terms.csv`` that lists the terms associated with each topic, and ``doc-topics.csv`` that lists the documents associated with each topic
        
          - **S3Uri** *(string) --* **[REQUIRED]** 
        
            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see `https\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__ .
        
        :type JobName: string
        :param JobName: 
        
          The identifier of the job.
        
        :type NumberOfTopics: integer
        :param NumberOfTopics: 
        
          The number of topics to detect.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier generated for the job. To get the status of the job, use this identifier with the ``DescribeTopicDetectionJob`` operation.
        
            - **JobStatus** *(string) --* 
        
              The status of the job: 
        
              * SUBMITTED - The job has been received and is queued for processing. 
               
              * IN_PROGRESS - Amazon Comprehend is processing the job. 
               
              * COMPLETED - The job was successfully completed and the output is available. 
               
              * FAILED - The job did not complete. To get details, use the ``DescribeTopicDetectionJob`` operation. 
               
        """
        pass

    def stop_dominant_language_detection_job(self, JobId: str) -> Dict:
        """
        
        If the job state is ``IN_PROGRESS`` the job is marked for termination and put into the ``STOP_REQUESTED`` state. If the job completes before it can be stopped, it is put into the ``COMPLETED`` state; otherwise the job is stopped and put into the ``STOPPED`` state.
        
        If the job is in the ``COMPLETED`` or ``FAILED`` state when you call the ``StopDominantLanguageDetectionJob`` operation, the operation returns a 400 Internal Request Exception. 
        
        When a job is stopped, any documents already processed are written to the output location.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopDominantLanguageDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_dominant_language_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier of the dominant language detection job to stop.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier of the dominant language detection job to stop.
        
            - **JobStatus** *(string) --* 
        
              Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job was previously stopped with the ``StopDominantLanguageDetectionJob`` operation.
        
        """
        pass

    def stop_entities_detection_job(self, JobId: str) -> Dict:
        """
        
        If the job state is ``IN_PROGRESS`` the job is marked for termination and put into the ``STOP_REQUESTED`` state. If the job completes before it can be stopped, it is put into the ``COMPLETED`` state; otherwise the job is stopped and put into the ``STOPPED`` state.
        
        If the job is in the ``COMPLETED`` or ``FAILED`` state when you call the ``StopDominantLanguageDetectionJob`` operation, the operation returns a 400 Internal Request Exception. 
        
        When a job is stopped, any documents already processed are written to the output location.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopEntitiesDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_entities_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier of the entities detection job to stop.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier of the entities detection job to stop.
        
            - **JobStatus** *(string) --* 
        
              Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job was previously stopped with the ``StopEntitiesDetectionJob`` operation.
        
        """
        pass

    def stop_key_phrases_detection_job(self, JobId: str) -> Dict:
        """
        
        If the job state is ``IN_PROGRESS`` the job is marked for termination and put into the ``STOP_REQUESTED`` state. If the job completes before it can be stopped, it is put into the ``COMPLETED`` state; otherwise the job is stopped and put into the ``STOPPED`` state.
        
        If the job is in the ``COMPLETED`` or ``FAILED`` state when you call the ``StopDominantLanguageDetectionJob`` operation, the operation returns a 400 Internal Request Exception. 
        
        When a job is stopped, any documents already processed are written to the output location.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopKeyPhrasesDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_key_phrases_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier of the key phrases detection job to stop.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier of the key phrases detection job to stop.
        
            - **JobStatus** *(string) --* 
        
              Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job was previously stopped with the ``StopKeyPhrasesDetectionJob`` operation.
        
        """
        pass

    def stop_sentiment_detection_job(self, JobId: str) -> Dict:
        """
        
        If the job state is ``IN_PROGRESS`` the job is marked for termination and put into the ``STOP_REQUESTED`` state. If the job completes before it can be stopped, it is put into the ``COMPLETED`` state; otherwise the job is be stopped and put into the ``STOPPED`` state.
        
        If the job is in the ``COMPLETED`` or ``FAILED`` state when you call the ``StopDominantLanguageDetectionJob`` operation, the operation returns a 400 Internal Request Exception. 
        
        When a job is stopped, any documents already processed are written to the output location.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopSentimentDetectionJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_sentiment_detection_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The identifier of the sentiment detection job to stop.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The identifier of the sentiment detection job to stop.
        
            - **JobStatus** *(string) --* 
        
              Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job was previously stopped with the ``StopSentimentDetectionJob`` operation.
        
        """
        pass
