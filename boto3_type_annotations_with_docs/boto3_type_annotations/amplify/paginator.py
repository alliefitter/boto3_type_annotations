from typing import Dict
from botocore.paginate import Paginator


class ListApps(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Amplify.Client.list_apps`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListApps>`_
        
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
                'apps': [
                    {
                        'appId': 'string',
                        'appArn': 'string',
                        'name': 'string',
                        'tags': {
                            'string': 'string'
                        },
                        'description': 'string',
                        'repository': 'string',
                        'platform': 'IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
                        'createTime': datetime(2015, 1, 1),
                        'updateTime': datetime(2015, 1, 1),
                        'iamServiceRoleArn': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'defaultDomain': 'string',
                        'enableBranchAutoBuild': True|False,
                        'enableBasicAuth': True|False,
                        'basicAuthCredentials': 'string',
                        'customRules': [
                            {
                                'source': 'string',
                                'target': 'string',
                                'status': 'string',
                                'condition': 'string'
                            },
                        ],
                        'productionBranch': {
                            'lastDeployTime': datetime(2015, 1, 1),
                            'status': 'string',
                            'thumbnailUrl': 'string',
                            'branchName': 'string'
                        },
                        'buildSpec': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for an Amplify App list request. 
            - **apps** *(list) --* 
              List of Amplify Apps. 
              - *(dict) --* 
                Amplify App represents different branches of a repository for building, deploying, and hosting. 
                - **appId** *(string) --* 
                  Unique Id for the Amplify App. 
                - **appArn** *(string) --* 
                  ARN for the Amplify App. 
                - **name** *(string) --* 
                  Name for the Amplify App. 
                - **tags** *(dict) --* 
                  Tag for Amplify App. 
                  - *(string) --* 
                    - *(string) --* 
                - **description** *(string) --* 
                  Description for the Amplify App. 
                - **repository** *(string) --* 
                  Repository for the Amplify App. 
                - **platform** *(string) --* 
                  Platform for the Amplify App. 
                - **createTime** *(datetime) --* 
                  Create date / time for the Amplify App. 
                - **updateTime** *(datetime) --* 
                  Update date / time for the Amplify App. 
                - **iamServiceRoleArn** *(string) --* 
                  IAM service role ARN for the Amplify App. 
                - **environmentVariables** *(dict) --* 
                  Environment Variables for the Amplify App. 
                  - *(string) --* 
                    - *(string) --* 
                - **defaultDomain** *(string) --* 
                  Default domain for the Amplify App. 
                - **enableBranchAutoBuild** *(boolean) --* 
                  Enables auto-building of branches for the Amplify App. 
                - **enableBasicAuth** *(boolean) --* 
                  Enables Basic Authorization for branches for the Amplify App. 
                - **basicAuthCredentials** *(string) --* 
                  Basic Authorization credentials for branches for the Amplify App. 
                - **customRules** *(list) --* 
                  Custom redirect / rewrite rules for the Amplify App. 
                  - *(dict) --* 
                    Custom rewrite / redirect rule. 
                    - **source** *(string) --* 
                      The source pattern for a URL rewrite or redirect rule. 
                    - **target** *(string) --* 
                      The target pattern for a URL rewrite or redirect rule. 
                    - **status** *(string) --* 
                      The status code for a URL rewrite or redirect rule. 
                    - **condition** *(string) --* 
                      The condition for a URL rewrite or redirect rule, e.g. country code. 
                - **productionBranch** *(dict) --* 
                  Structure with Production Branch information. 
                  - **lastDeployTime** *(datetime) --* 
                    Last Deploy Time of Production Branch. 
                  - **status** *(string) --* 
                    Status of Production Branch. 
                  - **thumbnailUrl** *(string) --* 
                    Thumbnail Url for Production Branch. 
                  - **branchName** *(string) --* 
                    Branch Name for Production Branch. 
                - **buildSpec** *(string) --* 
                  BuildSpec content for Amplify App. 
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


class ListBranches(Paginator):
    def paginate(self, appId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Amplify.Client.list_branches`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListBranches>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              appId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'branches': [
                    {
                        'branchArn': 'string',
                        'branchName': 'string',
                        'description': 'string',
                        'tags': {
                            'string': 'string'
                        },
                        'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
                        'displayName': 'string',
                        'enableNotification': True|False,
                        'createTime': datetime(2015, 1, 1),
                        'updateTime': datetime(2015, 1, 1),
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'enableAutoBuild': True|False,
                        'customDomains': [
                            'string',
                        ],
                        'framework': 'string',
                        'activeJobId': 'string',
                        'totalNumberOfJobs': 'string',
                        'enableBasicAuth': True|False,
                        'thumbnailUrl': 'string',
                        'basicAuthCredentials': 'string',
                        'buildSpec': 'string',
                        'ttl': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for list branches request. 
            - **branches** *(list) --* 
              List of branches for an Amplify App. 
              - *(dict) --* 
                Branch for an Amplify App, which maps to a 3rd party repository branch. 
                - **branchArn** *(string) --* 
                  ARN for a branch, part of an Amplify App. 
                - **branchName** *(string) --* 
                  Name for a branch, part of an Amplify App. 
                - **description** *(string) --* 
                  Description for a branch, part of an Amplify App. 
                - **tags** *(dict) --* 
                  Tag for branch for Amplify App. 
                  - *(string) --* 
                    - *(string) --* 
                - **stage** *(string) --* 
                  Stage for a branch, part of an Amplify App. 
                - **displayName** *(string) --* 
                  Display name for a branch, part of an Amplify App. 
                - **enableNotification** *(boolean) --* 
                  Enables notifications for a branch, part of an Amplify App. 
                - **createTime** *(datetime) --* 
                  Creation date and time for a branch, part of an Amplify App. 
                - **updateTime** *(datetime) --* 
                  Last updated date and time for a branch, part of an Amplify App. 
                - **environmentVariables** *(dict) --* 
                  Environment Variables specific to a branch, part of an Amplify App. 
                  - *(string) --* 
                    - *(string) --* 
                - **enableAutoBuild** *(boolean) --* 
                  Enables auto-building on push for a branch, part of an Amplify App. 
                - **customDomains** *(list) --* 
                  Custom domains for a branch, part of an Amplify App. 
                  - *(string) --* 
                - **framework** *(string) --* 
                  Framework for a branch, part of an Amplify App. 
                - **activeJobId** *(string) --* 
                  Id of the active job for a branch, part of an Amplify App. 
                - **totalNumberOfJobs** *(string) --* 
                  Total number of Jobs part of an Amplify App. 
                - **enableBasicAuth** *(boolean) --* 
                  Enables Basic Authorization for a branch, part of an Amplify App. 
                - **thumbnailUrl** *(string) --* 
                  Thumbnail Url for the branch. 
                - **basicAuthCredentials** *(string) --* 
                  Basic Authorization credentials for a branch, part of an Amplify App. 
                - **buildSpec** *(string) --* 
                  BuildSpec content for branch for Amplify App. 
                - **ttl** *(string) --* 
                  The content TTL for the website in seconds. 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
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


class ListDomainAssociations(Paginator):
    def paginate(self, appId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Amplify.Client.list_domain_associations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListDomainAssociations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              appId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'domainAssociations': [
                    {
                        'domainAssociationArn': 'string',
                        'domainName': 'string',
                        'enableAutoSubDomain': True|False,
                        'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED',
                        'statusReason': 'string',
                        'certificateVerificationDNSRecord': 'string',
                        'subDomains': [
                            {
                                'subDomainSetting': {
                                    'prefix': 'string',
                                    'branchName': 'string'
                                },
                                'verified': True|False,
                                'dnsRecord': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for the list Domain Association request. 
            - **domainAssociations** *(list) --* 
              List of Domain Associations. 
              - *(dict) --* 
                Structure for Domain Association, which associates a custom domain with an Amplify App. 
                - **domainAssociationArn** *(string) --* 
                  ARN for the Domain Association. 
                - **domainName** *(string) --* 
                  Name of the domain. 
                - **enableAutoSubDomain** *(boolean) --* 
                  Enables automated creation of Subdomains for branches. 
                - **domainStatus** *(string) --* 
                  Status fo the Domain Association. 
                - **statusReason** *(string) --* 
                  Reason for the current status of the Domain Association. 
                - **certificateVerificationDNSRecord** *(string) --* 
                  DNS Record for certificate verification. 
                - **subDomains** *(list) --* 
                  Subdomains for the Domain Association. 
                  - *(dict) --* 
                    Subdomain for the Domain Association. 
                    - **subDomainSetting** *(dict) --* 
                      Setting structure for the Subdomain. 
                      - **prefix** *(string) --* 
                        Prefix setting for the Subdomain. 
                      - **branchName** *(string) --* 
                        Branch name setting for the Subdomain. 
                    - **verified** *(boolean) --* 
                      Verified status of the Subdomain 
                    - **dnsRecord** *(string) --* 
                      DNS record for the Subdomain. 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
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


class ListJobs(Paginator):
    def paginate(self, appId: str, branchName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Amplify.Client.list_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              appId='string',
              branchName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'jobSummaries': [
                    {
                        'jobArn': 'string',
                        'jobId': 'string',
                        'commitId': 'string',
                        'commitMessage': 'string',
                        'commitTime': datetime(2015, 1, 1),
                        'startTime': datetime(2015, 1, 1),
                        'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                        'endTime': datetime(2015, 1, 1),
                        'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Maximum number of records to list in a single response. 
            - **jobSummaries** *(list) --* 
              Result structure for list job result request. 
              - *(dict) --* 
                Structure for the summary of a Job. 
                - **jobArn** *(string) --* 
                  Arn for the Job. 
                - **jobId** *(string) --* 
                  Unique Id for the Job. 
                - **commitId** *(string) --* 
                  Commit Id from 3rd party repository provider for the Job. 
                - **commitMessage** *(string) --* 
                  Commit message from 3rd party repository provider for the Job. 
                - **commitTime** *(datetime) --* 
                  Commit date / time for the Job. 
                - **startTime** *(datetime) --* 
                  Start date / time for the Job. 
                - **status** *(string) --* 
                  Status for the Job. 
                - **endTime** *(datetime) --* 
                  End date / time for the Job. 
                - **jobType** *(string) --* 
                  Type for the Job. 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for a branch.
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
