from typing import Dict
from botocore.paginate import Paginator


class GetConnectors(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetConnectors>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'connectorList\': [
                    {
                        \'connectorId\': \'string\',
                        \'version\': \'string\',
                        \'status\': \'HEALTHY\'|\'UNHEALTHY\',
                        \'capabilityList\': [
                            \'VSPHERE\',
                        ],
                        \'vmManagerName\': \'string\',
                        \'vmManagerType\': \'VSPHERE\',
                        \'vmManagerId\': \'string\',
                        \'ipAddress\': \'string\',
                        \'macAddress\': \'string\',
                        \'associatedOn\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **connectorList** *(list) --* List of connectors
              
              - *(dict) --* Object representing a Connector
                
                - **connectorId** *(string) --* Unique Identifier for Connector
                
                - **version** *(string) --* Connector version string
                
                - **status** *(string) --* Status of on-premise Connector
                
                - **capabilityList** *(list) --* List of Connector Capabilities
                  
                  - *(string) --* Capabilities for a Connector
              
                - **vmManagerName** *(string) --* VM Manager Name
                
                - **vmManagerType** *(string) --* VM Management Product
                
                - **vmManagerId** *(string) --* Unique Identifier for VM Manager
                
                - **ipAddress** *(string) --* Internet Protocol (IP) Address
                
                - **macAddress** *(string) --* Hardware (MAC) address
                
                - **associatedOn** *(datetime) --* Timestamp of an operation
            
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetReplicationJobs(Paginator):
    def paginate(self, replicationJobId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationJobs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              replicationJobId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type replicationJobId: string
        :param replicationJobId: The unique identifier for a Replication Job.
        
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
                \'replicationJobList\': [
                    {
                        \'replicationJobId\': \'string\',
                        \'serverId\': \'string\',
                        \'serverType\': \'VIRTUAL_MACHINE\',
                        \'vmServer\': {
                            \'vmServerAddress\': {
                                \'vmManagerId\': \'string\',
                                \'vmId\': \'string\'
                            },
                            \'vmName\': \'string\',
                            \'vmManagerName\': \'string\',
                            \'vmManagerType\': \'VSPHERE\',
                            \'vmPath\': \'string\'
                        },
                        \'seedReplicationTime\': datetime(2015, 1, 1),
                        \'frequency\': 123,
                        \'nextReplicationRunStartTime\': datetime(2015, 1, 1),
                        \'licenseType\': \'AWS\'|\'BYOL\',
                        \'roleName\': \'string\',
                        \'latestAmiId\': \'string\',
                        \'state\': \'PENDING\'|\'ACTIVE\'|\'FAILED\'|\'DELETING\'|\'DELETED\',
                        \'statusMessage\': \'string\',
                        \'description\': \'string\',
                        \'replicationRunList\': [
                            {
                                \'replicationRunId\': \'string\',
                                \'state\': \'PENDING\'|\'MISSED\'|\'ACTIVE\'|\'FAILED\'|\'COMPLETED\'|\'DELETING\'|\'DELETED\',
                                \'type\': \'ON_DEMAND\'|\'AUTOMATIC\',
                                \'statusMessage\': \'string\',
                                \'amiId\': \'string\',
                                \'scheduledStartTime\': datetime(2015, 1, 1),
                                \'completedTime\': datetime(2015, 1, 1),
                                \'description\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **replicationJobList** *(list) --* List of Replication Jobs
              
              - *(dict) --* Object representing a Replication Job
                
                - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
                
                - **serverId** *(string) --* Unique Identifier for a server
                
                - **serverType** *(string) --* Type of server.
                
                - **vmServer** *(dict) --* Object representing a VM server
                  
                  - **vmServerAddress** *(dict) --* Object representing a server\'s location
                    
                    - **vmManagerId** *(string) --* Unique Identifier for VM Manager
                    
                    - **vmId** *(string) --* Unique Identifier for a VM
                
                  - **vmName** *(string) --* Name of Virtual Machine
                  
                  - **vmManagerName** *(string) --* VM Manager Name
                  
                  - **vmManagerType** *(string) --* VM Management Product
                  
                  - **vmPath** *(string) --* Path to VM
              
                - **seedReplicationTime** *(datetime) --* Timestamp of an operation
                
                - **frequency** *(integer) --* Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
                
                - **nextReplicationRunStartTime** *(datetime) --* Timestamp of an operation
                
                - **licenseType** *(string) --* The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
                
                - **roleName** *(string) --* Name of service role in customer\'s account to be used by SMS service.
                
                - **latestAmiId** *(string) --* The AMI id for the image resulting from a Replication Run.
                
                - **state** *(string) --* Current state of Replication Job
                
                - **statusMessage** *(string) --* String describing current status of Replication Job
                
                - **description** *(string) --* The description for a Replication Job/Run.
                
                - **replicationRunList** *(list) --* List of Replication Runs
                  
                  - *(dict) --* Object representing a Replication Run
                    
                    - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
                    
                    - **state** *(string) --* Current state of Replication Run
                    
                    - **type** *(string) --* Type of Replication Run
                    
                    - **statusMessage** *(string) --* String describing current status of Replication Run
                    
                    - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
                    
                    - **scheduledStartTime** *(datetime) --* Timestamp of an operation
                    
                    - **completedTime** *(datetime) --* Timestamp of an operation
                    
                    - **description** *(string) --* The description for a Replication Job/Run.
                
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetReplicationRuns(Paginator):
    def paginate(self, replicationJobId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationRuns>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              replicationJobId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.
        
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
                \'replicationJob\': {
                    \'replicationJobId\': \'string\',
                    \'serverId\': \'string\',
                    \'serverType\': \'VIRTUAL_MACHINE\',
                    \'vmServer\': {
                        \'vmServerAddress\': {
                            \'vmManagerId\': \'string\',
                            \'vmId\': \'string\'
                        },
                        \'vmName\': \'string\',
                        \'vmManagerName\': \'string\',
                        \'vmManagerType\': \'VSPHERE\',
                        \'vmPath\': \'string\'
                    },
                    \'seedReplicationTime\': datetime(2015, 1, 1),
                    \'frequency\': 123,
                    \'nextReplicationRunStartTime\': datetime(2015, 1, 1),
                    \'licenseType\': \'AWS\'|\'BYOL\',
                    \'roleName\': \'string\',
                    \'latestAmiId\': \'string\',
                    \'state\': \'PENDING\'|\'ACTIVE\'|\'FAILED\'|\'DELETING\'|\'DELETED\',
                    \'statusMessage\': \'string\',
                    \'description\': \'string\',
                    \'replicationRunList\': [
                        {
                            \'replicationRunId\': \'string\',
                            \'state\': \'PENDING\'|\'MISSED\'|\'ACTIVE\'|\'FAILED\'|\'COMPLETED\'|\'DELETING\'|\'DELETED\',
                            \'type\': \'ON_DEMAND\'|\'AUTOMATIC\',
                            \'statusMessage\': \'string\',
                            \'amiId\': \'string\',
                            \'scheduledStartTime\': datetime(2015, 1, 1),
                            \'completedTime\': datetime(2015, 1, 1),
                            \'description\': \'string\'
                        },
                    ]
                },
                \'replicationRunList\': [
                    {
                        \'replicationRunId\': \'string\',
                        \'state\': \'PENDING\'|\'MISSED\'|\'ACTIVE\'|\'FAILED\'|\'COMPLETED\'|\'DELETING\'|\'DELETED\',
                        \'type\': \'ON_DEMAND\'|\'AUTOMATIC\',
                        \'statusMessage\': \'string\',
                        \'amiId\': \'string\',
                        \'scheduledStartTime\': datetime(2015, 1, 1),
                        \'completedTime\': datetime(2015, 1, 1),
                        \'description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **replicationJob** *(dict) --* Object representing a Replication Job
              
              - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
              
              - **serverId** *(string) --* Unique Identifier for a server
              
              - **serverType** *(string) --* Type of server.
              
              - **vmServer** *(dict) --* Object representing a VM server
                
                - **vmServerAddress** *(dict) --* Object representing a server\'s location
                  
                  - **vmManagerId** *(string) --* Unique Identifier for VM Manager
                  
                  - **vmId** *(string) --* Unique Identifier for a VM
              
                - **vmName** *(string) --* Name of Virtual Machine
                
                - **vmManagerName** *(string) --* VM Manager Name
                
                - **vmManagerType** *(string) --* VM Management Product
                
                - **vmPath** *(string) --* Path to VM
            
              - **seedReplicationTime** *(datetime) --* Timestamp of an operation
              
              - **frequency** *(integer) --* Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
              
              - **nextReplicationRunStartTime** *(datetime) --* Timestamp of an operation
              
              - **licenseType** *(string) --* The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
              
              - **roleName** *(string) --* Name of service role in customer\'s account to be used by SMS service.
              
              - **latestAmiId** *(string) --* The AMI id for the image resulting from a Replication Run.
              
              - **state** *(string) --* Current state of Replication Job
              
              - **statusMessage** *(string) --* String describing current status of Replication Job
              
              - **description** *(string) --* The description for a Replication Job/Run.
              
              - **replicationRunList** *(list) --* List of Replication Runs
                
                - *(dict) --* Object representing a Replication Run
                  
                  - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
                  
                  - **state** *(string) --* Current state of Replication Run
                  
                  - **type** *(string) --* Type of Replication Run
                  
                  - **statusMessage** *(string) --* String describing current status of Replication Run
                  
                  - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
                  
                  - **scheduledStartTime** *(datetime) --* Timestamp of an operation
                  
                  - **completedTime** *(datetime) --* Timestamp of an operation
                  
                  - **description** *(string) --* The description for a Replication Job/Run.
              
            - **replicationRunList** *(list) --* List of Replication Runs
              
              - *(dict) --* Object representing a Replication Run
                
                - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
                
                - **state** *(string) --* Current state of Replication Run
                
                - **type** *(string) --* Type of Replication Run
                
                - **statusMessage** *(string) --* String describing current status of Replication Run
                
                - **amiId** *(string) --* The AMI id for the image resulting from a Replication Run.
                
                - **scheduledStartTime** *(datetime) --* Timestamp of an operation
                
                - **completedTime** *(datetime) --* Timestamp of an operation
                
                - **description** *(string) --* The description for a Replication Job/Run.
            
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetServers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetServers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'lastModifiedOn\': datetime(2015, 1, 1),
                \'serverCatalogStatus\': \'NOT_IMPORTED\'|\'IMPORTING\'|\'AVAILABLE\'|\'DELETED\'|\'EXPIRED\',
                \'serverList\': [
                    {
                        \'serverId\': \'string\',
                        \'serverType\': \'VIRTUAL_MACHINE\',
                        \'vmServer\': {
                            \'vmServerAddress\': {
                                \'vmManagerId\': \'string\',
                                \'vmId\': \'string\'
                            },
                            \'vmName\': \'string\',
                            \'vmManagerName\': \'string\',
                            \'vmManagerType\': \'VSPHERE\',
                            \'vmPath\': \'string\'
                        },
                        \'replicationJobId\': \'string\',
                        \'replicationJobTerminated\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **lastModifiedOn** *(datetime) --* Timestamp of an operation
            
            - **serverCatalogStatus** *(string) --* Status of Server catalog
            
            - **serverList** *(list) --* List of servers from catalog
              
              - *(dict) --* Object representing a server
                
                - **serverId** *(string) --* Unique Identifier for a server
                
                - **serverType** *(string) --* Type of server.
                
                - **vmServer** *(dict) --* Object representing a VM server
                  
                  - **vmServerAddress** *(dict) --* Object representing a server\'s location
                    
                    - **vmManagerId** *(string) --* Unique Identifier for VM Manager
                    
                    - **vmId** *(string) --* Unique Identifier for a VM
                
                  - **vmName** *(string) --* Name of Virtual Machine
                  
                  - **vmManagerName** *(string) --* VM Manager Name
                  
                  - **vmManagerType** *(string) --* VM Management Product
                  
                  - **vmPath** *(string) --* Path to VM
              
                - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
                
                - **replicationJobTerminated** *(boolean) --* An indicator of the Replication Job being deleted or failed.
            
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
