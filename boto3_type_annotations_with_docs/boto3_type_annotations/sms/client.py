from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from datetime import datetime
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
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

    def create_app(self, name: str = None, description: str = None, roleName: str = None, clientToken: str = None, serverGroups: List = None, tags: List = None) -> Dict:
        """
        Creates an application. An application consists of one or more server groups. Each server group contain one or more servers.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/CreateApp>`_
        
        **Request Syntax**
        ::
          response = client.create_app(
              name='string',
              description='string',
              roleName='string',
              clientToken='string',
              serverGroups=[
                  {
                      'serverGroupId': 'string',
                      'name': 'string',
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
                      ]
                  },
              ],
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'appSummary': {
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
                'serverGroups': [
                    {
                        'serverGroupId': 'string',
                        'name': 'string',
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
                        ]
                    },
                ],
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **appSummary** *(dict) --* 
              Summary description of the application.
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
            - **serverGroups** *(list) --* 
              List of server groups included in the application.
              - *(dict) --* 
                A logical grouping of servers.
                - **serverGroupId** *(string) --* 
                  Identifier of a server group.
                - **name** *(string) --* 
                  Name of a server group.
                - **serverList** *(list) --* 
                  List of servers belonging to a server group.
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
            - **tags** *(list) --* 
              List of taags associated with the application.
              - *(dict) --* 
                A label that can be assigned to an application.
                - **key** *(string) --* 
                  Tag key.
                - **value** *(string) --* 
                  Tag value.
        :type name: string
        :param name:
          Name of the new application.
        :type description: string
        :param description:
          Description of the new application
        :type roleName: string
        :param roleName:
          Name of service role in customer\'s account to be used by AWS SMS.
        :type clientToken: string
        :param clientToken:
          A unique, case-sensitive identifier you provide to ensure idempotency of application creation.
        :type serverGroups: list
        :param serverGroups:
          List of server groups to include in the application.
          - *(dict) --*
            A logical grouping of servers.
            - **serverGroupId** *(string) --*
              Identifier of a server group.
            - **name** *(string) --*
              Name of a server group.
            - **serverList** *(list) --*
              List of servers belonging to a server group.
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
        :type tags: list
        :param tags:
          List of tags to be associated with the application.
          - *(dict) --*
            A label that can be assigned to an application.
            - **key** *(string) --*
              Tag key.
            - **value** *(string) --*
              Tag value.
        :rtype: dict
        :returns:
        """
        pass

    def create_replication_job(self, serverId: str, seedReplicationTime: datetime, frequency: int = None, runOnce: bool = None, licenseType: str = None, roleName: str = None, description: str = None, numberOfRecentAmisToKeep: int = None, encrypted: bool = None, kmsKeyId: str = None) -> Dict:
        """
        Creates a replication job. The replication job schedules periodic replication runs to replicate your server to AWS. Each replication run creates an Amazon Machine Image (AMI).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/CreateReplicationJob>`_
        
        **Request Syntax**
        ::
          response = client.create_replication_job(
              serverId='string',
              seedReplicationTime=datetime(2015, 1, 1),
              frequency=123,
              runOnce=True|False,
              licenseType='AWS'|'BYOL',
              roleName='string',
              description='string',
              numberOfRecentAmisToKeep=123,
              encrypted=True|False,
              kmsKeyId='string'
          )
        
        **Response Syntax**
        ::
            {
                'replicationJobId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **replicationJobId** *(string) --* 
              The unique identifier of the replication job.
        :type serverId: string
        :param serverId: **[REQUIRED]**
          The identifier of the server.
        :type seedReplicationTime: datetime
        :param seedReplicationTime: **[REQUIRED]**
          The seed replication time.
        :type frequency: integer
        :param frequency:
          The time between consecutive replication runs, in hours.
        :type runOnce: boolean
        :param runOnce:
        :type licenseType: string
        :param licenseType:
          The license type to be used for the AMI created by a successful replication run.
        :type roleName: string
        :param roleName:
          The name of the IAM role to be used by the AWS SMS.
        :type description: string
        :param description:
          The description of the replication job.
        :type numberOfRecentAmisToKeep: integer
        :param numberOfRecentAmisToKeep:
          The maximum number of SMS-created AMIs to retain. The oldest will be deleted once the maximum number is reached and a new AMI is created.
        :type encrypted: boolean
        :param encrypted:
          When *true* , the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.
        :type kmsKeyId: string
        :param kmsKeyId:
          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:
          * KMS key ID
          * KMS key alias
          * ARN referring to KMS key ID
          * ARN referring to KMS key alias
          If encrypted is *true* but a KMS key id is not specified, the customer\'s default KMS key for EBS is used.
        :rtype: dict
        :returns:
        """
        pass

    def delete_app(self, appId: str = None, forceStopAppReplication: bool = None, forceTerminateApp: bool = None) -> Dict:
        """
        Deletes an existing application. Optionally deletes the launched stack associated with the application and all AWS SMS replication jobs for servers in the application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteApp>`_
        
        **Request Syntax**
        ::
          response = client.delete_app(
              appId='string',
              forceStopAppReplication=True|False,
              forceTerminateApp=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application to delete.
        :type forceStopAppReplication: boolean
        :param forceStopAppReplication:
          While deleting the application, stop all replication jobs corresponding to the servers in the application.
        :type forceTerminateApp: boolean
        :param forceTerminateApp:
          While deleting the application, terminate the stack corresponding to the application.
        :rtype: dict
        :returns:
        """
        pass

    def delete_app_launch_configuration(self, appId: str = None) -> Dict:
        """
        Deletes existing launch configuration for an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteAppLaunchConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_app_launch_configuration(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application associated with the launch configuration.
        :rtype: dict
        :returns:
        """
        pass

    def delete_app_replication_configuration(self, appId: str = None) -> Dict:
        """
        Deletes existing replication configuration for an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteAppReplicationConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_app_replication_configuration(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application associated with the replication configuration.
        :rtype: dict
        :returns:
        """
        pass

    def delete_replication_job(self, replicationJobId: str) -> Dict:
        """
        Deletes the specified replication job.
        After you delete a replication job, there are no further replication runs. AWS deletes the contents of the Amazon S3 bucket used to store AWS SMS artifacts. The AMIs created by the replication runs are not deleted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteReplicationJob>`_
        
        **Request Syntax**
        ::
          response = client.delete_replication_job(
              replicationJobId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]**
          The identifier of the replication job.
        :rtype: dict
        :returns:
        """
        pass

    def delete_server_catalog(self) -> Dict:
        """
        Deletes all servers from your server catalog.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DeleteServerCatalog>`_
        
        **Request Syntax**
        ::
          response = client.delete_server_catalog()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_connector(self, connectorId: str) -> Dict:
        """
        Disassociates the specified connector from AWS SMS.
        After you disassociate a connector, it is no longer available to support replication jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/DisassociateConnector>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_connector(
              connectorId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type connectorId: string
        :param connectorId: **[REQUIRED]**
          The identifier of the connector.
        :rtype: dict
        :returns:
        """
        pass

    def generate_change_set(self, appId: str = None, changesetFormat: str = None) -> Dict:
        """
        Generates a target change set for a currently launched stack and writes it to an Amazon S3 object in the customer’s Amazon S3 bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GenerateChangeSet>`_
        
        **Request Syntax**
        ::
          response = client.generate_change_set(
              appId='string',
              changesetFormat='JSON'|'YAML'
          )
        
        **Response Syntax**
        ::
            {
                's3Location': {
                    'bucket': 'string',
                    'key': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **s3Location** *(dict) --* 
              Location of the Amazon S3 object.
              - **bucket** *(string) --* 
                Amazon S3 bucket name.
              - **key** *(string) --* 
                Amazon S3 bucket key.
        :type appId: string
        :param appId:
          ID of the application associated with the change set.
        :type changesetFormat: string
        :param changesetFormat:
          Format for the change set.
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
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

    def generate_template(self, appId: str = None, templateFormat: str = None) -> Dict:
        """
        Generates an Amazon CloudFormation template based on the current launch configuration and writes it to an Amazon S3 object in the customer’s Amazon S3 bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GenerateTemplate>`_
        
        **Request Syntax**
        ::
          response = client.generate_template(
              appId='string',
              templateFormat='JSON'|'YAML'
          )
        
        **Response Syntax**
        ::
            {
                's3Location': {
                    'bucket': 'string',
                    'key': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **s3Location** *(dict) --* 
              Location of the Amazon S3 object.
              - **bucket** *(string) --* 
                Amazon S3 bucket name.
              - **key** *(string) --* 
                Amazon S3 bucket key.
        :type appId: string
        :param appId:
          ID of the application associated with the Amazon CloudFormation template.
        :type templateFormat: string
        :param templateFormat:
          Format for generating the Amazon CloudFormation template.
        :rtype: dict
        :returns:
        """
        pass

    def get_app(self, appId: str = None) -> Dict:
        """
        Retrieve information about an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetApp>`_
        
        **Request Syntax**
        ::
          response = client.get_app(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {
                'appSummary': {
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
                'serverGroups': [
                    {
                        'serverGroupId': 'string',
                        'name': 'string',
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
                        ]
                    },
                ],
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **appSummary** *(dict) --* 
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
            - **serverGroups** *(list) --* 
              List of server groups belonging to the application.
              - *(dict) --* 
                A logical grouping of servers.
                - **serverGroupId** *(string) --* 
                  Identifier of a server group.
                - **name** *(string) --* 
                  Name of a server group.
                - **serverList** *(list) --* 
                  List of servers belonging to a server group.
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
            - **tags** *(list) --* 
              List of tags associated with the application.
              - *(dict) --* 
                A label that can be assigned to an application.
                - **key** *(string) --* 
                  Tag key.
                - **value** *(string) --* 
                  Tag value.
        :type appId: string
        :param appId:
          ID of the application whose information is being retrieved.
        :rtype: dict
        :returns:
        """
        pass

    def get_app_launch_configuration(self, appId: str = None) -> Dict:
        """
        Retrieves the application launch configuration associated with an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetAppLaunchConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_app_launch_configuration(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {
                'appId': 'string',
                'roleName': 'string',
                'serverGroupLaunchConfigurations': [
                    {
                        'serverGroupId': 'string',
                        'launchOrder': 123,
                        'serverLaunchConfigurations': [
                            {
                                'server': {
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
                                'logicalId': 'string',
                                'vpc': 'string',
                                'subnet': 'string',
                                'securityGroup': 'string',
                                'ec2KeyName': 'string',
                                'userData': {
                                    's3Location': {
                                        'bucket': 'string',
                                        'key': 'string'
                                    }
                                },
                                'instanceType': 'string',
                                'associatePublicIpAddress': True|False
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **appId** *(string) --* 
              ID of the application associated with the launch configuration.
            - **roleName** *(string) --* 
              Name of the service role in the customer's account that Amazon CloudFormation uses to launch the application.
            - **serverGroupLaunchConfigurations** *(list) --* 
              List of launch configurations for server groups in this application.
              - *(dict) --* 
                Launch configuration for a server group.
                - **serverGroupId** *(string) --* 
                  Identifier of the server group the launch configuration is associated with.
                - **launchOrder** *(integer) --* 
                  Launch order of servers in the server group.
                - **serverLaunchConfigurations** *(list) --* 
                  Launch configuration for servers in the server group.
                  - *(dict) --* 
                    Launch configuration for a server.
                    - **server** *(dict) --* 
                      Identifier of the server the launch configuration is associated with.
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
                    - **logicalId** *(string) --* 
                      Logical ID of the server in the Amazon CloudFormation template.
                    - **vpc** *(string) --* 
                      Identifier of the VPC the server should be launched into.
                    - **subnet** *(string) --* 
                      Identifier of the subnet the server should be launched into.
                    - **securityGroup** *(string) --* 
                      Identifier of the security group that applies to the launched server.
                    - **ec2KeyName** *(string) --* 
                      Name of the EC2 SSH Key to be used for connecting to the launched server.
                    - **userData** *(dict) --* 
                      Location of the user-data script to be executed when launching the server.
                      - **s3Location** *(dict) --* 
                        Amazon S3 location of the user-data script.
                        - **bucket** *(string) --* 
                          Amazon S3 bucket name.
                        - **key** *(string) --* 
                          Amazon S3 bucket key.
                    - **instanceType** *(string) --* 
                      Instance type to be used for launching the server.
                    - **associatePublicIpAddress** *(boolean) --* 
                      If true, a publicly accessible IP address is created when launching the server.
        :type appId: string
        :param appId:
          ID of the application launch configuration.
        :rtype: dict
        :returns:
        """
        pass

    def get_app_replication_configuration(self, appId: str = None) -> Dict:
        """
        Retrieves an application replication configuration associatd with an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetAppReplicationConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_app_replication_configuration(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {
                'serverGroupReplicationConfigurations': [
                    {
                        'serverGroupId': 'string',
                        'serverReplicationConfigurations': [
                            {
                                'server': {
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
                                'serverReplicationParameters': {
                                    'seedTime': datetime(2015, 1, 1),
                                    'frequency': 123,
                                    'runOnce': True|False,
                                    'licenseType': 'AWS'|'BYOL',
                                    'numberOfRecentAmisToKeep': 123,
                                    'encrypted': True|False,
                                    'kmsKeyId': 'string'
                                }
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **serverGroupReplicationConfigurations** *(list) --* 
              Replication configurations associated with server groups in this application.
              - *(dict) --* 
                Replication configuration for a server group.
                - **serverGroupId** *(string) --* 
                  Identifier of the server group this replication configuration is associated with.
                - **serverReplicationConfigurations** *(list) --* 
                  Replication configuration for servers in the server group.
                  - *(dict) --* 
                    Replication configuration of a server.
                    - **server** *(dict) --* 
                      Identifier of the server this replication configuration is associated with.
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
                    - **serverReplicationParameters** *(dict) --* 
                      Parameters for replicating the server.
                      - **seedTime** *(datetime) --* 
                        Seed time for creating a replication job for the server.
                      - **frequency** *(integer) --* 
                        Frequency of creating replication jobs for the server.
                      - **runOnce** *(boolean) --* 
                      - **licenseType** *(string) --* 
                        License type for creating a replication job for the server.
                      - **numberOfRecentAmisToKeep** *(integer) --* 
                        Number of recent AMIs to keep when creating a replication job for this server.
                      - **encrypted** *(boolean) --* 
                        When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.
                      - **kmsKeyId** *(string) --* 
                        KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following: 
                        * KMS key ID 
                        * KMS key alias 
                        * ARN referring to KMS key ID 
                        * ARN referring to KMS key alias 
                        If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key for EBS is used. 
        :type appId: string
        :param appId:
          ID of the application associated with the replication configuration.
        :rtype: dict
        :returns:
        """
        pass

    def get_connectors(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Describes the connectors registered with the AWS SMS.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetConnectors>`_
        
        **Request Syntax**
        ::
          response = client.get_connectors(
              nextToken='string',
              maxResults=123
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              The token required to retrieve the next set of results. This value is null when there are no more results to return.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return in a single call. The default value is 50. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :rtype: dict
        :returns:
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        Create a paginator for an operation.
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
        Describes the specified replication job or all of your replication jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationJobs>`_
        
        **Request Syntax**
        ::
          response = client.get_replication_jobs(
              replicationJobId='string',
              nextToken='string',
              maxResults=123
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              The token required to retrieve the next set of results. This value is null when there are no more results to return.
        :type replicationJobId: string
        :param replicationJobId:
          The identifier of the replication job.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return in a single call. The default value is 50. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :rtype: dict
        :returns:
        """
        pass

    def get_replication_runs(self, replicationJobId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Describes the replication runs for the specified replication job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetReplicationRuns>`_
        
        **Request Syntax**
        ::
          response = client.get_replication_runs(
              replicationJobId='string',
              nextToken='string',
              maxResults=123
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              The token required to retrieve the next set of results. This value is null when there are no more results to return.
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]**
          The identifier of the replication job.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return in a single call. The default value is 50. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :rtype: dict
        :returns:
        """
        pass

    def get_servers(self, nextToken: str = None, maxResults: int = None, vmServerAddressList: List = None) -> Dict:
        """
        Describes the servers in your server catalog.
        Before you can describe your servers, you must import them using  ImportServerCatalog .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/GetServers>`_
        
        **Request Syntax**
        ::
          response = client.get_servers(
              nextToken='string',
              maxResults=123,
              vmServerAddressList=[
                  {
                      'vmManagerId': 'string',
                      'vmId': 'string'
                  },
              ]
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              The token required to retrieve the next set of results. This value is null when there are no more results to return.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return in a single call. The default value is 50. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :type vmServerAddressList: list
        :param vmServerAddressList:
          List of ``VmServerAddress`` objects
          - *(dict) --*
            Represents a VM server location.
            - **vmManagerId** *(string) --*
              The identifier of the VM manager.
            - **vmId** *(string) --*
              The identifier of the VM.
        :rtype: dict
        :returns:
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def import_server_catalog(self) -> Dict:
        """
        Gathers a complete list of on-premises servers. Connectors must be installed and monitoring all servers that you want to import.
        This call returns immediately, but might take additional time to retrieve all the servers.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/ImportServerCatalog>`_
        
        **Request Syntax**
        ::
          response = client.import_server_catalog()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :rtype: dict
        :returns:
        """
        pass

    def launch_app(self, appId: str = None) -> Dict:
        """
        Launches an application stack.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/LaunchApp>`_
        
        **Request Syntax**
        ::
          response = client.launch_app(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application to launch.
        :rtype: dict
        :returns:
        """
        pass

    def list_apps(self, appIds: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Returns a list of summaries for all applications.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/ListApps>`_
        
        **Request Syntax**
        ::
          response = client.list_apps(
              appIds=[
                  'string',
              ],
              nextToken='string',
              maxResults=123
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              The token required to retrieve the next set of results. This value is null when there are no more results to return.
        :type appIds: list
        :param appIds:
          - *(string) --*
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return in a single call. The default value is 50. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :rtype: dict
        :returns:
        """
        pass

    def put_app_launch_configuration(self, appId: str = None, roleName: str = None, serverGroupLaunchConfigurations: List = None) -> Dict:
        """
        Creates a launch configuration for an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/PutAppLaunchConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_app_launch_configuration(
              appId='string',
              roleName='string',
              serverGroupLaunchConfigurations=[
                  {
                      'serverGroupId': 'string',
                      'launchOrder': 123,
                      'serverLaunchConfigurations': [
                          {
                              'server': {
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
                              'logicalId': 'string',
                              'vpc': 'string',
                              'subnet': 'string',
                              'securityGroup': 'string',
                              'ec2KeyName': 'string',
                              'userData': {
                                  's3Location': {
                                      'bucket': 'string',
                                      'key': 'string'
                                  }
                              },
                              'instanceType': 'string',
                              'associatePublicIpAddress': True|False
                          },
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application associated with the launch configuration.
        :type roleName: string
        :param roleName:
          Name of service role in the customer\'s account that Amazon CloudFormation uses to launch the application.
        :type serverGroupLaunchConfigurations: list
        :param serverGroupLaunchConfigurations:
          Launch configurations for server groups in the application.
          - *(dict) --*
            Launch configuration for a server group.
            - **serverGroupId** *(string) --*
              Identifier of the server group the launch configuration is associated with.
            - **launchOrder** *(integer) --*
              Launch order of servers in the server group.
            - **serverLaunchConfigurations** *(list) --*
              Launch configuration for servers in the server group.
              - *(dict) --*
                Launch configuration for a server.
                - **server** *(dict) --*
                  Identifier of the server the launch configuration is associated with.
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
                - **logicalId** *(string) --*
                  Logical ID of the server in the Amazon CloudFormation template.
                - **vpc** *(string) --*
                  Identifier of the VPC the server should be launched into.
                - **subnet** *(string) --*
                  Identifier of the subnet the server should be launched into.
                - **securityGroup** *(string) --*
                  Identifier of the security group that applies to the launched server.
                - **ec2KeyName** *(string) --*
                  Name of the EC2 SSH Key to be used for connecting to the launched server.
                - **userData** *(dict) --*
                  Location of the user-data script to be executed when launching the server.
                  - **s3Location** *(dict) --*
                    Amazon S3 location of the user-data script.
                    - **bucket** *(string) --*
                      Amazon S3 bucket name.
                    - **key** *(string) --*
                      Amazon S3 bucket key.
                - **instanceType** *(string) --*
                  Instance type to be used for launching the server.
                - **associatePublicIpAddress** *(boolean) --*
                  If true, a publicly accessible IP address is created when launching the server.
        :rtype: dict
        :returns:
        """
        pass

    def put_app_replication_configuration(self, appId: str = None, serverGroupReplicationConfigurations: List = None) -> Dict:
        """
        Creates or updates a replication configuration for an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/PutAppReplicationConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_app_replication_configuration(
              appId='string',
              serverGroupReplicationConfigurations=[
                  {
                      'serverGroupId': 'string',
                      'serverReplicationConfigurations': [
                          {
                              'server': {
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
                              'serverReplicationParameters': {
                                  'seedTime': datetime(2015, 1, 1),
                                  'frequency': 123,
                                  'runOnce': True|False,
                                  'licenseType': 'AWS'|'BYOL',
                                  'numberOfRecentAmisToKeep': 123,
                                  'encrypted': True|False,
                                  'kmsKeyId': 'string'
                              }
                          },
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application tassociated with the replication configuration.
        :type serverGroupReplicationConfigurations: list
        :param serverGroupReplicationConfigurations:
          Replication configurations for server groups in the application.
          - *(dict) --*
            Replication configuration for a server group.
            - **serverGroupId** *(string) --*
              Identifier of the server group this replication configuration is associated with.
            - **serverReplicationConfigurations** *(list) --*
              Replication configuration for servers in the server group.
              - *(dict) --*
                Replication configuration of a server.
                - **server** *(dict) --*
                  Identifier of the server this replication configuration is associated with.
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
                - **serverReplicationParameters** *(dict) --*
                  Parameters for replicating the server.
                  - **seedTime** *(datetime) --*
                    Seed time for creating a replication job for the server.
                  - **frequency** *(integer) --*
                    Frequency of creating replication jobs for the server.
                  - **runOnce** *(boolean) --*
                  - **licenseType** *(string) --*
                    License type for creating a replication job for the server.
                  - **numberOfRecentAmisToKeep** *(integer) --*
                    Number of recent AMIs to keep when creating a replication job for this server.
                  - **encrypted** *(boolean) --*
                    When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.
                  - **kmsKeyId** *(string) --*
                    KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:
                    * KMS key ID
                    * KMS key alias
                    * ARN referring to KMS key ID
                    * ARN referring to KMS key alias
                    If encrypted is *true* but a KMS key id is not specified, the customer\'s default KMS key for EBS is used.
        :rtype: dict
        :returns:
        """
        pass

    def start_app_replication(self, appId: str = None) -> Dict:
        """
        Starts replicating an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/StartAppReplication>`_
        
        **Request Syntax**
        ::
          response = client.start_app_replication(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application to replicate.
        :rtype: dict
        :returns:
        """
        pass

    def start_on_demand_replication_run(self, replicationJobId: str, description: str = None) -> Dict:
        """
        Starts an on-demand replication run for the specified replication job. This replication run starts immediately. This replication run is in addition to the ones already scheduled.
        There is a limit on the number of on-demand replications runs you can request in a 24-hour period.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/StartOnDemandReplicationRun>`_
        
        **Request Syntax**
        ::
          response = client.start_on_demand_replication_run(
              replicationJobId='string',
              description='string'
          )
        
        **Response Syntax**
        ::
            {
                'replicationRunId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **replicationRunId** *(string) --* 
              The identifier of the replication run.
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]**
          The identifier of the replication job.
        :type description: string
        :param description:
          The description of the replication run.
        :rtype: dict
        :returns:
        """
        pass

    def stop_app_replication(self, appId: str = None) -> Dict:
        """
        Stops replicating an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/StopAppReplication>`_
        
        **Request Syntax**
        ::
          response = client.stop_app_replication(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application to stop replicating.
        :rtype: dict
        :returns:
        """
        pass

    def terminate_app(self, appId: str = None) -> Dict:
        """
        Terminates the stack for an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/TerminateApp>`_
        
        **Request Syntax**
        ::
          response = client.terminate_app(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type appId: string
        :param appId:
          ID of the application to terminate.
        :rtype: dict
        :returns:
        """
        pass

    def update_app(self, appId: str = None, name: str = None, description: str = None, roleName: str = None, serverGroups: List = None, tags: List = None) -> Dict:
        """
        Updates an application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/UpdateApp>`_
        
        **Request Syntax**
        ::
          response = client.update_app(
              appId='string',
              name='string',
              description='string',
              roleName='string',
              serverGroups=[
                  {
                      'serverGroupId': 'string',
                      'name': 'string',
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
                      ]
                  },
              ],
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'appSummary': {
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
                'serverGroups': [
                    {
                        'serverGroupId': 'string',
                        'name': 'string',
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
                        ]
                    },
                ],
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **appSummary** *(dict) --* 
              Summary description of the application.
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
            - **serverGroups** *(list) --* 
              List of updated server groups in the application.
              - *(dict) --* 
                A logical grouping of servers.
                - **serverGroupId** *(string) --* 
                  Identifier of a server group.
                - **name** *(string) --* 
                  Name of a server group.
                - **serverList** *(list) --* 
                  List of servers belonging to a server group.
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
            - **tags** *(list) --* 
              List of tags associated with the application.
              - *(dict) --* 
                A label that can be assigned to an application.
                - **key** *(string) --* 
                  Tag key.
                - **value** *(string) --* 
                  Tag value.
        :type appId: string
        :param appId:
          ID of the application to update.
        :type name: string
        :param name:
          New name of the application.
        :type description: string
        :param description:
          New description of the application.
        :type roleName: string
        :param roleName:
          Name of the service role in the customer\'s account used by AWS SMS.
        :type serverGroups: list
        :param serverGroups:
          List of server groups in the application to update.
          - *(dict) --*
            A logical grouping of servers.
            - **serverGroupId** *(string) --*
              Identifier of a server group.
            - **name** *(string) --*
              Name of a server group.
            - **serverList** *(list) --*
              List of servers belonging to a server group.
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
        :type tags: list
        :param tags:
          List of tags to associate with the application.
          - *(dict) --*
            A label that can be assigned to an application.
            - **key** *(string) --*
              Tag key.
            - **value** *(string) --*
              Tag value.
        :rtype: dict
        :returns:
        """
        pass

    def update_replication_job(self, replicationJobId: str, frequency: int = None, nextReplicationRunStartTime: datetime = None, licenseType: str = None, roleName: str = None, description: str = None, numberOfRecentAmisToKeep: int = None, encrypted: bool = None, kmsKeyId: str = None) -> Dict:
        """
        Updates the specified settings for the specified replication job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/UpdateReplicationJob>`_
        
        **Request Syntax**
        ::
          response = client.update_replication_job(
              replicationJobId='string',
              frequency=123,
              nextReplicationRunStartTime=datetime(2015, 1, 1),
              licenseType='AWS'|'BYOL',
              roleName='string',
              description='string',
              numberOfRecentAmisToKeep=123,
              encrypted=True|False,
              kmsKeyId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type replicationJobId: string
        :param replicationJobId: **[REQUIRED]**
          The identifier of the replication job.
        :type frequency: integer
        :param frequency:
          The time between consecutive replication runs, in hours.
        :type nextReplicationRunStartTime: datetime
        :param nextReplicationRunStartTime:
          The start time of the next replication run.
        :type licenseType: string
        :param licenseType:
          The license type to be used for the AMI created by a successful replication run.
        :type roleName: string
        :param roleName:
          The name of the IAM role to be used by AWS SMS.
        :type description: string
        :param description:
          The description of the replication job.
        :type numberOfRecentAmisToKeep: integer
        :param numberOfRecentAmisToKeep:
          The maximum number of SMS-created AMIs to retain. The oldest will be deleted once the maximum number is reached and a new AMI is created.
        :type encrypted: boolean
        :param encrypted:
          When true, the replication job produces encrypted AMIs . See also ``KmsKeyId`` below.
        :type kmsKeyId: string
        :param kmsKeyId:
          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:
          * KMS key ID
          * KMS key alias
          * ARN referring to KMS key ID
          * ARN referring to KMS key alias
          If encrypted is *true* but a KMS key id is not specified, the customer\'s default KMS key for EBS is used.
        :rtype: dict
        :returns:
        """
        pass
