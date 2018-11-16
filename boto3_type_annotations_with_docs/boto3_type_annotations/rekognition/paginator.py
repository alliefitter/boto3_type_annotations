from typing import Dict
from botocore.paginate import Paginator


class ListCollections(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListCollections>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'CollectionIds\': [
                    \'string\',
                ],
                \'FaceModelVersions\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CollectionIds** *(list) --* 
        
              An array of collection IDs.
        
              - *(string) --* 
          
            - **FaceModelVersions** *(list) --* 
        
              Version numbers of the face detection models associated with the collections in the array ``CollectionIds`` . For example, the value of ``FaceModelVersions[2]`` is the version number for the face detection model used by the collection in ``CollectionId[2]`` .
        
              - *(string) --* 
          
        """
        pass


class ListFaces(Paginator):
    def paginate(self, CollectionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListFaces>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CollectionId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]** 
        
          ID of the collection from which to list the faces.
        
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
                \'Faces\': [
                    {
                        \'FaceId\': \'string\',
                        \'BoundingBox\': {
                            \'Width\': ...,
                            \'Height\': ...,
                            \'Left\': ...,
                            \'Top\': ...
                        },
                        \'ImageId\': \'string\',
                        \'ExternalImageId\': \'string\',
                        \'Confidence\': ...
                    },
                ],
                \'FaceModelVersion\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Faces** *(list) --* 
        
              An array of ``Face`` objects. 
        
              - *(dict) --* 
        
                Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned. 
        
                - **FaceId** *(string) --* 
        
                  Unique identifier that Amazon Rekognition assigns to the face.
        
                - **BoundingBox** *(dict) --* 
        
                  Bounding box of the face.
        
                  - **Width** *(float) --* 
        
                    Width of the bounding box as a ratio of the overall image width.
        
                  - **Height** *(float) --* 
        
                    Height of the bounding box as a ratio of the overall image height.
        
                  - **Left** *(float) --* 
        
                    Left coordinate of the bounding box as a ratio of overall image width.
        
                  - **Top** *(float) --* 
        
                    Top coordinate of the bounding box as a ratio of overall image height.
        
                - **ImageId** *(string) --* 
        
                  Unique identifier that Amazon Rekognition assigns to the input image.
        
                - **ExternalImageId** *(string) --* 
        
                  Identifier that you assign to all the faces in the input image.
        
                - **Confidence** *(float) --* 
        
                  Confidence level that the bounding box contains a face (and not a different object such as a tree).
        
            - **FaceModelVersion** *(string) --* 
        
              Version number of the face detection model associated with the input collection (``CollectionId`` ).
        
        """
        pass


class ListStreamProcessors(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListStreamProcessors>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'StreamProcessors\': [
                    {
                        \'Name\': \'string\',
                        \'Status\': \'STOPPED\'|\'STARTING\'|\'RUNNING\'|\'FAILED\'|\'STOPPING\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StreamProcessors** *(list) --* 
        
              List of stream processors that you have created.
        
              - *(dict) --* 
        
                An object that recognizes faces in a streaming video. An Amazon Rekognition stream processor is created by a call to . The request parameters for ``CreateStreamProcessor`` describe the Kinesis video stream source for the streaming video, face recognition parameters, and where to stream the analysis resullts. 
        
                - **Name** *(string) --* 
        
                  Name of the Amazon Rekognition stream processor. 
        
                - **Status** *(string) --* 
        
                  Current status of the Amazon Rekognition stream processor.
        
        """
        pass
