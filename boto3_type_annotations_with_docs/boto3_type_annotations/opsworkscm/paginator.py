from typing import Dict
from botocore.paginate import Paginator


class DescribeBackups(Paginator):
    def paginate(self, BackupId: str = None, ServerName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`OpsWorksCM.Client.describe_backups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeBackups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              BackupId='string',
              ServerName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Backups': [
                    {
                        'BackupArn': 'string',
                        'BackupId': 'string',
                        'BackupType': 'AUTOMATED'|'MANUAL',
                        'CreatedAt': datetime(2015, 1, 1),
                        'Description': 'string',
                        'Engine': 'string',
                        'EngineModel': 'string',
                        'EngineVersion': 'string',
                        'InstanceProfileArn': 'string',
                        'InstanceType': 'string',
                        'KeyPair': 'string',
                        'PreferredBackupWindow': 'string',
                        'PreferredMaintenanceWindow': 'string',
                        'S3DataSize': 123,
                        'S3DataUrl': 'string',
                        'S3LogUrl': 'string',
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'ServerName': 'string',
                        'ServiceRoleArn': 'string',
                        'Status': 'IN_PROGRESS'|'OK'|'FAILED'|'DELETING',
                        'StatusDescription': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'ToolsVersion': 'string',
                        'UserArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Backups** *(list) --* 
              Contains the response to a ``DescribeBackups`` request. 
              - *(dict) --* 
                Describes a single backup. 
                - **BackupArn** *(string) --* 
                  The ARN of the backup. 
                - **BackupId** *(string) --* 
                  The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``  
                - **BackupType** *(string) --* 
                  The backup type. Valid values are ``automated`` or ``manual`` . 
                - **CreatedAt** *(datetime) --* 
                  The time stamp when the backup was created in the database. Example: ``2016-07-29T13:38:47.520Z``  
                - **Description** *(string) --* 
                  A user-provided description for a manual backup. This field is empty for automated backups. 
                - **Engine** *(string) --* 
                  The engine type that is obtained from the server when the backup is created. 
                - **EngineModel** *(string) --* 
                  The engine model that is obtained from the server when the backup is created. 
                - **EngineVersion** *(string) --* 
                  The engine version that is obtained from the server when the backup is created. 
                - **InstanceProfileArn** *(string) --* 
                  The EC2 instance profile ARN that is obtained from the server when the backup is created. Because this value is stored, you are not required to provide the InstanceProfileArn again if you restore a backup. 
                - **InstanceType** *(string) --* 
                  The instance type that is obtained from the server when the backup is created. 
                - **KeyPair** *(string) --* 
                  The key pair that is obtained from the server when the backup is created. 
                - **PreferredBackupWindow** *(string) --* 
                  The preferred backup period that is obtained from the server when the backup is created. 
                - **PreferredMaintenanceWindow** *(string) --* 
                  The preferred maintenance period that is obtained from the server when the backup is created. 
                - **S3DataSize** *(integer) --* 
                  This field is deprecated and is no longer used. 
                - **S3DataUrl** *(string) --* 
                  This field is deprecated and is no longer used. 
                - **S3LogUrl** *(string) --* 
                  The Amazon S3 URL of the backup's log file. 
                - **SecurityGroupIds** *(list) --* 
                  The security group IDs that are obtained from the server when the backup is created. 
                  - *(string) --* 
                - **ServerName** *(string) --* 
                  The name of the server from which the backup was made. 
                - **ServiceRoleArn** *(string) --* 
                  The service role ARN that is obtained from the server when the backup is created. 
                - **Status** *(string) --* 
                  The status of a backup while in progress. 
                - **StatusDescription** *(string) --* 
                  An informational message about backup status. 
                - **SubnetIds** *(list) --* 
                  The subnet IDs that are obtained from the server when the backup is created. 
                  - *(string) --* 
                - **ToolsVersion** *(string) --* 
                  The version of AWS OpsWorks CM-specific tools that is obtained from the server when the backup is created. 
                - **UserArn** *(string) --* 
                  The IAM user ARN of the requester for manual backups. This field is empty for automated backups. 
        :type BackupId: string
        :param BackupId:
          Describes a single backup.
        :type ServerName: string
        :param ServerName:
          Returns backups for the server with the specified ServerName.
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


class DescribeEvents(Paginator):
    def paginate(self, ServerName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`OpsWorksCM.Client.describe_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ServerName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ServerEvents': [
                    {
                        'CreatedAt': datetime(2015, 1, 1),
                        'ServerName': 'string',
                        'Message': 'string',
                        'LogUrl': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServerEvents** *(list) --* 
              Contains the response to a ``DescribeEvents`` request. 
              - *(dict) --* 
                An event that is related to the server, such as the start of maintenance or backup. 
                - **CreatedAt** *(datetime) --* 
                  The time when the event occurred. 
                - **ServerName** *(string) --* 
                  The name of the server on or for which the event occurred. 
                - **Message** *(string) --* 
                  A human-readable informational or status message.
                - **LogUrl** *(string) --* 
                  The Amazon S3 URL of the event's log file.
        :type ServerName: string
        :param ServerName: **[REQUIRED]**
          The name of the server for which you want to view events.
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


class DescribeServers(Paginator):
    def paginate(self, ServerName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`OpsWorksCM.Client.describe_servers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeServers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ServerName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Servers': [
                    {
                        'AssociatePublicIpAddress': True|False,
                        'BackupRetentionCount': 123,
                        'ServerName': 'string',
                        'CreatedAt': datetime(2015, 1, 1),
                        'CloudFormationStackArn': 'string',
                        'DisableAutomatedBackup': True|False,
                        'Endpoint': 'string',
                        'Engine': 'string',
                        'EngineModel': 'string',
                        'EngineAttributes': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ],
                        'EngineVersion': 'string',
                        'InstanceProfileArn': 'string',
                        'InstanceType': 'string',
                        'KeyPair': 'string',
                        'MaintenanceStatus': 'SUCCESS'|'FAILED',
                        'PreferredMaintenanceWindow': 'string',
                        'PreferredBackupWindow': 'string',
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'ServiceRoleArn': 'string',
                        'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
                        'StatusReason': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'ServerArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Servers** *(list) --* 
              Contains the response to a ``DescribeServers`` request.
               *For Puppet Server:*  ``DescribeServersResponse$Servers$EngineAttributes`` contains PUPPET_API_CA_CERT. This is the PEM-encoded CA certificate that is used by the Puppet API over TCP port number 8140. The CA certificate is also used to sign node certificates.
              - *(dict) --* 
                Describes a configuration management server. 
                - **AssociatePublicIpAddress** *(boolean) --* 
                  Associate a public IP address with a server that you are launching. 
                - **BackupRetentionCount** *(integer) --* 
                  The number of automated backups to keep. 
                - **ServerName** *(string) --* 
                  The name of the server. 
                - **CreatedAt** *(datetime) --* 
                  Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``  
                - **CloudFormationStackArn** *(string) --* 
                  The ARN of the CloudFormation stack that was used to create the server. 
                - **DisableAutomatedBackup** *(boolean) --* 
                  Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount. 
                - **Endpoint** *(string) --* 
                  A DNS name that can be used to access the engine. Example: ``myserver-asdfghjkl.us-east-1.opsworks.io``  
                - **Engine** *(string) --* 
                  The engine type of the server. Valid values in this release include ``Chef`` and ``Puppet`` . 
                - **EngineModel** *(string) --* 
                  The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef. 
                - **EngineAttributes** *(list) --* 
                  The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer(). 
        
        **Attributes returned in a createServer response for Chef**
                  * ``CHEF_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API. 
                  * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands. 
        
        **Attributes returned in a createServer response for Puppet**
                  * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. 
                  * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online. 
                  - *(dict) --* 
                    A name and value pair that is specific to the engine of the server. 
                    - **Name** *(string) --* 
                      The name of the engine attribute. 
                    - **Value** *(string) --* 
                      The value of the engine attribute. 
                - **EngineVersion** *(string) --* 
                  The engine version of the server. For a Chef server, the valid value for EngineVersion is currently ``12`` . For a Puppet server, the valid value is ``2017`` . 
                - **InstanceProfileArn** *(string) --* 
                  The instance profile ARN of the server. 
                - **InstanceType** *(string) --* 
                  The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console. 
                - **KeyPair** *(string) --* 
                  The key pair associated with the server. 
                - **MaintenanceStatus** *(string) --* 
                  The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` . 
                - **PreferredMaintenanceWindow** *(string) --* 
                  The preferred maintenance period specified for the server. 
                - **PreferredBackupWindow** *(string) --* 
                  The preferred backup period specified for the server. 
                - **SecurityGroupIds** *(list) --* 
                  The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console. 
                  - *(string) --* 
                - **ServiceRoleArn** *(string) --* 
                  The service role ARN used to create the server. 
                - **Status** *(string) --* 
                  The server's status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server's health state. 
                - **StatusReason** *(string) --* 
                  Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results). 
                - **SubnetIds** *(list) --* 
                  The subnet IDs specified in a CreateServer request. 
                  - *(string) --* 
                - **ServerArn** *(string) --* 
                  The ARN of the server. 
        :type ServerName: string
        :param ServerName:
          Describes the server with the specified ServerName.
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
