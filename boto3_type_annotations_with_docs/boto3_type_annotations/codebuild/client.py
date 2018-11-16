from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_delete_builds(self, ids: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchDeleteBuilds>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_delete_builds(
              ids=[
                  \'string\',
              ]
          )
        :type ids: list
        :param ids: **[REQUIRED]** 
        
          The IDs of the builds to delete.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'buildsDeleted\': [
                    \'string\',
                ],
                \'buildsNotDeleted\': [
                    {
                        \'id\': \'string\',
                        \'statusCode\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **buildsDeleted** *(list) --* 
        
              The IDs of the builds that were successfully deleted.
        
              - *(string) --* 
          
            - **buildsNotDeleted** *(list) --* 
        
              Information about any builds that could not be successfully deleted.
        
              - *(dict) --* 
        
                Information about a build that could not be successfully deleted.
        
                - **id** *(string) --* 
        
                  The ID of the build that could not be successfully deleted.
        
                - **statusCode** *(string) --* 
        
                  Additional information about the build that could not be successfully deleted.
        
        """
        pass

    def batch_get_builds(self, ids: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetBuilds>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_get_builds(
              ids=[
                  \'string\',
              ]
          )
        :type ids: list
        :param ids: **[REQUIRED]** 
        
          The IDs of the builds.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'builds\': [
                    {
                        \'id\': \'string\',
                        \'arn\': \'string\',
                        \'startTime\': datetime(2015, 1, 1),
                        \'endTime\': datetime(2015, 1, 1),
                        \'currentPhase\': \'string\',
                        \'buildStatus\': \'SUCCEEDED\'|\'FAILED\'|\'FAULT\'|\'TIMED_OUT\'|\'IN_PROGRESS\'|\'STOPPED\',
                        \'sourceVersion\': \'string\',
                        \'resolvedSourceVersion\': \'string\',
                        \'projectName\': \'string\',
                        \'phases\': [
                            {
                                \'phaseType\': \'SUBMITTED\'|\'PROVISIONING\'|\'DOWNLOAD_SOURCE\'|\'INSTALL\'|\'PRE_BUILD\'|\'BUILD\'|\'POST_BUILD\'|\'UPLOAD_ARTIFACTS\'|\'FINALIZING\'|\'COMPLETED\',
                                \'phaseStatus\': \'SUCCEEDED\'|\'FAILED\'|\'FAULT\'|\'TIMED_OUT\'|\'IN_PROGRESS\'|\'STOPPED\',
                                \'startTime\': datetime(2015, 1, 1),
                                \'endTime\': datetime(2015, 1, 1),
                                \'durationInSeconds\': 123,
                                \'contexts\': [
                                    {
                                        \'statusCode\': \'string\',
                                        \'message\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'source\': {
                            \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                            \'location\': \'string\',
                            \'gitCloneDepth\': 123,
                            \'buildspec\': \'string\',
                            \'auth\': {
                                \'type\': \'OAUTH\',
                                \'resource\': \'string\'
                            },
                            \'reportBuildStatus\': True|False,
                            \'insecureSsl\': True|False,
                            \'sourceIdentifier\': \'string\'
                        },
                        \'secondarySources\': [
                            {
                                \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                                \'location\': \'string\',
                                \'gitCloneDepth\': 123,
                                \'buildspec\': \'string\',
                                \'auth\': {
                                    \'type\': \'OAUTH\',
                                    \'resource\': \'string\'
                                },
                                \'reportBuildStatus\': True|False,
                                \'insecureSsl\': True|False,
                                \'sourceIdentifier\': \'string\'
                            },
                        ],
                        \'secondarySourceVersions\': [
                            {
                                \'sourceIdentifier\': \'string\',
                                \'sourceVersion\': \'string\'
                            },
                        ],
                        \'artifacts\': {
                            \'location\': \'string\',
                            \'sha256sum\': \'string\',
                            \'md5sum\': \'string\',
                            \'overrideArtifactName\': True|False,
                            \'encryptionDisabled\': True|False,
                            \'artifactIdentifier\': \'string\'
                        },
                        \'secondaryArtifacts\': [
                            {
                                \'location\': \'string\',
                                \'sha256sum\': \'string\',
                                \'md5sum\': \'string\',
                                \'overrideArtifactName\': True|False,
                                \'encryptionDisabled\': True|False,
                                \'artifactIdentifier\': \'string\'
                            },
                        ],
                        \'cache\': {
                            \'type\': \'NO_CACHE\'|\'S3\',
                            \'location\': \'string\'
                        },
                        \'environment\': {
                            \'type\': \'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
                            \'image\': \'string\',
                            \'computeType\': \'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
                            \'environmentVariables\': [
                                {
                                    \'name\': \'string\',
                                    \'value\': \'string\',
                                    \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                                },
                            ],
                            \'privilegedMode\': True|False,
                            \'certificate\': \'string\'
                        },
                        \'serviceRole\': \'string\',
                        \'logs\': {
                            \'groupName\': \'string\',
                            \'streamName\': \'string\',
                            \'deepLink\': \'string\',
                            \'s3DeepLink\': \'string\',
                            \'cloudWatchLogs\': {
                                \'status\': \'ENABLED\'|\'DISABLED\',
                                \'groupName\': \'string\',
                                \'streamName\': \'string\'
                            },
                            \'s3Logs\': {
                                \'status\': \'ENABLED\'|\'DISABLED\',
                                \'location\': \'string\'
                            }
                        },
                        \'timeoutInMinutes\': 123,
                        \'buildComplete\': True|False,
                        \'initiator\': \'string\',
                        \'vpcConfig\': {
                            \'vpcId\': \'string\',
                            \'subnets\': [
                                \'string\',
                            ],
                            \'securityGroupIds\': [
                                \'string\',
                            ]
                        },
                        \'networkInterface\': {
                            \'subnetId\': \'string\',
                            \'networkInterfaceId\': \'string\'
                        },
                        \'encryptionKey\': \'string\'
                    },
                ],
                \'buildsNotFound\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **builds** *(list) --* 
        
              Information about the requested builds.
        
              - *(dict) --* 
        
                Information about a build.
        
                - **id** *(string) --* 
        
                  The unique ID for the build.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the build.
        
                - **startTime** *(datetime) --* 
        
                  When the build process started, expressed in Unix time format.
        
                - **endTime** *(datetime) --* 
        
                  When the build process ended, expressed in Unix time format.
        
                - **currentPhase** *(string) --* 
        
                  The current build phase.
        
                - **buildStatus** *(string) --* 
        
                  The current status of the build. Valid values include:
        
                  * ``FAILED`` : The build failed. 
                   
                  * ``FAULT`` : The build faulted. 
                   
                  * ``IN_PROGRESS`` : The build is still in progress. 
                   
                  * ``STOPPED`` : The build stopped. 
                   
                  * ``SUCCEEDED`` : The build succeeded. 
                   
                  * ``TIMED_OUT`` : The build timed out. 
                   
                - **sourceVersion** *(string) --* 
        
                  Any version identifier for the version of the source code to be built.
        
                - **resolvedSourceVersion** *(string) --* 
        
                  An identifier for the version of this build\'s source code. 
        
                  * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.  
                   
                  * For AWS CodePipeline, the source revision provided by AWS CodePipeline.  
                   
                  * For Amazon Simple Storage Service (Amazon S3), this does not apply.  
                   
                - **projectName** *(string) --* 
        
                  The name of the AWS CodeBuild project.
        
                - **phases** *(list) --* 
        
                  Information about all previous build phases that are completed and information about any current build phase that is not yet complete.
        
                  - *(dict) --* 
        
                    Information about a stage for a build.
        
                    - **phaseType** *(string) --* 
        
                      The name of the build phase. Valid values include:
        
                      * ``BUILD`` : Core build activities typically occur in this build phase. 
                       
                      * ``COMPLETED`` : The build has been completed. 
                       
                      * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase. 
                       
                      * ``FINALIZING`` : The build process is completing in this build phase. 
                       
                      * ``INSTALL`` : Installation activities typically occur in this build phase. 
                       
                      * ``POST_BUILD`` : Post-build activities typically occur in this build phase. 
                       
                      * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase. 
                       
                      * ``PROVISIONING`` : The build environment is being set up. 
                       
                      * ``SUBMITTED`` : The build has been submitted. 
                       
                      * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output location. 
                       
                    - **phaseStatus** *(string) --* 
        
                      The current status of the build phase. Valid values include:
        
                      * ``FAILED`` : The build phase failed. 
                       
                      * ``FAULT`` : The build phase faulted. 
                       
                      * ``IN_PROGRESS`` : The build phase is still in progress. 
                       
                      * ``STOPPED`` : The build phase stopped. 
                       
                      * ``SUCCEEDED`` : The build phase succeeded. 
                       
                      * ``TIMED_OUT`` : The build phase timed out. 
                       
                    - **startTime** *(datetime) --* 
        
                      When the build phase started, expressed in Unix time format.
        
                    - **endTime** *(datetime) --* 
        
                      When the build phase ended, expressed in Unix time format.
        
                    - **durationInSeconds** *(integer) --* 
        
                      How long, in seconds, between the starting and ending times of the build\'s phase.
        
                    - **contexts** *(list) --* 
        
                      Additional information about a build phase, especially to help troubleshoot a failed build.
        
                      - *(dict) --* 
        
                        Additional information about a build phase that has an error. You can use this information to help troubleshoot a failed build.
        
                        - **statusCode** *(string) --* 
        
                          The status code for the context of the build phase.
        
                        - **message** *(string) --* 
        
                          An explanation of the build phase\'s context. This explanation might include a command ID and an exit code.
        
                - **source** *(dict) --* 
        
                  Information about the source code to be built.
        
                  - **type** *(string) --* 
        
                    The type of repository that contains the source code to be built. Valid values include:
        
                    * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                     
                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                     
                    * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                     
                    * ``GITHUB`` : The source code is in a GitHub repository. 
                     
                    * ``NO_SOURCE`` : The project does not have input source code. 
                     
                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                     
                  - **location** *(string) --* 
        
                    Information about the location of the source code to be built. Valid values include:
        
                    * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                     
                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                     
                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                      * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                       
                      * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                       
                    * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                    * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                  - **gitCloneDepth** *(integer) --* 
        
                    Information about the git clone depth for the build project.
        
                  - **buildspec** *(string) --* 
        
                    The build spec declaration to use for the builds in this build project.
        
                    If this value is not specified, a build spec must be included along with the source code to be built.
        
                  - **auth** *(dict) --* 
        
                    Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                    This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                    - **type** *(string) --* 
        
                      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                    - **resource** *(string) --* 
        
                      The resource value that applies to the specified authorization type.
        
                  - **reportBuildStatus** *(boolean) --* 
        
                    Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                  - **insecureSsl** *(boolean) --* 
        
                    Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                  - **sourceIdentifier** *(string) --* 
        
                    An identifier for this project source. 
        
                - **secondarySources** *(list) --* 
        
                  An array of ``ProjectSource`` objects. 
        
                  - *(dict) --* 
        
                    Information about the build input source code for the build project.
        
                    - **type** *(string) --* 
        
                      The type of repository that contains the source code to be built. Valid values include:
        
                      * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                       
                      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                       
                      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                       
                      * ``GITHUB`` : The source code is in a GitHub repository. 
                       
                      * ``NO_SOURCE`` : The project does not have input source code. 
                       
                      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                       
                    - **location** *(string) --* 
        
                      Information about the location of the source code to be built. Valid values include:
        
                      * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                       
                      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                       
                      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                        * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                         
                        * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                         
                      * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                       
                      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                       
                    - **gitCloneDepth** *(integer) --* 
        
                      Information about the git clone depth for the build project.
        
                    - **buildspec** *(string) --* 
        
                      The build spec declaration to use for the builds in this build project.
        
                      If this value is not specified, a build spec must be included along with the source code to be built.
        
                    - **auth** *(dict) --* 
        
                      Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                      This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                      - **type** *(string) --* 
        
                        The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                      - **resource** *(string) --* 
        
                        The resource value that applies to the specified authorization type.
        
                    - **reportBuildStatus** *(boolean) --* 
        
                      Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                    - **insecureSsl** *(boolean) --* 
        
                      Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                    - **sourceIdentifier** *(string) --* 
        
                      An identifier for this project source. 
        
                - **secondarySourceVersions** *(list) --* 
        
                  An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one of: 
        
                  * For AWS CodeCommit: the commit ID to use. 
                   
                  * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                   
                  * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                   
                  * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
                   
                  - *(dict) --* 
        
                    A source identifier and its corresponding version.
        
                    - **sourceIdentifier** *(string) --* 
        
                      An identifier for a source in the build project.
        
                    - **sourceVersion** *(string) --* 
        
                      The source version for the corresponding source identifier. If specified, must be one of:
        
                      * For AWS CodeCommit: the commit ID to use. 
                       
                      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                       
                      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                       
                      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
                       
                - **artifacts** *(dict) --* 
        
                  Information about the output artifacts for the build.
        
                  - **location** *(string) --* 
        
                    Information about the location of the build artifacts.
        
                  - **sha256sum** *(string) --* 
        
                    The SHA-256 hash of the build artifact.
        
                    You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                    .. note::
        
                      This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                  - **md5sum** *(string) --* 
        
                    The MD5 hash of the build artifact.
        
                    You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                    .. note::
        
                      This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                  - **overrideArtifactName** *(boolean) --* 
        
                    If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                  - **encryptionDisabled** *(boolean) --* 
        
                    Information that tells you if encryption for build artifacts is disabled. 
        
                  - **artifactIdentifier** *(string) --* 
        
                    An identifier for this artifact definition. 
        
                - **secondaryArtifacts** *(list) --* 
        
                  An array of ``ProjectArtifacts`` objects. 
        
                  - *(dict) --* 
        
                    Information about build output artifacts.
        
                    - **location** *(string) --* 
        
                      Information about the location of the build artifacts.
        
                    - **sha256sum** *(string) --* 
        
                      The SHA-256 hash of the build artifact.
        
                      You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                      .. note::
        
                        This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                    - **md5sum** *(string) --* 
        
                      The MD5 hash of the build artifact.
        
                      You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                      .. note::
        
                        This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                    - **overrideArtifactName** *(boolean) --* 
        
                      If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                    - **encryptionDisabled** *(boolean) --* 
        
                      Information that tells you if encryption for build artifacts is disabled. 
        
                    - **artifactIdentifier** *(string) --* 
        
                      An identifier for this artifact definition. 
        
                - **cache** *(dict) --* 
        
                  Information about the cache for the build.
        
                  - **type** *(string) --* 
        
                    The type of cache used by the build project. Valid values include:
        
                    * ``NO_CACHE`` : The build project will not use any cache. 
                     
                    * ``S3`` : The build project will read and write from/to S3. 
                     
                  - **location** *(string) --* 
        
                    Information about the cache location, as follows: 
        
                    * ``NO_CACHE`` : This value will be ignored. 
                     
                    * ``S3`` : This is the S3 bucket name/prefix. 
                     
                - **environment** *(dict) --* 
        
                  Information about the build environment for this build.
        
                  - **type** *(string) --* 
        
                    The type of build environment to use for related builds.
        
                  - **image** *(string) --* 
        
                    The ID of the Docker image to use for this build project.
        
                  - **computeType** *(string) --* 
        
                    Information about the compute resources the build project will use. Available values include:
        
                    * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
                     
                    * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
                     
                    * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
                     
                  - **environmentVariables** *(list) --* 
        
                    A set of environment variables to make available to builds for this build project.
        
                    - *(dict) --* 
        
                      Information about an environment variable for a build project or a build.
        
                      - **name** *(string) --* 
        
                        The name or key of the environment variable.
        
                      - **value** *(string) --* 
        
                        The value of the environment variable.
        
                        .. warning::
        
                          We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
                      - **type** *(string) --* 
        
                        The type of environment variable. Valid values include:
        
                        * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                         
                        * ``PLAINTEXT`` : An environment variable in plaintext format. 
                         
                  - **privilegedMode** *(boolean) --* 
        
                    Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
        
                    If the operating system\'s base image is Ubuntu Linux:
        
                     ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                    If the operating system\'s base image is Alpine Linux, add the ``-t`` argument to ``timeout`` :
        
                     ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                  - **certificate** *(string) --* 
        
                    The certificate to use with this build project.
        
                - **serviceRole** *(string) --* 
        
                  The name of a service role used for this build.
        
                - **logs** *(dict) --* 
        
                  Information about the build\'s logs in Amazon CloudWatch Logs.
        
                  - **groupName** *(string) --* 
        
                    The name of the Amazon CloudWatch Logs group for the build logs.
        
                  - **streamName** *(string) --* 
        
                    The name of the Amazon CloudWatch Logs stream for the build logs.
        
                  - **deepLink** *(string) --* 
        
                    The URL to an individual build log in Amazon CloudWatch Logs.
        
                  - **s3DeepLink** *(string) --* 
        
                    The URL to an individual build log in an S3 bucket. 
        
                  - **cloudWatchLogs** *(dict) --* 
        
                    Information about Amazon CloudWatch Logs for a build project. 
        
                    - **status** *(string) --* 
        
                      The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
                      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
                       
                      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
                       
                    - **groupName** *(string) --* 
        
                      The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                    - **streamName** *(string) --* 
        
                      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                  - **s3Logs** *(dict) --* 
        
                    Information about S3 logs for a build project. 
        
                    - **status** *(string) --* 
        
                      The current status of the S3 build logs. Valid values are:
        
                      * ``ENABLED`` : S3 build logs are enabled for this build project. 
                       
                      * ``DISABLED`` : S3 build logs are not enabled for this build project. 
                       
                    - **location** *(string) --* 
        
                      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
                - **timeoutInMinutes** *(integer) --* 
        
                  How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.
        
                - **buildComplete** *(boolean) --* 
        
                  Whether the build has finished. True if completed; otherwise, false.
        
                - **initiator** *(string) --* 
        
                  The entity that started the build. Valid values include:
        
                  * If AWS CodePipeline started the build, the pipeline\'s name (for example, ``codepipeline/my-demo-pipeline`` ). 
                   
                  * If an AWS Identity and Access Management (IAM) user started the build, the user\'s name (for example ``MyUserName`` ). 
                   
                  * If the Jenkins plugin for AWS CodeBuild started the build, the string ``CodeBuild-Jenkins-Plugin`` . 
                   
                - **vpcConfig** *(dict) --* 
        
                  If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.
        
                  - **vpcId** *(string) --* 
        
                    The ID of the Amazon VPC.
        
                  - **subnets** *(list) --* 
        
                    A list of one or more subnet IDs in your Amazon VPC.
        
                    - *(string) --* 
                
                  - **securityGroupIds** *(list) --* 
        
                    A list of one or more security groups IDs in your Amazon VPC.
        
                    - *(string) --* 
                
                - **networkInterface** *(dict) --* 
        
                  Describes a network interface.
        
                  - **subnetId** *(string) --* 
        
                    The ID of the subnet.
        
                  - **networkInterfaceId** *(string) --* 
        
                    The ID of the network interface.
        
                - **encryptionKey** *(string) --* 
        
                  The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
        
                  This is expressed either as the CMK\'s Amazon Resource Name (ARN) or, if specified, the CMK\'s alias (using the format ``alias/*alias-name* `` ).
        
            - **buildsNotFound** *(list) --* 
        
              The IDs of builds for which information could not be found.
        
              - *(string) --* 
          
        """
        pass

    def batch_get_projects(self, names: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetProjects>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_get_projects(
              names=[
                  \'string\',
              ]
          )
        :type names: list
        :param names: **[REQUIRED]** 
        
          The names of the build projects.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'projects\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'description\': \'string\',
                        \'source\': {
                            \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                            \'location\': \'string\',
                            \'gitCloneDepth\': 123,
                            \'buildspec\': \'string\',
                            \'auth\': {
                                \'type\': \'OAUTH\',
                                \'resource\': \'string\'
                            },
                            \'reportBuildStatus\': True|False,
                            \'insecureSsl\': True|False,
                            \'sourceIdentifier\': \'string\'
                        },
                        \'secondarySources\': [
                            {
                                \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                                \'location\': \'string\',
                                \'gitCloneDepth\': 123,
                                \'buildspec\': \'string\',
                                \'auth\': {
                                    \'type\': \'OAUTH\',
                                    \'resource\': \'string\'
                                },
                                \'reportBuildStatus\': True|False,
                                \'insecureSsl\': True|False,
                                \'sourceIdentifier\': \'string\'
                            },
                        ],
                        \'artifacts\': {
                            \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                            \'location\': \'string\',
                            \'path\': \'string\',
                            \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                            \'name\': \'string\',
                            \'packaging\': \'NONE\'|\'ZIP\',
                            \'overrideArtifactName\': True|False,
                            \'encryptionDisabled\': True|False,
                            \'artifactIdentifier\': \'string\'
                        },
                        \'secondaryArtifacts\': [
                            {
                                \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                                \'location\': \'string\',
                                \'path\': \'string\',
                                \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                                \'name\': \'string\',
                                \'packaging\': \'NONE\'|\'ZIP\',
                                \'overrideArtifactName\': True|False,
                                \'encryptionDisabled\': True|False,
                                \'artifactIdentifier\': \'string\'
                            },
                        ],
                        \'cache\': {
                            \'type\': \'NO_CACHE\'|\'S3\',
                            \'location\': \'string\'
                        },
                        \'environment\': {
                            \'type\': \'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
                            \'image\': \'string\',
                            \'computeType\': \'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
                            \'environmentVariables\': [
                                {
                                    \'name\': \'string\',
                                    \'value\': \'string\',
                                    \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                                },
                            ],
                            \'privilegedMode\': True|False,
                            \'certificate\': \'string\'
                        },
                        \'serviceRole\': \'string\',
                        \'timeoutInMinutes\': 123,
                        \'encryptionKey\': \'string\',
                        \'tags\': [
                            {
                                \'key\': \'string\',
                                \'value\': \'string\'
                            },
                        ],
                        \'created\': datetime(2015, 1, 1),
                        \'lastModified\': datetime(2015, 1, 1),
                        \'webhook\': {
                            \'url\': \'string\',
                            \'payloadUrl\': \'string\',
                            \'secret\': \'string\',
                            \'branchFilter\': \'string\',
                            \'lastModifiedSecret\': datetime(2015, 1, 1)
                        },
                        \'vpcConfig\': {
                            \'vpcId\': \'string\',
                            \'subnets\': [
                                \'string\',
                            ],
                            \'securityGroupIds\': [
                                \'string\',
                            ]
                        },
                        \'badge\': {
                            \'badgeEnabled\': True|False,
                            \'badgeRequestUrl\': \'string\'
                        },
                        \'logsConfig\': {
                            \'cloudWatchLogs\': {
                                \'status\': \'ENABLED\'|\'DISABLED\',
                                \'groupName\': \'string\',
                                \'streamName\': \'string\'
                            },
                            \'s3Logs\': {
                                \'status\': \'ENABLED\'|\'DISABLED\',
                                \'location\': \'string\'
                            }
                        }
                    },
                ],
                \'projectsNotFound\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **projects** *(list) --* 
        
              Information about the requested build projects.
        
              - *(dict) --* 
        
                Information about a build project.
        
                - **name** *(string) --* 
        
                  The name of the build project.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the build project.
        
                - **description** *(string) --* 
        
                  A description that makes the build project easy to identify.
        
                - **source** *(dict) --* 
        
                  Information about the build input source code for this build project.
        
                  - **type** *(string) --* 
        
                    The type of repository that contains the source code to be built. Valid values include:
        
                    * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                     
                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                     
                    * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                     
                    * ``GITHUB`` : The source code is in a GitHub repository. 
                     
                    * ``NO_SOURCE`` : The project does not have input source code. 
                     
                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                     
                  - **location** *(string) --* 
        
                    Information about the location of the source code to be built. Valid values include:
        
                    * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                     
                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                     
                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                      * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                       
                      * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                       
                    * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                    * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                  - **gitCloneDepth** *(integer) --* 
        
                    Information about the git clone depth for the build project.
        
                  - **buildspec** *(string) --* 
        
                    The build spec declaration to use for the builds in this build project.
        
                    If this value is not specified, a build spec must be included along with the source code to be built.
        
                  - **auth** *(dict) --* 
        
                    Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                    This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                    - **type** *(string) --* 
        
                      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                    - **resource** *(string) --* 
        
                      The resource value that applies to the specified authorization type.
        
                  - **reportBuildStatus** *(boolean) --* 
        
                    Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                  - **insecureSsl** *(boolean) --* 
        
                    Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                  - **sourceIdentifier** *(string) --* 
        
                    An identifier for this project source. 
        
                - **secondarySources** *(list) --* 
        
                  An array of ``ProjectSource`` objects. 
        
                  - *(dict) --* 
        
                    Information about the build input source code for the build project.
        
                    - **type** *(string) --* 
        
                      The type of repository that contains the source code to be built. Valid values include:
        
                      * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                       
                      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                       
                      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                       
                      * ``GITHUB`` : The source code is in a GitHub repository. 
                       
                      * ``NO_SOURCE`` : The project does not have input source code. 
                       
                      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                       
                    - **location** *(string) --* 
        
                      Information about the location of the source code to be built. Valid values include:
        
                      * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                       
                      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                       
                      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                        * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                         
                        * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                         
                      * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                       
                      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                       
                    - **gitCloneDepth** *(integer) --* 
        
                      Information about the git clone depth for the build project.
        
                    - **buildspec** *(string) --* 
        
                      The build spec declaration to use for the builds in this build project.
        
                      If this value is not specified, a build spec must be included along with the source code to be built.
        
                    - **auth** *(dict) --* 
        
                      Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                      This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                      - **type** *(string) --* 
        
                        The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                      - **resource** *(string) --* 
        
                        The resource value that applies to the specified authorization type.
        
                    - **reportBuildStatus** *(boolean) --* 
        
                      Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                    - **insecureSsl** *(boolean) --* 
        
                      Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                    - **sourceIdentifier** *(string) --* 
        
                      An identifier for this project source. 
        
                - **artifacts** *(dict) --* 
        
                  Information about the build output artifacts for the build project.
        
                  - **type** *(string) --* 
        
                    The type of build output artifact. Valid values include:
        
                    * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
                     
                    * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
                     
                    * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
                     
                  - **location** *(string) --* 
        
                    Information about the build output artifact location, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
                     
                  - **path** *(string) --* 
        
                    Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
                     
                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
                  - **namespaceType** *(string) --* 
        
                    Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , then valid values include: 
        
                      * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                       
                      * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                       
                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
                  - **name** *(string) --* 
        
                    Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
                     
                    For example:
        
                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
                     
                    * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
                     
                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
                     
                  - **packaging** *(string) --* 
        
                    The type of build output artifact to create, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , valid values include: 
        
                      * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                       
                      * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                       
                  - **overrideArtifactName** *(boolean) --* 
        
                    If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                  - **encryptionDisabled** *(boolean) --* 
        
                    Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
                  - **artifactIdentifier** *(string) --* 
        
                    An identifier for this artifact definition. 
        
                - **secondaryArtifacts** *(list) --* 
        
                  An array of ``ProjectArtifacts`` objects. 
        
                  - *(dict) --* 
        
                    Information about the build output artifacts for the build project.
        
                    - **type** *(string) --* 
        
                      The type of build output artifact. Valid values include:
        
                      * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
                       
                      * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
                       
                      * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
                       
                    - **location** *(string) --* 
        
                      Information about the build output artifact location, as follows:
        
                      * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
                       
                      * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                       
                      * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
                       
                    - **path** *(string) --* 
        
                      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                      * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                       
                      * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                       
                      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
                       
                      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
                    - **namespaceType** *(string) --* 
        
                      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
                      * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                       
                      * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                       
                      * If ``type`` is set to ``S3`` , then valid values include: 
        
                        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                         
                        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                         
                      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
                    - **name** *(string) --* 
        
                      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                      * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                       
                      * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                       
                      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
                       
                      For example:
        
                      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
                       
                      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
                       
                      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
                       
                    - **packaging** *(string) --* 
        
                      The type of build output artifact to create, as follows:
        
                      * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
                       
                      * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                       
                      * If ``type`` is set to ``S3`` , valid values include: 
        
                        * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                         
                        * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                         
                    - **overrideArtifactName** *(boolean) --* 
        
                      If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                    - **encryptionDisabled** *(boolean) --* 
        
                      Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
                    - **artifactIdentifier** *(string) --* 
        
                      An identifier for this artifact definition. 
        
                - **cache** *(dict) --* 
        
                  Information about the cache for the build project.
        
                  - **type** *(string) --* 
        
                    The type of cache used by the build project. Valid values include:
        
                    * ``NO_CACHE`` : The build project will not use any cache. 
                     
                    * ``S3`` : The build project will read and write from/to S3. 
                     
                  - **location** *(string) --* 
        
                    Information about the cache location, as follows: 
        
                    * ``NO_CACHE`` : This value will be ignored. 
                     
                    * ``S3`` : This is the S3 bucket name/prefix. 
                     
                - **environment** *(dict) --* 
        
                  Information about the build environment for this build project.
        
                  - **type** *(string) --* 
        
                    The type of build environment to use for related builds.
        
                  - **image** *(string) --* 
        
                    The ID of the Docker image to use for this build project.
        
                  - **computeType** *(string) --* 
        
                    Information about the compute resources the build project will use. Available values include:
        
                    * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
                     
                    * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
                     
                    * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
                     
                  - **environmentVariables** *(list) --* 
        
                    A set of environment variables to make available to builds for this build project.
        
                    - *(dict) --* 
        
                      Information about an environment variable for a build project or a build.
        
                      - **name** *(string) --* 
        
                        The name or key of the environment variable.
        
                      - **value** *(string) --* 
        
                        The value of the environment variable.
        
                        .. warning::
        
                          We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
                      - **type** *(string) --* 
        
                        The type of environment variable. Valid values include:
        
                        * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                         
                        * ``PLAINTEXT`` : An environment variable in plaintext format. 
                         
                  - **privilegedMode** *(boolean) --* 
        
                    Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
        
                    If the operating system\'s base image is Ubuntu Linux:
        
                     ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                    If the operating system\'s base image is Alpine Linux, add the ``-t`` argument to ``timeout`` :
        
                     ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                  - **certificate** *(string) --* 
        
                    The certificate to use with this build project.
        
                - **serviceRole** *(string) --* 
        
                  The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
        
                - **timeoutInMinutes** *(integer) --* 
        
                  How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.
        
                - **encryptionKey** *(string) --* 
        
                  The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
        
                  This is expressed either as the CMK\'s Amazon Resource Name (ARN) or, if specified, the CMK\'s alias (using the format ``alias/*alias-name* `` ).
        
                - **tags** *(list) --* 
        
                  The tags for this build project.
        
                  These tags are available for use by AWS services that support AWS CodeBuild build project tags.
        
                  - *(dict) --* 
        
                    A tag, consisting of a key and a value.
        
                    This tag is available for use by AWS services that support tags in AWS CodeBuild.
        
                    - **key** *(string) --* 
        
                      The tag\'s key.
        
                    - **value** *(string) --* 
        
                      The tag\'s value.
        
                - **created** *(datetime) --* 
        
                  When the build project was created, expressed in Unix time format.
        
                - **lastModified** *(datetime) --* 
        
                  When the build project\'s settings were last modified, expressed in Unix time format.
        
                - **webhook** *(dict) --* 
        
                  Information about a webhook that connects repository events to a build project in AWS CodeBuild.
        
                  - **url** *(string) --* 
        
                    The URL to the webhook.
        
                  - **payloadUrl** *(string) --* 
        
                    The CodeBuild endpoint where webhook events are sent.
        
                  - **secret** *(string) --* 
        
                    The secret token of the associated repository. 
        
                    .. note::
        
                      A Bitbucket webhook does not support ``secret`` . 
        
                  - **branchFilter** *(string) --* 
        
                    A regular expression used to determine which branches in a repository are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If it doesn\'t match, then it is not. If ``branchFilter`` is empty, then all branches are built.
        
                  - **lastModifiedSecret** *(datetime) --* 
        
                    A timestamp indicating the last time a repository\'s secret token was modified. 
        
                - **vpcConfig** *(dict) --* 
        
                  Information about the VPC configuration that AWS CodeBuild will access.
        
                  - **vpcId** *(string) --* 
        
                    The ID of the Amazon VPC.
        
                  - **subnets** *(list) --* 
        
                    A list of one or more subnet IDs in your Amazon VPC.
        
                    - *(string) --* 
                
                  - **securityGroupIds** *(list) --* 
        
                    A list of one or more security groups IDs in your Amazon VPC.
        
                    - *(string) --* 
                
                - **badge** *(dict) --* 
        
                  Information about the build badge for the build project.
        
                  - **badgeEnabled** *(boolean) --* 
        
                    Set this to true to generate a publicly-accessible URL for your project\'s build badge.
        
                  - **badgeRequestUrl** *(string) --* 
        
                    The publicly-accessible URL through which you can access the build badge for your project. 
        
                - **logsConfig** *(dict) --* 
        
                  Information about logs for the build project. A project can create Amazon CloudWatch Logs, logs in an S3 bucket, or both. 
        
                  - **cloudWatchLogs** *(dict) --* 
        
                    Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default. 
        
                    - **status** *(string) --* 
        
                      The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
                      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
                       
                      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
                       
                    - **groupName** *(string) --* 
        
                      The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                    - **streamName** *(string) --* 
        
                      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                  - **s3Logs** *(dict) --* 
        
                    Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default. 
        
                    - **status** *(string) --* 
        
                      The current status of the S3 build logs. Valid values are:
        
                      * ``ENABLED`` : S3 build logs are enabled for this build project. 
                       
                      * ``DISABLED`` : S3 build logs are not enabled for this build project. 
                       
                    - **location** *(string) --* 
        
                      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
            - **projectsNotFound** *(list) --* 
        
              The names of build projects for which information could not be found.
        
              - *(string) --* 
          
        """
        pass

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

    def create_project(self, name: str, source: Dict, artifacts: Dict, environment: Dict, serviceRole: str, description: str = None, secondarySources: List = None, secondaryArtifacts: List = None, cache: Dict = None, timeoutInMinutes: int = None, encryptionKey: str = None, tags: List = None, vpcConfig: Dict = None, badgeEnabled: bool = None, logsConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/CreateProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_project(
              name=\'string\',
              description=\'string\',
              source={
                  \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                  \'location\': \'string\',
                  \'gitCloneDepth\': 123,
                  \'buildspec\': \'string\',
                  \'auth\': {
                      \'type\': \'OAUTH\',
                      \'resource\': \'string\'
                  },
                  \'reportBuildStatus\': True|False,
                  \'insecureSsl\': True|False,
                  \'sourceIdentifier\': \'string\'
              },
              secondarySources=[
                  {
                      \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                      \'location\': \'string\',
                      \'gitCloneDepth\': 123,
                      \'buildspec\': \'string\',
                      \'auth\': {
                          \'type\': \'OAUTH\',
                          \'resource\': \'string\'
                      },
                      \'reportBuildStatus\': True|False,
                      \'insecureSsl\': True|False,
                      \'sourceIdentifier\': \'string\'
                  },
              ],
              artifacts={
                  \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                  \'location\': \'string\',
                  \'path\': \'string\',
                  \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                  \'name\': \'string\',
                  \'packaging\': \'NONE\'|\'ZIP\',
                  \'overrideArtifactName\': True|False,
                  \'encryptionDisabled\': True|False,
                  \'artifactIdentifier\': \'string\'
              },
              secondaryArtifacts=[
                  {
                      \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                      \'location\': \'string\',
                      \'path\': \'string\',
                      \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                      \'name\': \'string\',
                      \'packaging\': \'NONE\'|\'ZIP\',
                      \'overrideArtifactName\': True|False,
                      \'encryptionDisabled\': True|False,
                      \'artifactIdentifier\': \'string\'
                  },
              ],
              cache={
                  \'type\': \'NO_CACHE\'|\'S3\',
                  \'location\': \'string\'
              },
              environment={
                  \'type\': \'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
                  \'image\': \'string\',
                  \'computeType\': \'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
                  \'environmentVariables\': [
                      {
                          \'name\': \'string\',
                          \'value\': \'string\',
                          \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                      },
                  ],
                  \'privilegedMode\': True|False,
                  \'certificate\': \'string\'
              },
              serviceRole=\'string\',
              timeoutInMinutes=123,
              encryptionKey=\'string\',
              tags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ],
              vpcConfig={
                  \'vpcId\': \'string\',
                  \'subnets\': [
                      \'string\',
                  ],
                  \'securityGroupIds\': [
                      \'string\',
                  ]
              },
              badgeEnabled=True|False,
              logsConfig={
                  \'cloudWatchLogs\': {
                      \'status\': \'ENABLED\'|\'DISABLED\',
                      \'groupName\': \'string\',
                      \'streamName\': \'string\'
                  },
                  \'s3Logs\': {
                      \'status\': \'ENABLED\'|\'DISABLED\',
                      \'location\': \'string\'
                  }
              }
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the build project.
        
        :type description: string
        :param description: 
        
          A description that makes the build project easy to identify.
        
        :type source: dict
        :param source: **[REQUIRED]** 
        
          Information about the build input source code for the build project.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of repository that contains the source code to be built. Valid values include:
        
            * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
             
            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
             
            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
             
            * ``GITHUB`` : The source code is in a GitHub repository. 
             
            * ``NO_SOURCE`` : The project does not have input source code. 
             
            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
             
          - **location** *(string) --* 
        
            Information about the location of the source code to be built. Valid values include:
        
            * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
             
            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
             
            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
              * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
               
              * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
               
            * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
             
            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
             
          - **gitCloneDepth** *(integer) --* 
        
            Information about the git clone depth for the build project.
        
          - **buildspec** *(string) --* 
        
            The build spec declaration to use for the builds in this build project.
        
            If this value is not specified, a build spec must be included along with the source code to be built.
        
          - **auth** *(dict) --* 
        
            Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
            This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
            - **resource** *(string) --* 
        
              The resource value that applies to the specified authorization type.
        
          - **reportBuildStatus** *(boolean) --* 
        
            Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
          - **insecureSsl** *(boolean) --* 
        
            Enable this flag to ignore SSL warnings while connecting to the project source code.
        
          - **sourceIdentifier** *(string) --* 
        
            An identifier for this project source. 
        
        :type secondarySources: list
        :param secondarySources: 
        
          An array of ``ProjectSource`` objects. 
        
          - *(dict) --* 
        
            Information about the build input source code for the build project.
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The type of repository that contains the source code to be built. Valid values include:
        
              * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
               
              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
               
              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
               
              * ``GITHUB`` : The source code is in a GitHub repository. 
               
              * ``NO_SOURCE`` : The project does not have input source code. 
               
              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
               
            - **location** *(string) --* 
        
              Information about the location of the source code to be built. Valid values include:
        
              * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
               
              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
               
              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                 
                * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                 
              * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
               
              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
               
            - **gitCloneDepth** *(integer) --* 
        
              Information about the git clone depth for the build project.
        
            - **buildspec** *(string) --* 
        
              The build spec declaration to use for the builds in this build project.
        
              If this value is not specified, a build spec must be included along with the source code to be built.
        
            - **auth** *(dict) --* 
        
              Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
              This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
              - **type** *(string) --* **[REQUIRED]** 
        
                The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
              - **resource** *(string) --* 
        
                The resource value that applies to the specified authorization type.
        
            - **reportBuildStatus** *(boolean) --* 
        
              Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
            - **insecureSsl** *(boolean) --* 
        
              Enable this flag to ignore SSL warnings while connecting to the project source code.
        
            - **sourceIdentifier** *(string) --* 
        
              An identifier for this project source. 
        
        :type artifacts: dict
        :param artifacts: **[REQUIRED]** 
        
          Information about the build output artifacts for the build project.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of build output artifact. Valid values include:
        
            * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
             
            * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
             
            * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
             
          - **location** *(string) --* 
        
            Information about the build output artifact location, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
             
          - **path** *(string) --* 
        
            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
             
            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
          - **namespaceType** *(string) --* 
        
            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , then valid values include: 
        
              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
               
              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
               
            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
          - **name** *(string) --* 
        
            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
             
            For example:
        
            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
             
            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
             
            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
             
          - **packaging** *(string) --* 
        
            The type of build output artifact to create, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , valid values include: 
        
              * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
               
              * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
               
          - **overrideArtifactName** *(boolean) --* 
        
            If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
          - **encryptionDisabled** *(boolean) --* 
        
            Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
          - **artifactIdentifier** *(string) --* 
        
            An identifier for this artifact definition. 
        
        :type secondaryArtifacts: list
        :param secondaryArtifacts: 
        
          An array of ``ProjectArtifacts`` objects. 
        
          - *(dict) --* 
        
            Information about the build output artifacts for the build project.
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The type of build output artifact. Valid values include:
        
              * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
               
              * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
               
              * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
               
            - **location** *(string) --* 
        
              Information about the build output artifact location, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
               
            - **path** *(string) --* 
        
              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
               
              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
            - **namespaceType** *(string) --* 
        
              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , then valid values include: 
        
                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                 
                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                 
              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
            - **name** *(string) --* 
        
              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
               
              For example:
        
              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
               
              * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
               
              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
               
            - **packaging** *(string) --* 
        
              The type of build output artifact to create, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , valid values include: 
        
                * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                 
                * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                 
            - **overrideArtifactName** *(boolean) --* 
        
              If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
            - **encryptionDisabled** *(boolean) --* 
        
              Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
            - **artifactIdentifier** *(string) --* 
        
              An identifier for this artifact definition. 
        
        :type cache: dict
        :param cache: 
        
          Stores recently used information so that it can be quickly accessed at a later time.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of cache used by the build project. Valid values include:
        
            * ``NO_CACHE`` : The build project will not use any cache. 
             
            * ``S3`` : The build project will read and write from/to S3. 
             
          - **location** *(string) --* 
        
            Information about the cache location, as follows: 
        
            * ``NO_CACHE`` : This value will be ignored. 
             
            * ``S3`` : This is the S3 bucket name/prefix. 
             
        :type environment: dict
        :param environment: **[REQUIRED]** 
        
          Information about the build environment for the build project.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of build environment to use for related builds.
        
          - **image** *(string) --* **[REQUIRED]** 
        
            The ID of the Docker image to use for this build project.
        
          - **computeType** *(string) --* **[REQUIRED]** 
        
            Information about the compute resources the build project will use. Available values include:
        
            * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
             
            * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
             
            * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
             
          - **environmentVariables** *(list) --* 
        
            A set of environment variables to make available to builds for this build project.
        
            - *(dict) --* 
        
              Information about an environment variable for a build project or a build.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name or key of the environment variable.
        
              - **value** *(string) --* **[REQUIRED]** 
        
                The value of the environment variable.
        
                .. warning::
        
                  We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
              - **type** *(string) --* 
        
                The type of environment variable. Valid values include:
        
                * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                 
                * ``PLAINTEXT`` : An environment variable in plaintext format. 
                 
          - **privilegedMode** *(boolean) --* 
        
            Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
        
            If the operating system\'s base image is Ubuntu Linux:
        
             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
            If the operating system\'s base image is Alpine Linux, add the ``-t`` argument to ``timeout`` :
        
             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
          - **certificate** *(string) --* 
        
            The certificate to use with this build project.
        
        :type serviceRole: string
        :param serviceRole: **[REQUIRED]** 
        
          The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
        
        :type timeoutInMinutes: integer
        :param timeoutInMinutes: 
        
          How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any build that has not been marked as completed. The default is 60 minutes.
        
        :type encryptionKey: string
        :param encryptionKey: 
        
          The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
        
          You can specify either the CMK\'s Amazon Resource Name (ARN) or, if available, the CMK\'s alias (using the format ``alias/*alias-name* `` ).
        
        :type tags: list
        :param tags: 
        
          A set of tags for this build project.
        
          These tags are available for use by AWS services that support AWS CodeBuild build project tags.
        
          - *(dict) --* 
        
            A tag, consisting of a key and a value.
        
            This tag is available for use by AWS services that support tags in AWS CodeBuild.
        
            - **key** *(string) --* 
        
              The tag\'s key.
        
            - **value** *(string) --* 
        
              The tag\'s value.
        
        :type vpcConfig: dict
        :param vpcConfig: 
        
          VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
        
          - **vpcId** *(string) --* 
        
            The ID of the Amazon VPC.
        
          - **subnets** *(list) --* 
        
            A list of one or more subnet IDs in your Amazon VPC.
        
            - *(string) --* 
        
          - **securityGroupIds** *(list) --* 
        
            A list of one or more security groups IDs in your Amazon VPC.
        
            - *(string) --* 
        
        :type badgeEnabled: boolean
        :param badgeEnabled: 
        
          Set this to true to generate a publicly-accessible URL for your project\'s build badge.
        
        :type logsConfig: dict
        :param logsConfig: 
        
          Information about logs for the build project. Logs can be Amazon CloudWatch Logs, uploaded to a specified S3 bucket, or both. 
        
          - **cloudWatchLogs** *(dict) --* 
        
            Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default. 
        
            - **status** *(string) --* **[REQUIRED]** 
        
              The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
              * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
               
              * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
               
            - **groupName** *(string) --* 
        
              The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
            - **streamName** *(string) --* 
        
              The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
          - **s3Logs** *(dict) --* 
        
            Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default. 
        
            - **status** *(string) --* **[REQUIRED]** 
        
              The current status of the S3 build logs. Valid values are:
        
              * ``ENABLED`` : S3 build logs are enabled for this build project. 
               
              * ``DISABLED`` : S3 build logs are not enabled for this build project. 
               
            - **location** *(string) --* 
        
              The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'project\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'description\': \'string\',
                    \'source\': {
                        \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                        \'location\': \'string\',
                        \'gitCloneDepth\': 123,
                        \'buildspec\': \'string\',
                        \'auth\': {
                            \'type\': \'OAUTH\',
                            \'resource\': \'string\'
                        },
                        \'reportBuildStatus\': True|False,
                        \'insecureSsl\': True|False,
                        \'sourceIdentifier\': \'string\'
                    },
                    \'secondarySources\': [
                        {
                            \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                            \'location\': \'string\',
                            \'gitCloneDepth\': 123,
                            \'buildspec\': \'string\',
                            \'auth\': {
                                \'type\': \'OAUTH\',
                                \'resource\': \'string\'
                            },
                            \'reportBuildStatus\': True|False,
                            \'insecureSsl\': True|False,
                            \'sourceIdentifier\': \'string\'
                        },
                    ],
                    \'artifacts\': {
                        \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                        \'location\': \'string\',
                        \'path\': \'string\',
                        \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                        \'name\': \'string\',
                        \'packaging\': \'NONE\'|\'ZIP\',
                        \'overrideArtifactName\': True|False,
                        \'encryptionDisabled\': True|False,
                        \'artifactIdentifier\': \'string\'
                    },
                    \'secondaryArtifacts\': [
                        {
                            \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                            \'location\': \'string\',
                            \'path\': \'string\',
                            \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                            \'name\': \'string\',
                            \'packaging\': \'NONE\'|\'ZIP\',
                            \'overrideArtifactName\': True|False,
                            \'encryptionDisabled\': True|False,
                            \'artifactIdentifier\': \'string\'
                        },
                    ],
                    \'cache\': {
                        \'type\': \'NO_CACHE\'|\'S3\',
                        \'location\': \'string\'
                    },
                    \'environment\': {
                        \'type\': \'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
                        \'image\': \'string\',
                        \'computeType\': \'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
                        \'environmentVariables\': [
                            {
                                \'name\': \'string\',
                                \'value\': \'string\',
                                \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                            },
                        ],
                        \'privilegedMode\': True|False,
                        \'certificate\': \'string\'
                    },
                    \'serviceRole\': \'string\',
                    \'timeoutInMinutes\': 123,
                    \'encryptionKey\': \'string\',
                    \'tags\': [
                        {
                            \'key\': \'string\',
                            \'value\': \'string\'
                        },
                    ],
                    \'created\': datetime(2015, 1, 1),
                    \'lastModified\': datetime(2015, 1, 1),
                    \'webhook\': {
                        \'url\': \'string\',
                        \'payloadUrl\': \'string\',
                        \'secret\': \'string\',
                        \'branchFilter\': \'string\',
                        \'lastModifiedSecret\': datetime(2015, 1, 1)
                    },
                    \'vpcConfig\': {
                        \'vpcId\': \'string\',
                        \'subnets\': [
                            \'string\',
                        ],
                        \'securityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'badge\': {
                        \'badgeEnabled\': True|False,
                        \'badgeRequestUrl\': \'string\'
                    },
                    \'logsConfig\': {
                        \'cloudWatchLogs\': {
                            \'status\': \'ENABLED\'|\'DISABLED\',
                            \'groupName\': \'string\',
                            \'streamName\': \'string\'
                        },
                        \'s3Logs\': {
                            \'status\': \'ENABLED\'|\'DISABLED\',
                            \'location\': \'string\'
                        }
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **project** *(dict) --* 
        
              Information about the build project that was created.
        
              - **name** *(string) --* 
        
                The name of the build project.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the build project.
        
              - **description** *(string) --* 
        
                A description that makes the build project easy to identify.
        
              - **source** *(dict) --* 
        
                Information about the build input source code for this build project.
        
                - **type** *(string) --* 
        
                  The type of repository that contains the source code to be built. Valid values include:
        
                  * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                   
                  * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                   
                  * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                   
                  * ``GITHUB`` : The source code is in a GitHub repository. 
                   
                  * ``NO_SOURCE`` : The project does not have input source code. 
                   
                  * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                   
                - **location** *(string) --* 
        
                  Information about the location of the source code to be built. Valid values include:
        
                  * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                   
                  * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                   
                  * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                    * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                     
                    * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                     
                  * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                   
                  * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                   
                - **gitCloneDepth** *(integer) --* 
        
                  Information about the git clone depth for the build project.
        
                - **buildspec** *(string) --* 
        
                  The build spec declaration to use for the builds in this build project.
        
                  If this value is not specified, a build spec must be included along with the source code to be built.
        
                - **auth** *(dict) --* 
        
                  Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                  This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                  - **type** *(string) --* 
        
                    The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                  - **resource** *(string) --* 
        
                    The resource value that applies to the specified authorization type.
        
                - **reportBuildStatus** *(boolean) --* 
        
                  Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                - **insecureSsl** *(boolean) --* 
        
                  Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                - **sourceIdentifier** *(string) --* 
        
                  An identifier for this project source. 
        
              - **secondarySources** *(list) --* 
        
                An array of ``ProjectSource`` objects. 
        
                - *(dict) --* 
        
                  Information about the build input source code for the build project.
        
                  - **type** *(string) --* 
        
                    The type of repository that contains the source code to be built. Valid values include:
        
                    * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                     
                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                     
                    * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                     
                    * ``GITHUB`` : The source code is in a GitHub repository. 
                     
                    * ``NO_SOURCE`` : The project does not have input source code. 
                     
                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                     
                  - **location** *(string) --* 
        
                    Information about the location of the source code to be built. Valid values include:
        
                    * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                     
                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                     
                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                      * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                       
                      * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                       
                    * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                    * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                  - **gitCloneDepth** *(integer) --* 
        
                    Information about the git clone depth for the build project.
        
                  - **buildspec** *(string) --* 
        
                    The build spec declaration to use for the builds in this build project.
        
                    If this value is not specified, a build spec must be included along with the source code to be built.
        
                  - **auth** *(dict) --* 
        
                    Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                    This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                    - **type** *(string) --* 
        
                      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                    - **resource** *(string) --* 
        
                      The resource value that applies to the specified authorization type.
        
                  - **reportBuildStatus** *(boolean) --* 
        
                    Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                  - **insecureSsl** *(boolean) --* 
        
                    Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                  - **sourceIdentifier** *(string) --* 
        
                    An identifier for this project source. 
        
              - **artifacts** *(dict) --* 
        
                Information about the build output artifacts for the build project.
        
                - **type** *(string) --* 
        
                  The type of build output artifact. Valid values include:
        
                  * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
                   
                  * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
                   
                  * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
                   
                - **location** *(string) --* 
        
                  Information about the build output artifact location, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
                   
                - **path** *(string) --* 
        
                  Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
                   
                  For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
                - **namespaceType** *(string) --* 
        
                  Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , then valid values include: 
        
                    * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                     
                    * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                     
                  For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
                - **name** *(string) --* 
        
                  Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
                   
                  For example:
        
                  * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
                   
                  * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
                   
                  * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
                   
                - **packaging** *(string) --* 
        
                  The type of build output artifact to create, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , valid values include: 
        
                    * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                     
                    * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                     
                - **overrideArtifactName** *(boolean) --* 
        
                  If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                - **encryptionDisabled** *(boolean) --* 
        
                  Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
                - **artifactIdentifier** *(string) --* 
        
                  An identifier for this artifact definition. 
        
              - **secondaryArtifacts** *(list) --* 
        
                An array of ``ProjectArtifacts`` objects. 
        
                - *(dict) --* 
        
                  Information about the build output artifacts for the build project.
        
                  - **type** *(string) --* 
        
                    The type of build output artifact. Valid values include:
        
                    * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
                     
                    * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
                     
                    * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
                     
                  - **location** *(string) --* 
        
                    Information about the build output artifact location, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
                     
                  - **path** *(string) --* 
        
                    Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
                     
                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
                  - **namespaceType** *(string) --* 
        
                    Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , then valid values include: 
        
                      * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                       
                      * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                       
                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
                  - **name** *(string) --* 
        
                    Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
                     
                    For example:
        
                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
                     
                    * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
                     
                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
                     
                  - **packaging** *(string) --* 
        
                    The type of build output artifact to create, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , valid values include: 
        
                      * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                       
                      * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                       
                  - **overrideArtifactName** *(boolean) --* 
        
                    If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                  - **encryptionDisabled** *(boolean) --* 
        
                    Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
                  - **artifactIdentifier** *(string) --* 
        
                    An identifier for this artifact definition. 
        
              - **cache** *(dict) --* 
        
                Information about the cache for the build project.
        
                - **type** *(string) --* 
        
                  The type of cache used by the build project. Valid values include:
        
                  * ``NO_CACHE`` : The build project will not use any cache. 
                   
                  * ``S3`` : The build project will read and write from/to S3. 
                   
                - **location** *(string) --* 
        
                  Information about the cache location, as follows: 
        
                  * ``NO_CACHE`` : This value will be ignored. 
                   
                  * ``S3`` : This is the S3 bucket name/prefix. 
                   
              - **environment** *(dict) --* 
        
                Information about the build environment for this build project.
        
                - **type** *(string) --* 
        
                  The type of build environment to use for related builds.
        
                - **image** *(string) --* 
        
                  The ID of the Docker image to use for this build project.
        
                - **computeType** *(string) --* 
        
                  Information about the compute resources the build project will use. Available values include:
        
                  * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
                   
                  * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
                   
                  * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
                   
                - **environmentVariables** *(list) --* 
        
                  A set of environment variables to make available to builds for this build project.
        
                  - *(dict) --* 
        
                    Information about an environment variable for a build project or a build.
        
                    - **name** *(string) --* 
        
                      The name or key of the environment variable.
        
                    - **value** *(string) --* 
        
                      The value of the environment variable.
        
                      .. warning::
        
                        We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
                    - **type** *(string) --* 
        
                      The type of environment variable. Valid values include:
        
                      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                       
                      * ``PLAINTEXT`` : An environment variable in plaintext format. 
                       
                - **privilegedMode** *(boolean) --* 
        
                  Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
        
                  If the operating system\'s base image is Ubuntu Linux:
        
                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                  If the operating system\'s base image is Alpine Linux, add the ``-t`` argument to ``timeout`` :
        
                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                - **certificate** *(string) --* 
        
                  The certificate to use with this build project.
        
              - **serviceRole** *(string) --* 
        
                The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
        
              - **timeoutInMinutes** *(integer) --* 
        
                How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.
        
              - **encryptionKey** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
        
                This is expressed either as the CMK\'s Amazon Resource Name (ARN) or, if specified, the CMK\'s alias (using the format ``alias/*alias-name* `` ).
        
              - **tags** *(list) --* 
        
                The tags for this build project.
        
                These tags are available for use by AWS services that support AWS CodeBuild build project tags.
        
                - *(dict) --* 
        
                  A tag, consisting of a key and a value.
        
                  This tag is available for use by AWS services that support tags in AWS CodeBuild.
        
                  - **key** *(string) --* 
        
                    The tag\'s key.
        
                  - **value** *(string) --* 
        
                    The tag\'s value.
        
              - **created** *(datetime) --* 
        
                When the build project was created, expressed in Unix time format.
        
              - **lastModified** *(datetime) --* 
        
                When the build project\'s settings were last modified, expressed in Unix time format.
        
              - **webhook** *(dict) --* 
        
                Information about a webhook that connects repository events to a build project in AWS CodeBuild.
        
                - **url** *(string) --* 
        
                  The URL to the webhook.
        
                - **payloadUrl** *(string) --* 
        
                  The CodeBuild endpoint where webhook events are sent.
        
                - **secret** *(string) --* 
        
                  The secret token of the associated repository. 
        
                  .. note::
        
                    A Bitbucket webhook does not support ``secret`` . 
        
                - **branchFilter** *(string) --* 
        
                  A regular expression used to determine which branches in a repository are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If it doesn\'t match, then it is not. If ``branchFilter`` is empty, then all branches are built.
        
                - **lastModifiedSecret** *(datetime) --* 
        
                  A timestamp indicating the last time a repository\'s secret token was modified. 
        
              - **vpcConfig** *(dict) --* 
        
                Information about the VPC configuration that AWS CodeBuild will access.
        
                - **vpcId** *(string) --* 
        
                  The ID of the Amazon VPC.
        
                - **subnets** *(list) --* 
        
                  A list of one or more subnet IDs in your Amazon VPC.
        
                  - *(string) --* 
              
                - **securityGroupIds** *(list) --* 
        
                  A list of one or more security groups IDs in your Amazon VPC.
        
                  - *(string) --* 
              
              - **badge** *(dict) --* 
        
                Information about the build badge for the build project.
        
                - **badgeEnabled** *(boolean) --* 
        
                  Set this to true to generate a publicly-accessible URL for your project\'s build badge.
        
                - **badgeRequestUrl** *(string) --* 
        
                  The publicly-accessible URL through which you can access the build badge for your project. 
        
              - **logsConfig** *(dict) --* 
        
                Information about logs for the build project. A project can create Amazon CloudWatch Logs, logs in an S3 bucket, or both. 
        
                - **cloudWatchLogs** *(dict) --* 
        
                  Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default. 
        
                  - **status** *(string) --* 
        
                    The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
                    * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
                     
                    * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
                     
                  - **groupName** *(string) --* 
        
                    The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                  - **streamName** *(string) --* 
        
                    The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                - **s3Logs** *(dict) --* 
        
                  Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default. 
        
                  - **status** *(string) --* 
        
                    The current status of the S3 build logs. Valid values are:
        
                    * ``ENABLED`` : S3 build logs are enabled for this build project. 
                     
                    * ``DISABLED`` : S3 build logs are not enabled for this build project. 
                     
                  - **location** *(string) --* 
        
                    The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
        """
        pass

    def create_webhook(self, projectName: str, branchFilter: str = None) -> Dict:
        """
        
        .. warning::
        
          If you enable webhooks for an AWS CodeBuild project, and the project is used as a build step in AWS CodePipeline, then two identical builds will be created for each commit. One build is triggered through webhooks, and one through AWS CodePipeline. Because billing is on a per-build basis, you will be billed for both builds. Therefore, if you are using AWS CodePipeline, we recommend that you disable webhooks in CodeBuild. In the AWS CodeBuild console, clear the Webhook box. For more information, see step 5 in `Change a Build Project\'s Settings <http://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/CreateWebhook>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_webhook(
              projectName=\'string\',
              branchFilter=\'string\'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the AWS CodeBuild project.
        
        :type branchFilter: string
        :param branchFilter: 
        
          A regular expression used to determine which branches in a repository are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If it doesn\'t match, then it is not. If ``branchFilter`` is empty, then all branches are built.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'webhook\': {
                    \'url\': \'string\',
                    \'payloadUrl\': \'string\',
                    \'secret\': \'string\',
                    \'branchFilter\': \'string\',
                    \'lastModifiedSecret\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **webhook** *(dict) --* 
        
              Information about a webhook that connects repository events to a build project in AWS CodeBuild.
        
              - **url** *(string) --* 
        
                The URL to the webhook.
        
              - **payloadUrl** *(string) --* 
        
                The CodeBuild endpoint where webhook events are sent.
        
              - **secret** *(string) --* 
        
                The secret token of the associated repository. 
        
                .. note::
        
                  A Bitbucket webhook does not support ``secret`` . 
        
              - **branchFilter** *(string) --* 
        
                A regular expression used to determine which branches in a repository are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If it doesn\'t match, then it is not. If ``branchFilter`` is empty, then all branches are built.
        
              - **lastModifiedSecret** *(datetime) --* 
        
                A timestamp indicating the last time a repository\'s secret token was modified. 
        
        """
        pass

    def delete_project(self, name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_project(
              name=\'string\'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the build project.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_webhook(self, projectName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteWebhook>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_webhook(
              projectName=\'string\'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the AWS CodeBuild project.
        
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

    def invalidate_project_cache(self, projectName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/InvalidateProjectCache>`_
        
        **Request Syntax** 
        ::
        
          response = client.invalidate_project_cache(
              projectName=\'string\'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the AWS CodeBuild build project that the cache will be reset for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def list_builds(self, sortOrder: str = None, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuilds>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_builds(
              sortOrder=\'ASCENDING\'|\'DESCENDING\',
              nextToken=\'string\'
          )
        :type sortOrder: string
        :param sortOrder: 
        
          The order to list build IDs. Valid values include:
        
          * ``ASCENDING`` : List the build IDs in ascending order by build ID. 
           
          * ``DESCENDING`` : List the build IDs in descending order by build ID. 
           
        :type nextToken: string
        :param nextToken: 
        
          During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ids\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ids** *(list) --* 
        
              A list of build IDs, with each build ID representing a single build.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call.
        
        """
        pass

    def list_builds_for_project(self, projectName: str, sortOrder: str = None, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuildsForProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_builds_for_project(
              projectName=\'string\',
              sortOrder=\'ASCENDING\'|\'DESCENDING\',
              nextToken=\'string\'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the AWS CodeBuild project.
        
        :type sortOrder: string
        :param sortOrder: 
        
          The order to list build IDs. Valid values include:
        
          * ``ASCENDING`` : List the build IDs in ascending order by build ID. 
           
          * ``DESCENDING`` : List the build IDs in descending order by build ID. 
           
        :type nextToken: string
        :param nextToken: 
        
          During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ids\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ids** *(list) --* 
        
              A list of build IDs for the specified build project, with each build ID representing a single build.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call.
        
        """
        pass

    def list_curated_environment_images(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListCuratedEnvironmentImages>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_curated_environment_images()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'platforms\': [
                    {
                        \'platform\': \'DEBIAN\'|\'AMAZON_LINUX\'|\'UBUNTU\'|\'WINDOWS_SERVER\',
                        \'languages\': [
                            {
                                \'language\': \'JAVA\'|\'PYTHON\'|\'NODE_JS\'|\'RUBY\'|\'GOLANG\'|\'DOCKER\'|\'ANDROID\'|\'DOTNET\'|\'BASE\',
                                \'images\': [
                                    {
                                        \'name\': \'string\',
                                        \'description\': \'string\',
                                        \'versions\': [
                                            \'string\',
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **platforms** *(list) --* 
        
              Information about supported platforms for Docker images that are managed by AWS CodeBuild.
        
              - *(dict) --* 
        
                A set of Docker images that are related by platform and are managed by AWS CodeBuild.
        
                - **platform** *(string) --* 
        
                  The platform\'s name.
        
                - **languages** *(list) --* 
        
                  The list of programming languages that are available for the specified platform.
        
                  - *(dict) --* 
        
                    A set of Docker images that are related by programming language and are managed by AWS CodeBuild.
        
                    - **language** *(string) --* 
        
                      The programming language for the Docker images.
        
                    - **images** *(list) --* 
        
                      The list of Docker images that are related by the specified programming language.
        
                      - *(dict) --* 
        
                        Information about a Docker image that is managed by AWS CodeBuild.
        
                        - **name** *(string) --* 
        
                          The name of the Docker image.
        
                        - **description** *(string) --* 
        
                          The description of the Docker image.
        
                        - **versions** *(list) --* 
        
                          A list of environment image versions.
        
                          - *(string) --* 
                      
        """
        pass

    def list_projects(self, sortBy: str = None, sortOrder: str = None, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListProjects>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_projects(
              sortBy=\'NAME\'|\'CREATED_TIME\'|\'LAST_MODIFIED_TIME\',
              sortOrder=\'ASCENDING\'|\'DESCENDING\',
              nextToken=\'string\'
          )
        :type sortBy: string
        :param sortBy: 
        
          The criterion to be used to list build project names. Valid values include:
        
          * ``CREATED_TIME`` : List the build project names based on when each build project was created. 
           
          * ``LAST_MODIFIED_TIME`` : List the build project names based on when information about each build project was last changed. 
           
          * ``NAME`` : List the build project names based on each build project\'s name. 
           
          Use ``sortOrder`` to specify in what order to list the build project names based on the preceding criteria.
        
        :type sortOrder: string
        :param sortOrder: 
        
          The order in which to list build projects. Valid values include:
        
          * ``ASCENDING`` : List the build project names in ascending order. 
           
          * ``DESCENDING`` : List the build project names in descending order. 
           
          Use ``sortBy`` to specify the criterion to be used to list build project names.
        
        :type nextToken: string
        :param nextToken: 
        
          During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'nextToken\': \'string\',
                \'projects\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **nextToken** *(string) --* 
        
              If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call.
        
            - **projects** *(list) --* 
        
              The list of build project names, with each build project name representing a single build project.
        
              - *(string) --* 
          
        """
        pass

    def start_build(self, projectName: str, secondarySourcesOverride: List = None, secondarySourcesVersionOverride: List = None, sourceVersion: str = None, artifactsOverride: Dict = None, secondaryArtifactsOverride: List = None, environmentVariablesOverride: List = None, sourceTypeOverride: str = None, sourceLocationOverride: str = None, sourceAuthOverride: Dict = None, gitCloneDepthOverride: int = None, buildspecOverride: str = None, insecureSslOverride: bool = None, reportBuildStatusOverride: bool = None, environmentTypeOverride: str = None, imageOverride: str = None, computeTypeOverride: str = None, certificateOverride: str = None, cacheOverride: Dict = None, serviceRoleOverride: str = None, privilegedModeOverride: bool = None, timeoutInMinutesOverride: int = None, idempotencyToken: str = None, logsConfigOverride: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StartBuild>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_build(
              projectName=\'string\',
              secondarySourcesOverride=[
                  {
                      \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                      \'location\': \'string\',
                      \'gitCloneDepth\': 123,
                      \'buildspec\': \'string\',
                      \'auth\': {
                          \'type\': \'OAUTH\',
                          \'resource\': \'string\'
                      },
                      \'reportBuildStatus\': True|False,
                      \'insecureSsl\': True|False,
                      \'sourceIdentifier\': \'string\'
                  },
              ],
              secondarySourcesVersionOverride=[
                  {
                      \'sourceIdentifier\': \'string\',
                      \'sourceVersion\': \'string\'
                  },
              ],
              sourceVersion=\'string\',
              artifactsOverride={
                  \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                  \'location\': \'string\',
                  \'path\': \'string\',
                  \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                  \'name\': \'string\',
                  \'packaging\': \'NONE\'|\'ZIP\',
                  \'overrideArtifactName\': True|False,
                  \'encryptionDisabled\': True|False,
                  \'artifactIdentifier\': \'string\'
              },
              secondaryArtifactsOverride=[
                  {
                      \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                      \'location\': \'string\',
                      \'path\': \'string\',
                      \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                      \'name\': \'string\',
                      \'packaging\': \'NONE\'|\'ZIP\',
                      \'overrideArtifactName\': True|False,
                      \'encryptionDisabled\': True|False,
                      \'artifactIdentifier\': \'string\'
                  },
              ],
              environmentVariablesOverride=[
                  {
                      \'name\': \'string\',
                      \'value\': \'string\',
                      \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                  },
              ],
              sourceTypeOverride=\'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
              sourceLocationOverride=\'string\',
              sourceAuthOverride={
                  \'type\': \'OAUTH\',
                  \'resource\': \'string\'
              },
              gitCloneDepthOverride=123,
              buildspecOverride=\'string\',
              insecureSslOverride=True|False,
              reportBuildStatusOverride=True|False,
              environmentTypeOverride=\'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
              imageOverride=\'string\',
              computeTypeOverride=\'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
              certificateOverride=\'string\',
              cacheOverride={
                  \'type\': \'NO_CACHE\'|\'S3\',
                  \'location\': \'string\'
              },
              serviceRoleOverride=\'string\',
              privilegedModeOverride=True|False,
              timeoutInMinutesOverride=123,
              idempotencyToken=\'string\',
              logsConfigOverride={
                  \'cloudWatchLogs\': {
                      \'status\': \'ENABLED\'|\'DISABLED\',
                      \'groupName\': \'string\',
                      \'streamName\': \'string\'
                  },
                  \'s3Logs\': {
                      \'status\': \'ENABLED\'|\'DISABLED\',
                      \'location\': \'string\'
                  }
              }
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the AWS CodeBuild build project to start running a build.
        
        :type secondarySourcesOverride: list
        :param secondarySourcesOverride: 
        
          An array of ``ProjectSource`` objects. 
        
          - *(dict) --* 
        
            Information about the build input source code for the build project.
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The type of repository that contains the source code to be built. Valid values include:
        
              * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
               
              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
               
              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
               
              * ``GITHUB`` : The source code is in a GitHub repository. 
               
              * ``NO_SOURCE`` : The project does not have input source code. 
               
              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
               
            - **location** *(string) --* 
        
              Information about the location of the source code to be built. Valid values include:
        
              * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
               
              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
               
              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                 
                * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                 
              * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
               
              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
               
            - **gitCloneDepth** *(integer) --* 
        
              Information about the git clone depth for the build project.
        
            - **buildspec** *(string) --* 
        
              The build spec declaration to use for the builds in this build project.
        
              If this value is not specified, a build spec must be included along with the source code to be built.
        
            - **auth** *(dict) --* 
        
              Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
              This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
              - **type** *(string) --* **[REQUIRED]** 
        
                The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
              - **resource** *(string) --* 
        
                The resource value that applies to the specified authorization type.
        
            - **reportBuildStatus** *(boolean) --* 
        
              Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
            - **insecureSsl** *(boolean) --* 
        
              Enable this flag to ignore SSL warnings while connecting to the project source code.
        
            - **sourceIdentifier** *(string) --* 
        
              An identifier for this project source. 
        
        :type secondarySourcesVersionOverride: list
        :param secondarySourcesVersionOverride: 
        
          An array of ``ProjectSourceVersion`` objects that specify one or more versions of the project\'s secondary sources to be used for this build only. 
        
          - *(dict) --* 
        
            A source identifier and its corresponding version.
        
            - **sourceIdentifier** *(string) --* **[REQUIRED]** 
        
              An identifier for a source in the build project.
        
            - **sourceVersion** *(string) --* **[REQUIRED]** 
        
              The source version for the corresponding source identifier. If specified, must be one of:
        
              * For AWS CodeCommit: the commit ID to use. 
               
              * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
               
              * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
               
              * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
               
        :type sourceVersion: string
        :param sourceVersion: 
        
          A version of the build input to be built, for this build only. If not specified, the latest version will be used. If specified, must be one of:
        
          * For AWS CodeCommit: the commit ID to use. 
           
          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
           
          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
           
          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
           
        :type artifactsOverride: dict
        :param artifactsOverride: 
        
          Build output artifact settings that override, for this build only, the latest ones already defined in the build project.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of build output artifact. Valid values include:
        
            * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
             
            * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
             
            * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
             
          - **location** *(string) --* 
        
            Information about the build output artifact location, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
             
          - **path** *(string) --* 
        
            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
             
            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
          - **namespaceType** *(string) --* 
        
            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , then valid values include: 
        
              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
               
              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
               
            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
          - **name** *(string) --* 
        
            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
             
            For example:
        
            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
             
            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
             
            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
             
          - **packaging** *(string) --* 
        
            The type of build output artifact to create, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , valid values include: 
        
              * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
               
              * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
               
          - **overrideArtifactName** *(boolean) --* 
        
            If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
          - **encryptionDisabled** *(boolean) --* 
        
            Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
          - **artifactIdentifier** *(string) --* 
        
            An identifier for this artifact definition. 
        
        :type secondaryArtifactsOverride: list
        :param secondaryArtifactsOverride: 
        
          An array of ``ProjectArtifacts`` objects. 
        
          - *(dict) --* 
        
            Information about the build output artifacts for the build project.
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The type of build output artifact. Valid values include:
        
              * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
               
              * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
               
              * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
               
            - **location** *(string) --* 
        
              Information about the build output artifact location, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
               
            - **path** *(string) --* 
        
              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
               
              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
            - **namespaceType** *(string) --* 
        
              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , then valid values include: 
        
                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                 
                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                 
              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
            - **name** *(string) --* 
        
              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
               
              For example:
        
              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
               
              * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
               
              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
               
            - **packaging** *(string) --* 
        
              The type of build output artifact to create, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , valid values include: 
        
                * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                 
                * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                 
            - **overrideArtifactName** *(boolean) --* 
        
              If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
            - **encryptionDisabled** *(boolean) --* 
        
              Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
            - **artifactIdentifier** *(string) --* 
        
              An identifier for this artifact definition. 
        
        :type environmentVariablesOverride: list
        :param environmentVariablesOverride: 
        
          A set of environment variables that overrides, for this build only, the latest ones already defined in the build project.
        
          - *(dict) --* 
        
            Information about an environment variable for a build project or a build.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name or key of the environment variable.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The value of the environment variable.
        
              .. warning::
        
                We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
            - **type** *(string) --* 
        
              The type of environment variable. Valid values include:
        
              * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
               
              * ``PLAINTEXT`` : An environment variable in plaintext format. 
               
        :type sourceTypeOverride: string
        :param sourceTypeOverride: 
        
          A source input type for this build that overrides the source input defined in the build project.
        
        :type sourceLocationOverride: string
        :param sourceLocationOverride: 
        
          A location that overrides for this build the source location for the one defined in the build project.
        
        :type sourceAuthOverride: dict
        :param sourceAuthOverride: 
        
          An authorization type for this build that overrides the one defined in the build project. This override applies only if the build project\'s source is BitBucket or GitHub.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
          - **resource** *(string) --* 
        
            The resource value that applies to the specified authorization type.
        
        :type gitCloneDepthOverride: integer
        :param gitCloneDepthOverride: 
        
          The user-defined depth of history, with a minimum value of 0, that overrides, for this build only, any previous depth of history defined in the build project.
        
        :type buildspecOverride: string
        :param buildspecOverride: 
        
          A build spec declaration that overrides, for this build only, the latest one already defined in the build project.
        
        :type insecureSslOverride: boolean
        :param insecureSslOverride: 
        
          Enable this flag to override the insecure SSL setting that is specified in the build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the build\'s source is GitHub Enterprise.
        
        :type reportBuildStatusOverride: boolean
        :param reportBuildStatusOverride: 
        
          Set to true to report to your source provider the status of a build\'s start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, or Bitbucket, an invalidInputException is thrown. 
        
        :type environmentTypeOverride: string
        :param environmentTypeOverride: 
        
          A container type for this build that overrides the one specified in the build project.
        
        :type imageOverride: string
        :param imageOverride: 
        
          The name of an image for this build that overrides the one specified in the build project.
        
        :type computeTypeOverride: string
        :param computeTypeOverride: 
        
          The name of a compute type for this build that overrides the one specified in the build project.
        
        :type certificateOverride: string
        :param certificateOverride: 
        
          The name of a certificate for this build that overrides the one specified in the build project.
        
        :type cacheOverride: dict
        :param cacheOverride: 
        
          A ProjectCache object specified for this build that overrides the one defined in the build project.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of cache used by the build project. Valid values include:
        
            * ``NO_CACHE`` : The build project will not use any cache. 
             
            * ``S3`` : The build project will read and write from/to S3. 
             
          - **location** *(string) --* 
        
            Information about the cache location, as follows: 
        
            * ``NO_CACHE`` : This value will be ignored. 
             
            * ``S3`` : This is the S3 bucket name/prefix. 
             
        :type serviceRoleOverride: string
        :param serviceRoleOverride: 
        
          The name of a service role for this build that overrides the one specified in the build project.
        
        :type privilegedModeOverride: boolean
        :param privilegedModeOverride: 
        
          Enable this flag to override privileged mode in the build project.
        
        :type timeoutInMinutesOverride: integer
        :param timeoutInMinutesOverride: 
        
          The number of build timeout minutes, from 5 to 480 (8 hours), that overrides, for this build only, the latest setting already defined in the build project.
        
        :type idempotencyToken: string
        :param idempotencyToken: 
        
          A unique, case sensitive identifier you provide to ensure the idempotency of the StartBuild request. The token is included in the StartBuild request and is valid for 12 hours. If you repeat the StartBuild request with the same token, but change a parameter, AWS CodeBuild returns a parameter mismatch error. 
        
        :type logsConfigOverride: dict
        :param logsConfigOverride: 
        
          Log settings for this build that override the log settings defined in the build project. 
        
          - **cloudWatchLogs** *(dict) --* 
        
            Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default. 
        
            - **status** *(string) --* **[REQUIRED]** 
        
              The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
              * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
               
              * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
               
            - **groupName** *(string) --* 
        
              The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
            - **streamName** *(string) --* 
        
              The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
          - **s3Logs** *(dict) --* 
        
            Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default. 
        
            - **status** *(string) --* **[REQUIRED]** 
        
              The current status of the S3 build logs. Valid values are:
        
              * ``ENABLED`` : S3 build logs are enabled for this build project. 
               
              * ``DISABLED`` : S3 build logs are not enabled for this build project. 
               
            - **location** *(string) --* 
        
              The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'build\': {
                    \'id\': \'string\',
                    \'arn\': \'string\',
                    \'startTime\': datetime(2015, 1, 1),
                    \'endTime\': datetime(2015, 1, 1),
                    \'currentPhase\': \'string\',
                    \'buildStatus\': \'SUCCEEDED\'|\'FAILED\'|\'FAULT\'|\'TIMED_OUT\'|\'IN_PROGRESS\'|\'STOPPED\',
                    \'sourceVersion\': \'string\',
                    \'resolvedSourceVersion\': \'string\',
                    \'projectName\': \'string\',
                    \'phases\': [
                        {
                            \'phaseType\': \'SUBMITTED\'|\'PROVISIONING\'|\'DOWNLOAD_SOURCE\'|\'INSTALL\'|\'PRE_BUILD\'|\'BUILD\'|\'POST_BUILD\'|\'UPLOAD_ARTIFACTS\'|\'FINALIZING\'|\'COMPLETED\',
                            \'phaseStatus\': \'SUCCEEDED\'|\'FAILED\'|\'FAULT\'|\'TIMED_OUT\'|\'IN_PROGRESS\'|\'STOPPED\',
                            \'startTime\': datetime(2015, 1, 1),
                            \'endTime\': datetime(2015, 1, 1),
                            \'durationInSeconds\': 123,
                            \'contexts\': [
                                {
                                    \'statusCode\': \'string\',
                                    \'message\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'source\': {
                        \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                        \'location\': \'string\',
                        \'gitCloneDepth\': 123,
                        \'buildspec\': \'string\',
                        \'auth\': {
                            \'type\': \'OAUTH\',
                            \'resource\': \'string\'
                        },
                        \'reportBuildStatus\': True|False,
                        \'insecureSsl\': True|False,
                        \'sourceIdentifier\': \'string\'
                    },
                    \'secondarySources\': [
                        {
                            \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                            \'location\': \'string\',
                            \'gitCloneDepth\': 123,
                            \'buildspec\': \'string\',
                            \'auth\': {
                                \'type\': \'OAUTH\',
                                \'resource\': \'string\'
                            },
                            \'reportBuildStatus\': True|False,
                            \'insecureSsl\': True|False,
                            \'sourceIdentifier\': \'string\'
                        },
                    ],
                    \'secondarySourceVersions\': [
                        {
                            \'sourceIdentifier\': \'string\',
                            \'sourceVersion\': \'string\'
                        },
                    ],
                    \'artifacts\': {
                        \'location\': \'string\',
                        \'sha256sum\': \'string\',
                        \'md5sum\': \'string\',
                        \'overrideArtifactName\': True|False,
                        \'encryptionDisabled\': True|False,
                        \'artifactIdentifier\': \'string\'
                    },
                    \'secondaryArtifacts\': [
                        {
                            \'location\': \'string\',
                            \'sha256sum\': \'string\',
                            \'md5sum\': \'string\',
                            \'overrideArtifactName\': True|False,
                            \'encryptionDisabled\': True|False,
                            \'artifactIdentifier\': \'string\'
                        },
                    ],
                    \'cache\': {
                        \'type\': \'NO_CACHE\'|\'S3\',
                        \'location\': \'string\'
                    },
                    \'environment\': {
                        \'type\': \'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
                        \'image\': \'string\',
                        \'computeType\': \'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
                        \'environmentVariables\': [
                            {
                                \'name\': \'string\',
                                \'value\': \'string\',
                                \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                            },
                        ],
                        \'privilegedMode\': True|False,
                        \'certificate\': \'string\'
                    },
                    \'serviceRole\': \'string\',
                    \'logs\': {
                        \'groupName\': \'string\',
                        \'streamName\': \'string\',
                        \'deepLink\': \'string\',
                        \'s3DeepLink\': \'string\',
                        \'cloudWatchLogs\': {
                            \'status\': \'ENABLED\'|\'DISABLED\',
                            \'groupName\': \'string\',
                            \'streamName\': \'string\'
                        },
                        \'s3Logs\': {
                            \'status\': \'ENABLED\'|\'DISABLED\',
                            \'location\': \'string\'
                        }
                    },
                    \'timeoutInMinutes\': 123,
                    \'buildComplete\': True|False,
                    \'initiator\': \'string\',
                    \'vpcConfig\': {
                        \'vpcId\': \'string\',
                        \'subnets\': [
                            \'string\',
                        ],
                        \'securityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'networkInterface\': {
                        \'subnetId\': \'string\',
                        \'networkInterfaceId\': \'string\'
                    },
                    \'encryptionKey\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **build** *(dict) --* 
        
              Information about the build to be run.
        
              - **id** *(string) --* 
        
                The unique ID for the build.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the build.
        
              - **startTime** *(datetime) --* 
        
                When the build process started, expressed in Unix time format.
        
              - **endTime** *(datetime) --* 
        
                When the build process ended, expressed in Unix time format.
        
              - **currentPhase** *(string) --* 
        
                The current build phase.
        
              - **buildStatus** *(string) --* 
        
                The current status of the build. Valid values include:
        
                * ``FAILED`` : The build failed. 
                 
                * ``FAULT`` : The build faulted. 
                 
                * ``IN_PROGRESS`` : The build is still in progress. 
                 
                * ``STOPPED`` : The build stopped. 
                 
                * ``SUCCEEDED`` : The build succeeded. 
                 
                * ``TIMED_OUT`` : The build timed out. 
                 
              - **sourceVersion** *(string) --* 
        
                Any version identifier for the version of the source code to be built.
        
              - **resolvedSourceVersion** *(string) --* 
        
                An identifier for the version of this build\'s source code. 
        
                * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.  
                 
                * For AWS CodePipeline, the source revision provided by AWS CodePipeline.  
                 
                * For Amazon Simple Storage Service (Amazon S3), this does not apply.  
                 
              - **projectName** *(string) --* 
        
                The name of the AWS CodeBuild project.
        
              - **phases** *(list) --* 
        
                Information about all previous build phases that are completed and information about any current build phase that is not yet complete.
        
                - *(dict) --* 
        
                  Information about a stage for a build.
        
                  - **phaseType** *(string) --* 
        
                    The name of the build phase. Valid values include:
        
                    * ``BUILD`` : Core build activities typically occur in this build phase. 
                     
                    * ``COMPLETED`` : The build has been completed. 
                     
                    * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase. 
                     
                    * ``FINALIZING`` : The build process is completing in this build phase. 
                     
                    * ``INSTALL`` : Installation activities typically occur in this build phase. 
                     
                    * ``POST_BUILD`` : Post-build activities typically occur in this build phase. 
                     
                    * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase. 
                     
                    * ``PROVISIONING`` : The build environment is being set up. 
                     
                    * ``SUBMITTED`` : The build has been submitted. 
                     
                    * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output location. 
                     
                  - **phaseStatus** *(string) --* 
        
                    The current status of the build phase. Valid values include:
        
                    * ``FAILED`` : The build phase failed. 
                     
                    * ``FAULT`` : The build phase faulted. 
                     
                    * ``IN_PROGRESS`` : The build phase is still in progress. 
                     
                    * ``STOPPED`` : The build phase stopped. 
                     
                    * ``SUCCEEDED`` : The build phase succeeded. 
                     
                    * ``TIMED_OUT`` : The build phase timed out. 
                     
                  - **startTime** *(datetime) --* 
        
                    When the build phase started, expressed in Unix time format.
        
                  - **endTime** *(datetime) --* 
        
                    When the build phase ended, expressed in Unix time format.
        
                  - **durationInSeconds** *(integer) --* 
        
                    How long, in seconds, between the starting and ending times of the build\'s phase.
        
                  - **contexts** *(list) --* 
        
                    Additional information about a build phase, especially to help troubleshoot a failed build.
        
                    - *(dict) --* 
        
                      Additional information about a build phase that has an error. You can use this information to help troubleshoot a failed build.
        
                      - **statusCode** *(string) --* 
        
                        The status code for the context of the build phase.
        
                      - **message** *(string) --* 
        
                        An explanation of the build phase\'s context. This explanation might include a command ID and an exit code.
        
              - **source** *(dict) --* 
        
                Information about the source code to be built.
        
                - **type** *(string) --* 
        
                  The type of repository that contains the source code to be built. Valid values include:
        
                  * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                   
                  * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                   
                  * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                   
                  * ``GITHUB`` : The source code is in a GitHub repository. 
                   
                  * ``NO_SOURCE`` : The project does not have input source code. 
                   
                  * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                   
                - **location** *(string) --* 
        
                  Information about the location of the source code to be built. Valid values include:
        
                  * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                   
                  * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                   
                  * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                    * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                     
                    * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                     
                  * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                   
                  * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                   
                - **gitCloneDepth** *(integer) --* 
        
                  Information about the git clone depth for the build project.
        
                - **buildspec** *(string) --* 
        
                  The build spec declaration to use for the builds in this build project.
        
                  If this value is not specified, a build spec must be included along with the source code to be built.
        
                - **auth** *(dict) --* 
        
                  Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                  This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                  - **type** *(string) --* 
        
                    The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                  - **resource** *(string) --* 
        
                    The resource value that applies to the specified authorization type.
        
                - **reportBuildStatus** *(boolean) --* 
        
                  Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                - **insecureSsl** *(boolean) --* 
        
                  Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                - **sourceIdentifier** *(string) --* 
        
                  An identifier for this project source. 
        
              - **secondarySources** *(list) --* 
        
                An array of ``ProjectSource`` objects. 
        
                - *(dict) --* 
        
                  Information about the build input source code for the build project.
        
                  - **type** *(string) --* 
        
                    The type of repository that contains the source code to be built. Valid values include:
        
                    * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                     
                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                     
                    * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                     
                    * ``GITHUB`` : The source code is in a GitHub repository. 
                     
                    * ``NO_SOURCE`` : The project does not have input source code. 
                     
                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                     
                  - **location** *(string) --* 
        
                    Information about the location of the source code to be built. Valid values include:
        
                    * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                     
                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                     
                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                      * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                       
                      * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                       
                    * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                    * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                  - **gitCloneDepth** *(integer) --* 
        
                    Information about the git clone depth for the build project.
        
                  - **buildspec** *(string) --* 
        
                    The build spec declaration to use for the builds in this build project.
        
                    If this value is not specified, a build spec must be included along with the source code to be built.
        
                  - **auth** *(dict) --* 
        
                    Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                    This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                    - **type** *(string) --* 
        
                      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                    - **resource** *(string) --* 
        
                      The resource value that applies to the specified authorization type.
        
                  - **reportBuildStatus** *(boolean) --* 
        
                    Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                  - **insecureSsl** *(boolean) --* 
        
                    Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                  - **sourceIdentifier** *(string) --* 
        
                    An identifier for this project source. 
        
              - **secondarySourceVersions** *(list) --* 
        
                An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one of: 
        
                * For AWS CodeCommit: the commit ID to use. 
                 
                * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                 
                * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                 
                * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
                 
                - *(dict) --* 
        
                  A source identifier and its corresponding version.
        
                  - **sourceIdentifier** *(string) --* 
        
                    An identifier for a source in the build project.
        
                  - **sourceVersion** *(string) --* 
        
                    The source version for the corresponding source identifier. If specified, must be one of:
        
                    * For AWS CodeCommit: the commit ID to use. 
                     
                    * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                     
                    * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                     
                    * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
                     
              - **artifacts** *(dict) --* 
        
                Information about the output artifacts for the build.
        
                - **location** *(string) --* 
        
                  Information about the location of the build artifacts.
        
                - **sha256sum** *(string) --* 
        
                  The SHA-256 hash of the build artifact.
        
                  You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                  .. note::
        
                    This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                - **md5sum** *(string) --* 
        
                  The MD5 hash of the build artifact.
        
                  You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                  .. note::
        
                    This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                - **overrideArtifactName** *(boolean) --* 
        
                  If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                - **encryptionDisabled** *(boolean) --* 
        
                  Information that tells you if encryption for build artifacts is disabled. 
        
                - **artifactIdentifier** *(string) --* 
        
                  An identifier for this artifact definition. 
        
              - **secondaryArtifacts** *(list) --* 
        
                An array of ``ProjectArtifacts`` objects. 
        
                - *(dict) --* 
        
                  Information about build output artifacts.
        
                  - **location** *(string) --* 
        
                    Information about the location of the build artifacts.
        
                  - **sha256sum** *(string) --* 
        
                    The SHA-256 hash of the build artifact.
        
                    You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                    .. note::
        
                      This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                  - **md5sum** *(string) --* 
        
                    The MD5 hash of the build artifact.
        
                    You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                    .. note::
        
                      This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                  - **overrideArtifactName** *(boolean) --* 
        
                    If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                  - **encryptionDisabled** *(boolean) --* 
        
                    Information that tells you if encryption for build artifacts is disabled. 
        
                  - **artifactIdentifier** *(string) --* 
        
                    An identifier for this artifact definition. 
        
              - **cache** *(dict) --* 
        
                Information about the cache for the build.
        
                - **type** *(string) --* 
        
                  The type of cache used by the build project. Valid values include:
        
                  * ``NO_CACHE`` : The build project will not use any cache. 
                   
                  * ``S3`` : The build project will read and write from/to S3. 
                   
                - **location** *(string) --* 
        
                  Information about the cache location, as follows: 
        
                  * ``NO_CACHE`` : This value will be ignored. 
                   
                  * ``S3`` : This is the S3 bucket name/prefix. 
                   
              - **environment** *(dict) --* 
        
                Information about the build environment for this build.
        
                - **type** *(string) --* 
        
                  The type of build environment to use for related builds.
        
                - **image** *(string) --* 
        
                  The ID of the Docker image to use for this build project.
        
                - **computeType** *(string) --* 
        
                  Information about the compute resources the build project will use. Available values include:
        
                  * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
                   
                  * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
                   
                  * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
                   
                - **environmentVariables** *(list) --* 
        
                  A set of environment variables to make available to builds for this build project.
        
                  - *(dict) --* 
        
                    Information about an environment variable for a build project or a build.
        
                    - **name** *(string) --* 
        
                      The name or key of the environment variable.
        
                    - **value** *(string) --* 
        
                      The value of the environment variable.
        
                      .. warning::
        
                        We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
                    - **type** *(string) --* 
        
                      The type of environment variable. Valid values include:
        
                      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                       
                      * ``PLAINTEXT`` : An environment variable in plaintext format. 
                       
                - **privilegedMode** *(boolean) --* 
        
                  Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
        
                  If the operating system\'s base image is Ubuntu Linux:
        
                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                  If the operating system\'s base image is Alpine Linux, add the ``-t`` argument to ``timeout`` :
        
                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                - **certificate** *(string) --* 
        
                  The certificate to use with this build project.
        
              - **serviceRole** *(string) --* 
        
                The name of a service role used for this build.
        
              - **logs** *(dict) --* 
        
                Information about the build\'s logs in Amazon CloudWatch Logs.
        
                - **groupName** *(string) --* 
        
                  The name of the Amazon CloudWatch Logs group for the build logs.
        
                - **streamName** *(string) --* 
        
                  The name of the Amazon CloudWatch Logs stream for the build logs.
        
                - **deepLink** *(string) --* 
        
                  The URL to an individual build log in Amazon CloudWatch Logs.
        
                - **s3DeepLink** *(string) --* 
        
                  The URL to an individual build log in an S3 bucket. 
        
                - **cloudWatchLogs** *(dict) --* 
        
                  Information about Amazon CloudWatch Logs for a build project. 
        
                  - **status** *(string) --* 
        
                    The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
                    * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
                     
                    * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
                     
                  - **groupName** *(string) --* 
        
                    The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                  - **streamName** *(string) --* 
        
                    The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                - **s3Logs** *(dict) --* 
        
                  Information about S3 logs for a build project. 
        
                  - **status** *(string) --* 
        
                    The current status of the S3 build logs. Valid values are:
        
                    * ``ENABLED`` : S3 build logs are enabled for this build project. 
                     
                    * ``DISABLED`` : S3 build logs are not enabled for this build project. 
                     
                  - **location** *(string) --* 
        
                    The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
              - **timeoutInMinutes** *(integer) --* 
        
                How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.
        
              - **buildComplete** *(boolean) --* 
        
                Whether the build has finished. True if completed; otherwise, false.
        
              - **initiator** *(string) --* 
        
                The entity that started the build. Valid values include:
        
                * If AWS CodePipeline started the build, the pipeline\'s name (for example, ``codepipeline/my-demo-pipeline`` ). 
                 
                * If an AWS Identity and Access Management (IAM) user started the build, the user\'s name (for example ``MyUserName`` ). 
                 
                * If the Jenkins plugin for AWS CodeBuild started the build, the string ``CodeBuild-Jenkins-Plugin`` . 
                 
              - **vpcConfig** *(dict) --* 
        
                If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.
        
                - **vpcId** *(string) --* 
        
                  The ID of the Amazon VPC.
        
                - **subnets** *(list) --* 
        
                  A list of one or more subnet IDs in your Amazon VPC.
        
                  - *(string) --* 
              
                - **securityGroupIds** *(list) --* 
        
                  A list of one or more security groups IDs in your Amazon VPC.
        
                  - *(string) --* 
              
              - **networkInterface** *(dict) --* 
        
                Describes a network interface.
        
                - **subnetId** *(string) --* 
        
                  The ID of the subnet.
        
                - **networkInterfaceId** *(string) --* 
        
                  The ID of the network interface.
        
              - **encryptionKey** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
        
                This is expressed either as the CMK\'s Amazon Resource Name (ARN) or, if specified, the CMK\'s alias (using the format ``alias/*alias-name* `` ).
        
        """
        pass

    def stop_build(self, id: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StopBuild>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_build(
              id=\'string\'
          )
        :type id: string
        :param id: **[REQUIRED]** 
        
          The ID of the build.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'build\': {
                    \'id\': \'string\',
                    \'arn\': \'string\',
                    \'startTime\': datetime(2015, 1, 1),
                    \'endTime\': datetime(2015, 1, 1),
                    \'currentPhase\': \'string\',
                    \'buildStatus\': \'SUCCEEDED\'|\'FAILED\'|\'FAULT\'|\'TIMED_OUT\'|\'IN_PROGRESS\'|\'STOPPED\',
                    \'sourceVersion\': \'string\',
                    \'resolvedSourceVersion\': \'string\',
                    \'projectName\': \'string\',
                    \'phases\': [
                        {
                            \'phaseType\': \'SUBMITTED\'|\'PROVISIONING\'|\'DOWNLOAD_SOURCE\'|\'INSTALL\'|\'PRE_BUILD\'|\'BUILD\'|\'POST_BUILD\'|\'UPLOAD_ARTIFACTS\'|\'FINALIZING\'|\'COMPLETED\',
                            \'phaseStatus\': \'SUCCEEDED\'|\'FAILED\'|\'FAULT\'|\'TIMED_OUT\'|\'IN_PROGRESS\'|\'STOPPED\',
                            \'startTime\': datetime(2015, 1, 1),
                            \'endTime\': datetime(2015, 1, 1),
                            \'durationInSeconds\': 123,
                            \'contexts\': [
                                {
                                    \'statusCode\': \'string\',
                                    \'message\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'source\': {
                        \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                        \'location\': \'string\',
                        \'gitCloneDepth\': 123,
                        \'buildspec\': \'string\',
                        \'auth\': {
                            \'type\': \'OAUTH\',
                            \'resource\': \'string\'
                        },
                        \'reportBuildStatus\': True|False,
                        \'insecureSsl\': True|False,
                        \'sourceIdentifier\': \'string\'
                    },
                    \'secondarySources\': [
                        {
                            \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                            \'location\': \'string\',
                            \'gitCloneDepth\': 123,
                            \'buildspec\': \'string\',
                            \'auth\': {
                                \'type\': \'OAUTH\',
                                \'resource\': \'string\'
                            },
                            \'reportBuildStatus\': True|False,
                            \'insecureSsl\': True|False,
                            \'sourceIdentifier\': \'string\'
                        },
                    ],
                    \'secondarySourceVersions\': [
                        {
                            \'sourceIdentifier\': \'string\',
                            \'sourceVersion\': \'string\'
                        },
                    ],
                    \'artifacts\': {
                        \'location\': \'string\',
                        \'sha256sum\': \'string\',
                        \'md5sum\': \'string\',
                        \'overrideArtifactName\': True|False,
                        \'encryptionDisabled\': True|False,
                        \'artifactIdentifier\': \'string\'
                    },
                    \'secondaryArtifacts\': [
                        {
                            \'location\': \'string\',
                            \'sha256sum\': \'string\',
                            \'md5sum\': \'string\',
                            \'overrideArtifactName\': True|False,
                            \'encryptionDisabled\': True|False,
                            \'artifactIdentifier\': \'string\'
                        },
                    ],
                    \'cache\': {
                        \'type\': \'NO_CACHE\'|\'S3\',
                        \'location\': \'string\'
                    },
                    \'environment\': {
                        \'type\': \'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
                        \'image\': \'string\',
                        \'computeType\': \'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
                        \'environmentVariables\': [
                            {
                                \'name\': \'string\',
                                \'value\': \'string\',
                                \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                            },
                        ],
                        \'privilegedMode\': True|False,
                        \'certificate\': \'string\'
                    },
                    \'serviceRole\': \'string\',
                    \'logs\': {
                        \'groupName\': \'string\',
                        \'streamName\': \'string\',
                        \'deepLink\': \'string\',
                        \'s3DeepLink\': \'string\',
                        \'cloudWatchLogs\': {
                            \'status\': \'ENABLED\'|\'DISABLED\',
                            \'groupName\': \'string\',
                            \'streamName\': \'string\'
                        },
                        \'s3Logs\': {
                            \'status\': \'ENABLED\'|\'DISABLED\',
                            \'location\': \'string\'
                        }
                    },
                    \'timeoutInMinutes\': 123,
                    \'buildComplete\': True|False,
                    \'initiator\': \'string\',
                    \'vpcConfig\': {
                        \'vpcId\': \'string\',
                        \'subnets\': [
                            \'string\',
                        ],
                        \'securityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'networkInterface\': {
                        \'subnetId\': \'string\',
                        \'networkInterfaceId\': \'string\'
                    },
                    \'encryptionKey\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **build** *(dict) --* 
        
              Information about the build.
        
              - **id** *(string) --* 
        
                The unique ID for the build.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the build.
        
              - **startTime** *(datetime) --* 
        
                When the build process started, expressed in Unix time format.
        
              - **endTime** *(datetime) --* 
        
                When the build process ended, expressed in Unix time format.
        
              - **currentPhase** *(string) --* 
        
                The current build phase.
        
              - **buildStatus** *(string) --* 
        
                The current status of the build. Valid values include:
        
                * ``FAILED`` : The build failed. 
                 
                * ``FAULT`` : The build faulted. 
                 
                * ``IN_PROGRESS`` : The build is still in progress. 
                 
                * ``STOPPED`` : The build stopped. 
                 
                * ``SUCCEEDED`` : The build succeeded. 
                 
                * ``TIMED_OUT`` : The build timed out. 
                 
              - **sourceVersion** *(string) --* 
        
                Any version identifier for the version of the source code to be built.
        
              - **resolvedSourceVersion** *(string) --* 
        
                An identifier for the version of this build\'s source code. 
        
                * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.  
                 
                * For AWS CodePipeline, the source revision provided by AWS CodePipeline.  
                 
                * For Amazon Simple Storage Service (Amazon S3), this does not apply.  
                 
              - **projectName** *(string) --* 
        
                The name of the AWS CodeBuild project.
        
              - **phases** *(list) --* 
        
                Information about all previous build phases that are completed and information about any current build phase that is not yet complete.
        
                - *(dict) --* 
        
                  Information about a stage for a build.
        
                  - **phaseType** *(string) --* 
        
                    The name of the build phase. Valid values include:
        
                    * ``BUILD`` : Core build activities typically occur in this build phase. 
                     
                    * ``COMPLETED`` : The build has been completed. 
                     
                    * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase. 
                     
                    * ``FINALIZING`` : The build process is completing in this build phase. 
                     
                    * ``INSTALL`` : Installation activities typically occur in this build phase. 
                     
                    * ``POST_BUILD`` : Post-build activities typically occur in this build phase. 
                     
                    * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase. 
                     
                    * ``PROVISIONING`` : The build environment is being set up. 
                     
                    * ``SUBMITTED`` : The build has been submitted. 
                     
                    * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output location. 
                     
                  - **phaseStatus** *(string) --* 
        
                    The current status of the build phase. Valid values include:
        
                    * ``FAILED`` : The build phase failed. 
                     
                    * ``FAULT`` : The build phase faulted. 
                     
                    * ``IN_PROGRESS`` : The build phase is still in progress. 
                     
                    * ``STOPPED`` : The build phase stopped. 
                     
                    * ``SUCCEEDED`` : The build phase succeeded. 
                     
                    * ``TIMED_OUT`` : The build phase timed out. 
                     
                  - **startTime** *(datetime) --* 
        
                    When the build phase started, expressed in Unix time format.
        
                  - **endTime** *(datetime) --* 
        
                    When the build phase ended, expressed in Unix time format.
        
                  - **durationInSeconds** *(integer) --* 
        
                    How long, in seconds, between the starting and ending times of the build\'s phase.
        
                  - **contexts** *(list) --* 
        
                    Additional information about a build phase, especially to help troubleshoot a failed build.
        
                    - *(dict) --* 
        
                      Additional information about a build phase that has an error. You can use this information to help troubleshoot a failed build.
        
                      - **statusCode** *(string) --* 
        
                        The status code for the context of the build phase.
        
                      - **message** *(string) --* 
        
                        An explanation of the build phase\'s context. This explanation might include a command ID and an exit code.
        
              - **source** *(dict) --* 
        
                Information about the source code to be built.
        
                - **type** *(string) --* 
        
                  The type of repository that contains the source code to be built. Valid values include:
        
                  * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                   
                  * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                   
                  * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                   
                  * ``GITHUB`` : The source code is in a GitHub repository. 
                   
                  * ``NO_SOURCE`` : The project does not have input source code. 
                   
                  * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                   
                - **location** *(string) --* 
        
                  Information about the location of the source code to be built. Valid values include:
        
                  * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                   
                  * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                   
                  * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                    * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                     
                    * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                     
                  * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                   
                  * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                   
                - **gitCloneDepth** *(integer) --* 
        
                  Information about the git clone depth for the build project.
        
                - **buildspec** *(string) --* 
        
                  The build spec declaration to use for the builds in this build project.
        
                  If this value is not specified, a build spec must be included along with the source code to be built.
        
                - **auth** *(dict) --* 
        
                  Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                  This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                  - **type** *(string) --* 
        
                    The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                  - **resource** *(string) --* 
        
                    The resource value that applies to the specified authorization type.
        
                - **reportBuildStatus** *(boolean) --* 
        
                  Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                - **insecureSsl** *(boolean) --* 
        
                  Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                - **sourceIdentifier** *(string) --* 
        
                  An identifier for this project source. 
        
              - **secondarySources** *(list) --* 
        
                An array of ``ProjectSource`` objects. 
        
                - *(dict) --* 
        
                  Information about the build input source code for the build project.
        
                  - **type** *(string) --* 
        
                    The type of repository that contains the source code to be built. Valid values include:
        
                    * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                     
                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                     
                    * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                     
                    * ``GITHUB`` : The source code is in a GitHub repository. 
                     
                    * ``NO_SOURCE`` : The project does not have input source code. 
                     
                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                     
                  - **location** *(string) --* 
        
                    Information about the location of the source code to be built. Valid values include:
        
                    * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                     
                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                     
                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                      * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                       
                      * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                       
                    * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                    * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                  - **gitCloneDepth** *(integer) --* 
        
                    Information about the git clone depth for the build project.
        
                  - **buildspec** *(string) --* 
        
                    The build spec declaration to use for the builds in this build project.
        
                    If this value is not specified, a build spec must be included along with the source code to be built.
        
                  - **auth** *(dict) --* 
        
                    Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                    This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                    - **type** *(string) --* 
        
                      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                    - **resource** *(string) --* 
        
                      The resource value that applies to the specified authorization type.
        
                  - **reportBuildStatus** *(boolean) --* 
        
                    Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                  - **insecureSsl** *(boolean) --* 
        
                    Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                  - **sourceIdentifier** *(string) --* 
        
                    An identifier for this project source. 
        
              - **secondarySourceVersions** *(list) --* 
        
                An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one of: 
        
                * For AWS CodeCommit: the commit ID to use. 
                 
                * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                 
                * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                 
                * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
                 
                - *(dict) --* 
        
                  A source identifier and its corresponding version.
        
                  - **sourceIdentifier** *(string) --* 
        
                    An identifier for a source in the build project.
        
                  - **sourceVersion** *(string) --* 
        
                    The source version for the corresponding source identifier. If specified, must be one of:
        
                    * For AWS CodeCommit: the commit ID to use. 
                     
                    * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                     
                    * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID will be used. If not specified, the default branch\'s HEAD commit ID will be used. 
                     
                    * For Amazon Simple Storage Service (Amazon S3): the version ID of the object representing the build input ZIP file to use. 
                     
              - **artifacts** *(dict) --* 
        
                Information about the output artifacts for the build.
        
                - **location** *(string) --* 
        
                  Information about the location of the build artifacts.
        
                - **sha256sum** *(string) --* 
        
                  The SHA-256 hash of the build artifact.
        
                  You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                  .. note::
        
                    This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                - **md5sum** *(string) --* 
        
                  The MD5 hash of the build artifact.
        
                  You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                  .. note::
        
                    This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                - **overrideArtifactName** *(boolean) --* 
        
                  If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                - **encryptionDisabled** *(boolean) --* 
        
                  Information that tells you if encryption for build artifacts is disabled. 
        
                - **artifactIdentifier** *(string) --* 
        
                  An identifier for this artifact definition. 
        
              - **secondaryArtifacts** *(list) --* 
        
                An array of ``ProjectArtifacts`` objects. 
        
                - *(dict) --* 
        
                  Information about build output artifacts.
        
                  - **location** *(string) --* 
        
                    Information about the location of the build artifacts.
        
                  - **sha256sum** *(string) --* 
        
                    The SHA-256 hash of the build artifact.
        
                    You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                    .. note::
        
                      This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                  - **md5sum** *(string) --* 
        
                    The MD5 hash of the build artifact.
        
                    You can use this hash along with a checksum tool to confirm both file integrity and authenticity.
        
                    .. note::
        
                      This value is available only if the build project\'s ``packaging`` value is set to ``ZIP`` .
        
                  - **overrideArtifactName** *(boolean) --* 
        
                    If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                  - **encryptionDisabled** *(boolean) --* 
        
                    Information that tells you if encryption for build artifacts is disabled. 
        
                  - **artifactIdentifier** *(string) --* 
        
                    An identifier for this artifact definition. 
        
              - **cache** *(dict) --* 
        
                Information about the cache for the build.
        
                - **type** *(string) --* 
        
                  The type of cache used by the build project. Valid values include:
        
                  * ``NO_CACHE`` : The build project will not use any cache. 
                   
                  * ``S3`` : The build project will read and write from/to S3. 
                   
                - **location** *(string) --* 
        
                  Information about the cache location, as follows: 
        
                  * ``NO_CACHE`` : This value will be ignored. 
                   
                  * ``S3`` : This is the S3 bucket name/prefix. 
                   
              - **environment** *(dict) --* 
        
                Information about the build environment for this build.
        
                - **type** *(string) --* 
        
                  The type of build environment to use for related builds.
        
                - **image** *(string) --* 
        
                  The ID of the Docker image to use for this build project.
        
                - **computeType** *(string) --* 
        
                  Information about the compute resources the build project will use. Available values include:
        
                  * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
                   
                  * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
                   
                  * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
                   
                - **environmentVariables** *(list) --* 
        
                  A set of environment variables to make available to builds for this build project.
        
                  - *(dict) --* 
        
                    Information about an environment variable for a build project or a build.
        
                    - **name** *(string) --* 
        
                      The name or key of the environment variable.
        
                    - **value** *(string) --* 
        
                      The value of the environment variable.
        
                      .. warning::
        
                        We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
                    - **type** *(string) --* 
        
                      The type of environment variable. Valid values include:
        
                      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                       
                      * ``PLAINTEXT`` : An environment variable in plaintext format. 
                       
                - **privilegedMode** *(boolean) --* 
        
                  Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
        
                  If the operating system\'s base image is Ubuntu Linux:
        
                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                  If the operating system\'s base image is Alpine Linux, add the ``-t`` argument to ``timeout`` :
        
                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                - **certificate** *(string) --* 
        
                  The certificate to use with this build project.
        
              - **serviceRole** *(string) --* 
        
                The name of a service role used for this build.
        
              - **logs** *(dict) --* 
        
                Information about the build\'s logs in Amazon CloudWatch Logs.
        
                - **groupName** *(string) --* 
        
                  The name of the Amazon CloudWatch Logs group for the build logs.
        
                - **streamName** *(string) --* 
        
                  The name of the Amazon CloudWatch Logs stream for the build logs.
        
                - **deepLink** *(string) --* 
        
                  The URL to an individual build log in Amazon CloudWatch Logs.
        
                - **s3DeepLink** *(string) --* 
        
                  The URL to an individual build log in an S3 bucket. 
        
                - **cloudWatchLogs** *(dict) --* 
        
                  Information about Amazon CloudWatch Logs for a build project. 
        
                  - **status** *(string) --* 
        
                    The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
                    * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
                     
                    * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
                     
                  - **groupName** *(string) --* 
        
                    The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                  - **streamName** *(string) --* 
        
                    The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                - **s3Logs** *(dict) --* 
        
                  Information about S3 logs for a build project. 
        
                  - **status** *(string) --* 
        
                    The current status of the S3 build logs. Valid values are:
        
                    * ``ENABLED`` : S3 build logs are enabled for this build project. 
                     
                    * ``DISABLED`` : S3 build logs are not enabled for this build project. 
                     
                  - **location** *(string) --* 
        
                    The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
              - **timeoutInMinutes** *(integer) --* 
        
                How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.
        
              - **buildComplete** *(boolean) --* 
        
                Whether the build has finished. True if completed; otherwise, false.
        
              - **initiator** *(string) --* 
        
                The entity that started the build. Valid values include:
        
                * If AWS CodePipeline started the build, the pipeline\'s name (for example, ``codepipeline/my-demo-pipeline`` ). 
                 
                * If an AWS Identity and Access Management (IAM) user started the build, the user\'s name (for example ``MyUserName`` ). 
                 
                * If the Jenkins plugin for AWS CodeBuild started the build, the string ``CodeBuild-Jenkins-Plugin`` . 
                 
              - **vpcConfig** *(dict) --* 
        
                If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.
        
                - **vpcId** *(string) --* 
        
                  The ID of the Amazon VPC.
        
                - **subnets** *(list) --* 
        
                  A list of one or more subnet IDs in your Amazon VPC.
        
                  - *(string) --* 
              
                - **securityGroupIds** *(list) --* 
        
                  A list of one or more security groups IDs in your Amazon VPC.
        
                  - *(string) --* 
              
              - **networkInterface** *(dict) --* 
        
                Describes a network interface.
        
                - **subnetId** *(string) --* 
        
                  The ID of the subnet.
        
                - **networkInterfaceId** *(string) --* 
        
                  The ID of the network interface.
        
              - **encryptionKey** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
        
                This is expressed either as the CMK\'s Amazon Resource Name (ARN) or, if specified, the CMK\'s alias (using the format ``alias/*alias-name* `` ).
        
        """
        pass

    def update_project(self, name: str, description: str = None, source: Dict = None, secondarySources: List = None, artifacts: Dict = None, secondaryArtifacts: List = None, cache: Dict = None, environment: Dict = None, serviceRole: str = None, timeoutInMinutes: int = None, encryptionKey: str = None, tags: List = None, vpcConfig: Dict = None, badgeEnabled: bool = None, logsConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_project(
              name=\'string\',
              description=\'string\',
              source={
                  \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                  \'location\': \'string\',
                  \'gitCloneDepth\': 123,
                  \'buildspec\': \'string\',
                  \'auth\': {
                      \'type\': \'OAUTH\',
                      \'resource\': \'string\'
                  },
                  \'reportBuildStatus\': True|False,
                  \'insecureSsl\': True|False,
                  \'sourceIdentifier\': \'string\'
              },
              secondarySources=[
                  {
                      \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                      \'location\': \'string\',
                      \'gitCloneDepth\': 123,
                      \'buildspec\': \'string\',
                      \'auth\': {
                          \'type\': \'OAUTH\',
                          \'resource\': \'string\'
                      },
                      \'reportBuildStatus\': True|False,
                      \'insecureSsl\': True|False,
                      \'sourceIdentifier\': \'string\'
                  },
              ],
              artifacts={
                  \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                  \'location\': \'string\',
                  \'path\': \'string\',
                  \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                  \'name\': \'string\',
                  \'packaging\': \'NONE\'|\'ZIP\',
                  \'overrideArtifactName\': True|False,
                  \'encryptionDisabled\': True|False,
                  \'artifactIdentifier\': \'string\'
              },
              secondaryArtifacts=[
                  {
                      \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                      \'location\': \'string\',
                      \'path\': \'string\',
                      \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                      \'name\': \'string\',
                      \'packaging\': \'NONE\'|\'ZIP\',
                      \'overrideArtifactName\': True|False,
                      \'encryptionDisabled\': True|False,
                      \'artifactIdentifier\': \'string\'
                  },
              ],
              cache={
                  \'type\': \'NO_CACHE\'|\'S3\',
                  \'location\': \'string\'
              },
              environment={
                  \'type\': \'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
                  \'image\': \'string\',
                  \'computeType\': \'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
                  \'environmentVariables\': [
                      {
                          \'name\': \'string\',
                          \'value\': \'string\',
                          \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                      },
                  ],
                  \'privilegedMode\': True|False,
                  \'certificate\': \'string\'
              },
              serviceRole=\'string\',
              timeoutInMinutes=123,
              encryptionKey=\'string\',
              tags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ],
              vpcConfig={
                  \'vpcId\': \'string\',
                  \'subnets\': [
                      \'string\',
                  ],
                  \'securityGroupIds\': [
                      \'string\',
                  ]
              },
              badgeEnabled=True|False,
              logsConfig={
                  \'cloudWatchLogs\': {
                      \'status\': \'ENABLED\'|\'DISABLED\',
                      \'groupName\': \'string\',
                      \'streamName\': \'string\'
                  },
                  \'s3Logs\': {
                      \'status\': \'ENABLED\'|\'DISABLED\',
                      \'location\': \'string\'
                  }
              }
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the build project.
        
          .. note::
        
            You cannot change a build project\'s name.
        
        :type description: string
        :param description: 
        
          A new or replacement description of the build project.
        
        :type source: dict
        :param source: 
        
          Information to be changed about the build input source code for the build project.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of repository that contains the source code to be built. Valid values include:
        
            * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
             
            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
             
            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
             
            * ``GITHUB`` : The source code is in a GitHub repository. 
             
            * ``NO_SOURCE`` : The project does not have input source code. 
             
            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
             
          - **location** *(string) --* 
        
            Information about the location of the source code to be built. Valid values include:
        
            * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
             
            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
             
            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
              * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
               
              * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
               
            * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
             
            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
             
          - **gitCloneDepth** *(integer) --* 
        
            Information about the git clone depth for the build project.
        
          - **buildspec** *(string) --* 
        
            The build spec declaration to use for the builds in this build project.
        
            If this value is not specified, a build spec must be included along with the source code to be built.
        
          - **auth** *(dict) --* 
        
            Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
            This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
            - **resource** *(string) --* 
        
              The resource value that applies to the specified authorization type.
        
          - **reportBuildStatus** *(boolean) --* 
        
            Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
          - **insecureSsl** *(boolean) --* 
        
            Enable this flag to ignore SSL warnings while connecting to the project source code.
        
          - **sourceIdentifier** *(string) --* 
        
            An identifier for this project source. 
        
        :type secondarySources: list
        :param secondarySources: 
        
          An array of ``ProjectSource`` objects. 
        
          - *(dict) --* 
        
            Information about the build input source code for the build project.
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The type of repository that contains the source code to be built. Valid values include:
        
              * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
               
              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
               
              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
               
              * ``GITHUB`` : The source code is in a GitHub repository. 
               
              * ``NO_SOURCE`` : The project does not have input source code. 
               
              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
               
            - **location** *(string) --* 
        
              Information about the location of the source code to be built. Valid values include:
        
              * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
               
              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
               
              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                 
                * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                 
              * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
               
              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
               
            - **gitCloneDepth** *(integer) --* 
        
              Information about the git clone depth for the build project.
        
            - **buildspec** *(string) --* 
        
              The build spec declaration to use for the builds in this build project.
        
              If this value is not specified, a build spec must be included along with the source code to be built.
        
            - **auth** *(dict) --* 
        
              Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
              This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
              - **type** *(string) --* **[REQUIRED]** 
        
                The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
              - **resource** *(string) --* 
        
                The resource value that applies to the specified authorization type.
        
            - **reportBuildStatus** *(boolean) --* 
        
              Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
            - **insecureSsl** *(boolean) --* 
        
              Enable this flag to ignore SSL warnings while connecting to the project source code.
        
            - **sourceIdentifier** *(string) --* 
        
              An identifier for this project source. 
        
        :type artifacts: dict
        :param artifacts: 
        
          Information to be changed about the build output artifacts for the build project.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of build output artifact. Valid values include:
        
            * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
             
            * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
             
            * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
             
          - **location** *(string) --* 
        
            Information about the build output artifact location, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
             
          - **path** *(string) --* 
        
            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
             
            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
          - **namespaceType** *(string) --* 
        
            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , then valid values include: 
        
              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
               
              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
               
            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
          - **name** *(string) --* 
        
            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
             
            For example:
        
            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
             
            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
             
            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
             
          - **packaging** *(string) --* 
        
            The type of build output artifact to create, as follows:
        
            * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
             
            * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
             
            * If ``type`` is set to ``S3`` , valid values include: 
        
              * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
               
              * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
               
          - **overrideArtifactName** *(boolean) --* 
        
            If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
          - **encryptionDisabled** *(boolean) --* 
        
            Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
          - **artifactIdentifier** *(string) --* 
        
            An identifier for this artifact definition. 
        
        :type secondaryArtifacts: list
        :param secondaryArtifacts: 
        
          An array of ``ProjectSource`` objects. 
        
          - *(dict) --* 
        
            Information about the build output artifacts for the build project.
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The type of build output artifact. Valid values include:
        
              * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
               
              * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
               
              * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
               
            - **location** *(string) --* 
        
              Information about the build output artifact location, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
               
            - **path** *(string) --* 
        
              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
               
              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
            - **namespaceType** *(string) --* 
        
              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , then valid values include: 
        
                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                 
                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                 
              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
            - **name** *(string) --* 
        
              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
               
              For example:
        
              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
               
              * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
               
              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
               
            - **packaging** *(string) --* 
        
              The type of build output artifact to create, as follows:
        
              * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
               
              * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
               
              * If ``type`` is set to ``S3`` , valid values include: 
        
                * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                 
                * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                 
            - **overrideArtifactName** *(boolean) --* 
        
              If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
            - **encryptionDisabled** *(boolean) --* 
        
              Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
            - **artifactIdentifier** *(string) --* 
        
              An identifier for this artifact definition. 
        
        :type cache: dict
        :param cache: 
        
          Stores recently used information so that it can be quickly accessed at a later time.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of cache used by the build project. Valid values include:
        
            * ``NO_CACHE`` : The build project will not use any cache. 
             
            * ``S3`` : The build project will read and write from/to S3. 
             
          - **location** *(string) --* 
        
            Information about the cache location, as follows: 
        
            * ``NO_CACHE`` : This value will be ignored. 
             
            * ``S3`` : This is the S3 bucket name/prefix. 
             
        :type environment: dict
        :param environment: 
        
          Information to be changed about the build environment for the build project.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of build environment to use for related builds.
        
          - **image** *(string) --* **[REQUIRED]** 
        
            The ID of the Docker image to use for this build project.
        
          - **computeType** *(string) --* **[REQUIRED]** 
        
            Information about the compute resources the build project will use. Available values include:
        
            * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
             
            * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
             
            * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
             
          - **environmentVariables** *(list) --* 
        
            A set of environment variables to make available to builds for this build project.
        
            - *(dict) --* 
        
              Information about an environment variable for a build project or a build.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name or key of the environment variable.
        
              - **value** *(string) --* **[REQUIRED]** 
        
                The value of the environment variable.
        
                .. warning::
        
                  We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
              - **type** *(string) --* 
        
                The type of environment variable. Valid values include:
        
                * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                 
                * ``PLAINTEXT`` : An environment variable in plaintext format. 
                 
          - **privilegedMode** *(boolean) --* 
        
            Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
        
            If the operating system\'s base image is Ubuntu Linux:
        
             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
            If the operating system\'s base image is Alpine Linux, add the ``-t`` argument to ``timeout`` :
        
             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
          - **certificate** *(string) --* 
        
            The certificate to use with this build project.
        
        :type serviceRole: string
        :param serviceRole: 
        
          The replacement ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
        
        :type timeoutInMinutes: integer
        :param timeoutInMinutes: 
        
          The replacement value in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed.
        
        :type encryptionKey: string
        :param encryptionKey: 
        
          The replacement AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
        
          You can specify either the CMK\'s Amazon Resource Name (ARN) or, if available, the CMK\'s alias (using the format ``alias/*alias-name* `` ).
        
        :type tags: list
        :param tags: 
        
          The replacement set of tags for this build project.
        
          These tags are available for use by AWS services that support AWS CodeBuild build project tags.
        
          - *(dict) --* 
        
            A tag, consisting of a key and a value.
        
            This tag is available for use by AWS services that support tags in AWS CodeBuild.
        
            - **key** *(string) --* 
        
              The tag\'s key.
        
            - **value** *(string) --* 
        
              The tag\'s value.
        
        :type vpcConfig: dict
        :param vpcConfig: 
        
          VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
        
          - **vpcId** *(string) --* 
        
            The ID of the Amazon VPC.
        
          - **subnets** *(list) --* 
        
            A list of one or more subnet IDs in your Amazon VPC.
        
            - *(string) --* 
        
          - **securityGroupIds** *(list) --* 
        
            A list of one or more security groups IDs in your Amazon VPC.
        
            - *(string) --* 
        
        :type badgeEnabled: boolean
        :param badgeEnabled: 
        
          Set this to true to generate a publicly-accessible URL for your project\'s build badge.
        
        :type logsConfig: dict
        :param logsConfig: 
        
          Information about logs for the build project. A project can create Amazon CloudWatch Logs, logs in an S3 bucket, or both. 
        
          - **cloudWatchLogs** *(dict) --* 
        
            Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default. 
        
            - **status** *(string) --* **[REQUIRED]** 
        
              The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
              * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
               
              * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
               
            - **groupName** *(string) --* 
        
              The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
            - **streamName** *(string) --* 
        
              The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
          - **s3Logs** *(dict) --* 
        
            Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default. 
        
            - **status** *(string) --* **[REQUIRED]** 
        
              The current status of the S3 build logs. Valid values are:
        
              * ``ENABLED`` : S3 build logs are enabled for this build project. 
               
              * ``DISABLED`` : S3 build logs are not enabled for this build project. 
               
            - **location** *(string) --* 
        
              The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'project\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'description\': \'string\',
                    \'source\': {
                        \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                        \'location\': \'string\',
                        \'gitCloneDepth\': 123,
                        \'buildspec\': \'string\',
                        \'auth\': {
                            \'type\': \'OAUTH\',
                            \'resource\': \'string\'
                        },
                        \'reportBuildStatus\': True|False,
                        \'insecureSsl\': True|False,
                        \'sourceIdentifier\': \'string\'
                    },
                    \'secondarySources\': [
                        {
                            \'type\': \'CODECOMMIT\'|\'CODEPIPELINE\'|\'GITHUB\'|\'S3\'|\'BITBUCKET\'|\'GITHUB_ENTERPRISE\'|\'NO_SOURCE\',
                            \'location\': \'string\',
                            \'gitCloneDepth\': 123,
                            \'buildspec\': \'string\',
                            \'auth\': {
                                \'type\': \'OAUTH\',
                                \'resource\': \'string\'
                            },
                            \'reportBuildStatus\': True|False,
                            \'insecureSsl\': True|False,
                            \'sourceIdentifier\': \'string\'
                        },
                    ],
                    \'artifacts\': {
                        \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                        \'location\': \'string\',
                        \'path\': \'string\',
                        \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                        \'name\': \'string\',
                        \'packaging\': \'NONE\'|\'ZIP\',
                        \'overrideArtifactName\': True|False,
                        \'encryptionDisabled\': True|False,
                        \'artifactIdentifier\': \'string\'
                    },
                    \'secondaryArtifacts\': [
                        {
                            \'type\': \'CODEPIPELINE\'|\'S3\'|\'NO_ARTIFACTS\',
                            \'location\': \'string\',
                            \'path\': \'string\',
                            \'namespaceType\': \'NONE\'|\'BUILD_ID\',
                            \'name\': \'string\',
                            \'packaging\': \'NONE\'|\'ZIP\',
                            \'overrideArtifactName\': True|False,
                            \'encryptionDisabled\': True|False,
                            \'artifactIdentifier\': \'string\'
                        },
                    ],
                    \'cache\': {
                        \'type\': \'NO_CACHE\'|\'S3\',
                        \'location\': \'string\'
                    },
                    \'environment\': {
                        \'type\': \'WINDOWS_CONTAINER\'|\'LINUX_CONTAINER\',
                        \'image\': \'string\',
                        \'computeType\': \'BUILD_GENERAL1_SMALL\'|\'BUILD_GENERAL1_MEDIUM\'|\'BUILD_GENERAL1_LARGE\',
                        \'environmentVariables\': [
                            {
                                \'name\': \'string\',
                                \'value\': \'string\',
                                \'type\': \'PLAINTEXT\'|\'PARAMETER_STORE\'
                            },
                        ],
                        \'privilegedMode\': True|False,
                        \'certificate\': \'string\'
                    },
                    \'serviceRole\': \'string\',
                    \'timeoutInMinutes\': 123,
                    \'encryptionKey\': \'string\',
                    \'tags\': [
                        {
                            \'key\': \'string\',
                            \'value\': \'string\'
                        },
                    ],
                    \'created\': datetime(2015, 1, 1),
                    \'lastModified\': datetime(2015, 1, 1),
                    \'webhook\': {
                        \'url\': \'string\',
                        \'payloadUrl\': \'string\',
                        \'secret\': \'string\',
                        \'branchFilter\': \'string\',
                        \'lastModifiedSecret\': datetime(2015, 1, 1)
                    },
                    \'vpcConfig\': {
                        \'vpcId\': \'string\',
                        \'subnets\': [
                            \'string\',
                        ],
                        \'securityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'badge\': {
                        \'badgeEnabled\': True|False,
                        \'badgeRequestUrl\': \'string\'
                    },
                    \'logsConfig\': {
                        \'cloudWatchLogs\': {
                            \'status\': \'ENABLED\'|\'DISABLED\',
                            \'groupName\': \'string\',
                            \'streamName\': \'string\'
                        },
                        \'s3Logs\': {
                            \'status\': \'ENABLED\'|\'DISABLED\',
                            \'location\': \'string\'
                        }
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **project** *(dict) --* 
        
              Information about the build project that was changed.
        
              - **name** *(string) --* 
        
                The name of the build project.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the build project.
        
              - **description** *(string) --* 
        
                A description that makes the build project easy to identify.
        
              - **source** *(dict) --* 
        
                Information about the build input source code for this build project.
        
                - **type** *(string) --* 
        
                  The type of repository that contains the source code to be built. Valid values include:
        
                  * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                   
                  * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                   
                  * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                   
                  * ``GITHUB`` : The source code is in a GitHub repository. 
                   
                  * ``NO_SOURCE`` : The project does not have input source code. 
                   
                  * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                   
                - **location** *(string) --* 
        
                  Information about the location of the source code to be built. Valid values include:
        
                  * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                   
                  * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                   
                  * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                    * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                     
                    * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                     
                  * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                   
                  * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                   
                - **gitCloneDepth** *(integer) --* 
        
                  Information about the git clone depth for the build project.
        
                - **buildspec** *(string) --* 
        
                  The build spec declaration to use for the builds in this build project.
        
                  If this value is not specified, a build spec must be included along with the source code to be built.
        
                - **auth** *(dict) --* 
        
                  Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                  This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                  - **type** *(string) --* 
        
                    The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                  - **resource** *(string) --* 
        
                    The resource value that applies to the specified authorization type.
        
                - **reportBuildStatus** *(boolean) --* 
        
                  Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                - **insecureSsl** *(boolean) --* 
        
                  Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                - **sourceIdentifier** *(string) --* 
        
                  An identifier for this project source. 
        
              - **secondarySources** *(list) --* 
        
                An array of ``ProjectSource`` objects. 
        
                - *(dict) --* 
        
                  Information about the build input source code for the build project.
        
                  - **type** *(string) --* 
        
                    The type of repository that contains the source code to be built. Valid values include:
        
                    * ``BITBUCKET`` : The source code is in a Bitbucket repository. 
                     
                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository. 
                     
                    * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline in AWS CodePipeline. 
                     
                    * ``GITHUB`` : The source code is in a GitHub repository. 
                     
                    * ``NO_SOURCE`` : The project does not have input source code. 
                     
                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket. 
                     
                  - **location** *(string) --* 
        
                    Information about the location of the source code to be built. Valid values include:
        
                    * For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline will ignore it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value. 
                     
                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ). 
                     
                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.  
        
                      * The path to the ZIP file that contains the source code (for example, `` *bucket-name* /*path* /*to* /*object-name* .zip`` ).  
                       
                      * The path to the folder that contains the source code (for example, `` *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).  
                       
                    * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your GitHub account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page that displays, for **Organization access** , choose **Request access** next to each repository you want to allow AWS CodeBuild to have access to. Then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                    * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. Also, you must connect your AWS account to your Bitbucket account. To do this, use the AWS CodeBuild console to begin creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page that displays, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project, and you may then leave the AWS CodeBuild console.) To instruct AWS CodeBuild to then use this connection, in the ``source`` object, set the ``auth`` object\'s ``type`` value to ``OAUTH`` . 
                     
                  - **gitCloneDepth** *(integer) --* 
        
                    Information about the git clone depth for the build project.
        
                  - **buildspec** *(string) --* 
        
                    The build spec declaration to use for the builds in this build project.
        
                    If this value is not specified, a build spec must be included along with the source code to be built.
        
                  - **auth** *(dict) --* 
        
                    Information about the authorization settings for AWS CodeBuild to access the source code to be built.
        
                    This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly (unless the build project\'s source ``type`` value is ``BITBUCKET`` or ``GITHUB`` ).
        
                    - **type** *(string) --* 
        
                      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth authorization type.
        
                    - **resource** *(string) --* 
        
                      The resource value that applies to the specified authorization type.
        
                  - **reportBuildStatus** *(boolean) --* 
        
                    Set to true to report the status of a build\'s start and finish to your source provider. This option is only valid when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown. 
        
                  - **insecureSsl** *(boolean) --* 
        
                    Enable this flag to ignore SSL warnings while connecting to the project source code.
        
                  - **sourceIdentifier** *(string) --* 
        
                    An identifier for this project source. 
        
              - **artifacts** *(dict) --* 
        
                Information about the build output artifacts for the build project.
        
                - **type** *(string) --* 
        
                  The type of build output artifact. Valid values include:
        
                  * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
                   
                  * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
                   
                  * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
                   
                - **location** *(string) --* 
        
                  Information about the build output artifact location, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
                   
                - **path** *(string) --* 
        
                  Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
                   
                  For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
                - **namespaceType** *(string) --* 
        
                  Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , then valid values include: 
        
                    * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                     
                    * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                     
                  For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
                - **name** *(string) --* 
        
                  Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
                   
                  For example:
        
                  * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
                   
                  * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
                   
                  * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
                   
                - **packaging** *(string) --* 
        
                  The type of build output artifact to create, as follows:
        
                  * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
                   
                  * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                   
                  * If ``type`` is set to ``S3`` , valid values include: 
        
                    * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                     
                    * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                     
                - **overrideArtifactName** *(boolean) --* 
        
                  If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                - **encryptionDisabled** *(boolean) --* 
        
                  Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
                - **artifactIdentifier** *(string) --* 
        
                  An identifier for this artifact definition. 
        
              - **secondaryArtifacts** *(list) --* 
        
                An array of ``ProjectArtifacts`` objects. 
        
                - *(dict) --* 
        
                  Information about the build output artifacts for the build project.
        
                  - **type** *(string) --* 
        
                    The type of build output artifact. Valid values include:
        
                    * ``CODEPIPELINE`` : The build project will have build output generated through AWS CodePipeline. 
                     
                    * ``NO_ARTIFACTS`` : The build project will not produce any build output. 
                     
                    * ``S3`` : The build project will store build output in Amazon Simple Storage Service (Amazon S3). 
                     
                  - **location** *(string) --* 
        
                    Information about the build output artifact location, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the name of the output bucket. 
                     
                  - **path** *(string) --* 
        
                    Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not specified, then ``path`` will not be used. 
                     
                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .
        
                  - **namespaceType** *(string) --* 
        
                    Along with ``path`` and ``name`` , the pattern that AWS CodeBuild will use to determine the name and location to store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , then valid values include: 
        
                      * ``BUILD_ID`` : Include the build ID in the location of the build output artifact. 
                       
                      * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not specified. 
                       
                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .
        
                  - **name** *(string) --* 
        
                    Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild will use to name and store the output artifact, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the name to be a forward slash (\"/\"), then the artifact is stored in the root of the output bucket. 
                     
                    For example:
        
                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact would be stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .  
                     
                    * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in the root of the output bucket.  
                     
                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and ``name`` is set to \"``/`` \", then the output artifact would be stored in ``MyArtifacts/*build-ID* `` .  
                     
                  - **packaging** *(string) --* 
        
                    The type of build output artifact to create, as follows:
        
                    * If ``type`` is set to ``CODEPIPELINE`` , then AWS CodePipeline will ignore this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild. 
                     
                    * If ``type`` is set to ``NO_ARTIFACTS`` , then this value will be ignored if specified, because no build output will be produced. 
                     
                    * If ``type`` is set to ``S3`` , valid values include: 
        
                      * ``NONE`` : AWS CodeBuild will create in the output bucket a folder containing the build output. This is the default if ``packaging`` is not specified. 
                       
                      * ``ZIP`` : AWS CodeBuild will create in the output bucket a ZIP file containing the build output. 
                       
                  - **overrideArtifactName** *(boolean) --* 
        
                    If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. 
        
                  - **encryptionDisabled** *(boolean) --* 
        
                    Set to true if you do not want your output artifacts encrypted. This option is only valid if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException will be thrown. 
        
                  - **artifactIdentifier** *(string) --* 
        
                    An identifier for this artifact definition. 
        
              - **cache** *(dict) --* 
        
                Information about the cache for the build project.
        
                - **type** *(string) --* 
        
                  The type of cache used by the build project. Valid values include:
        
                  * ``NO_CACHE`` : The build project will not use any cache. 
                   
                  * ``S3`` : The build project will read and write from/to S3. 
                   
                - **location** *(string) --* 
        
                  Information about the cache location, as follows: 
        
                  * ``NO_CACHE`` : This value will be ignored. 
                   
                  * ``S3`` : This is the S3 bucket name/prefix. 
                   
              - **environment** *(dict) --* 
        
                Information about the build environment for this build project.
        
                - **type** *(string) --* 
        
                  The type of build environment to use for related builds.
        
                - **image** *(string) --* 
        
                  The ID of the Docker image to use for this build project.
        
                - **computeType** *(string) --* 
        
                  Information about the compute resources the build project will use. Available values include:
        
                  * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds. 
                   
                  * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds. 
                   
                  * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds. 
                   
                - **environmentVariables** *(list) --* 
        
                  A set of environment variables to make available to builds for this build project.
        
                  - *(dict) --* 
        
                    Information about an environment variable for a build project or a build.
        
                    - **name** *(string) --* 
        
                      The name or key of the environment variable.
        
                    - **value** *(string) --* 
        
                      The value of the environment variable.
        
                      .. warning::
        
                        We strongly discourage using environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using tools such as the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
        
                    - **type** *(string) --* 
        
                      The type of environment variable. Valid values include:
        
                      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. 
                       
                      * ``PLAINTEXT`` : An environment variable in plaintext format. 
                       
                - **privilegedMode** *(boolean) --* 
        
                  Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon will fail. Note that you must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run the following build commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
        
                  If the operating system\'s base image is Ubuntu Linux:
        
                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                  If the operating system\'s base image is Alpine Linux, add the ``-t`` argument to ``timeout`` :
        
                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c \"until docker info; do echo .; sleep 1; done\"``  
        
                - **certificate** *(string) --* 
        
                  The certificate to use with this build project.
        
              - **serviceRole** *(string) --* 
        
                The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
        
              - **timeoutInMinutes** *(integer) --* 
        
                How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.
        
              - **encryptionKey** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
        
                This is expressed either as the CMK\'s Amazon Resource Name (ARN) or, if specified, the CMK\'s alias (using the format ``alias/*alias-name* `` ).
        
              - **tags** *(list) --* 
        
                The tags for this build project.
        
                These tags are available for use by AWS services that support AWS CodeBuild build project tags.
        
                - *(dict) --* 
        
                  A tag, consisting of a key and a value.
        
                  This tag is available for use by AWS services that support tags in AWS CodeBuild.
        
                  - **key** *(string) --* 
        
                    The tag\'s key.
        
                  - **value** *(string) --* 
        
                    The tag\'s value.
        
              - **created** *(datetime) --* 
        
                When the build project was created, expressed in Unix time format.
        
              - **lastModified** *(datetime) --* 
        
                When the build project\'s settings were last modified, expressed in Unix time format.
        
              - **webhook** *(dict) --* 
        
                Information about a webhook that connects repository events to a build project in AWS CodeBuild.
        
                - **url** *(string) --* 
        
                  The URL to the webhook.
        
                - **payloadUrl** *(string) --* 
        
                  The CodeBuild endpoint where webhook events are sent.
        
                - **secret** *(string) --* 
        
                  The secret token of the associated repository. 
        
                  .. note::
        
                    A Bitbucket webhook does not support ``secret`` . 
        
                - **branchFilter** *(string) --* 
        
                  A regular expression used to determine which branches in a repository are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If it doesn\'t match, then it is not. If ``branchFilter`` is empty, then all branches are built.
        
                - **lastModifiedSecret** *(datetime) --* 
        
                  A timestamp indicating the last time a repository\'s secret token was modified. 
        
              - **vpcConfig** *(dict) --* 
        
                Information about the VPC configuration that AWS CodeBuild will access.
        
                - **vpcId** *(string) --* 
        
                  The ID of the Amazon VPC.
        
                - **subnets** *(list) --* 
        
                  A list of one or more subnet IDs in your Amazon VPC.
        
                  - *(string) --* 
              
                - **securityGroupIds** *(list) --* 
        
                  A list of one or more security groups IDs in your Amazon VPC.
        
                  - *(string) --* 
              
              - **badge** *(dict) --* 
        
                Information about the build badge for the build project.
        
                - **badgeEnabled** *(boolean) --* 
        
                  Set this to true to generate a publicly-accessible URL for your project\'s build badge.
        
                - **badgeRequestUrl** *(string) --* 
        
                  The publicly-accessible URL through which you can access the build badge for your project. 
        
              - **logsConfig** *(dict) --* 
        
                Information about logs for the build project. A project can create Amazon CloudWatch Logs, logs in an S3 bucket, or both. 
        
                - **cloudWatchLogs** *(dict) --* 
        
                  Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default. 
        
                  - **status** *(string) --* 
        
                    The current status of the Amazon CloudWatch Logs for a build project. Valid values are:
        
                    * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project. 
                     
                    * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project. 
                     
                  - **groupName** *(string) --* 
        
                    The group name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                  - **streamName** *(string) --* 
        
                    The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see `Working with Log Groups and Log Streams <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__  
        
                - **s3Logs** *(dict) --* 
        
                  Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default. 
        
                  - **status** *(string) --* 
        
                    The current status of the S3 build logs. Valid values are:
        
                    * ``ENABLED`` : S3 build logs are enabled for this build project. 
                     
                    * ``DISABLED`` : S3 build logs are not enabled for this build project. 
                     
                  - **location** *(string) --* 
        
                    The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` . 
        
        """
        pass

    def update_webhook(self, projectName: str, branchFilter: str = None, rotateSecret: bool = None) -> Dict:
        """
        
        .. note::
        
          If you use Bitbucket for your repository then ``rotateSecret`` is ignored. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateWebhook>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_webhook(
              projectName=\'string\',
              branchFilter=\'string\',
              rotateSecret=True|False
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the AWS CodeBuild project.
        
        :type branchFilter: string
        :param branchFilter: 
        
          A regular expression used to determine which branches in a repository are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If it doesn\'t match, then it is not. If ``branchFilter`` is empty, then all branches are built.
        
        :type rotateSecret: boolean
        :param rotateSecret: 
        
          A boolean value that specifies whether the associated GitHub repository\'s secret token should be updated. If you use Bitbucket for your repository then ``rotateSecret`` is ignored. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'webhook\': {
                    \'url\': \'string\',
                    \'payloadUrl\': \'string\',
                    \'secret\': \'string\',
                    \'branchFilter\': \'string\',
                    \'lastModifiedSecret\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **webhook** *(dict) --* 
        
              Information about a repository\'s webhook that is associated with a project in AWS CodeBuild. 
        
              - **url** *(string) --* 
        
                The URL to the webhook.
        
              - **payloadUrl** *(string) --* 
        
                The CodeBuild endpoint where webhook events are sent.
        
              - **secret** *(string) --* 
        
                The secret token of the associated repository. 
        
                .. note::
        
                  A Bitbucket webhook does not support ``secret`` . 
        
              - **branchFilter** *(string) --* 
        
                A regular expression used to determine which branches in a repository are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If it doesn\'t match, then it is not. If ``branchFilter`` is empty, then all branches are built.
        
              - **lastModifiedSecret** *(datetime) --* 
        
                A timestamp indicating the last time a repository\'s secret token was modified. 
        
        """
        pass
