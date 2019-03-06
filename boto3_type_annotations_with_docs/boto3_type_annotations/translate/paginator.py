from typing import Dict
from botocore.paginate import Paginator


class ListTerminologies(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Translate.Client.list_terminologies`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/ListTerminologies>`_
        
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
