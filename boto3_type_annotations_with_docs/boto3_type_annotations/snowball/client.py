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

    def cancel_cluster(self, ClusterId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/CancelCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_cluster(
              ClusterId=\'string\'
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The 39-character ID for the cluster that you want to cancel, for example ``CID123e4567-e89b-12d3-a456-426655440000`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def cancel_job(self, JobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/CancelJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The 39-character job ID for the job that you want to cancel, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def create_address(self, Address: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/CreateAddress>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_address(
              Address={
                  \'AddressId\': \'string\',
                  \'Name\': \'string\',
                  \'Company\': \'string\',
                  \'Street1\': \'string\',
                  \'Street2\': \'string\',
                  \'Street3\': \'string\',
                  \'City\': \'string\',
                  \'StateOrProvince\': \'string\',
                  \'PrefectureOrDistrict\': \'string\',
                  \'Landmark\': \'string\',
                  \'Country\': \'string\',
                  \'PostalCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'IsRestricted\': True|False
              }
          )
        :type Address: dict
        :param Address: **[REQUIRED]** 
        
          The address that you want the Snowball shipped to.
        
          - **AddressId** *(string) --* 
        
            The unique ID for an address.
        
          - **Name** *(string) --* 
        
            The name of a person to receive a Snowball at an address.
        
          - **Company** *(string) --* 
        
            The name of the company to receive a Snowball at an address.
        
          - **Street1** *(string) --* 
        
            The first line in a street address that a Snowball is to be delivered to.
        
          - **Street2** *(string) --* 
        
            The second line in a street address that a Snowball is to be delivered to.
        
          - **Street3** *(string) --* 
        
            The third line in a street address that a Snowball is to be delivered to.
        
          - **City** *(string) --* 
        
            The city in an address that a Snowball is to be delivered to.
        
          - **StateOrProvince** *(string) --* 
        
            The state or province in an address that a Snowball is to be delivered to.
        
          - **PrefectureOrDistrict** *(string) --* 
        
            This field is no longer used and the value is ignored.
        
          - **Landmark** *(string) --* 
        
            This field is no longer used and the value is ignored.
        
          - **Country** *(string) --* 
        
            The country in an address that a Snowball is to be delivered to.
        
          - **PostalCode** *(string) --* 
        
            The postal code in an address that a Snowball is to be delivered to.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number associated with an address that a Snowball is to be delivered to.
        
          - **IsRestricted** *(boolean) --* 
        
            If the address you are creating is a primary address, then set this option to true. This field is not supported in most regions.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AddressId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AddressId** *(string) --* 
        
              The automatically generated ID for a specific address. You\'ll use this ID when you create a job to specify which address you want the Snowball for that job shipped to.
        
        """
        pass

    def create_cluster(self, JobType: str, Resources: Dict, AddressId: str, RoleARN: str, ShippingOption: str, Description: str = None, KmsKeyARN: str = None, SnowballType: str = None, Notification: Dict = None, ForwardingAddressId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/CreateCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster(
              JobType=\'IMPORT\'|\'EXPORT\'|\'LOCAL_USE\',
              Resources={
                  \'S3Resources\': [
                      {
                          \'BucketArn\': \'string\',
                          \'KeyRange\': {
                              \'BeginMarker\': \'string\',
                              \'EndMarker\': \'string\'
                          }
                      },
                  ],
                  \'LambdaResources\': [
                      {
                          \'LambdaArn\': \'string\',
                          \'EventTriggers\': [
                              {
                                  \'EventResourceARN\': \'string\'
                              },
                          ]
                      },
                  ],
                  \'Ec2AmiResources\': [
                      {
                          \'AmiId\': \'string\',
                          \'SnowballAmiId\': \'string\'
                      },
                  ]
              },
              Description=\'string\',
              AddressId=\'string\',
              KmsKeyARN=\'string\',
              RoleARN=\'string\',
              SnowballType=\'STANDARD\'|\'EDGE\',
              ShippingOption=\'SECOND_DAY\'|\'NEXT_DAY\'|\'EXPRESS\'|\'STANDARD\',
              Notification={
                  \'SnsTopicARN\': \'string\',
                  \'JobStatesToNotify\': [
                      \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                  ],
                  \'NotifyAll\': True|False
              },
              ForwardingAddressId=\'string\'
          )
        :type JobType: string
        :param JobType: **[REQUIRED]** 
        
          The type of job for this cluster. Currently, the only job type supported for clusters is ``LOCAL_USE`` .
        
        :type Resources: dict
        :param Resources: **[REQUIRED]** 
        
          The resources associated with the cluster job. These resources include Amazon S3 buckets and optional AWS Lambda functions written in the Python language. 
        
          - **S3Resources** *(list) --* 
        
            An array of ``S3Resource`` objects.
        
            - *(dict) --* 
        
              Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional ``KeyRange`` value. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
              - **BucketArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of an Amazon S3 bucket.
        
              - **KeyRange** *(dict) --* 
        
                For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                - **BeginMarker** *(string) --* 
        
                  The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                - **EndMarker** *(string) --* 
        
                  The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
          - **LambdaResources** *(list) --* 
        
            The Python-language Lambda functions for this job.
        
            - *(dict) --* 
        
              Identifies 
        
              - **LambdaArn** *(string) --* 
        
                An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.
        
              - **EventTriggers** *(list) --* 
        
                The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.
        
                - *(dict) --* 
        
                  The container for the  EventTriggerDefinition$EventResourceARN .
        
                  - **EventResourceARN** *(string) --* 
        
                    The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.
        
          - **Ec2AmiResources** *(list) --* 
        
            The Amazon Machine Images (AMIs) associated with this job.
        
            - *(dict) --* 
        
              A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
        
              - **AmiId** *(string) --* **[REQUIRED]** 
        
                The ID of the AMI in Amazon EC2.
        
              - **SnowballAmiId** *(string) --* 
        
                The ID of the AMI on the Snowball Edge device.
        
        :type Description: string
        :param Description: 
        
          An optional description of this specific cluster, for example ``Environmental Data Cluster-01`` .
        
        :type AddressId: string
        :param AddressId: **[REQUIRED]** 
        
          The ID for the address that you want the cluster shipped to.
        
        :type KmsKeyARN: string
        :param KmsKeyARN: 
        
          The ``KmsKeyARN`` value that you want to associate with this cluster. ``KmsKeyARN`` values are created by using the `CreateKey <http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in AWS Key Management Service (AWS KMS). 
        
        :type RoleARN: string
        :param RoleARN: **[REQUIRED]** 
        
          The ``RoleARN`` that you want to associate with this cluster. ``RoleArn`` values are created by using the `CreateRole <http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in AWS Identity and Access Management (IAM).
        
        :type SnowballType: string
        :param SnowballType: 
        
          The type of AWS Snowball device to use for this cluster. Currently, the only supported device type for cluster jobs is ``EDGE`` .
        
        :type ShippingOption: string
        :param ShippingOption: **[REQUIRED]** 
        
          The shipping speed for each node in this cluster. This speed doesn\'t dictate how soon you\'ll get each Snowball Edge device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows:
        
          * In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day. 
           
          * In the European Union (EU), you have access to express shipping. Typically, Snowball Edges shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way. 
           
          * In India, Snowball Edges are delivered in one to seven days. 
           
          * In the US, you have access to one-day shipping and two-day shipping. 
           
        :type Notification: dict
        :param Notification: 
        
          The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.
        
          - **SnsTopicARN** *(string) --* 
        
            The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the `CreateTopic <http://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
        
            You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the `Subscribe <http://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple Notification Service (SNS) API action.
        
          - **JobStatesToNotify** *(list) --* 
        
            The list of job states that will trigger a notification for this job.
        
            - *(string) --* 
        
          - **NotifyAll** *(boolean) --* 
        
            Any change in job state will trigger a notification for this job.
        
        :type ForwardingAddressId: string
        :param ForwardingAddressId: 
        
          The forwarding address ID for a cluster. This field is not supported in most regions.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ClusterId** *(string) --* 
        
              The automatically generated ID for a cluster.
        
        """
        pass

    def create_job(self, JobType: str = None, Resources: Dict = None, Description: str = None, AddressId: str = None, KmsKeyARN: str = None, RoleARN: str = None, SnowballCapacityPreference: str = None, ShippingOption: str = None, Notification: Dict = None, ClusterId: str = None, SnowballType: str = None, ForwardingAddressId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/CreateJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_job(
              JobType=\'IMPORT\'|\'EXPORT\'|\'LOCAL_USE\',
              Resources={
                  \'S3Resources\': [
                      {
                          \'BucketArn\': \'string\',
                          \'KeyRange\': {
                              \'BeginMarker\': \'string\',
                              \'EndMarker\': \'string\'
                          }
                      },
                  ],
                  \'LambdaResources\': [
                      {
                          \'LambdaArn\': \'string\',
                          \'EventTriggers\': [
                              {
                                  \'EventResourceARN\': \'string\'
                              },
                          ]
                      },
                  ],
                  \'Ec2AmiResources\': [
                      {
                          \'AmiId\': \'string\',
                          \'SnowballAmiId\': \'string\'
                      },
                  ]
              },
              Description=\'string\',
              AddressId=\'string\',
              KmsKeyARN=\'string\',
              RoleARN=\'string\',
              SnowballCapacityPreference=\'T50\'|\'T80\'|\'T100\'|\'NoPreference\',
              ShippingOption=\'SECOND_DAY\'|\'NEXT_DAY\'|\'EXPRESS\'|\'STANDARD\',
              Notification={
                  \'SnsTopicARN\': \'string\',
                  \'JobStatesToNotify\': [
                      \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                  ],
                  \'NotifyAll\': True|False
              },
              ClusterId=\'string\',
              SnowballType=\'STANDARD\'|\'EDGE\',
              ForwardingAddressId=\'string\'
          )
        :type JobType: string
        :param JobType: 
        
          Defines the type of job that you\'re creating. 
        
        :type Resources: dict
        :param Resources: 
        
          Defines the Amazon S3 buckets associated with this job.
        
          With ``IMPORT`` jobs, you specify the bucket or buckets that your transferred data will be imported into.
        
          With ``EXPORT`` jobs, you specify the bucket or buckets that your transferred data will be exported from. Optionally, you can also specify a ``KeyRange`` value. If you choose to export a range, you define the length of the range by providing either an inclusive ``BeginMarker`` value, an inclusive ``EndMarker`` value, or both. Ranges are UTF-8 binary sorted.
        
          - **S3Resources** *(list) --* 
        
            An array of ``S3Resource`` objects.
        
            - *(dict) --* 
        
              Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional ``KeyRange`` value. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
              - **BucketArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of an Amazon S3 bucket.
        
              - **KeyRange** *(dict) --* 
        
                For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                - **BeginMarker** *(string) --* 
        
                  The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                - **EndMarker** *(string) --* 
        
                  The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
          - **LambdaResources** *(list) --* 
        
            The Python-language Lambda functions for this job.
        
            - *(dict) --* 
        
              Identifies 
        
              - **LambdaArn** *(string) --* 
        
                An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.
        
              - **EventTriggers** *(list) --* 
        
                The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.
        
                - *(dict) --* 
        
                  The container for the  EventTriggerDefinition$EventResourceARN .
        
                  - **EventResourceARN** *(string) --* 
        
                    The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.
        
          - **Ec2AmiResources** *(list) --* 
        
            The Amazon Machine Images (AMIs) associated with this job.
        
            - *(dict) --* 
        
              A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
        
              - **AmiId** *(string) --* **[REQUIRED]** 
        
                The ID of the AMI in Amazon EC2.
        
              - **SnowballAmiId** *(string) --* 
        
                The ID of the AMI on the Snowball Edge device.
        
        :type Description: string
        :param Description: 
        
          Defines an optional description of this specific job, for example ``Important Photos 2016-08-11`` .
        
        :type AddressId: string
        :param AddressId: 
        
          The ID for the address that you want the Snowball shipped to.
        
        :type KmsKeyARN: string
        :param KmsKeyARN: 
        
          The ``KmsKeyARN`` that you want to associate with this job. ``KmsKeyARN`` s are created using the `CreateKey <http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ AWS Key Management Service (KMS) API action.
        
        :type RoleARN: string
        :param RoleARN: 
        
          The ``RoleARN`` that you want to associate with this job. ``RoleArn`` s are created using the `CreateRole <http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ AWS Identity and Access Management (IAM) API action.
        
        :type SnowballCapacityPreference: string
        :param SnowballCapacityPreference: 
        
          If your job is being created in one of the US regions, you have the option of specifying what size Snowball you\'d like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.
        
        :type ShippingOption: string
        :param ShippingOption: 
        
          The shipping speed for this job. This speed doesn\'t dictate how soon you\'ll get the Snowball, rather it represents how quickly the Snowball moves to its destination while in transit. Regional shipping speeds are as follows:
        
          * In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. 
           
          * In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way. 
           
          * In India, Snowballs are delivered in one to seven days. 
           
          * In the US, you have access to one-day shipping and two-day shipping. 
           
        :type Notification: dict
        :param Notification: 
        
          Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.
        
          - **SnsTopicARN** *(string) --* 
        
            The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the `CreateTopic <http://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
        
            You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the `Subscribe <http://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple Notification Service (SNS) API action.
        
          - **JobStatesToNotify** *(list) --* 
        
            The list of job states that will trigger a notification for this job.
        
            - *(string) --* 
        
          - **NotifyAll** *(boolean) --* 
        
            Any change in job state will trigger a notification for this job.
        
        :type ClusterId: string
        :param ClusterId: 
        
          The ID of a cluster. If you\'re creating a job for a node in a cluster, you need to provide only this ``clusterId`` value. The other job attributes are inherited from the cluster.
        
        :type SnowballType: string
        :param SnowballType: 
        
          The type of AWS Snowball device to use for this job. Currently, the only supported device type for cluster jobs is ``EDGE`` .
        
        :type ForwardingAddressId: string
        :param ForwardingAddressId: 
        
          The forwarding address ID for a job. This field is not supported in most regions.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobId** *(string) --* 
        
              The automatically generated ID for a job, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
        """
        pass

    def describe_address(self, AddressId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/DescribeAddress>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_address(
              AddressId=\'string\'
          )
        :type AddressId: string
        :param AddressId: **[REQUIRED]** 
        
          The automatically generated ID for a specific address.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Address\': {
                    \'AddressId\': \'string\',
                    \'Name\': \'string\',
                    \'Company\': \'string\',
                    \'Street1\': \'string\',
                    \'Street2\': \'string\',
                    \'Street3\': \'string\',
                    \'City\': \'string\',
                    \'StateOrProvince\': \'string\',
                    \'PrefectureOrDistrict\': \'string\',
                    \'Landmark\': \'string\',
                    \'Country\': \'string\',
                    \'PostalCode\': \'string\',
                    \'PhoneNumber\': \'string\',
                    \'IsRestricted\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Address** *(dict) --* 
        
              The address that you want the Snowball or Snowballs associated with a specific job to be shipped to.
        
              - **AddressId** *(string) --* 
        
                The unique ID for an address.
        
              - **Name** *(string) --* 
        
                The name of a person to receive a Snowball at an address.
        
              - **Company** *(string) --* 
        
                The name of the company to receive a Snowball at an address.
        
              - **Street1** *(string) --* 
        
                The first line in a street address that a Snowball is to be delivered to.
        
              - **Street2** *(string) --* 
        
                The second line in a street address that a Snowball is to be delivered to.
        
              - **Street3** *(string) --* 
        
                The third line in a street address that a Snowball is to be delivered to.
        
              - **City** *(string) --* 
        
                The city in an address that a Snowball is to be delivered to.
        
              - **StateOrProvince** *(string) --* 
        
                The state or province in an address that a Snowball is to be delivered to.
        
              - **PrefectureOrDistrict** *(string) --* 
        
                This field is no longer used and the value is ignored.
        
              - **Landmark** *(string) --* 
        
                This field is no longer used and the value is ignored.
        
              - **Country** *(string) --* 
        
                The country in an address that a Snowball is to be delivered to.
        
              - **PostalCode** *(string) --* 
        
                The postal code in an address that a Snowball is to be delivered to.
        
              - **PhoneNumber** *(string) --* 
        
                The phone number associated with an address that a Snowball is to be delivered to.
        
              - **IsRestricted** *(boolean) --* 
        
                If the address you are creating is a primary address, then set this option to true. This field is not supported in most regions.
        
        """
        pass

    def describe_addresses(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_addresses(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          The number of ``ADDRESS`` objects to return.
        
        :type NextToken: string
        :param NextToken: 
        
          HTTP requests are stateless. To identify what object comes \"next\" in the list of ``ADDRESS`` objects, you have the option of specifying a value for ``NextToken`` as the starting point for your list of returned addresses.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Addresses\': [
                    {
                        \'AddressId\': \'string\',
                        \'Name\': \'string\',
                        \'Company\': \'string\',
                        \'Street1\': \'string\',
                        \'Street2\': \'string\',
                        \'Street3\': \'string\',
                        \'City\': \'string\',
                        \'StateOrProvince\': \'string\',
                        \'PrefectureOrDistrict\': \'string\',
                        \'Landmark\': \'string\',
                        \'Country\': \'string\',
                        \'PostalCode\': \'string\',
                        \'PhoneNumber\': \'string\',
                        \'IsRestricted\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Addresses** *(list) --* 
        
              The Snowball shipping addresses that were created for this account.
        
              - *(dict) --* 
        
                The address that you want the Snowball or Snowballs associated with a specific job to be shipped to. Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. Although no individual elements of the ``Address`` are required, if the address is invalid or unsupported, then an exception is thrown.
        
                - **AddressId** *(string) --* 
        
                  The unique ID for an address.
        
                - **Name** *(string) --* 
        
                  The name of a person to receive a Snowball at an address.
        
                - **Company** *(string) --* 
        
                  The name of the company to receive a Snowball at an address.
        
                - **Street1** *(string) --* 
        
                  The first line in a street address that a Snowball is to be delivered to.
        
                - **Street2** *(string) --* 
        
                  The second line in a street address that a Snowball is to be delivered to.
        
                - **Street3** *(string) --* 
        
                  The third line in a street address that a Snowball is to be delivered to.
        
                - **City** *(string) --* 
        
                  The city in an address that a Snowball is to be delivered to.
        
                - **StateOrProvince** *(string) --* 
        
                  The state or province in an address that a Snowball is to be delivered to.
        
                - **PrefectureOrDistrict** *(string) --* 
        
                  This field is no longer used and the value is ignored.
        
                - **Landmark** *(string) --* 
        
                  This field is no longer used and the value is ignored.
        
                - **Country** *(string) --* 
        
                  The country in an address that a Snowball is to be delivered to.
        
                - **PostalCode** *(string) --* 
        
                  The postal code in an address that a Snowball is to be delivered to.
        
                - **PhoneNumber** *(string) --* 
        
                  The phone number associated with an address that a Snowball is to be delivered to.
        
                - **IsRestricted** *(boolean) --* 
        
                  If the address you are creating is a primary address, then set this option to true. This field is not supported in most regions.
        
            - **NextToken** *(string) --* 
        
              HTTP requests are stateless. If you use the automatically generated ``NextToken`` value in your next ``DescribeAddresses`` call, your list of returned addresses will start from this point in the array.
        
        """
        pass

    def describe_cluster(self, ClusterId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/DescribeCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster(
              ClusterId=\'string\'
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The automatically generated ID for a cluster.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterMetadata\': {
                    \'ClusterId\': \'string\',
                    \'Description\': \'string\',
                    \'KmsKeyARN\': \'string\',
                    \'RoleARN\': \'string\',
                    \'ClusterState\': \'AwaitingQuorum\'|\'Pending\'|\'InUse\'|\'Complete\'|\'Cancelled\',
                    \'JobType\': \'IMPORT\'|\'EXPORT\'|\'LOCAL_USE\',
                    \'SnowballType\': \'STANDARD\'|\'EDGE\',
                    \'CreationDate\': datetime(2015, 1, 1),
                    \'Resources\': {
                        \'S3Resources\': [
                            {
                                \'BucketArn\': \'string\',
                                \'KeyRange\': {
                                    \'BeginMarker\': \'string\',
                                    \'EndMarker\': \'string\'
                                }
                            },
                        ],
                        \'LambdaResources\': [
                            {
                                \'LambdaArn\': \'string\',
                                \'EventTriggers\': [
                                    {
                                        \'EventResourceARN\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'Ec2AmiResources\': [
                            {
                                \'AmiId\': \'string\',
                                \'SnowballAmiId\': \'string\'
                            },
                        ]
                    },
                    \'AddressId\': \'string\',
                    \'ShippingOption\': \'SECOND_DAY\'|\'NEXT_DAY\'|\'EXPRESS\'|\'STANDARD\',
                    \'Notification\': {
                        \'SnsTopicARN\': \'string\',
                        \'JobStatesToNotify\': [
                            \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                        ],
                        \'NotifyAll\': True|False
                    },
                    \'ForwardingAddressId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ClusterMetadata** *(dict) --* 
        
              Information about a specific cluster, including shipping information, cluster status, and other important metadata.
        
              - **ClusterId** *(string) --* 
        
                The automatically generated ID for a cluster.
        
              - **Description** *(string) --* 
        
                The optional description of the cluster.
        
              - **KmsKeyARN** *(string) --* 
        
                The ``KmsKeyARN`` Amazon Resource Name (ARN) associated with this cluster. This ARN was created using the `CreateKey <http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in AWS Key Management Service (AWS KMS).
        
              - **RoleARN** *(string) --* 
        
                The role ARN associated with this cluster. This ARN was created using the `CreateRole <http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in AWS Identity and Access Management (IAM).
        
              - **ClusterState** *(string) --* 
        
                The current status of the cluster.
        
              - **JobType** *(string) --* 
        
                The type of job for this cluster. Currently, the only job type supported for clusters is ``LOCAL_USE`` .
        
              - **SnowballType** *(string) --* 
        
                The type of AWS Snowball device to use for this cluster. Currently, the only supported device type for cluster jobs is ``EDGE`` .
        
              - **CreationDate** *(datetime) --* 
        
                The creation date for this cluster.
        
              - **Resources** *(dict) --* 
        
                The arrays of  JobResource objects that can include updated  S3Resource objects or  LambdaResource objects.
        
                - **S3Resources** *(list) --* 
        
                  An array of ``S3Resource`` objects.
        
                  - *(dict) --* 
        
                    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional ``KeyRange`` value. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                    - **BucketArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of an Amazon S3 bucket.
        
                    - **KeyRange** *(dict) --* 
        
                      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                      - **BeginMarker** *(string) --* 
        
                        The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                      - **EndMarker** *(string) --* 
        
                        The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                - **LambdaResources** *(list) --* 
        
                  The Python-language Lambda functions for this job.
        
                  - *(dict) --* 
        
                    Identifies 
        
                    - **LambdaArn** *(string) --* 
        
                      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.
        
                    - **EventTriggers** *(list) --* 
        
                      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.
        
                      - *(dict) --* 
        
                        The container for the  EventTriggerDefinition$EventResourceARN .
        
                        - **EventResourceARN** *(string) --* 
        
                          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.
        
                - **Ec2AmiResources** *(list) --* 
        
                  The Amazon Machine Images (AMIs) associated with this job.
        
                  - *(dict) --* 
        
                    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
        
                    - **AmiId** *(string) --* 
        
                      The ID of the AMI in Amazon EC2.
        
                    - **SnowballAmiId** *(string) --* 
        
                      The ID of the AMI on the Snowball Edge device.
        
              - **AddressId** *(string) --* 
        
                The automatically generated ID for a specific address.
        
              - **ShippingOption** *(string) --* 
        
                The shipping speed for each node in this cluster. This speed doesn\'t dictate how soon you\'ll get each Snowball Edge device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows:
        
                * In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day. 
                 
                * In the European Union (EU), you have access to express shipping. Typically, Snowball Edges shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way. 
                 
                * In India, Snowball Edges are delivered in one to seven days. 
                 
                * In the US, you have access to one-day shipping and two-day shipping. 
                 
              - **Notification** *(dict) --* 
        
                The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.
        
                - **SnsTopicARN** *(string) --* 
        
                  The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the `CreateTopic <http://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
        
                  You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the `Subscribe <http://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple Notification Service (SNS) API action.
        
                - **JobStatesToNotify** *(list) --* 
        
                  The list of job states that will trigger a notification for this job.
        
                  - *(string) --* 
              
                - **NotifyAll** *(boolean) --* 
        
                  Any change in job state will trigger a notification for this job.
        
              - **ForwardingAddressId** *(string) --* 
        
                The ID of the address that you want a cluster shipped to, after it will be shipped to its primary address. This field is not supported in most regions.
        
        """
        pass

    def describe_job(self, JobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/DescribeJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_job(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The automatically generated ID for a job, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobMetadata\': {
                    \'JobId\': \'string\',
                    \'JobState\': \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                    \'JobType\': \'IMPORT\'|\'EXPORT\'|\'LOCAL_USE\',
                    \'SnowballType\': \'STANDARD\'|\'EDGE\',
                    \'CreationDate\': datetime(2015, 1, 1),
                    \'Resources\': {
                        \'S3Resources\': [
                            {
                                \'BucketArn\': \'string\',
                                \'KeyRange\': {
                                    \'BeginMarker\': \'string\',
                                    \'EndMarker\': \'string\'
                                }
                            },
                        ],
                        \'LambdaResources\': [
                            {
                                \'LambdaArn\': \'string\',
                                \'EventTriggers\': [
                                    {
                                        \'EventResourceARN\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'Ec2AmiResources\': [
                            {
                                \'AmiId\': \'string\',
                                \'SnowballAmiId\': \'string\'
                            },
                        ]
                    },
                    \'Description\': \'string\',
                    \'KmsKeyARN\': \'string\',
                    \'RoleARN\': \'string\',
                    \'AddressId\': \'string\',
                    \'ShippingDetails\': {
                        \'ShippingOption\': \'SECOND_DAY\'|\'NEXT_DAY\'|\'EXPRESS\'|\'STANDARD\',
                        \'InboundShipment\': {
                            \'Status\': \'string\',
                            \'TrackingNumber\': \'string\'
                        },
                        \'OutboundShipment\': {
                            \'Status\': \'string\',
                            \'TrackingNumber\': \'string\'
                        }
                    },
                    \'SnowballCapacityPreference\': \'T50\'|\'T80\'|\'T100\'|\'NoPreference\',
                    \'Notification\': {
                        \'SnsTopicARN\': \'string\',
                        \'JobStatesToNotify\': [
                            \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                        ],
                        \'NotifyAll\': True|False
                    },
                    \'DataTransferProgress\': {
                        \'BytesTransferred\': 123,
                        \'ObjectsTransferred\': 123,
                        \'TotalBytes\': 123,
                        \'TotalObjects\': 123
                    },
                    \'JobLogInfo\': {
                        \'JobCompletionReportURI\': \'string\',
                        \'JobSuccessLogURI\': \'string\',
                        \'JobFailureLogURI\': \'string\'
                    },
                    \'ClusterId\': \'string\',
                    \'ForwardingAddressId\': \'string\'
                },
                \'SubJobMetadata\': [
                    {
                        \'JobId\': \'string\',
                        \'JobState\': \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                        \'JobType\': \'IMPORT\'|\'EXPORT\'|\'LOCAL_USE\',
                        \'SnowballType\': \'STANDARD\'|\'EDGE\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'Resources\': {
                            \'S3Resources\': [
                                {
                                    \'BucketArn\': \'string\',
                                    \'KeyRange\': {
                                        \'BeginMarker\': \'string\',
                                        \'EndMarker\': \'string\'
                                    }
                                },
                            ],
                            \'LambdaResources\': [
                                {
                                    \'LambdaArn\': \'string\',
                                    \'EventTriggers\': [
                                        {
                                            \'EventResourceARN\': \'string\'
                                        },
                                    ]
                                },
                            ],
                            \'Ec2AmiResources\': [
                                {
                                    \'AmiId\': \'string\',
                                    \'SnowballAmiId\': \'string\'
                                },
                            ]
                        },
                        \'Description\': \'string\',
                        \'KmsKeyARN\': \'string\',
                        \'RoleARN\': \'string\',
                        \'AddressId\': \'string\',
                        \'ShippingDetails\': {
                            \'ShippingOption\': \'SECOND_DAY\'|\'NEXT_DAY\'|\'EXPRESS\'|\'STANDARD\',
                            \'InboundShipment\': {
                                \'Status\': \'string\',
                                \'TrackingNumber\': \'string\'
                            },
                            \'OutboundShipment\': {
                                \'Status\': \'string\',
                                \'TrackingNumber\': \'string\'
                            }
                        },
                        \'SnowballCapacityPreference\': \'T50\'|\'T80\'|\'T100\'|\'NoPreference\',
                        \'Notification\': {
                            \'SnsTopicARN\': \'string\',
                            \'JobStatesToNotify\': [
                                \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                            ],
                            \'NotifyAll\': True|False
                        },
                        \'DataTransferProgress\': {
                            \'BytesTransferred\': 123,
                            \'ObjectsTransferred\': 123,
                            \'TotalBytes\': 123,
                            \'TotalObjects\': 123
                        },
                        \'JobLogInfo\': {
                            \'JobCompletionReportURI\': \'string\',
                            \'JobSuccessLogURI\': \'string\',
                            \'JobFailureLogURI\': \'string\'
                        },
                        \'ClusterId\': \'string\',
                        \'ForwardingAddressId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobMetadata** *(dict) --* 
        
              Information about a specific job, including shipping information, job status, and other important metadata.
        
              - **JobId** *(string) --* 
        
                The automatically generated ID for a job, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
              - **JobState** *(string) --* 
        
                The current status of the jobs.
        
              - **JobType** *(string) --* 
        
                The type of job.
        
              - **SnowballType** *(string) --* 
        
                The type of device used with this job.
        
              - **CreationDate** *(datetime) --* 
        
                The creation date for this job.
        
              - **Resources** *(dict) --* 
        
                An array of ``S3Resource`` objects. Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into.
        
                - **S3Resources** *(list) --* 
        
                  An array of ``S3Resource`` objects.
        
                  - *(dict) --* 
        
                    Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional ``KeyRange`` value. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                    - **BucketArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of an Amazon S3 bucket.
        
                    - **KeyRange** *(dict) --* 
        
                      For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                      - **BeginMarker** *(string) --* 
        
                        The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                      - **EndMarker** *(string) --* 
        
                        The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                - **LambdaResources** *(list) --* 
        
                  The Python-language Lambda functions for this job.
        
                  - *(dict) --* 
        
                    Identifies 
        
                    - **LambdaArn** *(string) --* 
        
                      An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.
        
                    - **EventTriggers** *(list) --* 
        
                      The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.
        
                      - *(dict) --* 
        
                        The container for the  EventTriggerDefinition$EventResourceARN .
        
                        - **EventResourceARN** *(string) --* 
        
                          The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.
        
                - **Ec2AmiResources** *(list) --* 
        
                  The Amazon Machine Images (AMIs) associated with this job.
        
                  - *(dict) --* 
        
                    A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
        
                    - **AmiId** *(string) --* 
        
                      The ID of the AMI in Amazon EC2.
        
                    - **SnowballAmiId** *(string) --* 
        
                      The ID of the AMI on the Snowball Edge device.
        
              - **Description** *(string) --* 
        
                The description of the job, provided at job creation.
        
              - **KmsKeyARN** *(string) --* 
        
                The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated with this job. This ARN was created using the `CreateKey <http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in AWS KMS.
        
              - **RoleARN** *(string) --* 
        
                The role ARN associated with this job. This ARN was created using the `CreateRole <http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in AWS Identity and Access Management (IAM).
        
              - **AddressId** *(string) --* 
        
                The ID for the address that you want the Snowball shipped to.
        
              - **ShippingDetails** *(dict) --* 
        
                A job\'s shipping information, including inbound and outbound tracking numbers and shipping speed options.
        
                - **ShippingOption** *(string) --* 
        
                  The shipping speed for a particular job. This speed doesn\'t dictate how soon you\'ll get the Snowball from the job\'s creation date. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:
        
                  * In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. 
                   
                  * In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way. 
                   
                  * In India, Snowballs are delivered in one to seven days. 
                   
                  * In the United States of America (US), you have access to one-day shipping and two-day shipping. 
                   
                - **InboundShipment** *(dict) --* 
        
                  The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a particular job.
        
                  - **Status** *(string) --* 
        
                    Status information for a shipment.
        
                  - **TrackingNumber** *(string) --* 
        
                    The tracking number for this job. Using this tracking number with your region\'s carrier\'s website, you can track a Snowball as the carrier transports it.
        
                    For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
        
                - **OutboundShipment** *(dict) --* 
        
                  The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the address that you specified for a particular job.
        
                  - **Status** *(string) --* 
        
                    Status information for a shipment.
        
                  - **TrackingNumber** *(string) --* 
        
                    The tracking number for this job. Using this tracking number with your region\'s carrier\'s website, you can track a Snowball as the carrier transports it.
        
                    For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
        
              - **SnowballCapacityPreference** *(string) --* 
        
                The Snowball capacity preference for this job, specified at job creation. In US regions, you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity Snowballs.
        
              - **Notification** *(dict) --* 
        
                The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The ``Notification`` object is returned as a part of the response syntax of the ``DescribeJob`` action in the ``JobMetadata`` data type.
        
                - **SnsTopicARN** *(string) --* 
        
                  The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the `CreateTopic <http://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
        
                  You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the `Subscribe <http://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple Notification Service (SNS) API action.
        
                - **JobStatesToNotify** *(list) --* 
        
                  The list of job states that will trigger a notification for this job.
        
                  - *(string) --* 
              
                - **NotifyAll** *(boolean) --* 
        
                  Any change in job state will trigger a notification for this job.
        
              - **DataTransferProgress** *(dict) --* 
        
                A value that defines the real-time status of a Snowball\'s data transfer while the device is at AWS. This data is only available while a job has a ``JobState`` value of ``InProgress`` , for both import and export jobs.
        
                - **BytesTransferred** *(integer) --* 
        
                  The number of bytes transferred between a Snowball and Amazon S3.
        
                - **ObjectsTransferred** *(integer) --* 
        
                  The number of objects transferred between a Snowball and Amazon S3.
        
                - **TotalBytes** *(integer) --* 
        
                  The total bytes of data for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
        
                - **TotalObjects** *(integer) --* 
        
                  The total number of objects for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
        
              - **JobLogInfo** *(dict) --* 
        
                Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snowball for your job part is being delivered to you.
        
                - **JobCompletionReportURI** *(string) --* 
        
                  A link to an Amazon S3 presigned URL where the job completion report is located.
        
                - **JobSuccessLogURI** *(string) --* 
        
                  A link to an Amazon S3 presigned URL where the job success log is located.
        
                - **JobFailureLogURI** *(string) --* 
        
                  A link to an Amazon S3 presigned URL where the job failure log is located.
        
              - **ClusterId** *(string) --* 
        
                The 39-character ID for the cluster, for example ``CID123e4567-e89b-12d3-a456-426655440000`` .
        
              - **ForwardingAddressId** *(string) --* 
        
                The ID of the address that you want a job shipped to, after it will be shipped to its primary address. This field is not supported in most regions.
        
            - **SubJobMetadata** *(list) --* 
        
              Information about a specific job part (in the case of an export job), including shipping information, job status, and other important metadata.
        
              - *(dict) --* 
        
                Contains information about a specific job including shipping information, job status, and other important metadata. This information is returned as a part of the response syntax of the ``DescribeJob`` action.
        
                - **JobId** *(string) --* 
        
                  The automatically generated ID for a job, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
                - **JobState** *(string) --* 
        
                  The current status of the jobs.
        
                - **JobType** *(string) --* 
        
                  The type of job.
        
                - **SnowballType** *(string) --* 
        
                  The type of device used with this job.
        
                - **CreationDate** *(datetime) --* 
        
                  The creation date for this job.
        
                - **Resources** *(dict) --* 
        
                  An array of ``S3Resource`` objects. Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into.
        
                  - **S3Resources** *(list) --* 
        
                    An array of ``S3Resource`` objects.
        
                    - *(dict) --* 
        
                      Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional ``KeyRange`` value. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                      - **BucketArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of an Amazon S3 bucket.
        
                      - **KeyRange** *(dict) --* 
        
                        For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                        - **BeginMarker** *(string) --* 
        
                          The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                        - **EndMarker** *(string) --* 
        
                          The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                  - **LambdaResources** *(list) --* 
        
                    The Python-language Lambda functions for this job.
        
                    - *(dict) --* 
        
                      Identifies 
        
                      - **LambdaArn** *(string) --* 
        
                        An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.
        
                      - **EventTriggers** *(list) --* 
        
                        The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.
        
                        - *(dict) --* 
        
                          The container for the  EventTriggerDefinition$EventResourceARN .
        
                          - **EventResourceARN** *(string) --* 
        
                            The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.
        
                  - **Ec2AmiResources** *(list) --* 
        
                    The Amazon Machine Images (AMIs) associated with this job.
        
                    - *(dict) --* 
        
                      A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
        
                      - **AmiId** *(string) --* 
        
                        The ID of the AMI in Amazon EC2.
        
                      - **SnowballAmiId** *(string) --* 
        
                        The ID of the AMI on the Snowball Edge device.
        
                - **Description** *(string) --* 
        
                  The description of the job, provided at job creation.
        
                - **KmsKeyARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated with this job. This ARN was created using the `CreateKey <http://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html>`__ API action in AWS KMS.
        
                - **RoleARN** *(string) --* 
        
                  The role ARN associated with this job. This ARN was created using the `CreateRole <http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in AWS Identity and Access Management (IAM).
        
                - **AddressId** *(string) --* 
        
                  The ID for the address that you want the Snowball shipped to.
        
                - **ShippingDetails** *(dict) --* 
        
                  A job\'s shipping information, including inbound and outbound tracking numbers and shipping speed options.
        
                  - **ShippingOption** *(string) --* 
        
                    The shipping speed for a particular job. This speed doesn\'t dictate how soon you\'ll get the Snowball from the job\'s creation date. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:
        
                    * In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. 
                     
                    * In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way. 
                     
                    * In India, Snowballs are delivered in one to seven days. 
                     
                    * In the United States of America (US), you have access to one-day shipping and two-day shipping. 
                     
                  - **InboundShipment** *(dict) --* 
        
                    The ``Status`` and ``TrackingNumber`` values for a Snowball being returned to AWS for a particular job.
        
                    - **Status** *(string) --* 
        
                      Status information for a shipment.
        
                    - **TrackingNumber** *(string) --* 
        
                      The tracking number for this job. Using this tracking number with your region\'s carrier\'s website, you can track a Snowball as the carrier transports it.
        
                      For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
        
                  - **OutboundShipment** *(dict) --* 
        
                    The ``Status`` and ``TrackingNumber`` values for a Snowball being delivered to the address that you specified for a particular job.
        
                    - **Status** *(string) --* 
        
                      Status information for a shipment.
        
                    - **TrackingNumber** *(string) --* 
        
                      The tracking number for this job. Using this tracking number with your region\'s carrier\'s website, you can track a Snowball as the carrier transports it.
        
                      For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
        
                - **SnowballCapacityPreference** *(string) --* 
        
                  The Snowball capacity preference for this job, specified at job creation. In US regions, you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity Snowballs.
        
                - **Notification** *(dict) --* 
        
                  The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The ``Notification`` object is returned as a part of the response syntax of the ``DescribeJob`` action in the ``JobMetadata`` data type.
        
                  - **SnsTopicARN** *(string) --* 
        
                    The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the `CreateTopic <http://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
        
                    You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the `Subscribe <http://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple Notification Service (SNS) API action.
        
                  - **JobStatesToNotify** *(list) --* 
        
                    The list of job states that will trigger a notification for this job.
        
                    - *(string) --* 
                
                  - **NotifyAll** *(boolean) --* 
        
                    Any change in job state will trigger a notification for this job.
        
                - **DataTransferProgress** *(dict) --* 
        
                  A value that defines the real-time status of a Snowball\'s data transfer while the device is at AWS. This data is only available while a job has a ``JobState`` value of ``InProgress`` , for both import and export jobs.
        
                  - **BytesTransferred** *(integer) --* 
        
                    The number of bytes transferred between a Snowball and Amazon S3.
        
                  - **ObjectsTransferred** *(integer) --* 
        
                    The number of objects transferred between a Snowball and Amazon S3.
        
                  - **TotalBytes** *(integer) --* 
        
                    The total bytes of data for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
        
                  - **TotalObjects** *(integer) --* 
        
                    The total number of objects for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
        
                - **JobLogInfo** *(dict) --* 
        
                  Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snowball for your job part is being delivered to you.
        
                  - **JobCompletionReportURI** *(string) --* 
        
                    A link to an Amazon S3 presigned URL where the job completion report is located.
        
                  - **JobSuccessLogURI** *(string) --* 
        
                    A link to an Amazon S3 presigned URL where the job success log is located.
        
                  - **JobFailureLogURI** *(string) --* 
        
                    A link to an Amazon S3 presigned URL where the job failure log is located.
        
                - **ClusterId** *(string) --* 
        
                  The 39-character ID for the cluster, for example ``CID123e4567-e89b-12d3-a456-426655440000`` .
        
                - **ForwardingAddressId** *(string) --* 
        
                  The ID of the address that you want a job shipped to, after it will be shipped to its primary address. This field is not supported in most regions.
        
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

    def get_job_manifest(self, JobId: str) -> Dict:
        """
        
        The manifest is an encrypted file that you can download after your job enters the ``WithCustomer`` status. The manifest is decrypted by using the ``UnlockCode`` code value, when you pass both values to the Snowball through the Snowball client when the client is started for the first time.
        
        As a best practice, we recommend that you don\'t save a copy of an ``UnlockCode`` value in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snowball associated with that job.
        
        The credentials of a given job, including its manifest file and unlock code, expire 90 days after the job is created.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/GetJobManifest>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_job_manifest(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The ID for a job that you want to get the manifest file for, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ManifestURI\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ManifestURI** *(string) --* 
        
              The Amazon S3 presigned URL for the manifest file associated with the specified ``JobId`` value.
        
        """
        pass

    def get_job_unlock_code(self, JobId: str) -> Dict:
        """
        
        The ``UnlockCode`` value is a 29-character code with 25 alphanumeric characters and 4 hyphens. This code is used to decrypt the manifest file when it is passed along with the manifest to the Snowball through the Snowball client when the client is started for the first time.
        
        As a best practice, we recommend that you don\'t save a copy of the ``UnlockCode`` in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snowball associated with that job.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/GetJobUnlockCode>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_job_unlock_code(
              JobId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The ID for the job that you want to get the ``UnlockCode`` value for, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnlockCode\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UnlockCode** *(string) --* 
        
              The ``UnlockCode`` value for the specified job. The ``UnlockCode`` value can be accessed for up to 90 days after the job has been created.
        
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

    def get_snowball_usage(self) -> Dict:
        """
        
        The default service limit for the number of Snowballs that you can have at one time is 1. If you want to increase your service limit, contact AWS Support.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/GetSnowballUsage>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_snowball_usage()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SnowballLimit\': 123,
                \'SnowballsInUse\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SnowballLimit** *(integer) --* 
        
              The service limit for number of Snowballs this account can have at once. The default service limit is 1 (one).
        
            - **SnowballsInUse** *(integer) --* 
        
              The number of Snowballs that this account is currently using.
        
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

    def list_cluster_jobs(self, ClusterId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/ListClusterJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_cluster_jobs(
              ClusterId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The 39-character ID for the cluster that you want to list, for example ``CID123e4567-e89b-12d3-a456-426655440000`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The number of ``JobListEntry`` objects to return.
        
        :type NextToken: string
        :param NextToken: 
        
          HTTP requests are stateless. To identify what object comes \"next\" in the list of ``JobListEntry`` objects, you have the option of specifying ``NextToken`` as the starting point for your returned list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobListEntries\': [
                    {
                        \'JobId\': \'string\',
                        \'JobState\': \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                        \'IsMaster\': True|False,
                        \'JobType\': \'IMPORT\'|\'EXPORT\'|\'LOCAL_USE\',
                        \'SnowballType\': \'STANDARD\'|\'EDGE\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobListEntries** *(list) --* 
        
              Each ``JobListEntry`` object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of export jobs. 
        
              - *(dict) --* 
        
                Each ``JobListEntry`` object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of an export job.
        
                - **JobId** *(string) --* 
        
                  The automatically generated ID for a job, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
                - **JobState** *(string) --* 
        
                  The current state of this job.
        
                - **IsMaster** *(boolean) --* 
        
                  A value that indicates that this job is a master job. A master job represents a successful request to create an export job. Master jobs aren\'t associated with any Snowballs. Instead, each master job will have at least one job part, and each job part is associated with a Snowball. It might take some time before the job parts associated with a particular master job are listed, because they are created after the master job is created.
        
                - **JobType** *(string) --* 
        
                  The type of job.
        
                - **SnowballType** *(string) --* 
        
                  The type of device used with this job.
        
                - **CreationDate** *(datetime) --* 
        
                  The creation date for this job.
        
                - **Description** *(string) --* 
        
                  The optional description of this specific job, for example ``Important Photos 2016-08-11`` .
        
            - **NextToken** *(string) --* 
        
              HTTP requests are stateless. If you use the automatically generated ``NextToken`` value in your next ``ListClusterJobsResult`` call, your list of returned jobs will start from this point in the array.
        
        """
        pass

    def list_clusters(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/ListClusters>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_clusters(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          The number of ``ClusterListEntry`` objects to return.
        
        :type NextToken: string
        :param NextToken: 
        
          HTTP requests are stateless. To identify what object comes \"next\" in the list of ``ClusterListEntry`` objects, you have the option of specifying ``NextToken`` as the starting point for your returned list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterListEntries\': [
                    {
                        \'ClusterId\': \'string\',
                        \'ClusterState\': \'AwaitingQuorum\'|\'Pending\'|\'InUse\'|\'Complete\'|\'Cancelled\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ClusterListEntries** *(list) --* 
        
              Each ``ClusterListEntry`` object contains a cluster\'s state, a cluster\'s ID, and other important status information.
        
              - *(dict) --* 
        
                Contains a cluster\'s state, a cluster\'s ID, and other important information.
        
                - **ClusterId** *(string) --* 
        
                  The 39-character ID for the cluster that you want to list, for example ``CID123e4567-e89b-12d3-a456-426655440000`` .
        
                - **ClusterState** *(string) --* 
        
                  The current state of this cluster. For information about the state of a specific node, see  JobListEntry$JobState .
        
                - **CreationDate** *(datetime) --* 
        
                  The creation date for this cluster.
        
                - **Description** *(string) --* 
        
                  Defines an optional description of the cluster, for example ``Environmental Data Cluster-01`` .
        
            - **NextToken** *(string) --* 
        
              HTTP requests are stateless. If you use the automatically generated ``NextToken`` value in your next ``ClusterListEntry`` call, your list of returned clusters will start from this point in the array.
        
        """
        pass

    def list_compatible_images(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/ListCompatibleImages>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_compatible_images(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results for the list of compatible images. Currently, a Snowball Edge device can store 10 AMIs.
        
        :type NextToken: string
        :param NextToken: 
        
          HTTP requests are stateless. To identify what object comes \"next\" in the list of compatible images, you can specify a value for ``NextToken`` as the starting point for your list of returned images.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CompatibleImages\': [
                    {
                        \'AmiId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CompatibleImages** *(list) --* 
        
              A JSON-formatted object that describes a compatible AMI, including the ID and name for a Snowball Edge AMI.
        
              - *(dict) --* 
        
                A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including the ID and name for a Snowball Edge AMI. This AMI is compatible with the device\'s physical hardware requirements, and it should be able to be run in an SBE1 instance on the device.
        
                - **AmiId** *(string) --* 
        
                  The unique identifier for an individual Snowball Edge AMI.
        
                - **Name** *(string) --* 
        
                  The optional name of a compatible image.
        
            - **NextToken** *(string) --* 
        
              Because HTTP requests are stateless, this is the starting point for your next list of returned images.
        
        """
        pass

    def list_jobs(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/ListJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_jobs(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          The number of ``JobListEntry`` objects to return.
        
        :type NextToken: string
        :param NextToken: 
        
          HTTP requests are stateless. To identify what object comes \"next\" in the list of ``JobListEntry`` objects, you have the option of specifying ``NextToken`` as the starting point for your returned list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobListEntries\': [
                    {
                        \'JobId\': \'string\',
                        \'JobState\': \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                        \'IsMaster\': True|False,
                        \'JobType\': \'IMPORT\'|\'EXPORT\'|\'LOCAL_USE\',
                        \'SnowballType\': \'STANDARD\'|\'EDGE\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobListEntries** *(list) --* 
        
              Each ``JobListEntry`` object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of export jobs. 
        
              - *(dict) --* 
        
                Each ``JobListEntry`` object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of an export job.
        
                - **JobId** *(string) --* 
        
                  The automatically generated ID for a job, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
                - **JobState** *(string) --* 
        
                  The current state of this job.
        
                - **IsMaster** *(boolean) --* 
        
                  A value that indicates that this job is a master job. A master job represents a successful request to create an export job. Master jobs aren\'t associated with any Snowballs. Instead, each master job will have at least one job part, and each job part is associated with a Snowball. It might take some time before the job parts associated with a particular master job are listed, because they are created after the master job is created.
        
                - **JobType** *(string) --* 
        
                  The type of job.
        
                - **SnowballType** *(string) --* 
        
                  The type of device used with this job.
        
                - **CreationDate** *(datetime) --* 
        
                  The creation date for this job.
        
                - **Description** *(string) --* 
        
                  The optional description of this specific job, for example ``Important Photos 2016-08-11`` .
        
            - **NextToken** *(string) --* 
        
              HTTP requests are stateless. If you use this automatically generated ``NextToken`` value in your next ``ListJobs`` call, your returned ``JobListEntry`` objects will start from this point in the array.
        
        """
        pass

    def update_cluster(self, ClusterId: str, RoleARN: str = None, Description: str = None, Resources: Dict = None, AddressId: str = None, ShippingOption: str = None, Notification: Dict = None, ForwardingAddressId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/UpdateCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_cluster(
              ClusterId=\'string\',
              RoleARN=\'string\',
              Description=\'string\',
              Resources={
                  \'S3Resources\': [
                      {
                          \'BucketArn\': \'string\',
                          \'KeyRange\': {
                              \'BeginMarker\': \'string\',
                              \'EndMarker\': \'string\'
                          }
                      },
                  ],
                  \'LambdaResources\': [
                      {
                          \'LambdaArn\': \'string\',
                          \'EventTriggers\': [
                              {
                                  \'EventResourceARN\': \'string\'
                              },
                          ]
                      },
                  ],
                  \'Ec2AmiResources\': [
                      {
                          \'AmiId\': \'string\',
                          \'SnowballAmiId\': \'string\'
                      },
                  ]
              },
              AddressId=\'string\',
              ShippingOption=\'SECOND_DAY\'|\'NEXT_DAY\'|\'EXPRESS\'|\'STANDARD\',
              Notification={
                  \'SnsTopicARN\': \'string\',
                  \'JobStatesToNotify\': [
                      \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                  ],
                  \'NotifyAll\': True|False
              },
              ForwardingAddressId=\'string\'
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The cluster ID of the cluster that you want to update, for example ``CID123e4567-e89b-12d3-a456-426655440000`` .
        
        :type RoleARN: string
        :param RoleARN: 
        
          The new role Amazon Resource Name (ARN) that you want to associate with this cluster. To create a role ARN, use the `CreateRole <http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ API action in AWS Identity and Access Management (IAM).
        
        :type Description: string
        :param Description: 
        
          The updated description of this cluster.
        
        :type Resources: dict
        :param Resources: 
        
          The updated arrays of  JobResource objects that can include updated  S3Resource objects or  LambdaResource objects.
        
          - **S3Resources** *(list) --* 
        
            An array of ``S3Resource`` objects.
        
            - *(dict) --* 
        
              Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional ``KeyRange`` value. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
              - **BucketArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of an Amazon S3 bucket.
        
              - **KeyRange** *(dict) --* 
        
                For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                - **BeginMarker** *(string) --* 
        
                  The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                - **EndMarker** *(string) --* 
        
                  The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
          - **LambdaResources** *(list) --* 
        
            The Python-language Lambda functions for this job.
        
            - *(dict) --* 
        
              Identifies 
        
              - **LambdaArn** *(string) --* 
        
                An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.
        
              - **EventTriggers** *(list) --* 
        
                The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.
        
                - *(dict) --* 
        
                  The container for the  EventTriggerDefinition$EventResourceARN .
        
                  - **EventResourceARN** *(string) --* 
        
                    The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.
        
          - **Ec2AmiResources** *(list) --* 
        
            The Amazon Machine Images (AMIs) associated with this job.
        
            - *(dict) --* 
        
              A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
        
              - **AmiId** *(string) --* **[REQUIRED]** 
        
                The ID of the AMI in Amazon EC2.
        
              - **SnowballAmiId** *(string) --* 
        
                The ID of the AMI on the Snowball Edge device.
        
        :type AddressId: string
        :param AddressId: 
        
          The ID of the updated  Address object.
        
        :type ShippingOption: string
        :param ShippingOption: 
        
          The updated shipping option value of this cluster\'s  ShippingDetails object.
        
        :type Notification: dict
        :param Notification: 
        
          The new or updated  Notification object.
        
          - **SnsTopicARN** *(string) --* 
        
            The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the `CreateTopic <http://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
        
            You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the `Subscribe <http://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple Notification Service (SNS) API action.
        
          - **JobStatesToNotify** *(list) --* 
        
            The list of job states that will trigger a notification for this job.
        
            - *(string) --* 
        
          - **NotifyAll** *(boolean) --* 
        
            Any change in job state will trigger a notification for this job.
        
        :type ForwardingAddressId: string
        :param ForwardingAddressId: 
        
          The updated ID for the forwarding address for a cluster. This field is not supported in most regions.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_job(self, JobId: str, RoleARN: str = None, Notification: Dict = None, Resources: Dict = None, AddressId: str = None, ShippingOption: str = None, Description: str = None, SnowballCapacityPreference: str = None, ForwardingAddressId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/UpdateJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_job(
              JobId=\'string\',
              RoleARN=\'string\',
              Notification={
                  \'SnsTopicARN\': \'string\',
                  \'JobStatesToNotify\': [
                      \'New\'|\'PreparingAppliance\'|\'PreparingShipment\'|\'InTransitToCustomer\'|\'WithCustomer\'|\'InTransitToAWS\'|\'WithAWSSortingFacility\'|\'WithAWS\'|\'InProgress\'|\'Complete\'|\'Cancelled\'|\'Listing\'|\'Pending\',
                  ],
                  \'NotifyAll\': True|False
              },
              Resources={
                  \'S3Resources\': [
                      {
                          \'BucketArn\': \'string\',
                          \'KeyRange\': {
                              \'BeginMarker\': \'string\',
                              \'EndMarker\': \'string\'
                          }
                      },
                  ],
                  \'LambdaResources\': [
                      {
                          \'LambdaArn\': \'string\',
                          \'EventTriggers\': [
                              {
                                  \'EventResourceARN\': \'string\'
                              },
                          ]
                      },
                  ],
                  \'Ec2AmiResources\': [
                      {
                          \'AmiId\': \'string\',
                          \'SnowballAmiId\': \'string\'
                      },
                  ]
              },
              AddressId=\'string\',
              ShippingOption=\'SECOND_DAY\'|\'NEXT_DAY\'|\'EXPRESS\'|\'STANDARD\',
              Description=\'string\',
              SnowballCapacityPreference=\'T50\'|\'T80\'|\'T100\'|\'NoPreference\',
              ForwardingAddressId=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** 
        
          The job ID of the job that you want to update, for example ``JID123e4567-e89b-12d3-a456-426655440000`` .
        
        :type RoleARN: string
        :param RoleARN: 
        
          The new role Amazon Resource Name (ARN) that you want to associate with this job. To create a role ARN, use the `CreateRole <http://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`__ AWS Identity and Access Management (IAM) API action.
        
        :type Notification: dict
        :param Notification: 
        
          The new or updated  Notification object.
        
          - **SnsTopicARN** *(string) --* 
        
            The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the `CreateTopic <http://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
        
            You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the `Subscribe <http://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__ AWS Simple Notification Service (SNS) API action.
        
          - **JobStatesToNotify** *(list) --* 
        
            The list of job states that will trigger a notification for this job.
        
            - *(string) --* 
        
          - **NotifyAll** *(boolean) --* 
        
            Any change in job state will trigger a notification for this job.
        
        :type Resources: dict
        :param Resources: 
        
          The updated ``JobResource`` object, or the updated  JobResource object. 
        
          - **S3Resources** *(list) --* 
        
            An array of ``S3Resource`` objects.
        
            - *(dict) --* 
        
              Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional ``KeyRange`` value. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
              - **BucketArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of an Amazon S3 bucket.
        
              - **KeyRange** *(dict) --* 
        
                For export jobs, you can provide an optional ``KeyRange`` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
        
                - **BeginMarker** *(string) --* 
        
                  The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
                - **EndMarker** *(string) --* 
        
                  The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
        
          - **LambdaResources** *(list) --* 
        
            The Python-language Lambda functions for this job.
        
            - *(dict) --* 
        
              Identifies 
        
              - **LambdaArn** *(string) --* 
        
                An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.
        
              - **EventTriggers** *(list) --* 
        
                The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.
        
                - *(dict) --* 
        
                  The container for the  EventTriggerDefinition$EventResourceARN .
        
                  - **EventResourceARN** *(string) --* 
        
                    The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.
        
          - **Ec2AmiResources** *(list) --* 
        
            The Amazon Machine Images (AMIs) associated with this job.
        
            - *(dict) --* 
        
              A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.
        
              - **AmiId** *(string) --* **[REQUIRED]** 
        
                The ID of the AMI in Amazon EC2.
        
              - **SnowballAmiId** *(string) --* 
        
                The ID of the AMI on the Snowball Edge device.
        
        :type AddressId: string
        :param AddressId: 
        
          The ID of the updated  Address object.
        
        :type ShippingOption: string
        :param ShippingOption: 
        
          The updated shipping option value of this job\'s  ShippingDetails object.
        
        :type Description: string
        :param Description: 
        
          The updated description of this job\'s  JobMetadata object.
        
        :type SnowballCapacityPreference: string
        :param SnowballCapacityPreference: 
        
          The updated ``SnowballCapacityPreference`` of this job\'s  JobMetadata object. The 50 TB Snowballs are only available in the US regions.
        
        :type ForwardingAddressId: string
        :param ForwardingAddressId: 
        
          The updated ID for the forwarding address for a job. This field is not supported in most regions.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
