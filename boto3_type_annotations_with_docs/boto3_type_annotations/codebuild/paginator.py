from typing import Dict
from botocore.paginate import Paginator


class ListBuilds(Paginator):
    def paginate(self, sortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuilds>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              sortOrder=\'ASCENDING\'|\'DESCENDING\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type sortOrder: string
        :param sortOrder: 
        
          The order to list build IDs. Valid values include:
        
          * ``ASCENDING`` : List the build IDs in ascending order by build ID. 
           
          * ``DESCENDING`` : List the build IDs in descending order by build ID. 
           
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
                \'ids\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ids** *(list) --* 
        
              A list of build IDs, with each build ID representing a single build.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListBuildsForProject(Paginator):
    def paginate(self, projectName: str, sortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuildsForProject>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              projectName=\'string\',
              sortOrder=\'ASCENDING\'|\'DESCENDING\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the AWS CodeBuild project.
        
        :type sortOrder: string
        :param sortOrder: 
        
          The order to list build IDs. Valid values include:
        
          * ``ASCENDING`` : List the build IDs in ascending order by build ID. 
           
          * ``DESCENDING`` : List the build IDs in descending order by build ID. 
           
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
                \'ids\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ids** *(list) --* 
        
              A list of build IDs for the specified build project, with each build ID representing a single build.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListProjects(Paginator):
    def paginate(self, sortBy: str = None, sortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListProjects>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              sortBy=\'NAME\'|\'CREATED_TIME\'|\'LAST_MODIFIED_TIME\',
              sortOrder=\'ASCENDING\'|\'DESCENDING\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **projects** *(list) --* 
        
              The list of build project names, with each build project name representing a single build project.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
