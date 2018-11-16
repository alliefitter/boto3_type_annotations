from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def batch_check_layer_availability(self, repositoryName: str, layerDigests: List, registryId: str = None) -> Dict:
        """
        
        .. note::
        
          This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the ``docker`` CLI to pull, tag, and push images.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/BatchCheckLayerAvailability>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_check_layer_availability(
              registryId=\'string\',
              repositoryName=\'string\',
              layerDigests=[
                  \'string\',
              ]
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository that is associated with the image layers to check.
        
        :type layerDigests: list
        :param layerDigests: **[REQUIRED]** 
        
          The digests of the image layers to check.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'layers\': [
                    {
                        \'layerDigest\': \'string\',
                        \'layerAvailability\': \'AVAILABLE\'|\'UNAVAILABLE\',
                        \'layerSize\': 123,
                        \'mediaType\': \'string\'
                    },
                ],
                \'failures\': [
                    {
                        \'layerDigest\': \'string\',
                        \'failureCode\': \'InvalidLayerDigest\'|\'MissingLayerDigest\',
                        \'failureReason\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **layers** *(list) --* 
        
              A list of image layer objects corresponding to the image layer references in the request.
        
              - *(dict) --* 
        
                An object representing an Amazon ECR image layer.
        
                - **layerDigest** *(string) --* 
        
                  The ``sha256`` digest of the image layer.
        
                - **layerAvailability** *(string) --* 
        
                  The availability status of the image layer.
        
                - **layerSize** *(integer) --* 
        
                  The size, in bytes, of the image layer.
        
                - **mediaType** *(string) --* 
        
                  The media type of the layer, such as ``application/vnd.docker.image.rootfs.diff.tar.gzip`` or ``application/vnd.oci.image.layer.v1.tar+gzip`` .
        
            - **failures** *(list) --* 
        
              Any failures associated with the call.
        
              - *(dict) --* 
        
                An object representing an Amazon ECR image layer failure.
        
                - **layerDigest** *(string) --* 
        
                  The layer digest associated with the failure.
        
                - **failureCode** *(string) --* 
        
                  The failure code associated with the failure.
        
                - **failureReason** *(string) --* 
        
                  The reason for the failure.
        
        """
        pass

    def batch_delete_image(self, repositoryName: str, imageIds: List, registryId: str = None) -> Dict:
        """
        
        You can remove a tag from an image by specifying the image\'s tag in your request. When you remove the last tag from an image, the image is deleted from your repository.
        
        You can completely delete an image (and all of its tags) by specifying the image\'s digest in your request.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/BatchDeleteImage>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_delete_image(
              registryId=\'string\',
              repositoryName=\'string\',
              imageIds=[
                  {
                      \'imageDigest\': \'string\',
                      \'imageTag\': \'string\'
                  },
              ]
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The repository that contains the image to delete.
        
        :type imageIds: list
        :param imageIds: **[REQUIRED]** 
        
          A list of image ID references that correspond to images to delete. The format of the ``imageIds`` reference is ``imageTag=tag`` or ``imageDigest=digest`` .
        
          - *(dict) --* 
        
            An object with identifying information for an Amazon ECR image.
        
            - **imageDigest** *(string) --* 
        
              The ``sha256`` digest of the image manifest.
        
            - **imageTag** *(string) --* 
        
              The tag used for the image.
        
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
                \'failures\': [
                    {
                        \'imageId\': {
                            \'imageDigest\': \'string\',
                            \'imageTag\': \'string\'
                        },
                        \'failureCode\': \'InvalidImageDigest\'|\'InvalidImageTag\'|\'ImageTagDoesNotMatchDigest\'|\'ImageNotFound\'|\'MissingDigestAndTag\',
                        \'failureReason\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **imageIds** *(list) --* 
        
              The image IDs of the deleted images.
        
              - *(dict) --* 
        
                An object with identifying information for an Amazon ECR image.
        
                - **imageDigest** *(string) --* 
        
                  The ``sha256`` digest of the image manifest.
        
                - **imageTag** *(string) --* 
        
                  The tag used for the image.
        
            - **failures** *(list) --* 
        
              Any failures associated with the call.
        
              - *(dict) --* 
        
                An object representing an Amazon ECR image failure.
        
                - **imageId** *(dict) --* 
        
                  The image ID associated with the failure.
        
                  - **imageDigest** *(string) --* 
        
                    The ``sha256`` digest of the image manifest.
        
                  - **imageTag** *(string) --* 
        
                    The tag used for the image.
        
                - **failureCode** *(string) --* 
        
                  The code associated with the failure.
        
                - **failureReason** *(string) --* 
        
                  The reason for the failure.
        
        """
        pass

    def batch_get_image(self, repositoryName: str, imageIds: List, registryId: str = None, acceptedMediaTypes: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/BatchGetImage>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_get_image(
              registryId=\'string\',
              repositoryName=\'string\',
              imageIds=[
                  {
                      \'imageDigest\': \'string\',
                      \'imageTag\': \'string\'
                  },
              ],
              acceptedMediaTypes=[
                  \'string\',
              ]
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The repository that contains the images to describe.
        
        :type imageIds: list
        :param imageIds: **[REQUIRED]** 
        
          A list of image ID references that correspond to images to describe. The format of the ``imageIds`` reference is ``imageTag=tag`` or ``imageDigest=digest`` .
        
          - *(dict) --* 
        
            An object with identifying information for an Amazon ECR image.
        
            - **imageDigest** *(string) --* 
        
              The ``sha256`` digest of the image manifest.
        
            - **imageTag** *(string) --* 
        
              The tag used for the image.
        
        :type acceptedMediaTypes: list
        :param acceptedMediaTypes: 
        
          The accepted media types for the request.
        
          Valid values: ``application/vnd.docker.distribution.manifest.v1+json`` | ``application/vnd.docker.distribution.manifest.v2+json`` | ``application/vnd.oci.image.manifest.v1+json``  
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'images\': [
                    {
                        \'registryId\': \'string\',
                        \'repositoryName\': \'string\',
                        \'imageId\': {
                            \'imageDigest\': \'string\',
                            \'imageTag\': \'string\'
                        },
                        \'imageManifest\': \'string\'
                    },
                ],
                \'failures\': [
                    {
                        \'imageId\': {
                            \'imageDigest\': \'string\',
                            \'imageTag\': \'string\'
                        },
                        \'failureCode\': \'InvalidImageDigest\'|\'InvalidImageTag\'|\'ImageTagDoesNotMatchDigest\'|\'ImageNotFound\'|\'MissingDigestAndTag\',
                        \'failureReason\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **images** *(list) --* 
        
              A list of image objects corresponding to the image references in the request.
        
              - *(dict) --* 
        
                An object representing an Amazon ECR image.
        
                - **registryId** *(string) --* 
        
                  The AWS account ID associated with the registry containing the image.
        
                - **repositoryName** *(string) --* 
        
                  The name of the repository associated with the image.
        
                - **imageId** *(dict) --* 
        
                  An object containing the image tag and image digest associated with an image.
        
                  - **imageDigest** *(string) --* 
        
                    The ``sha256`` digest of the image manifest.
        
                  - **imageTag** *(string) --* 
        
                    The tag used for the image.
        
                - **imageManifest** *(string) --* 
        
                  The image manifest associated with the image.
        
            - **failures** *(list) --* 
        
              Any failures associated with the call.
        
              - *(dict) --* 
        
                An object representing an Amazon ECR image failure.
        
                - **imageId** *(dict) --* 
        
                  The image ID associated with the failure.
        
                  - **imageDigest** *(string) --* 
        
                    The ``sha256`` digest of the image manifest.
        
                  - **imageTag** *(string) --* 
        
                    The tag used for the image.
        
                - **failureCode** *(string) --* 
        
                  The code associated with the failure.
        
                - **failureReason** *(string) --* 
        
                  The reason for the failure.
        
        """
        pass

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

    def complete_layer_upload(self, repositoryName: str, uploadId: str, layerDigests: List, registryId: str = None) -> Dict:
        """
        
        .. note::
        
          This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the ``docker`` CLI to pull, tag, and push images.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/CompleteLayerUpload>`_
        
        **Request Syntax** 
        ::
        
          response = client.complete_layer_upload(
              registryId=\'string\',
              repositoryName=\'string\',
              uploadId=\'string\',
              layerDigests=[
                  \'string\',
              ]
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to associate with the image layer.
        
        :type uploadId: string
        :param uploadId: **[REQUIRED]** 
        
          The upload ID from a previous  InitiateLayerUpload operation to associate with the image layer.
        
        :type layerDigests: list
        :param layerDigests: **[REQUIRED]** 
        
          The ``sha256`` digest of the image layer.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'uploadId\': \'string\',
                \'layerDigest\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **uploadId** *(string) --* 
        
              The upload ID associated with the layer.
        
            - **layerDigest** *(string) --* 
        
              The ``sha256`` digest of the image layer.
        
        """
        pass

    def create_repository(self, repositoryName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/CreateRepository>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_repository(
              repositoryName=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name to use for the repository. The repository name may be specified on its own (such as ``nginx-web-app`` ) or it can be prepended with a namespace to group the repository into a category (such as ``project-a/nginx-web-app`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repository\': {
                    \'repositoryArn\': \'string\',
                    \'registryId\': \'string\',
                    \'repositoryName\': \'string\',
                    \'repositoryUri\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **repository** *(dict) --* 
        
              The repository that was created.
        
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
        
        """
        pass

    def delete_lifecycle_policy(self, repositoryName: str, registryId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DeleteLifecyclePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_lifecycle_policy(
              registryId=\'string\',
              repositoryName=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'lifecyclePolicyText\': \'string\',
                \'lastEvaluatedAt\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **lifecyclePolicyText** *(string) --* 
        
              The JSON lifecycle policy text.
        
            - **lastEvaluatedAt** *(datetime) --* 
        
              The time stamp of the last time that the lifecycle policy was run.
        
        """
        pass

    def delete_repository(self, repositoryName: str, registryId: str = None, force: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DeleteRepository>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_repository(
              registryId=\'string\',
              repositoryName=\'string\',
              force=True|False
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to delete.
        
        :type force: boolean
        :param force: 
        
          If a repository contains images, forces the deletion.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repository\': {
                    \'repositoryArn\': \'string\',
                    \'registryId\': \'string\',
                    \'repositoryName\': \'string\',
                    \'repositoryUri\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **repository** *(dict) --* 
        
              The repository that was deleted.
        
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
        
        """
        pass

    def delete_repository_policy(self, repositoryName: str, registryId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DeleteRepositoryPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_repository_policy(
              registryId=\'string\',
              repositoryName=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository policy to delete. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository that is associated with the repository policy to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'policyText\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **policyText** *(string) --* 
        
              The JSON repository policy that was deleted from the repository.
        
        """
        pass

    def describe_images(self, repositoryName: str, registryId: str = None, imageIds: List = None, nextToken: str = None, maxResults: int = None, filter: Dict = None) -> Dict:
        """
        
        .. note::
        
          Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the ``docker images`` command shows the uncompressed image size, so it may return a larger image size than the image sizes returned by  DescribeImages .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_images(
              registryId=\'string\',
              repositoryName=\'string\',
              imageIds=[
                  {
                      \'imageDigest\': \'string\',
                      \'imageTag\': \'string\'
                  },
              ],
              nextToken=\'string\',
              maxResults=123,
              filter={
                  \'tagStatus\': \'TAGGED\'|\'UNTAGGED\'
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
        
        :type nextToken: string
        :param nextToken: 
        
          The ``nextToken`` value returned from a previous paginated ``DescribeImages`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return. This option cannot be used when you specify images with ``imageIds`` .
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of repository results returned by ``DescribeImages`` in paginated output. When this parameter is used, ``DescribeImages`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeImages`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``DescribeImages`` returns up to 100 results and a ``nextToken`` value, if applicable. This option cannot be used when you specify images with ``imageIds`` .
        
        :type filter: dict
        :param filter: 
        
          The filter key and value with which to filter your ``DescribeImages`` results.
        
          - **tagStatus** *(string) --* 
        
            The tag status with which to filter your  DescribeImages results. You can filter results based on whether they are ``TAGGED`` or ``UNTAGGED`` .
        
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
                \'nextToken\': \'string\'
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
        
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``DescribeImages`` request. When the results of a ``DescribeImages`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
        """
        pass

    def describe_repositories(self, registryId: str = None, repositoryNames: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeRepositories>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_repositories(
              registryId=\'string\',
              repositoryNames=[
                  \'string\',
              ],
              nextToken=\'string\',
              maxResults=123
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryNames: list
        :param repositoryNames: 
        
          A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.
        
          - *(string) --* 
        
        :type nextToken: string
        :param nextToken: 
        
          The ``nextToken`` value returned from a previous paginated ``DescribeRepositories`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return. This option cannot be used when you specify repositories with ``repositoryNames`` .
        
          .. note::
        
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of repository results returned by ``DescribeRepositories`` in paginated output. When this parameter is used, ``DescribeRepositories`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeRepositories`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``DescribeRepositories`` returns up to 100 results and a ``nextToken`` value, if applicable. This option cannot be used when you specify repositories with ``repositoryNames`` .
        
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
                \'nextToken\': \'string\'
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
        
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``DescribeRepositories`` request. When the results of a ``DescribeRepositories`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
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

    def get_authorization_token(self, registryIds: List = None) -> Dict:
        """
        
        The ``authorizationToken`` returned for each registry specified is a base64 encoded string that can be decoded and used in a ``docker login`` command to authenticate to a registry. The AWS CLI offers an ``aws ecr get-login`` command that simplifies the login process.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/GetAuthorizationToken>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_authorization_token(
              registryIds=[
                  \'string\',
              ]
          )
        :type registryIds: list
        :param registryIds: 
        
          A list of AWS account IDs that are associated with the registries for which to get authorization tokens. If you do not specify a registry, the default registry is assumed.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'authorizationData\': [
                    {
                        \'authorizationToken\': \'string\',
                        \'expiresAt\': datetime(2015, 1, 1),
                        \'proxyEndpoint\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **authorizationData** *(list) --* 
        
              A list of authorization token data objects that correspond to the ``registryIds`` values in the request.
        
              - *(dict) --* 
        
                An object representing authorization data for an Amazon ECR registry.
        
                - **authorizationToken** *(string) --* 
        
                  A base64-encoded string that contains authorization data for the specified Amazon ECR registry. When the string is decoded, it is presented in the format ``user:password`` for private registry authentication using ``docker login`` .
        
                - **expiresAt** *(datetime) --* 
        
                  The Unix time in seconds and milliseconds when the authorization token expires. Authorization tokens are valid for 12 hours.
        
                - **proxyEndpoint** *(string) --* 
        
                  The registry URL to use for this authorization token in a ``docker login`` command. The Amazon ECR registry URL format is ``https://aws_account_id.dkr.ecr.region.amazonaws.com`` . For example, ``https://012345678910.dkr.ecr.us-east-1.amazonaws.com`` .. 
        
        """
        pass

    def get_download_url_for_layer(self, repositoryName: str, layerDigest: str, registryId: str = None) -> Dict:
        """
        
        .. note::
        
          This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the ``docker`` CLI to pull, tag, and push images.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/GetDownloadUrlForLayer>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_download_url_for_layer(
              registryId=\'string\',
              repositoryName=\'string\',
              layerDigest=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository that is associated with the image layer to download.
        
        :type layerDigest: string
        :param layerDigest: **[REQUIRED]** 
        
          The digest of the image layer to download.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'downloadUrl\': \'string\',
                \'layerDigest\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **downloadUrl** *(string) --* 
        
              The pre-signed Amazon S3 download URL for the requested layer.
        
            - **layerDigest** *(string) --* 
        
              The digest of the image layer to download.
        
        """
        pass

    def get_lifecycle_policy(self, repositoryName: str, registryId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/GetLifecyclePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_lifecycle_policy(
              registryId=\'string\',
              repositoryName=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'lifecyclePolicyText\': \'string\',
                \'lastEvaluatedAt\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **lifecyclePolicyText** *(string) --* 
        
              The JSON lifecycle policy text.
        
            - **lastEvaluatedAt** *(datetime) --* 
        
              The time stamp of the last time that the lifecycle policy was run.
        
        """
        pass

    def get_lifecycle_policy_preview(self, repositoryName: str, registryId: str = None, imageIds: List = None, nextToken: str = None, maxResults: int = None, filter: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/GetLifecyclePolicyPreview>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_lifecycle_policy_preview(
              registryId=\'string\',
              repositoryName=\'string\',
              imageIds=[
                  {
                      \'imageDigest\': \'string\',
                      \'imageTag\': \'string\'
                  },
              ],
              nextToken=\'string\',
              maxResults=123,
              filter={
                  \'tagStatus\': \'TAGGED\'|\'UNTAGGED\'
              }
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository.
        
        :type imageIds: list
        :param imageIds: 
        
          The list of imageIDs to be included.
        
          - *(dict) --* 
        
            An object with identifying information for an Amazon ECR image.
        
            - **imageDigest** *(string) --* 
        
              The ``sha256`` digest of the image manifest.
        
            - **imageTag** *(string) --* 
        
              The tag used for the image.
        
        :type nextToken: string
        :param nextToken: 
        
          The ``nextToken`` value returned from a previous paginated ``GetLifecyclePolicyPreviewRequest`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return. This option cannot be used when you specify images with ``imageIds`` .
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of repository results returned by ``GetLifecyclePolicyPreviewRequest`` in paginated output. When this parameter is used, ``GetLifecyclePolicyPreviewRequest`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``GetLifecyclePolicyPreviewRequest`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``GetLifecyclePolicyPreviewRequest`` returns up to 100 results and a ``nextToken`` value, if applicable. This option cannot be used when you specify images with ``imageIds`` .
        
        :type filter: dict
        :param filter: 
        
          An optional parameter that filters results based on image tag status and all tags, if tagged.
        
          - **tagStatus** *(string) --* 
        
            The tag status of the image.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'lifecyclePolicyText\': \'string\',
                \'status\': \'IN_PROGRESS\'|\'COMPLETE\'|\'EXPIRED\'|\'FAILED\',
                \'nextToken\': \'string\',
                \'previewResults\': [
                    {
                        \'imageTags\': [
                            \'string\',
                        ],
                        \'imageDigest\': \'string\',
                        \'imagePushedAt\': datetime(2015, 1, 1),
                        \'action\': {
                            \'type\': \'EXPIRE\'
                        },
                        \'appliedRulePriority\': 123
                    },
                ],
                \'summary\': {
                    \'expiringImageTotalCount\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **lifecyclePolicyText** *(string) --* 
        
              The JSON lifecycle policy text.
        
            - **status** *(string) --* 
        
              The status of the lifecycle policy preview request.
        
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``GetLifecyclePolicyPreview`` request. When the results of a ``GetLifecyclePolicyPreview`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
            - **previewResults** *(list) --* 
        
              The results of the lifecycle policy preview request.
        
              - *(dict) --* 
        
                The result of the lifecycle policy preview.
        
                - **imageTags** *(list) --* 
        
                  The list of tags associated with this image.
        
                  - *(string) --* 
              
                - **imageDigest** *(string) --* 
        
                  The ``sha256`` digest of the image manifest.
        
                - **imagePushedAt** *(datetime) --* 
        
                  The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository.
        
                - **action** *(dict) --* 
        
                  The type of action to be taken.
        
                  - **type** *(string) --* 
        
                    The type of action to be taken.
        
                - **appliedRulePriority** *(integer) --* 
        
                  The priority of the applied rule.
        
            - **summary** *(dict) --* 
        
              The list of images that is returned as a result of the action.
        
              - **expiringImageTotalCount** *(integer) --* 
        
                The number of expiring images.
        
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

    def get_repository_policy(self, repositoryName: str, registryId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/GetRepositoryPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_repository_policy(
              registryId=\'string\',
              repositoryName=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository with the policy to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'policyText\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **policyText** *(string) --* 
        
              The JSON repository policy text associated with the repository.
        
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

    def initiate_layer_upload(self, repositoryName: str, registryId: str = None) -> Dict:
        """
        
        .. note::
        
          This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the ``docker`` CLI to pull, tag, and push images.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/InitiateLayerUpload>`_
        
        **Request Syntax** 
        ::
        
          response = client.initiate_layer_upload(
              registryId=\'string\',
              repositoryName=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry to which you intend to upload layers. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to which you intend to upload layers.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'uploadId\': \'string\',
                \'partSize\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **uploadId** *(string) --* 
        
              The upload ID for the layer upload. This parameter is passed to further  UploadLayerPart and  CompleteLayerUpload operations.
        
            - **partSize** *(integer) --* 
        
              The size, in bytes, that Amazon ECR expects future layer part uploads to be.
        
        """
        pass

    def list_images(self, repositoryName: str, registryId: str = None, nextToken: str = None, maxResults: int = None, filter: Dict = None) -> Dict:
        """
        
        You can filter images based on whether or not they are tagged by setting the ``tagStatus`` parameter to ``TAGGED`` or ``UNTAGGED`` . For example, you can filter your results to return only ``UNTAGGED`` images and then pipe that result to a  BatchDeleteImage operation to delete them. Or, you can filter your results to return only ``TAGGED`` images to list all of the tags in your repository.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/ListImages>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_images(
              registryId=\'string\',
              repositoryName=\'string\',
              nextToken=\'string\',
              maxResults=123,
              filter={
                  \'tagStatus\': \'TAGGED\'|\'UNTAGGED\'
              }
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The repository with image IDs to be listed.
        
        :type nextToken: string
        :param nextToken: 
        
          The ``nextToken`` value returned from a previous paginated ``ListImages`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.
        
          .. note::
        
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of image results returned by ``ListImages`` in paginated output. When this parameter is used, ``ListImages`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListImages`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListImages`` returns up to 100 results and a ``nextToken`` value, if applicable.
        
        :type filter: dict
        :param filter: 
        
          The filter key and value with which to filter your ``ListImages`` results.
        
          - **tagStatus** *(string) --* 
        
            The tag status with which to filter your  ListImages results. You can filter results based on whether they are ``TAGGED`` or ``UNTAGGED`` .
        
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
                \'nextToken\': \'string\'
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
        
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``ListImages`` request. When the results of a ``ListImages`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
        """
        pass

    def put_image(self, repositoryName: str, imageManifest: str, registryId: str = None, imageTag: str = None) -> Dict:
        """
        
        .. note::
        
          This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the ``docker`` CLI to pull, tag, and push images.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/PutImage>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_image(
              registryId=\'string\',
              repositoryName=\'string\',
              imageManifest=\'string\',
              imageTag=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository in which to put the image.
        
        :type imageManifest: string
        :param imageManifest: **[REQUIRED]** 
        
          The image manifest corresponding to the image to be uploaded.
        
        :type imageTag: string
        :param imageTag: 
        
          The tag to associate with the image. This parameter is required for images that use the Docker Image Manifest V2 Schema 2 or OCI formats.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'image\': {
                    \'registryId\': \'string\',
                    \'repositoryName\': \'string\',
                    \'imageId\': {
                        \'imageDigest\': \'string\',
                        \'imageTag\': \'string\'
                    },
                    \'imageManifest\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **image** *(dict) --* 
        
              Details of the image uploaded.
        
              - **registryId** *(string) --* 
        
                The AWS account ID associated with the registry containing the image.
        
              - **repositoryName** *(string) --* 
        
                The name of the repository associated with the image.
        
              - **imageId** *(dict) --* 
        
                An object containing the image tag and image digest associated with an image.
        
                - **imageDigest** *(string) --* 
        
                  The ``sha256`` digest of the image manifest.
        
                - **imageTag** *(string) --* 
        
                  The tag used for the image.
        
              - **imageManifest** *(string) --* 
        
                The image manifest associated with the image.
        
        """
        pass

    def put_lifecycle_policy(self, repositoryName: str, lifecyclePolicyText: str, registryId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/PutLifecyclePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_lifecycle_policy(
              registryId=\'string\',
              repositoryName=\'string\',
              lifecyclePolicyText=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to receive the policy.
        
        :type lifecyclePolicyText: string
        :param lifecyclePolicyText: **[REQUIRED]** 
        
          The JSON repository policy text to apply to the repository.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'lifecyclePolicyText\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **lifecyclePolicyText** *(string) --* 
        
              The JSON repository policy text.
        
        """
        pass

    def set_repository_policy(self, repositoryName: str, policyText: str, registryId: str = None, force: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/SetRepositoryPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_repository_policy(
              registryId=\'string\',
              repositoryName=\'string\',
              policyText=\'string\',
              force=True|False
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to receive the policy.
        
        :type policyText: string
        :param policyText: **[REQUIRED]** 
        
          The JSON repository policy text to apply to the repository.
        
        :type force: boolean
        :param force: 
        
          If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the  SetRepositoryPolicy operation. This is intended to prevent accidental repository lock outs.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'policyText\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **policyText** *(string) --* 
        
              The JSON repository policy text applied to the repository.
        
        """
        pass

    def start_lifecycle_policy_preview(self, repositoryName: str, registryId: str = None, lifecyclePolicyText: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/StartLifecyclePolicyPreview>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_lifecycle_policy_preview(
              registryId=\'string\',
              repositoryName=\'string\',
              lifecyclePolicyText=\'string\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to be evaluated.
        
        :type lifecyclePolicyText: string
        :param lifecyclePolicyText: 
        
          The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'lifecyclePolicyText\': \'string\',
                \'status\': \'IN_PROGRESS\'|\'COMPLETE\'|\'EXPIRED\'|\'FAILED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **lifecyclePolicyText** *(string) --* 
        
              The JSON repository policy text.
        
            - **status** *(string) --* 
        
              The status of the lifecycle policy preview request.
        
        """
        pass

    def upload_layer_part(self, repositoryName: str, uploadId: str, partFirstByte: int, partLastByte: int, layerPartBlob: bytes, registryId: str = None) -> Dict:
        """
        
        .. note::
        
          This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the ``docker`` CLI to pull, tag, and push images.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/UploadLayerPart>`_
        
        **Request Syntax** 
        ::
        
          response = client.upload_layer_part(
              registryId=\'string\',
              repositoryName=\'string\',
              uploadId=\'string\',
              partFirstByte=123,
              partLastByte=123,
              layerPartBlob=b\'bytes\'
          )
        :type registryId: string
        :param registryId: 
        
          The AWS account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to which you are uploading layer parts.
        
        :type uploadId: string
        :param uploadId: **[REQUIRED]** 
        
          The upload ID from a previous  InitiateLayerUpload operation to associate with the layer part upload.
        
        :type partFirstByte: integer
        :param partFirstByte: **[REQUIRED]** 
        
          The integer value of the first byte of the layer part.
        
        :type partLastByte: integer
        :param partLastByte: **[REQUIRED]** 
        
          The integer value of the last byte of the layer part.
        
        :type layerPartBlob: bytes
        :param layerPartBlob: **[REQUIRED]** 
        
          The base64-encoded layer part payload.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'registryId\': \'string\',
                \'repositoryName\': \'string\',
                \'uploadId\': \'string\',
                \'lastByteReceived\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **registryId** *(string) --* 
        
              The registry ID associated with the request.
        
            - **repositoryName** *(string) --* 
        
              The repository name associated with the request.
        
            - **uploadId** *(string) --* 
        
              The upload ID associated with the request.
        
            - **lastByteReceived** *(integer) --* 
        
              The integer value of the last byte received in the request.
        
        """
        pass
