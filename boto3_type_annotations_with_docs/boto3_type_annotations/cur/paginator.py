from typing import Dict
from botocore.paginate import Paginator


class DescribeReportDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CostandUsageReportService.Client.describe_report_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/DescribeReportDefinitions>`_
        
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
                'ReportDefinitions': [
                    {
                        'ReportName': 'string',
                        'TimeUnit': 'HOURLY'|'DAILY',
                        'Format': 'textORcsv'|'Parquet',
                        'Compression': 'ZIP'|'GZIP'|'Parquet',
                        'AdditionalSchemaElements': [
                            'RESOURCES',
                        ],
                        'S3Bucket': 'string',
                        'S3Prefix': 'string',
                        'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'eu-north-1'|'ap-northeast-3',
                        'AdditionalArtifacts': [
                            'REDSHIFT'|'QUICKSIGHT'|'ATHENA',
                        ],
                        'RefreshClosedReports': True|False,
                        'ReportVersioning': 'CREATE_NEW_REPORT'|'OVERWRITE_REPORT'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            If the action is successful, the service sends back an HTTP 200 response.
            - **ReportDefinitions** *(list) --* 
              A list of AWS Cost and Usage reports owned by the account.
              - *(dict) --* 
                The definition of AWS Cost and Usage Report. You can specify the report name, time unit, report format, compression format, S3 bucket, additional artifacts, and schema elements in the definition. 
                - **ReportName** *(string) --* 
                  The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces. 
                - **TimeUnit** *(string) --* 
                  The length of time covered by the report. 
                - **Format** *(string) --* 
                  The format that AWS saves the report in.
                - **Compression** *(string) --* 
                  The compression format that AWS uses for the report.
                - **AdditionalSchemaElements** *(list) --* 
                  A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs. 
                  - *(string) --* 
                    Whether or not AWS includes resource IDs in the report. 
                - **S3Bucket** *(string) --* 
                  The S3 bucket where AWS delivers the report.
                - **S3Prefix** *(string) --* 
                  The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.
                - **S3Region** *(string) --* 
                  The region of the S3 bucket that AWS delivers the report into.
                - **AdditionalArtifacts** *(list) --* 
                  A list of manifests that you want Amazon Web Services to create for this report.
                  - *(string) --* 
                    The types of manifest that you want AWS to create for this report.
                - **RefreshClosedReports** *(boolean) --* 
                  Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.
                - **ReportVersioning** *(string) --* 
                  Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
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
