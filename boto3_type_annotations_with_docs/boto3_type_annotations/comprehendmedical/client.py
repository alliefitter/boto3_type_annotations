from typing import Optional
from botocore.client import BaseClient
from botocore.waiter import Waiter
from typing import Union
from typing import Dict
from botocore.paginate import Paginator


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

    def detect_entities(self, Text: str) -> Dict:
        """
        Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DetectEntities>`_
        
        **Request Syntax**
        ::
          response = client.detect_entities(
              Text='string'
          )
        
        **Response Syntax**
        ::
            {
                'Entities': [
                    {
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Score': ...,
                        'Text': 'string',
                        'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                        'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ],
                        'Attributes': [
                            {
                                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                                'Score': ...,
                                'RelationshipScore': ...,
                                'Id': 123,
                                'BeginOffset': 123,
                                'EndOffset': 123,
                                'Text': 'string',
                                'Traits': [
                                    {
                                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                        'Score': ...
                                    },
                                ]
                            },
                        ]
                    },
                ],
                'UnmappedAttributes': [
                    {
                        'Type': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                        'Attribute': {
                            'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                            'Score': ...,
                            'RelationshipScore': ...,
                            'Id': 123,
                            'BeginOffset': 123,
                            'EndOffset': 123,
                            'Text': 'string',
                            'Traits': [
                                {
                                    'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                    'Score': ...
                                },
                            ]
                        }
                    },
                ],
                'PaginationToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Entities** *(list) --* 
              The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.
              - *(dict) --* 
                Provides information about an extracted medical entity.
                - **Id** *(integer) --* 
                  The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier. 
                - **BeginOffset** *(integer) --* 
                  The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string. 
                - **EndOffset** *(integer) --* 
                  The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string. 
                - **Score** *(float) --* 
                  The level of confidence that Comprehend Medical has in the accuracy of the detection.
                - **Text** *(string) --* 
                  The segment of input text extracted as this entity.
                - **Category** *(string) --* 
                  The category of the entity.
                - **Type** *(string) --* 
                  Describes the specific type of entity with category of entities. 
                - **Traits** *(list) --* 
                  Contextual information for the entity
                  - *(dict) --* 
                    Provides contextual information about the extracted entity. 
                    - **Name** *(string) --* 
                      Provides a name or contextual description about the trait. 
                    - **Score** *(float) --* 
                      The level of confidence that Comprehend Medical has in the accuracy of this trait.
                - **Attributes** *(list) --* 
                  The extracted attributes that relate to this entity.
                  - *(dict) --* 
                    An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken. It contains information about the attribute such as id, begin and end offset within the input text, and the segment of the input text. 
                    - **Type** *(string) --* 
                      The type of attribute. 
                    - **Score** *(float) --* 
                      The level of confidence that Comprehend Medical has that the segment of text is correctly recognized as an attribute. 
                    - **RelationshipScore** *(float) --* 
                      The level of confidence that Comprehend Medical has that this attribute is correctly related to this entity. 
                    - **Id** *(integer) --* 
                      The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier. 
                    - **BeginOffset** *(integer) --* 
                      The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string. 
                    - **EndOffset** *(integer) --* 
                      The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string. 
                    - **Text** *(string) --* 
                      The segment of input text extracted as this attribute.
                    - **Traits** *(list) --* 
                      Contextual information for this attribute. 
                      - *(dict) --* 
                        Provides contextual information about the extracted entity. 
                        - **Name** *(string) --* 
                          Provides a name or contextual description about the trait. 
                        - **Score** *(float) --* 
                          The level of confidence that Comprehend Medical has in the accuracy of this trait.
            - **UnmappedAttributes** *(list) --* 
              Attributes extracted from the input text that we were unable to relate to an entity.
              - *(dict) --* 
                An attribute that we extracted, but were unable to relate to an entity. 
                - **Type** *(string) --* 
                  The type of the attribute, could be one of the following values: "MEDICATION", "MEDICAL_CONDITION", "ANATOMY", "TEST_AND_TREATMENT_PROCEDURE" or "PERSONAL_HEALTH_INFORMATION". 
                - **Attribute** *(dict) --* 
                  The specific attribute that has been extracted but not mapped to an entity. 
                  - **Type** *(string) --* 
                    The type of attribute. 
                  - **Score** *(float) --* 
                    The level of confidence that Comprehend Medical has that the segment of text is correctly recognized as an attribute. 
                  - **RelationshipScore** *(float) --* 
                    The level of confidence that Comprehend Medical has that this attribute is correctly related to this entity. 
                  - **Id** *(integer) --* 
                    The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier. 
                  - **BeginOffset** *(integer) --* 
                    The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string. 
                  - **EndOffset** *(integer) --* 
                    The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string. 
                  - **Text** *(string) --* 
                    The segment of input text extracted as this attribute.
                  - **Traits** *(list) --* 
                    Contextual information for this attribute. 
                    - *(dict) --* 
                      Provides contextual information about the extracted entity. 
                      - **Name** *(string) --* 
                        Provides a name or contextual description about the trait. 
                      - **Score** *(float) --* 
                        The level of confidence that Comprehend Medical has in the accuracy of this trait.
            - **PaginationToken** *(string) --* 
              If the result of the previous request to DetectEntities was truncated, include the Paginationtoken to fetch the next page of entities.
        :type Text: string
        :param Text: **[REQUIRED]**
          A UTF-8 text string containing the clinical content being examined for entities. Each string must contain fewer than 20,000 bytes of characters.
        :rtype: dict
        :returns:
        """
        pass

    def detect_phi(self, Text: str) -> Dict:
        """
        Inspects the clinical text for personal health information (PHI) entities and entity category, location, and confidence score on that information.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DetectPHI>`_
        
        **Request Syntax**
        ::
          response = client.detect_phi(
              Text='string'
          )
        
        **Response Syntax**
        ::
            {
                'Entities': [
                    {
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Score': ...,
                        'Text': 'string',
                        'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                        'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ],
                        'Attributes': [
                            {
                                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                                'Score': ...,
                                'RelationshipScore': ...,
                                'Id': 123,
                                'BeginOffset': 123,
                                'EndOffset': 123,
                                'Text': 'string',
                                'Traits': [
                                    {
                                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                        'Score': ...
                                    },
                                ]
                            },
                        ]
                    },
                ],
                'PaginationToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Entities** *(list) --* 
              The collection of PHI entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Comprehend Medical has in its detection. 
              - *(dict) --* 
                Provides information about an extracted medical entity.
                - **Id** *(integer) --* 
                  The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier. 
                - **BeginOffset** *(integer) --* 
                  The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string. 
                - **EndOffset** *(integer) --* 
                  The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string. 
                - **Score** *(float) --* 
                  The level of confidence that Comprehend Medical has in the accuracy of the detection.
                - **Text** *(string) --* 
                  The segment of input text extracted as this entity.
                - **Category** *(string) --* 
                  The category of the entity.
                - **Type** *(string) --* 
                  Describes the specific type of entity with category of entities. 
                - **Traits** *(list) --* 
                  Contextual information for the entity
                  - *(dict) --* 
                    Provides contextual information about the extracted entity. 
                    - **Name** *(string) --* 
                      Provides a name or contextual description about the trait. 
                    - **Score** *(float) --* 
                      The level of confidence that Comprehend Medical has in the accuracy of this trait.
                - **Attributes** *(list) --* 
                  The extracted attributes that relate to this entity.
                  - *(dict) --* 
                    An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken. It contains information about the attribute such as id, begin and end offset within the input text, and the segment of the input text. 
                    - **Type** *(string) --* 
                      The type of attribute. 
                    - **Score** *(float) --* 
                      The level of confidence that Comprehend Medical has that the segment of text is correctly recognized as an attribute. 
                    - **RelationshipScore** *(float) --* 
                      The level of confidence that Comprehend Medical has that this attribute is correctly related to this entity. 
                    - **Id** *(integer) --* 
                      The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier. 
                    - **BeginOffset** *(integer) --* 
                      The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string. 
                    - **EndOffset** *(integer) --* 
                      The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string. 
                    - **Text** *(string) --* 
                      The segment of input text extracted as this attribute.
                    - **Traits** *(list) --* 
                      Contextual information for this attribute. 
                      - *(dict) --* 
                        Provides contextual information about the extracted entity. 
                        - **Name** *(string) --* 
                          Provides a name or contextual description about the trait. 
                        - **Score** *(float) --* 
                          The level of confidence that Comprehend Medical has in the accuracy of this trait.
            - **PaginationToken** *(string) --* 
              If the result of the previous request to DetectPHI was truncated, include the Paginationtoken to fetch the next page of PHI entities. 
        :type Text: string
        :param Text: **[REQUIRED]**
          A UTF-8 text string containing the clinical content being examined for PHI entities. Each string must contain fewer than 20,000 bytes of characters.
        :rtype: dict
        :returns:
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
