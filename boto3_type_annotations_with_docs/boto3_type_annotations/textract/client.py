from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def analyze_document(self, Document: Dict, FeatureTypes: List) -> Dict:
        """
        Analyzes an input document for relationships between detected items. 
        The types of information returned are as follows: 
        * Words and lines that are related to nearby lines and words. The related information is returned in two  Block objects each of type ``KEY_VALUE_SET`` : a KEY Block object and a VALUE Block object. For example, *Name: Ana Silva Carolina* contains a key and value. *Name:* is the key. *Ana Silva Carolina* is the value. 
        * Table and table cell data. A TABLE Block object contains information about a detected table. A CELL Block object is returned for each cell in a table. 
        * Selectable elements such as checkboxes and radio buttons. A SELECTION_ELEMENT Block object contains information about a selectable element. 
        * Lines and words of text. A LINE Block object contains one or more WORD Block objects. 
        You can choose which type of analysis to perform by specifying the ``FeatureTypes`` list. 
        The output is returned in a list of ``BLOCK`` objects.
         ``AnalyzeDocument`` is a synchronous operation. To analyze documents asynchronously, use  StartDocumentAnalysis .
        For more information, see `Document Text Analysis <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/AnalyzeDocument>`_
        
        **Request Syntax**
        ::
          response = client.analyze_document(
              Document={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              FeatureTypes=[
                  'TABLES'|'FORMS',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DocumentMetadata': {
                    'Pages': 123
                },
                'Blocks': [
                    {
                        'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
                        'Confidence': ...,
                        'Text': 'string',
                        'RowIndex': 123,
                        'ColumnIndex': 123,
                        'RowSpan': 123,
                        'ColumnSpan': 123,
                        'Geometry': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Polygon': [
                                {
                                    'X': ...,
                                    'Y': ...
                                },
                            ]
                        },
                        'Id': 'string',
                        'Relationships': [
                            {
                                'Type': 'VALUE'|'CHILD',
                                'Ids': [
                                    'string',
                                ]
                            },
                        ],
                        'EntityTypes': [
                            'KEY'|'VALUE',
                        ],
                        'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
                        'Page': 123
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DocumentMetadata** *(dict) --* 
              Metadata about the analyzed document. An example is the number of pages.
              - **Pages** *(integer) --* 
                The number of pages detected in the document.
            - **Blocks** *(list) --* 
              The text that's detected and analyzed by ``AnalyzeDocument`` .
              - *(dict) --* 
                A ``Block`` represents items that are recognized in a document within a group of pixels close to each other. The information returned in a ``Block`` depends on the type of operation. In document-text detection (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables and selection elements that are detected in the document.
                An array of ``Block`` objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.
                For more information, see `How Amazon Textract Works <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .
                - **BlockType** *(string) --* 
                  The type of text that's recognized in a block. In text-detection operations, the following types are returned:
                  * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page. 
                  * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces. 
                  * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page. 
                  In text analysis operations, the following types are returned:
                  * *PAGE* - Contains a list of child Block objects that are detected on a document page. 
                  * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.  
                  * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces that's detected on a document page. 
                  * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page. 
                  * *TABLE* - A table that's detected on a document page. A table is any grid-based information with 2 or more rows or columns with a cell span of 1 row and 1 column each.  
                  * *CELL* - A cell within a detected table. The cell is the parent of the block that contains the text in the cell. 
                  * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's detected on a document page. Use the value of ``SelectionStatus`` to determine the status of the selection element. 
                - **Confidence** *(float) --* 
                  The confidence that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.
                - **Text** *(string) --* 
                  The word or line of text that's recognized by Amazon Textract. 
                - **RowIndex** *(integer) --* 
                  The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **ColumnIndex** *(integer) --* 
                  The column in which a table cell appears. The first column position is 1. ``ColumnIndex`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **RowSpan** *(integer) --* 
                  The number of rows that a table spans. ``RowSpan`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **ColumnSpan** *(integer) --* 
                  The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` . 
                - **Geometry** *(dict) --* 
                  The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information. 
                  - **BoundingBox** *(dict) --* 
                    An axis-aligned coarse representation of the location of the recognized text on the document page.
                    - **Width** *(float) --* 
                      The width of the bounding box as a ratio of the overall document page width.
                    - **Height** *(float) --* 
                      The height of the bounding box as a ratio of the overall document page height.
                    - **Left** *(float) --* 
                      The left coordinate of the bounding box as a ratio of overall document page width.
                    - **Top** *(float) --* 
                      The top coordinate of the bounding box as a ratio of overall document page height.
                  - **Polygon** *(list) --* 
                    Within the bounding box, a fine-grained polygon around the recognized text.
                    - *(dict) --* 
                      The X and Y coordinates of a point on a document page. The X and Y values returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.
                      An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText . ``Polygon`` represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide. 
                      - **X** *(float) --* 
                        The value of the X coordinate for a point on a ``Polygon`` .
                      - **Y** *(float) --* 
                        The value of the Y coordinate for a point on a ``Polygon`` .
                - **Id** *(string) --* 
                  The identifier for the recognized text. The identifier is only unique for a single operation. 
                - **Relationships** *(list) --* 
                  A list of child blocks of the current block. For example a LINE object has child blocks for each WORD block that's part of the line of text. There aren't Relationship objects in the list for relationships that don't exist, such as when the current block has no child blocks. The list size can be the following:
                  * 0 - The block has no child blocks. 
                  * 1 - The block has child blocks. 
                  - *(dict) --* 
                    Information about how blocks are related to each other. A ``Block`` object contains 0 or more ``Relation`` objects in a list, ``Relationships`` . For more information, see  Block .
                    The ``Type`` element provides the type of the relationship for all blocks in the ``IDs`` array. 
                    - **Type** *(string) --* 
                      The type of relationship that the blocks in the IDs array have with the current block. The relationship can be ``VALUE`` or ``CHILD`` .
                    - **Ids** *(list) --* 
                      An array of IDs for related blocks. You can get the type of the relationship from the ``Type`` element.
                      - *(string) --* 
                - **EntityTypes** *(list) --* 
                  The type of entity. The following can be returned:
                  * *KEY* - An identifier for a field on the document. 
                  * *VALUE* - The field text. 
                   ``EntityTypes`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                  - *(string) --* 
                - **SelectionStatus** *(string) --* 
                  The selection status of a selectable element such as a radio button or checkbox. 
                - **Page** *(integer) --* 
                  The page in which a block was detected. ``Page`` is returned by asynchronous operations. Page values greater than 1 are only returned for multi-page documents that are in PDF format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always considered to be a single-page document and the value of ``Page`` is always 1. Synchronous operations don't return ``Page`` as every input document is considered to be a single-page document.
        :type Document: dict
        :param Document: **[REQUIRED]**
          The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can\'t pass image bytes. The document must be an image in JPG or PNG format.
          If you are using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the ``Bytes`` field.
          - **Bytes** *(bytes) --*
            A blob of base-64 encoded documents bytes. The maximum size of a document that\'s provided in a blob of bytes is 5 MB. The document bytes must be in PNG or JPG format.
            If you are using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the ``Bytes`` field.
          - **S3Object** *(dict) --*
            Identifies an S3 object as the document source. The maximum size of a document stored in an S3 bucket is 5 MB.
            - **Bucket** *(string) --*
              The name of the S3 bucket.
            - **Name** *(string) --*
              The file name of the input document. It must be an image file (.JPG or .PNG format). Asynchronous operations also support PDF files.
            - **Version** *(string) --*
              If the bucket has versioning enabled, you can specify the object version.
        :type FeatureTypes: list
        :param FeatureTypes: **[REQUIRED]**
          A list of the types of analysis to perform. Add TABLES to the list to return information about the tables detected in the input document. Add FORMS to return detected fields and the associated text. To perform both types of analysis, add TABLES and FORMS to ``FeatureTypes`` .
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

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

    def detect_document_text(self, Document: Dict) -> Dict:
        """
        Detects text in the input document. Amazon Textract can detect lines of text and the words that make up a line of text. The input document must be an image in JPG or PNG format. ``DetectDocumentText`` returns the detected text in an array of  Block objects. 
        Each document page has as an associated ``Block`` of type PAGE. Each PAGE ``Block`` object is the parent of LINE ``Block`` objects that represent the lines of detected text on a page. A LINE ``Block`` object is a parent for each word that makes up the line. Words are represented by ``Block`` objects of type WORD.
         ``DetectDocumentText`` is a synchronous operation. To analyze documents asynchronously, use  StartDocumentTextDetection .
        For more information, see `Document Text Detection <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/DetectDocumentText>`_
        
        **Request Syntax**
        ::
          response = client.detect_document_text(
              Document={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'DocumentMetadata': {
                    'Pages': 123
                },
                'Blocks': [
                    {
                        'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
                        'Confidence': ...,
                        'Text': 'string',
                        'RowIndex': 123,
                        'ColumnIndex': 123,
                        'RowSpan': 123,
                        'ColumnSpan': 123,
                        'Geometry': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Polygon': [
                                {
                                    'X': ...,
                                    'Y': ...
                                },
                            ]
                        },
                        'Id': 'string',
                        'Relationships': [
                            {
                                'Type': 'VALUE'|'CHILD',
                                'Ids': [
                                    'string',
                                ]
                            },
                        ],
                        'EntityTypes': [
                            'KEY'|'VALUE',
                        ],
                        'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
                        'Page': 123
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DocumentMetadata** *(dict) --* 
              Metadata about the document. Contains the number of pages that are detected in the document.
              - **Pages** *(integer) --* 
                The number of pages detected in the document.
            - **Blocks** *(list) --* 
              An array of Block objects containing the text detected in the document.
              - *(dict) --* 
                A ``Block`` represents items that are recognized in a document within a group of pixels close to each other. The information returned in a ``Block`` depends on the type of operation. In document-text detection (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables and selection elements that are detected in the document.
                An array of ``Block`` objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.
                For more information, see `How Amazon Textract Works <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .
                - **BlockType** *(string) --* 
                  The type of text that's recognized in a block. In text-detection operations, the following types are returned:
                  * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page. 
                  * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces. 
                  * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page. 
                  In text analysis operations, the following types are returned:
                  * *PAGE* - Contains a list of child Block objects that are detected on a document page. 
                  * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.  
                  * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces that's detected on a document page. 
                  * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page. 
                  * *TABLE* - A table that's detected on a document page. A table is any grid-based information with 2 or more rows or columns with a cell span of 1 row and 1 column each.  
                  * *CELL* - A cell within a detected table. The cell is the parent of the block that contains the text in the cell. 
                  * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's detected on a document page. Use the value of ``SelectionStatus`` to determine the status of the selection element. 
                - **Confidence** *(float) --* 
                  The confidence that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.
                - **Text** *(string) --* 
                  The word or line of text that's recognized by Amazon Textract. 
                - **RowIndex** *(integer) --* 
                  The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **ColumnIndex** *(integer) --* 
                  The column in which a table cell appears. The first column position is 1. ``ColumnIndex`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **RowSpan** *(integer) --* 
                  The number of rows that a table spans. ``RowSpan`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **ColumnSpan** *(integer) --* 
                  The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` . 
                - **Geometry** *(dict) --* 
                  The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information. 
                  - **BoundingBox** *(dict) --* 
                    An axis-aligned coarse representation of the location of the recognized text on the document page.
                    - **Width** *(float) --* 
                      The width of the bounding box as a ratio of the overall document page width.
                    - **Height** *(float) --* 
                      The height of the bounding box as a ratio of the overall document page height.
                    - **Left** *(float) --* 
                      The left coordinate of the bounding box as a ratio of overall document page width.
                    - **Top** *(float) --* 
                      The top coordinate of the bounding box as a ratio of overall document page height.
                  - **Polygon** *(list) --* 
                    Within the bounding box, a fine-grained polygon around the recognized text.
                    - *(dict) --* 
                      The X and Y coordinates of a point on a document page. The X and Y values returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.
                      An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText . ``Polygon`` represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide. 
                      - **X** *(float) --* 
                        The value of the X coordinate for a point on a ``Polygon`` .
                      - **Y** *(float) --* 
                        The value of the Y coordinate for a point on a ``Polygon`` .
                - **Id** *(string) --* 
                  The identifier for the recognized text. The identifier is only unique for a single operation. 
                - **Relationships** *(list) --* 
                  A list of child blocks of the current block. For example a LINE object has child blocks for each WORD block that's part of the line of text. There aren't Relationship objects in the list for relationships that don't exist, such as when the current block has no child blocks. The list size can be the following:
                  * 0 - The block has no child blocks. 
                  * 1 - The block has child blocks. 
                  - *(dict) --* 
                    Information about how blocks are related to each other. A ``Block`` object contains 0 or more ``Relation`` objects in a list, ``Relationships`` . For more information, see  Block .
                    The ``Type`` element provides the type of the relationship for all blocks in the ``IDs`` array. 
                    - **Type** *(string) --* 
                      The type of relationship that the blocks in the IDs array have with the current block. The relationship can be ``VALUE`` or ``CHILD`` .
                    - **Ids** *(list) --* 
                      An array of IDs for related blocks. You can get the type of the relationship from the ``Type`` element.
                      - *(string) --* 
                - **EntityTypes** *(list) --* 
                  The type of entity. The following can be returned:
                  * *KEY* - An identifier for a field on the document. 
                  * *VALUE* - The field text. 
                   ``EntityTypes`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                  - *(string) --* 
                - **SelectionStatus** *(string) --* 
                  The selection status of a selectable element such as a radio button or checkbox. 
                - **Page** *(integer) --* 
                  The page in which a block was detected. ``Page`` is returned by asynchronous operations. Page values greater than 1 are only returned for multi-page documents that are in PDF format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always considered to be a single-page document and the value of ``Page`` is always 1. Synchronous operations don't return ``Page`` as every input document is considered to be a single-page document.
        :type Document: dict
        :param Document: **[REQUIRED]**
          The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can\'t pass image bytes. The document must be an image in JPG or PNG format.
          If you are using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the ``Bytes`` field.
          - **Bytes** *(bytes) --*
            A blob of base-64 encoded documents bytes. The maximum size of a document that\'s provided in a blob of bytes is 5 MB. The document bytes must be in PNG or JPG format.
            If you are using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the ``Bytes`` field.
          - **S3Object** *(dict) --*
            Identifies an S3 object as the document source. The maximum size of a document stored in an S3 bucket is 5 MB.
            - **Bucket** *(string) --*
              The name of the S3 bucket.
            - **Name** *(string) --*
              The file name of the input document. It must be an image file (.JPG or .PNG format). Asynchronous operations also support PDF files.
            - **Version** *(string) --*
              If the bucket has versioning enabled, you can specify the object version.
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

    def get_document_analysis(self, JobId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Gets the results for an Amazon Textract asynchronous operation that analyzes text in a document.
        You start asynchronous text analysis by calling  StartDocumentAnalysis , which returns a job identifier (``JobId`` ). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to ``StartDocumentAnalysis`` . To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call ``GetDocumentAnalysis`` , and pass the job identifier (``JobId`` ) from the initial call to ``StartDocumentAnalysis`` .
         ``GetDocumentAnalysis`` returns an array of  Block objects. The following types of information are returned: 
        * Words and lines that are related to nearby lines and words. The related information is returned in two  Block objects each of type ``KEY_VALUE_SET`` : a KEY Block object and a VALUE Block object. For example, *Name: Ana Silva Carolina* contains a key and value. *Name:* is the key. *Ana Silva Carolina* is the value. 
        * Table and table cell data. A TABLE Block object contains information about a detected table. A CELL Block object is returned for each cell in a table. 
        * Selectable elements such as checkboxes and radio buttons. A SELECTION_ELEMENT Block object contains information about a selectable element. 
        * Lines and words of text. A LINE Block object contains one or more WORD Block objects. 
        Use the ``MaxResults`` parameter to limit the number of blocks returned. If there are more results than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call ``GetDocumentAnalysis`` , and populate the ``NextToken`` request parameter with the token value that's returned from the previous call to ``GetDocumentAnalysis`` .
        For more information, see `Document Text Analysis <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/GetDocumentAnalysis>`_
        
        **Request Syntax**
        ::
          response = client.get_document_analysis(
              JobId='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'DocumentMetadata': {
                    'Pages': 123
                },
                'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'PARTIAL_SUCCESS',
                'NextToken': 'string',
                'Blocks': [
                    {
                        'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
                        'Confidence': ...,
                        'Text': 'string',
                        'RowIndex': 123,
                        'ColumnIndex': 123,
                        'RowSpan': 123,
                        'ColumnSpan': 123,
                        'Geometry': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Polygon': [
                                {
                                    'X': ...,
                                    'Y': ...
                                },
                            ]
                        },
                        'Id': 'string',
                        'Relationships': [
                            {
                                'Type': 'VALUE'|'CHILD',
                                'Ids': [
                                    'string',
                                ]
                            },
                        ],
                        'EntityTypes': [
                            'KEY'|'VALUE',
                        ],
                        'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
                        'Page': 123
                    },
                ],
                'Warnings': [
                    {
                        'ErrorCode': 'string',
                        'Pages': [
                            123,
                        ]
                    },
                ],
                'StatusMessage': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DocumentMetadata** *(dict) --* 
              Information about a document that Amazon Textract processed. ``DocumentMetadata`` is returned in every page of paginated responses from an Amazon Textract video operation.
              - **Pages** *(integer) --* 
                The number of pages detected in the document.
            - **JobStatus** *(string) --* 
              The current status of the text detection job.
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon Textract returns this token. You can use this token in the subsequent request to retrieve the next set of text detection results.
            - **Blocks** *(list) --* 
              The results of the text analysis operation.
              - *(dict) --* 
                A ``Block`` represents items that are recognized in a document within a group of pixels close to each other. The information returned in a ``Block`` depends on the type of operation. In document-text detection (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables and selection elements that are detected in the document.
                An array of ``Block`` objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.
                For more information, see `How Amazon Textract Works <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .
                - **BlockType** *(string) --* 
                  The type of text that's recognized in a block. In text-detection operations, the following types are returned:
                  * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page. 
                  * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces. 
                  * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page. 
                  In text analysis operations, the following types are returned:
                  * *PAGE* - Contains a list of child Block objects that are detected on a document page. 
                  * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.  
                  * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces that's detected on a document page. 
                  * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page. 
                  * *TABLE* - A table that's detected on a document page. A table is any grid-based information with 2 or more rows or columns with a cell span of 1 row and 1 column each.  
                  * *CELL* - A cell within a detected table. The cell is the parent of the block that contains the text in the cell. 
                  * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's detected on a document page. Use the value of ``SelectionStatus`` to determine the status of the selection element. 
                - **Confidence** *(float) --* 
                  The confidence that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.
                - **Text** *(string) --* 
                  The word or line of text that's recognized by Amazon Textract. 
                - **RowIndex** *(integer) --* 
                  The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **ColumnIndex** *(integer) --* 
                  The column in which a table cell appears. The first column position is 1. ``ColumnIndex`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **RowSpan** *(integer) --* 
                  The number of rows that a table spans. ``RowSpan`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **ColumnSpan** *(integer) --* 
                  The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` . 
                - **Geometry** *(dict) --* 
                  The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information. 
                  - **BoundingBox** *(dict) --* 
                    An axis-aligned coarse representation of the location of the recognized text on the document page.
                    - **Width** *(float) --* 
                      The width of the bounding box as a ratio of the overall document page width.
                    - **Height** *(float) --* 
                      The height of the bounding box as a ratio of the overall document page height.
                    - **Left** *(float) --* 
                      The left coordinate of the bounding box as a ratio of overall document page width.
                    - **Top** *(float) --* 
                      The top coordinate of the bounding box as a ratio of overall document page height.
                  - **Polygon** *(list) --* 
                    Within the bounding box, a fine-grained polygon around the recognized text.
                    - *(dict) --* 
                      The X and Y coordinates of a point on a document page. The X and Y values returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.
                      An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText . ``Polygon`` represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide. 
                      - **X** *(float) --* 
                        The value of the X coordinate for a point on a ``Polygon`` .
                      - **Y** *(float) --* 
                        The value of the Y coordinate for a point on a ``Polygon`` .
                - **Id** *(string) --* 
                  The identifier for the recognized text. The identifier is only unique for a single operation. 
                - **Relationships** *(list) --* 
                  A list of child blocks of the current block. For example a LINE object has child blocks for each WORD block that's part of the line of text. There aren't Relationship objects in the list for relationships that don't exist, such as when the current block has no child blocks. The list size can be the following:
                  * 0 - The block has no child blocks. 
                  * 1 - The block has child blocks. 
                  - *(dict) --* 
                    Information about how blocks are related to each other. A ``Block`` object contains 0 or more ``Relation`` objects in a list, ``Relationships`` . For more information, see  Block .
                    The ``Type`` element provides the type of the relationship for all blocks in the ``IDs`` array. 
                    - **Type** *(string) --* 
                      The type of relationship that the blocks in the IDs array have with the current block. The relationship can be ``VALUE`` or ``CHILD`` .
                    - **Ids** *(list) --* 
                      An array of IDs for related blocks. You can get the type of the relationship from the ``Type`` element.
                      - *(string) --* 
                - **EntityTypes** *(list) --* 
                  The type of entity. The following can be returned:
                  * *KEY* - An identifier for a field on the document. 
                  * *VALUE* - The field text. 
                   ``EntityTypes`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                  - *(string) --* 
                - **SelectionStatus** *(string) --* 
                  The selection status of a selectable element such as a radio button or checkbox. 
                - **Page** *(integer) --* 
                  The page in which a block was detected. ``Page`` is returned by asynchronous operations. Page values greater than 1 are only returned for multi-page documents that are in PDF format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always considered to be a single-page document and the value of ``Page`` is always 1. Synchronous operations don't return ``Page`` as every input document is considered to be a single-page document.
            - **Warnings** *(list) --* 
              A list of warnings that occurred during the document analysis operation.
              - *(dict) --* 
                A warning about an issue that occurred during asynchronous text analysis ( StartDocumentAnalysis ) or asynchronous document-text detection ( StartDocumentTextDetection ). 
                - **ErrorCode** *(string) --* 
                  The error code for the warning.
                - **Pages** *(list) --* 
                  A list of the pages that the warning applies to.
                  - *(integer) --* 
            - **StatusMessage** *(string) --* 
              The current status of an asynchronous document analysis operation.
        :type JobId: string
        :param JobId: **[REQUIRED]**
          A unique identifier for the text-detection job. The ``JobId`` is returned from ``StartDocumentAnalysis`` .
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return per paginated call. The largest value that you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.
        :type NextToken: string
        :param NextToken:
          If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.
        :rtype: dict
        :returns:
        """
        pass

    def get_document_text_detection(self, JobId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Gets the results for an Amazon Textract asynchronous operation that detects text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.
        You start asynchronous text detection by calling  StartDocumentTextDetection , which returns a job identifier (``JobId`` ). When the text detection operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to ``StartDocumentTextDetection`` . To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call ``GetDocumentTextDetection`` , and pass the job identifier (``JobId`` ) from the initial call to ``StartDocumentTextDetection`` .
         ``GetDocumentTextDetection`` returns an array of  Block objects. 
        Each document page has as an associated ``Block`` of type PAGE. Each PAGE ``Block`` object is the parent of LINE ``Block`` objects that represent the lines of detected text on a page. A LINE ``Block`` object is a parent for each word that makes up the line. Words are represented by ``Block`` objects of type WORD.
        Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call ``GetDocumentTextDetection`` , and populate the ``NextToken`` request parameter with the token value that's returned from the previous call to ``GetDocumentTextDetection`` .
        For more information, see `Document Text Detection <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/GetDocumentTextDetection>`_
        
        **Request Syntax**
        ::
          response = client.get_document_text_detection(
              JobId='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'DocumentMetadata': {
                    'Pages': 123
                },
                'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'PARTIAL_SUCCESS',
                'NextToken': 'string',
                'Blocks': [
                    {
                        'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
                        'Confidence': ...,
                        'Text': 'string',
                        'RowIndex': 123,
                        'ColumnIndex': 123,
                        'RowSpan': 123,
                        'ColumnSpan': 123,
                        'Geometry': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Polygon': [
                                {
                                    'X': ...,
                                    'Y': ...
                                },
                            ]
                        },
                        'Id': 'string',
                        'Relationships': [
                            {
                                'Type': 'VALUE'|'CHILD',
                                'Ids': [
                                    'string',
                                ]
                            },
                        ],
                        'EntityTypes': [
                            'KEY'|'VALUE',
                        ],
                        'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
                        'Page': 123
                    },
                ],
                'Warnings': [
                    {
                        'ErrorCode': 'string',
                        'Pages': [
                            123,
                        ]
                    },
                ],
                'StatusMessage': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DocumentMetadata** *(dict) --* 
              Information about a document that Amazon Textract processed. ``DocumentMetadata`` is returned in every page of paginated responses from an Amazon Textract video operation.
              - **Pages** *(integer) --* 
                The number of pages detected in the document.
            - **JobStatus** *(string) --* 
              The current status of the text detection job.
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon Textract returns this token. You can use this token in the subsequent request to retrieve the next set of text-detection results.
            - **Blocks** *(list) --* 
              The results of the text-detection operation.
              - *(dict) --* 
                A ``Block`` represents items that are recognized in a document within a group of pixels close to each other. The information returned in a ``Block`` depends on the type of operation. In document-text detection (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables and selection elements that are detected in the document.
                An array of ``Block`` objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.
                For more information, see `How Amazon Textract Works <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .
                - **BlockType** *(string) --* 
                  The type of text that's recognized in a block. In text-detection operations, the following types are returned:
                  * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page. 
                  * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces. 
                  * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page. 
                  In text analysis operations, the following types are returned:
                  * *PAGE* - Contains a list of child Block objects that are detected on a document page. 
                  * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.  
                  * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren't separated by spaces that's detected on a document page. 
                  * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page. 
                  * *TABLE* - A table that's detected on a document page. A table is any grid-based information with 2 or more rows or columns with a cell span of 1 row and 1 column each.  
                  * *CELL* - A cell within a detected table. The cell is the parent of the block that contains the text in the cell. 
                  * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's detected on a document page. Use the value of ``SelectionStatus`` to determine the status of the selection element. 
                - **Confidence** *(float) --* 
                  The confidence that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.
                - **Text** *(string) --* 
                  The word or line of text that's recognized by Amazon Textract. 
                - **RowIndex** *(integer) --* 
                  The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **ColumnIndex** *(integer) --* 
                  The column in which a table cell appears. The first column position is 1. ``ColumnIndex`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **RowSpan** *(integer) --* 
                  The number of rows that a table spans. ``RowSpan`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                - **ColumnSpan** *(integer) --* 
                  The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` . 
                - **Geometry** *(dict) --* 
                  The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information. 
                  - **BoundingBox** *(dict) --* 
                    An axis-aligned coarse representation of the location of the recognized text on the document page.
                    - **Width** *(float) --* 
                      The width of the bounding box as a ratio of the overall document page width.
                    - **Height** *(float) --* 
                      The height of the bounding box as a ratio of the overall document page height.
                    - **Left** *(float) --* 
                      The left coordinate of the bounding box as a ratio of overall document page width.
                    - **Top** *(float) --* 
                      The top coordinate of the bounding box as a ratio of overall document page height.
                  - **Polygon** *(list) --* 
                    Within the bounding box, a fine-grained polygon around the recognized text.
                    - *(dict) --* 
                      The X and Y coordinates of a point on a document page. The X and Y values returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.
                      An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText . ``Polygon`` represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide. 
                      - **X** *(float) --* 
                        The value of the X coordinate for a point on a ``Polygon`` .
                      - **Y** *(float) --* 
                        The value of the Y coordinate for a point on a ``Polygon`` .
                - **Id** *(string) --* 
                  The identifier for the recognized text. The identifier is only unique for a single operation. 
                - **Relationships** *(list) --* 
                  A list of child blocks of the current block. For example a LINE object has child blocks for each WORD block that's part of the line of text. There aren't Relationship objects in the list for relationships that don't exist, such as when the current block has no child blocks. The list size can be the following:
                  * 0 - The block has no child blocks. 
                  * 1 - The block has child blocks. 
                  - *(dict) --* 
                    Information about how blocks are related to each other. A ``Block`` object contains 0 or more ``Relation`` objects in a list, ``Relationships`` . For more information, see  Block .
                    The ``Type`` element provides the type of the relationship for all blocks in the ``IDs`` array. 
                    - **Type** *(string) --* 
                      The type of relationship that the blocks in the IDs array have with the current block. The relationship can be ``VALUE`` or ``CHILD`` .
                    - **Ids** *(list) --* 
                      An array of IDs for related blocks. You can get the type of the relationship from the ``Type`` element.
                      - *(string) --* 
                - **EntityTypes** *(list) --* 
                  The type of entity. The following can be returned:
                  * *KEY* - An identifier for a field on the document. 
                  * *VALUE* - The field text. 
                   ``EntityTypes`` isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .
                  - *(string) --* 
                - **SelectionStatus** *(string) --* 
                  The selection status of a selectable element such as a radio button or checkbox. 
                - **Page** *(integer) --* 
                  The page in which a block was detected. ``Page`` is returned by asynchronous operations. Page values greater than 1 are only returned for multi-page documents that are in PDF format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always considered to be a single-page document and the value of ``Page`` is always 1. Synchronous operations don't return ``Page`` as every input document is considered to be a single-page document.
            - **Warnings** *(list) --* 
              A list of warnings that occurred during the document text-detection operation.
              - *(dict) --* 
                A warning about an issue that occurred during asynchronous text analysis ( StartDocumentAnalysis ) or asynchronous document-text detection ( StartDocumentTextDetection ). 
                - **ErrorCode** *(string) --* 
                  The error code for the warning.
                - **Pages** *(list) --* 
                  A list of the pages that the warning applies to.
                  - *(integer) --* 
            - **StatusMessage** *(string) --* 
              The current status of an asynchronous document text-detection operation. 
        :type JobId: string
        :param JobId: **[REQUIRED]**
          A unique identifier for the text detection job. The ``JobId`` is returned from ``StartDocumentTextDetection`` .
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return per paginated call. The largest value you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.
        :type NextToken: string
        :param NextToken:
          If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.
        :rtype: dict
        :returns:
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

    def start_document_analysis(self, DocumentLocation: Dict, FeatureTypes: List, ClientRequestToken: str = None, JobTag: str = None, NotificationChannel: Dict = None) -> Dict:
        """
        Starts asynchronous analysis of an input document for relationships between detected items such as key and value pairs, tables, and selection elements.
         ``StartDocumentAnalysis`` can analyze text in documents that are in JPG, PNG, and PDF format. The documents are stored in an Amazon S3 bucket. Use  DocumentLocation to specify the bucket name and file name of the document. 
         ``StartDocumentAnalysis`` returns a job identifier (``JobId`` ) that you use to get the results of the operation. When text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in ``NotificationChannel`` . To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call  GetDocumentAnalysis , and pass the job identifier (``JobId`` ) from the initial call to ``StartDocumentAnalysis`` .
        For more information, see `Document Text Analysis <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/StartDocumentAnalysis>`_
        
        **Request Syntax**
        ::
          response = client.start_document_analysis(
              DocumentLocation={
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              FeatureTypes=[
                  'TABLES'|'FORMS',
              ],
              ClientRequestToken='string',
              JobTag='string',
              NotificationChannel={
                  'SNSTopicArn': 'string',
                  'RoleArn': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'JobId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **JobId** *(string) --* 
              The identifier for the document text detection job. Use ``JobId`` to identify the job in a subsequent call to ``GetDocumentAnalysis`` .
        :type DocumentLocation: dict
        :param DocumentLocation: **[REQUIRED]**
          The location of the document to be processed.
          - **S3Object** *(dict) --*
            The Amazon S3 bucket that contains the input document.
            - **Bucket** *(string) --*
              The name of the S3 bucket.
            - **Name** *(string) --*
              The file name of the input document. It must be an image file (.JPG or .PNG format). Asynchronous operations also support PDF files.
            - **Version** *(string) --*
              If the bucket has versioning enabled, you can specify the object version.
        :type FeatureTypes: list
        :param FeatureTypes: **[REQUIRED]**
          A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected fields and the associated text. To perform both types of analysis, add TABLES and FORMS to ``FeatureTypes`` . All selectable elements (``SELECTION_ELEMENT`` ) that are detected are returned, whatever the value of ``FeatureTypes`` .
          - *(string) --*
        :type ClientRequestToken: string
        :param ClientRequestToken:
          The idempotent token that you use to identify the start request. If you use the same token with multiple ``StartDocumentAnalysis`` requests, the same ``JobId`` is returned. Use ``ClientRequestToken`` to prevent the same job from being accidentally started more than once.
        :type JobTag: string
        :param JobTag:
          An identifier you specify that\'s included in the completion notification that\'s published to the Amazon SNS topic. For example, you can use ``JobTag`` to identify the type of document, such as a tax form or a receipt, that the completion notification corresponds to.
        :type NotificationChannel: dict
        :param NotificationChannel:
          The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to.
          - **SNSTopicArn** *(string) --* **[REQUIRED]**
            The Amazon SNS topic that Amazon Textract posts the completion status to.
          - **RoleArn** *(string) --* **[REQUIRED]**
            The Amazon Resource Name (ARN) of an IAM role that gives Amazon Textract publishing permissions to the Amazon SNS topic.
        :rtype: dict
        :returns:
        """
        pass

    def start_document_text_detection(self, DocumentLocation: Dict, ClientRequestToken: str = None, JobTag: str = None, NotificationChannel: Dict = None) -> Dict:
        """
        Starts the asynchronous detection of text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.
         ``StartDocumentTextDetection`` can analyze text in documents that are in JPG, PNG, and PDF format. The documents are stored in an Amazon S3 bucket. Use  DocumentLocation to specify the bucket name and file name of the document. 
         ``StartTextDetection`` returns a job identifier (``JobId`` ) that you use to get the results of the operation. When text detection is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in ``NotificationChannel`` . To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call  GetDocumentTextDetection , and pass the job identifier (``JobId`` ) from the initial call to ``StartDocumentTextDetection`` .
        For more information, see `Document Text Detection <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/StartDocumentTextDetection>`_
        
        **Request Syntax**
        ::
          response = client.start_document_text_detection(
              DocumentLocation={
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              ClientRequestToken='string',
              JobTag='string',
              NotificationChannel={
                  'SNSTopicArn': 'string',
                  'RoleArn': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'JobId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **JobId** *(string) --* 
              The identifier for the document text-detection job. Use ``JobId`` to identify the job in a subsequent call to ``GetDocumentTextDetection`` .
        :type DocumentLocation: dict
        :param DocumentLocation: **[REQUIRED]**
          The location of the document to be processed.
          - **S3Object** *(dict) --*
            The Amazon S3 bucket that contains the input document.
            - **Bucket** *(string) --*
              The name of the S3 bucket.
            - **Name** *(string) --*
              The file name of the input document. It must be an image file (.JPG or .PNG format). Asynchronous operations also support PDF files.
            - **Version** *(string) --*
              If the bucket has versioning enabled, you can specify the object version.
        :type ClientRequestToken: string
        :param ClientRequestToken:
          The idempotent token that\'s used to identify the start request. If you use the same token with multiple ``StartDocumentTextDetection`` requests, the same ``JobId`` is returned. Use ``ClientRequestToken`` to prevent the same job from being accidentally started more than once.
        :type JobTag: string
        :param JobTag:
          An identifier you specify that\'s included in the completion notification that\'s published to the Amazon SNS topic. For example, you can use ``JobTag`` to identify the type of document, such as a tax form or a receipt, that the completion notification corresponds to.
        :type NotificationChannel: dict
        :param NotificationChannel:
          The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to.
          - **SNSTopicArn** *(string) --* **[REQUIRED]**
            The Amazon SNS topic that Amazon Textract posts the completion status to.
          - **RoleArn** *(string) --* **[REQUIRED]**
            The Amazon Resource Name (ARN) of an IAM role that gives Amazon Textract publishing permissions to the Amazon SNS topic.
        :rtype: dict
        :returns:
        """
        pass
