from typing import Dict
from botocore.paginate import Paginator


class ListJobs(Paginator):
    def paginate(self, APIVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/ListJobs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              APIVersion=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type APIVersion: string
        :param APIVersion: Specifies the version of the client tool.
        
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
                \'Jobs\': [
                    {
                        \'JobId\': \'string\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'IsCanceled\': True|False,
                        \'JobType\': \'Import\'|\'Export\'
                    },
                ],
                \'IsTruncated\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Output structure for the ListJobs operation.
            
            - **Jobs** *(list) --* A list container for Jobs returned by the ListJobs operation.
              
              - *(dict) --* Representation of a job returned by the ListJobs operation.
                
                - **JobId** *(string) --* A unique identifier which refers to a particular job.
                
                - **CreationDate** *(datetime) --* Timestamp of the CreateJob request in ISO8601 date format. For example \"2010-03-28T20:27:35Z\".
                
                - **IsCanceled** *(boolean) --* Indicates whether the job was canceled.
                
                - **JobType** *(string) --* Specifies whether the job to initiate is an import or export job.
            
            - **IsTruncated** *(boolean) --* Indicates whether the list of jobs was truncated. If true, then call ListJobs again using the last JobId element as the marker.
            
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
