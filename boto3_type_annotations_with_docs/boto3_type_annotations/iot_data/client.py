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

    def delete_thing_shadow(self, thingName: str) -> Dict:
        """
        
        For more information, see `DeleteThingShadow <http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html>`__ in the *AWS IoT Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/DeleteThingShadow>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_thing_shadow(
              thingName=\'string\'
          )
        :type thingName: string
        :param thingName: **[REQUIRED]** 
        
          The name of the thing.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'payload\': StreamingBody()
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the DeleteThingShadow operation.
        
            - **payload** (:class:`.StreamingBody`) -- 
        
              The state information, in JSON format.
        
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

    def get_thing_shadow(self, thingName: str) -> Dict:
        """
        
        For more information, see `GetThingShadow <http://docs.aws.amazon.com/iot/latest/developerguide/API_GetThingShadow.html>`__ in the *AWS IoT Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/GetThingShadow>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_thing_shadow(
              thingName=\'string\'
          )
        :type thingName: string
        :param thingName: **[REQUIRED]** 
        
          The name of the thing.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'payload\': StreamingBody()
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the GetThingShadow operation.
        
            - **payload** (:class:`.StreamingBody`) -- 
        
              The state information, in JSON format.
        
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

    def publish(self, topic: str, qos: int = None, payload: Union[bytes, IO] = None) -> NoReturn:
        """
        
        For more information, see `HTTP Protocol <http://docs.aws.amazon.com/iot/latest/developerguide/protocols.html#http>`__ in the *AWS IoT Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/Publish>`_
        
        **Request Syntax** 
        ::
        
          response = client.publish(
              topic=\'string\',
              qos=123,
              payload=b\'bytes\'|file
          )
        :type topic: string
        :param topic: **[REQUIRED]** 
        
          The name of the MQTT topic.
        
        :type qos: integer
        :param qos: 
        
          The Quality of Service (QoS) level.
        
        :type payload: bytes or seekable file-like object
        :param payload: 
        
          The state information, in JSON format.
        
        :returns: None
        """
        pass

    def update_thing_shadow(self, thingName: str, payload: Union[bytes, IO]) -> Dict:
        """
        
        For more information, see `UpdateThingShadow <http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html>`__ in the *AWS IoT Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/UpdateThingShadow>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_thing_shadow(
              thingName=\'string\',
              payload=b\'bytes\'|file
          )
        :type thingName: string
        :param thingName: **[REQUIRED]** 
        
          The name of the thing.
        
        :type payload: bytes or seekable file-like object
        :param payload: **[REQUIRED]** 
        
          The state information, in JSON format.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'payload\': StreamingBody()
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the UpdateThingShadow operation.
        
            - **payload** (:class:`.StreamingBody`) -- 
        
              The state information, in JSON format.
        
        """
        pass
