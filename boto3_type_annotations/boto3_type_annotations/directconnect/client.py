from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def allocate_connection_on_interconnect(self, bandwidth: str, connectionName: str, ownerAccount: str, interconnectId: str, vlan: int) -> Dict:
        pass

    def allocate_hosted_connection(self, connectionId: str, ownerAccount: str, bandwidth: str, connectionName: str, vlan: int) -> Dict:
        pass

    def allocate_private_virtual_interface(self, connectionId: str, ownerAccount: str, newPrivateVirtualInterfaceAllocation: Dict) -> Dict:
        pass

    def allocate_public_virtual_interface(self, connectionId: str, ownerAccount: str, newPublicVirtualInterfaceAllocation: Dict) -> Dict:
        pass

    def associate_connection_with_lag(self, connectionId: str, lagId: str) -> Dict:
        pass

    def associate_hosted_connection(self, connectionId: str, parentConnectionId: str) -> Dict:
        pass

    def associate_virtual_interface(self, virtualInterfaceId: str, connectionId: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def confirm_connection(self, connectionId: str) -> Dict:
        pass

    def confirm_private_virtual_interface(self, virtualInterfaceId: str, virtualGatewayId: str = None, directConnectGatewayId: str = None) -> Dict:
        pass

    def confirm_public_virtual_interface(self, virtualInterfaceId: str) -> Dict:
        pass

    def create_bgp_peer(self, virtualInterfaceId: str = None, newBGPPeer: Dict = None) -> Dict:
        pass

    def create_connection(self, location: str, bandwidth: str, connectionName: str, lagId: str = None) -> Dict:
        pass

    def create_direct_connect_gateway(self, directConnectGatewayName: str, amazonSideAsn: int = None) -> Dict:
        pass

    def create_direct_connect_gateway_association(self, directConnectGatewayId: str, virtualGatewayId: str) -> Dict:
        pass

    def create_interconnect(self, interconnectName: str, bandwidth: str, location: str, lagId: str = None) -> Dict:
        pass

    def create_lag(self, numberOfConnections: int, location: str, connectionsBandwidth: str, lagName: str, connectionId: str = None) -> Dict:
        pass

    def create_private_virtual_interface(self, connectionId: str, newPrivateVirtualInterface: Dict) -> Dict:
        pass

    def create_public_virtual_interface(self, connectionId: str, newPublicVirtualInterface: Dict) -> Dict:
        pass

    def delete_bgp_peer(self, virtualInterfaceId: str = None, asn: int = None, customerAddress: str = None) -> Dict:
        pass

    def delete_connection(self, connectionId: str) -> Dict:
        pass

    def delete_direct_connect_gateway(self, directConnectGatewayId: str) -> Dict:
        pass

    def delete_direct_connect_gateway_association(self, directConnectGatewayId: str, virtualGatewayId: str) -> Dict:
        pass

    def delete_interconnect(self, interconnectId: str) -> Dict:
        pass

    def delete_lag(self, lagId: str) -> Dict:
        pass

    def delete_virtual_interface(self, virtualInterfaceId: str) -> Dict:
        pass

    def describe_connection_loa(self, connectionId: str, providerName: str = None, loaContentType: str = None) -> Dict:
        pass

    def describe_connections(self, connectionId: str = None) -> Dict:
        pass

    def describe_connections_on_interconnect(self, interconnectId: str) -> Dict:
        pass

    def describe_direct_connect_gateway_associations(self, directConnectGatewayId: str = None, virtualGatewayId: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_direct_connect_gateway_attachments(self, directConnectGatewayId: str = None, virtualInterfaceId: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_direct_connect_gateways(self, directConnectGatewayId: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_hosted_connections(self, connectionId: str) -> Dict:
        pass

    def describe_interconnect_loa(self, interconnectId: str, providerName: str = None, loaContentType: str = None) -> Dict:
        pass

    def describe_interconnects(self, interconnectId: str = None) -> Dict:
        pass

    def describe_lags(self, lagId: str = None) -> Dict:
        pass

    def describe_loa(self, connectionId: str, providerName: str = None, loaContentType: str = None) -> Dict:
        pass

    def describe_locations(self) -> Dict:
        pass

    def describe_tags(self, resourceArns: List) -> Dict:
        pass

    def describe_virtual_gateways(self) -> Dict:
        pass

    def describe_virtual_interfaces(self, connectionId: str = None, virtualInterfaceId: str = None) -> Dict:
        pass

    def disassociate_connection_from_lag(self, connectionId: str, lagId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def tag_resource(self, resourceArn: str, tags: List) -> Dict:
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        pass

    def update_lag(self, lagId: str, lagName: str = None, minimumLinks: int = None) -> Dict:
        pass

    def update_virtual_interface_attributes(self, virtualInterfaceId: str, mtu: int = None) -> Dict:
        pass
