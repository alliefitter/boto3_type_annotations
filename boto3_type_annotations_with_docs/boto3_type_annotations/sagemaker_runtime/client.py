from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient
from typing import IO


class Client(BaseClient):
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

    def invoke_endpoint(self, EndpointName: str, Body: Union[bytes, IO], ContentType: str = None, Accept: str = None, CustomAttributes: str = None) -> Dict:
        """
        
        For an overview of Amazon SageMaker, see `How It Works <http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__ . 
        
        Amazon SageMaker strips all POST headers except those supported by the API. Amazon SageMaker might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax. 
        
        Cals to ``InvokeEndpoint`` are authenticated by using AWS Signature Version 4. For information, see `Authenticating Requests (AWS Signature Version 4) <http://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html>`__ in the *Amazon S3 API Reference* .
        
        .. note::
        
          Endpoints are scoped to an individual account, and are not public. The URL does not contain the account ID, but Amazon SageMaker determines the account ID from the authentication token that is supplied by the caller.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/runtime.sagemaker-2017-05-13/InvokeEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.invoke_endpoint(
              EndpointName=\'string\',
              Body=b\'bytes\'|file,
              ContentType=\'string\',
              Accept=\'string\',
              CustomAttributes=\'string\'
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]** 
        
          The name of the endpoint that you specified when you created the endpoint using the `CreateEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html>`__ API. 
        
        :type Body: bytes or seekable file-like object
        :param Body: **[REQUIRED]** 
        
          Provides input data, in the format specified in the ``ContentType`` request header. Amazon SageMaker passes all of the data in the body to the model. 
        
          For information about the format of the request body, see `Common Data Formats—Inference <http://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html>`__ .
        
        :type ContentType: string
        :param ContentType: 
        
          The MIME type of the input data in the request body.
        
        :type Accept: string
        :param Accept: 
        
          The desired MIME type of the inference in the response.
        
        :type CustomAttributes: string
        :param CustomAttributes: 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Body\': StreamingBody(),
                \'ContentType\': \'string\',
                \'InvokedProductionVariant\': \'string\',
                \'CustomAttributes\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Body** (:class:`.StreamingBody`) -- 
        
              Includes the inference provided by the model.
        
              For information about the format of the response body, see `Common Data Formats—Inference <http://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html>`__ .
        
            - **ContentType** *(string) --* 
        
              The MIME type of the inference returned in the response body.
        
            - **InvokedProductionVariant** *(string) --* 
        
              Identifies the production variant that was invoked.
        
            - **CustomAttributes** *(string) --* 
        
        """
        pass
