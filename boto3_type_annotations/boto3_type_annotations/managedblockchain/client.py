from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_member(self, ClientRequestToken: str, InvitationId: str, NetworkId: str, MemberConfiguration: Dict) -> Dict:
        pass

    def create_network(self, ClientRequestToken: str, Name: str, Framework: str, FrameworkVersion: str, VotingPolicy: Dict, MemberConfiguration: Dict, Description: str = None, FrameworkConfiguration: Dict = None) -> Dict:
        pass

    def create_node(self, ClientRequestToken: str, NetworkId: str, MemberId: str, NodeConfiguration: Dict) -> Dict:
        pass

    def create_proposal(self, ClientRequestToken: str, NetworkId: str, MemberId: str, Actions: Dict, Description: str = None) -> Dict:
        pass

    def delete_member(self, NetworkId: str, MemberId: str) -> Dict:
        pass

    def delete_node(self, NetworkId: str, MemberId: str, NodeId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_member(self, NetworkId: str, MemberId: str) -> Dict:
        pass

    def get_network(self, NetworkId: str) -> Dict:
        pass

    def get_node(self, NetworkId: str, MemberId: str, NodeId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_proposal(self, NetworkId: str, ProposalId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_invitations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_members(self, NetworkId: str, Name: str = None, Status: str = None, IsOwned: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_networks(self, Name: str = None, Framework: str = None, Status: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_nodes(self, NetworkId: str, MemberId: str, Status: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_proposal_votes(self, NetworkId: str, ProposalId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_proposals(self, NetworkId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def reject_invitation(self, InvitationId: str) -> Dict:
        pass

    def vote_on_proposal(self, NetworkId: str, ProposalId: str, VoterMemberId: str, Vote: str) -> Dict:
        pass
