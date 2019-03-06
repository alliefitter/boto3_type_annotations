from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetConnectors(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.get_connectors`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetConnectors>`_
        
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
                'connectorList': [
                    {
                        'connectorId': 'string',
                        'version': 'string',
                        'status': 'HEALTHY'|'UNHEALTHY',
                        'capabilityList': [
                            'VSPHERE'|'SCVMM'|'HYPERV-MANAGER'|'SNAPSHOT_BATCHING',
                        ],
                        'vmManagerName': 'string',
                        'vmManagerType': 'VSPHERE'|'SCVMM'|'HYPERV-MANAGER',
                        'vmManagerId': 'string',
                        'ipAddress': 'string',
                        'macAddress': 'string',
                        'associatedOn': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **connectorList** *(list) --* 
              Information about the registered connectors.
              - *(dict) --* 
                Represents a connector.
                - **connectorId** *(string) --* 
                  The identifier of the connector.
                - **version** *(string) --* 
                  The connector version.
                - **status** *(string) --* 
                  The status of the connector.
                - **capabilityList** *(list) --* 
                  The capabilities of the connector.
                  - *(string) --* 
                - **vmManagerName** *(string) --* 
                  The name of the VM manager.
                - **vmManagerType** *(string) --* 
                  The VM management product.
                - **vmManagerId** *(string) --* 
                  The identifier of the VM manager.
                - **ipAddress** *(string) --* 
                  The IP address of the connector.
                - **macAddress** *(string) --* 
                  The MAC address of the connector.
                - **associatedOn** *(datetime) --* 
                  The time the connector was associated.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetReplicationJobs(Paginator):
    def paginate(self, replicationJobId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.get_replication_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              replicationJobId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'replicationJobList': [
                    {
                        'replicationJobId': 'string',
                        'serverId': 'string',
                        'serverType': 'VIRTUAL_MACHINE',
                        'vmServer': {
                            'vmServerAddress': {
                                'vmManagerId': 'string',
                                'vmId': 'string'
                            },
                            'vmName': 'string',
                            'vmManagerName': 'string',
                            'vmManagerType': 'VSPHERE'|'SCVMM'|'HYPERV-MANAGER',
                            'vmPath': 'string'
                        },
                        'seedReplicationTime': datetime(2015, 1, 1),
                        'frequency': 123,
                        'runOnce': True|False,
                        'nextReplicationRunStartTime': datetime(2015, 1, 1),
                        'licenseType': 'AWS'|'BYOL',
                        'roleName': 'string',
                        'latestAmiId': 'string',
                        'state': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED'|'COMPLETED'|'PAUSED_ON_FAILURE'|'FAILING',
                        'statusMessage': 'string',
                        'description': 'string',
                        'numberOfRecentAmisToKeep': 123,
                        'encrypted': True|False,
                        'kmsKeyId': 'string',
                        'replicationRunList': [
                            {
                                'replicationRunId': 'string',
                                'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                                'type': 'ON_DEMAND'|'AUTOMATIC',
                                'stageDetails': {
                                    'stage': 'string',
                                    'stageProgress': 'string'
                                },
                                'statusMessage': 'string',
                                'amiId': 'string',
                                'scheduledStartTime': datetime(2015, 1, 1),
                                'completedTime': datetime(2015, 1, 1),
                                'description': 'string',
                                'encrypted': True|False,
                                'kmsKeyId': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **replicationJobList** *(list) --* 
              Information about the replication jobs.
              - *(dict) --* 
                Represents a replication job.
                - **replicationJobId** *(string) --* 
                  The identifier of the replication job.
                - **serverId** *(string) --* 
                  The identifier of the server.
                - **serverType** *(string) --* 
                  The type of server.
                - **vmServer** *(dict) --* 
                  Information about the VM server.
                  - **vmServerAddress** *(dict) --* 
                    Information about the VM server location.
                    - **vmManagerId** *(string) --* 
                      The identifier of the VM manager.
                    - **vmId** *(string) --* 
                      The identifier of the VM.
                  - **vmName** *(string) --* 
                    The name of the VM.
                  - **vmManagerName** *(string) --* 
                    The name of the VM manager.
                  - **vmManagerType** *(string) --* 
                    The type of VM management product.
                  - **vmPath** *(string) --* 
                    The VM folder path in the vCenter Server virtual machine inventory tree.
                - **seedReplicationTime** *(datetime) --* 
                  The seed replication time.
                - **frequency** *(integer) --* 
                  The time between consecutive replication runs, in hours.
                - **runOnce** *(boolean) --* 
                - **nextReplicationRunStartTime** *(datetime) --* 
                  The start time of the next replication run.
                - **licenseType** *(string) --* 
                  The license type to be used for the AMI created by a successful replication run.
                - **roleName** *(string) --* 
                  The name of the IAM role to be used by the Server Migration Service.
                - **latestAmiId** *(string) --* 
                  The ID of the latest Amazon Machine Image (AMI).
                - **state** *(string) --* 
                  The state of the replication job.
                - **statusMessage** *(string) --* 
                  The description of the current status of the replication job.
                - **description** *(string) --* 
                  The description of the replication job.
                - **numberOfRecentAmisToKeep** *(integer) --* 
                  Number of recent AMIs to keep in the customer's account for a replication job. By default the value is set to zero, meaning that all AMIs are kept.
                - **encrypted** *(boolean) --* 
                  Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId`` below.
                - **kmsKeyId** *(string) --* 
                  KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following: 
                  * KMS key ID 
                  * KMS key alias 
                  * ARN referring to KMS key ID 
                  * ARN referring to KMS key alias 
                  If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key for EBS is used. 
                - **replicationRunList** *(list) --* 
                  Information about the replication runs.
                  - *(dict) --* 
                    Represents a replication run.
                    - **replicationRunId** *(string) --* 
                      The identifier of the replication run.
                    - **state** *(string) --* 
                      The state of the replication run.
                    - **type** *(string) --* 
                      The type of replication run.
                    - **stageDetails** *(dict) --* 
                      Details of the current stage of the replication run.
                      - **stage** *(string) --* 
                        String describing the current stage of a replication run.
                      - **stageProgress** *(string) --* 
                        String describing the progress of the current stage of a replication run.
                    - **statusMessage** *(string) --* 
                      The description of the current status of the replication job.
                    - **amiId** *(string) --* 
                      The identifier of the Amazon Machine Image (AMI) from the replication run.
                    - **scheduledStartTime** *(datetime) --* 
                      The start time of the next replication run.
                    - **completedTime** *(datetime) --* 
                      The completion time of the last replication run.
                    - **description** *(string) --* 
                      The description of the replication run.
                    - **encrypted** *(boolean) --* 
                      Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId`` below.
                    - **kmsKeyId** *(string) --* 
                      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following: 
                      * KMS key ID 
                      * KMS key alias 
                      * ARN referring to KMS key ID 
                      * ARN referring to KMS key alias 
                      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key for EBS is used. 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type replicationJobId: string
        :param replicationJobId:
          The identifier of the replication job.
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


class GetReplicationRuns(Paginator):
    def paginate(self, replicationJobId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.get_replication_runs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationRuns>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              replicationJobId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'replicationJob': {
                    'replicationJobId': 'string',
                    'serverId': 'string',
                    'serverType': 'VIRTUAL_MACHINE',
                    'vmServer': {
                        'vmServerAddress': {
                            'vmManagerId': 'string',
                            'vmId': 'string'
                        },
                        'vmName': 'string',
                        'vmManagerName': 'string',
                        'vmManagerType': 'VSPHERE'|'SCVMM'|'HYPERV-MANAGER',
                        'vmPath': 'string'
                    },
                    'seedReplicationTime': datetime(2015, 1, 1),
                    'frequency': 123,
                    'runOnce': True|False,
                    'nextReplicationRunStartTime': datetime(2015, 1, 1),
                    'licenseType': 'AWS'|'BYOL',
                    'roleName': 'string',
                    'latestAmiId': 'string',
                    'state': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED'|'COMPLETED'|'PAUSED_ON_FAILURE'|'FAILING',
                    'statusMessage': 'string',
                    'description': 'string',
                    'numberOfRecentAmisToKeep': 123,
                    'encrypted': True|False,
                    'kmsKeyId': 'string',
                    'replicationRunList': [
                        {
                            'replicationRunId': 'string',
                            'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                            'type': 'ON_DEMAND'|'AUTOMATIC',
                            'stageDetails': {
                                'stage': 'string',
                                'stageProgress': 'string'
                            },
                            'statusMessage': 'string',
                            'amiId': 'string',
                            'scheduledStartTime': datetime(2015, 1, 1),
                            'completedTime': datetime(2015, 1, 1),
                            'description': 'string',
                            'encrypted': True|False,
                            'kmsKeyId': 'string'
                        },
                    ]
                },
                'replicationRunList': [
                    {
                        'replicationRunId': 'string',
                        'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                        'type': 'ON_DEMAND'|'AUTOMATIC',
                        'stageDetails': {
                            'stage': 'string',
                            'stageProgress': 'string'
                        },
                        'statusMessage': 'string',
                        'amiId': 'string',
                        'scheduledStartTime': datetime(2015, 1, 1),
                        'completedTime': datetime(2015, 1, 1),
                        'description': 'string',
                        'encrypted': True|False,
                        'kmsKeyId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **replicationJob** *(dict) --* 
              Information about the replication job.
              - **replicationJobId** *(string) --* 
                The identifier of the replication job.
              - **serverId** *(string) --* 
                The identifier of the server.
              - **serverType** *(string) --* 
                The type of server.
              - **vmServer** *(dict) --* 
                Information about the VM server.
                - **vmServerAddress** *(dict) --* 
                  Information about the VM server location.
                  - **vmManagerId** *(string) --* 
                    The identifier of the VM manager.
                  - **vmId** *(string) --* 
                    The identifier of the VM.
                - **vmName** *(string) --* 
                  The name of the VM.
                - **vmManagerName** *(string) --* 
                  The name of the VM manager.
                - **vmManagerType** *(string) --* 
                  The type of VM management product.
                - **vmPath** *(string) --* 
                  The VM folder path in the vCenter Server virtual machine inventory tree.
              - **seedReplicationTime** *(datetime) --* 
                The seed replication time.
              - **frequency** *(integer) --* 
                The time between consecutive replication runs, in hours.
              - **runOnce** *(boolean) --* 
              - **nextReplicationRunStartTime** *(datetime) --* 
                The start time of the next replication run.
              - **licenseType** *(string) --* 
                The license type to be used for the AMI created by a successful replication run.
              - **roleName** *(string) --* 
                The name of the IAM role to be used by the Server Migration Service.
              - **latestAmiId** *(string) --* 
                The ID of the latest Amazon Machine Image (AMI).
              - **state** *(string) --* 
                The state of the replication job.
              - **statusMessage** *(string) --* 
                The description of the current status of the replication job.
              - **description** *(string) --* 
                The description of the replication job.
              - **numberOfRecentAmisToKeep** *(integer) --* 
                Number of recent AMIs to keep in the customer's account for a replication job. By default the value is set to zero, meaning that all AMIs are kept.
              - **encrypted** *(boolean) --* 
                Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId`` below.
              - **kmsKeyId** *(string) --* 
                KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following: 
                * KMS key ID 
                * KMS key alias 
                * ARN referring to KMS key ID 
                * ARN referring to KMS key alias 
                If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key for EBS is used. 
              - **replicationRunList** *(list) --* 
                Information about the replication runs.
                - *(dict) --* 
                  Represents a replication run.
                  - **replicationRunId** *(string) --* 
                    The identifier of the replication run.
                  - **state** *(string) --* 
                    The state of the replication run.
                  - **type** *(string) --* 
                    The type of replication run.
                  - **stageDetails** *(dict) --* 
                    Details of the current stage of the replication run.
                    - **stage** *(string) --* 
                      String describing the current stage of a replication run.
                    - **stageProgress** *(string) --* 
                      String describing the progress of the current stage of a replication run.
                  - **statusMessage** *(string) --* 
                    The description of the current status of the replication job.
                  - **amiId** *(string) --* 
                    The identifier of the Amazon Machine Image (AMI) from the replication run.
                  - **scheduledStartTime** *(datetime) --* 
                    The start time of the next replication run.
                  - **completedTime** *(datetime) --* 
                    The completion time of the last replication run.
                  - **description** *(string) --* 
                    The description of the replication run.
                  - **encrypted** *(boolean) --* 
                    Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId`` below.
                  - **kmsKeyId** *(string) --* 
                    KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following: 
                    * KMS key ID 
                    * KMS key alias 
                    * ARN referring to KMS key ID 
                    * ARN referring to KMS key alias 
                    If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key for EBS is used. 
            - **replicationRunList** *(list) --* 
              Information about the replication runs.
              - *(dict) --* 
                Represents a replication run.
                - **replicationRunId** *(string) --* 
                  The identifier of the replication run.
                - **state** *(string) --* 
                  The state of the replication run.
                - **type** *(string) --* 
                  The type of replication run.
                - **stageDetails** *(dict) --* 
                  Details of the current stage of the replication run.
                  - **stage** *(string) --* 
                    String describing the current stage of a replication run.
                  - **stageProgress** *(string) --* 
                    String describing the progress of the current stage of a replication run.
                - **statusMessage** *(string) --* 
                  The description of the current status of the replication job.
                - **amiId** *(string) --* 
                  The identifier of the Amazon Machine Image (AMI) from the replication run.
                - **scheduledStartTime** *(datetime) --* 
                  The start time of the next replication run.
                - **completedTime** *(datetime) --* 
                  The completion time of the last replication run.
                - **description** *(string) --* 
                  The description of the replication run.
                - **encrypted** *(boolean) --* 
                  Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId`` below.
                - **kmsKeyId** *(string) --* 
                  KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following: 
                  * KMS key ID 
                  * KMS key alias 
                  * ARN referring to KMS key ID 
                  * ARN referring to KMS key alias 
                  If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key for EBS is used. 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]**
          The identifier of the replication job.
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


class GetServers(Paginator):
    def paginate(self, vmServerAddressList: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.get_servers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetServers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              vmServerAddressList=[
                  {
                      'vmManagerId': 'string',
                      'vmId': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'lastModifiedOn': datetime(2015, 1, 1),
                'serverCatalogStatus': 'NOT_IMPORTED'|'IMPORTING'|'AVAILABLE'|'DELETED'|'EXPIRED',
                'serverList': [
                    {
                        'serverId': 'string',
                        'serverType': 'VIRTUAL_MACHINE',
                        'vmServer': {
                            'vmServerAddress': {
                                'vmManagerId': 'string',
                                'vmId': 'string'
                            },
                            'vmName': 'string',
                            'vmManagerName': 'string',
                            'vmManagerType': 'VSPHERE'|'SCVMM'|'HYPERV-MANAGER',
                            'vmPath': 'string'
                        },
                        'replicationJobId': 'string',
                        'replicationJobTerminated': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **lastModifiedOn** *(datetime) --* 
              The time when the server was last modified.
            - **serverCatalogStatus** *(string) --* 
              The status of the server catalog.
            - **serverList** *(list) --* 
              Information about the servers.
              - *(dict) --* 
                Represents a server.
                - **serverId** *(string) --* 
                  The identifier of the server.
                - **serverType** *(string) --* 
                  The type of server.
                - **vmServer** *(dict) --* 
                  Information about the VM server.
                  - **vmServerAddress** *(dict) --* 
                    Information about the VM server location.
                    - **vmManagerId** *(string) --* 
                      The identifier of the VM manager.
                    - **vmId** *(string) --* 
                      The identifier of the VM.
                  - **vmName** *(string) --* 
                    The name of the VM.
                  - **vmManagerName** *(string) --* 
                    The name of the VM manager.
                  - **vmManagerType** *(string) --* 
                    The type of VM management product.
                  - **vmPath** *(string) --* 
                    The VM folder path in the vCenter Server virtual machine inventory tree.
                - **replicationJobId** *(string) --* 
                  The identifier of the replication job.
                - **replicationJobTerminated** *(boolean) --* 
                  Indicates whether the replication job is deleted or failed.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type vmServerAddressList: list
        :param vmServerAddressList:
          List of ``VmServerAddress`` objects
          - *(dict) --*
            Represents a VM server location.
            - **vmManagerId** *(string) --*
              The identifier of the VM manager.
            - **vmId** *(string) --*
              The identifier of the VM.
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


class ListApps(Paginator):
    def paginate(self, appIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SMS.Client.list_apps`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/ListApps>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              appIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'apps': [
                    {
                        'appId': 'string',
                        'name': 'string',
                        'description': 'string',
                        'status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'DELETED'|'DELETE_FAILED',
                        'statusMessage': 'string',
                        'replicationStatus': 'READY_FOR_CONFIGURATION'|'CONFIGURATION_IN_PROGRESS'|'CONFIGURATION_INVALID'|'READY_FOR_REPLICATION'|'VALIDATION_IN_PROGRESS'|'REPLICATION_PENDING'|'REPLICATION_IN_PROGRESS'|'REPLICATED'|'DELTA_REPLICATION_IN_PROGRESS'|'DELTA_REPLICATED'|'DELTA_REPLICATION_FAILED'|'REPLICATION_FAILED'|'REPLICATION_STOPPING'|'REPLICATION_STOP_FAILED'|'REPLICATION_STOPPED',
                        'replicationStatusMessage': 'string',
                        'latestReplicationTime': datetime(2015, 1, 1),
                        'launchStatus': 'READY_FOR_CONFIGURATION'|'CONFIGURATION_IN_PROGRESS'|'CONFIGURATION_INVALID'|'READY_FOR_LAUNCH'|'VALIDATION_IN_PROGRESS'|'LAUNCH_PENDING'|'LAUNCH_IN_PROGRESS'|'LAUNCHED'|'DELTA_LAUNCH_IN_PROGRESS'|'DELTA_LAUNCH_FAILED'|'LAUNCH_FAILED'|'TERMINATE_IN_PROGRESS'|'TERMINATE_FAILED'|'TERMINATED',
                        'launchStatusMessage': 'string',
                        'launchDetails': {
                            'latestLaunchTime': datetime(2015, 1, 1),
                            'stackName': 'string',
                            'stackId': 'string'
                        },
                        'creationTime': datetime(2015, 1, 1),
                        'lastModified': datetime(2015, 1, 1),
                        'roleName': 'string',
                        'totalServerGroups': 123,
                        'totalServers': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **apps** *(list) --* 
              A list of application summaries.
              - *(dict) --* 
                Information about the application.
                - **appId** *(string) --* 
                  Unique ID of the application.
                - **name** *(string) --* 
                  Name of the application.
                - **description** *(string) --* 
                  Description of the application.
                - **status** *(string) --* 
                  Status of the application.
                - **statusMessage** *(string) --* 
                  A message related to the status of the application
                - **replicationStatus** *(string) --* 
                  Replication status of the application.
                - **replicationStatusMessage** *(string) --* 
                  A message related to the replication status of the application.
                - **latestReplicationTime** *(datetime) --* 
                  Timestamp of the application's most recent successful replication.
                - **launchStatus** *(string) --* 
                  Launch status of the application.
                - **launchStatusMessage** *(string) --* 
                  A message related to the launch status of the application.
                - **launchDetails** *(dict) --* 
                  Details about the latest launch of the application.
                  - **latestLaunchTime** *(datetime) --* 
                    Latest time this application was launched successfully.
                  - **stackName** *(string) --* 
                    Name of the latest stack launched for this application.
                  - **stackId** *(string) --* 
                    Identifier of the latest stack launched for this application.
                - **creationTime** *(datetime) --* 
                  Time of creation of this application.
                - **lastModified** *(datetime) --* 
                  Timestamp of the application's creation.
                - **roleName** *(string) --* 
                  Name of the service role in the customer's account used by AWS SMS.
                - **totalServerGroups** *(integer) --* 
                  Number of server groups present in the application.
                - **totalServers** *(integer) --* 
                  Number of servers present in the application.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type appIds: list
        :param appIds:
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
        """
        pass
