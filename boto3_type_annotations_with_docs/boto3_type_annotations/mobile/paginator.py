from typing import Dict
from botocore.paginate import Paginator


class ListBundles(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/ListBundles>`_
        
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
                \'bundleList\': [
                    {
                        \'bundleId\': \'string\',
                        \'title\': \'string\',
                        \'version\': \'string\',
                        \'description\': \'string\',
                        \'iconUrl\': \'string\',
                        \'availablePlatforms\': [
                            \'OSX\'|\'WINDOWS\'|\'LINUX\'|\'OBJC\'|\'SWIFT\'|\'ANDROID\'|\'JAVASCRIPT\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Result structure contains a list of all available bundles with details. 
        
            - **bundleList** *(list) --* 
        
              A list of bundles. 
        
              - *(dict) --* 
        
                The details of the bundle. 
        
                - **bundleId** *(string) --* 
        
                  Unique bundle identifier. 
        
                - **title** *(string) --* 
        
                  Title of the download bundle. 
        
                - **version** *(string) --* 
        
                  Version of the download bundle. 
        
                - **description** *(string) --* 
        
                  Description of the download bundle. 
        
                - **iconUrl** *(string) --* 
        
                  Icon for the download bundle. 
        
                - **availablePlatforms** *(list) --* 
        
                  Developer desktop or mobile app or website platforms. 
        
                  - *(string) --* 
        
                    Developer desktop or target mobile app or website platform. 
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListProjects(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/ListProjects>`_
        
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
                \'projects\': [
                    {
                        \'name\': \'string\',
                        \'projectId\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Result structure used for requests to list projects in AWS Mobile Hub. 
        
            - **projects** *(list) --* 
        
              List of projects. 
        
              - *(dict) --* 
        
                Summary information about an AWS Mobile Hub project. 
        
                - **name** *(string) --* 
        
                  Name of the project. 
        
                - **projectId** *(string) --* 
        
                  Unique project identifier. 
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
