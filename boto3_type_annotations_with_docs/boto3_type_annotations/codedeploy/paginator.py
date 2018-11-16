from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListApplicationRevisions(Paginator):
    def paginate(self, applicationName: str, sortBy: str = None, sortOrder: str = None, s3Bucket: str = None, s3KeyPrefix: str = None, deployed: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplicationRevisions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              applicationName=\'string\',
              sortBy=\'registerTime\'|\'firstUsedTime\'|\'lastUsedTime\',
              sortOrder=\'ascending\'|\'descending\',
              s3Bucket=\'string\',
              s3KeyPrefix=\'string\',
              deployed=\'include\'|\'exclude\'|\'ignore\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]** 
        
          The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
        
        :type sortBy: string
        :param sortBy: 
        
          The column name to use to sort the list results:
        
          * registerTime: Sort by the time the revisions were registered with AWS CodeDeploy. 
           
          * firstUsedTime: Sort by the time the revisions were first used in a deployment. 
           
          * lastUsedTime: Sort by the time the revisions were last used in a deployment. 
           
          If not specified or set to null, the results will be returned in an arbitrary order.
        
        :type sortOrder: string
        :param sortOrder: 
        
          The order in which to sort the list results:
        
          * ascending: ascending order. 
           
          * descending: descending order. 
           
          If not specified, the results will be sorted in ascending order.
        
          If set to null, the results will be sorted in an arbitrary order.
        
        :type s3Bucket: string
        :param s3Bucket: 
        
          An Amazon S3 bucket name to limit the search for revisions.
        
          If set to null, all of the user\'s buckets will be searched.
        
        :type s3KeyPrefix: string
        :param s3KeyPrefix: 
        
          A key prefix for the set of Amazon S3 objects to limit the search for revisions.
        
        :type deployed: string
        :param deployed: 
        
          Whether to list revisions based on whether the revision is the target revision of an deployment group:
        
          * include: List revisions that are target revisions of a deployment group. 
           
          * exclude: Do not list revisions that are target revisions of a deployment group. 
           
          * ignore: List all revisions. 
           
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
                \'revisions\': [
                    {
                        \'revisionType\': \'S3\'|\'GitHub\'|\'String\',
                        \'s3Location\': {
                            \'bucket\': \'string\',
                            \'key\': \'string\',
                            \'bundleType\': \'tar\'|\'tgz\'|\'zip\'|\'YAML\'|\'JSON\',
                            \'version\': \'string\',
                            \'eTag\': \'string\'
                        },
                        \'gitHubLocation\': {
                            \'repository\': \'string\',
                            \'commitId\': \'string\'
                        },
                        \'string\': {
                            \'content\': \'string\',
                            \'sha256\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListApplicationRevisions operation.
        
            - **revisions** *(list) --* 
        
              A list of locations that contain the matching revisions.
        
              - *(dict) --* 
        
                Information about the location of an application revision.
        
                - **revisionType** *(string) --* 
        
                  The type of application revision:
        
                  * S3: An application revision stored in Amazon S3. 
                   
                  * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only) 
                   
                  * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only) 
                   
                - **s3Location** *(dict) --* 
        
                  Information about the location of a revision stored in Amazon S3. 
        
                  - **bucket** *(string) --* 
        
                    The name of the Amazon S3 bucket where the application revision is stored.
        
                  - **key** *(string) --* 
        
                    The name of the Amazon S3 object that represents the bundled artifacts for the application revision.
        
                  - **bundleType** *(string) --* 
        
                    The file type of the application revision. Must be one of the following:
        
                    * tar: A tar archive file. 
                     
                    * tgz: A compressed tar archive file. 
                     
                    * zip: A zip archive file. 
                     
                  - **version** *(string) --* 
        
                    A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
        
                    If the version is not specified, the system will use the most recent version by default.
        
                  - **eTag** *(string) --* 
        
                    The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
        
                    If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.
        
                - **gitHubLocation** *(dict) --* 
        
                  Information about the location of application artifacts stored in GitHub.
        
                  - **repository** *(string) --* 
        
                    The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. 
        
                    Specified as account/repository.
        
                  - **commitId** *(string) --* 
        
                    The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.
        
                - **string** *(dict) --* 
        
                  Information about the location of an AWS Lambda deployment revision stored as a RawString.
        
                  - **content** *(string) --* 
        
                    The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.
        
                  - **sha256** *(string) --* 
        
                    The SHA256 hash value of the revision that is specified as a RawString.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListApplications(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplications>`_
        
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
                \'applications\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListApplications operation.
        
            - **applications** *(list) --* 
        
              A list of application names.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListDeploymentConfigs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentConfigs>`_
        
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
                \'deploymentConfigsList\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListDeploymentConfigs operation.
        
            - **deploymentConfigsList** *(list) --* 
        
              A list of deployment configurations, including built-in configurations such as CodeDeployDefault.OneAtATime.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListDeploymentGroups(Paginator):
    def paginate(self, applicationName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              applicationName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]** 
        
          The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
        
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
                \'applicationName\': \'string\',
                \'deploymentGroups\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListDeploymentGroups operation.
        
            - **applicationName** *(string) --* 
        
              The application name.
        
            - **deploymentGroups** *(list) --* 
        
              A list of corresponding deployment group names.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListDeploymentInstances(Paginator):
    def paginate(self, deploymentId: str, instanceStatusFilter: List = None, instanceTypeFilter: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              deploymentId=\'string\',
              instanceStatusFilter=[
                  \'Pending\'|\'InProgress\'|\'Succeeded\'|\'Failed\'|\'Skipped\'|\'Unknown\'|\'Ready\',
              ],
              instanceTypeFilter=[
                  \'Blue\'|\'Green\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]** 
        
          The unique ID of a deployment.
        
        :type instanceStatusFilter: list
        :param instanceStatusFilter: 
        
          A subset of instances to list by status:
        
          * Pending: Include those instance with pending deployments. 
           
          * InProgress: Include those instance where deployments are still in progress. 
           
          * Succeeded: Include those instances with successful deployments. 
           
          * Failed: Include those instance with failed deployments. 
           
          * Skipped: Include those instance with skipped deployments. 
           
          * Unknown: Include those instance with deployments in an unknown state. 
           
          - *(string) --* 
        
        :type instanceTypeFilter: list
        :param instanceTypeFilter: 
        
          The set of instances in a blue/green deployment, either those in the original environment (\"BLUE\") or those in the replacement environment (\"GREEN\"), for which you want to view instance information.
        
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
                \'instancesList\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListDeploymentInstances operation.
        
            - **instancesList** *(list) --* 
        
              A list of instance IDs.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListDeployments(Paginator):
    def paginate(self, applicationName: str = None, deploymentGroupName: str = None, includeOnlyStatuses: List = None, createTimeRange: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeployments>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              applicationName=\'string\',
              deploymentGroupName=\'string\',
              includeOnlyStatuses=[
                  \'Created\'|\'Queued\'|\'InProgress\'|\'Succeeded\'|\'Failed\'|\'Stopped\'|\'Ready\',
              ],
              createTimeRange={
                  \'start\': datetime(2015, 1, 1),
                  \'end\': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type applicationName: string
        :param applicationName: 
        
          The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
        
        :type deploymentGroupName: string
        :param deploymentGroupName: 
        
          The name of an existing deployment group for the specified application.
        
        :type includeOnlyStatuses: list
        :param includeOnlyStatuses: 
        
          A subset of deployments to list by status:
        
          * Created: Include created deployments in the resulting list. 
           
          * Queued: Include queued deployments in the resulting list. 
           
          * In Progress: Include in-progress deployments in the resulting list. 
           
          * Succeeded: Include successful deployments in the resulting list. 
           
          * Failed: Include failed deployments in the resulting list. 
           
          * Stopped: Include stopped deployments in the resulting list. 
           
          - *(string) --* 
        
        :type createTimeRange: dict
        :param createTimeRange: 
        
          A time range (start and end) for returning a subset of the list of deployments.
        
          - **start** *(datetime) --* 
        
            The start time of the time range.
        
            .. note::
        
              Specify null to leave the start time open-ended.
        
          - **end** *(datetime) --* 
        
            The end time of the time range.
        
            .. note::
        
              Specify null to leave the end time open-ended.
        
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
                \'deployments\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListDeployments operation.
        
            - **deployments** *(list) --* 
        
              A list of deployment IDs.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
