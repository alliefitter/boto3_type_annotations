from typing import Dict
from botocore.paginate import Paginator


class ListEntitlements(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MediaConnect.Client.list_entitlements`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/ListEntitlements>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Entitlements': [
                    {
                        'EntitlementArn': 'string',
                        'EntitlementName': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* AWS Elemental MediaConnect returned the list of entitlements successfully.
            - **Entitlements** *(list) --* A list of entitlements that have been granted to you from other AWS accounts.
              - *(dict) --* An entitlement that has been granted to you from other AWS accounts.
                - **EntitlementArn** *(string) --* The ARN of the entitlement.
                - **EntitlementName** *(string) --* The name of the entitlement.
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


class ListFlows(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MediaConnect.Client.list_flows`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/ListFlows>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Flows': [
                    {
                        'AvailabilityZone': 'string',
                        'Description': 'string',
                        'FlowArn': 'string',
                        'Name': 'string',
                        'SourceType': 'OWNED'|'ENTITLED',
                        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* AWS Elemental MediaConnect returned the list of flows successfully.
            - **Flows** *(list) --* A list of flow summaries.
              - *(dict) --* Provides a summary of a flow, including its ARN, Availability Zone, and source type.
                - **AvailabilityZone** *(string) --* The Availability Zone that the flow was created in.
                - **Description** *(string) --* A description of the flow.
                - **FlowArn** *(string) --* The ARN of the flow.
                - **Name** *(string) --* The name of the flow.
                - **SourceType** *(string) --* The type of source. This value is either owned (originated somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).
                - **Status** *(string) --* The current status of the flow.
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
