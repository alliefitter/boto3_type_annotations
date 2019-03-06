from typing import Dict
from botocore.paginate import Paginator


class DescribeDirectConnectGatewayAssociations(Paginator):
    def paginate(self, directConnectGatewayId: str = None, virtualGatewayId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectConnect.Client.describe_direct_connect_gateway_associations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              directConnectGatewayId='string',
              virtualGatewayId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'directConnectGatewayAssociations': [
                    {
                        'directConnectGatewayId': 'string',
                        'virtualGatewayId': 'string',
                        'virtualGatewayRegion': 'string',
                        'virtualGatewayOwnerAccount': 'string',
                        'associationState': 'associating'|'associated'|'disassociating'|'disassociated',
                        'stateChangeError': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **directConnectGatewayAssociations** *(list) --* 
              The associations.
              - *(dict) --* 
                Information about an association between a Direct Connect gateway and a virtual private gateway.
                - **directConnectGatewayId** *(string) --* 
                  The ID of the Direct Connect gateway.
                - **virtualGatewayId** *(string) --* 
                  The ID of the virtual private gateway. Applies only to private virtual interfaces.
                - **virtualGatewayRegion** *(string) --* 
                  The AWS Region where the virtual private gateway is located.
                - **virtualGatewayOwnerAccount** *(string) --* 
                  The ID of the AWS account that owns the virtual private gateway.
                - **associationState** *(string) --* 
                  The state of the association. The following are the possible values:
                  * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation . 
                  * ``associated`` : The Direct Connect gateway and virtual private gateway are successfully associated and ready to pass traffic. 
                  * ``disassociating`` : The initial state after calling  DeleteDirectConnectGatewayAssociation . 
                  * ``disassociated`` : The virtual private gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway is stopped. 
                - **stateChangeError** *(string) --* 
                  The error message if the state of an object failed to advance.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type directConnectGatewayId: string
        :param directConnectGatewayId:
          The ID of the Direct Connect gateway.
        :type virtualGatewayId: string
        :param virtualGatewayId:
          The ID of the virtual private gateway.
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
        """
        pass


class DescribeDirectConnectGatewayAttachments(Paginator):
    def paginate(self, directConnectGatewayId: str = None, virtualInterfaceId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectConnect.Client.describe_direct_connect_gateway_attachments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              directConnectGatewayId='string',
              virtualInterfaceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'directConnectGatewayAttachments': [
                    {
                        'directConnectGatewayId': 'string',
                        'virtualInterfaceId': 'string',
                        'virtualInterfaceRegion': 'string',
                        'virtualInterfaceOwnerAccount': 'string',
                        'attachmentState': 'attaching'|'attached'|'detaching'|'detached',
                        'stateChangeError': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **directConnectGatewayAttachments** *(list) --* 
              The attachments.
              - *(dict) --* 
                Information about an attachment between a Direct Connect gateway and a virtual interface.
                - **directConnectGatewayId** *(string) --* 
                  The ID of the Direct Connect gateway.
                - **virtualInterfaceId** *(string) --* 
                  The ID of the virtual interface.
                - **virtualInterfaceRegion** *(string) --* 
                  The AWS Region where the virtual interface is located.
                - **virtualInterfaceOwnerAccount** *(string) --* 
                  The ID of the AWS account that owns the virtual interface.
                - **attachmentState** *(string) --* 
                  The state of the attachment. The following are the possible values:
                  * ``attaching`` : The initial state after a virtual interface is created using the Direct Connect gateway. 
                  * ``attached`` : The Direct Connect gateway and virtual interface are attached and ready to pass traffic. 
                  * ``detaching`` : The initial state after calling  DeleteVirtualInterface . 
                  * ``detached`` : The virtual interface is detached from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual interface is stopped. 
                - **stateChangeError** *(string) --* 
                  The error message if the state of an object failed to advance.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type directConnectGatewayId: string
        :param directConnectGatewayId:
          The ID of the Direct Connect gateway.
        :type virtualInterfaceId: string
        :param virtualInterfaceId:
          The ID of the virtual interface.
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
        """
        pass


class DescribeDirectConnectGateways(Paginator):
    def paginate(self, directConnectGatewayId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectConnect.Client.describe_direct_connect_gateways`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeDirectConnectGateways>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              directConnectGatewayId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'directConnectGateways': [
                    {
                        'directConnectGatewayId': 'string',
                        'directConnectGatewayName': 'string',
                        'amazonSideAsn': 123,
                        'ownerAccount': 'string',
                        'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
                        'stateChangeError': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **directConnectGateways** *(list) --* 
              The Direct Connect gateways.
              - *(dict) --* 
                Information about a Direct Connect gateway, which enables you to connect virtual interfaces and virtual private gateways.
                - **directConnectGatewayId** *(string) --* 
                  The ID of the Direct Connect gateway.
                - **directConnectGatewayName** *(string) --* 
                  The name of the Direct Connect gateway.
                - **amazonSideAsn** *(integer) --* 
                  The autonomous system number (ASN) for the Amazon side of the connection.
                - **ownerAccount** *(string) --* 
                  The ID of the AWS account that owns the Direct Connect gateway.
                - **directConnectGatewayState** *(string) --* 
                  The state of the Direct Connect gateway. The following are the possible values:
                  * ``pending`` : The initial state after calling  CreateDirectConnectGateway . 
                  * ``available`` : The Direct Connect gateway is ready for use. 
                  * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway . 
                  * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic. 
                - **stateChangeError** *(string) --* 
                  The error message if the state of an object failed to advance.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type directConnectGatewayId: string
        :param directConnectGatewayId:
          The ID of the Direct Connect gateway.
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
        """
        pass
