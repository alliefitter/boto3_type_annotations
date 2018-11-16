from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
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

    def create_container(self, ContainerName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/CreateContainer>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_container(
              ContainerName=\'string\'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]** 
        
          The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named ``movies`` in every region, as long as you don’t have an existing container with that name.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Container\': {
                    \'Endpoint\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'ARN\': \'string\',
                    \'Name\': \'string\',
                    \'Status\': \'ACTIVE\'|\'CREATING\'|\'DELETING\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Container** *(dict) --* 
        
              ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN has the following format: arn:aws:<region>:<account that owns this container>:container/<name of container>. For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 
        
              ContainerName: The container name as specified in the request.
        
              CreationTime: Unix time stamp.
        
              Status: The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When an endpoint is available, the status changes to ``ACTIVE`` .
        
              The return value does not include the container\'s endpoint. To make downstream requests, you must obtain this value by using  DescribeContainer or  ListContainers .
        
              - **Endpoint** *(string) --* 
        
                The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.
        
              - **CreationTime** *(datetime) --* 
        
                Unix timestamp.
        
              - **ARN** *(string) --* 
        
                The Amazon Resource Name (ARN) of the container. The ARN has the following format:
        
                arn:aws:<region>:<account that owns this container>:container/<name of container> 
        
                For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 
        
              - **Name** *(string) --* 
        
                The name of the container.
        
              - **Status** *(string) --* 
        
                The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When the endpoint is available, the status changes to ``ACTIVE`` .
        
        """
        pass

    def delete_container(self, ContainerName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteContainer>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_container(
              ContainerName=\'string\'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]** 
        
          The name of the container to delete. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_container_policy(self, ContainerName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteContainerPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_container_policy(
              ContainerName=\'string\'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]** 
        
          The name of the container that holds the policy.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_cors_policy(self, ContainerName: str) -> Dict:
        """
        
        To use this operation, you must have permission to perform the ``MediaStore:DeleteCorsPolicy`` action. The container owner has this permission by default and can grant this permission to others.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteCorsPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cors_policy(
              ContainerName=\'string\'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]** 
        
          The name of the container to remove the policy from.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_container(self, ContainerName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DescribeContainer>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_container(
              ContainerName=\'string\'
          )
        :type ContainerName: string
        :param ContainerName: 
        
          The name of the container to query.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Container\': {
                    \'Endpoint\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'ARN\': \'string\',
                    \'Name\': \'string\',
                    \'Status\': \'ACTIVE\'|\'CREATING\'|\'DELETING\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Container** *(dict) --* 
        
              The name of the queried container.
        
              - **Endpoint** *(string) --* 
        
                The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.
        
              - **CreationTime** *(datetime) --* 
        
                Unix timestamp.
        
              - **ARN** *(string) --* 
        
                The Amazon Resource Name (ARN) of the container. The ARN has the following format:
        
                arn:aws:<region>:<account that owns this container>:container/<name of container> 
        
                For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 
        
              - **Name** *(string) --* 
        
                The name of the container.
        
              - **Status** *(string) --* 
        
                The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When the endpoint is available, the status changes to ``ACTIVE`` .
        
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

    def get_container_policy(self, ContainerName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/GetContainerPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_container_policy(
              ContainerName=\'string\'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]** 
        
          The name of the container. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policy\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policy** *(string) --* 
        
              The contents of the access policy.
        
        """
        pass

    def get_cors_policy(self, ContainerName: str) -> Dict:
        """
        
        To use this operation, you must have permission to perform the ``MediaStore:GetCorsPolicy`` action. By default, the container owner has this permission and can grant it to others.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/GetCorsPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_cors_policy(
              ContainerName=\'string\'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]** 
        
          The name of the container that the policy is assigned to.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CorsPolicy\': [
                    {
                        \'AllowedOrigins\': [
                            \'string\',
                        ],
                        \'AllowedMethods\': [
                            \'PUT\'|\'GET\'|\'DELETE\'|\'HEAD\',
                        ],
                        \'AllowedHeaders\': [
                            \'string\',
                        ],
                        \'MaxAgeSeconds\': 123,
                        \'ExposeHeaders\': [
                            \'string\',
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CorsPolicy** *(list) --* 
        
              The CORS policy of the container. 
        
              - *(dict) --* 
        
                A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
        
                - **AllowedOrigins** *(list) --* 
        
                  One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object).
        
                  Each CORS rule must have at least one ``AllowedOrigin`` element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.
        
                  - *(string) --* 
              
                - **AllowedMethods** *(list) --* 
        
                  Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.
        
                  Each CORS rule must contain at least one ``AllowedMethod`` and one ``AllowedOrigin`` element.
        
                  - *(string) --* 
              
                - **AllowedHeaders** *(list) --* 
        
                  Specifies which headers are allowed in a preflight ``OPTIONS`` request through the ``Access-Control-Request-Headers`` header. Each header name that is specified in ``Access-Control-Request-Headers`` must have a corresponding entry in the rule. Only the headers that were requested are sent back. 
        
                  This element can contain only one wildcard character (*).
        
                  - *(string) --* 
              
                - **MaxAgeSeconds** *(integer) --* 
        
                  The time in seconds that your browser caches the preflight response for the specified resource.
        
                  A CORS rule can have only one ``MaxAgeSeconds`` element.
        
                - **ExposeHeaders** *(list) --* 
        
                  One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object).
        
                  This element is optional for each rule.
        
                  - *(string) --* 
              
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

    def list_containers(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        You can query to receive all the containers in one response. Or you can include the ``MaxResults`` parameter to receive a limited number of containers in each response. In this case, the response includes a token. To get the next set of containers, send the command again, this time with the ``NextToken`` parameter (with the returned token as its value). The next set of responses appears, with a token if there are still more containers to receive. 
        
        See also  DescribeContainer , which gets the properties of one container. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/ListContainers>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_containers(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          Only if you used ``MaxResults`` in the first command, enter the token (which was included in the previous response) to obtain the next set of containers. This token is included in a response only if there actually are more containers to list.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Enter the maximum number of containers in the response. Use from 1 to 255 characters. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Containers\': [
                    {
                        \'Endpoint\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'ARN\': \'string\',
                        \'Name\': \'string\',
                        \'Status\': \'ACTIVE\'|\'CREATING\'|\'DELETING\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Containers** *(list) --* 
        
              The names of the containers.
        
              - *(dict) --* 
        
                This section describes operations that you can perform on an AWS Elemental MediaStore container.
        
                - **Endpoint** *(string) --* 
        
                  The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.
        
                - **CreationTime** *(datetime) --* 
        
                  Unix timestamp.
        
                - **ARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the container. The ARN has the following format:
        
                  arn:aws:<region>:<account that owns this container>:container/<name of container> 
        
                  For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 
        
                - **Name** *(string) --* 
        
                  The name of the container.
        
                - **Status** *(string) --* 
        
                  The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When the endpoint is available, the status changes to ``ACTIVE`` .
        
            - **NextToken** *(string) --* 
        
               ``NextToken`` is the token to use in the next call to ``ListContainers`` . This token is returned only if you included the ``MaxResults`` tag in the original command, and only if there are still containers to return. 
        
        """
        pass

    def put_container_policy(self, ContainerName: str, Policy: str) -> Dict:
        """
        
        For this release of the REST API, you can create only one policy for a container. If you enter ``PutContainerPolicy`` twice, the second command modifies the existing policy. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/PutContainerPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_container_policy(
              ContainerName=\'string\',
              Policy=\'string\'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]** 
        
          The name of the container.
        
        :type Policy: string
        :param Policy: **[REQUIRED]** 
        
          The contents of the policy, which includes the following: 
        
          * One ``Version`` tag 
           
          * One ``Statement`` tag that contains the standard tags for the policy. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def put_cors_policy(self, ContainerName: str, CorsPolicy: List) -> Dict:
        """
        
        To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/PutCorsPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_cors_policy(
              ContainerName=\'string\',
              CorsPolicy=[
                  {
                      \'AllowedOrigins\': [
                          \'string\',
                      ],
                      \'AllowedMethods\': [
                          \'PUT\'|\'GET\'|\'DELETE\'|\'HEAD\',
                      ],
                      \'AllowedHeaders\': [
                          \'string\',
                      ],
                      \'MaxAgeSeconds\': 123,
                      \'ExposeHeaders\': [
                          \'string\',
                      ]
                  },
              ]
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]** 
        
          The name of the container that you want to assign the CORS policy to.
        
        :type CorsPolicy: list
        :param CorsPolicy: **[REQUIRED]** 
        
          The CORS policy to apply to the container. 
        
          - *(dict) --* 
        
            A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
        
            - **AllowedOrigins** *(list) --* 
        
              One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object).
        
              Each CORS rule must have at least one ``AllowedOrigin`` element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.
        
              - *(string) --* 
        
            - **AllowedMethods** *(list) --* 
        
              Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.
        
              Each CORS rule must contain at least one ``AllowedMethod`` and one ``AllowedOrigin`` element.
        
              - *(string) --* 
        
            - **AllowedHeaders** *(list) --* 
        
              Specifies which headers are allowed in a preflight ``OPTIONS`` request through the ``Access-Control-Request-Headers`` header. Each header name that is specified in ``Access-Control-Request-Headers`` must have a corresponding entry in the rule. Only the headers that were requested are sent back. 
        
              This element can contain only one wildcard character (*).
        
              - *(string) --* 
        
            - **MaxAgeSeconds** *(integer) --* 
        
              The time in seconds that your browser caches the preflight response for the specified resource.
        
              A CORS rule can have only one ``MaxAgeSeconds`` element.
        
            - **ExposeHeaders** *(list) --* 
        
              One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object).
        
              This element is optional for each rule.
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
