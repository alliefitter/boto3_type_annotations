from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def accept_match(self, TicketId: str, PlayerIds: List, AcceptanceType: str) -> Dict:
        """
        
        When FlexMatch builds a match, all the matchmaking tickets involved in the proposed match are placed into status ``REQUIRES_ACCEPTANCE`` . This is a trigger for your game to get acceptance from all players in the ticket. Acceptances are only valid for tickets when they are in this status; all other acceptances result in an error.
        
        To register acceptance, specify the ticket ID, a response, and one or more players. Once all players have registered acceptance, the matchmaking tickets advance to status ``PLACING`` , where a new game session is created for the match. 
        
        If any player rejects the match, or if acceptances are not received before a specified timeout, the proposed match is dropped. The matchmaking tickets are then handled in one of two ways: For tickets where all players accepted the match, the ticket status is returned to ``SEARCHING`` to find a new match. For tickets where one or more players failed to accept the match, the ticket status is set to ``FAILED`` , and processing is terminated. A new matchmaking request for these players can be submitted as needed. 
        
        Matchmaking-related operations include:
        
        *  StartMatchmaking   
         
        *  DescribeMatchmaking   
         
        *  StopMatchmaking   
         
        *  AcceptMatch   
         
        *  StartMatchBackfill   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/AcceptMatch>`_
        
        **Request Syntax** 
        ::
        
          response = client.accept_match(
              TicketId=\'string\',
              PlayerIds=[
                  \'string\',
              ],
              AcceptanceType=\'ACCEPT\'|\'REJECT\'
          )
        :type TicketId: string
        :param TicketId: **[REQUIRED]** 
        
          Unique identifier for a matchmaking ticket. The ticket must be in status ``REQUIRES_ACCEPTANCE`` ; otherwise this request will fail.
        
        :type PlayerIds: list
        :param PlayerIds: **[REQUIRED]** 
        
          Unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.
        
          - *(string) --* 
        
        :type AcceptanceType: string
        :param AcceptanceType: **[REQUIRED]** 
        
          Player response to the proposed match.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
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

    def create_alias(self, Name: str, RoutingStrategy: Dict, Description: str = None) -> Dict:
        """
        
        Amazon GameLift supports two types of routing strategies for aliases: simple and terminal. A simple alias points to an active fleet. A terminal alias is used to display messaging or link to a URL instead of routing players to an active fleet. For example, you might use a terminal alias when a game version is no longer supported and you want to direct players to an upgrade site. 
        
        To create a fleet alias, specify an alias name, routing strategy, and optional description. Each simple alias can point to only one fleet, but a fleet can have multiple aliases. If successful, a new alias record is returned, including an alias ID, which you can reference when creating a game session. You can reassign an alias to another fleet by calling ``UpdateAlias`` .
        
        Alias-related operations include:
        
        *  CreateAlias   
         
        *  ListAliases   
         
        *  DescribeAlias   
         
        *  UpdateAlias   
         
        *  DeleteAlias   
         
        *  ResolveAlias   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_alias(
              Name=\'string\',
              Description=\'string\',
              RoutingStrategy={
                  \'Type\': \'SIMPLE\'|\'TERMINAL\',
                  \'FleetId\': \'string\',
                  \'Message\': \'string\'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Descriptive label that is associated with an alias. Alias names do not need to be unique.
        
        :type Description: string
        :param Description: 
        
          Human-readable description of an alias.
        
        :type RoutingStrategy: dict
        :param RoutingStrategy: **[REQUIRED]** 
        
          Object that specifies the fleet and routing type to use for the alias.
        
          - **Type** *(string) --* 
        
            Type of routing strategy.
        
            Possible routing types include the following:
        
            * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets. 
             
            * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded. 
             
          - **FleetId** *(string) --* 
        
            Unique identifier for a fleet that the alias points to.
        
          - **Message** *(string) --* 
        
            Message text to be used with a terminal routing strategy.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Alias\': {
                    \'AliasId\': \'string\',
                    \'Name\': \'string\',
                    \'AliasArn\': \'string\',
                    \'Description\': \'string\',
                    \'RoutingStrategy\': {
                        \'Type\': \'SIMPLE\'|\'TERMINAL\',
                        \'FleetId\': \'string\',
                        \'Message\': \'string\'
                    },
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'LastUpdatedTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Alias** *(dict) --* 
        
              Object that describes the newly created alias record.
        
              - **AliasId** *(string) --* 
        
                Unique identifier for an alias; alias IDs are unique within a region.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with an alias. Alias names do not need to be unique.
        
              - **AliasArn** *(string) --* 
        
                Unique identifier for an alias; alias ARNs are unique across all regions.
        
              - **Description** *(string) --* 
        
                Human-readable description of an alias.
        
              - **RoutingStrategy** *(dict) --* 
        
                Alias configuration for the alias, including routing type and settings.
        
                - **Type** *(string) --* 
        
                  Type of routing strategy.
        
                  Possible routing types include the following:
        
                  * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets. 
                   
                  * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded. 
                   
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that the alias points to.
        
                - **Message** *(string) --* 
        
                  Message text to be used with a terminal routing strategy.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **LastUpdatedTime** *(datetime) --* 
        
                Time stamp indicating when this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
        """
        pass

    def create_build(self, Name: str = None, Version: str = None, StorageLocation: Dict = None, OperatingSystem: str = None) -> Dict:
        """
        
        Game server binaries must be combined into a ``.zip`` file for use with Amazon GameLift. See `Uploading Your Game <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html>`__ for more information. 
        
        .. warning::
        
          To create new builds quickly and easily, use the AWS CLI command ** `upload-build <http://docs.aws.amazon.com/cli/latest/reference/gamelift/upload-build.html>`__ ** . This helper command uploads your build and creates a new build record in one step, and automatically handles the necessary permissions. See `Upload Build Files to Amazon GameLift <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html>`__ for more help.
        
        The ``CreateBuild`` operation should be used only when you need to manually upload your build files, as in the following scenarios:
        
        * Store a build file in an Amazon S3 bucket under your own AWS account. To use this option, you must first give Amazon GameLift access to that Amazon S3 bucket. See `Create a Build with Files in Amazon S3 <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build>`__ for detailed help. To create a new build record using files in your Amazon S3 bucket, call ``CreateBuild`` and specify a build name, operating system, and the storage location of your game build. 
         
        * Upload a build file directly to Amazon GameLift\'s Amazon S3 account. To use this option, you first call ``CreateBuild`` with a build name and operating system. This action creates a new build record and returns an Amazon S3 storage location (bucket and key only) and temporary access credentials. Use the credentials to manually upload your build file to the storage location (see the Amazon S3 topic `Uploading Objects <http://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html>`__ ). You can upload files to a location only once.  
         
        If successful, this operation creates a new build record with a unique build ID and places it in ``INITIALIZED`` status. You can use  DescribeBuild to check the status of your build. A build must be in ``READY`` status before it can be used to create fleets.
        
        Build-related operations include:
        
        *  CreateBuild   
         
        *  ListBuilds   
         
        *  DescribeBuild   
         
        *  UpdateBuild   
         
        *  DeleteBuild   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateBuild>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_build(
              Name=\'string\',
              Version=\'string\',
              StorageLocation={
                  \'Bucket\': \'string\',
                  \'Key\': \'string\',
                  \'RoleArn\': \'string\'
              },
              OperatingSystem=\'WINDOWS_2012\'|\'AMAZON_LINUX\'
          )
        :type Name: string
        :param Name: 
        
          Descriptive label that is associated with a build. Build names do not need to be unique. You can use  UpdateBuild to change this value later. 
        
        :type Version: string
        :param Version: 
        
          Version that is associated with this build. Version strings do not need to be unique. You can use  UpdateBuild to change this value later. 
        
        :type StorageLocation: dict
        :param StorageLocation: 
        
          Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key, as well as a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket must be in the same region that you want to create a new build in.
        
          - **Bucket** *(string) --* 
        
            Amazon S3 bucket identifier. This is the name of your S3 bucket.
        
          - **Key** *(string) --* 
        
            Name of the zip file containing your build files. 
        
          - **RoleArn** *(string) --* 
        
            Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for the access role that allows Amazon GameLift to access your S3 bucket.
        
        :type OperatingSystem: string
        :param OperatingSystem: 
        
          Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Build\': {
                    \'BuildId\': \'string\',
                    \'Name\': \'string\',
                    \'Version\': \'string\',
                    \'Status\': \'INITIALIZED\'|\'READY\'|\'FAILED\',
                    \'SizeOnDisk\': 123,
                    \'OperatingSystem\': \'WINDOWS_2012\'|\'AMAZON_LINUX\',
                    \'CreationTime\': datetime(2015, 1, 1)
                },
                \'UploadCredentials\': {
                    \'AccessKeyId\': \'string\',
                    \'SecretAccessKey\': \'string\',
                    \'SessionToken\': \'string\'
                },
                \'StorageLocation\': {
                    \'Bucket\': \'string\',
                    \'Key\': \'string\',
                    \'RoleArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Build** *(dict) --* 
        
              The newly created build record, including a unique build ID and status. 
        
              - **BuildId** *(string) --* 
        
                Unique identifier for a build.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .
        
              - **Version** *(string) --* 
        
                Version that is associated with this build. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .
        
              - **Status** *(string) --* 
        
                Current status of the build.
        
                Possible build statuses include the following:
        
                * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.  
                 
                * **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build. 
                 
                * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.  
                 
              - **SizeOnDisk** *(integer) --* 
        
                File size of the uploaded game build, expressed in bytes. When the build status is ``INITIALIZED`` , this value is 0.
        
              - **OperatingSystem** *(string) --* 
        
                Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
            - **UploadCredentials** *(dict) --* 
        
              This element is returned only when the operation is called without a storage location. It contains credentials to use when you are uploading a build file to an Amazon S3 bucket that is owned by Amazon GameLift. Credentials have a limited life span. To refresh these credentials, call  RequestUploadCredentials . 
        
              - **AccessKeyId** *(string) --* 
        
                Temporary key allowing access to the Amazon GameLift S3 account.
        
              - **SecretAccessKey** *(string) --* 
        
                Temporary secret key allowing access to the Amazon GameLift S3 account.
        
              - **SessionToken** *(string) --* 
        
                Token used to associate a specific build ID with the files uploaded using these credentials.
        
            - **StorageLocation** *(dict) --* 
        
              Amazon S3 location for your game build file, including bucket name and key.
        
              - **Bucket** *(string) --* 
        
                Amazon S3 bucket identifier. This is the name of your S3 bucket.
        
              - **Key** *(string) --* 
        
                Name of the zip file containing your build files. 
        
              - **RoleArn** *(string) --* 
        
                Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for the access role that allows Amazon GameLift to access your S3 bucket.
        
        """
        pass

    def create_fleet(self, Name: str, BuildId: str, EC2InstanceType: str, Description: str = None, ServerLaunchPath: str = None, ServerLaunchParameters: str = None, LogPaths: List = None, EC2InboundPermissions: List = None, NewGameSessionProtectionPolicy: str = None, RuntimeConfiguration: Dict = None, ResourceCreationLimitPolicy: Dict = None, MetricGroups: List = None, PeerVpcAwsAccountId: str = None, PeerVpcId: str = None, FleetType: str = None) -> Dict:
        """
        
        To create a new fleet, you must specify the following: (1) a fleet name, (2) the build ID of a successfully uploaded game build, (3) an EC2 instance type, and (4) a run-time configuration, which describes the server processes to run on each instance in the fleet. If you don\'t specify a fleet type (on-demand or spot), the new fleet uses on-demand instances by default.
        
        You can also configure the new fleet with the following settings:
        
        * Fleet description 
         
        * Access permissions for inbound traffic 
         
        * Fleet-wide game session protection 
         
        * Resource usage limits 
         
        * VPC peering connection (see `VPC Peering with Amazon GameLift Fleets <http://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`__ ) 
         
        If you use Amazon CloudWatch for metrics, you can add the new fleet to a metric group. By adding multiple fleets to a metric group, you can view aggregated metrics for all the fleets in the group. 
        
        If the ``CreateFleet`` call is successful, Amazon GameLift performs the following tasks. You can track the process of a fleet by checking the fleet status or by monitoring fleet creation events:
        
        * Creates a fleet record. Status: ``NEW`` . 
         
        * Begins writing events to the fleet event log, which can be accessed in the Amazon GameLift console. Sets the fleet\'s target capacity to 1 (desired instances), which triggers Amazon GameLift to start one new EC2 instance. 
         
        * Downloads the game build to the new instance and installs it. Statuses: ``DOWNLOADING`` , ``VALIDATING`` , ``BUILDING`` .  
         
        * Starts launching server processes on the instance. If the fleet is configured to run multiple server processes per instance, Amazon GameLift staggers each launch by a few seconds. Status: ``ACTIVATING`` . 
         
        * Sets the fleet\'s status to ``ACTIVE`` as soon as one server process is ready to host a game session. 
         
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_fleet(
              Name=\'string\',
              Description=\'string\',
              BuildId=\'string\',
              ServerLaunchPath=\'string\',
              ServerLaunchParameters=\'string\',
              LogPaths=[
                  \'string\',
              ],
              EC2InstanceType=\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\',
              EC2InboundPermissions=[
                  {
                      \'FromPort\': 123,
                      \'ToPort\': 123,
                      \'IpRange\': \'string\',
                      \'Protocol\': \'TCP\'|\'UDP\'
                  },
              ],
              NewGameSessionProtectionPolicy=\'NoProtection\'|\'FullProtection\',
              RuntimeConfiguration={
                  \'ServerProcesses\': [
                      {
                          \'LaunchPath\': \'string\',
                          \'Parameters\': \'string\',
                          \'ConcurrentExecutions\': 123
                      },
                  ],
                  \'MaxConcurrentGameSessionActivations\': 123,
                  \'GameSessionActivationTimeoutSeconds\': 123
              },
              ResourceCreationLimitPolicy={
                  \'NewGameSessionsPerCreator\': 123,
                  \'PolicyPeriodInMinutes\': 123
              },
              MetricGroups=[
                  \'string\',
              ],
              PeerVpcAwsAccountId=\'string\',
              PeerVpcId=\'string\',
              FleetType=\'ON_DEMAND\'|\'SPOT\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        
        :type Description: string
        :param Description: 
        
          Human-readable description of a fleet.
        
        :type BuildId: string
        :param BuildId: **[REQUIRED]** 
        
          Unique identifier for a build to be deployed on the new fleet. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.
        
        :type ServerLaunchPath: string
        :param ServerLaunchPath: 
        
          This parameter is no longer used. Instead, specify a server launch path using the ``RuntimeConfiguration`` parameter. (Requests that specify a server launch path and launch parameters instead of a run-time configuration will continue to work.)
        
        :type ServerLaunchParameters: string
        :param ServerLaunchParameters: 
        
          This parameter is no longer used. Instead, specify server launch parameters in the ``RuntimeConfiguration`` parameter. (Requests that specify a server launch path and launch parameters instead of a run-time configuration will continue to work.)
        
        :type LogPaths: list
        :param LogPaths: 
        
          This parameter is no longer used. Instead, to specify where Amazon GameLift should store log files once a server process shuts down, use the Amazon GameLift server API ``ProcessReady()`` and specify one or more directory paths in ``logParameters`` . See more information in the `Server API Reference <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api-ref.html#gamelift-sdk-server-api-ref-dataypes-process>`__ . 
        
          - *(string) --* 
        
        :type EC2InstanceType: string
        :param EC2InstanceType: **[REQUIRED]** 
        
          Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.
        
        :type EC2InboundPermissions: list
        :param EC2InboundPermissions: 
        
          Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. If no inbound permissions are set, including both IP address range and port range, the server processes in the fleet cannot accept connections. You can specify one or more sets of permissions for a fleet.
        
          - *(dict) --* 
        
            A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet\'s allowed ranges. This combination is included in the  GameSession object. 
        
            - **FromPort** *(integer) --* **[REQUIRED]** 
        
              Starting value for a range of allowed port numbers.
        
            - **ToPort** *(integer) --* **[REQUIRED]** 
        
              Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than ``FromPort`` .
        
            - **IpRange** *(string) --* **[REQUIRED]** 
        
              Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: \"``000.000.000.000/[subnet mask]`` \" or optionally the shortened version \"``0.0.0.0/[subnet mask]`` \".
        
            - **Protocol** *(string) --* **[REQUIRED]** 
        
              Network communication protocol used by the fleet.
        
        :type NewGameSessionProtectionPolicy: string
        :param NewGameSessionProtectionPolicy: 
        
          Game session protection policy to apply to all instances in this fleet. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet\'s protection policy using  UpdateFleetAttributes , but this change will only affect sessions created after the policy change. You can also set protection for individual instances using  UpdateGameSession .
        
          * **NoProtection** -- The game session can be terminated during a scale-down event. 
           
          * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be terminated during a scale-down event. 
           
        :type RuntimeConfiguration: dict
        :param RuntimeConfiguration: 
        
          Instructions for launching server processes on each instance in the fleet. The run-time configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance. A CreateFleet request must include a run-time configuration with at least one server process configuration; otherwise the request fails with an invalid request exception. (This parameter replaces the parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` ; requests that contain values for these parameters instead of a run-time configuration will continue to work.) 
        
          - **ServerProcesses** *(list) --* 
        
            Collection of server process configurations that describe which server processes to run on each instance in a fleet.
        
            - *(dict) --* 
        
              A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s ``  RuntimeConfiguration `` .
        
              - **LaunchPath** *(string) --* **[REQUIRED]** 
        
                Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances ``C:\game`` , and for Linux instances ``/local/game`` . A Windows game build with an executable file located at ``MyGame\latest\server.exe`` must have a launch path of \"``C:\game\MyGame\latest\server.exe`` \". A Linux game build with an executable file located at ``MyGame/latest/server.exe`` must have a launch path of \"``/local/game/MyGame/latest/server.exe`` \". 
        
              - **Parameters** *(string) --* 
        
                Optional list of parameters to pass to the server executable on launch.
        
              - **ConcurrentExecutions** *(integer) --* **[REQUIRED]** 
        
                Number of server processes using this configuration to run concurrently on an instance.
        
          - **MaxConcurrentGameSessionActivations** *(integer) --* 
        
            Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
        
          - **GameSessionActivationTimeoutSeconds** *(integer) --* 
        
            Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING`` . If the game session is not active before the timeout, activation is terminated and the game session status is changed to ``TERMINATED`` .
        
        :type ResourceCreationLimitPolicy: dict
        :param ResourceCreationLimitPolicy: 
        
          Policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
        
          - **NewGameSessionsPerCreator** *(integer) --* 
        
            Maximum number of game sessions that an individual can create during the policy period. 
        
          - **PolicyPeriodInMinutes** *(integer) --* 
        
            Time span used in evaluating the resource creation limit policy. 
        
        :type MetricGroups: list
        :param MetricGroups: 
        
          Name of a metric group to add this fleet to. A metric group tracks metrics across all fleets in the group. Use an existing metric group name to add this fleet to the group, or use a new name to create a new metric group. A fleet can only be included in one metric group at a time.
        
          - *(string) --* 
        
        :type PeerVpcAwsAccountId: string
        :param PeerVpcAwsAccountId: 
        
          Unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your Account ID in the AWS Management Console under account settings.
        
        :type PeerVpcId: string
        :param PeerVpcId: 
        
          Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
        
        :type FleetType: string
        :param FleetType: 
        
          Indicates whether to use on-demand instances or spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations, based on the instance type selected for this fleet. You can acquire on-demand instances at any time for a fixed price and keep them as long as you need them. Spot instances have lower prices, but spot pricing is variable, and while in use they can be interrupted (with a two-minute notification). Learn more about Amazon GameLift spot instances with at `Choose Computing Resources <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html>`__ . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetAttributes\': {
                    \'FleetId\': \'string\',
                    \'FleetArn\': \'string\',
                    \'FleetType\': \'ON_DEMAND\'|\'SPOT\',
                    \'InstanceType\': \'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\',
                    \'Description\': \'string\',
                    \'Name\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'TerminationTime\': datetime(2015, 1, 1),
                    \'Status\': \'NEW\'|\'DOWNLOADING\'|\'VALIDATING\'|\'BUILDING\'|\'ACTIVATING\'|\'ACTIVE\'|\'DELETING\'|\'ERROR\'|\'TERMINATED\',
                    \'BuildId\': \'string\',
                    \'ServerLaunchPath\': \'string\',
                    \'ServerLaunchParameters\': \'string\',
                    \'LogPaths\': [
                        \'string\',
                    ],
                    \'NewGameSessionProtectionPolicy\': \'NoProtection\'|\'FullProtection\',
                    \'OperatingSystem\': \'WINDOWS_2012\'|\'AMAZON_LINUX\',
                    \'ResourceCreationLimitPolicy\': {
                        \'NewGameSessionsPerCreator\': 123,
                        \'PolicyPeriodInMinutes\': 123
                    },
                    \'MetricGroups\': [
                        \'string\',
                    ],
                    \'StoppedActions\': [
                        \'AUTO_SCALING\',
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetAttributes** *(dict) --* 
        
              Properties for the newly created fleet.
        
              - **FleetId** *(string) --* 
        
                Unique identifier for a fleet.
        
              - **FleetArn** *(string) --* 
        
                Identifier for a fleet that is unique across all regions.
        
              - **FleetType** *(string) --* 
        
                Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may be interrupted with a two-minute notification.
        
              - **InstanceType** *(string) --* 
        
                EC2 instance type indicating the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.
        
              - **Description** *(string) --* 
        
                Human-readable description of the fleet.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **TerminationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **Status** *(string) --* 
        
                Current status of the fleet.
        
                Possible fleet statuses include the following:
        
                * **NEW** -- A new fleet has been defined and desired instances is set to 1.  
                 
                * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new fleet, creating new instances with the game build and starting server processes. 
                 
                * **ACTIVE** -- Hosts can now accept game sessions. 
                 
                * **ERROR** -- An error occurred when downloading, validating, building, or activating the fleet. 
                 
                * **DELETING** -- Hosts are responding to a delete fleet request. 
                 
                * **TERMINATED** -- The fleet no longer exists. 
                 
              - **BuildId** *(string) --* 
        
                Unique identifier for a build.
        
              - **ServerLaunchPath** *(string) --* 
        
                Path to a game server executable in the fleet\'s build, specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after this date are specified in the fleet\'s  RuntimeConfiguration .
        
              - **ServerLaunchParameters** *(string) --* 
        
                Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch parameters for fleets created after this date are specified in the fleet\'s  RuntimeConfiguration .
        
              - **LogPaths** *(list) --* 
        
                Location of default log files. When a server process is shut down, Amazon GameLift captures and stores any log files in this location. These logs are in addition to game session logs; see more on game session logs in the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__ . If no default log path for a fleet is specified, Amazon GameLift automatically uploads logs that are stored on each instance at ``C:\game\logs`` (for Windows) or ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs. 
        
                - *(string) --* 
            
              - **NewGameSessionProtectionPolicy** *(string) --* 
        
                Type of game session protection to set for all new instances started in the fleet.
        
                * **NoProtection** -- The game session can be terminated during a scale-down event. 
                 
                * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be terminated during a scale-down event. 
                 
              - **OperatingSystem** *(string) --* 
        
                Operating system of the fleet\'s computing resources. A fleet\'s operating system depends on the OS specified for the build that is deployed on this fleet.
        
              - **ResourceCreationLimitPolicy** *(dict) --* 
        
                Fleet policy to limit the number of game sessions an individual player can create over a span of time.
        
                - **NewGameSessionsPerCreator** *(integer) --* 
        
                  Maximum number of game sessions that an individual can create during the policy period. 
        
                - **PolicyPeriodInMinutes** *(integer) --* 
        
                  Time span used in evaluating the resource creation limit policy. 
        
              - **MetricGroups** *(list) --* 
        
                Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view metrics for an individual fleet or aggregated metrics for fleets that are in a fleet metric group. A fleet can be included in only one metric group at a time.
        
                - *(string) --* 
            
              - **StoppedActions** *(list) --* 
        
                List of fleet actions that have been suspended using  StopFleetActions . This includes auto-scaling.
        
                - *(string) --* 
            
        """
        pass

    def create_game_session(self, MaximumPlayerSessionCount: int, FleetId: str = None, AliasId: str = None, Name: str = None, GameProperties: List = None, CreatorId: str = None, GameSessionId: str = None, IdempotencyToken: str = None, GameSessionData: str = None) -> Dict:
        """
        
        To create a game session, specify either fleet ID or alias ID and indicate a maximum number of players to allow in the game session. You can also provide a name and game-specific properties for this game session. If successful, a  GameSession object is returned containing the game session properties and other settings you specified.
        
         **Idempotency tokens.** You can add a token that uniquely identifies game session requests. This is useful for ensuring that game session requests are idempotent. Multiple requests with the same idempotency token are processed only once; subsequent requests return the original result. All response values are the same with the exception of game session status, which may change.
        
         **Resource creation limits.** If you are creating a game session on a fleet with a resource creation limit policy in force, then you must specify a creator ID. Without this ID, Amazon GameLift has no way to evaluate the policy for this new game session request.
        
         **Player acceptance policy.** By default, newly created game sessions are open to new players. You can restrict new player access by using  UpdateGameSession to change the game session\'s player session creation policy.
        
         **Game session logs.** Logs are retained for all active game sessions for 14 days. To access the logs, call  GetGameSessionLogUrl to download the log files.
        
         *Available in Amazon GameLift Local.*  
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateGameSession>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_game_session(
              FleetId=\'string\',
              AliasId=\'string\',
              MaximumPlayerSessionCount=123,
              Name=\'string\',
              GameProperties=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              CreatorId=\'string\',
              GameSessionId=\'string\',
              IdempotencyToken=\'string\',
              GameSessionData=\'string\'
          )
        :type FleetId: string
        :param FleetId: 
        
          Unique identifier for a fleet to create a game session in. Each request must reference either a fleet ID or alias ID, but not both.
        
        :type AliasId: string
        :param AliasId: 
        
          Unique identifier for an alias associated with the fleet to create a game session in. Each request must reference either a fleet ID or alias ID, but not both.
        
        :type MaximumPlayerSessionCount: integer
        :param MaximumPlayerSessionCount: **[REQUIRED]** 
        
          Maximum number of players that can be connected simultaneously to the game session.
        
        :type Name: string
        :param Name: 
        
          Descriptive label that is associated with a game session. Session names do not need to be unique.
        
        :type GameProperties: list
        :param GameProperties: 
        
          Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
          - *(dict) --* 
        
            Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              Game property identifier.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              Game property value.
        
        :type CreatorId: string
        :param CreatorId: 
        
          Unique identifier for a player or entity creating the game session. This ID is used to enforce a resource protection policy (if one exists) that limits the number of concurrent active game sessions one player can have.
        
        :type GameSessionId: string
        :param GameSessionId: 
        
           *This parameter is no longer preferred. Please use ``IdempotencyToken`` instead.* Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session\'s ID. (A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .) 
        
        :type IdempotencyToken: string
        :param IdempotencyToken: 
        
          Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session\'s ID. (A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .) Idempotency tokens remain in use for 30 days after a game session has ended; game session objects are retained for this time period and then deleted.
        
        :type GameSessionData: string
        :param GameSessionData: 
        
          Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSession\': {
                    \'GameSessionId\': \'string\',
                    \'Name\': \'string\',
                    \'FleetId\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'TerminationTime\': datetime(2015, 1, 1),
                    \'CurrentPlayerSessionCount\': 123,
                    \'MaximumPlayerSessionCount\': 123,
                    \'Status\': \'ACTIVE\'|\'ACTIVATING\'|\'TERMINATED\'|\'TERMINATING\'|\'ERROR\',
                    \'StatusReason\': \'INTERRUPTED\',
                    \'GameProperties\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'IpAddress\': \'string\',
                    \'Port\': 123,
                    \'PlayerSessionCreationPolicy\': \'ACCEPT_ALL\'|\'DENY_ALL\',
                    \'CreatorId\': \'string\',
                    \'GameSessionData\': \'string\',
                    \'MatchmakerData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSession** *(dict) --* 
        
              Object that describes the newly created game session record.
        
              - **GameSessionId** *(string) --* 
        
                Unique identifier for the game session. A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with a game session. Session names do not need to be unique.
        
              - **FleetId** *(string) --* 
        
                Unique identifier for a fleet that the game session is running on.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **TerminationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **CurrentPlayerSessionCount** *(integer) --* 
        
                Number of players currently in the game session.
        
              - **MaximumPlayerSessionCount** *(integer) --* 
        
                Maximum number of players that can be connected simultaneously to the game session.
        
              - **Status** *(string) --* 
        
                Current status of the game session. A game session must have an ``ACTIVE`` status to have player sessions.
        
              - **StatusReason** *(string) --* 
        
                Provides additional information about game session status. ``INTERRUPTED`` indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.
        
              - **GameProperties** *(list) --* 
        
                Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). You can search for active game sessions based on this custom data with  SearchGameSessions .
        
                - *(dict) --* 
        
                  Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                  - **Key** *(string) --* 
        
                    Game property identifier.
        
                  - **Value** *(string) --* 
        
                    Game property value.
        
              - **IpAddress** *(string) --* 
        
                IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
              - **Port** *(integer) --* 
        
                Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
              - **PlayerSessionCreationPolicy** *(string) --* 
        
                Indicates whether or not the game session is accepting new players.
        
              - **CreatorId** *(string) --* 
        
                Unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
        
              - **GameSessionData** *(string) --* 
        
                Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
              - **MatchmakerData** *(string) --* 
        
                Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ). 
        
        """
        pass

    def create_game_session_queue(self, Name: str, TimeoutInSeconds: int = None, PlayerLatencyPolicies: List = None, Destinations: List = None) -> Dict:
        """
        
         **Destination order.** When processing a request for a game session, Amazon GameLift tries each destination in order until it finds one with available resources to host the new game session. A queue\'s default order is determined by how destinations are listed. The default order is overridden when a game session placement request provides player latency information. Player latency information enables Amazon GameLift to prioritize destinations where players report the lowest average latency, as a result placing the new game session where the majority of players will have the best possible gameplay experience.
        
         **Player latency policies.** For placement requests containing player latency information, use player latency policies to protect individual players from very high latencies. With a latency cap, even when a destination can deliver a low latency for most players, the game is not placed where any individual player is reporting latency higher than a policy\'s maximum. A queue can have multiple latency policies, which are enforced consecutively starting with the policy with the lowest latency cap. Use multiple policies to gradually relax latency controls; for example, you might set a policy with a low latency cap for the first 60 seconds, a second policy with a higher cap for the next 60 seconds, etc. 
        
        To create a new queue, provide a name, timeout value, a list of destinations and, if desired, a set of latency policies. If successful, a new queue object is returned.
        
        Queue-related operations include:
        
        *  CreateGameSessionQueue   
         
        *  DescribeGameSessionQueues   
         
        *  UpdateGameSessionQueue   
         
        *  DeleteGameSessionQueue   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateGameSessionQueue>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_game_session_queue(
              Name=\'string\',
              TimeoutInSeconds=123,
              PlayerLatencyPolicies=[
                  {
                      \'MaximumIndividualPlayerLatencyMilliseconds\': 123,
                      \'PolicyDurationSeconds\': 123
                  },
              ],
              Destinations=[
                  {
                      \'DestinationArn\': \'string\'
                  },
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
        :type TimeoutInSeconds: integer
        :param TimeoutInSeconds: 
        
          Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status.
        
        :type PlayerLatencyPolicies: list
        :param PlayerLatencyPolicies: 
        
          Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. A player latency policy must set a value for MaximumIndividualPlayerLatencyMilliseconds; if none is set, this API requests will fail.
        
          - *(dict) --* 
        
            Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
        
            Queue-related operations include:
        
            *  CreateGameSessionQueue   
             
            *  DescribeGameSessionQueues   
             
            *  UpdateGameSessionQueue   
             
            *  DeleteGameSessionQueue   
             
            - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --* 
        
              The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
        
            - **PolicyDurationSeconds** *(integer) --* 
        
              The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
        
        :type Destinations: list
        :param Destinations: 
        
          List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
        
          - *(dict) --* 
        
            Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue. 
        
            Queue-related operations include:
        
            *  CreateGameSessionQueue   
             
            *  DescribeGameSessionQueues   
             
            *  UpdateGameSessionQueue   
             
            *  DeleteGameSessionQueue   
             
            - **DestinationArn** *(string) --* 
        
              Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessionQueue\': {
                    \'Name\': \'string\',
                    \'GameSessionQueueArn\': \'string\',
                    \'TimeoutInSeconds\': 123,
                    \'PlayerLatencyPolicies\': [
                        {
                            \'MaximumIndividualPlayerLatencyMilliseconds\': 123,
                            \'PolicyDurationSeconds\': 123
                        },
                    ],
                    \'Destinations\': [
                        {
                            \'DestinationArn\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessionQueue** *(dict) --* 
        
              Object that describes the newly created game session queue.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
              - **GameSessionQueueArn** *(string) --* 
        
                Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` .
        
              - **TimeoutInSeconds** *(integer) --* 
        
                Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status.
        
              - **PlayerLatencyPolicies** *(list) --* 
        
                Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. 
        
                - *(dict) --* 
        
                  Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
        
                  Queue-related operations include:
        
                  *  CreateGameSessionQueue   
                   
                  *  DescribeGameSessionQueues   
                   
                  *  UpdateGameSessionQueue   
                   
                  *  DeleteGameSessionQueue   
                   
                  - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --* 
        
                    The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
        
                  - **PolicyDurationSeconds** *(integer) --* 
        
                    The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
        
              - **Destinations** *(list) --* 
        
                List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
        
                - *(dict) --* 
        
                  Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue. 
        
                  Queue-related operations include:
        
                  *  CreateGameSessionQueue   
                   
                  *  DescribeGameSessionQueues   
                   
                  *  UpdateGameSessionQueue   
                   
                  *  DeleteGameSessionQueue   
                   
                  - **DestinationArn** *(string) --* 
        
                    Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions. 
        
        """
        pass

    def create_matchmaking_configuration(self, Name: str, GameSessionQueueArns: List, RequestTimeoutSeconds: int, AcceptanceRequired: bool, RuleSetName: str, Description: str = None, AcceptanceTimeoutSeconds: int = None, NotificationTarget: str = None, AdditionalPlayerCount: int = None, CustomEventData: str = None, GameProperties: List = None, GameSessionData: str = None) -> Dict:
        """
        
        To create a matchmaking configuration, at a minimum you must specify the following: configuration name; a rule set that governs how to evaluate players and find acceptable matches; a game session queue to use when placing a new game session for the match; and the maximum time allowed for a matchmaking attempt.
        
         **Player acceptance** -- In each configuration, you have the option to require that all players accept participation in a proposed match. To enable this feature, set *AcceptanceRequired* to true and specify a time limit for player acceptance. Players have the option to accept or reject a proposed match, and a match does not move ahead to game session placement unless all matched players accept. 
        
         **Matchmaking status notification** -- There are two ways to track the progress of matchmaking tickets: (1) polling ticket status with  DescribeMatchmaking ; or (2) receiving notifications with Amazon Simple Notification Service (SNS). To use notifications, you first need to set up an SNS topic to receive the notifications, and provide the topic ARN in the matchmaking configuration (see `Setting up Notifications for Matchmaking <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-notification.html>`__ ). Since notifications promise only \"best effort\" delivery, we recommend calling ``DescribeMatchmaking`` if no notifications are received within 30 seconds.
        
        Operations related to match configurations and rule sets include:
        
        *  CreateMatchmakingConfiguration   
         
        *  DescribeMatchmakingConfigurations   
         
        *  UpdateMatchmakingConfiguration   
         
        *  DeleteMatchmakingConfiguration   
         
        *  CreateMatchmakingRuleSet   
         
        *  DescribeMatchmakingRuleSets   
         
        *  ValidateMatchmakingRuleSet   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateMatchmakingConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_matchmaking_configuration(
              Name=\'string\',
              Description=\'string\',
              GameSessionQueueArns=[
                  \'string\',
              ],
              RequestTimeoutSeconds=123,
              AcceptanceTimeoutSeconds=123,
              AcceptanceRequired=True|False,
              RuleSetName=\'string\',
              NotificationTarget=\'string\',
              AdditionalPlayerCount=123,
              CustomEventData=\'string\',
              GameProperties=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              GameSessionData=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
        
        :type Description: string
        :param Description: 
        
          Meaningful description of the matchmaking configuration. 
        
        :type GameSessionQueueArns: list
        :param GameSessionQueueArns: **[REQUIRED]** 
        
          Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
        
          - *(string) --* 
        
        :type RequestTimeoutSeconds: integer
        :param RequestTimeoutSeconds: **[REQUIRED]** 
        
          Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
        
        :type AcceptanceTimeoutSeconds: integer
        :param AcceptanceTimeoutSeconds: 
        
          Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
        
        :type AcceptanceRequired: boolean
        :param AcceptanceRequired: **[REQUIRED]** 
        
          Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
        
        :type RuleSetName: string
        :param RuleSetName: **[REQUIRED]** 
        
          Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
        
        :type NotificationTarget: string
        :param NotificationTarget: 
        
          SNS topic ARN that is set up to receive matchmaking notifications.
        
        :type AdditionalPlayerCount: integer
        :param AdditionalPlayerCount: 
        
          Number of player slots in a match to keep open for future players. For example, if the configuration\'s rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.
        
        :type CustomEventData: string
        :param CustomEventData: 
        
          Information to attached to all events related to the matchmaking configuration. 
        
        :type GameProperties: list
        :param GameProperties: 
        
          Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
          - *(dict) --* 
        
            Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              Game property identifier.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              Game property value.
        
        :type GameSessionData: string
        :param GameSessionData: 
        
          Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Configuration\': {
                    \'Name\': \'string\',
                    \'Description\': \'string\',
                    \'GameSessionQueueArns\': [
                        \'string\',
                    ],
                    \'RequestTimeoutSeconds\': 123,
                    \'AcceptanceTimeoutSeconds\': 123,
                    \'AcceptanceRequired\': True|False,
                    \'RuleSetName\': \'string\',
                    \'NotificationTarget\': \'string\',
                    \'AdditionalPlayerCount\': 123,
                    \'CustomEventData\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'GameProperties\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'GameSessionData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Configuration** *(dict) --* 
        
              Object that describes the newly created matchmaking configuration.
        
              - **Name** *(string) --* 
        
                Unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
        
              - **Description** *(string) --* 
        
                Descriptive label that is associated with matchmaking configuration.
        
              - **GameSessionQueueArns** *(list) --* 
        
                Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
        
                - *(string) --* 
            
              - **RequestTimeoutSeconds** *(integer) --* 
        
                Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
        
              - **AcceptanceTimeoutSeconds** *(integer) --* 
        
                Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
        
              - **AcceptanceRequired** *(boolean) --* 
        
                Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
        
              - **RuleSetName** *(string) --* 
        
                Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
        
              - **NotificationTarget** *(string) --* 
        
                SNS topic ARN that is set up to receive matchmaking notifications.
        
              - **AdditionalPlayerCount** *(integer) --* 
        
                Number of player slots in a match to keep open for future players. For example, if the configuration\'s rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.
        
              - **CustomEventData** *(string) --* 
        
                Information to attached to all events related to the matchmaking configuration. 
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **GameProperties** *(list) --* 
        
                Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
                - *(dict) --* 
        
                  Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                  - **Key** *(string) --* 
        
                    Game property identifier.
        
                  - **Value** *(string) --* 
        
                    Game property value.
        
              - **GameSessionData** *(string) --* 
        
                Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
        """
        pass

    def create_matchmaking_rule_set(self, Name: str, RuleSetBody: str) -> Dict:
        """
        
        Once created, matchmaking rule sets cannot be changed or deleted, so we recommend checking the rule set syntax using  ValidateMatchmakingRuleSet before creating the rule set.
        
        To create a matchmaking rule set, provide the set of rules and a unique name. Rule sets must be defined in the same region as the matchmaking configuration they will be used with. Rule sets cannot be edited or deleted. If you need to change a rule set, create a new one with the necessary edits and then update matchmaking configurations to use the new rule set.
        
        Operations related to match configurations and rule sets include:
        
        *  CreateMatchmakingConfiguration   
         
        *  DescribeMatchmakingConfigurations   
         
        *  UpdateMatchmakingConfiguration   
         
        *  DeleteMatchmakingConfiguration   
         
        *  CreateMatchmakingRuleSet   
         
        *  DescribeMatchmakingRuleSets   
         
        *  ValidateMatchmakingRuleSet   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateMatchmakingRuleSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_matchmaking_rule_set(
              Name=\'string\',
              RuleSetBody=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Unique identifier for a matchmaking rule set. This name is used to identify the rule set associated with a matchmaking configuration.
        
        :type RuleSetBody: string
        :param RuleSetBody: **[REQUIRED]** 
        
          Collection of matchmaking rules, formatted as a JSON string. (Note that comments are not allowed in JSON, but most elements support a description field.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RuleSet\': {
                    \'RuleSetName\': \'string\',
                    \'RuleSetBody\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **RuleSet** *(dict) --* 
        
              Object that describes the newly created matchmaking rule set.
        
              - **RuleSetName** *(string) --* 
        
                Unique identifier for a matchmaking rule set
        
              - **RuleSetBody** *(string) --* 
        
                Collection of matchmaking rules, formatted as a JSON string. (Note that comments14 are not allowed in JSON, but most elements support a description field.)
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
        """
        pass

    def create_player_session(self, GameSessionId: str, PlayerId: str, PlayerData: str = None) -> Dict:
        """
        
        To create a player session, specify a game session ID, player ID, and optionally a string of player data. If successful, the player is added to the game session and a new  PlayerSession object is returned. Player sessions cannot be updated. 
        
         *Available in Amazon GameLift Local.*  
        
        Player-session-related operations include:
        
        *  CreatePlayerSession   
         
        *  CreatePlayerSessions   
         
        *  DescribePlayerSessions   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreatePlayerSession>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_player_session(
              GameSessionId=\'string\',
              PlayerId=\'string\',
              PlayerData=\'string\'
          )
        :type GameSessionId: string
        :param GameSessionId: **[REQUIRED]** 
        
          Unique identifier for the game session to add a player to.
        
        :type PlayerId: string
        :param PlayerId: **[REQUIRED]** 
        
          Unique identifier for a player. Player IDs are developer-defined.
        
        :type PlayerData: string
        :param PlayerData: 
        
          Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PlayerSession\': {
                    \'PlayerSessionId\': \'string\',
                    \'PlayerId\': \'string\',
                    \'GameSessionId\': \'string\',
                    \'FleetId\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'TerminationTime\': datetime(2015, 1, 1),
                    \'Status\': \'RESERVED\'|\'ACTIVE\'|\'COMPLETED\'|\'TIMEDOUT\',
                    \'IpAddress\': \'string\',
                    \'Port\': 123,
                    \'PlayerData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **PlayerSession** *(dict) --* 
        
              Object that describes the newly created player session record.
        
              - **PlayerSessionId** *(string) --* 
        
                Unique identifier for a player session.
        
              - **PlayerId** *(string) --* 
        
                Unique identifier for a player that is associated with this player session.
        
              - **GameSessionId** *(string) --* 
        
                Unique identifier for the game session that the player session is connected to.
        
              - **FleetId** *(string) --* 
        
                Unique identifier for a fleet that the player\'s game session is running on.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **TerminationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **Status** *(string) --* 
        
                Current status of the player session.
        
                Possible player session statuses include the following:
        
                * **RESERVED** -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.  
                 
                * **ACTIVE** -- The player has been validated by the server process and is currently connected. 
                 
                * **COMPLETED** -- The player connection has been dropped. 
                 
                * **TIMEDOUT** -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds). 
                 
              - **IpAddress** *(string) --* 
        
                IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
              - **Port** *(integer) --* 
        
                Port number for the game session. To connect to a Amazon GameLift server process, an app needs both the IP address and port number.
        
              - **PlayerData** *(string) --* 
        
                Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. 
        
        """
        pass

    def create_player_sessions(self, GameSessionId: str, PlayerIds: List, PlayerDataMap: Dict = None) -> Dict:
        """
        
        To create player sessions, specify a game session ID, a list of player IDs, and optionally a set of player data strings. If successful, the players are added to the game session and a set of new  PlayerSession objects is returned. Player sessions cannot be updated.
        
         *Available in Amazon GameLift Local.*  
        
        Player-session-related operations include:
        
        *  CreatePlayerSession   
         
        *  CreatePlayerSessions   
         
        *  DescribePlayerSessions   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreatePlayerSessions>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_player_sessions(
              GameSessionId=\'string\',
              PlayerIds=[
                  \'string\',
              ],
              PlayerDataMap={
                  \'string\': \'string\'
              }
          )
        :type GameSessionId: string
        :param GameSessionId: **[REQUIRED]** 
        
          Unique identifier for the game session to add players to.
        
        :type PlayerIds: list
        :param PlayerIds: **[REQUIRED]** 
        
          List of unique identifiers for the players to be added.
        
          - *(string) --* 
        
        :type PlayerDataMap: dict
        :param PlayerDataMap: 
        
          Map of string pairs, each specifying a player ID and a set of developer-defined information related to the player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. Player data strings for player IDs not included in the ``PlayerIds`` parameter are ignored. 
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PlayerSessions\': [
                    {
                        \'PlayerSessionId\': \'string\',
                        \'PlayerId\': \'string\',
                        \'GameSessionId\': \'string\',
                        \'FleetId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'TerminationTime\': datetime(2015, 1, 1),
                        \'Status\': \'RESERVED\'|\'ACTIVE\'|\'COMPLETED\'|\'TIMEDOUT\',
                        \'IpAddress\': \'string\',
                        \'Port\': 123,
                        \'PlayerData\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **PlayerSessions** *(list) --* 
        
              Collection of player session objects created for the added players.
        
              - *(dict) --* 
        
                Properties describing a player session. Player session objects are created either by creating a player session for a specific game session, or as part of a game session placement. A player session represents either a player reservation for a game session (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A player session object (including player data) is automatically passed to a game session when the player connects to the game session and is validated.
        
                When a player disconnects, the player session status changes to ``COMPLETED`` . Once the session ends, the player session object is retained for 30 days and then removed.
        
                Player-session-related operations include:
        
                *  CreatePlayerSession   
                 
                *  CreatePlayerSessions   
                 
                *  DescribePlayerSessions   
                 
                * Game session placements 
        
                  *  StartGameSessionPlacement   
                   
                  *  DescribeGameSessionPlacement   
                   
                  *  StopGameSessionPlacement   
                   
                - **PlayerSessionId** *(string) --* 
        
                  Unique identifier for a player session.
        
                - **PlayerId** *(string) --* 
        
                  Unique identifier for a player that is associated with this player session.
        
                - **GameSessionId** *(string) --* 
        
                  Unique identifier for the game session that the player session is connected to.
        
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that the player\'s game session is running on.
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **TerminationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **Status** *(string) --* 
        
                  Current status of the player session.
        
                  Possible player session statuses include the following:
        
                  * **RESERVED** -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.  
                   
                  * **ACTIVE** -- The player has been validated by the server process and is currently connected. 
                   
                  * **COMPLETED** -- The player connection has been dropped. 
                   
                  * **TIMEDOUT** -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds). 
                   
                - **IpAddress** *(string) --* 
        
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **Port** *(integer) --* 
        
                  Port number for the game session. To connect to a Amazon GameLift server process, an app needs both the IP address and port number.
        
                - **PlayerData** *(string) --* 
        
                  Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. 
        
        """
        pass

    def create_vpc_peering_authorization(self, GameLiftAwsAccountId: str, PeerVpcId: str) -> Dict:
        """
        
        You can peer with VPCs that are owned by any AWS account you have access to, including the account that you use to manage your Amazon GameLift fleets. You cannot peer with VPCs that are in different regions.
        
        To request authorization to create a connection, call this operation from the AWS account with the VPC that you want to peer to your Amazon GameLift fleet. For example, to enable your game servers to retrieve data from a DynamoDB table, use the account that manages that DynamoDB resource. Identify the following values: (1) The ID of the VPC that you want to peer with, and (2) the ID of the AWS account that you use to manage Amazon GameLift. If successful, VPC peering is authorized for the specified VPC. 
        
        To request authorization to delete a connection, call this operation from the AWS account with the VPC that is peered with your Amazon GameLift fleet. Identify the following values: (1) VPC ID that you want to delete the peering connection for, and (2) ID of the AWS account that you use to manage Amazon GameLift. 
        
        The authorization remains valid for 24 hours unless it is canceled by a call to  DeleteVpcPeeringAuthorization . You must create or delete the peering connection while the authorization is valid. 
        
        VPC peering connection operations include:
        
        *  CreateVpcPeeringAuthorization   
         
        *  DescribeVpcPeeringAuthorizations   
         
        *  DeleteVpcPeeringAuthorization   
         
        *  CreateVpcPeeringConnection   
         
        *  DescribeVpcPeeringConnections   
         
        *  DeleteVpcPeeringConnection   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateVpcPeeringAuthorization>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_vpc_peering_authorization(
              GameLiftAwsAccountId=\'string\',
              PeerVpcId=\'string\'
          )
        :type GameLiftAwsAccountId: string
        :param GameLiftAwsAccountId: **[REQUIRED]** 
        
          Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
        
        :type PeerVpcId: string
        :param PeerVpcId: **[REQUIRED]** 
        
          Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'VpcPeeringAuthorization\': {
                    \'GameLiftAwsAccountId\': \'string\',
                    \'PeerVpcAwsAccountId\': \'string\',
                    \'PeerVpcId\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'ExpirationTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **VpcPeeringAuthorization** *(dict) --* 
        
              Details on the requested VPC peering authorization, including expiration.
        
              - **GameLiftAwsAccountId** *(string) --* 
        
                Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
        
              - **PeerVpcAwsAccountId** *(string) --* 
        
              - **PeerVpcId** *(string) --* 
        
                Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this authorization was issued. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **ExpirationTime** *(datetime) --* 
        
                Time stamp indicating when this authorization expires (24 hours after issuance). Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
        """
        pass

    def create_vpc_peering_connection(self, FleetId: str, PeerVpcAwsAccountId: str, PeerVpcId: str) -> Dict:
        """
        
        Before calling this operation to establish the peering connection, you first need to call  CreateVpcPeeringAuthorization and identify the VPC you want to peer with. Once the authorization for the specified VPC is issued, you have 24 hours to establish the connection. These two operations handle all tasks necessary to peer the two VPCs, including acceptance, updating routing tables, etc. 
        
        To establish the connection, call this operation from the AWS account that is used to manage the Amazon GameLift fleets. Identify the following values: (1) The ID of the fleet you want to be enable a VPC peering connection for; (2) The AWS account with the VPC that you want to peer with; and (3) The ID of the VPC you want to peer with. This operation is asynchronous. If successful, a  VpcPeeringConnection request is created. You can use continuous polling to track the request\'s status using  DescribeVpcPeeringConnections , or by monitoring fleet events for success or failure using  DescribeFleetEvents . 
        
        VPC peering connection operations include:
        
        *  CreateVpcPeeringAuthorization   
         
        *  DescribeVpcPeeringAuthorizations   
         
        *  DeleteVpcPeeringAuthorization   
         
        *  CreateVpcPeeringConnection   
         
        *  DescribeVpcPeeringConnections   
         
        *  DeleteVpcPeeringConnection   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateVpcPeeringConnection>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_vpc_peering_connection(
              FleetId=\'string\',
              PeerVpcAwsAccountId=\'string\',
              PeerVpcId=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet. This tells Amazon GameLift which GameLift VPC to peer with. 
        
        :type PeerVpcAwsAccountId: string
        :param PeerVpcAwsAccountId: **[REQUIRED]** 
        
          Unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your Account ID in the AWS Management Console under account settings.
        
        :type PeerVpcId: string
        :param PeerVpcId: **[REQUIRED]** 
        
          Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_alias(self, AliasId: str) -> NoReturn:
        """
        
        Alias-related operations include:
        
        *  CreateAlias   
         
        *  ListAliases   
         
        *  DescribeAlias   
         
        *  UpdateAlias   
         
        *  DeleteAlias   
         
        *  ResolveAlias   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DeleteAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_alias(
              AliasId=\'string\'
          )
        :type AliasId: string
        :param AliasId: **[REQUIRED]** 
        
          Unique identifier for a fleet alias. Specify the alias you want to delete.
        
        :returns: None
        """
        pass

    def delete_build(self, BuildId: str) -> NoReturn:
        """
        
        To delete a build, specify its ID. Deleting a build does not affect the status of any active fleets using the build, but you can no longer create new fleets with the deleted build.
        
        Build-related operations include:
        
        *  CreateBuild   
         
        *  ListBuilds   
         
        *  DescribeBuild   
         
        *  UpdateBuild   
         
        *  DeleteBuild   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DeleteBuild>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_build(
              BuildId=\'string\'
          )
        :type BuildId: string
        :param BuildId: **[REQUIRED]** 
        
          Unique identifier for a build to delete.
        
        :returns: None
        """
        pass

    def delete_fleet(self, FleetId: str) -> NoReturn:
        """
        
        This action removes the fleet\'s resources and the fleet record. Once a fleet is deleted, you can no longer use that fleet.
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DeleteFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_fleet(
              FleetId=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to be deleted.
        
        :returns: None
        """
        pass

    def delete_game_session_queue(self, Name: str) -> Dict:
        """
        
        Queue-related operations include:
        
        *  CreateGameSessionQueue   
         
        *  DescribeGameSessionQueues   
         
        *  UpdateGameSessionQueue   
         
        *  DeleteGameSessionQueue   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DeleteGameSessionQueue>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_game_session_queue(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_matchmaking_configuration(self, Name: str) -> Dict:
        """
        
        Operations related to match configurations and rule sets include:
        
        *  CreateMatchmakingConfiguration   
         
        *  DescribeMatchmakingConfigurations   
         
        *  UpdateMatchmakingConfiguration   
         
        *  DeleteMatchmakingConfiguration   
         
        *  CreateMatchmakingRuleSet   
         
        *  DescribeMatchmakingRuleSets   
         
        *  ValidateMatchmakingRuleSet   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DeleteMatchmakingConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_matchmaking_configuration(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Unique identifier for a matchmaking configuration
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_scaling_policy(self, Name: str, FleetId: str) -> NoReturn:
        """
        
        To temporarily suspend scaling policies, call  StopFleetActions . This operation suspends all policies for the fleet.
        
        Operations related to fleet capacity scaling include:
        
        *  DescribeFleetCapacity   
         
        *  UpdateFleetCapacity   
         
        *  DescribeEC2InstanceLimits   
         
        * Manage scaling policies: 
        
          *  PutScalingPolicy (auto-scaling) 
           
          *  DescribeScalingPolicies (auto-scaling) 
           
          *  DeleteScalingPolicy (auto-scaling) 
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DeleteScalingPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_scaling_policy(
              Name=\'string\',
              FleetId=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Descriptive label that is associated with a scaling policy. Policy names do not need to be unique.
        
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to be deleted.
        
        :returns: None
        """
        pass

    def delete_vpc_peering_authorization(self, GameLiftAwsAccountId: str, PeerVpcId: str) -> Dict:
        """
        
        VPC peering connection operations include:
        
        *  CreateVpcPeeringAuthorization   
         
        *  DescribeVpcPeeringAuthorizations   
         
        *  DeleteVpcPeeringAuthorization   
         
        *  CreateVpcPeeringConnection   
         
        *  DescribeVpcPeeringConnections   
         
        *  DeleteVpcPeeringConnection   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DeleteVpcPeeringAuthorization>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_vpc_peering_authorization(
              GameLiftAwsAccountId=\'string\',
              PeerVpcId=\'string\'
          )
        :type GameLiftAwsAccountId: string
        :param GameLiftAwsAccountId: **[REQUIRED]** 
        
          Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
        
        :type PeerVpcId: string
        :param PeerVpcId: **[REQUIRED]** 
        
          Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_vpc_peering_connection(self, FleetId: str, VpcPeeringConnectionId: str) -> Dict:
        """
        
        Once a valid authorization exists, call this operation from the AWS account that is used to manage the Amazon GameLift fleets. Identify the connection to delete by the connection ID and fleet ID. If successful, the connection is removed. 
        
        VPC peering connection operations include:
        
        *  CreateVpcPeeringAuthorization   
         
        *  DescribeVpcPeeringAuthorizations   
         
        *  DeleteVpcPeeringAuthorization   
         
        *  CreateVpcPeeringConnection   
         
        *  DescribeVpcPeeringConnections   
         
        *  DeleteVpcPeeringConnection   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DeleteVpcPeeringConnection>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_vpc_peering_connection(
              FleetId=\'string\',
              VpcPeeringConnectionId=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet. This value must match the fleet ID referenced in the VPC peering connection record.
        
        :type VpcPeeringConnectionId: string
        :param VpcPeeringConnectionId: **[REQUIRED]** 
        
          Unique identifier for a VPC peering connection. This value is included in the  VpcPeeringConnection object, which can be retrieved by calling  DescribeVpcPeeringConnections .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_alias(self, AliasId: str) -> Dict:
        """
        
        To get alias properties, specify the alias ID. If successful, the requested alias record is returned.
        
        Alias-related operations include:
        
        *  CreateAlias   
         
        *  ListAliases   
         
        *  DescribeAlias   
         
        *  UpdateAlias   
         
        *  DeleteAlias   
         
        *  ResolveAlias   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_alias(
              AliasId=\'string\'
          )
        :type AliasId: string
        :param AliasId: **[REQUIRED]** 
        
          Unique identifier for a fleet alias. Specify the alias you want to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Alias\': {
                    \'AliasId\': \'string\',
                    \'Name\': \'string\',
                    \'AliasArn\': \'string\',
                    \'Description\': \'string\',
                    \'RoutingStrategy\': {
                        \'Type\': \'SIMPLE\'|\'TERMINAL\',
                        \'FleetId\': \'string\',
                        \'Message\': \'string\'
                    },
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'LastUpdatedTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Alias** *(dict) --* 
        
              Object that contains the requested alias.
        
              - **AliasId** *(string) --* 
        
                Unique identifier for an alias; alias IDs are unique within a region.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with an alias. Alias names do not need to be unique.
        
              - **AliasArn** *(string) --* 
        
                Unique identifier for an alias; alias ARNs are unique across all regions.
        
              - **Description** *(string) --* 
        
                Human-readable description of an alias.
        
              - **RoutingStrategy** *(dict) --* 
        
                Alias configuration for the alias, including routing type and settings.
        
                - **Type** *(string) --* 
        
                  Type of routing strategy.
        
                  Possible routing types include the following:
        
                  * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets. 
                   
                  * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded. 
                   
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that the alias points to.
        
                - **Message** *(string) --* 
        
                  Message text to be used with a terminal routing strategy.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **LastUpdatedTime** *(datetime) --* 
        
                Time stamp indicating when this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
        """
        pass

    def describe_build(self, BuildId: str) -> Dict:
        """
        
        Build-related operations include:
        
        *  CreateBuild   
         
        *  ListBuilds   
         
        *  DescribeBuild   
         
        *  UpdateBuild   
         
        *  DeleteBuild   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeBuild>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_build(
              BuildId=\'string\'
          )
        :type BuildId: string
        :param BuildId: **[REQUIRED]** 
        
          Unique identifier for a build to retrieve properties for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Build\': {
                    \'BuildId\': \'string\',
                    \'Name\': \'string\',
                    \'Version\': \'string\',
                    \'Status\': \'INITIALIZED\'|\'READY\'|\'FAILED\',
                    \'SizeOnDisk\': 123,
                    \'OperatingSystem\': \'WINDOWS_2012\'|\'AMAZON_LINUX\',
                    \'CreationTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Build** *(dict) --* 
        
              Set of properties describing the requested build.
        
              - **BuildId** *(string) --* 
        
                Unique identifier for a build.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .
        
              - **Version** *(string) --* 
        
                Version that is associated with this build. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .
        
              - **Status** *(string) --* 
        
                Current status of the build.
        
                Possible build statuses include the following:
        
                * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.  
                 
                * **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build. 
                 
                * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.  
                 
              - **SizeOnDisk** *(integer) --* 
        
                File size of the uploaded game build, expressed in bytes. When the build status is ``INITIALIZED`` , this value is 0.
        
              - **OperatingSystem** *(string) --* 
        
                Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
        """
        pass

    def describe_ec2_instance_limits(self, EC2InstanceType: str = None) -> Dict:
        """
        Retrieves the following information for the specified EC2 instance type:
        
        * maximum number of instances allowed per AWS account (service limit) 
         
        * current usage level for the AWS account 
         
        Service limits vary depending on region. Available regions for Amazon GameLift can be found in the AWS Management Console for Amazon GameLift (see the drop-down list in the upper right corner).
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeEC2InstanceLimits>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_ec2_instance_limits(
              EC2InstanceType=\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'
          )
        :type EC2InstanceType: string
        :param EC2InstanceType: 
        
          Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions. Leave this parameter blank to retrieve limits for all types.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EC2InstanceLimits\': [
                    {
                        \'EC2InstanceType\': \'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\',
                        \'CurrentInstances\': 123,
                        \'InstanceLimit\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **EC2InstanceLimits** *(list) --* 
        
              Object that contains the maximum number of instances for the specified instance type.
        
              - *(dict) --* 
        
                Maximum number of instances allowed based on the Amazon Elastic Compute Cloud (Amazon EC2) instance type. Instance limits can be retrieved by calling  DescribeEC2InstanceLimits .
        
                - **EC2InstanceType** *(string) --* 
        
                  Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.
        
                - **CurrentInstances** *(integer) --* 
        
                  Number of instances of the specified type that are currently in use by this AWS account.
        
                - **InstanceLimit** *(integer) --* 
        
                  Number of instances allowed.
        
        """
        pass

    def describe_fleet_attributes(self, FleetIds: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          Some API actions may limit the number of fleet IDs allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_fleet_attributes(
              FleetIds=[
                  \'string\',
              ],
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetIds: list
        :param FleetIds: 
        
          Unique identifier for a fleet(s) to retrieve attributes for. To request attributes for all fleets, leave this parameter empty.
        
          - *(string) --* 
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetAttributes\': [
                    {
                        \'FleetId\': \'string\',
                        \'FleetArn\': \'string\',
                        \'FleetType\': \'ON_DEMAND\'|\'SPOT\',
                        \'InstanceType\': \'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\',
                        \'Description\': \'string\',
                        \'Name\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'TerminationTime\': datetime(2015, 1, 1),
                        \'Status\': \'NEW\'|\'DOWNLOADING\'|\'VALIDATING\'|\'BUILDING\'|\'ACTIVATING\'|\'ACTIVE\'|\'DELETING\'|\'ERROR\'|\'TERMINATED\',
                        \'BuildId\': \'string\',
                        \'ServerLaunchPath\': \'string\',
                        \'ServerLaunchParameters\': \'string\',
                        \'LogPaths\': [
                            \'string\',
                        ],
                        \'NewGameSessionProtectionPolicy\': \'NoProtection\'|\'FullProtection\',
                        \'OperatingSystem\': \'WINDOWS_2012\'|\'AMAZON_LINUX\',
                        \'ResourceCreationLimitPolicy\': {
                            \'NewGameSessionsPerCreator\': 123,
                            \'PolicyPeriodInMinutes\': 123
                        },
                        \'MetricGroups\': [
                            \'string\',
                        ],
                        \'StoppedActions\': [
                            \'AUTO_SCALING\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetAttributes** *(list) --* 
        
              Collection of objects containing attribute metadata for each requested fleet ID.
        
              - *(dict) --* 
        
                General properties describing a fleet.
        
                Fleet-related operations include:
        
                *  CreateFleet   
                 
                *  ListFleets   
                 
                *  DeleteFleet   
                 
                * Describe fleets: 
        
                  *  DescribeFleetAttributes   
                   
                  *  DescribeFleetCapacity   
                   
                  *  DescribeFleetPortSettings   
                   
                  *  DescribeFleetUtilization   
                   
                  *  DescribeRuntimeConfiguration   
                   
                  *  DescribeEC2InstanceLimits   
                   
                  *  DescribeFleetEvents   
                   
                * Update fleets: 
        
                  *  UpdateFleetAttributes   
                   
                  *  UpdateFleetCapacity   
                   
                  *  UpdateFleetPortSettings   
                   
                  *  UpdateRuntimeConfiguration   
                   
                * Manage fleet actions: 
        
                  *  StartFleetActions   
                   
                  *  StopFleetActions   
                   
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet.
        
                - **FleetArn** *(string) --* 
        
                  Identifier for a fleet that is unique across all regions.
        
                - **FleetType** *(string) --* 
        
                  Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may be interrupted with a two-minute notification.
        
                - **InstanceType** *(string) --* 
        
                  EC2 instance type indicating the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.
        
                - **Description** *(string) --* 
        
                  Human-readable description of the fleet.
        
                - **Name** *(string) --* 
        
                  Descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **TerminationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **Status** *(string) --* 
        
                  Current status of the fleet.
        
                  Possible fleet statuses include the following:
        
                  * **NEW** -- A new fleet has been defined and desired instances is set to 1.  
                   
                  * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new fleet, creating new instances with the game build and starting server processes. 
                   
                  * **ACTIVE** -- Hosts can now accept game sessions. 
                   
                  * **ERROR** -- An error occurred when downloading, validating, building, or activating the fleet. 
                   
                  * **DELETING** -- Hosts are responding to a delete fleet request. 
                   
                  * **TERMINATED** -- The fleet no longer exists. 
                   
                - **BuildId** *(string) --* 
        
                  Unique identifier for a build.
        
                - **ServerLaunchPath** *(string) --* 
        
                  Path to a game server executable in the fleet\'s build, specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after this date are specified in the fleet\'s  RuntimeConfiguration .
        
                - **ServerLaunchParameters** *(string) --* 
        
                  Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch parameters for fleets created after this date are specified in the fleet\'s  RuntimeConfiguration .
        
                - **LogPaths** *(list) --* 
        
                  Location of default log files. When a server process is shut down, Amazon GameLift captures and stores any log files in this location. These logs are in addition to game session logs; see more on game session logs in the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__ . If no default log path for a fleet is specified, Amazon GameLift automatically uploads logs that are stored on each instance at ``C:\game\logs`` (for Windows) or ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs. 
        
                  - *(string) --* 
              
                - **NewGameSessionProtectionPolicy** *(string) --* 
        
                  Type of game session protection to set for all new instances started in the fleet.
        
                  * **NoProtection** -- The game session can be terminated during a scale-down event. 
                   
                  * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be terminated during a scale-down event. 
                   
                - **OperatingSystem** *(string) --* 
        
                  Operating system of the fleet\'s computing resources. A fleet\'s operating system depends on the OS specified for the build that is deployed on this fleet.
        
                - **ResourceCreationLimitPolicy** *(dict) --* 
        
                  Fleet policy to limit the number of game sessions an individual player can create over a span of time.
        
                  - **NewGameSessionsPerCreator** *(integer) --* 
        
                    Maximum number of game sessions that an individual can create during the policy period. 
        
                  - **PolicyPeriodInMinutes** *(integer) --* 
        
                    Time span used in evaluating the resource creation limit policy. 
        
                - **MetricGroups** *(list) --* 
        
                  Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view metrics for an individual fleet or aggregated metrics for fleets that are in a fleet metric group. A fleet can be included in only one metric group at a time.
        
                  - *(string) --* 
              
                - **StoppedActions** *(list) --* 
        
                  List of fleet actions that have been suspended using  StopFleetActions . This includes auto-scaling.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_fleet_capacity(self, FleetIds: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          Some API actions may limit the number of fleet IDs allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetCapacity>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_fleet_capacity(
              FleetIds=[
                  \'string\',
              ],
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetIds: list
        :param FleetIds: 
        
          Unique identifier for a fleet(s) to retrieve capacity information for. To request capacity information for all fleets, leave this parameter empty.
        
          - *(string) --* 
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetCapacity\': [
                    {
                        \'FleetId\': \'string\',
                        \'InstanceType\': \'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\',
                        \'InstanceCounts\': {
                            \'DESIRED\': 123,
                            \'MINIMUM\': 123,
                            \'MAXIMUM\': 123,
                            \'PENDING\': 123,
                            \'ACTIVE\': 123,
                            \'IDLE\': 123,
                            \'TERMINATING\': 123
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetCapacity** *(list) --* 
        
              Collection of objects containing capacity information for each requested fleet ID. Leave this parameter empty to retrieve capacity information for all fleets.
        
              - *(dict) --* 
        
                Information about the fleet\'s capacity. Fleet capacity is measured in EC2 instances. By default, new fleets have a capacity of one instance, but can be updated as needed. The maximum number of instances for a fleet is determined by the fleet\'s instance type.
        
                Fleet-related operations include:
        
                *  CreateFleet   
                 
                *  ListFleets   
                 
                *  DeleteFleet   
                 
                * Describe fleets: 
        
                  *  DescribeFleetAttributes   
                   
                  *  DescribeFleetCapacity   
                   
                  *  DescribeFleetPortSettings   
                   
                  *  DescribeFleetUtilization   
                   
                  *  DescribeRuntimeConfiguration   
                   
                  *  DescribeEC2InstanceLimits   
                   
                  *  DescribeFleetEvents   
                   
                * Update fleets: 
        
                  *  UpdateFleetAttributes   
                   
                  *  UpdateFleetCapacity   
                   
                  *  UpdateFleetPortSettings   
                   
                  *  UpdateRuntimeConfiguration   
                   
                * Manage fleet actions: 
        
                  *  StartFleetActions   
                   
                  *  StopFleetActions   
                   
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet.
        
                - **InstanceType** *(string) --* 
        
                  Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.
        
                - **InstanceCounts** *(dict) --* 
        
                  Current status of fleet capacity.
        
                  - **DESIRED** *(integer) --* 
        
                    Ideal number of active instances in the fleet.
        
                  - **MINIMUM** *(integer) --* 
        
                    Minimum value allowed for the fleet\'s instance count.
        
                  - **MAXIMUM** *(integer) --* 
        
                    Maximum value allowed for the fleet\'s instance count.
        
                  - **PENDING** *(integer) --* 
        
                    Number of instances in the fleet that are starting but not yet active.
        
                  - **ACTIVE** *(integer) --* 
        
                    Actual number of active instances in the fleet.
        
                  - **IDLE** *(integer) --* 
        
                    Number of active instances in the fleet that are not currently hosting a game session.
        
                  - **TERMINATING** *(integer) --* 
        
                    Number of instances in the fleet that are no longer active but haven\'t yet been terminated.
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_fleet_events(self, FleetId: str, StartTime: datetime = None, EndTime: datetime = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_fleet_events(
              FleetId=\'string\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to get event logs for.
        
        :type StartTime: datetime
        :param StartTime: 
        
          Earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: \"1469498468.057\").
        
        :type EndTime: datetime
        :param EndTime: 
        
          Most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: \"1469498468.057\").
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Events\': [
                    {
                        \'EventId\': \'string\',
                        \'ResourceId\': \'string\',
                        \'EventCode\': \'GENERIC_EVENT\'|\'FLEET_CREATED\'|\'FLEET_DELETED\'|\'FLEET_SCALING_EVENT\'|\'FLEET_STATE_DOWNLOADING\'|\'FLEET_STATE_VALIDATING\'|\'FLEET_STATE_BUILDING\'|\'FLEET_STATE_ACTIVATING\'|\'FLEET_STATE_ACTIVE\'|\'FLEET_STATE_ERROR\'|\'FLEET_INITIALIZATION_FAILED\'|\'FLEET_BINARY_DOWNLOAD_FAILED\'|\'FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND\'|\'FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE\'|\'FLEET_VALIDATION_TIMED_OUT\'|\'FLEET_ACTIVATION_FAILED\'|\'FLEET_ACTIVATION_FAILED_NO_INSTANCES\'|\'FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED\'|\'SERVER_PROCESS_INVALID_PATH\'|\'SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT\'|\'SERVER_PROCESS_PROCESS_READY_TIMEOUT\'|\'SERVER_PROCESS_CRASHED\'|\'SERVER_PROCESS_TERMINATED_UNHEALTHY\'|\'SERVER_PROCESS_FORCE_TERMINATED\'|\'SERVER_PROCESS_PROCESS_EXIT_TIMEOUT\'|\'GAME_SESSION_ACTIVATION_TIMEOUT\'|\'FLEET_CREATION_EXTRACTING_BUILD\'|\'FLEET_CREATION_RUNNING_INSTALLER\'|\'FLEET_CREATION_VALIDATING_RUNTIME_CONFIG\'|\'FLEET_VPC_PEERING_SUCCEEDED\'|\'FLEET_VPC_PEERING_FAILED\'|\'FLEET_VPC_PEERING_DELETED\'|\'INSTANCE_INTERRUPTED\',
                        \'Message\': \'string\',
                        \'EventTime\': datetime(2015, 1, 1),
                        \'PreSignedLogUrl\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Events** *(list) --* 
        
              Collection of objects containing event log entries for the specified fleet.
        
              - *(dict) --* 
        
                Log entry describing an event that involves Amazon GameLift resources (such as a fleet). In addition to tracking activity, event codes and messages can provide additional information for troubleshooting and debugging problems.
        
                - **EventId** *(string) --* 
        
                  Unique identifier for a fleet event.
        
                - **ResourceId** *(string) --* 
        
                  Unique identifier for an event resource, such as a fleet ID.
        
                - **EventCode** *(string) --* 
        
                  Type of event being logged. The following events are currently in use:
        
                   **Fleet creation events:**  
        
                  * FLEET_CREATED -- A fleet record was successfully created with a status of ``NEW`` . Event messaging includes the fleet ID. 
                   
                  * FLEET_STATE_DOWNLOADING -- Fleet status changed from ``NEW`` to ``DOWNLOADING`` . The compressed build has started downloading to a fleet instance for installation. 
                   
                  * FLEET_BINARY_DOWNLOAD_FAILED -- The build failed to download to the fleet instance. 
                   
                  * FLEET_CREATION_EXTRACTING_BUILD – The game server build was successfully downloaded to an instance, and the build files are now being extracted from the uploaded build and saved to an instance. Failure at this stage prevents a fleet from moving to ``ACTIVE`` status. Logs for this stage display a list of the files that are extracted and saved on the instance. Access the logs by using the URL in *PreSignedLogUrl* . 
                   
                  * FLEET_CREATION_RUNNING_INSTALLER – The game server build files were successfully extracted, and the Amazon GameLift is now running the build\'s install script (if one is included). Failure in this stage prevents a fleet from moving to ``ACTIVE`` status. Logs for this stage list the installation steps and whether or not the install completed successfully. Access the logs by using the URL in *PreSignedLogUrl* .  
                   
                  * FLEET_CREATION_VALIDATING_RUNTIME_CONFIG -- The build process was successful, and the Amazon GameLift is now verifying that the game server launch paths, which are specified in the fleet\'s run-time configuration, exist. If any listed launch path exists, Amazon GameLift tries to launch a game server process and waits for the process to report ready. Failures in this stage prevent a fleet from moving to ``ACTIVE`` status. Logs for this stage list the launch paths in the run-time configuration and indicate whether each is found. Access the logs by using the URL in *PreSignedLogUrl* .  
                   
                  * FLEET_STATE_VALIDATING -- Fleet status changed from ``DOWNLOADING`` to ``VALIDATING`` . 
                   
                  * FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND -- Validation of the run-time configuration failed because the executable specified in a launch path does not exist on the instance. 
                   
                  * FLEET_STATE_BUILDING -- Fleet status changed from ``VALIDATING`` to ``BUILDING`` . 
                   
                  * FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE -- Validation of the run-time configuration failed because the executable specified in a launch path failed to run on the fleet instance. 
                   
                  * FLEET_STATE_ACTIVATING -- Fleet status changed from ``BUILDING`` to ``ACTIVATING`` .  
                   
                  * FLEET_ACTIVATION_FAILED - The fleet failed to successfully complete one of the steps in the fleet activation process. This event code indicates that the game build was successfully downloaded to a fleet instance, built, and validated, but was not able to start a server process. A possible reason for failure is that the game server is not reporting \"process ready\" to the Amazon GameLift service. 
                   
                  * FLEET_STATE_ACTIVE -- The fleet\'s status changed from ``ACTIVATING`` to ``ACTIVE`` . The fleet is now ready to host game sessions. 
                   
                   **VPC peering events:**  
        
                  * FLEET_VPC_PEERING_SUCCEEDED -- A VPC peering connection has been established between the VPC for an Amazon GameLift fleet and a VPC in your AWS account. 
                   
                  * FLEET_VPC_PEERING_FAILED -- A requested VPC peering connection has failed. Event details and status information (see  DescribeVpcPeeringConnections ) provide additional detail. A common reason for peering failure is that the two VPCs have overlapping CIDR blocks of IPv4 addresses. To resolve this, change the CIDR block for the VPC in your AWS account. For more information on VPC peering failures, see `http\://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html <http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html>`__   
                   
                  * FLEET_VPC_PEERING_DELETED -- A VPC peering connection has been successfully deleted. 
                   
                   **Spot instance events:**  
        
                  * INSTANCE_INTERRUPTED -- A spot instance was interrupted by EC2 with a two-minute notification. 
                   
                   **Other fleet events:**  
        
                  * FLEET_SCALING_EVENT -- A change was made to the fleet\'s capacity settings (desired instances, minimum/maximum scaling limits). Event messaging includes the new capacity settings. 
                   
                  * FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED -- A change was made to the fleet\'s game session protection policy setting. Event messaging includes both the old and new policy setting.  
                   
                  * FLEET_DELETED -- A request to delete a fleet was initiated. 
                   
                  * GENERIC_EVENT -- An unspecified event has occurred. 
                   
                - **Message** *(string) --* 
        
                  Additional information related to the event.
        
                - **EventTime** *(datetime) --* 
        
                  Time stamp indicating when this event occurred. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **PreSignedLogUrl** *(string) --* 
        
                  Location of stored logs with additional detail that is related to the event. This is useful for debugging issues. The URL is valid for 15 minutes. You can also access fleet creation logs through the Amazon GameLift console.
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_fleet_port_settings(self, FleetId: str) -> Dict:
        """
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetPortSettings>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_fleet_port_settings(
              FleetId=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to retrieve port settings for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InboundPermissions\': [
                    {
                        \'FromPort\': 123,
                        \'ToPort\': 123,
                        \'IpRange\': \'string\',
                        \'Protocol\': \'TCP\'|\'UDP\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **InboundPermissions** *(list) --* 
        
              Object that contains port settings for the requested fleet ID.
        
              - *(dict) --* 
        
                A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet\'s allowed ranges. This combination is included in the  GameSession object. 
        
                - **FromPort** *(integer) --* 
        
                  Starting value for a range of allowed port numbers.
        
                - **ToPort** *(integer) --* 
        
                  Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than ``FromPort`` .
        
                - **IpRange** *(string) --* 
        
                  Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: \"``000.000.000.000/[subnet mask]`` \" or optionally the shortened version \"``0.0.0.0/[subnet mask]`` \".
        
                - **Protocol** *(string) --* 
        
                  Network communication protocol used by the fleet.
        
        """
        pass

    def describe_fleet_utilization(self, FleetIds: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          Some API actions may limit the number of fleet IDs allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetUtilization>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_fleet_utilization(
              FleetIds=[
                  \'string\',
              ],
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetIds: list
        :param FleetIds: 
        
          Unique identifier for a fleet(s) to retrieve utilization data for. To request utilization data for all fleets, leave this parameter empty.
        
          - *(string) --* 
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetUtilization\': [
                    {
                        \'FleetId\': \'string\',
                        \'ActiveServerProcessCount\': 123,
                        \'ActiveGameSessionCount\': 123,
                        \'CurrentPlayerSessionCount\': 123,
                        \'MaximumPlayerSessionCount\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetUtilization** *(list) --* 
        
              Collection of objects containing utilization information for each requested fleet ID.
        
              - *(dict) --* 
        
                Current status of fleet utilization, including the number of game and player sessions being hosted.
        
                Fleet-related operations include:
        
                *  CreateFleet   
                 
                *  ListFleets   
                 
                *  DeleteFleet   
                 
                * Describe fleets: 
        
                  *  DescribeFleetAttributes   
                   
                  *  DescribeFleetCapacity   
                   
                  *  DescribeFleetPortSettings   
                   
                  *  DescribeFleetUtilization   
                   
                  *  DescribeRuntimeConfiguration   
                   
                  *  DescribeEC2InstanceLimits   
                   
                  *  DescribeFleetEvents   
                   
                * Update fleets: 
        
                  *  UpdateFleetAttributes   
                   
                  *  UpdateFleetCapacity   
                   
                  *  UpdateFleetPortSettings   
                   
                  *  UpdateRuntimeConfiguration   
                   
                * Manage fleet actions: 
        
                  *  StartFleetActions   
                   
                  *  StopFleetActions   
                   
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet.
        
                - **ActiveServerProcessCount** *(integer) --* 
        
                  Number of server processes in an ``ACTIVE`` status currently running across all instances in the fleet
        
                - **ActiveGameSessionCount** *(integer) --* 
        
                  Number of active game sessions currently being hosted on all instances in the fleet.
        
                - **CurrentPlayerSessionCount** *(integer) --* 
        
                  Number of active player sessions currently being hosted on all instances in the fleet.
        
                - **MaximumPlayerSessionCount** *(integer) --* 
        
                  Maximum players allowed across all game sessions currently being hosted on all instances in the fleet.
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_game_session_details(self, FleetId: str = None, GameSessionId: str = None, AliasId: str = None, StatusFilter: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        To get game session record(s), specify just one of the following: game session ID, fleet ID, or alias ID. You can filter this request by game session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSessionDetail object is returned for each session matching the request.
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeGameSessionDetails>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_game_session_details(
              FleetId=\'string\',
              GameSessionId=\'string\',
              AliasId=\'string\',
              StatusFilter=\'string\',
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetId: string
        :param FleetId: 
        
          Unique identifier for a fleet to retrieve all game sessions active on the fleet.
        
        :type GameSessionId: string
        :param GameSessionId: 
        
          Unique identifier for the game session to retrieve.
        
        :type AliasId: string
        :param AliasId: 
        
          Unique identifier for an alias associated with the fleet to retrieve all game sessions for.
        
        :type StatusFilter: string
        :param StatusFilter: 
        
          Game session status to filter results on. Possible game session statuses include ``ACTIVE`` , ``TERMINATED`` , ``ACTIVATING`` and ``TERMINATING`` (the last two are transitory). 
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessionDetails\': [
                    {
                        \'GameSession\': {
                            \'GameSessionId\': \'string\',
                            \'Name\': \'string\',
                            \'FleetId\': \'string\',
                            \'CreationTime\': datetime(2015, 1, 1),
                            \'TerminationTime\': datetime(2015, 1, 1),
                            \'CurrentPlayerSessionCount\': 123,
                            \'MaximumPlayerSessionCount\': 123,
                            \'Status\': \'ACTIVE\'|\'ACTIVATING\'|\'TERMINATED\'|\'TERMINATING\'|\'ERROR\',
                            \'StatusReason\': \'INTERRUPTED\',
                            \'GameProperties\': [
                                {
                                    \'Key\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ],
                            \'IpAddress\': \'string\',
                            \'Port\': 123,
                            \'PlayerSessionCreationPolicy\': \'ACCEPT_ALL\'|\'DENY_ALL\',
                            \'CreatorId\': \'string\',
                            \'GameSessionData\': \'string\',
                            \'MatchmakerData\': \'string\'
                        },
                        \'ProtectionPolicy\': \'NoProtection\'|\'FullProtection\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessionDetails** *(list) --* 
        
              Collection of objects containing game session properties and the protection policy currently in force for each session matching the request.
        
              - *(dict) --* 
        
                A game session\'s properties plus the protection policy currently in force.
        
                - **GameSession** *(dict) --* 
        
                  Object that describes a game session.
        
                  - **GameSessionId** *(string) --* 
        
                    Unique identifier for the game session. A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .
        
                  - **Name** *(string) --* 
        
                    Descriptive label that is associated with a game session. Session names do not need to be unique.
        
                  - **FleetId** *(string) --* 
        
                    Unique identifier for a fleet that the game session is running on.
        
                  - **CreationTime** *(datetime) --* 
        
                    Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                  - **TerminationTime** *(datetime) --* 
        
                    Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                  - **CurrentPlayerSessionCount** *(integer) --* 
        
                    Number of players currently in the game session.
        
                  - **MaximumPlayerSessionCount** *(integer) --* 
        
                    Maximum number of players that can be connected simultaneously to the game session.
        
                  - **Status** *(string) --* 
        
                    Current status of the game session. A game session must have an ``ACTIVE`` status to have player sessions.
        
                  - **StatusReason** *(string) --* 
        
                    Provides additional information about game session status. ``INTERRUPTED`` indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.
        
                  - **GameProperties** *(list) --* 
        
                    Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). You can search for active game sessions based on this custom data with  SearchGameSessions .
        
                    - *(dict) --* 
        
                      Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                      - **Key** *(string) --* 
        
                        Game property identifier.
        
                      - **Value** *(string) --* 
        
                        Game property value.
        
                  - **IpAddress** *(string) --* 
        
                    IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                  - **Port** *(integer) --* 
        
                    Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                  - **PlayerSessionCreationPolicy** *(string) --* 
        
                    Indicates whether or not the game session is accepting new players.
        
                  - **CreatorId** *(string) --* 
        
                    Unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
        
                  - **GameSessionData** *(string) --* 
        
                    Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
                  - **MatchmakerData** *(string) --* 
        
                    Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ). 
        
                - **ProtectionPolicy** *(string) --* 
        
                  Current status of protection for the game session.
        
                  * **NoProtection** -- The game session can be terminated during a scale-down event. 
                   
                  * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be terminated during a scale-down event. 
                   
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_game_session_placement(self, PlacementId: str) -> Dict:
        """
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeGameSessionPlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_game_session_placement(
              PlacementId=\'string\'
          )
        :type PlacementId: string
        :param PlacementId: **[REQUIRED]** 
        
          Unique identifier for a game session placement to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessionPlacement\': {
                    \'PlacementId\': \'string\',
                    \'GameSessionQueueName\': \'string\',
                    \'Status\': \'PENDING\'|\'FULFILLED\'|\'CANCELLED\'|\'TIMED_OUT\',
                    \'GameProperties\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'MaximumPlayerSessionCount\': 123,
                    \'GameSessionName\': \'string\',
                    \'GameSessionId\': \'string\',
                    \'GameSessionArn\': \'string\',
                    \'GameSessionRegion\': \'string\',
                    \'PlayerLatencies\': [
                        {
                            \'PlayerId\': \'string\',
                            \'RegionIdentifier\': \'string\',
                            \'LatencyInMilliseconds\': ...
                        },
                    ],
                    \'StartTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'IpAddress\': \'string\',
                    \'Port\': 123,
                    \'PlacedPlayerSessions\': [
                        {
                            \'PlayerId\': \'string\',
                            \'PlayerSessionId\': \'string\'
                        },
                    ],
                    \'GameSessionData\': \'string\',
                    \'MatchmakerData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessionPlacement** *(dict) --* 
        
              Object that describes the requested game session placement.
        
              - **PlacementId** *(string) --* 
        
                Unique identifier for a game session placement.
        
              - **GameSessionQueueName** *(string) --* 
        
                Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
              - **Status** *(string) --* 
        
                Current status of the game session placement request.
        
                * **PENDING** -- The placement request is currently in the queue waiting to be processed. 
                 
                * **FULFILLED** -- A new game session and player sessions (if requested) have been successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.  
                 
                * **CANCELLED** -- The placement request was canceled with a call to  StopGameSessionPlacement . 
                 
                * **TIMED_OUT** -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed. 
                 
              - **GameProperties** *(list) --* 
        
                Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
                - *(dict) --* 
        
                  Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                  - **Key** *(string) --* 
        
                    Game property identifier.
        
                  - **Value** *(string) --* 
        
                    Game property value.
        
              - **MaximumPlayerSessionCount** *(integer) --* 
        
                Maximum number of players that can be connected simultaneously to the game session.
        
              - **GameSessionName** *(string) --* 
        
                Descriptive label that is associated with a game session. Session names do not need to be unique.
        
              - **GameSessionId** *(string) --* 
        
                Unique identifier for the game session. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **GameSessionArn** *(string) --* 
        
                Identifier for the game session created by this placement request. This value is set once the new game session is placed (placement status is ``FULFILLED`` ). This identifier is unique across all regions. You can use this value as a ``GameSessionId`` value as needed.
        
              - **GameSessionRegion** *(string) --* 
        
                Name of the region where the game session created by this placement request is running. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **PlayerLatencies** *(list) --* 
        
                Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions.
        
                - *(dict) --* 
        
                  Regional latency information for a player, used when requesting a new game session with  StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified region. The relative difference between a player\'s latency values for multiple regions are used to determine which fleets are best suited to place a new game session for the player. 
        
                  - **PlayerId** *(string) --* 
        
                    Unique identifier for a player associated with the latency data.
        
                  - **RegionIdentifier** *(string) --* 
        
                    Name of the region that is associated with the latency value.
        
                  - **LatencyInMilliseconds** *(float) --* 
        
                    Amount of time that represents the time lag experienced by the player when connected to the specified region.
        
              - **StartTime** *(datetime) --* 
        
                Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **EndTime** *(datetime) --* 
        
                Time stamp indicating when this request was completed, canceled, or timed out.
        
              - **IpAddress** *(string) --* 
        
                IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is ``FULFILLED`` ). 
        
              - **Port** *(integer) --* 
        
                Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **PlacedPlayerSessions** *(list) --* 
        
                Collection of information on player sessions created in response to the game session placement request. These player sessions are created only once a new game session is successfully placed (placement status is ``FULFILLED`` ). This information includes the player ID (as provided in the placement request) and the corresponding player session ID. Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.
        
                - *(dict) --* 
        
                  Information about a player session that was created as part of a  StartGameSessionPlacement request. This object contains only the player ID and player session ID. To retrieve full details on a player session, call  DescribePlayerSessions with the player session ID.
        
                  Player-session-related operations include:
        
                  *  CreatePlayerSession   
                   
                  *  CreatePlayerSessions   
                   
                  *  DescribePlayerSessions   
                   
                  * Game session placements 
        
                    *  StartGameSessionPlacement   
                     
                    *  DescribeGameSessionPlacement   
                     
                    *  StopGameSessionPlacement   
                     
                  - **PlayerId** *(string) --* 
        
                    Unique identifier for a player that is associated with this player session.
        
                  - **PlayerSessionId** *(string) --* 
        
                    Unique identifier for a player session.
        
              - **GameSessionData** *(string) --* 
        
                Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
              - **MatchmakerData** *(string) --* 
        
                Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ .
        
        """
        pass

    def describe_game_session_queues(self, Names: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        Queue-related operations include:
        
        *  CreateGameSessionQueue   
         
        *  DescribeGameSessionQueues   
         
        *  UpdateGameSessionQueue   
         
        *  DeleteGameSessionQueue   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeGameSessionQueues>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_game_session_queues(
              Names=[
                  \'string\',
              ],
              Limit=123,
              NextToken=\'string\'
          )
        :type Names: list
        :param Names: 
        
          List of queue names to retrieve information for. To request settings for all queues, leave this parameter empty.
        
          - *(string) --* 
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessionQueues\': [
                    {
                        \'Name\': \'string\',
                        \'GameSessionQueueArn\': \'string\',
                        \'TimeoutInSeconds\': 123,
                        \'PlayerLatencyPolicies\': [
                            {
                                \'MaximumIndividualPlayerLatencyMilliseconds\': 123,
                                \'PolicyDurationSeconds\': 123
                            },
                        ],
                        \'Destinations\': [
                            {
                                \'DestinationArn\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessionQueues** *(list) --* 
        
              Collection of objects that describes the requested game session queues.
        
              - *(dict) --* 
        
                Configuration of a queue that is used to process game session placement requests. The queue configuration identifies several game features:
        
                * The destinations where a new game session can potentially be hosted. Amazon GameLift tries these destinations in an order based on either the queue\'s default order or player latency information, if provided in a placement request. With latency information, Amazon GameLift can place game sessions where the majority of players are reporting the lowest possible latency.  
                 
                * The length of time that placement requests can wait in the queue before timing out.  
                 
                * A set of optional latency policies that protect individual players from high latencies, preventing game sessions from being placed where any individual player is reporting latency higher than a policy\'s maximum. 
                 
                Queue-related operations include:
        
                *  CreateGameSessionQueue   
                 
                *  DescribeGameSessionQueues   
                 
                *  UpdateGameSessionQueue   
                 
                *  DeleteGameSessionQueue   
                 
                - **Name** *(string) --* 
        
                  Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
                - **GameSessionQueueArn** *(string) --* 
        
                  Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` .
        
                - **TimeoutInSeconds** *(integer) --* 
        
                  Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status.
        
                - **PlayerLatencyPolicies** *(list) --* 
        
                  Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. 
        
                  - *(dict) --* 
        
                    Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
        
                    Queue-related operations include:
        
                    *  CreateGameSessionQueue   
                     
                    *  DescribeGameSessionQueues   
                     
                    *  UpdateGameSessionQueue   
                     
                    *  DeleteGameSessionQueue   
                     
                    - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --* 
        
                      The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
        
                    - **PolicyDurationSeconds** *(integer) --* 
        
                      The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
        
                - **Destinations** *(list) --* 
        
                  List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
        
                  - *(dict) --* 
        
                    Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue. 
        
                    Queue-related operations include:
        
                    *  CreateGameSessionQueue   
                     
                    *  DescribeGameSessionQueues   
                     
                    *  UpdateGameSessionQueue   
                     
                    *  DeleteGameSessionQueue   
                     
                    - **DestinationArn** *(string) --* 
        
                      Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions. 
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_game_sessions(self, FleetId: str = None, GameSessionId: str = None, AliasId: str = None, StatusFilter: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        To get game sessions, specify one of the following: game session ID, fleet ID, or alias ID. You can filter this request by game session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSession object is returned for each game session matching the request.
        
         *Available in Amazon GameLift Local.*  
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeGameSessions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_game_sessions(
              FleetId=\'string\',
              GameSessionId=\'string\',
              AliasId=\'string\',
              StatusFilter=\'string\',
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetId: string
        :param FleetId: 
        
          Unique identifier for a fleet to retrieve all game sessions for.
        
        :type GameSessionId: string
        :param GameSessionId: 
        
          Unique identifier for the game session to retrieve. You can use either a ``GameSessionId`` or ``GameSessionArn`` value. 
        
        :type AliasId: string
        :param AliasId: 
        
          Unique identifier for an alias associated with the fleet to retrieve all game sessions for. 
        
        :type StatusFilter: string
        :param StatusFilter: 
        
          Game session status to filter results on. Possible game session statuses include ``ACTIVE`` , ``TERMINATED`` , ``ACTIVATING`` , and ``TERMINATING`` (the last two are transitory). 
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessions\': [
                    {
                        \'GameSessionId\': \'string\',
                        \'Name\': \'string\',
                        \'FleetId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'TerminationTime\': datetime(2015, 1, 1),
                        \'CurrentPlayerSessionCount\': 123,
                        \'MaximumPlayerSessionCount\': 123,
                        \'Status\': \'ACTIVE\'|\'ACTIVATING\'|\'TERMINATED\'|\'TERMINATING\'|\'ERROR\',
                        \'StatusReason\': \'INTERRUPTED\',
                        \'GameProperties\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'IpAddress\': \'string\',
                        \'Port\': 123,
                        \'PlayerSessionCreationPolicy\': \'ACCEPT_ALL\'|\'DENY_ALL\',
                        \'CreatorId\': \'string\',
                        \'GameSessionData\': \'string\',
                        \'MatchmakerData\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessions** *(list) --* 
        
              Collection of objects containing game session properties for each session matching the request.
        
              - *(dict) --* 
        
                Properties describing a game session.
        
                A game session in ACTIVE status can host players. When a game session ends, its status is set to ``TERMINATED`` . 
        
                Once the session ends, the game session object is retained for 30 days. This means you can reuse idempotency token values after this time. Game session logs are retained for 14 days.
        
                Game-session-related operations include:
        
                *  CreateGameSession   
                 
                *  DescribeGameSessions   
                 
                *  DescribeGameSessionDetails   
                 
                *  SearchGameSessions   
                 
                *  UpdateGameSession   
                 
                *  GetGameSessionLogUrl   
                 
                * Game session placements 
        
                  *  StartGameSessionPlacement   
                   
                  *  DescribeGameSessionPlacement   
                   
                  *  StopGameSessionPlacement   
                   
                - **GameSessionId** *(string) --* 
        
                  Unique identifier for the game session. A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .
        
                - **Name** *(string) --* 
        
                  Descriptive label that is associated with a game session. Session names do not need to be unique.
        
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that the game session is running on.
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **TerminationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **CurrentPlayerSessionCount** *(integer) --* 
        
                  Number of players currently in the game session.
        
                - **MaximumPlayerSessionCount** *(integer) --* 
        
                  Maximum number of players that can be connected simultaneously to the game session.
        
                - **Status** *(string) --* 
        
                  Current status of the game session. A game session must have an ``ACTIVE`` status to have player sessions.
        
                - **StatusReason** *(string) --* 
        
                  Provides additional information about game session status. ``INTERRUPTED`` indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.
        
                - **GameProperties** *(list) --* 
        
                  Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). You can search for active game sessions based on this custom data with  SearchGameSessions .
        
                  - *(dict) --* 
        
                    Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                    - **Key** *(string) --* 
        
                      Game property identifier.
        
                    - **Value** *(string) --* 
        
                      Game property value.
        
                - **IpAddress** *(string) --* 
        
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **Port** *(integer) --* 
        
                  Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **PlayerSessionCreationPolicy** *(string) --* 
        
                  Indicates whether or not the game session is accepting new players.
        
                - **CreatorId** *(string) --* 
        
                  Unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
        
                - **GameSessionData** *(string) --* 
        
                  Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
                - **MatchmakerData** *(string) --* 
        
                  Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ). 
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_instances(self, FleetId: str, InstanceId: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        To get a specific instance, specify fleet ID and instance ID. To get all instances in a fleet, specify a fleet ID only. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, an  Instance object is returned for each result.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_instances(
              FleetId=\'string\',
              InstanceId=\'string\',
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to retrieve instance information for.
        
        :type InstanceId: string
        :param InstanceId: 
        
          Unique identifier for an instance to retrieve. Specify an instance ID or leave blank to retrieve all instances in the fleet.
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Instances\': [
                    {
                        \'FleetId\': \'string\',
                        \'InstanceId\': \'string\',
                        \'IpAddress\': \'string\',
                        \'OperatingSystem\': \'WINDOWS_2012\'|\'AMAZON_LINUX\',
                        \'Type\': \'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\',
                        \'Status\': \'PENDING\'|\'ACTIVE\'|\'TERMINATING\',
                        \'CreationTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Instances** *(list) --* 
        
              Collection of objects containing properties for each instance returned.
        
              - *(dict) --* 
        
                Properties that describe an instance of a virtual computing resource that hosts one or more game servers. A fleet may contain zero or more instances.
        
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that the instance is in.
        
                - **InstanceId** *(string) --* 
        
                  Unique identifier for an instance.
        
                - **IpAddress** *(string) --* 
        
                  IP address assigned to the instance.
        
                - **OperatingSystem** *(string) --* 
        
                  Operating system that is running on this instance. 
        
                - **Type** *(string) --* 
        
                  EC2 instance type that defines the computing resources of this instance. 
        
                - **Status** *(string) --* 
        
                  Current status of the instance. Possible statuses include the following:
        
                  * **PENDING** -- The instance is in the process of being created and launching server processes as defined in the fleet\'s run-time configuration.  
                   
                  * **ACTIVE** -- The instance has been successfully created and at least one server process has successfully launched and reported back to Amazon GameLift that it is ready to host a game session. The instance is now considered ready to host game sessions.  
                   
                  * **TERMINATING** -- The instance is in the process of shutting down. This may happen to reduce capacity during a scaling down event or to recycle resources in the event of a problem. 
                   
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_matchmaking(self, TicketIds: List) -> Dict:
        """
        
        You can use this operation to track the progress of matchmaking requests (through polling) as an alternative to using event notifications. See more details on tracking matchmaking requests through polling or notifications in  StartMatchmaking . 
        
        To request matchmaking tickets, provide a list of up to 10 ticket IDs. If the request is successful, a ticket object is returned for each requested ID that currently exists.
        
        Matchmaking-related operations include:
        
        *  StartMatchmaking   
         
        *  DescribeMatchmaking   
         
        *  StopMatchmaking   
         
        *  AcceptMatch   
         
        *  StartMatchBackfill   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeMatchmaking>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_matchmaking(
              TicketIds=[
                  \'string\',
              ]
          )
        :type TicketIds: list
        :param TicketIds: **[REQUIRED]** 
        
          Unique identifier for a matchmaking ticket. You can include up to 10 ID values. 
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TicketList\': [
                    {
                        \'TicketId\': \'string\',
                        \'ConfigurationName\': \'string\',
                        \'Status\': \'CANCELLED\'|\'COMPLETED\'|\'FAILED\'|\'PLACING\'|\'QUEUED\'|\'REQUIRES_ACCEPTANCE\'|\'SEARCHING\'|\'TIMED_OUT\',
                        \'StatusReason\': \'string\',
                        \'StatusMessage\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'Players\': [
                            {
                                \'PlayerId\': \'string\',
                                \'PlayerAttributes\': {
                                    \'string\': {
                                        \'S\': \'string\',
                                        \'N\': 123.0,
                                        \'SL\': [
                                            \'string\',
                                        ],
                                        \'SDM\': {
                                            \'string\': 123.0
                                        }
                                    }
                                },
                                \'Team\': \'string\',
                                \'LatencyInMs\': {
                                    \'string\': 123
                                }
                            },
                        ],
                        \'GameSessionConnectionInfo\': {
                            \'GameSessionArn\': \'string\',
                            \'IpAddress\': \'string\',
                            \'Port\': 123,
                            \'MatchedPlayerSessions\': [
                                {
                                    \'PlayerId\': \'string\',
                                    \'PlayerSessionId\': \'string\'
                                },
                            ]
                        },
                        \'EstimatedWaitTime\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **TicketList** *(list) --* 
        
              Collection of existing matchmaking ticket objects matching the request.
        
              - *(dict) --* 
        
                Ticket generated to track the progress of a matchmaking request. Each ticket is uniquely identified by a ticket ID, supplied by the requester, when creating a matchmaking request with  StartMatchmaking . Tickets can be retrieved by calling  DescribeMatchmaking with the ticket ID.
        
                - **TicketId** *(string) --* 
        
                  Unique identifier for a matchmaking ticket.
        
                - **ConfigurationName** *(string) --* 
        
                  Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.
        
                - **Status** *(string) --* 
        
                  Current status of the matchmaking request.
        
                  * **QUEUED** -- The matchmaking request has been received and is currently waiting to be processed. 
                   
                  * **SEARCHING** -- The matchmaking request is currently being processed.  
                   
                  * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the match (see  AcceptMatch ). This status is used only with requests that use a matchmaking configuration with a player acceptance requirement. 
                   
                  * **PLACING** -- The FlexMatch engine has matched players and is in the process of placing a new game session for the match. 
                   
                  * **COMPLETED** -- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players. 
                   
                  * **FAILED** -- The matchmaking request was not completed. Tickets with players who fail to accept a proposed match are placed in ``FAILED`` status. 
                   
                  * **CANCELLED** -- The matchmaking request was canceled with a call to  StopMatchmaking . 
                   
                  * **TIMED_OUT** -- The matchmaking request was not successful within the duration specified in the matchmaking configuration.  
                   
                  .. note::
        
                    Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket IDs.
        
                - **StatusReason** *(string) --* 
        
                  Code to explain the current status. For example, a status reason may indicate when a ticket has returned to ``SEARCHING`` status after a proposed match fails to receive player acceptances.
        
                - **StatusMessage** *(string) --* 
        
                  Additional information about the current status.
        
                - **StartTime** *(datetime) --* 
        
                  Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **EndTime** *(datetime) --* 
        
                  Time stamp indicating when this matchmaking request stopped being processed due to success, failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **Players** *(list) --* 
        
                  A set of ``Player`` objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the players were assigned to in the resulting match.
        
                  - *(dict) --* 
        
                    Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
        
                    - **PlayerId** *(string) --* 
        
                      Unique identifier for a player
        
                    - **PlayerAttributes** *(dict) --* 
        
                      Collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example: ``\"PlayerAttributes\": {\"skill\": {\"N\": \"23\"}, \"gameMode\": {\"S\": \"deathmatch\"}}`` .
        
                      - *(string) --* 
                        
                        - *(dict) --* 
        
                          Values for use in  Player attribute key:value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array or data map. Each ``AttributeValue`` object can use only one of the available properties.
        
                          - **S** *(string) --* 
        
                            For single string values. Maximum string length is 100 characters.
        
                          - **N** *(float) --* 
        
                            For number values, expressed as double.
        
                          - **SL** *(list) --* 
        
                            For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
        
                            - *(string) --* 
                        
                          - **SDM** *(dict) --* 
        
                            For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters. 
        
                            - *(string) --* 
                              
                              - *(float) --* 
                        
                    - **Team** *(string) --* 
        
                      Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
        
                    - **LatencyInMs** *(dict) --* 
        
                      Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. If this property is present, FlexMatch considers placing the match only in regions for which latency is reported. 
        
                      If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no regions are available to the player and the ticket is not matchable. 
        
                      - *(string) --* 
                        
                        - *(integer) --* 
                  
                - **GameSessionConnectionInfo** *(dict) --* 
        
                  Identifier and connection information of the game session created for the match. This information is added to the ticket only after the matchmaking request has been successfully completed.
        
                  - **GameSessionArn** *(string) --* 
        
                    Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session and uniquely identifies it.
        
                  - **IpAddress** *(string) --* 
        
                    IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                  - **Port** *(integer) --* 
        
                    Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                  - **MatchedPlayerSessions** *(list) --* 
        
                    Collection of player session IDs, one for each player ID that was included in the original matchmaking request. 
        
                    - *(dict) --* 
        
                      Represents a new player session that is created as a result of a successful FlexMatch match. A successful match automatically creates new player sessions for every player ID in the original matchmaking request. 
        
                      When players connect to the match\'s game session, they must include both player ID and player session ID in order to claim their assigned player slot.
        
                      - **PlayerId** *(string) --* 
        
                        Unique identifier for a player 
        
                      - **PlayerSessionId** *(string) --* 
        
                        Unique identifier for a player session
        
                - **EstimatedWaitTime** *(integer) --* 
        
                  Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.
        
        """
        pass

    def describe_matchmaking_configurations(self, Names: List = None, RuleSetName: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        Operations related to match configurations and rule sets include:
        
        *  CreateMatchmakingConfiguration   
         
        *  DescribeMatchmakingConfigurations   
         
        *  UpdateMatchmakingConfiguration   
         
        *  DeleteMatchmakingConfiguration   
         
        *  CreateMatchmakingRuleSet   
         
        *  DescribeMatchmakingRuleSets   
         
        *  ValidateMatchmakingRuleSet   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeMatchmakingConfigurations>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_matchmaking_configurations(
              Names=[
                  \'string\',
              ],
              RuleSetName=\'string\',
              Limit=123,
              NextToken=\'string\'
          )
        :type Names: list
        :param Names: 
        
          Unique identifier for a matchmaking configuration(s) to retrieve. To request all existing configurations, leave this parameter empty.
        
          - *(string) --* 
        
        :type RuleSetName: string
        :param RuleSetName: 
        
          Unique identifier for a matchmaking rule set. Use this parameter to retrieve all matchmaking configurations that use this rule set.
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages. This parameter is limited to 10.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Configurations\': [
                    {
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'GameSessionQueueArns\': [
                            \'string\',
                        ],
                        \'RequestTimeoutSeconds\': 123,
                        \'AcceptanceTimeoutSeconds\': 123,
                        \'AcceptanceRequired\': True|False,
                        \'RuleSetName\': \'string\',
                        \'NotificationTarget\': \'string\',
                        \'AdditionalPlayerCount\': 123,
                        \'CustomEventData\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'GameProperties\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'GameSessionData\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Configurations** *(list) --* 
        
              Collection of requested matchmaking configuration objects.
        
              - *(dict) --* 
        
                Guidelines for use with FlexMatch to match players into games. All matchmaking requests must specify a matchmaking configuration.
        
                - **Name** *(string) --* 
        
                  Unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
        
                - **Description** *(string) --* 
        
                  Descriptive label that is associated with matchmaking configuration.
        
                - **GameSessionQueueArns** *(list) --* 
        
                  Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
        
                  - *(string) --* 
              
                - **RequestTimeoutSeconds** *(integer) --* 
        
                  Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
        
                - **AcceptanceTimeoutSeconds** *(integer) --* 
        
                  Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
        
                - **AcceptanceRequired** *(boolean) --* 
        
                  Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
        
                - **RuleSetName** *(string) --* 
        
                  Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
        
                - **NotificationTarget** *(string) --* 
        
                  SNS topic ARN that is set up to receive matchmaking notifications.
        
                - **AdditionalPlayerCount** *(integer) --* 
        
                  Number of player slots in a match to keep open for future players. For example, if the configuration\'s rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.
        
                - **CustomEventData** *(string) --* 
        
                  Information to attached to all events related to the matchmaking configuration. 
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **GameProperties** *(list) --* 
        
                  Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
                  - *(dict) --* 
        
                    Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                    - **Key** *(string) --* 
        
                      Game property identifier.
        
                    - **Value** *(string) --* 
        
                      Game property value.
        
                - **GameSessionData** *(string) --* 
        
                  Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_matchmaking_rule_sets(self, Names: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        Operations related to match configurations and rule sets include:
        
        *  CreateMatchmakingConfiguration   
         
        *  DescribeMatchmakingConfigurations   
         
        *  UpdateMatchmakingConfiguration   
         
        *  DeleteMatchmakingConfiguration   
         
        *  CreateMatchmakingRuleSet   
         
        *  DescribeMatchmakingRuleSets   
         
        *  ValidateMatchmakingRuleSet   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeMatchmakingRuleSets>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_matchmaking_rule_sets(
              Names=[
                  \'string\',
              ],
              Limit=123,
              NextToken=\'string\'
          )
        :type Names: list
        :param Names: 
        
          Unique identifier for a matchmaking rule set. This name is used to identify the rule set associated with a matchmaking configuration.
        
          - *(string) --* 
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RuleSets\': [
                    {
                        \'RuleSetName\': \'string\',
                        \'RuleSetBody\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **RuleSets** *(list) --* 
        
              Collection of requested matchmaking rule set objects. 
        
              - *(dict) --* 
        
                Set of rule statements, used with FlexMatch, that determine how to build a certain kind of player match. Each rule set describes a type of group to be created and defines the parameters for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.
        
                A rule set may define the following elements for a match. For detailed information and examples showing how to construct a rule set, see `Build a FlexMatch Rule Set <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ . 
        
                * Teams -- Required. A rule set must define one or multiple teams for the match and set minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that requires all eight slots to be filled.  
                 
                * Player attributes -- Optional. These attributes specify a set of player characteristics to evaluate when looking for a match. Matchmaking requests that use a rule set with player attributes must provide the corresponding attribute values. For example, an attribute might specify a player\'s skill or level. 
                 
                * Rules -- Optional. Rules define how to evaluate potential players for a match based on player attributes. A rule might specify minimum requirements for individual players, teams, or entire matches. For example, a rule might require each player to meet a certain skill level, each team to have at least one player in a certain role, or the match to have a minimum average skill level. or may describe an entire group--such as all teams must be evenly matched or have at least one player in a certain role.  
                 
                * Expansions -- Optional. Expansions allow you to relax the rules after a period of time when no acceptable matches are found. This feature lets you balance getting players into games in a reasonable amount of time instead of making them wait indefinitely for the best possible match. For example, you might use an expansion to increase the maximum skill variance between players after 30 seconds. 
                 
                - **RuleSetName** *(string) --* 
        
                  Unique identifier for a matchmaking rule set
        
                - **RuleSetBody** *(string) --* 
        
                  Collection of matchmaking rules, formatted as a JSON string. (Note that comments14 are not allowed in JSON, but most elements support a description field.)
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_player_sessions(self, GameSessionId: str = None, PlayerId: str = None, PlayerSessionId: str = None, PlayerSessionStatusFilter: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        To get game session record(s), specify only one of the following: a player session ID, a game session ID, or a player ID. You can filter this request by player session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  PlayerSession object is returned for each session matching the request.
        
         *Available in Amazon GameLift Local.*  
        
        Player-session-related operations include:
        
        *  CreatePlayerSession   
         
        *  CreatePlayerSessions   
         
        *  DescribePlayerSessions   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribePlayerSessions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_player_sessions(
              GameSessionId=\'string\',
              PlayerId=\'string\',
              PlayerSessionId=\'string\',
              PlayerSessionStatusFilter=\'string\',
              Limit=123,
              NextToken=\'string\'
          )
        :type GameSessionId: string
        :param GameSessionId: 
        
          Unique identifier for the game session to retrieve player sessions for.
        
        :type PlayerId: string
        :param PlayerId: 
        
          Unique identifier for a player to retrieve player sessions for.
        
        :type PlayerSessionId: string
        :param PlayerSessionId: 
        
          Unique identifier for a player session to retrieve.
        
        :type PlayerSessionStatusFilter: string
        :param PlayerSessionStatusFilter: 
        
          Player session status to filter results on.
        
          Possible player session statuses include the following:
        
          * **RESERVED** -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.  
           
          * **ACTIVE** -- The player has been validated by the server process and is currently connected. 
           
          * **COMPLETED** -- The player connection has been dropped. 
           
          * **TIMEDOUT** -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds). 
           
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PlayerSessions\': [
                    {
                        \'PlayerSessionId\': \'string\',
                        \'PlayerId\': \'string\',
                        \'GameSessionId\': \'string\',
                        \'FleetId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'TerminationTime\': datetime(2015, 1, 1),
                        \'Status\': \'RESERVED\'|\'ACTIVE\'|\'COMPLETED\'|\'TIMEDOUT\',
                        \'IpAddress\': \'string\',
                        \'Port\': 123,
                        \'PlayerData\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **PlayerSessions** *(list) --* 
        
              Collection of objects containing properties for each player session that matches the request.
        
              - *(dict) --* 
        
                Properties describing a player session. Player session objects are created either by creating a player session for a specific game session, or as part of a game session placement. A player session represents either a player reservation for a game session (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A player session object (including player data) is automatically passed to a game session when the player connects to the game session and is validated.
        
                When a player disconnects, the player session status changes to ``COMPLETED`` . Once the session ends, the player session object is retained for 30 days and then removed.
        
                Player-session-related operations include:
        
                *  CreatePlayerSession   
                 
                *  CreatePlayerSessions   
                 
                *  DescribePlayerSessions   
                 
                * Game session placements 
        
                  *  StartGameSessionPlacement   
                   
                  *  DescribeGameSessionPlacement   
                   
                  *  StopGameSessionPlacement   
                   
                - **PlayerSessionId** *(string) --* 
        
                  Unique identifier for a player session.
        
                - **PlayerId** *(string) --* 
        
                  Unique identifier for a player that is associated with this player session.
        
                - **GameSessionId** *(string) --* 
        
                  Unique identifier for the game session that the player session is connected to.
        
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that the player\'s game session is running on.
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **TerminationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **Status** *(string) --* 
        
                  Current status of the player session.
        
                  Possible player session statuses include the following:
        
                  * **RESERVED** -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.  
                   
                  * **ACTIVE** -- The player has been validated by the server process and is currently connected. 
                   
                  * **COMPLETED** -- The player connection has been dropped. 
                   
                  * **TIMEDOUT** -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds). 
                   
                - **IpAddress** *(string) --* 
        
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **Port** *(integer) --* 
        
                  Port number for the game session. To connect to a Amazon GameLift server process, an app needs both the IP address and port number.
        
                - **PlayerData** *(string) --* 
        
                  Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. 
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_runtime_configuration(self, FleetId: str) -> Dict:
        """
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeRuntimeConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_runtime_configuration(
              FleetId=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to get the run-time configuration for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RuntimeConfiguration\': {
                    \'ServerProcesses\': [
                        {
                            \'LaunchPath\': \'string\',
                            \'Parameters\': \'string\',
                            \'ConcurrentExecutions\': 123
                        },
                    ],
                    \'MaxConcurrentGameSessionActivations\': 123,
                    \'GameSessionActivationTimeoutSeconds\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **RuntimeConfiguration** *(dict) --* 
        
              Instructions describing how server processes should be launched and maintained on each instance in the fleet.
        
              - **ServerProcesses** *(list) --* 
        
                Collection of server process configurations that describe which server processes to run on each instance in a fleet.
        
                - *(dict) --* 
        
                  A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s ``  RuntimeConfiguration `` .
        
                  - **LaunchPath** *(string) --* 
        
                    Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances ``C:\game`` , and for Linux instances ``/local/game`` . A Windows game build with an executable file located at ``MyGame\latest\server.exe`` must have a launch path of \"``C:\game\MyGame\latest\server.exe`` \". A Linux game build with an executable file located at ``MyGame/latest/server.exe`` must have a launch path of \"``/local/game/MyGame/latest/server.exe`` \". 
        
                  - **Parameters** *(string) --* 
        
                    Optional list of parameters to pass to the server executable on launch.
        
                  - **ConcurrentExecutions** *(integer) --* 
        
                    Number of server processes using this configuration to run concurrently on an instance.
        
              - **MaxConcurrentGameSessionActivations** *(integer) --* 
        
                Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
        
              - **GameSessionActivationTimeoutSeconds** *(integer) --* 
        
                Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING`` . If the game session is not active before the timeout, activation is terminated and the game session status is changed to ``TERMINATED`` .
        
        """
        pass

    def describe_scaling_policies(self, FleetId: str, StatusFilter: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        To get a fleet\'s scaling policies, specify the fleet ID. You can filter this request by policy status, such as to retrieve only active scaling policies. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, set of  ScalingPolicy objects is returned for the fleet.
        
        A fleet may have all of its scaling policies suspended ( StopFleetActions ). This action does not affect the status of the scaling policies, which remains ACTIVE. To see whether a fleet\'s scaling policies are in force or suspended, call  DescribeFleetAttributes and check the stopped actions.
        
        Operations related to fleet capacity scaling include:
        
        *  DescribeFleetCapacity   
         
        *  UpdateFleetCapacity   
         
        *  DescribeEC2InstanceLimits   
         
        * Manage scaling policies: 
        
          *  PutScalingPolicy (auto-scaling) 
           
          *  DescribeScalingPolicies (auto-scaling) 
           
          *  DeleteScalingPolicy (auto-scaling) 
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeScalingPolicies>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_scaling_policies(
              FleetId=\'string\',
              StatusFilter=\'ACTIVE\'|\'UPDATE_REQUESTED\'|\'UPDATING\'|\'DELETE_REQUESTED\'|\'DELETING\'|\'DELETED\'|\'ERROR\',
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to retrieve scaling policies for.
        
        :type StatusFilter: string
        :param StatusFilter: 
        
          Scaling policy status to filter results on. A scaling policy is only in force when in an ``ACTIVE`` status.
        
          * **ACTIVE** -- The scaling policy is currently in force. 
           
          * **UPDATEREQUESTED** -- A request to update the scaling policy has been received. 
           
          * **UPDATING** -- A change is being made to the scaling policy. 
           
          * **DELETEREQUESTED** -- A request to delete the scaling policy has been received. 
           
          * **DELETING** -- The scaling policy is being deleted. 
           
          * **DELETED** -- The scaling policy has been deleted. 
           
          * **ERROR** -- An error occurred in creating the policy. It should be removed and recreated. 
           
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ScalingPolicies\': [
                    {
                        \'FleetId\': \'string\',
                        \'Name\': \'string\',
                        \'Status\': \'ACTIVE\'|\'UPDATE_REQUESTED\'|\'UPDATING\'|\'DELETE_REQUESTED\'|\'DELETING\'|\'DELETED\'|\'ERROR\',
                        \'ScalingAdjustment\': 123,
                        \'ScalingAdjustmentType\': \'ChangeInCapacity\'|\'ExactCapacity\'|\'PercentChangeInCapacity\',
                        \'ComparisonOperator\': \'GreaterThanOrEqualToThreshold\'|\'GreaterThanThreshold\'|\'LessThanThreshold\'|\'LessThanOrEqualToThreshold\',
                        \'Threshold\': 123.0,
                        \'EvaluationPeriods\': 123,
                        \'MetricName\': \'ActivatingGameSessions\'|\'ActiveGameSessions\'|\'ActiveInstances\'|\'AvailableGameSessions\'|\'AvailablePlayerSessions\'|\'CurrentPlayerSessions\'|\'IdleInstances\'|\'PercentAvailableGameSessions\'|\'PercentIdleInstances\'|\'QueueDepth\'|\'WaitTime\',
                        \'PolicyType\': \'RuleBased\'|\'TargetBased\',
                        \'TargetConfiguration\': {
                            \'TargetValue\': 123.0
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **ScalingPolicies** *(list) --* 
        
              Collection of objects containing the scaling policies matching the request.
        
              - *(dict) --* 
        
                Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
        
                Operations related to fleet capacity scaling include:
        
                *  DescribeFleetCapacity   
                 
                *  UpdateFleetCapacity   
                 
                *  DescribeEC2InstanceLimits   
                 
                * Manage scaling policies: 
        
                  *  PutScalingPolicy (auto-scaling) 
                   
                  *  DescribeScalingPolicies (auto-scaling) 
                   
                  *  DeleteScalingPolicy (auto-scaling) 
                   
                * Manage fleet actions: 
        
                  *  StartFleetActions   
                   
                  *  StopFleetActions   
                   
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that is associated with this scaling policy.
        
                - **Name** *(string) --* 
        
                  Descriptive label that is associated with a scaling policy. Policy names do not need to be unique.
        
                - **Status** *(string) --* 
        
                  Current status of the scaling policy. The scaling policy can be in force only when in an ``ACTIVE`` status. Scaling policies can be suspended for individual fleets (see  StopFleetActions ; if suspended for a fleet, the policy status does not change. View a fleet\'s stopped actions by calling  DescribeFleetCapacity .
        
                  * **ACTIVE** -- The scaling policy can be used for auto-scaling a fleet. 
                   
                  * **UPDATE_REQUESTED** -- A request to update the scaling policy has been received. 
                   
                  * **UPDATING** -- A change is being made to the scaling policy. 
                   
                  * **DELETE_REQUESTED** -- A request to delete the scaling policy has been received. 
                   
                  * **DELETING** -- The scaling policy is being deleted. 
                   
                  * **DELETED** -- The scaling policy has been deleted. 
                   
                  * **ERROR** -- An error occurred in creating the policy. It should be removed and recreated. 
                   
                - **ScalingAdjustment** *(integer) --* 
        
                  Amount of adjustment to make, based on the scaling adjustment type.
        
                - **ScalingAdjustmentType** *(string) --* 
        
                  Type of adjustment to make to a fleet\'s instance count (see  FleetCapacity ):
        
                  * **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down. 
                   
                  * **ExactCapacity** -- set the instance count to the scaling adjustment value. 
                   
                  * **PercentChangeInCapacity** -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down. 
                   
                - **ComparisonOperator** *(string) --* 
        
                  Comparison operator to use when measuring a metric against the threshold value.
        
                - **Threshold** *(float) --* 
        
                  Metric value used to trigger a scaling event.
        
                - **EvaluationPeriods** *(integer) --* 
        
                  Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
        
                - **MetricName** *(string) --* 
        
                  Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon CloudWatch <http://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`__ . 
        
                  * **ActivatingGameSessions** -- Game sessions in the process of being created. 
                   
                  * **ActiveGameSessions** -- Game sessions that are currently running. 
                   
                  * **ActiveInstances** -- Fleet instances that are currently running at least one game session. 
                   
                  * **AvailableGameSessions** -- Additional game sessions that fleet could host simultaneously, given current capacity. 
                   
                  * **AvailablePlayerSessions** -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included. 
                   
                  * **CurrentPlayerSessions** -- Player slots in active game sessions that are being used by a player or are reserved for a player.  
                   
                  * **IdleInstances** -- Active instances that are currently hosting zero game sessions.  
                   
                  * **PercentAvailableGameSessions** -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy. 
                   
                  * **PercentIdleInstances** -- Percentage of the total number of active instances that are hosting zero game sessions. 
                   
                  * **QueueDepth** -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination. 
                   
                  * **WaitTime** -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.  
                   
                - **PolicyType** *(string) --* 
        
                  Type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to \'PercentAvailableGameSessions\' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .
        
                - **TargetConfiguration** *(dict) --* 
        
                  Object that contains settings for a target-based scaling policy.
        
                  - **TargetValue** *(float) --* 
        
                    Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet\'s buffer (the percent of capacity that should be idle and ready for new game sessions).
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def describe_vpc_peering_authorizations(self) -> Dict:
        """
        
        VPC peering connection operations include:
        
        *  CreateVpcPeeringAuthorization   
         
        *  DescribeVpcPeeringAuthorizations   
         
        *  DeleteVpcPeeringAuthorization   
         
        *  CreateVpcPeeringConnection   
         
        *  DescribeVpcPeeringConnections   
         
        *  DeleteVpcPeeringConnection   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_vpc_peering_authorizations()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'VpcPeeringAuthorizations\': [
                    {
                        \'GameLiftAwsAccountId\': \'string\',
                        \'PeerVpcAwsAccountId\': \'string\',
                        \'PeerVpcId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'ExpirationTime\': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **VpcPeeringAuthorizations** *(list) --* 
        
              Collection of objects that describe all valid VPC peering operations for the current AWS account.
        
              - *(dict) --* 
        
                Represents an authorization for a VPC peering connection between the VPC for an Amazon GameLift fleet and another VPC on an account you have access to. This authorization must exist and be valid for the peering connection to be established. Authorizations are valid for 24 hours after they are issued.
        
                VPC peering connection operations include:
        
                *  CreateVpcPeeringAuthorization   
                 
                *  DescribeVpcPeeringAuthorizations   
                 
                *  DeleteVpcPeeringAuthorization   
                 
                *  CreateVpcPeeringConnection   
                 
                *  DescribeVpcPeeringConnections   
                 
                *  DeleteVpcPeeringConnection   
                 
                - **GameLiftAwsAccountId** *(string) --* 
        
                  Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
        
                - **PeerVpcAwsAccountId** *(string) --* 
        
                - **PeerVpcId** *(string) --* 
        
                  Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this authorization was issued. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **ExpirationTime** *(datetime) --* 
        
                  Time stamp indicating when this authorization expires (24 hours after issuance). Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
        """
        pass

    def describe_vpc_peering_connections(self, FleetId: str = None) -> Dict:
        """
        
        To retrieve connection information, call this operation from the AWS account that is used to manage the Amazon GameLift fleets. Specify a fleet ID or leave the parameter empty to retrieve all connection records. If successful, the retrieved information includes both active and pending connections. Active connections identify the IpV4 CIDR block that the VPC uses to connect. 
        
        VPC peering connection operations include:
        
        *  CreateVpcPeeringAuthorization   
         
        *  DescribeVpcPeeringAuthorizations   
         
        *  DeleteVpcPeeringAuthorization   
         
        *  CreateVpcPeeringConnection   
         
        *  DescribeVpcPeeringConnections   
         
        *  DeleteVpcPeeringConnection   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeVpcPeeringConnections>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_vpc_peering_connections(
              FleetId=\'string\'
          )
        :type FleetId: string
        :param FleetId: 
        
          Unique identifier for a fleet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'VpcPeeringConnections\': [
                    {
                        \'FleetId\': \'string\',
                        \'IpV4CidrBlock\': \'string\',
                        \'VpcPeeringConnectionId\': \'string\',
                        \'Status\': {
                            \'Code\': \'string\',
                            \'Message\': \'string\'
                        },
                        \'PeerVpcId\': \'string\',
                        \'GameLiftVpcId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **VpcPeeringConnections** *(list) --* 
        
              Collection of VPC peering connection records that match the request.
        
              - *(dict) --* 
        
                Represents a peering connection between a VPC on one of your AWS accounts and the VPC for your Amazon GameLift fleets. This record may be for an active peering connection or a pending connection that has not yet been established.
        
                VPC peering connection operations include:
        
                *  CreateVpcPeeringAuthorization   
                 
                *  DescribeVpcPeeringAuthorizations   
                 
                *  DeleteVpcPeeringAuthorization   
                 
                *  CreateVpcPeeringConnection   
                 
                *  DescribeVpcPeeringConnections   
                 
                *  DeleteVpcPeeringConnection   
                 
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet. This ID determines the ID of the Amazon GameLift VPC for your fleet.
        
                - **IpV4CidrBlock** *(string) --* 
        
                  CIDR block of IPv4 addresses assigned to the VPC peering connection for the GameLift VPC. The peered VPC also has an IPv4 CIDR block associated with it; these blocks cannot overlap or the peering connection cannot be created. 
        
                - **VpcPeeringConnectionId** *(string) --* 
        
                  Unique identifier that is automatically assigned to the connection record. This ID is referenced in VPC peering connection events, and is used when deleting a connection with  DeleteVpcPeeringConnection . 
        
                - **Status** *(dict) --* 
        
                  Object that contains status information about the connection. Status indicates if a connection is pending, successful, or failed.
        
                  - **Code** *(string) --* 
        
                    Code indicating the status of a VPC peering connection.
        
                  - **Message** *(string) --* 
        
                    Additional messaging associated with the connection status. 
        
                - **PeerVpcId** *(string) --* 
        
                  Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
        
                - **GameLiftVpcId** *(string) --* 
        
                  Unique identifier for the VPC that contains the Amazon GameLift fleet for this connection. This VPC is managed by Amazon GameLift and does not appear in your AWS account. 
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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

    def get_game_session_log_url(self, GameSessionId: str) -> Dict:
        """
        
        .. note::
        
          See the `AWS Service Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_gamelift>`__ page for maximum log file sizes. Log files that exceed this limit are not saved.
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/GetGameSessionLogUrl>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_game_session_log_url(
              GameSessionId=\'string\'
          )
        :type GameSessionId: string
        :param GameSessionId: **[REQUIRED]** 
        
          Unique identifier for the game session to get logs for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PreSignedUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **PreSignedUrl** *(string) --* 
        
              Location of the requested game session logs, available for download.
        
        """
        pass

    def get_instance_access(self, FleetId: str, InstanceId: str) -> Dict:
        """
        
        Access requires credentials that match the operating system of the instance. For a Windows instance, Amazon GameLift returns a user name and password as strings for use with a Windows Remote Desktop client. For a Linux instance, Amazon GameLift returns a user name and RSA private key, also as strings, for use with an SSH client. The private key must be saved in the proper format to a ``.pem`` file before using. If you\'re making this request using the AWS CLI, saving the secret can be handled as part of the GetInstanceAccess request. (See the example later in this topic). For more information on remote access, see `Remotely Accessing an Instance <http://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html>`__ .
        
        To request access to a specific instance, specify the IDs of the instance and the fleet it belongs to. If successful, an  InstanceAccess object is returned containing the instance\'s IP address and a set of credentials.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/GetInstanceAccess>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance_access(
              FleetId=\'string\',
              InstanceId=\'string\'
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet that contains the instance you want access to. The fleet can be in any of the following statuses: ``ACTIVATING`` , ``ACTIVE`` , or ``ERROR`` . Fleets with an ``ERROR`` status may be accessible for a short time before they are deleted.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          Unique identifier for an instance you want to get access to. You can access an instance in any status.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceAccess\': {
                    \'FleetId\': \'string\',
                    \'InstanceId\': \'string\',
                    \'IpAddress\': \'string\',
                    \'OperatingSystem\': \'WINDOWS_2012\'|\'AMAZON_LINUX\',
                    \'Credentials\': {
                        \'UserName\': \'string\',
                        \'Secret\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **InstanceAccess** *(dict) --* 
        
              Object that contains connection information for a fleet instance, including IP address and access credentials.
        
              - **FleetId** *(string) --* 
        
                Unique identifier for a fleet containing the instance being accessed.
        
              - **InstanceId** *(string) --* 
        
                Unique identifier for an instance being accessed.
        
              - **IpAddress** *(string) --* 
        
                IP address assigned to the instance.
        
              - **OperatingSystem** *(string) --* 
        
                Operating system that is running on the instance.
        
              - **Credentials** *(dict) --* 
        
                Credentials required to access the instance.
        
                - **UserName** *(string) --* 
        
                  User login string.
        
                - **Secret** *(string) --* 
        
                  Secret string. For Windows instances, the secret is a password for use with Windows Remote Desktop. For Linux instances, it is a private key (which must be saved as a ``.pem`` file) for use with SSH.
        
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_aliases(self, RoutingStrategyType: str = None, Name: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          Returned aliases are not listed in any particular order.
        
        Alias-related operations include:
        
        *  CreateAlias   
         
        *  ListAliases   
         
        *  DescribeAlias   
         
        *  UpdateAlias   
         
        *  DeleteAlias   
         
        *  ResolveAlias   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ListAliases>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_aliases(
              RoutingStrategyType=\'SIMPLE\'|\'TERMINAL\',
              Name=\'string\',
              Limit=123,
              NextToken=\'string\'
          )
        :type RoutingStrategyType: string
        :param RoutingStrategyType: 
        
          Type of routing to filter results on. Use this parameter to retrieve only aliases of a certain type. To retrieve all aliases, leave this parameter empty.
        
          Possible routing types include the following:
        
          * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets. 
           
          * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded. 
           
        :type Name: string
        :param Name: 
        
          Descriptive label that is associated with an alias. Alias names do not need to be unique.
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Aliases\': [
                    {
                        \'AliasId\': \'string\',
                        \'Name\': \'string\',
                        \'AliasArn\': \'string\',
                        \'Description\': \'string\',
                        \'RoutingStrategy\': {
                            \'Type\': \'SIMPLE\'|\'TERMINAL\',
                            \'FleetId\': \'string\',
                            \'Message\': \'string\'
                        },
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LastUpdatedTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Aliases** *(list) --* 
        
              Collection of alias records that match the list request.
        
              - *(dict) --* 
        
                Properties describing a fleet alias.
        
                Alias-related operations include:
        
                *  CreateAlias   
                 
                *  ListAliases   
                 
                *  DescribeAlias   
                 
                *  UpdateAlias   
                 
                *  DeleteAlias   
                 
                *  ResolveAlias   
                 
                - **AliasId** *(string) --* 
        
                  Unique identifier for an alias; alias IDs are unique within a region.
        
                - **Name** *(string) --* 
        
                  Descriptive label that is associated with an alias. Alias names do not need to be unique.
        
                - **AliasArn** *(string) --* 
        
                  Unique identifier for an alias; alias ARNs are unique across all regions.
        
                - **Description** *(string) --* 
        
                  Human-readable description of an alias.
        
                - **RoutingStrategy** *(dict) --* 
        
                  Alias configuration for the alias, including routing type and settings.
        
                  - **Type** *(string) --* 
        
                    Type of routing strategy.
        
                    Possible routing types include the following:
        
                    * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets. 
                     
                    * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded. 
                     
                  - **FleetId** *(string) --* 
        
                    Unique identifier for a fleet that the alias points to.
        
                  - **Message** *(string) --* 
        
                    Message text to be used with a terminal routing strategy.
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **LastUpdatedTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def list_builds(self, Status: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          Build records are not listed in any particular order.
        
        Build-related operations include:
        
        *  CreateBuild   
         
        *  ListBuilds   
         
        *  DescribeBuild   
         
        *  UpdateBuild   
         
        *  DeleteBuild   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ListBuilds>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_builds(
              Status=\'INITIALIZED\'|\'READY\'|\'FAILED\',
              Limit=123,
              NextToken=\'string\'
          )
        :type Status: string
        :param Status: 
        
          Build status to filter results by. To retrieve all builds, leave this parameter empty.
        
          Possible build statuses include the following:
        
          * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.  
           
          * **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build. 
           
          * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.  
           
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Builds\': [
                    {
                        \'BuildId\': \'string\',
                        \'Name\': \'string\',
                        \'Version\': \'string\',
                        \'Status\': \'INITIALIZED\'|\'READY\'|\'FAILED\',
                        \'SizeOnDisk\': 123,
                        \'OperatingSystem\': \'WINDOWS_2012\'|\'AMAZON_LINUX\',
                        \'CreationTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Builds** *(list) --* 
        
              Collection of build records that match the request.
        
              - *(dict) --* 
        
                Properties describing a game build.
        
                Build-related operations include:
        
                *  CreateBuild   
                 
                *  ListBuilds   
                 
                *  DescribeBuild   
                 
                *  UpdateBuild   
                 
                *  DeleteBuild   
                 
                - **BuildId** *(string) --* 
        
                  Unique identifier for a build.
        
                - **Name** *(string) --* 
        
                  Descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .
        
                - **Version** *(string) --* 
        
                  Version that is associated with this build. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .
        
                - **Status** *(string) --* 
        
                  Current status of the build.
        
                  Possible build statuses include the following:
        
                  * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.  
                   
                  * **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build. 
                   
                  * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.  
                   
                - **SizeOnDisk** *(integer) --* 
        
                  File size of the uploaded game build, expressed in bytes. When the build status is ``INITIALIZED`` , this value is 0.
        
                - **OperatingSystem** *(string) --* 
        
                  Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def list_fleets(self, BuildId: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          Fleet records are not listed in any particular order.
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ListFleets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_fleets(
              BuildId=\'string\',
              Limit=123,
              NextToken=\'string\'
          )
        :type BuildId: string
        :param BuildId: 
        
          Unique identifier for a build to return fleets for. Use this parameter to return only fleets using the specified build. To retrieve all fleets, leave this parameter empty.
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages.
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetIds\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetIds** *(list) --* 
        
              Set of fleet IDs matching the list request. You can retrieve additional information about all returned fleets by passing this result set to a call to  DescribeFleetAttributes ,  DescribeFleetCapacity , or  DescribeFleetUtilization .
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def put_scaling_policy(self, Name: str, FleetId: str, MetricName: str, ScalingAdjustment: int = None, ScalingAdjustmentType: str = None, Threshold: float = None, ComparisonOperator: str = None, EvaluationPeriods: int = None, PolicyType: str = None, TargetConfiguration: Dict = None) -> Dict:
        """
        
        Fleets can have multiple scaling policies of each type in force at the same time; you can have one target-based policy, one or multiple rule-based scaling policies, or both. We recommend caution, however, because multiple auto-scaling policies can have unintended consequences.
        
        You can temporarily suspend all scaling policies for a fleet by calling  StopFleetActions with the fleet action AUTO_SCALING. To resume scaling policies, call  StartFleetActions with the same fleet action. To stop just one scaling policy--or to permanently remove it, you must delete the policy with  DeleteScalingPolicy .
        
        Learn more about how to work with auto-scaling in `Set Up Fleet Automatic Scaling <http://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-autoscaling.html>`__ .
        
         **Target-based policy**  
        
        A target-based policy tracks a single metric: PercentAvailableGameSessions. This metric tells us how much of a fleet\'s hosting capacity is ready to host game sessions but is not currently in use. This is the fleet\'s buffer; it measures the additional player demand that the fleet could handle at current capacity. With a target-based policy, you set your ideal buffer size and leave it to Amazon GameLift to take whatever action is needed to maintain that target. 
        
        For example, you might choose to maintain a 10% buffer for a fleet that has the capacity to host 100 simultaneous game sessions. This policy tells Amazon GameLift to take action whenever the fleet\'s available capacity falls below or rises above 10 game sessions. Amazon GameLift will start new instances or stop unused instances in order to return to the 10% buffer. 
        
        To create or update a target-based policy, specify a fleet ID and name, and set the policy type to \"TargetBased\". Specify the metric to track (PercentAvailableGameSessions) and reference a  TargetConfiguration object with your desired buffer value. Exclude all other parameters. On a successful request, the policy name is returned. The scaling policy is automatically in force as soon as it\'s successfully created. If the fleet\'s auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.
        
         **Rule-based policy**  
        
        A rule-based policy tracks specified fleet metric, sets a threshold value, and specifies the type of action to initiate when triggered. With a rule-based policy, you can select from several available fleet metrics. Each policy specifies whether to scale up or scale down (and by how much), so you need one policy for each type of action. 
        
        For example, a policy may make the following statement: \"If the percentage of idle instances is greater than 20% for more than 15 minutes, then reduce the fleet capacity by 10%.\"
        
        A policy\'s rule statement has the following structure:
        
        If ``[MetricName]`` is ``[ComparisonOperator]``  ``[Threshold]`` for ``[EvaluationPeriods]`` minutes, then ``[ScalingAdjustmentType]`` to/by ``[ScalingAdjustment]`` .
        
        To implement the example, the rule statement would look like this:
        
        If ``[PercentIdleInstances]`` is ``[GreaterThanThreshold]``  ``[20]`` for ``[15]`` minutes, then ``[PercentChangeInCapacity]`` to/by ``[10]`` .
        
        To create or update a scaling policy, specify a unique combination of name and fleet ID, and set the policy type to \"RuleBased\". Specify the parameter values for a policy rule statement. On a successful request, the policy name is returned. Scaling policies are automatically in force as soon as they\'re successfully created. If the fleet\'s auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.
        
        Operations related to fleet capacity scaling include:
        
        *  DescribeFleetCapacity   
         
        *  UpdateFleetCapacity   
         
        *  DescribeEC2InstanceLimits   
         
        * Manage scaling policies: 
        
          *  PutScalingPolicy (auto-scaling) 
           
          *  DescribeScalingPolicies (auto-scaling) 
           
          *  DeleteScalingPolicy (auto-scaling) 
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/PutScalingPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_scaling_policy(
              Name=\'string\',
              FleetId=\'string\',
              ScalingAdjustment=123,
              ScalingAdjustmentType=\'ChangeInCapacity\'|\'ExactCapacity\'|\'PercentChangeInCapacity\',
              Threshold=123.0,
              ComparisonOperator=\'GreaterThanOrEqualToThreshold\'|\'GreaterThanThreshold\'|\'LessThanThreshold\'|\'LessThanOrEqualToThreshold\',
              EvaluationPeriods=123,
              MetricName=\'ActivatingGameSessions\'|\'ActiveGameSessions\'|\'ActiveInstances\'|\'AvailableGameSessions\'|\'AvailablePlayerSessions\'|\'CurrentPlayerSessions\'|\'IdleInstances\'|\'PercentAvailableGameSessions\'|\'PercentIdleInstances\'|\'QueueDepth\'|\'WaitTime\',
              PolicyType=\'RuleBased\'|\'TargetBased\',
              TargetConfiguration={
                  \'TargetValue\': 123.0
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Descriptive label that is associated with a scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.
        
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to apply this policy to. The fleet cannot be in any of the following statuses: ERROR or DELETING.
        
        :type ScalingAdjustment: integer
        :param ScalingAdjustment: 
        
          Amount of adjustment to make, based on the scaling adjustment type.
        
        :type ScalingAdjustmentType: string
        :param ScalingAdjustmentType: 
        
          Type of adjustment to make to a fleet\'s instance count (see  FleetCapacity ):
        
          * **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down. 
           
          * **ExactCapacity** -- set the instance count to the scaling adjustment value. 
           
          * **PercentChangeInCapacity** -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of \"-10\" scales the fleet down by 10%. 
           
        :type Threshold: float
        :param Threshold: 
        
          Metric value used to trigger a scaling event.
        
        :type ComparisonOperator: string
        :param ComparisonOperator: 
        
          Comparison operator to use when measuring the metric against the threshold value.
        
        :type EvaluationPeriods: integer
        :param EvaluationPeriods: 
        
          Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
        
        :type MetricName: string
        :param MetricName: **[REQUIRED]** 
        
          Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon CloudWatch <http://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`__ . 
        
          * **ActivatingGameSessions** -- Game sessions in the process of being created. 
           
          * **ActiveGameSessions** -- Game sessions that are currently running. 
           
          * **ActiveInstances** -- Fleet instances that are currently running at least one game session. 
           
          * **AvailableGameSessions** -- Additional game sessions that fleet could host simultaneously, given current capacity. 
           
          * **AvailablePlayerSessions** -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included. 
           
          * **CurrentPlayerSessions** -- Player slots in active game sessions that are being used by a player or are reserved for a player.  
           
          * **IdleInstances** -- Active instances that are currently hosting zero game sessions.  
           
          * **PercentAvailableGameSessions** -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy. 
           
          * **PercentIdleInstances** -- Percentage of the total number of active instances that are hosting zero game sessions. 
           
          * **QueueDepth** -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination. 
           
          * **WaitTime** -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.  
           
        :type PolicyType: string
        :param PolicyType: 
        
          Type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to \'PercentAvailableGameSessions\' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .
        
        :type TargetConfiguration: dict
        :param TargetConfiguration: 
        
          Object that contains settings for a target-based scaling policy.
        
          - **TargetValue** *(float) --* **[REQUIRED]** 
        
            Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet\'s buffer (the percent of capacity that should be idle and ready for new game sessions).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Name** *(string) --* 
        
              Descriptive label that is associated with a scaling policy. Policy names do not need to be unique.
        
        """
        pass

    def request_upload_credentials(self, BuildId: str) -> Dict:
        """
        
        To request new credentials, specify the build ID as returned with an initial ``CreateBuild`` request. If successful, a new set of credentials are returned, along with the S3 storage location associated with the build ID.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/RequestUploadCredentials>`_
        
        **Request Syntax** 
        ::
        
          response = client.request_upload_credentials(
              BuildId=\'string\'
          )
        :type BuildId: string
        :param BuildId: **[REQUIRED]** 
        
          Unique identifier for a build to get credentials for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UploadCredentials\': {
                    \'AccessKeyId\': \'string\',
                    \'SecretAccessKey\': \'string\',
                    \'SessionToken\': \'string\'
                },
                \'StorageLocation\': {
                    \'Bucket\': \'string\',
                    \'Key\': \'string\',
                    \'RoleArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **UploadCredentials** *(dict) --* 
        
              AWS credentials required when uploading a game build to the storage location. These credentials have a limited lifespan and are valid only for the build they were issued for.
        
              - **AccessKeyId** *(string) --* 
        
                Temporary key allowing access to the Amazon GameLift S3 account.
        
              - **SecretAccessKey** *(string) --* 
        
                Temporary secret key allowing access to the Amazon GameLift S3 account.
        
              - **SessionToken** *(string) --* 
        
                Token used to associate a specific build ID with the files uploaded using these credentials.
        
            - **StorageLocation** *(dict) --* 
        
              Amazon S3 path and key, identifying where the game build files are stored.
        
              - **Bucket** *(string) --* 
        
                Amazon S3 bucket identifier. This is the name of your S3 bucket.
        
              - **Key** *(string) --* 
        
                Name of the zip file containing your build files. 
        
              - **RoleArn** *(string) --* 
        
                Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for the access role that allows Amazon GameLift to access your S3 bucket.
        
        """
        pass

    def resolve_alias(self, AliasId: str) -> Dict:
        """
        
        Alias-related operations include:
        
        *  CreateAlias   
         
        *  ListAliases   
         
        *  DescribeAlias   
         
        *  UpdateAlias   
         
        *  DeleteAlias   
         
        *  ResolveAlias   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ResolveAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.resolve_alias(
              AliasId=\'string\'
          )
        :type AliasId: string
        :param AliasId: **[REQUIRED]** 
        
          Unique identifier for the alias you want to resolve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetId** *(string) --* 
        
              Fleet identifier that is associated with the requested alias.
        
        """
        pass

    def search_game_sessions(self, FleetId: str = None, AliasId: str = None, FilterExpression: str = None, SortExpression: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Retrieves all active game sessions that match a set of search criteria and sorts them in a specified order. You can search or sort by the following game session attributes:
        
        * **gameSessionId** -- Unique identifier for the game session. You can use either a ``GameSessionId`` or ``GameSessionArn`` value.  
         
        * **gameSessionName** -- Name assigned to a game session. This value is set when requesting a new game session with  CreateGameSession or updating with  UpdateGameSession . Game session names do not need to be unique to a game session. 
         
        * **gameSessionProperties** -- Custom data defined in a game session\'s ``GameProperty`` parameter. ``GameProperty`` values are stored as key:value pairs; the filter expression must indicate the key and a string to search the data values for. For example, to search for game sessions with custom data containing the key:value pair \"gameMode:brawl\", specify the following: ``gameSessionProperties.gameMode = \"brawl\"`` . All custom data values are searched as strings. 
         
        * **maximumSessions** -- Maximum number of player sessions allowed for a game session. This value is set when requesting a new game session with  CreateGameSession or updating with  UpdateGameSession . 
         
        * **creationTimeMillis** -- Value indicating when a game session was created. It is expressed in Unix time as milliseconds. 
         
        * **playerSessionCount** -- Number of players currently connected to a game session. This value changes rapidly as players join the session or drop out. 
         
        * **hasAvailablePlayerSessions** -- Boolean value indicating whether a game session has reached its maximum number of players. It is highly recommended that all search requests include this filter attribute to optimize search performance and return only sessions that players can join.  
         
        .. note::
        
          Returned values for ``playerSessionCount`` and ``hasAvailablePlayerSessions`` change quickly as players join sessions and others drop out. Results should be considered a snapshot in time. Be sure to refresh search results often, and handle sessions that fill up before a player can join. 
        
        To search or sort, specify either a fleet ID or an alias ID, and provide a search filter expression, a sort expression, or both. If successful, a collection of  GameSession objects matching the request is returned. Use the pagination parameters to retrieve results as a set of sequential pages. 
        
        You can search for game sessions one fleet at a time only. To find game sessions across multiple fleets, you must search each fleet separately and combine the results. This search feature finds only game sessions that are in ``ACTIVE`` status. To locate games in statuses other than active, use  DescribeGameSessionDetails .
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/SearchGameSessions>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_game_sessions(
              FleetId=\'string\',
              AliasId=\'string\',
              FilterExpression=\'string\',
              SortExpression=\'string\',
              Limit=123,
              NextToken=\'string\'
          )
        :type FleetId: string
        :param FleetId: 
        
          Unique identifier for a fleet to search for active game sessions. Each request must reference either a fleet ID or alias ID, but not both.
        
        :type AliasId: string
        :param AliasId: 
        
          Unique identifier for an alias associated with the fleet to search for active game sessions. Each request must reference either a fleet ID or alias ID, but not both.
        
        :type FilterExpression: string
        :param FilterExpression: 
        
          String containing the search criteria for the session search. If no filter expression is included, the request returns results for all game sessions in the fleet that are in ``ACTIVE`` status.
        
          A filter expression can contain one or multiple conditions. Each condition consists of the following:
        
          * **Operand** -- Name of a game session attribute. Valid values are ``gameSessionName`` , ``gameSessionId`` , ``gameSessionProperties`` , ``maximumSessions`` , ``creationTimeMillis`` , ``playerSessionCount`` , ``hasAvailablePlayerSessions`` . 
           
          * **Comparator** -- Valid comparators are: ``=`` , ``<>`` , ``<`` , ``>`` , ``<=`` , ``>=`` .  
           
          * **Value** -- Value to be searched for. Values may be numbers, boolean values (true/false) or strings depending on the operand. String values are case sensitive and must be enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators ``=`` and ``<>`` . For example, the following filter expression searches on ``gameSessionName`` : \"``FilterExpression\": \"gameSessionName = \'Matt\\\'s Awesome Game 1\'\"`` .  
           
          To chain multiple conditions in a single expression, use the logical keywords ``AND`` , ``OR`` , and ``NOT`` and parentheses as needed. For example: ``x AND y AND NOT z`` , ``NOT (x OR y)`` .
        
          Session search evaluates conditions from left to right using the following precedence rules:
        
          * ``=`` , ``<>`` , ``<`` , ``>`` , ``<=`` , ``>=``   
           
          * Parentheses 
           
          * NOT 
           
          * AND 
           
          * OR 
           
          For example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: ``\"maximumSessions>=10 AND hasAvailablePlayerSessions=true\"`` . 
        
        :type SortExpression: string
        :param SortExpression: 
        
          Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:
        
          * **Operand** -- Name of a game session attribute. Valid values are ``gameSessionName`` , ``gameSessionId`` , ``gameSessionProperties`` , ``maximumSessions`` , ``creationTimeMillis`` , ``playerSessionCount`` , ``hasAvailablePlayerSessions`` . 
           
          * **Order** -- Valid sort orders are ``ASC`` (ascending) and ``DESC`` (descending). 
           
          For example, this sort expression returns the oldest active sessions first: ``\"SortExpression\": \"creationTimeMillis ASC\"`` . Results with a null value for the sort operand are returned at the end of the list.
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of results to return. Use this parameter with ``NextToken`` to get results as a set of sequential pages. The maximum number of results returned is 20, even if this value is not set or is set higher than 20. 
        
        :type NextToken: string
        :param NextToken: 
        
          Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessions\': [
                    {
                        \'GameSessionId\': \'string\',
                        \'Name\': \'string\',
                        \'FleetId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'TerminationTime\': datetime(2015, 1, 1),
                        \'CurrentPlayerSessionCount\': 123,
                        \'MaximumPlayerSessionCount\': 123,
                        \'Status\': \'ACTIVE\'|\'ACTIVATING\'|\'TERMINATED\'|\'TERMINATING\'|\'ERROR\',
                        \'StatusReason\': \'INTERRUPTED\',
                        \'GameProperties\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'IpAddress\': \'string\',
                        \'Port\': 123,
                        \'PlayerSessionCreationPolicy\': \'ACCEPT_ALL\'|\'DENY_ALL\',
                        \'CreatorId\': \'string\',
                        \'GameSessionData\': \'string\',
                        \'MatchmakerData\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessions** *(list) --* 
        
              Collection of objects containing game session properties for each session matching the request.
        
              - *(dict) --* 
        
                Properties describing a game session.
        
                A game session in ACTIVE status can host players. When a game session ends, its status is set to ``TERMINATED`` . 
        
                Once the session ends, the game session object is retained for 30 days. This means you can reuse idempotency token values after this time. Game session logs are retained for 14 days.
        
                Game-session-related operations include:
        
                *  CreateGameSession   
                 
                *  DescribeGameSessions   
                 
                *  DescribeGameSessionDetails   
                 
                *  SearchGameSessions   
                 
                *  UpdateGameSession   
                 
                *  GetGameSessionLogUrl   
                 
                * Game session placements 
        
                  *  StartGameSessionPlacement   
                   
                  *  DescribeGameSessionPlacement   
                   
                  *  StopGameSessionPlacement   
                   
                - **GameSessionId** *(string) --* 
        
                  Unique identifier for the game session. A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .
        
                - **Name** *(string) --* 
        
                  Descriptive label that is associated with a game session. Session names do not need to be unique.
        
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that the game session is running on.
        
                - **CreationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **TerminationTime** *(datetime) --* 
        
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
                - **CurrentPlayerSessionCount** *(integer) --* 
        
                  Number of players currently in the game session.
        
                - **MaximumPlayerSessionCount** *(integer) --* 
        
                  Maximum number of players that can be connected simultaneously to the game session.
        
                - **Status** *(string) --* 
        
                  Current status of the game session. A game session must have an ``ACTIVE`` status to have player sessions.
        
                - **StatusReason** *(string) --* 
        
                  Provides additional information about game session status. ``INTERRUPTED`` indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.
        
                - **GameProperties** *(list) --* 
        
                  Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). You can search for active game sessions based on this custom data with  SearchGameSessions .
        
                  - *(dict) --* 
        
                    Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                    - **Key** *(string) --* 
        
                      Game property identifier.
        
                    - **Value** *(string) --* 
        
                      Game property value.
        
                - **IpAddress** *(string) --* 
        
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **Port** *(integer) --* 
        
                  Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **PlayerSessionCreationPolicy** *(string) --* 
        
                  Indicates whether or not the game session is accepting new players.
        
                - **CreatorId** *(string) --* 
        
                  Unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
        
                - **GameSessionData** *(string) --* 
        
                  Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
                - **MatchmakerData** *(string) --* 
        
                  Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ). 
        
            - **NextToken** *(string) --* 
        
              Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.
        
        """
        pass

    def start_fleet_actions(self, FleetId: str, Actions: List) -> Dict:
        """
        
        To start fleet actions, specify the fleet ID and the type of actions to restart. When auto-scaling fleet actions are restarted, Amazon GameLift once again initiates scaling events as triggered by the fleet\'s scaling policies. If actions on the fleet were never stopped, this operation will have no effect. You can view a fleet\'s stopped actions using  DescribeFleetAttributes .
        
        Operations related to fleet capacity scaling include:
        
        *  DescribeFleetCapacity   
         
        *  UpdateFleetCapacity   
         
        *  DescribeEC2InstanceLimits   
         
        * Manage scaling policies: 
        
          *  PutScalingPolicy (auto-scaling) 
           
          *  DescribeScalingPolicies (auto-scaling) 
           
          *  DeleteScalingPolicy (auto-scaling) 
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StartFleetActions>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_fleet_actions(
              FleetId=\'string\',
              Actions=[
                  \'AUTO_SCALING\',
              ]
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet
        
        :type Actions: list
        :param Actions: **[REQUIRED]** 
        
          List of actions to restart on the fleet.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def start_game_session_placement(self, PlacementId: str, GameSessionQueueName: str, MaximumPlayerSessionCount: int, GameProperties: List = None, GameSessionName: str = None, PlayerLatencies: List = None, DesiredPlayerSessions: List = None, GameSessionData: str = None) -> Dict:
        """
        
        A game session placement request can also request player sessions. When a new game session is successfully created, Amazon GameLift creates a player session for each player included in the request.
        
        When placing a game session, by default Amazon GameLift tries each fleet in the order they are listed in the queue configuration. Ideally, a queue\'s destinations are listed in preference order.
        
        Alternatively, when requesting a game session with players, you can also provide latency data for each player in relevant regions. Latency data indicates the performance lag a player experiences when connected to a fleet in the region. Amazon GameLift uses latency data to reorder the list of destinations to place the game session in a region with minimal lag. If latency data is provided for multiple players, Amazon GameLift calculates each region\'s average lag for all players and reorders to get the best game play across all players. 
        
        To place a new game session request, specify the following:
        
        * The queue name and a set of game session properties and settings 
         
        * A unique ID (such as a UUID) for the placement. You use this ID to track the status of the placement request 
         
        * (Optional) A set of IDs and player data for each player you want to join to the new game session 
         
        * Latency data for all players (if you want to optimize game play for the players) 
         
        If successful, a new game session placement is created.
        
        To track the status of a placement request, call  DescribeGameSessionPlacement and check the request\'s status. If the status is ``FULFILLED`` , a new game session has been created and a game session ARN and region are referenced. If the placement request times out, you can resubmit the request or retry it with a different queue. 
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StartGameSessionPlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_game_session_placement(
              PlacementId=\'string\',
              GameSessionQueueName=\'string\',
              GameProperties=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              MaximumPlayerSessionCount=123,
              GameSessionName=\'string\',
              PlayerLatencies=[
                  {
                      \'PlayerId\': \'string\',
                      \'RegionIdentifier\': \'string\',
                      \'LatencyInMilliseconds\': ...
                  },
              ],
              DesiredPlayerSessions=[
                  {
                      \'PlayerId\': \'string\',
                      \'PlayerData\': \'string\'
                  },
              ],
              GameSessionData=\'string\'
          )
        :type PlacementId: string
        :param PlacementId: **[REQUIRED]** 
        
          Unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all regions and cannot be reused unless you are resubmitting a canceled or timed-out placement request.
        
        :type GameSessionQueueName: string
        :param GameSessionQueueName: **[REQUIRED]** 
        
          Name of the queue to use to place the new game session.
        
        :type GameProperties: list
        :param GameProperties: 
        
          Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
          - *(dict) --* 
        
            Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              Game property identifier.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              Game property value.
        
        :type MaximumPlayerSessionCount: integer
        :param MaximumPlayerSessionCount: **[REQUIRED]** 
        
          Maximum number of players that can be connected simultaneously to the game session.
        
        :type GameSessionName: string
        :param GameSessionName: 
        
          Descriptive label that is associated with a game session. Session names do not need to be unique.
        
        :type PlayerLatencies: list
        :param PlayerLatencies: 
        
          Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players. 
        
          - *(dict) --* 
        
            Regional latency information for a player, used when requesting a new game session with  StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified region. The relative difference between a player\'s latency values for multiple regions are used to determine which fleets are best suited to place a new game session for the player. 
        
            - **PlayerId** *(string) --* 
        
              Unique identifier for a player associated with the latency data.
        
            - **RegionIdentifier** *(string) --* 
        
              Name of the region that is associated with the latency value.
        
            - **LatencyInMilliseconds** *(float) --* 
        
              Amount of time that represents the time lag experienced by the player when connected to the specified region.
        
        :type DesiredPlayerSessions: list
        :param DesiredPlayerSessions: 
        
          Set of information on each player to create a player session for.
        
          - *(dict) --* 
        
            Player information for use when creating player sessions using a game session placement request with  StartGameSessionPlacement .
        
            - **PlayerId** *(string) --* 
        
              Unique identifier for a player to associate with the player session.
        
            - **PlayerData** *(string) --* 
        
              Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.
        
        :type GameSessionData: string
        :param GameSessionData: 
        
          Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessionPlacement\': {
                    \'PlacementId\': \'string\',
                    \'GameSessionQueueName\': \'string\',
                    \'Status\': \'PENDING\'|\'FULFILLED\'|\'CANCELLED\'|\'TIMED_OUT\',
                    \'GameProperties\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'MaximumPlayerSessionCount\': 123,
                    \'GameSessionName\': \'string\',
                    \'GameSessionId\': \'string\',
                    \'GameSessionArn\': \'string\',
                    \'GameSessionRegion\': \'string\',
                    \'PlayerLatencies\': [
                        {
                            \'PlayerId\': \'string\',
                            \'RegionIdentifier\': \'string\',
                            \'LatencyInMilliseconds\': ...
                        },
                    ],
                    \'StartTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'IpAddress\': \'string\',
                    \'Port\': 123,
                    \'PlacedPlayerSessions\': [
                        {
                            \'PlayerId\': \'string\',
                            \'PlayerSessionId\': \'string\'
                        },
                    ],
                    \'GameSessionData\': \'string\',
                    \'MatchmakerData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessionPlacement** *(dict) --* 
        
              Object that describes the newly created game session placement. This object includes all the information provided in the request, as well as start/end time stamps and placement status. 
        
              - **PlacementId** *(string) --* 
        
                Unique identifier for a game session placement.
        
              - **GameSessionQueueName** *(string) --* 
        
                Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
              - **Status** *(string) --* 
        
                Current status of the game session placement request.
        
                * **PENDING** -- The placement request is currently in the queue waiting to be processed. 
                 
                * **FULFILLED** -- A new game session and player sessions (if requested) have been successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.  
                 
                * **CANCELLED** -- The placement request was canceled with a call to  StopGameSessionPlacement . 
                 
                * **TIMED_OUT** -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed. 
                 
              - **GameProperties** *(list) --* 
        
                Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
                - *(dict) --* 
        
                  Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                  - **Key** *(string) --* 
        
                    Game property identifier.
        
                  - **Value** *(string) --* 
        
                    Game property value.
        
              - **MaximumPlayerSessionCount** *(integer) --* 
        
                Maximum number of players that can be connected simultaneously to the game session.
        
              - **GameSessionName** *(string) --* 
        
                Descriptive label that is associated with a game session. Session names do not need to be unique.
        
              - **GameSessionId** *(string) --* 
        
                Unique identifier for the game session. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **GameSessionArn** *(string) --* 
        
                Identifier for the game session created by this placement request. This value is set once the new game session is placed (placement status is ``FULFILLED`` ). This identifier is unique across all regions. You can use this value as a ``GameSessionId`` value as needed.
        
              - **GameSessionRegion** *(string) --* 
        
                Name of the region where the game session created by this placement request is running. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **PlayerLatencies** *(list) --* 
        
                Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions.
        
                - *(dict) --* 
        
                  Regional latency information for a player, used when requesting a new game session with  StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified region. The relative difference between a player\'s latency values for multiple regions are used to determine which fleets are best suited to place a new game session for the player. 
        
                  - **PlayerId** *(string) --* 
        
                    Unique identifier for a player associated with the latency data.
        
                  - **RegionIdentifier** *(string) --* 
        
                    Name of the region that is associated with the latency value.
        
                  - **LatencyInMilliseconds** *(float) --* 
        
                    Amount of time that represents the time lag experienced by the player when connected to the specified region.
        
              - **StartTime** *(datetime) --* 
        
                Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **EndTime** *(datetime) --* 
        
                Time stamp indicating when this request was completed, canceled, or timed out.
        
              - **IpAddress** *(string) --* 
        
                IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is ``FULFILLED`` ). 
        
              - **Port** *(integer) --* 
        
                Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **PlacedPlayerSessions** *(list) --* 
        
                Collection of information on player sessions created in response to the game session placement request. These player sessions are created only once a new game session is successfully placed (placement status is ``FULFILLED`` ). This information includes the player ID (as provided in the placement request) and the corresponding player session ID. Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.
        
                - *(dict) --* 
        
                  Information about a player session that was created as part of a  StartGameSessionPlacement request. This object contains only the player ID and player session ID. To retrieve full details on a player session, call  DescribePlayerSessions with the player session ID.
        
                  Player-session-related operations include:
        
                  *  CreatePlayerSession   
                   
                  *  CreatePlayerSessions   
                   
                  *  DescribePlayerSessions   
                   
                  * Game session placements 
        
                    *  StartGameSessionPlacement   
                     
                    *  DescribeGameSessionPlacement   
                     
                    *  StopGameSessionPlacement   
                     
                  - **PlayerId** *(string) --* 
        
                    Unique identifier for a player that is associated with this player session.
        
                  - **PlayerSessionId** *(string) --* 
        
                    Unique identifier for a player session.
        
              - **GameSessionData** *(string) --* 
        
                Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
              - **MatchmakerData** *(string) --* 
        
                Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ .
        
        """
        pass

    def start_match_backfill(self, ConfigurationName: str, GameSessionArn: str, Players: List, TicketId: str = None) -> Dict:
        """
        
        To request a match backfill, specify a unique ticket ID, the existing game session\'s ARN, a matchmaking configuration, and a set of data that describes all current players in the game session. If successful, a match backfill ticket is created and returned with status set to QUEUED. The ticket is placed in the matchmaker\'s ticket pool and processed. Track the status of the ticket to respond as needed. For more detail how to set up backfilling, see `Backfill Existing Games with FlexMatch <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ . 
        
        The process of finding backfill matches is essentially identical to the initial matchmaking process. The matchmaker searches the pool and groups tickets together to form potential matches, allowing only one backfill ticket per potential match. Once the a match is formed, the matchmaker creates player sessions for the new players. All tickets in the match are updated with the game session\'s connection information, and the  GameSession object is updated to include matchmaker data on the new players. For more detail on how match backfill requests are processed, see `How Amazon GameLift FlexMatch Works <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-intro.html>`__ . 
        
        Matchmaking-related operations include:
        
        *  StartMatchmaking   
         
        *  DescribeMatchmaking   
         
        *  StopMatchmaking   
         
        *  AcceptMatch   
         
        *  StartMatchBackfill   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StartMatchBackfill>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_match_backfill(
              TicketId=\'string\',
              ConfigurationName=\'string\',
              GameSessionArn=\'string\',
              Players=[
                  {
                      \'PlayerId\': \'string\',
                      \'PlayerAttributes\': {
                          \'string\': {
                              \'S\': \'string\',
                              \'N\': 123.0,
                              \'SL\': [
                                  \'string\',
                              ],
                              \'SDM\': {
                                  \'string\': 123.0
                              }
                          }
                      },
                      \'Team\': \'string\',
                      \'LatencyInMs\': {
                          \'string\': 123
                      }
                  },
              ]
          )
        :type TicketId: string
        :param TicketId: 
        
          Unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results.
        
        :type ConfigurationName: string
        :param ConfigurationName: **[REQUIRED]** 
        
          Name of the matchmaker to use for this request. The name of the matchmaker that was used with the original game session is listed in the  GameSession object, ``MatchmakerData`` property. This property contains a matchmaking configuration ARN value, which includes the matchmaker name. (In the ARN value \"arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MM-4v4\", the matchmaking configuration name is \"MM-4v4\".) Use only the name for this parameter.
        
        :type GameSessionArn: string
        :param GameSessionArn: **[REQUIRED]** 
        
          Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session and uniquely identifies it. 
        
        :type Players: list
        :param Players: **[REQUIRED]** 
        
          Match information on all players that are currently assigned to the game session. This information is used by the matchmaker to find new players and add them to the existing game.
        
          * PlayerID, PlayerAttributes, Team -\\- This information is maintained in the  GameSession object, ``MatchmakerData`` property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ .  
           
          * LatencyInMs -\\- If the matchmaker uses player latency, include a latency value, in milliseconds, for the region that the game session is currently in. Do not include latency values for any other region. 
           
          - *(dict) --* 
        
            Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
        
            - **PlayerId** *(string) --* 
        
              Unique identifier for a player
        
            - **PlayerAttributes** *(dict) --* 
        
              Collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example: ``\"PlayerAttributes\": {\"skill\": {\"N\": \"23\"}, \"gameMode\": {\"S\": \"deathmatch\"}}`` .
        
              - *(string) --* 
        
                - *(dict) --* 
        
                  Values for use in  Player attribute key:value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array or data map. Each ``AttributeValue`` object can use only one of the available properties.
        
                  - **S** *(string) --* 
        
                    For single string values. Maximum string length is 100 characters.
        
                  - **N** *(float) --* 
        
                    For number values, expressed as double.
        
                  - **SL** *(list) --* 
        
                    For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
        
                    - *(string) --* 
        
                  - **SDM** *(dict) --* 
        
                    For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters. 
        
                    - *(string) --* 
        
                      - *(float) --* 
        
            - **Team** *(string) --* 
        
              Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
        
            - **LatencyInMs** *(dict) --* 
        
              Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. If this property is present, FlexMatch considers placing the match only in regions for which latency is reported. 
        
              If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no regions are available to the player and the ticket is not matchable. 
        
              - *(string) --* 
        
                - *(integer) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'MatchmakingTicket\': {
                    \'TicketId\': \'string\',
                    \'ConfigurationName\': \'string\',
                    \'Status\': \'CANCELLED\'|\'COMPLETED\'|\'FAILED\'|\'PLACING\'|\'QUEUED\'|\'REQUIRES_ACCEPTANCE\'|\'SEARCHING\'|\'TIMED_OUT\',
                    \'StatusReason\': \'string\',
                    \'StatusMessage\': \'string\',
                    \'StartTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'Players\': [
                        {
                            \'PlayerId\': \'string\',
                            \'PlayerAttributes\': {
                                \'string\': {
                                    \'S\': \'string\',
                                    \'N\': 123.0,
                                    \'SL\': [
                                        \'string\',
                                    ],
                                    \'SDM\': {
                                        \'string\': 123.0
                                    }
                                }
                            },
                            \'Team\': \'string\',
                            \'LatencyInMs\': {
                                \'string\': 123
                            }
                        },
                    ],
                    \'GameSessionConnectionInfo\': {
                        \'GameSessionArn\': \'string\',
                        \'IpAddress\': \'string\',
                        \'Port\': 123,
                        \'MatchedPlayerSessions\': [
                            {
                                \'PlayerId\': \'string\',
                                \'PlayerSessionId\': \'string\'
                            },
                        ]
                    },
                    \'EstimatedWaitTime\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **MatchmakingTicket** *(dict) --* 
        
              Ticket representing the backfill matchmaking request. This object includes the information in the request, ticket status, and match results as generated during the matchmaking process.
        
              - **TicketId** *(string) --* 
        
                Unique identifier for a matchmaking ticket.
        
              - **ConfigurationName** *(string) --* 
        
                Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.
        
              - **Status** *(string) --* 
        
                Current status of the matchmaking request.
        
                * **QUEUED** -- The matchmaking request has been received and is currently waiting to be processed. 
                 
                * **SEARCHING** -- The matchmaking request is currently being processed.  
                 
                * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the match (see  AcceptMatch ). This status is used only with requests that use a matchmaking configuration with a player acceptance requirement. 
                 
                * **PLACING** -- The FlexMatch engine has matched players and is in the process of placing a new game session for the match. 
                 
                * **COMPLETED** -- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players. 
                 
                * **FAILED** -- The matchmaking request was not completed. Tickets with players who fail to accept a proposed match are placed in ``FAILED`` status. 
                 
                * **CANCELLED** -- The matchmaking request was canceled with a call to  StopMatchmaking . 
                 
                * **TIMED_OUT** -- The matchmaking request was not successful within the duration specified in the matchmaking configuration.  
                 
                .. note::
        
                  Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket IDs.
        
              - **StatusReason** *(string) --* 
        
                Code to explain the current status. For example, a status reason may indicate when a ticket has returned to ``SEARCHING`` status after a proposed match fails to receive player acceptances.
        
              - **StatusMessage** *(string) --* 
        
                Additional information about the current status.
        
              - **StartTime** *(datetime) --* 
        
                Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **EndTime** *(datetime) --* 
        
                Time stamp indicating when this matchmaking request stopped being processed due to success, failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **Players** *(list) --* 
        
                A set of ``Player`` objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the players were assigned to in the resulting match.
        
                - *(dict) --* 
        
                  Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
        
                  - **PlayerId** *(string) --* 
        
                    Unique identifier for a player
        
                  - **PlayerAttributes** *(dict) --* 
        
                    Collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example: ``\"PlayerAttributes\": {\"skill\": {\"N\": \"23\"}, \"gameMode\": {\"S\": \"deathmatch\"}}`` .
        
                    - *(string) --* 
                      
                      - *(dict) --* 
        
                        Values for use in  Player attribute key:value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array or data map. Each ``AttributeValue`` object can use only one of the available properties.
        
                        - **S** *(string) --* 
        
                          For single string values. Maximum string length is 100 characters.
        
                        - **N** *(float) --* 
        
                          For number values, expressed as double.
        
                        - **SL** *(list) --* 
        
                          For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
        
                          - *(string) --* 
                      
                        - **SDM** *(dict) --* 
        
                          For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters. 
        
                          - *(string) --* 
                            
                            - *(float) --* 
                      
                  - **Team** *(string) --* 
        
                    Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
        
                  - **LatencyInMs** *(dict) --* 
        
                    Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. If this property is present, FlexMatch considers placing the match only in regions for which latency is reported. 
        
                    If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no regions are available to the player and the ticket is not matchable. 
        
                    - *(string) --* 
                      
                      - *(integer) --* 
                
              - **GameSessionConnectionInfo** *(dict) --* 
        
                Identifier and connection information of the game session created for the match. This information is added to the ticket only after the matchmaking request has been successfully completed.
        
                - **GameSessionArn** *(string) --* 
        
                  Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session and uniquely identifies it.
        
                - **IpAddress** *(string) --* 
        
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **Port** *(integer) --* 
        
                  Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **MatchedPlayerSessions** *(list) --* 
        
                  Collection of player session IDs, one for each player ID that was included in the original matchmaking request. 
        
                  - *(dict) --* 
        
                    Represents a new player session that is created as a result of a successful FlexMatch match. A successful match automatically creates new player sessions for every player ID in the original matchmaking request. 
        
                    When players connect to the match\'s game session, they must include both player ID and player session ID in order to claim their assigned player slot.
        
                    - **PlayerId** *(string) --* 
        
                      Unique identifier for a player 
        
                    - **PlayerSessionId** *(string) --* 
        
                      Unique identifier for a player session
        
              - **EstimatedWaitTime** *(integer) --* 
        
                Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.
        
        """
        pass

    def start_matchmaking(self, ConfigurationName: str, Players: List, TicketId: str = None) -> Dict:
        """
        
        To start matchmaking, provide a unique ticket ID, specify a matchmaking configuration, and include the players to be matched. You must also include a set of player attributes relevant for the matchmaking configuration. If successful, a matchmaking ticket is returned with status set to ``QUEUED`` . Track the status of the ticket to respond as needed and acquire game session connection information for successfully completed matches.
        
         **Tracking ticket status** -- A couple of options are available for tracking the status of matchmaking requests: 
        
        * Polling -- Call ``DescribeMatchmaking`` . This operation returns the full ticket object, including current status and (for completed tickets) game session connection info. We recommend polling no more than once every 10 seconds. 
         
        * Notifications -- Get event notifications for changes in ticket status using Amazon Simple Notification Service (SNS). Notifications are easy to set up (see  CreateMatchmakingConfiguration ) and typically deliver match status changes faster and more efficiently than polling. We recommend that you use polling to back up to notifications (since delivery is not guaranteed) and call ``DescribeMatchmaking`` only when notifications are not received within 30 seconds. 
         
         **Processing a matchmaking request** -- FlexMatch handles a matchmaking request as follows: 
        
        * Your client code submits a ``StartMatchmaking`` request for one or more players and tracks the status of the request ticket.  
         
        * FlexMatch uses this ticket and others in process to build an acceptable match. When a potential match is identified, all tickets in the proposed match are advanced to the next status.  
         
        * If the match requires player acceptance (set in the matchmaking configuration), the tickets move into status ``REQUIRES_ACCEPTANCE`` . This status triggers your client code to solicit acceptance from all players in every ticket involved in the match, and then call  AcceptMatch for each player. If any player rejects or fails to accept the match before a specified timeout, the proposed match is dropped (see ``AcceptMatch`` for more details). 
         
        * Once a match is proposed and accepted, the matchmaking tickets move into status ``PLACING`` . FlexMatch locates resources for a new game session using the game session queue (set in the matchmaking configuration) and creates the game session based on the match data.  
         
        * When the match is successfully placed, the matchmaking tickets move into ``COMPLETED`` status. Connection information (including game session endpoint and player session) is added to the matchmaking tickets. Matched players can use the connection information to join the game.  
         
        Matchmaking-related operations include:
        
        *  StartMatchmaking   
         
        *  DescribeMatchmaking   
         
        *  StopMatchmaking   
         
        *  AcceptMatch   
         
        *  StartMatchBackfill   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StartMatchmaking>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_matchmaking(
              TicketId=\'string\',
              ConfigurationName=\'string\',
              Players=[
                  {
                      \'PlayerId\': \'string\',
                      \'PlayerAttributes\': {
                          \'string\': {
                              \'S\': \'string\',
                              \'N\': 123.0,
                              \'SL\': [
                                  \'string\',
                              ],
                              \'SDM\': {
                                  \'string\': 123.0
                              }
                          }
                      },
                      \'Team\': \'string\',
                      \'LatencyInMs\': {
                          \'string\': 123
                      }
                  },
              ]
          )
        :type TicketId: string
        :param TicketId: 
        
          Unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the matchmaking ticket status and retrieve match results.
        
        :type ConfigurationName: string
        :param ConfigurationName: **[REQUIRED]** 
        
          Name of the matchmaking configuration to use for this request. Matchmaking configurations must exist in the same region as this request.
        
        :type Players: list
        :param Players: **[REQUIRED]** 
        
          Information on each player to be matched. This information must include a player ID, and may contain player attributes and latency data to be used in the matchmaking process. After a successful match, ``Player`` objects contain the name of the team the player is assigned to.
        
          - *(dict) --* 
        
            Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
        
            - **PlayerId** *(string) --* 
        
              Unique identifier for a player
        
            - **PlayerAttributes** *(dict) --* 
        
              Collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example: ``\"PlayerAttributes\": {\"skill\": {\"N\": \"23\"}, \"gameMode\": {\"S\": \"deathmatch\"}}`` .
        
              - *(string) --* 
        
                - *(dict) --* 
        
                  Values for use in  Player attribute key:value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array or data map. Each ``AttributeValue`` object can use only one of the available properties.
        
                  - **S** *(string) --* 
        
                    For single string values. Maximum string length is 100 characters.
        
                  - **N** *(float) --* 
        
                    For number values, expressed as double.
        
                  - **SL** *(list) --* 
        
                    For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
        
                    - *(string) --* 
        
                  - **SDM** *(dict) --* 
        
                    For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters. 
        
                    - *(string) --* 
        
                      - *(float) --* 
        
            - **Team** *(string) --* 
        
              Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
        
            - **LatencyInMs** *(dict) --* 
        
              Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. If this property is present, FlexMatch considers placing the match only in regions for which latency is reported. 
        
              If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no regions are available to the player and the ticket is not matchable. 
        
              - *(string) --* 
        
                - *(integer) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'MatchmakingTicket\': {
                    \'TicketId\': \'string\',
                    \'ConfigurationName\': \'string\',
                    \'Status\': \'CANCELLED\'|\'COMPLETED\'|\'FAILED\'|\'PLACING\'|\'QUEUED\'|\'REQUIRES_ACCEPTANCE\'|\'SEARCHING\'|\'TIMED_OUT\',
                    \'StatusReason\': \'string\',
                    \'StatusMessage\': \'string\',
                    \'StartTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'Players\': [
                        {
                            \'PlayerId\': \'string\',
                            \'PlayerAttributes\': {
                                \'string\': {
                                    \'S\': \'string\',
                                    \'N\': 123.0,
                                    \'SL\': [
                                        \'string\',
                                    ],
                                    \'SDM\': {
                                        \'string\': 123.0
                                    }
                                }
                            },
                            \'Team\': \'string\',
                            \'LatencyInMs\': {
                                \'string\': 123
                            }
                        },
                    ],
                    \'GameSessionConnectionInfo\': {
                        \'GameSessionArn\': \'string\',
                        \'IpAddress\': \'string\',
                        \'Port\': 123,
                        \'MatchedPlayerSessions\': [
                            {
                                \'PlayerId\': \'string\',
                                \'PlayerSessionId\': \'string\'
                            },
                        ]
                    },
                    \'EstimatedWaitTime\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **MatchmakingTicket** *(dict) --* 
        
              Ticket representing the matchmaking request. This object include the information included in the request, ticket status, and match results as generated during the matchmaking process.
        
              - **TicketId** *(string) --* 
        
                Unique identifier for a matchmaking ticket.
        
              - **ConfigurationName** *(string) --* 
        
                Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.
        
              - **Status** *(string) --* 
        
                Current status of the matchmaking request.
        
                * **QUEUED** -- The matchmaking request has been received and is currently waiting to be processed. 
                 
                * **SEARCHING** -- The matchmaking request is currently being processed.  
                 
                * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the match (see  AcceptMatch ). This status is used only with requests that use a matchmaking configuration with a player acceptance requirement. 
                 
                * **PLACING** -- The FlexMatch engine has matched players and is in the process of placing a new game session for the match. 
                 
                * **COMPLETED** -- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players. 
                 
                * **FAILED** -- The matchmaking request was not completed. Tickets with players who fail to accept a proposed match are placed in ``FAILED`` status. 
                 
                * **CANCELLED** -- The matchmaking request was canceled with a call to  StopMatchmaking . 
                 
                * **TIMED_OUT** -- The matchmaking request was not successful within the duration specified in the matchmaking configuration.  
                 
                .. note::
        
                  Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket IDs.
        
              - **StatusReason** *(string) --* 
        
                Code to explain the current status. For example, a status reason may indicate when a ticket has returned to ``SEARCHING`` status after a proposed match fails to receive player acceptances.
        
              - **StatusMessage** *(string) --* 
        
                Additional information about the current status.
        
              - **StartTime** *(datetime) --* 
        
                Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **EndTime** *(datetime) --* 
        
                Time stamp indicating when this matchmaking request stopped being processed due to success, failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **Players** *(list) --* 
        
                A set of ``Player`` objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the players were assigned to in the resulting match.
        
                - *(dict) --* 
        
                  Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
        
                  - **PlayerId** *(string) --* 
        
                    Unique identifier for a player
        
                  - **PlayerAttributes** *(dict) --* 
        
                    Collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example: ``\"PlayerAttributes\": {\"skill\": {\"N\": \"23\"}, \"gameMode\": {\"S\": \"deathmatch\"}}`` .
        
                    - *(string) --* 
                      
                      - *(dict) --* 
        
                        Values for use in  Player attribute key:value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array or data map. Each ``AttributeValue`` object can use only one of the available properties.
        
                        - **S** *(string) --* 
        
                          For single string values. Maximum string length is 100 characters.
        
                        - **N** *(float) --* 
        
                          For number values, expressed as double.
        
                        - **SL** *(list) --* 
        
                          For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
        
                          - *(string) --* 
                      
                        - **SDM** *(dict) --* 
        
                          For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters. 
        
                          - *(string) --* 
                            
                            - *(float) --* 
                      
                  - **Team** *(string) --* 
        
                    Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
        
                  - **LatencyInMs** *(dict) --* 
        
                    Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. If this property is present, FlexMatch considers placing the match only in regions for which latency is reported. 
        
                    If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no regions are available to the player and the ticket is not matchable. 
        
                    - *(string) --* 
                      
                      - *(integer) --* 
                
              - **GameSessionConnectionInfo** *(dict) --* 
        
                Identifier and connection information of the game session created for the match. This information is added to the ticket only after the matchmaking request has been successfully completed.
        
                - **GameSessionArn** *(string) --* 
        
                  Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session and uniquely identifies it.
        
                - **IpAddress** *(string) --* 
        
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **Port** *(integer) --* 
        
                  Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
                - **MatchedPlayerSessions** *(list) --* 
        
                  Collection of player session IDs, one for each player ID that was included in the original matchmaking request. 
        
                  - *(dict) --* 
        
                    Represents a new player session that is created as a result of a successful FlexMatch match. A successful match automatically creates new player sessions for every player ID in the original matchmaking request. 
        
                    When players connect to the match\'s game session, they must include both player ID and player session ID in order to claim their assigned player slot.
        
                    - **PlayerId** *(string) --* 
        
                      Unique identifier for a player 
        
                    - **PlayerSessionId** *(string) --* 
        
                      Unique identifier for a player session
        
              - **EstimatedWaitTime** *(integer) --* 
        
                Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.
        
        """
        pass

    def stop_fleet_actions(self, FleetId: str, Actions: List) -> Dict:
        """
        
        To stop fleet actions, specify the fleet ID and the type of actions to suspend. When auto-scaling fleet actions are stopped, Amazon GameLift no longer initiates scaling events except to maintain the fleet\'s desired instances setting ( FleetCapacity . Changes to the fleet\'s capacity must be done manually using  UpdateFleetCapacity . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StopFleetActions>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_fleet_actions(
              FleetId=\'string\',
              Actions=[
                  \'AUTO_SCALING\',
              ]
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet
        
        :type Actions: list
        :param Actions: **[REQUIRED]** 
        
          List of actions to suspend on the fleet. 
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def stop_game_session_placement(self, PlacementId: str) -> Dict:
        """
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StopGameSessionPlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_game_session_placement(
              PlacementId=\'string\'
          )
        :type PlacementId: string
        :param PlacementId: **[REQUIRED]** 
        
          Unique identifier for a game session placement to cancel.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessionPlacement\': {
                    \'PlacementId\': \'string\',
                    \'GameSessionQueueName\': \'string\',
                    \'Status\': \'PENDING\'|\'FULFILLED\'|\'CANCELLED\'|\'TIMED_OUT\',
                    \'GameProperties\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'MaximumPlayerSessionCount\': 123,
                    \'GameSessionName\': \'string\',
                    \'GameSessionId\': \'string\',
                    \'GameSessionArn\': \'string\',
                    \'GameSessionRegion\': \'string\',
                    \'PlayerLatencies\': [
                        {
                            \'PlayerId\': \'string\',
                            \'RegionIdentifier\': \'string\',
                            \'LatencyInMilliseconds\': ...
                        },
                    ],
                    \'StartTime\': datetime(2015, 1, 1),
                    \'EndTime\': datetime(2015, 1, 1),
                    \'IpAddress\': \'string\',
                    \'Port\': 123,
                    \'PlacedPlayerSessions\': [
                        {
                            \'PlayerId\': \'string\',
                            \'PlayerSessionId\': \'string\'
                        },
                    ],
                    \'GameSessionData\': \'string\',
                    \'MatchmakerData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessionPlacement** *(dict) --* 
        
              Object that describes the canceled game session placement, with ``CANCELLED`` status and an end time stamp. 
        
              - **PlacementId** *(string) --* 
        
                Unique identifier for a game session placement.
        
              - **GameSessionQueueName** *(string) --* 
        
                Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
              - **Status** *(string) --* 
        
                Current status of the game session placement request.
        
                * **PENDING** -- The placement request is currently in the queue waiting to be processed. 
                 
                * **FULFILLED** -- A new game session and player sessions (if requested) have been successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.  
                 
                * **CANCELLED** -- The placement request was canceled with a call to  StopGameSessionPlacement . 
                 
                * **TIMED_OUT** -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed. 
                 
              - **GameProperties** *(list) --* 
        
                Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
                - *(dict) --* 
        
                  Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                  - **Key** *(string) --* 
        
                    Game property identifier.
        
                  - **Value** *(string) --* 
        
                    Game property value.
        
              - **MaximumPlayerSessionCount** *(integer) --* 
        
                Maximum number of players that can be connected simultaneously to the game session.
        
              - **GameSessionName** *(string) --* 
        
                Descriptive label that is associated with a game session. Session names do not need to be unique.
        
              - **GameSessionId** *(string) --* 
        
                Unique identifier for the game session. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **GameSessionArn** *(string) --* 
        
                Identifier for the game session created by this placement request. This value is set once the new game session is placed (placement status is ``FULFILLED`` ). This identifier is unique across all regions. You can use this value as a ``GameSessionId`` value as needed.
        
              - **GameSessionRegion** *(string) --* 
        
                Name of the region where the game session created by this placement request is running. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **PlayerLatencies** *(list) --* 
        
                Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions.
        
                - *(dict) --* 
        
                  Regional latency information for a player, used when requesting a new game session with  StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified region. The relative difference between a player\'s latency values for multiple regions are used to determine which fleets are best suited to place a new game session for the player. 
        
                  - **PlayerId** *(string) --* 
        
                    Unique identifier for a player associated with the latency data.
        
                  - **RegionIdentifier** *(string) --* 
        
                    Name of the region that is associated with the latency value.
        
                  - **LatencyInMilliseconds** *(float) --* 
        
                    Amount of time that represents the time lag experienced by the player when connected to the specified region.
        
              - **StartTime** *(datetime) --* 
        
                Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **EndTime** *(datetime) --* 
        
                Time stamp indicating when this request was completed, canceled, or timed out.
        
              - **IpAddress** *(string) --* 
        
                IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is ``FULFILLED`` ). 
        
              - **Port** *(integer) --* 
        
                Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is ``FULFILLED`` ).
        
              - **PlacedPlayerSessions** *(list) --* 
        
                Collection of information on player sessions created in response to the game session placement request. These player sessions are created only once a new game session is successfully placed (placement status is ``FULFILLED`` ). This information includes the player ID (as provided in the placement request) and the corresponding player session ID. Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.
        
                - *(dict) --* 
        
                  Information about a player session that was created as part of a  StartGameSessionPlacement request. This object contains only the player ID and player session ID. To retrieve full details on a player session, call  DescribePlayerSessions with the player session ID.
        
                  Player-session-related operations include:
        
                  *  CreatePlayerSession   
                   
                  *  CreatePlayerSessions   
                   
                  *  DescribePlayerSessions   
                   
                  * Game session placements 
        
                    *  StartGameSessionPlacement   
                     
                    *  DescribeGameSessionPlacement   
                     
                    *  StopGameSessionPlacement   
                     
                  - **PlayerId** *(string) --* 
        
                    Unique identifier for a player that is associated with this player session.
        
                  - **PlayerSessionId** *(string) --* 
        
                    Unique identifier for a player session.
        
              - **GameSessionData** *(string) --* 
        
                Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
              - **MatchmakerData** *(string) --* 
        
                Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ .
        
        """
        pass

    def stop_matchmaking(self, TicketId: str) -> Dict:
        """
        
        Matchmaking-related operations include:
        
        *  StartMatchmaking   
         
        *  DescribeMatchmaking   
         
        *  StopMatchmaking   
         
        *  AcceptMatch   
         
        *  StartMatchBackfill   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StopMatchmaking>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_matchmaking(
              TicketId=\'string\'
          )
        :type TicketId: string
        :param TicketId: **[REQUIRED]** 
        
          Unique identifier for a matchmaking ticket.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_alias(self, AliasId: str, Name: str = None, Description: str = None, RoutingStrategy: Dict = None) -> Dict:
        """
        
        Alias-related operations include:
        
        *  CreateAlias   
         
        *  ListAliases   
         
        *  DescribeAlias   
         
        *  UpdateAlias   
         
        *  DeleteAlias   
         
        *  ResolveAlias   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_alias(
              AliasId=\'string\',
              Name=\'string\',
              Description=\'string\',
              RoutingStrategy={
                  \'Type\': \'SIMPLE\'|\'TERMINAL\',
                  \'FleetId\': \'string\',
                  \'Message\': \'string\'
              }
          )
        :type AliasId: string
        :param AliasId: **[REQUIRED]** 
        
          Unique identifier for a fleet alias. Specify the alias you want to update.
        
        :type Name: string
        :param Name: 
        
          Descriptive label that is associated with an alias. Alias names do not need to be unique.
        
        :type Description: string
        :param Description: 
        
          Human-readable description of an alias.
        
        :type RoutingStrategy: dict
        :param RoutingStrategy: 
        
          Object that specifies the fleet and routing type to use for the alias.
        
          - **Type** *(string) --* 
        
            Type of routing strategy.
        
            Possible routing types include the following:
        
            * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets. 
             
            * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded. 
             
          - **FleetId** *(string) --* 
        
            Unique identifier for a fleet that the alias points to.
        
          - **Message** *(string) --* 
        
            Message text to be used with a terminal routing strategy.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Alias\': {
                    \'AliasId\': \'string\',
                    \'Name\': \'string\',
                    \'AliasArn\': \'string\',
                    \'Description\': \'string\',
                    \'RoutingStrategy\': {
                        \'Type\': \'SIMPLE\'|\'TERMINAL\',
                        \'FleetId\': \'string\',
                        \'Message\': \'string\'
                    },
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'LastUpdatedTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Alias** *(dict) --* 
        
              Object that contains the updated alias configuration.
        
              - **AliasId** *(string) --* 
        
                Unique identifier for an alias; alias IDs are unique within a region.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with an alias. Alias names do not need to be unique.
        
              - **AliasArn** *(string) --* 
        
                Unique identifier for an alias; alias ARNs are unique across all regions.
        
              - **Description** *(string) --* 
        
                Human-readable description of an alias.
        
              - **RoutingStrategy** *(dict) --* 
        
                Alias configuration for the alias, including routing type and settings.
        
                - **Type** *(string) --* 
        
                  Type of routing strategy.
        
                  Possible routing types include the following:
        
                  * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets. 
                   
                  * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded. 
                   
                - **FleetId** *(string) --* 
        
                  Unique identifier for a fleet that the alias points to.
        
                - **Message** *(string) --* 
        
                  Message text to be used with a terminal routing strategy.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **LastUpdatedTime** *(datetime) --* 
        
                Time stamp indicating when this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
        """
        pass

    def update_build(self, BuildId: str, Name: str = None, Version: str = None) -> Dict:
        """
        
        Build-related operations include:
        
        *  CreateBuild   
         
        *  ListBuilds   
         
        *  DescribeBuild   
         
        *  UpdateBuild   
         
        *  DeleteBuild   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateBuild>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_build(
              BuildId=\'string\',
              Name=\'string\',
              Version=\'string\'
          )
        :type BuildId: string
        :param BuildId: **[REQUIRED]** 
        
          Unique identifier for a build to update.
        
        :type Name: string
        :param Name: 
        
          Descriptive label that is associated with a build. Build names do not need to be unique. 
        
        :type Version: string
        :param Version: 
        
          Version that is associated with this build. Version strings do not need to be unique.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Build\': {
                    \'BuildId\': \'string\',
                    \'Name\': \'string\',
                    \'Version\': \'string\',
                    \'Status\': \'INITIALIZED\'|\'READY\'|\'FAILED\',
                    \'SizeOnDisk\': 123,
                    \'OperatingSystem\': \'WINDOWS_2012\'|\'AMAZON_LINUX\',
                    \'CreationTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Build** *(dict) --* 
        
              Object that contains the updated build record.
        
              - **BuildId** *(string) --* 
        
                Unique identifier for a build.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .
        
              - **Version** *(string) --* 
        
                Version that is associated with this build. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .
        
              - **Status** *(string) --* 
        
                Current status of the build.
        
                Possible build statuses include the following:
        
                * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.  
                 
                * **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build. 
                 
                * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.  
                 
              - **SizeOnDisk** *(integer) --* 
        
                File size of the uploaded game build, expressed in bytes. When the build status is ``INITIALIZED`` , this value is 0.
        
              - **OperatingSystem** *(string) --* 
        
                Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
        """
        pass

    def update_fleet_attributes(self, FleetId: str, Name: str = None, Description: str = None, NewGameSessionProtectionPolicy: str = None, ResourceCreationLimitPolicy: Dict = None, MetricGroups: List = None) -> Dict:
        """
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateFleetAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_fleet_attributes(
              FleetId=\'string\',
              Name=\'string\',
              Description=\'string\',
              NewGameSessionProtectionPolicy=\'NoProtection\'|\'FullProtection\',
              ResourceCreationLimitPolicy={
                  \'NewGameSessionsPerCreator\': 123,
                  \'PolicyPeriodInMinutes\': 123
              },
              MetricGroups=[
                  \'string\',
              ]
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to update attribute metadata for.
        
        :type Name: string
        :param Name: 
        
          Descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        
        :type Description: string
        :param Description: 
        
          Human-readable description of a fleet.
        
        :type NewGameSessionProtectionPolicy: string
        :param NewGameSessionProtectionPolicy: 
        
          Game session protection policy to apply to all new instances created in this fleet. Instances that already exist are not affected. You can set protection for individual instances using  UpdateGameSession .
        
          * **NoProtection** -- The game session can be terminated during a scale-down event. 
           
          * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be terminated during a scale-down event. 
           
        :type ResourceCreationLimitPolicy: dict
        :param ResourceCreationLimitPolicy: 
        
          Policy that limits the number of game sessions an individual player can create over a span of time. 
        
          - **NewGameSessionsPerCreator** *(integer) --* 
        
            Maximum number of game sessions that an individual can create during the policy period. 
        
          - **PolicyPeriodInMinutes** *(integer) --* 
        
            Time span used in evaluating the resource creation limit policy. 
        
        :type MetricGroups: list
        :param MetricGroups: 
        
          Names of metric groups to include this fleet in. Amazon CloudWatch uses a fleet metric group is to aggregate metrics from multiple fleets. Use an existing metric group name to add this fleet to the group. Or use a new name to create a new metric group. A fleet can only be included in one metric group at a time.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetId** *(string) --* 
        
              Unique identifier for a fleet that was updated.
        
        """
        pass

    def update_fleet_capacity(self, FleetId: str, DesiredInstances: int = None, MinSize: int = None, MaxSize: int = None) -> Dict:
        """
        
        Specify minimum and maximum number of instances. Amazon GameLift will not change fleet capacity to values fall outside of this range. This is particularly important when using auto-scaling (see  PutScalingPolicy ) to allow capacity to adjust based on player demand while imposing limits on automatic adjustments.
        
        To update fleet capacity, specify the fleet ID and the number of instances you want the fleet to host. If successful, Amazon GameLift starts or terminates instances so that the fleet\'s active instance count matches the desired instance count. You can view a fleet\'s current capacity information by calling  DescribeFleetCapacity . If the desired instance count is higher than the instance type\'s limit, the \"Limit Exceeded\" exception occurs.
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateFleetCapacity>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_fleet_capacity(
              FleetId=\'string\',
              DesiredInstances=123,
              MinSize=123,
              MaxSize=123
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to update capacity for.
        
        :type DesiredInstances: integer
        :param DesiredInstances: 
        
          Number of EC2 instances you want this fleet to host.
        
        :type MinSize: integer
        :param MinSize: 
        
          Minimum value allowed for the fleet\'s instance count. Default if not set is 0.
        
        :type MaxSize: integer
        :param MaxSize: 
        
          Maximum value allowed for the fleet\'s instance count. Default if not set is 1.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetId** *(string) --* 
        
              Unique identifier for a fleet that was updated.
        
        """
        pass

    def update_fleet_port_settings(self, FleetId: str, InboundPermissionAuthorizations: List = None, InboundPermissionRevocations: List = None) -> Dict:
        """
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateFleetPortSettings>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_fleet_port_settings(
              FleetId=\'string\',
              InboundPermissionAuthorizations=[
                  {
                      \'FromPort\': 123,
                      \'ToPort\': 123,
                      \'IpRange\': \'string\',
                      \'Protocol\': \'TCP\'|\'UDP\'
                  },
              ],
              InboundPermissionRevocations=[
                  {
                      \'FromPort\': 123,
                      \'ToPort\': 123,
                      \'IpRange\': \'string\',
                      \'Protocol\': \'TCP\'|\'UDP\'
                  },
              ]
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to update port settings for.
        
        :type InboundPermissionAuthorizations: list
        :param InboundPermissionAuthorizations: 
        
          Collection of port settings to be added to the fleet record.
        
          - *(dict) --* 
        
            A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet\'s allowed ranges. This combination is included in the  GameSession object. 
        
            - **FromPort** *(integer) --* **[REQUIRED]** 
        
              Starting value for a range of allowed port numbers.
        
            - **ToPort** *(integer) --* **[REQUIRED]** 
        
              Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than ``FromPort`` .
        
            - **IpRange** *(string) --* **[REQUIRED]** 
        
              Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: \"``000.000.000.000/[subnet mask]`` \" or optionally the shortened version \"``0.0.0.0/[subnet mask]`` \".
        
            - **Protocol** *(string) --* **[REQUIRED]** 
        
              Network communication protocol used by the fleet.
        
        :type InboundPermissionRevocations: list
        :param InboundPermissionRevocations: 
        
          Collection of port settings to be removed from the fleet record.
        
          - *(dict) --* 
        
            A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet\'s allowed ranges. This combination is included in the  GameSession object. 
        
            - **FromPort** *(integer) --* **[REQUIRED]** 
        
              Starting value for a range of allowed port numbers.
        
            - **ToPort** *(integer) --* **[REQUIRED]** 
        
              Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than ``FromPort`` .
        
            - **IpRange** *(string) --* **[REQUIRED]** 
        
              Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: \"``000.000.000.000/[subnet mask]`` \" or optionally the shortened version \"``0.0.0.0/[subnet mask]`` \".
        
            - **Protocol** *(string) --* **[REQUIRED]** 
        
              Network communication protocol used by the fleet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FleetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **FleetId** *(string) --* 
        
              Unique identifier for a fleet that was updated.
        
        """
        pass

    def update_game_session(self, GameSessionId: str, MaximumPlayerSessionCount: int = None, Name: str = None, PlayerSessionCreationPolicy: str = None, ProtectionPolicy: str = None) -> Dict:
        """
        
        Game-session-related operations include:
        
        *  CreateGameSession   
         
        *  DescribeGameSessions   
         
        *  DescribeGameSessionDetails   
         
        *  SearchGameSessions   
         
        *  UpdateGameSession   
         
        *  GetGameSessionLogUrl   
         
        * Game session placements 
        
          *  StartGameSessionPlacement   
           
          *  DescribeGameSessionPlacement   
           
          *  StopGameSessionPlacement   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateGameSession>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_game_session(
              GameSessionId=\'string\',
              MaximumPlayerSessionCount=123,
              Name=\'string\',
              PlayerSessionCreationPolicy=\'ACCEPT_ALL\'|\'DENY_ALL\',
              ProtectionPolicy=\'NoProtection\'|\'FullProtection\'
          )
        :type GameSessionId: string
        :param GameSessionId: **[REQUIRED]** 
        
          Unique identifier for the game session to update.
        
        :type MaximumPlayerSessionCount: integer
        :param MaximumPlayerSessionCount: 
        
          Maximum number of players that can be connected simultaneously to the game session.
        
        :type Name: string
        :param Name: 
        
          Descriptive label that is associated with a game session. Session names do not need to be unique.
        
        :type PlayerSessionCreationPolicy: string
        :param PlayerSessionCreationPolicy: 
        
          Policy determining whether or not the game session accepts new players.
        
        :type ProtectionPolicy: string
        :param ProtectionPolicy: 
        
          Game session protection policy to apply to this game session only.
        
          * **NoProtection** -- The game session can be terminated during a scale-down event. 
           
          * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be terminated during a scale-down event. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSession\': {
                    \'GameSessionId\': \'string\',
                    \'Name\': \'string\',
                    \'FleetId\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'TerminationTime\': datetime(2015, 1, 1),
                    \'CurrentPlayerSessionCount\': 123,
                    \'MaximumPlayerSessionCount\': 123,
                    \'Status\': \'ACTIVE\'|\'ACTIVATING\'|\'TERMINATED\'|\'TERMINATING\'|\'ERROR\',
                    \'StatusReason\': \'INTERRUPTED\',
                    \'GameProperties\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'IpAddress\': \'string\',
                    \'Port\': 123,
                    \'PlayerSessionCreationPolicy\': \'ACCEPT_ALL\'|\'DENY_ALL\',
                    \'CreatorId\': \'string\',
                    \'GameSessionData\': \'string\',
                    \'MatchmakerData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSession** *(dict) --* 
        
              Object that contains the updated game session metadata.
        
              - **GameSessionId** *(string) --* 
        
                Unique identifier for the game session. A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with a game session. Session names do not need to be unique.
        
              - **FleetId** *(string) --* 
        
                Unique identifier for a fleet that the game session is running on.
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **TerminationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **CurrentPlayerSessionCount** *(integer) --* 
        
                Number of players currently in the game session.
        
              - **MaximumPlayerSessionCount** *(integer) --* 
        
                Maximum number of players that can be connected simultaneously to the game session.
        
              - **Status** *(string) --* 
        
                Current status of the game session. A game session must have an ``ACTIVE`` status to have player sessions.
        
              - **StatusReason** *(string) --* 
        
                Provides additional information about game session status. ``INTERRUPTED`` indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.
        
              - **GameProperties** *(list) --* 
        
                Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). You can search for active game sessions based on this custom data with  SearchGameSessions .
        
                - *(dict) --* 
        
                  Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                  - **Key** *(string) --* 
        
                    Game property identifier.
        
                  - **Value** *(string) --* 
        
                    Game property value.
        
              - **IpAddress** *(string) --* 
        
                IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
              - **Port** *(integer) --* 
        
                Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
        
              - **PlayerSessionCreationPolicy** *(string) --* 
        
                Indicates whether or not the game session is accepting new players.
        
              - **CreatorId** *(string) --* 
        
                Unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
        
              - **GameSessionData** *(string) --* 
        
                Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
        
              - **MatchmakerData** *(string) --* 
        
                Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ). 
        
        """
        pass

    def update_game_session_queue(self, Name: str, TimeoutInSeconds: int = None, PlayerLatencyPolicies: List = None, Destinations: List = None) -> Dict:
        """
        
        Queue-related operations include:
        
        *  CreateGameSessionQueue   
         
        *  DescribeGameSessionQueues   
         
        *  UpdateGameSessionQueue   
         
        *  DeleteGameSessionQueue   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateGameSessionQueue>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_game_session_queue(
              Name=\'string\',
              TimeoutInSeconds=123,
              PlayerLatencyPolicies=[
                  {
                      \'MaximumIndividualPlayerLatencyMilliseconds\': 123,
                      \'PolicyDurationSeconds\': 123
                  },
              ],
              Destinations=[
                  {
                      \'DestinationArn\': \'string\'
                  },
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
        :type TimeoutInSeconds: integer
        :param TimeoutInSeconds: 
        
          Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status.
        
        :type PlayerLatencyPolicies: list
        :param PlayerLatencyPolicies: 
        
          Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. When updating policies, provide a complete collection of policies.
        
          - *(dict) --* 
        
            Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
        
            Queue-related operations include:
        
            *  CreateGameSessionQueue   
             
            *  DescribeGameSessionQueues   
             
            *  UpdateGameSessionQueue   
             
            *  DeleteGameSessionQueue   
             
            - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --* 
        
              The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
        
            - **PolicyDurationSeconds** *(integer) --* 
        
              The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
        
        :type Destinations: list
        :param Destinations: 
        
          List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order. When updating this list, provide a complete list of destinations.
        
          - *(dict) --* 
        
            Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue. 
        
            Queue-related operations include:
        
            *  CreateGameSessionQueue   
             
            *  DescribeGameSessionQueues   
             
            *  UpdateGameSessionQueue   
             
            *  DeleteGameSessionQueue   
             
            - **DestinationArn** *(string) --* 
        
              Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GameSessionQueue\': {
                    \'Name\': \'string\',
                    \'GameSessionQueueArn\': \'string\',
                    \'TimeoutInSeconds\': 123,
                    \'PlayerLatencyPolicies\': [
                        {
                            \'MaximumIndividualPlayerLatencyMilliseconds\': 123,
                            \'PolicyDurationSeconds\': 123
                        },
                    ],
                    \'Destinations\': [
                        {
                            \'DestinationArn\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **GameSessionQueue** *(dict) --* 
        
              Object that describes the newly updated game session queue.
        
              - **Name** *(string) --* 
        
                Descriptive label that is associated with game session queue. Queue names must be unique within each region.
        
              - **GameSessionQueueArn** *(string) --* 
        
                Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` .
        
              - **TimeoutInSeconds** *(integer) --* 
        
                Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status.
        
              - **PlayerLatencyPolicies** *(list) --* 
        
                Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. 
        
                - *(dict) --* 
        
                  Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
        
                  Queue-related operations include:
        
                  *  CreateGameSessionQueue   
                   
                  *  DescribeGameSessionQueues   
                   
                  *  UpdateGameSessionQueue   
                   
                  *  DeleteGameSessionQueue   
                   
                  - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --* 
        
                    The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
        
                  - **PolicyDurationSeconds** *(integer) --* 
        
                    The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
        
              - **Destinations** *(list) --* 
        
                List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
        
                - *(dict) --* 
        
                  Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue. 
        
                  Queue-related operations include:
        
                  *  CreateGameSessionQueue   
                   
                  *  DescribeGameSessionQueues   
                   
                  *  UpdateGameSessionQueue   
                   
                  *  DeleteGameSessionQueue   
                   
                  - **DestinationArn** *(string) --* 
        
                    Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions. 
        
        """
        pass

    def update_matchmaking_configuration(self, Name: str, Description: str = None, GameSessionQueueArns: List = None, RequestTimeoutSeconds: int = None, AcceptanceTimeoutSeconds: int = None, AcceptanceRequired: bool = None, RuleSetName: str = None, NotificationTarget: str = None, AdditionalPlayerCount: int = None, CustomEventData: str = None, GameProperties: List = None, GameSessionData: str = None) -> Dict:
        """
        
        Operations related to match configurations and rule sets include:
        
        *  CreateMatchmakingConfiguration   
         
        *  DescribeMatchmakingConfigurations   
         
        *  UpdateMatchmakingConfiguration   
         
        *  DeleteMatchmakingConfiguration   
         
        *  CreateMatchmakingRuleSet   
         
        *  DescribeMatchmakingRuleSets   
         
        *  ValidateMatchmakingRuleSet   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateMatchmakingConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_matchmaking_configuration(
              Name=\'string\',
              Description=\'string\',
              GameSessionQueueArns=[
                  \'string\',
              ],
              RequestTimeoutSeconds=123,
              AcceptanceTimeoutSeconds=123,
              AcceptanceRequired=True|False,
              RuleSetName=\'string\',
              NotificationTarget=\'string\',
              AdditionalPlayerCount=123,
              CustomEventData=\'string\',
              GameProperties=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              GameSessionData=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Unique identifier for a matchmaking configuration to update.
        
        :type Description: string
        :param Description: 
        
          Descriptive label that is associated with matchmaking configuration.
        
        :type GameSessionQueueArns: list
        :param GameSessionQueueArns: 
        
          Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
        
          - *(string) --* 
        
        :type RequestTimeoutSeconds: integer
        :param RequestTimeoutSeconds: 
        
          Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
        
        :type AcceptanceTimeoutSeconds: integer
        :param AcceptanceTimeoutSeconds: 
        
          Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
        
        :type AcceptanceRequired: boolean
        :param AcceptanceRequired: 
        
          Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
        
        :type RuleSetName: string
        :param RuleSetName: 
        
          Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
        
        :type NotificationTarget: string
        :param NotificationTarget: 
        
          SNS topic ARN that is set up to receive matchmaking notifications. See `Setting up Notifications for Matchmaking <http://docs.aws.amazon.com/gamelift/latest/developerguide/match-notification.html>`__ for more information.
        
        :type AdditionalPlayerCount: integer
        :param AdditionalPlayerCount: 
        
          Number of player slots in a match to keep open for future players. For example, if the configuration\'s rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.
        
        :type CustomEventData: string
        :param CustomEventData: 
        
          Information to attached to all events related to the matchmaking configuration. 
        
        :type GameProperties: list
        :param GameProperties: 
        
          Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
          - *(dict) --* 
        
            Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              Game property identifier.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              Game property value.
        
        :type GameSessionData: string
        :param GameSessionData: 
        
          Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Configuration\': {
                    \'Name\': \'string\',
                    \'Description\': \'string\',
                    \'GameSessionQueueArns\': [
                        \'string\',
                    ],
                    \'RequestTimeoutSeconds\': 123,
                    \'AcceptanceTimeoutSeconds\': 123,
                    \'AcceptanceRequired\': True|False,
                    \'RuleSetName\': \'string\',
                    \'NotificationTarget\': \'string\',
                    \'AdditionalPlayerCount\': 123,
                    \'CustomEventData\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'GameProperties\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'GameSessionData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Configuration** *(dict) --* 
        
              Object that describes the updated matchmaking configuration.
        
              - **Name** *(string) --* 
        
                Unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
        
              - **Description** *(string) --* 
        
                Descriptive label that is associated with matchmaking configuration.
        
              - **GameSessionQueueArns** *(list) --* 
        
                Amazon Resource Name (`ARN <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
        
                - *(string) --* 
            
              - **RequestTimeoutSeconds** *(integer) --* 
        
                Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
        
              - **AcceptanceTimeoutSeconds** *(integer) --* 
        
                Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
        
              - **AcceptanceRequired** *(boolean) --* 
        
                Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
        
              - **RuleSetName** *(string) --* 
        
                Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
        
              - **NotificationTarget** *(string) --* 
        
                SNS topic ARN that is set up to receive matchmaking notifications.
        
              - **AdditionalPlayerCount** *(integer) --* 
        
                Number of player slots in a match to keep open for future players. For example, if the configuration\'s rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.
        
              - **CustomEventData** *(string) --* 
        
                Information to attached to all events related to the matchmaking configuration. 
        
              - **CreationTime** *(datetime) --* 
        
                Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example \"1469498468.057\").
        
              - **GameProperties** *(list) --* 
        
                Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
                - *(dict) --* 
        
                  Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
        
                  - **Key** *(string) --* 
        
                    Game property identifier.
        
                  - **Value** *(string) --* 
        
                    Game property value.
        
              - **GameSessionData** *(string) --* 
        
                Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        
        """
        pass

    def update_runtime_configuration(self, FleetId: str, RuntimeConfiguration: Dict) -> Dict:
        """
        
        To update run-time configuration, specify the fleet ID and provide a ``RuntimeConfiguration`` object with the updated collection of server process configurations.
        
        Each instance in a Amazon GameLift fleet checks regularly for an updated run-time configuration and changes how it launches server processes to comply with the latest version. Existing server processes are not affected by the update; they continue to run until they end, while Amazon GameLift simply adds new server processes to fit the current run-time configuration. As a result, the run-time configuration changes are applied gradually as existing processes shut down and new processes are launched in Amazon GameLift\'s normal process recycling activity.
        
        Fleet-related operations include:
        
        *  CreateFleet   
         
        *  ListFleets   
         
        *  DeleteFleet   
         
        * Describe fleets: 
        
          *  DescribeFleetAttributes   
           
          *  DescribeFleetCapacity   
           
          *  DescribeFleetPortSettings   
           
          *  DescribeFleetUtilization   
           
          *  DescribeRuntimeConfiguration   
           
          *  DescribeEC2InstanceLimits   
           
          *  DescribeFleetEvents   
           
        * Update fleets: 
        
          *  UpdateFleetAttributes   
           
          *  UpdateFleetCapacity   
           
          *  UpdateFleetPortSettings   
           
          *  UpdateRuntimeConfiguration   
           
        * Manage fleet actions: 
        
          *  StartFleetActions   
           
          *  StopFleetActions   
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateRuntimeConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_runtime_configuration(
              FleetId=\'string\',
              RuntimeConfiguration={
                  \'ServerProcesses\': [
                      {
                          \'LaunchPath\': \'string\',
                          \'Parameters\': \'string\',
                          \'ConcurrentExecutions\': 123
                      },
                  ],
                  \'MaxConcurrentGameSessionActivations\': 123,
                  \'GameSessionActivationTimeoutSeconds\': 123
              }
          )
        :type FleetId: string
        :param FleetId: **[REQUIRED]** 
        
          Unique identifier for a fleet to update run-time configuration for.
        
        :type RuntimeConfiguration: dict
        :param RuntimeConfiguration: **[REQUIRED]** 
        
          Instructions for launching server processes on each instance in the fleet. The run-time configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance.
        
          - **ServerProcesses** *(list) --* 
        
            Collection of server process configurations that describe which server processes to run on each instance in a fleet.
        
            - *(dict) --* 
        
              A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s ``  RuntimeConfiguration `` .
        
              - **LaunchPath** *(string) --* **[REQUIRED]** 
        
                Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances ``C:\game`` , and for Linux instances ``/local/game`` . A Windows game build with an executable file located at ``MyGame\latest\server.exe`` must have a launch path of \"``C:\game\MyGame\latest\server.exe`` \". A Linux game build with an executable file located at ``MyGame/latest/server.exe`` must have a launch path of \"``/local/game/MyGame/latest/server.exe`` \". 
        
              - **Parameters** *(string) --* 
        
                Optional list of parameters to pass to the server executable on launch.
        
              - **ConcurrentExecutions** *(integer) --* **[REQUIRED]** 
        
                Number of server processes using this configuration to run concurrently on an instance.
        
          - **MaxConcurrentGameSessionActivations** *(integer) --* 
        
            Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
        
          - **GameSessionActivationTimeoutSeconds** *(integer) --* 
        
            Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING`` . If the game session is not active before the timeout, activation is terminated and the game session status is changed to ``TERMINATED`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RuntimeConfiguration\': {
                    \'ServerProcesses\': [
                        {
                            \'LaunchPath\': \'string\',
                            \'Parameters\': \'string\',
                            \'ConcurrentExecutions\': 123
                        },
                    ],
                    \'MaxConcurrentGameSessionActivations\': 123,
                    \'GameSessionActivationTimeoutSeconds\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **RuntimeConfiguration** *(dict) --* 
        
              The run-time configuration currently in force. If the update was successful, this object matches the one in the request.
        
              - **ServerProcesses** *(list) --* 
        
                Collection of server process configurations that describe which server processes to run on each instance in a fleet.
        
                - *(dict) --* 
        
                  A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s ``  RuntimeConfiguration `` .
        
                  - **LaunchPath** *(string) --* 
        
                    Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances ``C:\game`` , and for Linux instances ``/local/game`` . A Windows game build with an executable file located at ``MyGame\latest\server.exe`` must have a launch path of \"``C:\game\MyGame\latest\server.exe`` \". A Linux game build with an executable file located at ``MyGame/latest/server.exe`` must have a launch path of \"``/local/game/MyGame/latest/server.exe`` \". 
        
                  - **Parameters** *(string) --* 
        
                    Optional list of parameters to pass to the server executable on launch.
        
                  - **ConcurrentExecutions** *(integer) --* 
        
                    Number of server processes using this configuration to run concurrently on an instance.
        
              - **MaxConcurrentGameSessionActivations** *(integer) --* 
        
                Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
        
              - **GameSessionActivationTimeoutSeconds** *(integer) --* 
        
                Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING`` . If the game session is not active before the timeout, activation is terminated and the game session status is changed to ``TERMINATED`` .
        
        """
        pass

    def validate_matchmaking_rule_set(self, RuleSetBody: str) -> Dict:
        """
        
        Operations related to match configurations and rule sets include:
        
        *  CreateMatchmakingConfiguration   
         
        *  DescribeMatchmakingConfigurations   
         
        *  UpdateMatchmakingConfiguration   
         
        *  DeleteMatchmakingConfiguration   
         
        *  CreateMatchmakingRuleSet   
         
        *  DescribeMatchmakingRuleSets   
         
        *  ValidateMatchmakingRuleSet   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ValidateMatchmakingRuleSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.validate_matchmaking_rule_set(
              RuleSetBody=\'string\'
          )
        :type RuleSetBody: string
        :param RuleSetBody: **[REQUIRED]** 
        
          Collection of matchmaking rules to validate, formatted as a JSON string.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Valid\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the returned data in response to a request action.
        
            - **Valid** *(boolean) --* 
        
              Response indicating whether or not the rule set is valid.
        
        """
        pass
