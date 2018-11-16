from typing import Dict
from botocore.paginate import Paginator


class ListTopicsDetectionJobs(Paginator):
    def paginate(self, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListTopicsDetectionJobs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filter={
                  \'JobName\': \'string\',
                  \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                  \'SubmitTimeBefore\': datetime(2015, 1, 1),
                  \'SubmitTimeAfter\': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filter: dict
        :param Filter: 
        
          Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and time that they were submitted. You can set only one filter at a time.
        
          - **JobName** *(string) --* 
        
          - **JobStatus** *(string) --* 
        
            Filters the list of topic detection jobs based on job status. Returns only jobs with the specified status.
        
          - **SubmitTimeBefore** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.
        
          - **SubmitTimeAfter** *(datetime) --* 
        
            Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.
        
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
                \'TopicsDetectionJobPropertiesList\': [
                    {
                        \'JobId\': \'string\',
                        \'JobName\': \'string\',
                        \'JobStatus\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'COMPLETED\'|\'FAILED\'|\'STOP_REQUESTED\'|\'STOPPED\',
                        \'Message\': \'string\',
                        \'SubmitTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'InputDataConfig\': {
                            \'S3Uri\': \'string\',
                            \'InputFormat\': \'ONE_DOC_PER_FILE\'|\'ONE_DOC_PER_LINE\'
                        },
                        \'OutputDataConfig\': {
                            \'S3Uri\': \'string\'
                        },
                        \'NumberOfTopics\': 123
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TopicsDetectionJobPropertiesList** *(list) --* 
        
              A list containing the properties of each job that is returned.
        
              - *(dict) --* 
        
                Provides information about a topic detection job.
        
                - **JobId** *(string) --* 
        
                  The identifier assigned to the topic detection job.
        
                - **JobName** *(string) --* 
        
                  The name of the topic detection job.
        
                - **JobStatus** *(string) --* 
        
                  The current status of the topic detection job. If the status is ``Failed`` , the reason for the failure is shown in the ``Message`` field.
        
                - **Message** *(string) --* 
        
                  A description for the status of a job.
        
                - **SubmitTime** *(datetime) --* 
        
                  The time that the topic detection job was submitted for processing.
        
                - **EndTime** *(datetime) --* 
        
                  The time that the topic detection job was completed.
        
                - **InputDataConfig** *(dict) --* 
        
                  The input data configuration supplied when you created the topic detection job.
        
                  - **S3Uri** *(string) --* 
        
                    The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 
        
                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
        
                  - **InputFormat** *(string) --* 
        
                    Specifies how the text in an input file should be processed:
        
                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                     
                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                     
                - **OutputDataConfig** *(dict) --* 
        
                  The output data configuration supplied when you created the topic detection job.
        
                  - **S3Uri** *(string) --* 
        
                    When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
        
                    When the topic detection job is finished, the service creates an output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.
        
                - **NumberOfTopics** *(integer) --* 
        
                  The number of topics to detect supplied when you created the topic detection job. The default is 10. 
        
        """
        pass
