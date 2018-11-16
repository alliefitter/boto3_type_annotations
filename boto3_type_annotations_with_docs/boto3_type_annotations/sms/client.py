from datetime import datetime
from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


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

    def create_replication_job(self, serverId: str, seedReplicationTime: datetime, frequency: int, licenseType: str = None, roleName: str = None, description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/CreateReplicationJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_replication_job(
              serverId=\'string\',
              seedReplicationTime=datetime(2015, 1, 1),
              frequency=123,
              licenseType=\'AWS\'|\'BYOL\',
              roleName=\'string\',
              description=\'string\'
          )
        :type serverId: string
        :param serverId: **[REQUIRED]** Unique Identifier for a server
        
        :type seedReplicationTime: datetime
        :param seedReplicationTime: **[REQUIRED]** Timestamp of an operation
        
        :type frequency: integer
        :param frequency: **[REQUIRED]** Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
        
        :type licenseType: string
        :param licenseType: The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
        
        :type roleName: string
        :param roleName: Name of service role in customer\'s account to be used by SMS service.
        
        :type description: string
        :param description: The description for a Replication Job/Run.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'replicationJobId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **replicationJobId** *(string) --* The unique identifier for a Replication Job.
        """
        pass

    def delete_replication_job(self, replicationJobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteReplicationJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_replication_job(
              replicationJobId=\'string\'
          )
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_server_catalog(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteServerCatalog>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_server_catalog()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_connector(self, connectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DisassociateConnector>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_connector(
              connectorId=\'string\'
          )
        :type connectorId: string
        :param connectorId: **[REQUIRED]** Unique Identifier for Connector
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
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

    def get_connectors(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetConnectors>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_connectors(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: Pagination token to pass as input to API call
        
        :type maxResults: integer
        :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.
        
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
                \'nextToken\': \'string\'
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
            
            - **nextToken** *(string) --* Pagination token to pass as input to API call
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

    def get_replication_jobs(self, replicationJobId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_replication_jobs(
              replicationJobId=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type replicationJobId: string
        :param replicationJobId: The unique identifier for a Replication Job.
        
        :type nextToken: string
        :param nextToken: Pagination token to pass as input to API call
        
        :type maxResults: integer
        :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.
        
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
                \'nextToken\': \'string\'
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
                
            - **nextToken** *(string) --* Pagination token to pass as input to API call
        """
        pass

    def get_replication_runs(self, replicationJobId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationRuns>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_replication_runs(
              replicationJobId=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.
        
        :type nextToken: string
        :param nextToken: Pagination token to pass as input to API call
        
        :type maxResults: integer
        :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.
        
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
                \'nextToken\': \'string\'
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
            
            - **nextToken** *(string) --* Pagination token to pass as input to API call
        """
        pass

    def get_servers(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetServers>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_servers(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: Pagination token to pass as input to API call
        
        :type maxResults: integer
        :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.
        
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
                \'nextToken\': \'string\'
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
            
            - **nextToken** *(string) --* Pagination token to pass as input to API call
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

    def import_server_catalog(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/ImportServerCatalog>`_
        
        **Request Syntax** 
        ::
        
          response = client.import_server_catalog()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def start_on_demand_replication_run(self, replicationJobId: str, description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/StartOnDemandReplicationRun>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_on_demand_replication_run(
              replicationJobId=\'string\',
              description=\'string\'
          )
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.
        
        :type description: string
        :param description: The description for a Replication Job/Run.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'replicationRunId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **replicationRunId** *(string) --* The unique identifier for a Replication Run.
        """
        pass

    def update_replication_job(self, replicationJobId: str, frequency: int = None, nextReplicationRunStartTime: datetime = None, licenseType: str = None, roleName: str = None, description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/UpdateReplicationJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_replication_job(
              replicationJobId=\'string\',
              frequency=123,
              nextReplicationRunStartTime=datetime(2015, 1, 1),
              licenseType=\'AWS\'|\'BYOL\',
              roleName=\'string\',
              description=\'string\'
          )
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]** The unique identifier for a Replication Job.
        
        :type frequency: integer
        :param frequency: Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
        
        :type nextReplicationRunStartTime: datetime
        :param nextReplicationRunStartTime: Timestamp of an operation
        
        :type licenseType: string
        :param licenseType: The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
        
        :type roleName: string
        :param roleName: Name of service role in customer\'s account to be used by SMS service.
        
        :type description: string
        :param description: The description for a Replication Job/Run.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
