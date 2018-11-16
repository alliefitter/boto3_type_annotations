from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        """
        
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

    def generate_data_set(self, dataSetType: str, dataSetPublicationDate: datetime, roleNameArn: str, destinationS3BucketName: str, snsTopicArn: str, destinationS3Prefix: str = None, customerDefinedValues: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/marketplacecommerceanalytics-2015-07-01/GenerateDataSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.generate_data_set(
              dataSetType=\'customer_subscriber_hourly_monthly_subscriptions\'|\'customer_subscriber_annual_subscriptions\'|\'daily_business_usage_by_instance_type\'|\'daily_business_fees\'|\'daily_business_free_trial_conversions\'|\'daily_business_new_instances\'|\'daily_business_new_product_subscribers\'|\'daily_business_canceled_product_subscribers\'|\'monthly_revenue_billing_and_revenue_data\'|\'monthly_revenue_annual_subscriptions\'|\'disbursed_amount_by_product\'|\'disbursed_amount_by_product_with_uncollected_funds\'|\'disbursed_amount_by_instance_hours\'|\'disbursed_amount_by_customer_geo\'|\'disbursed_amount_by_age_of_uncollected_funds\'|\'disbursed_amount_by_age_of_disbursed_funds\'|\'customer_profile_by_industry\'|\'customer_profile_by_revenue\'|\'customer_profile_by_geography\'|\'sales_compensation_billed_revenue\'|\'us_sales_and_use_tax_records\',
              dataSetPublicationDate=datetime(2015, 1, 1),
              roleNameArn=\'string\',
              destinationS3BucketName=\'string\',
              destinationS3Prefix=\'string\',
              snsTopicArn=\'string\',
              customerDefinedValues={
                  \'string\': \'string\'
              }
          )
        :type dataSetType: string
        :param dataSetType: **[REQUIRED]** 
        
          The desired data set type.
        
          * customer_subscriber_hourly_monthly_subscriptions From 2014-07-21 to present: Available daily by 5:00 PM Pacific Time. 
           
          * customer_subscriber_annual_subscriptions From 2014-07-21 to present: Available daily by 5:00 PM Pacific Time. 
           
          * daily_business_usage_by_instance_type From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time. 
           
          * daily_business_fees From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time. 
           
          * daily_business_free_trial_conversions From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time. 
           
          * daily_business_new_instances From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time. 
           
          * daily_business_new_product_subscribers From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time. 
           
          * daily_business_canceled_product_subscribers From 2015-01-26 to present: Available daily by 5:00 PM Pacific Time. 
           
          * monthly_revenue_billing_and_revenue_data From 2015-02 to 2017-06: Available monthly on the 4th day of the month by 5:00pm Pacific Time. Data includes metered transactions (e.g. hourly) from two months prior. From 2017-07 to present: Available monthly on the 15th day of the month by 5:00pm Pacific Time. Data includes metered transactions (e.g. hourly) from one month prior. 
           
          * monthly_revenue_annual_subscriptions From 2015-02 to 2017-06: Available monthly on the 4th day of the month by 5:00pm Pacific Time. Data includes up-front software charges (e.g. annual) from one month prior. From 2017-07 to present: Available monthly on the 15th day of the month by 5:00pm Pacific Time. Data includes up-front software charges (e.g. annual) from one month prior. 
           
          * disbursed_amount_by_product From 2015-01-26 to present: Available every 30 days by 5:00 PM Pacific Time. 
           
          * disbursed_amount_by_product_with_uncollected_funds From 2012-04-19 to 2015-01-25: Available every 30 days by 5:00 PM Pacific Time. From 2015-01-26 to present: This data set was split into three data sets: disbursed_amount_by_product, disbursed_amount_by_age_of_uncollected_funds, and disbursed_amount_by_age_of_disbursed_funds. 
           
          * disbursed_amount_by_instance_hours From 2012-09-04 to present: Available every 30 days by 5:00 PM Pacific Time. 
           
          * disbursed_amount_by_customer_geo From 2012-04-19 to present: Available every 30 days by 5:00 PM Pacific Time. 
           
          * disbursed_amount_by_age_of_uncollected_funds From 2015-01-26 to present: Available every 30 days by 5:00 PM Pacific Time. 
           
          * disbursed_amount_by_age_of_disbursed_funds From 2015-01-26 to present: Available every 30 days by 5:00 PM Pacific Time. 
           
          * customer_profile_by_industry From 2015-10-01 to 2017-06-29: Available daily by 5:00 PM Pacific Time. From 2017-06-30 to present: This data set is no longer available. 
           
          * customer_profile_by_revenue From 2015-10-01 to 2017-06-29: Available daily by 5:00 PM Pacific Time. From 2017-06-30 to present: This data set is no longer available. 
           
          * customer_profile_by_geography From 2015-10-01 to 2017-06-29: Available daily by 5:00 PM Pacific Time. From 2017-06-30 to present: This data set is no longer available. 
           
          * sales_compensation_billed_revenue From 2016-12 to 2017-06: Available monthly on the 4th day of the month by 5:00pm Pacific Time. Data includes metered transactions (e.g. hourly) from two months prior, and up-front software charges (e.g. annual) from one month prior. From 2017-06 to present: Available monthly on the 15th day of the month by 5:00pm Pacific Time. Data includes metered transactions (e.g. hourly) from one month prior, and up-front software charges (e.g. annual) from one month prior. 
           
          * us_sales_and_use_tax_records From 2017-02-15 to present: Available monthly on the 15th day of the month by 5:00 PM Pacific Time. 
           
        :type dataSetPublicationDate: datetime
        :param dataSetPublicationDate: **[REQUIRED]** The date a data set was published. For daily data sets, provide a date with day-level granularity for the desired day. For weekly data sets, provide a date with day-level granularity within the desired week (the day value will be ignored). For monthly data sets, provide a date with month-level granularity for the desired month (the day value will be ignored).
        
        :type roleNameArn: string
        :param roleNameArn: **[REQUIRED]** The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services.
        
        :type destinationS3BucketName: string
        :param destinationS3BucketName: **[REQUIRED]** The name (friendly name, not ARN) of the destination S3 bucket.
        
        :type destinationS3Prefix: string
        :param destinationS3Prefix: (Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name \"mybucket\" and the prefix \"myprefix/mydatasets\", the output file \"outputfile\" would be published to \"s3://mybucket/myprefix/mydatasets/outputfile\". If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root.
        
        :type snsTopicArn: string
        :param snsTopicArn: **[REQUIRED]** Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred.
        
        :type customerDefinedValues: dict
        :param customerDefinedValues: (Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file. These key-value pairs can be used to correlated responses with tracking information from other systems.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'dataSetRequestId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Container for the result of the GenerateDataSet operation.
            
            - **dataSetRequestId** *(string) --* A unique identifier representing a specific request to the GenerateDataSet operation. This identifier can be used to correlate a request with notifications from the SNS topic.
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        """
        
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

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        
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
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def start_support_data_export(self, dataSetType: str, fromDate: datetime, roleNameArn: str, destinationS3BucketName: str, snsTopicArn: str, destinationS3Prefix: str = None, customerDefinedValues: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/marketplacecommerceanalytics-2015-07-01/StartSupportDataExport>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_support_data_export(
              dataSetType=\'customer_support_contacts_data\'|\'test_customer_support_contacts_data\',
              fromDate=datetime(2015, 1, 1),
              roleNameArn=\'string\',
              destinationS3BucketName=\'string\',
              destinationS3Prefix=\'string\',
              snsTopicArn=\'string\',
              customerDefinedValues={
                  \'string\': \'string\'
              }
          )
        :type dataSetType: string
        :param dataSetType: **[REQUIRED]** 
        
          Specifies the data set type to be written to the output csv file. The data set types customer_support_contacts_data and test_customer_support_contacts_data both result in a csv file containing the following fields: Product Id, Product Code, Customer Guid, Subscription Guid, Subscription Start Date, Organization, AWS Account Id, Given Name, Surname, Telephone Number, Email, Title, Country Code, ZIP Code, Operation Type, and Operation Time. 
        
          * *customer_support_contacts_data* Customer support contact data. The data set will contain all changes (Creates, Updates, and Deletes) to customer support contact data from the date specified in the from_date parameter.
           
          * *test_customer_support_contacts_data* An example data set containing static test data in the same format as customer_support_contacts_data
           
        :type fromDate: datetime
        :param fromDate: **[REQUIRED]** The start date from which to retrieve the data set in UTC. This parameter only affects the customer_support_contacts_data data set type.
        
        :type roleNameArn: string
        :param roleNameArn: **[REQUIRED]** The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services.
        
        :type destinationS3BucketName: string
        :param destinationS3BucketName: **[REQUIRED]** The name (friendly name, not ARN) of the destination S3 bucket.
        
        :type destinationS3Prefix: string
        :param destinationS3Prefix: (Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name \"mybucket\" and the prefix \"myprefix/mydatasets\", the output file \"outputfile\" would be published to \"s3://mybucket/myprefix/mydatasets/outputfile\". If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root.
        
        :type snsTopicArn: string
        :param snsTopicArn: **[REQUIRED]** Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred.
        
        :type customerDefinedValues: dict
        :param customerDefinedValues: (Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'dataSetRequestId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Container for the result of the StartSupportDataExport operation.
            
            - **dataSetRequestId** *(string) --* A unique identifier representing a specific request to the StartSupportDataExport operation. This identifier can be used to correlate a request with notifications from the SNS topic.
        """
        pass
