from typing import Dict
from botocore.paginate import Paginator


class DescribeReportDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/DescribeReportDefinitions>`_
        
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
                \'ReportDefinitions\': [
                    {
                        \'ReportName\': \'string\',
                        \'TimeUnit\': \'HOURLY\'|\'DAILY\',
                        \'Format\': \'textORcsv\',
                        \'Compression\': \'ZIP\'|\'GZIP\',
                        \'AdditionalSchemaElements\': [
                            \'RESOURCES\',
                        ],
                        \'S3Bucket\': \'string\',
                        \'S3Prefix\': \'string\',
                        \'S3Region\': \'us-east-1\'|\'us-west-1\'|\'us-west-2\'|\'eu-central-1\'|\'eu-west-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\',
                        \'AdditionalArtifacts\': [
                            \'REDSHIFT\'|\'QUICKSIGHT\',
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* Response of DescribeReportDefinitions
            
            - **ReportDefinitions** *(list) --* A list of report definitions.
              
              - *(dict) --* The definition of AWS Cost and Usage Report. Customer can specify the report name, time unit, report format, compression format, S3 bucket and additional artifacts and schema elements in the definition.
                
                - **ReportName** *(string) --* Preferred name for a report, it has to be unique. Must starts with a number/letter, case sensitive. Limited to 256 characters.
                
                - **TimeUnit** *(string) --* The frequency on which report data are measured and displayed.
                
                - **Format** *(string) --* Preferred format for report.
                
                - **Compression** *(string) --* Preferred compression format for report.
                
                - **AdditionalSchemaElements** *(list) --* A list of schema elements.
                  
                  - *(string) --* Preference of including Resource IDs. You can include additional details about individual resource IDs in your report.
              
                - **S3Bucket** *(string) --* Name of customer S3 bucket.
                
                - **S3Prefix** *(string) --* Preferred report path prefix. Limited to 256 characters.
                
                - **S3Region** *(string) --* Region of customer S3 bucket.
                
                - **AdditionalArtifacts** *(list) --* A list of additional artifacts.
                  
                  - *(string) --* Enable support for Redshift and/or QuickSight.
              
        """
        pass
