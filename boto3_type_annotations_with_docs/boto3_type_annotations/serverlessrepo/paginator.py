from typing import Dict
from botocore.paginate import Paginator


class ListApplicationDependencies(Paginator):
    def paginate(self, ApplicationId: str, SemanticVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServerlessApplicationRepository.Client.list_application_dependencies`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/ListApplicationDependencies>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ApplicationId='string',
              SemanticVersion='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Dependencies': [
                    {
                        'ApplicationId': 'string',
                        'SemanticVersion': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Dependencies** *(list) --* 
              An array of application summaries nested in the application.
              - *(dict) --* 
                A nested application summary.
                - **ApplicationId** *(string) --* 
                  The Amazon Resource Name (ARN) of the nested application.
                - **SemanticVersion** *(string) --* 
                  The semantic version of the nested application.
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the application.
        :type SemanticVersion: string
        :param SemanticVersion:
          The semantic version of the application to get.
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


class ListApplicationVersions(Paginator):
    def paginate(self, ApplicationId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServerlessApplicationRepository.Client.list_application_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/ListApplicationVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ApplicationId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'ApplicationId': 'string',
                        'CreationTime': 'string',
                        'SemanticVersion': 'string',
                        'SourceCodeUrl': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Versions** *(list) --* 
              An array of version summaries for the application.
              - *(dict) --* 
                An application version summary.
                - **ApplicationId** *(string) --* 
                  The application Amazon Resource Name (ARN).
                - **CreationTime** *(string) --* 
                  The date and time this resource was created.
                - **SemanticVersion** *(string) --* 
                  The semantic version of the application:
                   `https\://semver.org/ <https://semver.org/>`__  
                - **SourceCodeUrl** *(string) --* 
                  A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.
        :type ApplicationId: string
        :param ApplicationId: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the application.
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


class ListApplications(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServerlessApplicationRepository.Client.list_applications`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/ListApplications>`_
        
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
                'Applications': [
                    {
                        'ApplicationId': 'string',
                        'Author': 'string',
                        'CreationTime': 'string',
                        'Description': 'string',
                        'HomePageUrl': 'string',
                        'Labels': [
                            'string',
                        ],
                        'Name': 'string',
                        'SpdxLicenseId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Applications** *(list) --* 
              An array of application summaries.
              - *(dict) --* 
                Summary of details about the application.
                - **ApplicationId** *(string) --* 
                  The application Amazon Resource Name (ARN).
                - **Author** *(string) --* 
                  The name of the author publishing the app.
                  Minimum length=1. Maximum length=127.
                  Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
                - **CreationTime** *(string) --* 
                  The date and time this resource was created.
                - **Description** *(string) --* 
                  The description of the application.
                  Minimum length=1. Maximum length=256
                - **HomePageUrl** *(string) --* 
                  A URL with more information about the application, for example the location of your GitHub repository for the application.
                - **Labels** *(list) --* 
                  Labels to improve discovery of apps in search results.
                  Minimum length=1. Maximum length=127. Maximum number of labels: 10
                  Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";
                  - *(string) --* 
                - **Name** *(string) --* 
                  The name of the application.
                  Minimum length=1. Maximum length=140
                  Pattern: "[a-zA-Z0-9\\-]+";
                - **SpdxLicenseId** *(string) --* 
                  A valid identifier from `https\://spdx.org/licenses/ <https://spdx.org/licenses/>`__ .
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
