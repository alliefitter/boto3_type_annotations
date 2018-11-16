from typing import Union
from botocore.paginate import Paginator
from typing import IO
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

    def delete_object(self, Path: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/DeleteObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_object(
              Path=\'string\'
          )
        :type Path: string
        :param Path: **[REQUIRED]** 
        
          The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_object(self, Path: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/DescribeObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_object(
              Path=\'string\'
          )
        :type Path: string
        :param Path: **[REQUIRED]** 
        
          The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ETag\': \'string\',
                \'ContentType\': \'string\',
                \'ContentLength\': 123,
                \'CacheControl\': \'string\',
                \'LastModified\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ETag** *(string) --* 
        
              The ETag that represents a unique instance of the object.
        
            - **ContentType** *(string) --* 
        
              The content type of the object.
        
            - **ContentLength** *(integer) --* 
        
              The length of the object in bytes.
        
            - **CacheControl** *(string) --* 
        
              An optional ``CacheControl`` header that allows the caller to control the object\'s cache behavior. Headers can be passed in as specified in the HTTP at `https\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .
        
              Headers with a custom user-defined value are also accepted.
        
            - **LastModified** *(datetime) --* 
        
              The date and time that the object was last modified.
        
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

    def get_object(self, Path: str, Range: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/GetObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_object(
              Path=\'string\',
              Range=\'string\'
          )
        :type Path: string
        :param Path: **[REQUIRED]** 
        
          The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>
        
          For example, to upload the file ``mlaw.avi`` to the folder path ``premium\canada`` in the container ``movies`` , enter the path ``premium/canada/mlaw.avi`` .
        
          Do not include the container name in this path.
        
          If the path includes any folders that don\'t exist yet, the service creates them. For example, suppose you have an existing ``premium/usa`` subfolder. If you specify ``premium/canada`` , the service creates a ``canada`` subfolder in the ``premium`` folder. You then have two subfolders, ``usa`` and ``canada`` , in the ``premium`` folder. 
        
          There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.
        
          For more information about folders and how they exist in a container, see the `AWS Elemental MediaStore User Guide <http://docs.aws.amazon.com/mediastore/latest/ug/>`__ .
        
          The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. 
        
        :type Range: string
        :param Range: 
        
          The range bytes of an object to retrieve. For more information about the ``Range`` header, go to `http\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35>`__ .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Body\': StreamingBody(),
                \'CacheControl\': \'string\',
                \'ContentRange\': \'string\',
                \'ContentLength\': 123,
                \'ContentType\': \'string\',
                \'ETag\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'StatusCode\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Body** (:class:`.StreamingBody`) -- 
        
              The bytes of the object. 
        
            - **CacheControl** *(string) --* 
        
              An optional ``CacheControl`` header that allows the caller to control the object\'s cache behavior. Headers can be passed in as specified in the HTTP spec at `https\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .
        
              Headers with a custom user-defined value are also accepted.
        
            - **ContentRange** *(string) --* 
        
              The range of bytes to retrieve.
        
            - **ContentLength** *(integer) --* 
        
              The length of the object in bytes.
        
            - **ContentType** *(string) --* 
        
              The content type of the object.
        
            - **ETag** *(string) --* 
        
              The ETag that represents a unique instance of the object.
        
            - **LastModified** *(datetime) --* 
        
              The date and time that the object was last modified.
        
            - **StatusCode** *(integer) --* 
        
              The HTML status code of the request. Status codes ranging from 200 to 299 indicate success. All other status codes indicate the type of error that occurred.
        
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

    def list_items(self, Path: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/ListItems>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_items(
              Path=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Path: string
        :param Path: 
        
          The path in the container from which to retrieve items. Format: <folder name>/<folder name>/<file name>
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return per API request. For example, you submit a ``ListItems`` request with ``MaxResults`` set at 500. Although 2,000 items match your request, the service returns no more than the first 500 items. (The service also returns a ``NextToken`` value that you can use to fetch the next batch of results.) The service might return fewer results than the ``MaxResults`` value.
        
          If ``MaxResults`` is not included in the request, the service defaults to pagination with a maximum of 1,000 results per page.
        
        :type NextToken: string
        :param NextToken: 
        
          The token that identifies which batch of results that you want to see. For example, you submit a ``ListItems`` request with ``MaxResults`` set at 500. The service returns the first batch of results (up to 500) and a ``NextToken`` value. To see the next batch of results, you can submit the ``ListItems`` request a second time and specify the ``NextToken`` value.
        
          Tokens expire after 15 minutes.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Items\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'OBJECT\'|\'FOLDER\',
                        \'ETag\': \'string\',
                        \'LastModified\': datetime(2015, 1, 1),
                        \'ContentType\': \'string\',
                        \'ContentLength\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Items** *(list) --* 
        
              The metadata entries for the folders and objects at the requested path.
        
              - *(dict) --* 
        
                A metadata entry for a folder or object.
        
                - **Name** *(string) --* 
        
                  The name of the item.
        
                - **Type** *(string) --* 
        
                  The item type (folder or object).
        
                - **ETag** *(string) --* 
        
                  The ETag that represents a unique instance of the item.
        
                - **LastModified** *(datetime) --* 
        
                  The date and time that the item was last modified.
        
                - **ContentType** *(string) --* 
        
                  The content type of the item.
        
                - **ContentLength** *(integer) --* 
        
                  The length of the item in bytes.
        
            - **NextToken** *(string) --* 
        
              The token that can be used in a request to view the next set of results. For example, you submit a ``ListItems`` request that matches 2,000 items with ``MaxResults`` set at 500. The service returns the first batch of results (up to 500) and a ``NextToken`` value that can be used to fetch the next batch of results.
        
        """
        pass

    def put_object(self, Body: Union[bytes, IO], Path: str, ContentType: str = None, CacheControl: str = None, StorageClass: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/PutObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_object(
              Body=b\'bytes\'|file,
              Path=\'string\',
              ContentType=\'string\',
              CacheControl=\'string\',
              StorageClass=\'TEMPORAL\'
          )
        :type Body: bytes or seekable file-like object
        :param Body: **[REQUIRED]** 
        
          The bytes to be stored. 
        
        :type Path: string
        :param Path: **[REQUIRED]** 
        
          The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>
        
          For example, to upload the file ``mlaw.avi`` to the folder path ``premium\canada`` in the container ``movies`` , enter the path ``premium/canada/mlaw.avi`` .
        
          Do not include the container name in this path.
        
          If the path includes any folders that don\'t exist yet, the service creates them. For example, suppose you have an existing ``premium/usa`` subfolder. If you specify ``premium/canada`` , the service creates a ``canada`` subfolder in the ``premium`` folder. You then have two subfolders, ``usa`` and ``canada`` , in the ``premium`` folder. 
        
          There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.
        
          For more information about folders and how they exist in a container, see the `AWS Elemental MediaStore User Guide <http://docs.aws.amazon.com/mediastore/latest/ug/>`__ .
        
          The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. 
        
        :type ContentType: string
        :param ContentType: 
        
          The content type of the object.
        
        :type CacheControl: string
        :param CacheControl: 
        
          An optional ``CacheControl`` header that allows the caller to control the object\'s cache behavior. Headers can be passed in as specified in the HTTP at `https\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .
        
          Headers with a custom user-defined value are also accepted.
        
        :type StorageClass: string
        :param StorageClass: 
        
          Indicates the storage class of a ``Put`` request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ContentSHA256\': \'string\',
                \'ETag\': \'string\',
                \'StorageClass\': \'TEMPORAL\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ContentSHA256** *(string) --* 
        
              The SHA256 digest of the object that is persisted.
        
            - **ETag** *(string) --* 
        
              Unique identifier of the object in the container.
        
            - **StorageClass** *(string) --* 
        
              The storage class where the object was persisted. The class should be “Temporal”.
        
        """
        pass
