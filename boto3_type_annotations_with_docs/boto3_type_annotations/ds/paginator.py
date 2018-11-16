from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeDomainControllers(Paginator):
    def paginate(self, DirectoryId: str, DomainControllerIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeDomainControllers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryId=\'string\',
              DomainControllerIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier of the directory for which to retrieve the domain controller information.
        
        :type DomainControllerIds: list
        :param DomainControllerIds: 
        
          A list of identifiers for the domain controllers whose information will be provided.
        
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
                \'DomainControllers\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'DomainControllerId\': \'string\',
                        \'DnsIpAddr\': \'string\',
                        \'VpcId\': \'string\',
                        \'SubnetId\': \'string\',
                        \'AvailabilityZone\': \'string\',
                        \'Status\': \'Creating\'|\'Active\'|\'Impaired\'|\'Restoring\'|\'Deleting\'|\'Deleted\'|\'Failed\',
                        \'StatusReason\': \'string\',
                        \'LaunchTime\': datetime(2015, 1, 1),
                        \'StatusLastUpdatedDateTime\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DomainControllers** *(list) --* 
        
              List of the  DomainController objects that were retrieved.
        
              - *(dict) --* 
        
                Contains information about the domain controllers for a specified directory.
        
                - **DirectoryId** *(string) --* 
        
                  Identifier of the directory where the domain controller resides.
        
                - **DomainControllerId** *(string) --* 
        
                  Identifies a specific domain controller in the directory.
        
                - **DnsIpAddr** *(string) --* 
        
                  The IP address of the domain controller.
        
                - **VpcId** *(string) --* 
        
                  The identifier of the VPC that contains the domain controller.
        
                - **SubnetId** *(string) --* 
        
                  Identifier of the subnet in the VPC that contains the domain controller.
        
                - **AvailabilityZone** *(string) --* 
        
                  The Availability Zone where the domain controller is located.
        
                - **Status** *(string) --* 
        
                  The status of the domain controller.
        
                - **StatusReason** *(string) --* 
        
                  A description of the domain controller state.
        
                - **LaunchTime** *(datetime) --* 
        
                  Specifies when the domain controller was created.
        
                - **StatusLastUpdatedDateTime** *(datetime) --* 
        
                  The date and time that the status was last updated.
        
        """
        pass
