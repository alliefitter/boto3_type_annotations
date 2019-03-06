from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from datetime import datetime
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

    def create_app(self, name: str, repository: str, platform: str, oauthToken: str, description: str = None, iamServiceRoleArn: str = None, environmentVariables: Dict = None, enableBranchAutoBuild: bool = None, enableBasicAuth: bool = None, basicAuthCredentials: str = None, customRules: List = None, tags: Dict = None, buildSpec: str = None) -> Dict:
        """
        Creates a new Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateApp>`_
        
        **Request Syntax**
        ::
          response = client.create_app(
              name='string',
              description='string',
              repository='string',
              platform='IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
              iamServiceRoleArn='string',
              oauthToken='string',
              environmentVariables={
                  'string': 'string'
              },
              enableBranchAutoBuild=True|False,
              enableBasicAuth=True|False,
              basicAuthCredentials='string',
              customRules=[
                  {
                      'source': 'string',
                      'target': 'string',
                      'status': 'string',
                      'condition': 'string'
                  },
              ],
              tags={
                  'string': 'string'
              },
              buildSpec='string'
          )
        
        **Response Syntax**
        ::
            {
                'app': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **app** *(dict) --* 
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
        :type name: string
        :param name: **[REQUIRED]**
          Name for the Amplify App
        :type description: string
        :param description:
          Description for an Amplify App
        :type repository: string
        :param repository: **[REQUIRED]**
          Repository for an Amplify App
        :type platform: string
        :param platform: **[REQUIRED]**
          Platform / framework for an Amplify App
        :type iamServiceRoleArn: string
        :param iamServiceRoleArn:
          AWS IAM service role for an Amplify App
        :type oauthToken: string
        :param oauthToken: **[REQUIRED]**
          OAuth token for 3rd party source control system for an Amplify App, used to create webhook and read-only deploy key. OAuth token is not stored.
        :type environmentVariables: dict
        :param environmentVariables:
          Environment variables map for an Amplify App.
          - *(string) --*
            - *(string) --*
        :type enableBranchAutoBuild: boolean
        :param enableBranchAutoBuild:
          Enable the auto building of branches for an Amplify App.
        :type enableBasicAuth: boolean
        :param enableBasicAuth:
          Enable Basic Authorization for an Amplify App, this will apply to all branches part of this App.
        :type basicAuthCredentials: string
        :param basicAuthCredentials:
          Credentials for Basic Authorization for an Amplify App.
        :type customRules: list
        :param customRules:
          Custom rewrite / redirect rules for an Amplify App.
          - *(dict) --*
            Custom rewrite / redirect rule.
            - **source** *(string) --* **[REQUIRED]**
              The source pattern for a URL rewrite or redirect rule.
            - **target** *(string) --* **[REQUIRED]**
              The target pattern for a URL rewrite or redirect rule.
            - **status** *(string) --*
              The status code for a URL rewrite or redirect rule.
            - **condition** *(string) --*
              The condition for a URL rewrite or redirect rule, e.g. country code.
        :type tags: dict
        :param tags:
          Tag for an Amplify App
          - *(string) --*
            - *(string) --*
        :type buildSpec: string
        :param buildSpec:
          BuildSpec for an Amplify App
        :rtype: dict
        :returns:
        """
        pass

    def create_branch(self, appId: str, branchName: str, description: str = None, stage: str = None, framework: str = None, enableNotification: bool = None, enableAutoBuild: bool = None, environmentVariables: Dict = None, basicAuthCredentials: str = None, enableBasicAuth: bool = None, tags: Dict = None, buildSpec: str = None, ttl: str = None) -> Dict:
        """
        Creates a new Branch for an Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateBranch>`_
        
        **Request Syntax**
        ::
          response = client.create_branch(
              appId='string',
              branchName='string',
              description='string',
              stage='PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
              framework='string',
              enableNotification=True|False,
              enableAutoBuild=True|False,
              environmentVariables={
                  'string': 'string'
              },
              basicAuthCredentials='string',
              enableBasicAuth=True|False,
              tags={
                  'string': 'string'
              },
              buildSpec='string',
              ttl='string'
          )
        
        **Response Syntax**
        ::
            {
                'branch': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for create branch request. 
            - **branch** *(dict) --* 
              Branch structure for an Amplify App. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for the branch.
        :type description: string
        :param description:
          Description for the branch.
        :type stage: string
        :param stage:
          Stage for the branch.
        :type framework: string
        :param framework:
          Framework for the branch.
        :type enableNotification: boolean
        :param enableNotification:
          Enables notifications for the branch.
        :type enableAutoBuild: boolean
        :param enableAutoBuild:
          Enables auto building for the branch.
        :type environmentVariables: dict
        :param environmentVariables:
          Environment Variables for the branch.
          - *(string) --*
            - *(string) --*
        :type basicAuthCredentials: string
        :param basicAuthCredentials:
          Basic Authorization credentials for the branch.
        :type enableBasicAuth: boolean
        :param enableBasicAuth:
          Enables Basic Auth for the branch.
        :type tags: dict
        :param tags:
          Tag for the branch.
          - *(string) --*
            - *(string) --*
        :type buildSpec: string
        :param buildSpec:
          BuildSpec for the branch.
        :type ttl: string
        :param ttl:
          The content TTL for the website in seconds.
        :rtype: dict
        :returns:
        """
        pass

    def create_domain_association(self, appId: str, domainName: str, subDomainSettings: List, enableAutoSubDomain: bool = None) -> Dict:
        """
        Create a new DomainAssociation on an App 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateDomainAssociation>`_
        
        **Request Syntax**
        ::
          response = client.create_domain_association(
              appId='string',
              domainName='string',
              enableAutoSubDomain=True|False,
              subDomainSettings=[
                  {
                      'prefix': 'string',
                      'branchName': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'domainAssociation': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for the create Domain Association request. 
            - **domainAssociation** *(dict) --* 
              Domain Association structure. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type domainName: string
        :param domainName: **[REQUIRED]**
          Domain name for the Domain Association.
        :type enableAutoSubDomain: boolean
        :param enableAutoSubDomain:
          Enables automated creation of Subdomains for branches.
        :type subDomainSettings: list
        :param subDomainSettings: **[REQUIRED]**
          Setting structure for the Subdomain.
          - *(dict) --*
            Setting for the Subdomain.
            - **prefix** *(string) --* **[REQUIRED]**
              Prefix setting for the Subdomain.
            - **branchName** *(string) --* **[REQUIRED]**
              Branch name setting for the Subdomain.
        :rtype: dict
        :returns:
        """
        pass

    def delete_app(self, appId: str) -> Dict:
        """
        Delete an existing Amplify App by appId. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteApp>`_
        
        **Request Syntax**
        ::
          response = client.delete_app(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {
                'app': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for an Amplify App delete request. 
            - **app** *(dict) --* 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :rtype: dict
        :returns:
        """
        pass

    def delete_branch(self, appId: str, branchName: str) -> Dict:
        """
        Deletes a branch for an Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteBranch>`_
        
        **Request Syntax**
        ::
          response = client.delete_branch(
              appId='string',
              branchName='string'
          )
        
        **Response Syntax**
        ::
            {
                'branch': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for delete branch request. 
            - **branch** *(dict) --* 
              Branch structure for an Amplify App. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for the branch.
        :rtype: dict
        :returns:
        """
        pass

    def delete_domain_association(self, appId: str, domainName: str) -> Dict:
        """
        Deletes a DomainAssociation. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteDomainAssociation>`_
        
        **Request Syntax**
        ::
          response = client.delete_domain_association(
              appId='string',
              domainName='string'
          )
        
        **Response Syntax**
        ::
            {
                'domainAssociation': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **domainAssociation** *(dict) --* 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type domainName: string
        :param domainName: **[REQUIRED]**
          Name of the domain.
        :rtype: dict
        :returns:
        """
        pass

    def delete_job(self, appId: str, branchName: str, jobId: str) -> Dict:
        """
        Delete a job, for an Amplify branch, part of Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteJob>`_
        
        **Request Syntax**
        ::
          response = client.delete_job(
              appId='string',
              branchName='string',
              jobId='string'
          )
        
        **Response Syntax**
        ::
            {
                'jobSummary': {
                    'jobArn': 'string',
                    'jobId': 'string',
                    'commitId': 'string',
                    'commitMessage': 'string',
                    'commitTime': datetime(2015, 1, 1),
                    'startTime': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                    'endTime': datetime(2015, 1, 1),
                    'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for the delete job request. 
            - **jobSummary** *(dict) --* 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for the branch, for the Job.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          Unique Id for the Job.
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

    def get_app(self, appId: str) -> Dict:
        """
        Retrieves an existing Amplify App by appId. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetApp>`_
        
        **Request Syntax**
        ::
          response = client.get_app(
              appId='string'
          )
        
        **Response Syntax**
        ::
            {
                'app': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **app** *(dict) --* 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :rtype: dict
        :returns:
        """
        pass

    def get_branch(self, appId: str, branchName: str) -> Dict:
        """
        Retrieves a branch for an Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetBranch>`_
        
        **Request Syntax**
        ::
          response = client.get_branch(
              appId='string',
              branchName='string'
          )
        
        **Response Syntax**
        ::
            {
                'branch': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **branch** *(dict) --* 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for the branch.
        :rtype: dict
        :returns:
        """
        pass

    def get_domain_association(self, appId: str, domainName: str) -> Dict:
        """
        Retrieves domain info that corresponds to an appId and domainName. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetDomainAssociation>`_
        
        **Request Syntax**
        ::
          response = client.get_domain_association(
              appId='string',
              domainName='string'
          )
        
        **Response Syntax**
        ::
            {
                'domainAssociation': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for the get Domain Association request. 
            - **domainAssociation** *(dict) --* 
              Domain Association structure. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type domainName: string
        :param domainName: **[REQUIRED]**
          Name of the domain.
        :rtype: dict
        :returns:
        """
        pass

    def get_job(self, appId: str, branchName: str, jobId: str) -> Dict:
        """
        Get a job for a branch, part of an Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetJob>`_
        
        **Request Syntax**
        ::
          response = client.get_job(
              appId='string',
              branchName='string',
              jobId='string'
          )
        
        **Response Syntax**
        ::
            {
                'job': {
                    'summary': {
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
                    'steps': [
                        {
                            'stepName': 'string',
                            'startTime': datetime(2015, 1, 1),
                            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                            'endTime': datetime(2015, 1, 1),
                            'logUrl': 'string',
                            'artifactsUrl': 'string',
                            'screenshots': {
                                'string': 'string'
                            }
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **job** *(dict) --* 
              Structure for an execution job for an Amplify App. 
              - **summary** *(dict) --* 
                Summary for an execution job for an Amplify App. 
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
              - **steps** *(list) --* 
                Execution steps for an execution job, for an Amplify App. 
                - *(dict) --* 
                  Structure for an execution step for an execution job, for an Amplify App. 
                  - **stepName** *(string) --* 
                    Name of the execution step. 
                  - **startTime** *(datetime) --* 
                    Start date/ time of the execution step. 
                  - **status** *(string) --* 
                    Status of the execution step. 
                  - **endTime** *(datetime) --* 
                    End date/ time of the execution step. 
                  - **logUrl** *(string) --* 
                    Url to the logs for the execution step. 
                  - **artifactsUrl** *(string) --* 
                    Url to teh artifact for the execution step. 
                  - **screenshots** *(dict) --* 
                    List of screenshot Urls for the execution step, if relevant. 
                    - *(string) --* 
                      - *(string) --* 
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for the branch, for the Job.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          Unique Id for the Job.
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

    def list_apps(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists existing Amplify Apps. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListApps>`_
        
        **Request Syntax**
        ::
          response = client.list_apps(
              nextToken='string',
              maxResults=123
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              Pagination token. Set to null to start listing Apps from start. If non-null pagination token is returned in a result, then pass its value in here to list more projects. 
        :type nextToken: string
        :param nextToken:
          Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.
        :type maxResults: integer
        :param maxResults:
          Maximum number of records to list in a single response.
        :rtype: dict
        :returns:
        """
        pass

    def list_branches(self, appId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists branches for an Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListBranches>`_
        
        **Request Syntax**
        ::
          response = client.list_branches(
              appId='string',
              nextToken='string',
              maxResults=123
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries. 
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type nextToken: string
        :param nextToken:
          Pagination token. Set to null to start listing branches from start. If a non-null pagination token is returned in a result, then pass its value in here to list more branches.
        :type maxResults: integer
        :param maxResults:
          Maximum number of records to list in a single response.
        :rtype: dict
        :returns:
        """
        pass

    def list_domain_associations(self, appId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        List domains with an app 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListDomainAssociations>`_
        
        **Request Syntax**
        ::
          response = client.list_domain_associations(
              appId='string',
              nextToken='string',
              maxResults=123
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries. 
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type nextToken: string
        :param nextToken:
          Pagination token. Set to null to start listing Apps from start. If non-null pagination token is returned in a result, then pass its value in here to list more projects.
        :type maxResults: integer
        :param maxResults:
          Maximum number of records to list in a single response.
        :rtype: dict
        :returns:
        """
        pass

    def list_jobs(self, appId: str, branchName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        List Jobs for a branch, part of an Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_jobs(
              appId='string',
              branchName='string',
              nextToken='string',
              maxResults=123
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries. 
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for a branch.
        :type nextToken: string
        :param nextToken:
          Pagination token. Set to null to start listing steps from start. If a non-null pagination token is returned in a result, then pass its value in here to list more steps.
        :type maxResults: integer
        :param maxResults:
          Maximum number of records to list in a single response.
        :rtype: dict
        :returns:
        """
        pass

    def start_job(self, appId: str, branchName: str, jobType: str, jobId: str = None, jobReason: str = None, commitId: str = None, commitMessage: str = None, commitTime: datetime = None) -> Dict:
        """
        Starts a new job for a branch, part of an Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/StartJob>`_
        
        **Request Syntax**
        ::
          response = client.start_job(
              appId='string',
              branchName='string',
              jobId='string',
              jobType='RELEASE'|'RETRY'|'WEB_HOOK',
              jobReason='string',
              commitId='string',
              commitMessage='string',
              commitTime=datetime(2015, 1, 1)
          )
        
        **Response Syntax**
        ::
            {
                'jobSummary': {
                    'jobArn': 'string',
                    'jobId': 'string',
                    'commitId': 'string',
                    'commitMessage': 'string',
                    'commitTime': datetime(2015, 1, 1),
                    'startTime': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                    'endTime': datetime(2015, 1, 1),
                    'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for run job request. 
            - **jobSummary** *(dict) --* 
              Summary for the Job. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for the branch, for the Job.
        :type jobId: string
        :param jobId:
          Unique Id for the Job.
        :type jobType: string
        :param jobType: **[REQUIRED]**
          Type for the Job.
        :type jobReason: string
        :param jobReason:
          Reason for the Job.
        :type commitId: string
        :param commitId:
          Commit Id from 3rd party repository provider for the Job.
        :type commitMessage: string
        :param commitMessage:
          Commit message from 3rd party repository provider for the Job.
        :type commitTime: datetime
        :param commitTime:
          Commit date / time for the Job.
        :rtype: dict
        :returns:
        """
        pass

    def stop_job(self, appId: str, branchName: str, jobId: str) -> Dict:
        """
        Stop a job that is in progress, for an Amplify branch, part of Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/StopJob>`_
        
        **Request Syntax**
        ::
          response = client.stop_job(
              appId='string',
              branchName='string',
              jobId='string'
          )
        
        **Response Syntax**
        ::
            {
                'jobSummary': {
                    'jobArn': 'string',
                    'jobId': 'string',
                    'commitId': 'string',
                    'commitMessage': 'string',
                    'commitTime': datetime(2015, 1, 1),
                    'startTime': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                    'endTime': datetime(2015, 1, 1),
                    'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for the stop job request. 
            - **jobSummary** *(dict) --* 
              Summary for the Job. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for the branch, for the Job.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          Unique Id for the Job.
        :rtype: dict
        :returns:
        """
        pass

    def update_app(self, appId: str, name: str = None, description: str = None, platform: str = None, iamServiceRoleArn: str = None, environmentVariables: Dict = None, enableBranchAutoBuild: bool = None, enableBasicAuth: bool = None, basicAuthCredentials: str = None, customRules: List = None, buildSpec: str = None) -> Dict:
        """
        Updates an existing Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/UpdateApp>`_
        
        **Request Syntax**
        ::
          response = client.update_app(
              appId='string',
              name='string',
              description='string',
              platform='IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
              iamServiceRoleArn='string',
              environmentVariables={
                  'string': 'string'
              },
              enableBranchAutoBuild=True|False,
              enableBasicAuth=True|False,
              basicAuthCredentials='string',
              customRules=[
                  {
                      'source': 'string',
                      'target': 'string',
                      'status': 'string',
                      'condition': 'string'
                  },
              ],
              buildSpec='string'
          )
        
        **Response Syntax**
        ::
            {
                'app': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for an Amplify App update request. 
            - **app** *(dict) --* 
              App structure for the updated App. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type name: string
        :param name:
          Name for an Amplify App.
        :type description: string
        :param description:
          Description for an Amplify App.
        :type platform: string
        :param platform:
          Platform for an Amplify App.
        :type iamServiceRoleArn: string
        :param iamServiceRoleArn:
          IAM service role for an Amplify App.
        :type environmentVariables: dict
        :param environmentVariables:
          Environment Variables for an Amplify App.
          - *(string) --*
            - *(string) --*
        :type enableBranchAutoBuild: boolean
        :param enableBranchAutoBuild:
          Enables branch auto-building for an Amplify App.
        :type enableBasicAuth: boolean
        :param enableBasicAuth:
          Enables Basic Authorization for an Amplify App.
        :type basicAuthCredentials: string
        :param basicAuthCredentials:
          Basic Authorization credentials for an Amplify App.
        :type customRules: list
        :param customRules:
          Custom redirect / rewrite rules for an Amplify App.
          - *(dict) --*
            Custom rewrite / redirect rule.
            - **source** *(string) --* **[REQUIRED]**
              The source pattern for a URL rewrite or redirect rule.
            - **target** *(string) --* **[REQUIRED]**
              The target pattern for a URL rewrite or redirect rule.
            - **status** *(string) --*
              The status code for a URL rewrite or redirect rule.
            - **condition** *(string) --*
              The condition for a URL rewrite or redirect rule, e.g. country code.
        :type buildSpec: string
        :param buildSpec:
          BuildSpec for an Amplify App.
        :rtype: dict
        :returns:
        """
        pass

    def update_branch(self, appId: str, branchName: str, description: str = None, framework: str = None, stage: str = None, enableNotification: bool = None, enableAutoBuild: bool = None, environmentVariables: Dict = None, basicAuthCredentials: str = None, enableBasicAuth: bool = None, buildSpec: str = None, ttl: str = None) -> Dict:
        """
        Updates a branch for an Amplify App. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/UpdateBranch>`_
        
        **Request Syntax**
        ::
          response = client.update_branch(
              appId='string',
              branchName='string',
              description='string',
              framework='string',
              stage='PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
              enableNotification=True|False,
              enableAutoBuild=True|False,
              environmentVariables={
                  'string': 'string'
              },
              basicAuthCredentials='string',
              enableBasicAuth=True|False,
              buildSpec='string',
              ttl='string'
          )
        
        **Response Syntax**
        ::
            {
                'branch': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for update branch request. 
            - **branch** *(dict) --* 
              Branch structure for an Amplify App. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type branchName: string
        :param branchName: **[REQUIRED]**
          Name for the branch.
        :type description: string
        :param description:
          Description for the branch.
        :type framework: string
        :param framework:
          Framework for the branch.
        :type stage: string
        :param stage:
          Stage for the branch.
        :type enableNotification: boolean
        :param enableNotification:
          Enables notifications for the branch.
        :type enableAutoBuild: boolean
        :param enableAutoBuild:
          Enables auto building for the branch.
        :type environmentVariables: dict
        :param environmentVariables:
          Environment Variables for the branch.
          - *(string) --*
            - *(string) --*
        :type basicAuthCredentials: string
        :param basicAuthCredentials:
          Basic Authorization credentials for the branch.
        :type enableBasicAuth: boolean
        :param enableBasicAuth:
          Enables Basic Auth for the branch.
        :type buildSpec: string
        :param buildSpec:
          BuildSpec for the branch.
        :type ttl: string
        :param ttl:
          The content TTL for the website in seconds.
        :rtype: dict
        :returns:
        """
        pass

    def update_domain_association(self, appId: str, domainName: str, subDomainSettings: List, enableAutoSubDomain: bool = None) -> Dict:
        """
        Create a new DomainAssociation on an App 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/UpdateDomainAssociation>`_
        
        **Request Syntax**
        ::
          response = client.update_domain_association(
              appId='string',
              domainName='string',
              enableAutoSubDomain=True|False,
              subDomainSettings=[
                  {
                      'prefix': 'string',
                      'branchName': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'domainAssociation': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Result structure for the update Domain Association request. 
            - **domainAssociation** *(dict) --* 
              Domain Association structure. 
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
        :type appId: string
        :param appId: **[REQUIRED]**
          Unique Id for an Amplify App.
        :type domainName: string
        :param domainName: **[REQUIRED]**
          Name of the domain.
        :type enableAutoSubDomain: boolean
        :param enableAutoSubDomain:
          Enables automated creation of Subdomains for branches.
        :type subDomainSettings: list
        :param subDomainSettings: **[REQUIRED]**
          Setting structure for the Subdomain.
          - *(dict) --*
            Setting for the Subdomain.
            - **prefix** *(string) --* **[REQUIRED]**
              Prefix setting for the Subdomain.
            - **branchName** *(string) --* **[REQUIRED]**
              Branch name setting for the Subdomain.
        :rtype: dict
        :returns:
        """
        pass
