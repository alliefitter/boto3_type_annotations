from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeImages(Paginator):
    def paginate(self, repositoryName: str, registryId: str = None, imageIds: List = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              registryId=\'string\',
              repositoryName=\'string\',
              imageIds=[
                  {
                      \'imageDigest\': \'string\',
                      \'imageTag\': \'string\'
                  },
              ],
              filter={
                  \'tagStatus\': \'TAGGED\'|\'UNTAGGED\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.
        
        :type imageIds: list
        :param imageIds: 
        
          The list of image IDs for the requested repository.
        
          - *(dict) --* 
        
            An object with identifying information for an Amazon ECR image.
        
            - **imageDigest** *(string) --* 
        
              The ``sha256`` digest of the image manifest.
        
            - **imageTag** *(string) --* 
        
              The tag used for the image.
        
        :type filter: dict
        :param filter: 
        
          The filter key and value with which to filter your ``DescribeImages`` results.
        
          - **tagStatus** *(string) --* 
        
            The tag status with which to filter your  DescribeImages results. You can filter results based on whether they are ``TAGGED`` or ``UNTAGGED`` .
        
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
                \'imageDetails\': [
                    {
                        \'registryId\': \'string\',
                        \'repositoryName\': \'string\',
                        \'imageDigest\': \'string\',
                        \'imageTags\': [
                            \'string\',
                        ],
                        \'imageSizeInBytes\': 123,
                        \'imagePushedAt\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **imageDetails** *(list) --* 
        
              A list of  ImageDetail objects that contain data about the image.
        
              - *(dict) --* 
        
                An object that describes an image returned by a  DescribeImages operation.
        
                - **registryId** *(string) --* 
        
                  The AWS account ID associated with the registry to which this image belongs.
        
                - **repositoryName** *(string) --* 
        
                  The name of the repository to which this image belongs.
        
                - **imageDigest** *(string) --* 
        
                  The ``sha256`` digest of the image manifest.
        
                - **imageTags** *(list) --* 
        
                  The list of tags associated with this image.
        
                  - *(string) --* 
              
                - **imageSizeInBytes** *(integer) --* 
        
                  The size, in bytes, of the image in the repository.
        
                  .. note::
        
                    Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the ``docker images`` command shows the uncompressed image size, so it may return a larger image size than the image sizes returned by  DescribeImages .
        
                - **imagePushedAt** *(datetime) --* 
        
                  The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository. 
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeRepositories(Paginator):
    def paginate(self, registryId: str = None, repositoryNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeRepositories>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              registryId=\'string\',
              repositoryNames=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryNames: list
        :param repositoryNames: 
        
          A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.
        
          - *(string) --* 
        
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
                \'repositories\': [
                    {
                        \'repositoryArn\': \'string\',
                        \'registryId\': \'string\',
                        \'repositoryName\': \'string\',
                        \'repositoryUri\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **repositories** *(list) --* 
        
              A list of repository objects corresponding to valid repositories.
        
              - *(dict) --* 
        
                An object representing a repository.
        
                - **repositoryArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the repository owner, repository namespace, and repository name. For example, ``arn:aws:ecr:region:012345678910:repository/test`` .
        
                - **registryId** *(string) --* 
        
                  The AWS account ID associated with the registry that contains the repository.
        
                - **repositoryName** *(string) --* 
        
                  The name of the repository.
        
                - **repositoryUri** *(string) --* 
        
                  The URI for the repository. You can use this URI for Docker ``push`` or ``pull`` operations.
        
                - **createdAt** *(datetime) --* 
        
                  The date and time, in JavaScript date format, when the repository was created.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListImages(Paginator):
    def paginate(self, repositoryName: str, registryId: str = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/ListImages>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              registryId=\'string\',
              repositoryName=\'string\',
              filter={
                  \'tagStatus\': \'TAGGED\'|\'UNTAGGED\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The repository with image IDs to be listed.
        
        :type filter: dict
        :param filter: 
        
          The filter key and value with which to filter your ``ListImages`` results.
        
          - **tagStatus** *(string) --* 
        
            The tag status with which to filter your  ListImages results. You can filter results based on whether they are ``TAGGED`` or ``UNTAGGED`` .
        
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
                \'imageIds\': [
                    {
                        \'imageDigest\': \'string\',
                        \'imageTag\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **imageIds** *(list) --* 
        
              The list of image IDs for the requested repository.
        
              - *(dict) --* 
        
                An object with identifying information for an Amazon ECR image.
        
                - **imageDigest** *(string) --* 
        
                  The ``sha256`` digest of the image manifest.
        
                - **imageTag** *(string) --* 
        
                  The tag used for the image.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
