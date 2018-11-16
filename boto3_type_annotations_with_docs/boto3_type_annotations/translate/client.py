from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def translate_text(self, Text: str, SourceLanguageCode: str, TargetLanguageCode: str) -> Dict:
        """
        
        * Arabic (ar) 
         
        * Chinese (Simplified) (zh) 
         
        * French (fr) 
         
        * German (de) 
         
        * Portuguese (pt) 
         
        * Spanish (es) 
         
        To have Amazon Translate determine the source language of your text, you can specify ``auto`` in the ``SourceLanguageCode`` field. If you specify ``auto`` , Amazon Translate will call Amazon Comprehend to determine the source language.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/TranslateText>`_
        
        **Request Syntax** 
        ::
        
          response = client.translate_text(
              Text=\'string\',
              SourceLanguageCode=\'string\',
              TargetLanguageCode=\'string\'
          )
        :type Text: string
        :param Text: **[REQUIRED]** 
        
          The text to translate.
        
        :type SourceLanguageCode: string
        :param SourceLanguageCode: **[REQUIRED]** 
        
          One of the supported language codes for the source text. If the ``TargetLanguageCode`` is not \"en\", the ``SourceLanguageCode`` must be \"en\".
        
          To have Amazon Translate determine the source language of your text, you can specify ``auto`` in the ``SourceLanguageCode`` field. If you specify ``auto`` , Amazon Translate will call Amazon Comprehend to determine the source language.
        
        :type TargetLanguageCode: string
        :param TargetLanguageCode: **[REQUIRED]** 
        
          One of the supported language codes for the target text. If the ``SourceLanguageCode`` is not \"en\", the ``TargetLanguageCode`` must be \"en\".
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TranslatedText\': \'string\',
                \'SourceLanguageCode\': \'string\',
                \'TargetLanguageCode\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TranslatedText** *(string) --* 
        
              The text translated into the target language.
        
            - **SourceLanguageCode** *(string) --* 
        
              The language code for the language of the input text. 
        
            - **TargetLanguageCode** *(string) --* 
        
              The language code for the language of the translated text. 
        
        """
        pass
