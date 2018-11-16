from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_created_artifact(self, ProgressUpdateStream: str, MigrationTaskName: str, CreatedArtifact: Dict, DryRun: bool = None) -> Dict:
        """
        Associates a created artifact of an AWS cloud resource, the target receiving the migration, with the migration task performed by a migration tool. This API has the following traits:
        
        * Migration tools can call the ``AssociateCreatedArtifact`` operation to indicate which AWS artifact is associated with a migration task. 
         
        * The created artifact name must be provided in ARN (Amazon Resource Name) format which will contain information about type and region; for example: ``arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b`` . 
         
        * Examples of the AWS resource behind the created artifact are, AMI\'s, EC2 instance, or DMS endpoint, etc. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/AssociateCreatedArtifact>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_created_artifact(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              CreatedArtifact={
                  \'Name\': \'string\',
                  \'Description\': \'string\'
              },
              DryRun=True|False
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          Unique identifier that references the migration task.
        
        :type CreatedArtifact: dict
        :param CreatedArtifact: **[REQUIRED]** 
        
          An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.) 
        
          - **Name** *(string) --* **[REQUIRED]** 
        
            An ARN that uniquely identifies the result of a migration task.
        
          - **Description** *(string) --* 
        
            A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def associate_discovered_resource(self, ProgressUpdateStream: str, MigrationTaskName: str, DiscoveredResource: Dict, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/AssociateDiscoveredResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_discovered_resource(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              DiscoveredResource={
                  \'ConfigurationId\': \'string\',
                  \'Description\': \'string\'
              },
              DryRun=True|False
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream.
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          The identifier given to the MigrationTask.
        
        :type DiscoveredResource: dict
        :param DiscoveredResource: **[REQUIRED]** 
        
          Object representing a Resource.
        
          - **ConfigurationId** *(string) --* **[REQUIRED]** 
        
            The configurationId in ADS that uniquely identifies the on-premise resource.
        
          - **Description** *(string) --* 
        
            A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
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

    def create_progress_update_stream(self, ProgressUpdateStreamName: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_progress_update_stream(
              ProgressUpdateStreamName=\'string\',
              DryRun=True|False
          )
        :type ProgressUpdateStreamName: string
        :param ProgressUpdateStreamName: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_progress_update_stream(self, ProgressUpdateStreamName: str, DryRun: bool = None) -> Dict:
        """
        Deletes a progress update stream, including all of its tasks, which was previously created as an AWS resource used for access control. This API has the following traits:
        
        * The only parameter needed for ``DeleteProgressUpdateStream`` is the stream name (same as a ``CreateProgressUpdateStream`` call). 
         
        * The call will return, and a background process will asynchronously delete the stream and all of its resources (tasks, associated resources, resource attributes, created artifacts). 
         
        * If the stream takes time to be deleted, it might still show up on a ``ListProgressUpdateStreams`` call. 
         
        * ``CreateProgressUpdateStream`` , ``ImportMigrationTask`` , ``NotifyMigrationTaskState`` , and all Associate[*] APIs realted to the tasks belonging to the stream will throw \"InvalidInputException\" if the stream of the same name is in the process of being deleted. 
         
        * Once the stream and all of its resources are deleted, ``CreateProgressUpdateStream`` for a stream of the same name will succeed, and that stream will be an entirely new logical resource (without any resources associated with the old stream). 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DeleteProgressUpdateStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_progress_update_stream(
              ProgressUpdateStreamName=\'string\',
              DryRun=True|False
          )
        :type ProgressUpdateStreamName: string
        :param ProgressUpdateStreamName: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_application_state(self, ApplicationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DescribeApplicationState>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_application_state(
              ApplicationId=\'string\'
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The configurationId in ADS that uniquely identifies the grouped application.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ApplicationStatus\': \'NOT_STARTED\'|\'IN_PROGRESS\'|\'COMPLETED\',
                \'LastUpdatedTime\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ApplicationStatus** *(string) --* 
        
              Status of the application - Not Started, In-Progress, Complete.
        
            - **LastUpdatedTime** *(datetime) --* 
        
              The timestamp when the application status was last updated.
        
        """
        pass

    def describe_migration_task(self, ProgressUpdateStream: str, MigrationTaskName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DescribeMigrationTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_migration_task(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\'
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          The identifier given to the MigrationTask.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'MigrationTask\': {
                    \'ProgressUpdateStream\': \'string\',
                    \'MigrationTaskName\': \'string\',
                    \'Task\': {
                        \'Status\': \'NOT_STARTED\'|\'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                        \'StatusDetail\': \'string\',
                        \'ProgressPercent\': 123
                    },
                    \'UpdateDateTime\': datetime(2015, 1, 1),
                    \'ResourceAttributeList\': [
                        {
                            \'Type\': \'IPV4_ADDRESS\'|\'IPV6_ADDRESS\'|\'MAC_ADDRESS\'|\'FQDN\'|\'VM_MANAGER_ID\'|\'VM_MANAGED_OBJECT_REFERENCE\'|\'VM_NAME\'|\'VM_PATH\'|\'BIOS_ID\'|\'MOTHERBOARD_SERIAL_NUMBER\',
                            \'Value\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **MigrationTask** *(dict) --* 
        
              Object encapsulating information about the migration task.
        
              - **ProgressUpdateStream** *(string) --* 
        
                A name that identifies the vendor of the migration tool being used.
        
              - **MigrationTaskName** *(string) --* 
        
                Unique identifier that references the migration task.
        
              - **Task** *(dict) --* 
        
                Task object encapsulating task information.
        
                - **Status** *(string) --* 
        
                  Status of the task - Not Started, In-Progress, Complete.
        
                - **StatusDetail** *(string) --* 
        
                  Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.
        
                - **ProgressPercent** *(integer) --* 
        
                  Indication of the percentage completion of the task.
        
              - **UpdateDateTime** *(datetime) --* 
        
                The timestamp when the task was gathered.
        
              - **ResourceAttributeList** *(list) --* 
        
                - *(dict) --* 
        
                  Attribute associated with a resource.
        
                  Note the corresponding format required per type listed below:
        
                    IPV4  
        
                   ``x.x.x.x``  
        
                   *where x is an integer in the range [0,255]*  
        
                    IPV6  
        
                   ``y : y : y : y : y : y : y : y``  
        
                   *where y is a hexadecimal between 0 and FFFF. [0, FFFF]*  
        
                    MAC_ADDRESS  
        
                   ``^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$``  
        
                    FQDN  
        
                   ``^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$``  
        
                  - **Type** *(string) --* 
        
                    Type of resource.
        
                  - **Value** *(string) --* 
        
                    Value of the resource type.
        
        """
        pass

    def disassociate_created_artifact(self, ProgressUpdateStream: str, MigrationTaskName: str, CreatedArtifactName: str, DryRun: bool = None) -> Dict:
        """
        Disassociates a created artifact of an AWS resource with a migration task performed by a migration tool that was previously associated. This API has the following traits:
        
        * A migration user can call the ``DisassociateCreatedArtifacts`` operation to disassociate a created AWS Artifact from a migration task. 
         
        * The created artifact name must be provided in ARN (Amazon Resource Name) format which will contain information about type and region; for example: ``arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b`` . 
         
        * Examples of the AWS resource behind the created artifact are, AMI\'s, EC2 instance, or RDS instance, etc. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DisassociateCreatedArtifact>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_created_artifact(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              CreatedArtifactName=\'string\',
              DryRun=True|False
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          Unique identifier that references the migration task to be disassociated with the artifact.
        
        :type CreatedArtifactName: string
        :param CreatedArtifactName: **[REQUIRED]** 
        
          An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_discovered_resource(self, ProgressUpdateStream: str, MigrationTaskName: str, ConfigurationId: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/DisassociateDiscoveredResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_discovered_resource(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              ConfigurationId=\'string\',
              DryRun=True|False
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream.
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          The identifier given to the MigrationTask.
        
        :type ConfigurationId: string
        :param ConfigurationId: **[REQUIRED]** 
        
          ConfigurationId of the ADS resource to be disassociated.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
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

    def import_migration_task(self, ProgressUpdateStream: str, MigrationTaskName: str, DryRun: bool = None) -> Dict:
        """
        
        This API is a prerequisite to calling the ``NotifyMigrationTaskState`` API as the migration tool must first register the migration task with Migration Hub.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ImportMigrationTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.import_migration_task(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              DryRun=True|False
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          Unique identifier that references the migration task.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def list_created_artifacts(self, ProgressUpdateStream: str, MigrationTaskName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists the created artifacts attached to a given migration task in an update stream. This API has the following traits:
        
        * Gets the list of the created artifacts while migration is taking place. 
         
        * Shows the artifacts created by the migration tool that was associated by the ``AssociateCreatedArtifact`` API.  
         
        * Lists created artifacts in a paginated interface.  
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListCreatedArtifacts>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_created_artifacts(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          Unique identifier that references the migration task.
        
        :type NextToken: string
        :param NextToken: 
        
          If a ``NextToken`` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in ``NextToken`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Maximum number of results to be returned per page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'CreatedArtifactList\': [
                    {
                        \'Name\': \'string\',
                        \'Description\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              If there are more created artifacts than the max result, return the next token to be passed to the next call as a bookmark of where to start from.
        
            - **CreatedArtifactList** *(list) --* 
        
              List of created artifacts up to the maximum number of results specified in the request.
        
              - *(dict) --* 
        
                An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance, RDS instance, etc.).
        
                - **Name** *(string) --* 
        
                  An ARN that uniquely identifies the result of a migration task.
        
                - **Description** *(string) --* 
        
                  A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.
        
        """
        pass

    def list_discovered_resources(self, ProgressUpdateStream: str, MigrationTaskName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListDiscoveredResources>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_discovered_resources(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream.
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          The name of the MigrationTask.
        
        :type NextToken: string
        :param NextToken: 
        
          If a ``NextToken`` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in ``NextToken`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results returned per page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'DiscoveredResourceList\': [
                    {
                        \'ConfigurationId\': \'string\',
                        \'Description\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              If there are more discovered resources than the max result, return the next token to be passed to the next call as a bookmark of where to start from.
        
            - **DiscoveredResourceList** *(list) --* 
        
              Returned list of discovered resources associated with the given MigrationTask.
        
              - *(dict) --* 
        
                Object representing the on-premises resource being migrated.
        
                - **ConfigurationId** *(string) --* 
        
                  The configurationId in ADS that uniquely identifies the on-premise resource.
        
                - **Description** *(string) --* 
        
                  A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.
        
        """
        pass

    def list_migration_tasks(self, NextToken: str = None, MaxResults: int = None, ResourceName: str = None) -> Dict:
        """
        Lists all, or filtered by resource name, migration tasks associated with the user account making this call. This API has the following traits:
        
        * Can show a summary list of the most recent migration tasks. 
         
        * Can show a summary list of migration tasks associated with a given discovered resource. 
         
        * Lists migration tasks in a paginated interface. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListMigrationTasks>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_migration_tasks(
              NextToken=\'string\',
              MaxResults=123,
              ResourceName=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          If a ``NextToken`` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in ``NextToken`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Value to specify how many results are returned per page.
        
        :type ResourceName: string
        :param ResourceName: 
        
          Filter migration tasks by discovered resource name.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'MigrationTaskSummaryList\': [
                    {
                        \'ProgressUpdateStream\': \'string\',
                        \'MigrationTaskName\': \'string\',
                        \'Status\': \'NOT_STARTED\'|\'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                        \'ProgressPercent\': 123,
                        \'StatusDetail\': \'string\',
                        \'UpdateDateTime\': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              If there are more migration tasks than the max result, return the next token to be passed to the next call as a bookmark of where to start from.
        
            - **MigrationTaskSummaryList** *(list) --* 
        
              Lists the migration task\'s summary which includes: ``MigrationTaskName`` , ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and the ``UpdateDateTime`` for each task.
        
              - *(dict) --* 
        
                MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.
        
                - **ProgressUpdateStream** *(string) --* 
        
                  An AWS resource used for access control. It should uniquely identify the migration tool as it is used for all updates made by the tool.
        
                - **MigrationTaskName** *(string) --* 
        
                  Unique identifier that references the migration task.
        
                - **Status** *(string) --* 
        
                  Status of the task.
        
                - **ProgressPercent** *(integer) --* 
        
                - **StatusDetail** *(string) --* 
        
                  Detail information of what is being done within the overall status state.
        
                - **UpdateDateTime** *(datetime) --* 
        
                  The timestamp when the task was gathered.
        
        """
        pass

    def list_progress_update_streams(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_progress_update_streams(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          If a ``NextToken`` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in ``NextToken`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Filter to limit the maximum number of results to list per page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ProgressUpdateStreamSummaryList\': [
                    {
                        \'ProgressUpdateStreamName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ProgressUpdateStreamSummaryList** *(list) --* 
        
              List of progress update streams up to the max number of results passed in the input.
        
              - *(dict) --* 
        
                Summary of the AWS resource used for access control that is implicitly linked to your AWS account.
        
                - **ProgressUpdateStreamName** *(string) --* 
        
                  The name of the ProgressUpdateStream. 
        
            - **NextToken** *(string) --* 
        
              If there are more streams created than the max result, return the next token to be passed to the next call as a bookmark of where to start from.
        
        """
        pass

    def notify_application_state(self, ApplicationId: str, Status: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/NotifyApplicationState>`_
        
        **Request Syntax** 
        ::
        
          response = client.notify_application_state(
              ApplicationId=\'string\',
              Status=\'NOT_STARTED\'|\'IN_PROGRESS\'|\'COMPLETED\',
              DryRun=True|False
          )
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]** 
        
          The configurationId in ADS that uniquely identifies the grouped application.
        
        :type Status: string
        :param Status: **[REQUIRED]** 
        
          Status of the application - Not Started, In-Progress, Complete.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def notify_migration_task_state(self, ProgressUpdateStream: str, MigrationTaskName: str, Task: Dict, UpdateDateTime: datetime, NextUpdateSeconds: int, DryRun: bool = None) -> Dict:
        """
        Notifies Migration Hub of the current status, progress, or other detail regarding a migration task. This API has the following traits:
        
        * Migration tools will call the ``NotifyMigrationTaskState`` API to share the latest progress and status. 
         
        * ``MigrationTaskName`` is used for addressing updates to the correct target. 
         
        * ``ProgressUpdateStream`` is used for access control and to provide a namespace for each migration tool. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState>`_
        
        **Request Syntax** 
        ::
        
          response = client.notify_migration_task_state(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              Task={
                  \'Status\': \'NOT_STARTED\'|\'IN_PROGRESS\'|\'FAILED\'|\'COMPLETED\',
                  \'StatusDetail\': \'string\',
                  \'ProgressPercent\': 123
              },
              UpdateDateTime=datetime(2015, 1, 1),
              NextUpdateSeconds=123,
              DryRun=True|False
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          Unique identifier that references the migration task.
        
        :type Task: dict
        :param Task: **[REQUIRED]** 
        
          Information about the task\'s progress and status.
        
          - **Status** *(string) --* **[REQUIRED]** 
        
            Status of the task - Not Started, In-Progress, Complete.
        
          - **StatusDetail** *(string) --* 
        
            Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.
        
          - **ProgressPercent** *(integer) --* 
        
            Indication of the percentage completion of the task.
        
        :type UpdateDateTime: datetime
        :param UpdateDateTime: **[REQUIRED]** 
        
          The timestamp when the task was gathered.
        
        :type NextUpdateSeconds: integer
        :param NextUpdateSeconds: **[REQUIRED]** 
        
          Number of seconds after the UpdateDateTime within which the Migration Hub can expect an update. If Migration Hub does not receive an update within the specified interval, then the migration task will be considered stale.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def put_resource_attributes(self, ProgressUpdateStream: str, MigrationTaskName: str, ResourceAttributeList: List, DryRun: bool = None) -> Dict:
        """
        
        Provides identifying details of the resource being migrated so that it can be associated in the Application Discovery Service (ADS)\'s repository. This association occurs asynchronously after ``PutResourceAttributes`` returns.
        
        .. warning::
        
          * Keep in mind that subsequent calls to PutResourceAttributes will override previously stored attributes. For example, if it is first called with a MAC address, but later, it is desired to *add* an IP address, it will then be required to call it with *both* the IP and MAC addresses to prevent overiding the MAC address. 
           
          * Note the instructions regarding the special use case of the ` ``ResourceAttributeList`` https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html#migrationhub-PutResourceAttributes-request-ResourceAttributeList`__ parameter when specifying any \"VM\" related value.  
           
        .. note::
        
          Because this is an asynchronous call, it will always return 200, whether an association occurs or not. To confirm if an association was found based on the provided details, call ``ListDiscoveredResources`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/PutResourceAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_resource_attributes(
              ProgressUpdateStream=\'string\',
              MigrationTaskName=\'string\',
              ResourceAttributeList=[
                  {
                      \'Type\': \'IPV4_ADDRESS\'|\'IPV6_ADDRESS\'|\'MAC_ADDRESS\'|\'FQDN\'|\'VM_MANAGER_ID\'|\'VM_MANAGED_OBJECT_REFERENCE\'|\'VM_NAME\'|\'VM_PATH\'|\'BIOS_ID\'|\'MOTHERBOARD_SERIAL_NUMBER\',
                      \'Value\': \'string\'
                  },
              ],
              DryRun=True|False
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]** 
        
          The name of the ProgressUpdateStream. 
        
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]** 
        
          Unique identifier that references the migration task.
        
        :type ResourceAttributeList: list
        :param ResourceAttributeList: **[REQUIRED]** 
        
          Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service (ADS)\'s repository.
        
          .. note::
        
            Takes the object array of ``ResourceAttribute`` where the ``Type`` field is reserved for the following values: ``IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER`` where the identifying value can be a string up to 256 characters.
        
          .. warning::
        
            * If any \"VM\" related value is set for a ``ResourceAttribute`` object, it is required that ``VM_MANAGER_ID`` , as a minimum, is always set. If ``VM_MANAGER_ID`` is not set, then all \"VM\" fields will be discarded and \"VM\" fields will not be used for matching the migration task to a server in Application Discovery Service (ADS)\'s repository. See the `Example <https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html#API_PutResourceAttributes_Examples>`__ section below for a use case of specifying \"VM\" related values. 
             
            * If a server you are trying to match has multiple IP or MAC addresses, you should provide as many as you know in separate type/value pairs passed to the ``ResourceAttributeList`` parameter to maximize the chances of matching. 
             
          - *(dict) --* 
        
            Attribute associated with a resource.
        
            Note the corresponding format required per type listed below:
        
              IPV4  
        
             ``x.x.x.x``  
        
             *where x is an integer in the range [0,255]*  
        
              IPV6  
        
             ``y : y : y : y : y : y : y : y``  
        
             *where y is a hexadecimal between 0 and FFFF. [0, FFFF]*  
        
              MAC_ADDRESS  
        
             ``^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$``  
        
              FQDN  
        
             ``^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$``  
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              Type of resource.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              Value of the resource type.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
