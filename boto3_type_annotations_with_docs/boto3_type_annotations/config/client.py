from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def batch_get_aggregate_resource_config(self, ConfigurationAggregatorName: str, ResourceIdentifiers: List) -> Dict:
        """
        Returns the current configuration items for resources that are present in your AWS Config aggregator. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty ``unprocessedResourceIdentifiers`` list. 
        .. note::
          * The API does not return results for deleted resources. 
          * The API does not return tags and relationships. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/BatchGetAggregateResourceConfig>`_
        
        **Request Syntax**
        ::
          response = client.batch_get_aggregate_resource_config(
              ConfigurationAggregatorName='string',
              ResourceIdentifiers=[
                  {
                      'SourceAccountId': 'string',
                      'SourceRegion': 'string',
                      'ResourceId': 'string',
                      'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                      'ResourceName': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'BaseConfigurationItems': [
                    {
                        'version': 'string',
                        'accountId': 'string',
                        'configurationItemCaptureTime': datetime(2015, 1, 1),
                        'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
                        'configurationStateId': 'string',
                        'arn': 'string',
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'resourceId': 'string',
                        'resourceName': 'string',
                        'awsRegion': 'string',
                        'availabilityZone': 'string',
                        'resourceCreationTime': datetime(2015, 1, 1),
                        'configuration': 'string',
                        'supplementaryConfiguration': {
                            'string': 'string'
                        }
                    },
                ],
                'UnprocessedResourceIdentifiers': [
                    {
                        'SourceAccountId': 'string',
                        'SourceRegion': 'string',
                        'ResourceId': 'string',
                        'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'ResourceName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BaseConfigurationItems** *(list) --* 
              A list that contains the current configuration of one or more resources.
              - *(dict) --* 
                The detailed configuration of a specified resource.
                - **version** *(string) --* 
                  The version number of the resource configuration.
                - **accountId** *(string) --* 
                  The 12-digit AWS account ID associated with the resource.
                - **configurationItemCaptureTime** *(datetime) --* 
                  The time when the configuration recording was initiated.
                - **configurationItemStatus** *(string) --* 
                  The configuration item status.
                - **configurationStateId** *(string) --* 
                  An identifier that indicates the ordering of the configuration items of a resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the resource.
                - **resourceType** *(string) --* 
                  The type of AWS resource.
                - **resourceId** *(string) --* 
                  The ID of the resource (for example., sg-xxxxxx).
                - **resourceName** *(string) --* 
                  The custom name of the resource, if available.
                - **awsRegion** *(string) --* 
                  The region where the resource resides.
                - **availabilityZone** *(string) --* 
                  The Availability Zone associated with the resource.
                - **resourceCreationTime** *(datetime) --* 
                  The time stamp when the resource was created.
                - **configuration** *(string) --* 
                  The description of the resource configuration.
                - **supplementaryConfiguration** *(dict) --* 
                  Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the configuration parameter.
                  - *(string) --* 
                    - *(string) --* 
            - **UnprocessedResourceIdentifiers** *(list) --* 
              A list of resource identifiers that were not processed with current scope. The list is empty if all the resources are processed.
              - *(dict) --* 
                The details that identify a resource that is collected by AWS Config aggregator, including the resource type, ID, (if available) the custom resource name, the source account, and source region.
                - **SourceAccountId** *(string) --* 
                  The 12-digit account ID of the source account.
                - **SourceRegion** *(string) --* 
                  The source region where data is aggregated.
                - **ResourceId** *(string) --* 
                  The ID of the AWS resource.
                - **ResourceType** *(string) --* 
                  The type of the AWS resource.
                - **ResourceName** *(string) --* 
                  The name of the AWS resource.
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type ResourceIdentifiers: list
        :param ResourceIdentifiers: **[REQUIRED]**
          A list of aggregate ResourceIdentifiers objects.
          - *(dict) --*
            The details that identify a resource that is collected by AWS Config aggregator, including the resource type, ID, (if available) the custom resource name, the source account, and source region.
            - **SourceAccountId** *(string) --* **[REQUIRED]**
              The 12-digit account ID of the source account.
            - **SourceRegion** *(string) --* **[REQUIRED]**
              The source region where data is aggregated.
            - **ResourceId** *(string) --* **[REQUIRED]**
              The ID of the AWS resource.
            - **ResourceType** *(string) --* **[REQUIRED]**
              The type of the AWS resource.
            - **ResourceName** *(string) --*
              The name of the AWS resource.
        :rtype: dict
        :returns:
        """
        pass

    def batch_get_resource_config(self, resourceKeys: List) -> Dict:
        """
        Returns the current configuration for one or more requested resources. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty unprocessedResourceKeys list. 
        .. note::
          * The API does not return results for deleted resources. 
          * The API does not return any tags for the requested resources. This information is filtered out of the supplementaryConfiguration section of the API response. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/BatchGetResourceConfig>`_
        
        **Request Syntax**
        ::
          response = client.batch_get_resource_config(
              resourceKeys=[
                  {
                      'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                      'resourceId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'baseConfigurationItems': [
                    {
                        'version': 'string',
                        'accountId': 'string',
                        'configurationItemCaptureTime': datetime(2015, 1, 1),
                        'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
                        'configurationStateId': 'string',
                        'arn': 'string',
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'resourceId': 'string',
                        'resourceName': 'string',
                        'awsRegion': 'string',
                        'availabilityZone': 'string',
                        'resourceCreationTime': datetime(2015, 1, 1),
                        'configuration': 'string',
                        'supplementaryConfiguration': {
                            'string': 'string'
                        }
                    },
                ],
                'unprocessedResourceKeys': [
                    {
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'resourceId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **baseConfigurationItems** *(list) --* 
              A list that contains the current configuration of one or more resources.
              - *(dict) --* 
                The detailed configuration of a specified resource.
                - **version** *(string) --* 
                  The version number of the resource configuration.
                - **accountId** *(string) --* 
                  The 12-digit AWS account ID associated with the resource.
                - **configurationItemCaptureTime** *(datetime) --* 
                  The time when the configuration recording was initiated.
                - **configurationItemStatus** *(string) --* 
                  The configuration item status.
                - **configurationStateId** *(string) --* 
                  An identifier that indicates the ordering of the configuration items of a resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the resource.
                - **resourceType** *(string) --* 
                  The type of AWS resource.
                - **resourceId** *(string) --* 
                  The ID of the resource (for example., sg-xxxxxx).
                - **resourceName** *(string) --* 
                  The custom name of the resource, if available.
                - **awsRegion** *(string) --* 
                  The region where the resource resides.
                - **availabilityZone** *(string) --* 
                  The Availability Zone associated with the resource.
                - **resourceCreationTime** *(datetime) --* 
                  The time stamp when the resource was created.
                - **configuration** *(string) --* 
                  The description of the resource configuration.
                - **supplementaryConfiguration** *(dict) --* 
                  Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the configuration parameter.
                  - *(string) --* 
                    - *(string) --* 
            - **unprocessedResourceKeys** *(list) --* 
              A list of resource keys that were not processed with the current response. The unprocessesResourceKeys value is in the same form as ResourceKeys, so the value can be directly provided to a subsequent BatchGetResourceConfig operation. If there are no unprocessed resource keys, the response contains an empty unprocessedResourceKeys list. 
              - *(dict) --* 
                The details that identify a resource within AWS Config, including the resource type and resource ID.
                - **resourceType** *(string) --* 
                  The resource type.
                - **resourceId** *(string) --* 
                  The ID of the resource (for example., sg-xxxxxx). 
        :type resourceKeys: list
        :param resourceKeys: **[REQUIRED]**
          A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.
          - *(dict) --*
            The details that identify a resource within AWS Config, including the resource type and resource ID.
            - **resourceType** *(string) --* **[REQUIRED]**
              The resource type.
            - **resourceId** *(string) --* **[REQUIRED]**
              The ID of the resource (for example., sg-xxxxxx).
        :rtype: dict
        :returns:
        """
        pass

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

    def delete_aggregation_authorization(self, AuthorizedAccountId: str, AuthorizedAwsRegion: str):
        """
        Deletes the authorization granted to the specified configuration aggregator account in a specified region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteAggregationAuthorization>`_
        
        **Request Syntax**
        ::
          response = client.delete_aggregation_authorization(
              AuthorizedAccountId='string',
              AuthorizedAwsRegion='string'
          )
        :type AuthorizedAccountId: string
        :param AuthorizedAccountId: **[REQUIRED]**
          The 12-digit account ID of the account authorized to aggregate data.
        :type AuthorizedAwsRegion: string
        :param AuthorizedAwsRegion: **[REQUIRED]**
          The region authorized to collect aggregated data.
        :returns: None
        """
        pass

    def delete_config_rule(self, ConfigRuleName: str):
        """
        Deletes the specified AWS Config rule and all of its evaluation results.
        AWS Config sets the state of a rule to ``DELETING`` until the deletion is complete. You cannot update a rule while it is in this state. If you make a ``PutConfigRule`` or ``DeleteConfigRule`` request for the rule, you will receive a ``ResourceInUseException`` .
        You can check the state of a rule by using the ``DescribeConfigRules`` request.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteConfigRule>`_
        
        **Request Syntax**
        ::
          response = client.delete_config_rule(
              ConfigRuleName='string'
          )
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**
          The name of the AWS Config rule that you want to delete.
        :returns: None
        """
        pass

    def delete_configuration_aggregator(self, ConfigurationAggregatorName: str):
        """
        Deletes the specified configuration aggregator and the aggregated data associated with the aggregator.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteConfigurationAggregator>`_
        
        **Request Syntax**
        ::
          response = client.delete_configuration_aggregator(
              ConfigurationAggregatorName='string'
          )
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :returns: None
        """
        pass

    def delete_configuration_recorder(self, ConfigurationRecorderName: str):
        """
        Deletes the configuration recorder.
        After the configuration recorder is deleted, AWS Config will not record resource configuration changes until you create a new configuration recorder.
        This action does not delete the configuration information that was previously recorded. You will be able to access the previously recorded information by using the ``GetResourceConfigHistory`` action, but you will not be able to access this information in the AWS Config console until you create a new configuration recorder.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteConfigurationRecorder>`_
        
        **Request Syntax**
        ::
          response = client.delete_configuration_recorder(
              ConfigurationRecorderName='string'
          )
        :type ConfigurationRecorderName: string
        :param ConfigurationRecorderName: **[REQUIRED]**
          The name of the configuration recorder to be deleted. You can retrieve the name of your configuration recorder by using the ``DescribeConfigurationRecorders`` action.
        :returns: None
        """
        pass

    def delete_delivery_channel(self, DeliveryChannelName: str):
        """
        Deletes the delivery channel.
        Before you can delete the delivery channel, you must stop the configuration recorder by using the  StopConfigurationRecorder action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteDeliveryChannel>`_
        
        **Request Syntax**
        ::
          response = client.delete_delivery_channel(
              DeliveryChannelName='string'
          )
        :type DeliveryChannelName: string
        :param DeliveryChannelName: **[REQUIRED]**
          The name of the delivery channel to delete.
        :returns: None
        """
        pass

    def delete_evaluation_results(self, ConfigRuleName: str) -> Dict:
        """
        Deletes the evaluation results for the specified AWS Config rule. You can specify one AWS Config rule per request. After you delete the evaluation results, you can call the  StartConfigRulesEvaluation API to start evaluating your AWS resources against the rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteEvaluationResults>`_
        
        **Request Syntax**
        ::
          response = client.delete_evaluation_results(
              ConfigRuleName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output when you delete the evaluation results for the specified AWS Config rule.
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**
          The name of the AWS Config rule for which you want to delete the evaluation results.
        :rtype: dict
        :returns:
        """
        pass

    def delete_pending_aggregation_request(self, RequesterAccountId: str, RequesterAwsRegion: str):
        """
        Deletes pending authorization requests for a specified aggregator account in a specified region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeletePendingAggregationRequest>`_
        
        **Request Syntax**
        ::
          response = client.delete_pending_aggregation_request(
              RequesterAccountId='string',
              RequesterAwsRegion='string'
          )
        :type RequesterAccountId: string
        :param RequesterAccountId: **[REQUIRED]**
          The 12-digit account ID of the account requesting to aggregate data.
        :type RequesterAwsRegion: string
        :param RequesterAwsRegion: **[REQUIRED]**
          The region requesting to aggregate data.
        :returns: None
        """
        pass

    def delete_remediation_configuration(self, ConfigRuleName: str, ResourceType: str = None) -> Dict:
        """
        Deletes the remediation configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteRemediationConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_remediation_configuration(
              ConfigRuleName='string',
              ResourceType='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**
          The name of the AWS Config rule for which you want to delete remediation configuration.
        :type ResourceType: string
        :param ResourceType:
          The type of a resource.
        :rtype: dict
        :returns:
        """
        pass

    def delete_retention_configuration(self, RetentionConfigurationName: str):
        """
        Deletes the retention configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeleteRetentionConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_retention_configuration(
              RetentionConfigurationName='string'
          )
        :type RetentionConfigurationName: string
        :param RetentionConfigurationName: **[REQUIRED]**
          The name of the retention configuration to delete.
        :returns: None
        """
        pass

    def deliver_config_snapshot(self, deliveryChannelName: str) -> Dict:
        """
        Schedules delivery of a configuration snapshot to the Amazon S3 bucket in the specified delivery channel. After the delivery has started, AWS Config sends the following notifications using an Amazon SNS topic that you have specified.
        * Notification of the start of the delivery. 
        * Notification of the completion of the delivery, if the delivery was successfully completed. 
        * Notification of delivery failure, if the delivery failed. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DeliverConfigSnapshot>`_
        
        **Request Syntax**
        ::
          response = client.deliver_config_snapshot(
              deliveryChannelName='string'
          )
        
        **Response Syntax**
        ::
            {
                'configSnapshotId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  DeliverConfigSnapshot action, in JSON format.
            - **configSnapshotId** *(string) --* 
              The ID of the snapshot that is being created.
        :type deliveryChannelName: string
        :param deliveryChannelName: **[REQUIRED]**
          The name of the delivery channel through which the snapshot is delivered.
        :rtype: dict
        :returns:
        """
        pass

    def describe_aggregate_compliance_by_config_rules(self, ConfigurationAggregatorName: str, Filters: Dict = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of compliant and noncompliant rules with the number of resources for compliant and noncompliant rules. 
        .. note::
          The results can return an empty result page, but if you have a nextToken, the results are displayed on the next page.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeAggregateComplianceByConfigRules>`_
        
        **Request Syntax**
        ::
          response = client.describe_aggregate_compliance_by_config_rules(
              ConfigurationAggregatorName='string',
              Filters={
                  'ConfigRuleName': 'string',
                  'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                  'AccountId': 'string',
                  'AwsRegion': 'string'
              },
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'AggregateComplianceByConfigRules': [
                    {
                        'ConfigRuleName': 'string',
                        'Compliance': {
                            'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                            'ComplianceContributorCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            }
                        },
                        'AccountId': 'string',
                        'AwsRegion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AggregateComplianceByConfigRules** *(list) --* 
              Returns a list of AggregateComplianceByConfigRule object.
              - *(dict) --* 
                Indicates whether an AWS Config rule is compliant based on account ID, region, compliance, and rule name.
                A rule is compliant if all of the resources that the rule evaluated comply with it. It is noncompliant if any of these resources do not comply.
                - **ConfigRuleName** *(string) --* 
                  The name of the AWS Config rule.
                - **Compliance** *(dict) --* 
                  Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.
                  - **ComplianceType** *(string) --* 
                    Indicates whether an AWS resource or AWS Config rule is compliant.
                    A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
                    A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
                    AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or AWS Config rule.
                    For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.
                  - **ComplianceContributorCount** *(dict) --* 
                    The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.
                    - **CappedCount** *(integer) --* 
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                    - **CapExceeded** *(boolean) --* 
                      Indicates whether the maximum count is reached.
                - **AccountId** *(string) --* 
                  The 12-digit account ID of the source account.
                - **AwsRegion** *(string) --* 
                  The source region from where the data is aggregated.
            - **NextToken** *(string) --* 
              The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type Filters: dict
        :param Filters:
          Filters the results by ConfigRuleComplianceFilters object.
          - **ConfigRuleName** *(string) --*
            The name of the AWS Config rule.
          - **ComplianceType** *(string) --*
            The rule compliance status.
            For the ``ConfigRuleComplianceFilters`` data type, AWS Config supports only ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE`` and the ``INSUFFICIENT_DATA`` values.
          - **AccountId** *(string) --*
            The 12-digit account ID of the source account.
          - **AwsRegion** *(string) --*
            The source region where the data is aggregated.
        :type Limit: integer
        :param Limit:
          The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def describe_aggregation_authorizations(self, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of authorizations granted to various aggregator accounts and regions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeAggregationAuthorizations>`_
        
        **Request Syntax**
        ::
          response = client.describe_aggregation_authorizations(
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'AggregationAuthorizations': [
                    {
                        'AggregationAuthorizationArn': 'string',
                        'AuthorizedAccountId': 'string',
                        'AuthorizedAwsRegion': 'string',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AggregationAuthorizations** *(list) --* 
              Returns a list of authorizations granted to various aggregator accounts and regions.
              - *(dict) --* 
                An object that represents the authorizations granted to aggregator accounts and regions.
                - **AggregationAuthorizationArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the aggregation object.
                - **AuthorizedAccountId** *(string) --* 
                  The 12-digit account ID of the account authorized to aggregate data.
                - **AuthorizedAwsRegion** *(string) --* 
                  The region authorized to collect aggregated data.
                - **CreationTime** *(datetime) --* 
                  The time stamp when the aggregation authorization was created.
            - **NextToken** *(string) --* 
              The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type Limit: integer
        :param Limit:
          The maximum number of AggregationAuthorizations returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def describe_compliance_by_config_rule(self, ConfigRuleNames: List = None, ComplianceTypes: List = None, NextToken: str = None) -> Dict:
        """
        Indicates whether the specified AWS Config rules are compliant. If a rule is noncompliant, this action returns the number of AWS resources that do not comply with the rule.
        A rule is compliant if all of the evaluated resources comply with it. It is noncompliant if any of these resources do not comply.
        If AWS Config has no current evaluation results for the rule, it returns ``INSUFFICIENT_DATA`` . This result might indicate one of the following conditions:
        * AWS Config has never invoked an evaluation for the rule. To check whether it has, use the ``DescribeConfigRuleEvaluationStatus`` action to get the ``LastSuccessfulInvocationTime`` and ``LastFailedInvocationTime`` . 
        * The rule's AWS Lambda function is failing to send evaluation results to AWS Config. Verify that the role you assigned to your configuration recorder includes the ``config:PutEvaluations`` permission. If the rule is a custom rule, verify that the AWS Lambda execution role includes the ``config:PutEvaluations`` permission. 
        * The rule's AWS Lambda function has returned ``NOT_APPLICABLE`` for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByConfigRule>`_
        
        **Request Syntax**
        ::
          response = client.describe_compliance_by_config_rule(
              ConfigRuleNames=[
                  'string',
              ],
              ComplianceTypes=[
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              ],
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ComplianceByConfigRules': [
                    {
                        'ConfigRuleName': 'string',
                        'Compliance': {
                            'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                            'ComplianceContributorCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ComplianceByConfigRules** *(list) --* 
              Indicates whether each of the specified AWS Config rules is compliant.
              - *(dict) --* 
                Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the resources that the rule evaluated comply with it. A rule is noncompliant if any of these resources do not comply.
                - **ConfigRuleName** *(string) --* 
                  The name of the AWS Config rule.
                - **Compliance** *(dict) --* 
                  Indicates whether the AWS Config rule is compliant.
                  - **ComplianceType** *(string) --* 
                    Indicates whether an AWS resource or AWS Config rule is compliant.
                    A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
                    A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
                    AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or AWS Config rule.
                    For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.
                  - **ComplianceContributorCount** *(dict) --* 
                    The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.
                    - **CappedCount** *(integer) --* 
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                    - **CapExceeded** *(boolean) --* 
                      Indicates whether the maximum count is reached.
            - **NextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type ConfigRuleNames: list
        :param ConfigRuleNames:
          Specify one or more AWS Config rule names to filter the results by rule.
          - *(string) --*
        :type ComplianceTypes: list
        :param ComplianceTypes:
          Filters the results by compliance.
          The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def describe_compliance_by_resource(self, ResourceType: str = None, ResourceId: str = None, ComplianceTypes: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Indicates whether the specified AWS resources are compliant. If a resource is noncompliant, this action returns the number of AWS Config rules that the resource does not comply with.
        A resource is compliant if it complies with all the AWS Config rules that evaluate it. It is noncompliant if it does not comply with one or more of these rules.
        If AWS Config has no current evaluation results for the resource, it returns ``INSUFFICIENT_DATA`` . This result might indicate one of the following conditions about the rules that evaluate the resource:
        * AWS Config has never invoked an evaluation for the rule. To check whether it has, use the ``DescribeConfigRuleEvaluationStatus`` action to get the ``LastSuccessfulInvocationTime`` and ``LastFailedInvocationTime`` . 
        * The rule's AWS Lambda function is failing to send evaluation results to AWS Config. Verify that the role that you assigned to your configuration recorder includes the ``config:PutEvaluations`` permission. If the rule is a custom rule, verify that the AWS Lambda execution role includes the ``config:PutEvaluations`` permission. 
        * The rule's AWS Lambda function has returned ``NOT_APPLICABLE`` for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByResource>`_
        
        **Request Syntax**
        ::
          response = client.describe_compliance_by_resource(
              ResourceType='string',
              ResourceId='string',
              ComplianceTypes=[
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              ],
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ComplianceByResources': [
                    {
                        'ResourceType': 'string',
                        'ResourceId': 'string',
                        'Compliance': {
                            'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                            'ComplianceContributorCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ComplianceByResources** *(list) --* 
              Indicates whether the specified AWS resource complies with all of the AWS Config rules that evaluate it.
              - *(dict) --* 
                Indicates whether an AWS resource that is evaluated according to one or more AWS Config rules is compliant. A resource is compliant if it complies with all of the rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
                - **ResourceType** *(string) --* 
                  The type of the AWS resource that was evaluated.
                - **ResourceId** *(string) --* 
                  The ID of the AWS resource that was evaluated.
                - **Compliance** *(dict) --* 
                  Indicates whether the AWS resource complies with all of the AWS Config rules that evaluated it.
                  - **ComplianceType** *(string) --* 
                    Indicates whether an AWS resource or AWS Config rule is compliant.
                    A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
                    A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
                    AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or AWS Config rule.
                    For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.
                  - **ComplianceContributorCount** *(dict) --* 
                    The number of AWS resources or AWS Config rules that cause a result of ``NON_COMPLIANT`` , up to a maximum number.
                    - **CappedCount** *(integer) --* 
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                    - **CapExceeded** *(boolean) --* 
                      Indicates whether the maximum count is reached.
            - **NextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type ResourceType: string
        :param ResourceType:
          The types of AWS resources for which you want compliance information (for example, ``AWS::EC2::Instance`` ). For this action, you can specify that the resource type is an AWS account by specifying ``AWS::::Account`` .
        :type ResourceId: string
        :param ResourceId:
          The ID of the AWS resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for ``ResourceType`` .
        :type ComplianceTypes: list
        :param ComplianceTypes:
          Filters the results by compliance.
          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` .
          - *(string) --*
        :type Limit: integer
        :param Limit:
          The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def describe_config_rule_evaluation_status(self, ConfigRuleNames: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        Returns status information for each of your AWS managed Config rules. The status includes information such as the last time AWS Config invoked the rule, the last time AWS Config failed to invoke the rule, and the related error for the last failure.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRuleEvaluationStatus>`_
        
        **Request Syntax**
        ::
          response = client.describe_config_rule_evaluation_status(
              ConfigRuleNames=[
                  'string',
              ],
              NextToken='string',
              Limit=123
          )
        
        **Response Syntax**
        ::
            {
                'ConfigRulesEvaluationStatus': [
                    {
                        'ConfigRuleName': 'string',
                        'ConfigRuleArn': 'string',
                        'ConfigRuleId': 'string',
                        'LastSuccessfulInvocationTime': datetime(2015, 1, 1),
                        'LastFailedInvocationTime': datetime(2015, 1, 1),
                        'LastSuccessfulEvaluationTime': datetime(2015, 1, 1),
                        'LastFailedEvaluationTime': datetime(2015, 1, 1),
                        'FirstActivatedTime': datetime(2015, 1, 1),
                        'LastErrorCode': 'string',
                        'LastErrorMessage': 'string',
                        'FirstEvaluationStarted': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConfigRulesEvaluationStatus** *(list) --* 
              Status information about your AWS managed Config rules.
              - *(dict) --* 
                Status information for your AWS managed Config rules. The status includes information such as the last time the rule ran, the last time it failed, and the related error for the last failure.
                This action does not return status information about custom AWS Config rules.
                - **ConfigRuleName** *(string) --* 
                  The name of the AWS Config rule.
                - **ConfigRuleArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the AWS Config rule.
                - **ConfigRuleId** *(string) --* 
                  The ID of the AWS Config rule.
                - **LastSuccessfulInvocationTime** *(datetime) --* 
                  The time that AWS Config last successfully invoked the AWS Config rule to evaluate your AWS resources.
                - **LastFailedInvocationTime** *(datetime) --* 
                  The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS resources.
                - **LastSuccessfulEvaluationTime** *(datetime) --* 
                  The time that AWS Config last successfully evaluated your AWS resources against the rule.
                - **LastFailedEvaluationTime** *(datetime) --* 
                  The time that AWS Config last failed to evaluate your AWS resources against the rule.
                - **FirstActivatedTime** *(datetime) --* 
                  The time that you first activated the AWS Config rule.
                - **LastErrorCode** *(string) --* 
                  The error code that AWS Config returned when the rule last failed.
                - **LastErrorMessage** *(string) --* 
                  The error message that AWS Config returned when the rule last failed.
                - **FirstEvaluationStarted** *(boolean) --* 
                  Indicates whether AWS Config has evaluated your resources against the rule at least once.
                  * ``true`` - AWS Config has evaluated your AWS resources against the rule at least once. 
                  * ``false`` - AWS Config has not once finished evaluating your AWS resources against the rule. 
            - **NextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type ConfigRuleNames: list
        :param ConfigRuleNames:
          The name of the AWS managed Config rules for which you want status information. If you do not specify any names, AWS Config returns status information for all AWS managed Config rules that you use.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :type Limit: integer
        :param Limit:
          The number of rule evaluation results that you want returned.
          This parameter is required if the rule limit for your account is more than the default of 50 rules.
          For information about requesting a rule limit increase, see `AWS Config Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config>`__ in the *AWS General Reference Guide* .
        :rtype: dict
        :returns:
        """
        pass

    def describe_config_rules(self, ConfigRuleNames: List = None, NextToken: str = None) -> Dict:
        """
        Returns details about your AWS Config rules.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRules>`_
        
        **Request Syntax**
        ::
          response = client.describe_config_rules(
              ConfigRuleNames=[
                  'string',
              ],
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ConfigRules': [
                    {
                        'ConfigRuleName': 'string',
                        'ConfigRuleArn': 'string',
                        'ConfigRuleId': 'string',
                        'Description': 'string',
                        'Scope': {
                            'ComplianceResourceTypes': [
                                'string',
                            ],
                            'TagKey': 'string',
                            'TagValue': 'string',
                            'ComplianceResourceId': 'string'
                        },
                        'Source': {
                            'Owner': 'CUSTOM_LAMBDA'|'AWS',
                            'SourceIdentifier': 'string',
                            'SourceDetails': [
                                {
                                    'EventSource': 'aws.config',
                                    'MessageType': 'ConfigurationItemChangeNotification'|'ConfigurationSnapshotDeliveryCompleted'|'ScheduledNotification'|'OversizedConfigurationItemChangeNotification',
                                    'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                                },
                            ]
                        },
                        'InputParameters': 'string',
                        'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                        'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING',
                        'CreatedBy': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConfigRules** *(list) --* 
              The details about your AWS Config rules.
              - *(dict) --* 
                An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a predefined function for an AWS managed rule. The function evaluates configuration items to assess whether your AWS resources comply with your desired configurations. This function can run when AWS Config detects a configuration change to an AWS resource and at a periodic frequency that you choose (for example, every 24 hours).
                .. note::
                  You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .
                For more information about developing and using AWS Config rules, see `Evaluating AWS Resource Configurations with AWS Config <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the *AWS Config Developer Guide* .
                - **ConfigRuleName** *(string) --* 
                  The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.
                - **ConfigRuleArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the AWS Config rule.
                - **ConfigRuleId** *(string) --* 
                  The ID of the AWS Config rule.
                - **Description** *(string) --* 
                  The description that you provide for the AWS Config rule.
                - **Scope** *(dict) --* 
                  Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
                  - **ComplianceResourceTypes** *(list) --* 
                    The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .
                    - *(string) --* 
                  - **TagKey** *(string) --* 
                    The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
                  - **TagValue** *(string) --* 
                    The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .
                  - **ComplianceResourceId** *(string) --* 
                    The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .
                - **Source** *(dict) --* 
                  Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
                  - **Owner** *(string) --* 
                    Indicates whether AWS or the customer owns and manages the AWS Config rule.
                  - **SourceIdentifier** *(string) --* 
                    For AWS Config managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Managed Config Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__ .
                    For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .
                  - **SourceDetails** *(list) --* 
                    Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.
                    - *(dict) --* 
                      Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for ``SourceDetail`` only for custom rules. 
                      - **EventSource** *(string) --* 
                        The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.
                      - **MessageType** *(string) --* 
                        The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
                        * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. 
                        * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. 
                        * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` . 
                        * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot. 
                        If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for ``OversizedConfigurationItemChangeNotification`` .
                      - **MaximumExecutionFrequency** *(string) --* 
                        The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value.
                        .. note::
                          By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
                          Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once every three hours. In this case, ``Three_Hours`` is the frequency of this rule. 
                - **InputParameters** *(string) --* 
                  A string, in JSON format, that is passed to the AWS Config rule Lambda function.
                - **MaximumExecutionFrequency** *(string) --* 
                  The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when:
                  * You are using an AWS managed rule that is triggered at a periodic frequency. 
                  * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties . 
                  .. note::
                    By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
                - **ConfigRuleState** *(string) --* 
                  Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the AWS Config rule.
                  AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the ``StartConfigRulesEvaluation`` request to evaluate your resources against the AWS Config rule.
                  AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use the ``DeleteEvaluationResults`` request to delete the current evaluation results for the AWS Config rule.
                  AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.
                - **CreatedBy** *(string) --* 
                  Service principal name of the service that created the rule.
                  .. note::
                    The field is populated only if the service linked rule is created by a service. The field is empty if you create your own rule.
            - **NextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type ConfigRuleNames: list
        :param ConfigRuleNames:
          The names of the AWS Config rules for which you want details. If you do not specify any names, AWS Config returns details for all your rules.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def describe_configuration_aggregator_sources_status(self, ConfigurationAggregatorName: str, UpdateStatus: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        Returns status information for sources within an aggregator. The status includes information about the last time AWS Config verified authorization between the source account and an aggregator account. In case of a failure, the status contains the related error code or message. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus>`_
        
        **Request Syntax**
        ::
          response = client.describe_configuration_aggregator_sources_status(
              ConfigurationAggregatorName='string',
              UpdateStatus=[
                  'FAILED'|'SUCCEEDED'|'OUTDATED',
              ],
              NextToken='string',
              Limit=123
          )
        
        **Response Syntax**
        ::
            {
                'AggregatedSourceStatusList': [
                    {
                        'SourceId': 'string',
                        'SourceType': 'ACCOUNT'|'ORGANIZATION',
                        'AwsRegion': 'string',
                        'LastUpdateStatus': 'FAILED'|'SUCCEEDED'|'OUTDATED',
                        'LastUpdateTime': datetime(2015, 1, 1),
                        'LastErrorCode': 'string',
                        'LastErrorMessage': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AggregatedSourceStatusList** *(list) --* 
              Returns an AggregatedSourceStatus object. 
              - *(dict) --* 
                The current sync status between the source and the aggregator account.
                - **SourceId** *(string) --* 
                  The source account ID or an organization.
                - **SourceType** *(string) --* 
                  The source account or an organization.
                - **AwsRegion** *(string) --* 
                  The region authorized to collect aggregated data.
                - **LastUpdateStatus** *(string) --* 
                  Filters the last updated status type.
                  * Valid value FAILED indicates errors while moving data. 
                  * Valid value SUCCEEDED indicates the data was successfully moved. 
                  * Valid value OUTDATED indicates the data is not the most recent. 
                - **LastUpdateTime** *(datetime) --* 
                  The time of the last update.
                - **LastErrorCode** *(string) --* 
                  The error code that AWS Config returned when the source account aggregation last failed.
                - **LastErrorMessage** *(string) --* 
                  The message indicating that the source account aggregation failed due to an error.
            - **NextToken** *(string) --* 
              The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type UpdateStatus: list
        :param UpdateStatus:
          Filters the status type.
          * Valid value FAILED indicates errors while moving data.
          * Valid value SUCCEEDED indicates the data was successfully moved.
          * Valid value OUTDATED indicates the data is not the most recent.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type Limit: integer
        :param Limit:
          The maximum number of AggregatorSourceStatus returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
        :rtype: dict
        :returns:
        """
        pass

    def describe_configuration_aggregators(self, ConfigurationAggregatorNames: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        Returns the details of one or more configuration aggregators. If the configuration aggregator is not specified, this action returns the details for all the configuration aggregators associated with the account. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationAggregators>`_
        
        **Request Syntax**
        ::
          response = client.describe_configuration_aggregators(
              ConfigurationAggregatorNames=[
                  'string',
              ],
              NextToken='string',
              Limit=123
          )
        
        **Response Syntax**
        ::
            {
                'ConfigurationAggregators': [
                    {
                        'ConfigurationAggregatorName': 'string',
                        'ConfigurationAggregatorArn': 'string',
                        'AccountAggregationSources': [
                            {
                                'AccountIds': [
                                    'string',
                                ],
                                'AllAwsRegions': True|False,
                                'AwsRegions': [
                                    'string',
                                ]
                            },
                        ],
                        'OrganizationAggregationSource': {
                            'RoleArn': 'string',
                            'AwsRegions': [
                                'string',
                            ],
                            'AllAwsRegions': True|False
                        },
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConfigurationAggregators** *(list) --* 
              Returns a ConfigurationAggregators object.
              - *(dict) --* 
                The details about the configuration aggregator, including information about source accounts, regions, and metadata of the aggregator. 
                - **ConfigurationAggregatorName** *(string) --* 
                  The name of the aggregator.
                - **ConfigurationAggregatorArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the aggregator.
                - **AccountAggregationSources** *(list) --* 
                  Provides a list of source accounts and regions to be aggregated.
                  - *(dict) --* 
                    A collection of accounts and regions.
                    - **AccountIds** *(list) --* 
                      The 12-digit account ID of the account being aggregated. 
                      - *(string) --* 
                    - **AllAwsRegions** *(boolean) --* 
                      If true, aggregate existing AWS Config regions and future regions.
                    - **AwsRegions** *(list) --* 
                      The source regions being aggregated.
                      - *(string) --* 
                - **OrganizationAggregationSource** *(dict) --* 
                  Provides an organization and list of regions to be aggregated.
                  - **RoleArn** *(string) --* 
                    ARN of the IAM role used to retreive AWS Organization details associated with the aggregator account.
                  - **AwsRegions** *(list) --* 
                    The source regions being aggregated.
                    - *(string) --* 
                  - **AllAwsRegions** *(boolean) --* 
                    If true, aggregate existing AWS Config regions and future regions.
                - **CreationTime** *(datetime) --* 
                  The time stamp when the configuration aggregator was created.
                - **LastUpdatedTime** *(datetime) --* 
                  The time of the last update.
            - **NextToken** *(string) --* 
              The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type ConfigurationAggregatorNames: list
        :param ConfigurationAggregatorNames:
          The name of the configuration aggregators.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type Limit: integer
        :param Limit:
          The maximum number of configuration aggregators returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
        :rtype: dict
        :returns:
        """
        pass

    def describe_configuration_recorder_status(self, ConfigurationRecorderNames: List = None) -> Dict:
        """
        Returns the current status of the specified configuration recorder. If a configuration recorder is not specified, this action returns the status of all configuration recorders associated with the account.
        .. note::
          Currently, you can specify only one configuration recorder per region in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationRecorderStatus>`_
        
        **Request Syntax**
        ::
          response = client.describe_configuration_recorder_status(
              ConfigurationRecorderNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ConfigurationRecordersStatus': [
                    {
                        'name': 'string',
                        'lastStartTime': datetime(2015, 1, 1),
                        'lastStopTime': datetime(2015, 1, 1),
                        'recording': True|False,
                        'lastStatus': 'Pending'|'Success'|'Failure',
                        'lastErrorCode': 'string',
                        'lastErrorMessage': 'string',
                        'lastStatusChangeTime': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  DescribeConfigurationRecorderStatus action, in JSON format.
            - **ConfigurationRecordersStatus** *(list) --* 
              A list that contains status of the specified recorders.
              - *(dict) --* 
                The current status of the configuration recorder.
                - **name** *(string) --* 
                  The name of the configuration recorder.
                - **lastStartTime** *(datetime) --* 
                  The time the recorder was last started.
                - **lastStopTime** *(datetime) --* 
                  The time the recorder was last stopped.
                - **recording** *(boolean) --* 
                  Specifies whether or not the recorder is currently recording.
                - **lastStatus** *(string) --* 
                  The last (previous) status of the recorder.
                - **lastErrorCode** *(string) --* 
                  The error code indicating that the recording failed.
                - **lastErrorMessage** *(string) --* 
                  The message indicating that the recording failed due to an error.
                - **lastStatusChangeTime** *(datetime) --* 
                  The time when the status was last changed.
        :type ConfigurationRecorderNames: list
        :param ConfigurationRecorderNames:
          The name(s) of the configuration recorder. If the name is not specified, the action returns the current status of all the configuration recorders associated with the account.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_configuration_recorders(self, ConfigurationRecorderNames: List = None) -> Dict:
        """
        Returns the details for the specified configuration recorders. If the configuration recorder is not specified, this action returns the details for all configuration recorders associated with the account.
        .. note::
          Currently, you can specify only one configuration recorder per region in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationRecorders>`_
        
        **Request Syntax**
        ::
          response = client.describe_configuration_recorders(
              ConfigurationRecorderNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ConfigurationRecorders': [
                    {
                        'name': 'string',
                        'roleARN': 'string',
                        'recordingGroup': {
                            'allSupported': True|False,
                            'includeGlobalResourceTypes': True|False,
                            'resourceTypes': [
                                'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                            ]
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  DescribeConfigurationRecorders action.
            - **ConfigurationRecorders** *(list) --* 
              A list that contains the descriptions of the specified configuration recorders.
              - *(dict) --* 
                An object that represents the recording of configuration changes of an AWS resource.
                - **name** *(string) --* 
                  The name of the recorder. By default, AWS Config automatically assigns the name "default" when creating the configuration recorder. You cannot change the assigned name.
                - **roleARN** *(string) --* 
                  Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.
                - **recordingGroup** *(dict) --* 
                  Specifies the types of AWS resources for which AWS Config records configuration changes.
                  - **allSupported** *(boolean) --* 
                    Specifies whether AWS Config records configuration changes for every supported type of regional resource.
                    If you set this option to ``true`` , when AWS Config adds support for a new type of regional resource, it starts recording resources of that type automatically.
                    If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .
                  - **includeGlobalResourceTypes** *(boolean) --* 
                    Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.
                    Before you can set this option to ``true`` , you must set the ``allSupported`` option to ``true`` .
                    If you set this option to ``true`` , when AWS Config adds support for a new type of global resource, it starts recording resources of that type automatically.
                    The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.
                  - **resourceTypes** *(list) --* 
                    A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, ``AWS::EC2::Instance`` or ``AWS::CloudTrail::Trail`` ).
                    Before you can set this option to ``true`` , you must set the ``allSupported`` option to ``false`` .
                    If you set this option to ``true`` , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.
                    For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in `Supported AWS Resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__ .
                    - *(string) --* 
        :type ConfigurationRecorderNames: list
        :param ConfigurationRecorderNames:
          A list of configuration recorder names.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_delivery_channel_status(self, DeliveryChannelNames: List = None) -> Dict:
        """
        Returns the current status of the specified delivery channel. If a delivery channel is not specified, this action returns the current status of all delivery channels associated with the account.
        .. note::
          Currently, you can specify only one delivery channel per region in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeDeliveryChannelStatus>`_
        
        **Request Syntax**
        ::
          response = client.describe_delivery_channel_status(
              DeliveryChannelNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DeliveryChannelsStatus': [
                    {
                        'name': 'string',
                        'configSnapshotDeliveryInfo': {
                            'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                            'lastErrorCode': 'string',
                            'lastErrorMessage': 'string',
                            'lastAttemptTime': datetime(2015, 1, 1),
                            'lastSuccessfulTime': datetime(2015, 1, 1),
                            'nextDeliveryTime': datetime(2015, 1, 1)
                        },
                        'configHistoryDeliveryInfo': {
                            'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                            'lastErrorCode': 'string',
                            'lastErrorMessage': 'string',
                            'lastAttemptTime': datetime(2015, 1, 1),
                            'lastSuccessfulTime': datetime(2015, 1, 1),
                            'nextDeliveryTime': datetime(2015, 1, 1)
                        },
                        'configStreamDeliveryInfo': {
                            'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                            'lastErrorCode': 'string',
                            'lastErrorMessage': 'string',
                            'lastStatusChangeTime': datetime(2015, 1, 1)
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  DescribeDeliveryChannelStatus action.
            - **DeliveryChannelsStatus** *(list) --* 
              A list that contains the status of a specified delivery channel.
              - *(dict) --* 
                The status of a specified delivery channel.
                Valid values: ``Success`` | ``Failure``  
                - **name** *(string) --* 
                  The name of the delivery channel.
                - **configSnapshotDeliveryInfo** *(dict) --* 
                  A list containing the status of the delivery of the snapshot to the specified Amazon S3 bucket.
                  - **lastStatus** *(string) --* 
                    Status of the last attempted delivery.
                  - **lastErrorCode** *(string) --* 
                    The error code from the last attempted delivery.
                  - **lastErrorMessage** *(string) --* 
                    The error message from the last attempted delivery.
                  - **lastAttemptTime** *(datetime) --* 
                    The time of the last attempted delivery.
                  - **lastSuccessfulTime** *(datetime) --* 
                    The time of the last successful delivery.
                  - **nextDeliveryTime** *(datetime) --* 
                    The time that the next delivery occurs.
                - **configHistoryDeliveryInfo** *(dict) --* 
                  A list that contains the status of the delivery of the configuration history to the specified Amazon S3 bucket.
                  - **lastStatus** *(string) --* 
                    Status of the last attempted delivery.
                  - **lastErrorCode** *(string) --* 
                    The error code from the last attempted delivery.
                  - **lastErrorMessage** *(string) --* 
                    The error message from the last attempted delivery.
                  - **lastAttemptTime** *(datetime) --* 
                    The time of the last attempted delivery.
                  - **lastSuccessfulTime** *(datetime) --* 
                    The time of the last successful delivery.
                  - **nextDeliveryTime** *(datetime) --* 
                    The time that the next delivery occurs.
                - **configStreamDeliveryInfo** *(dict) --* 
                  A list containing the status of the delivery of the configuration stream notification to the specified Amazon SNS topic.
                  - **lastStatus** *(string) --* 
                    Status of the last attempted delivery.
                     **Note** Providing an SNS topic on a `DeliveryChannel <https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html>`__ for AWS Config is optional. If the SNS delivery is turned off, the last status will be **Not_Applicable** .
                  - **lastErrorCode** *(string) --* 
                    The error code from the last attempted delivery.
                  - **lastErrorMessage** *(string) --* 
                    The error message from the last attempted delivery.
                  - **lastStatusChangeTime** *(datetime) --* 
                    The time from the last status change.
        :type DeliveryChannelNames: list
        :param DeliveryChannelNames:
          A list of delivery channel names.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_delivery_channels(self, DeliveryChannelNames: List = None) -> Dict:
        """
        Returns details about the specified delivery channel. If a delivery channel is not specified, this action returns the details of all delivery channels associated with the account.
        .. note::
          Currently, you can specify only one delivery channel per region in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeDeliveryChannels>`_
        
        **Request Syntax**
        ::
          response = client.describe_delivery_channels(
              DeliveryChannelNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DeliveryChannels': [
                    {
                        'name': 'string',
                        's3BucketName': 'string',
                        's3KeyPrefix': 'string',
                        'snsTopicARN': 'string',
                        'configSnapshotDeliveryProperties': {
                            'deliveryFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  DescribeDeliveryChannels action.
            - **DeliveryChannels** *(list) --* 
              A list that contains the descriptions of the specified delivery channel.
              - *(dict) --* 
                The channel through which AWS Config delivers notifications and updated configuration states.
                - **name** *(string) --* 
                  The name of the delivery channel. By default, AWS Config assigns the name "default" when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.
                - **s3BucketName** *(string) --* 
                  The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.
                  If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`__ in the AWS Config Developer Guide.
                - **s3KeyPrefix** *(string) --* 
                  The prefix for the specified Amazon S3 bucket.
                - **snsTopicARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.
                  If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`__ in the AWS Config Developer Guide.
                - **configSnapshotDeliveryProperties** *(dict) --* 
                  The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.
                  - **deliveryFrequency** *(string) --* 
                    The frequency with which AWS Config delivers configuration snapshots.
        :type DeliveryChannelNames: list
        :param DeliveryChannelNames:
          A list of delivery channel names.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_pending_aggregation_requests(self, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of all pending aggregation requests.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribePendingAggregationRequests>`_
        
        **Request Syntax**
        ::
          response = client.describe_pending_aggregation_requests(
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'PendingAggregationRequests': [
                    {
                        'RequesterAccountId': 'string',
                        'RequesterAwsRegion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PendingAggregationRequests** *(list) --* 
              Returns a PendingAggregationRequests object.
              - *(dict) --* 
                An object that represents the account ID and region of an aggregator account that is requesting authorization but is not yet authorized.
                - **RequesterAccountId** *(string) --* 
                  The 12-digit account ID of the account requesting to aggregate data.
                - **RequesterAwsRegion** *(string) --* 
                  The region requesting to aggregate data. 
            - **NextToken** *(string) --* 
              The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type Limit: integer
        :param Limit:
          The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def describe_remediation_configurations(self, ConfigRuleNames: List) -> Dict:
        """
        Returns the details of one or more remediation configurations.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeRemediationConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.describe_remediation_configurations(
              ConfigRuleNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'RemediationConfigurations': [
                    {
                        'ConfigRuleName': 'string',
                        'TargetType': 'SSM_DOCUMENT',
                        'TargetId': 'string',
                        'TargetVersion': 'string',
                        'Parameters': {
                            'string': {
                                'ResourceValue': {
                                    'Value': 'RESOURCE_ID'
                                },
                                'StaticValue': {
                                    'Values': [
                                        'string',
                                    ]
                                }
                            }
                        },
                        'ResourceType': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RemediationConfigurations** *(list) --* 
              Returns a remediation configuration object.
              - *(dict) --* 
                An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.
                - **ConfigRuleName** *(string) --* 
                  The name of the AWS Config rule.
                - **TargetType** *(string) --* 
                  The type of the target. Target executes remediation. For example, SSM document.
                - **TargetId** *(string) --* 
                  Target ID is the name of the public document.
                - **TargetVersion** *(string) --* 
                  Version of the target. For example, version of the SSM document.
                - **Parameters** *(dict) --* 
                  An object of the RemediationParameterValue.
                  - *(string) --* 
                    - *(dict) --* 
                      The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.
                      - **ResourceValue** *(dict) --* 
                        The value is dynamic and changes at run-time.
                        - **Value** *(string) --* 
                          The value is a resource ID.
                      - **StaticValue** *(dict) --* 
                        The value is static and does not change at run-time.
                        - **Values** *(list) --* 
                          A list of values. For example, the ARN of the assumed role. 
                          - *(string) --* 
                - **ResourceType** *(string) --* 
                  The type of a resource. 
        :type ConfigRuleNames: list
        :param ConfigRuleNames: **[REQUIRED]**
          A list of AWS Config rule names of remediation configurations for which you want details.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_remediation_execution_status(self, ConfigRuleName: str, ResourceKeys: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Provides a detailed view of a Remediation Execution for a set of resources including state, timestamps for when steps for the remediation execution occur, and any error messages for steps that have failed. When you specify the limit and the next token, you receive a paginated response.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeRemediationExecutionStatus>`_
        
        **Request Syntax**
        ::
          response = client.describe_remediation_execution_status(
              ConfigRuleName='string',
              ResourceKeys=[
                  {
                      'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                      'resourceId': 'string'
                  },
              ],
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'RemediationExecutionStatuses': [
                    {
                        'ResourceKey': {
                            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                            'resourceId': 'string'
                        },
                        'State': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                        'StepDetails': [
                            {
                                'Name': 'string',
                                'State': 'SUCCEEDED'|'PENDING'|'FAILED',
                                'ErrorMessage': 'string',
                                'StartTime': datetime(2015, 1, 1),
                                'StopTime': datetime(2015, 1, 1)
                            },
                        ],
                        'InvocationTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RemediationExecutionStatuses** *(list) --* 
              Returns a list of remediation execution statuses objects.
              - *(dict) --* 
                Provides details of the current status of the invoked remediation action for that resource.
                - **ResourceKey** *(dict) --* 
                  The details that identify a resource within AWS Config, including the resource type and resource ID.
                  - **resourceType** *(string) --* 
                    The resource type.
                  - **resourceId** *(string) --* 
                    The ID of the resource (for example., sg-xxxxxx). 
                - **State** *(string) --* 
                  ENUM of the values.
                - **StepDetails** *(list) --* 
                  Details of every step.
                  - *(dict) --* 
                    Name of the step from the SSM document.
                    - **Name** *(string) --* 
                      The details of the step.
                    - **State** *(string) --* 
                      The valid status of the step.
                    - **ErrorMessage** *(string) --* 
                      An error message if the step was interrupted during execution.
                    - **StartTime** *(datetime) --* 
                      The time when the step started.
                    - **StopTime** *(datetime) --* 
                      The time when the step stopped.
                - **InvocationTime** *(datetime) --* 
                  Start time when the remediation was executed.
                - **LastUpdatedTime** *(datetime) --* 
                  The time when the remediation execution was last updated.
            - **NextToken** *(string) --* 
              The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**
          A list of AWS Config rule names.
        :type ResourceKeys: list
        :param ResourceKeys:
          A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.
          - *(dict) --*
            The details that identify a resource within AWS Config, including the resource type and resource ID.
            - **resourceType** *(string) --* **[REQUIRED]**
              The resource type.
            - **resourceId** *(string) --* **[REQUIRED]**
              The ID of the resource (for example., sg-xxxxxx).
        :type Limit: integer
        :param Limit:
          The maximum number of RemediationExecutionStatuses returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def describe_retention_configurations(self, RetentionConfigurationNames: List = None, NextToken: str = None) -> Dict:
        """
        Returns the details of one or more retention configurations. If the retention configuration name is not specified, this action returns the details for all the retention configurations for that account.
        .. note::
          Currently, AWS Config supports only one retention configuration per region in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeRetentionConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.describe_retention_configurations(
              RetentionConfigurationNames=[
                  'string',
              ],
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'RetentionConfigurations': [
                    {
                        'Name': 'string',
                        'RetentionPeriodInDays': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RetentionConfigurations** *(list) --* 
              Returns a retention configuration object.
              - *(dict) --* 
                An object with the name of the retention configuration and the retention period in days. The object stores the configuration for data retention in AWS Config.
                - **Name** *(string) --* 
                  The name of the retention configuration object.
                - **RetentionPeriodInDays** *(integer) --* 
                  Number of days AWS Config stores your historical information.
                  .. note::
                    Currently, only applicable to the configuration item history.
            - **NextToken** *(string) --* 
              The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response. 
        :type RetentionConfigurationNames: list
        :param RetentionConfigurationNames:
          A list of names of retention configurations for which you want details. If you do not specify a name, AWS Config returns details for all the retention configurations for that account.
          .. note::
            Currently, AWS Config supports only one retention configuration per region in your account.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
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

    def get_aggregate_compliance_details_by_config_rule(self, ConfigurationAggregatorName: str, ConfigRuleName: str, AccountId: str, AwsRegion: str, ComplianceType: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Returns the evaluation results for the specified AWS Config rule for a specific resource in a rule. The results indicate which AWS resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule. 
        .. note::
          The results can return an empty result page. But if you have a nextToken, the results are displayed on the next page.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetAggregateComplianceDetailsByConfigRule>`_
        
        **Request Syntax**
        ::
          response = client.get_aggregate_compliance_details_by_config_rule(
              ConfigurationAggregatorName='string',
              ConfigRuleName='string',
              AccountId='string',
              AwsRegion='string',
              ComplianceType='COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'AggregateEvaluationResults': [
                    {
                        'EvaluationResultIdentifier': {
                            'EvaluationResultQualifier': {
                                'ConfigRuleName': 'string',
                                'ResourceType': 'string',
                                'ResourceId': 'string'
                            },
                            'OrderingTimestamp': datetime(2015, 1, 1)
                        },
                        'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                        'ResultRecordedTime': datetime(2015, 1, 1),
                        'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                        'Annotation': 'string',
                        'AccountId': 'string',
                        'AwsRegion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AggregateEvaluationResults** *(list) --* 
              Returns an AggregateEvaluationResults object.
              - *(dict) --* 
                The details of an AWS Config evaluation for an account ID and region in an aggregator. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information. 
                - **EvaluationResultIdentifier** *(dict) --* 
                  Uniquely identifies the evaluation result.
                  - **EvaluationResultQualifier** *(dict) --* 
                    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.
                    - **ConfigRuleName** *(string) --* 
                      The name of the AWS Config rule that was used in the evaluation.
                    - **ResourceType** *(string) --* 
                      The type of AWS resource that was evaluated.
                    - **ResourceId** *(string) --* 
                      The ID of the evaluated AWS resource.
                  - **OrderingTimestamp** *(datetime) --* 
                    The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.
                - **ComplianceType** *(string) --* 
                  The resource compliance status.
                  For the ``AggregationEvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE`` and ``INSUFFICIENT_DATA`` value.
                - **ResultRecordedTime** *(datetime) --* 
                  The time when AWS Config recorded the aggregate evaluation result.
                - **ConfigRuleInvokedTime** *(datetime) --* 
                  The time when the AWS Config rule evaluated the AWS resource.
                - **Annotation** *(string) --* 
                  Supplementary information about how the agrregate evaluation determined the compliance.
                - **AccountId** *(string) --* 
                  The 12-digit account ID of the source account.
                - **AwsRegion** *(string) --* 
                  The source region from where the data is aggregated.
            - **NextToken** *(string) --* 
              The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**
          The name of the AWS Config rule for which you want compliance information.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The 12-digit account ID of the source account.
        :type AwsRegion: string
        :param AwsRegion: **[REQUIRED]**
          The source region from where the data is aggregated.
        :type ComplianceType: string
        :param ComplianceType:
          The resource compliance status.
          .. note::
            For the ``GetAggregateComplianceDetailsByConfigRuleRequest`` data type, AWS Config supports only the ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE`` and ``INSUFFICIENT_DATA`` values.
        :type Limit: integer
        :param Limit:
          The maximum number of evaluation results returned on each page. The default is 50. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def get_aggregate_config_rule_compliance_summary(self, ConfigurationAggregatorName: str, Filters: Dict = None, GroupByKey: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Returns the number of compliant and noncompliant rules for one or more accounts and regions in an aggregator.
        .. note::
          The results can return an empty result page, but if you have a nextToken, the results are displayed on the next page.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetAggregateConfigRuleComplianceSummary>`_
        
        **Request Syntax**
        ::
          response = client.get_aggregate_config_rule_compliance_summary(
              ConfigurationAggregatorName='string',
              Filters={
                  'AccountId': 'string',
                  'AwsRegion': 'string'
              },
              GroupByKey='ACCOUNT_ID'|'AWS_REGION',
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'GroupByKey': 'string',
                'AggregateComplianceCounts': [
                    {
                        'GroupName': 'string',
                        'ComplianceSummary': {
                            'CompliantResourceCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            },
                            'NonCompliantResourceCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            },
                            'ComplianceSummaryTimestamp': datetime(2015, 1, 1)
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GroupByKey** *(string) --* 
              Groups the result based on ACCOUNT_ID or AWS_REGION.
            - **AggregateComplianceCounts** *(list) --* 
              Returns a list of AggregateComplianceCounts object.
              - *(dict) --* 
                Returns the number of compliant and noncompliant rules for one or more accounts and regions in an aggregator.
                - **GroupName** *(string) --* 
                  The 12-digit account ID or region based on the GroupByKey value.
                - **ComplianceSummary** *(dict) --* 
                  The number of compliant and noncompliant AWS Config rules.
                  - **CompliantResourceCount** *(dict) --* 
                    The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.
                    - **CappedCount** *(integer) --* 
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                    - **CapExceeded** *(boolean) --* 
                      Indicates whether the maximum count is reached.
                  - **NonCompliantResourceCount** *(dict) --* 
                    The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.
                    - **CappedCount** *(integer) --* 
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                    - **CapExceeded** *(boolean) --* 
                      Indicates whether the maximum count is reached.
                  - **ComplianceSummaryTimestamp** *(datetime) --* 
                    The time that AWS Config created the compliance summary.
            - **NextToken** *(string) --* 
              The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type Filters: dict
        :param Filters:
          Filters the results based on the ConfigRuleComplianceSummaryFilters object.
          - **AccountId** *(string) --*
            The 12-digit account ID of the source account.
          - **AwsRegion** *(string) --*
            The source region where the data is aggregated.
        :type GroupByKey: string
        :param GroupByKey:
          Groups the result based on ACCOUNT_ID or AWS_REGION.
        :type Limit: integer
        :param Limit:
          The maximum number of evaluation results returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def get_aggregate_discovered_resource_counts(self, ConfigurationAggregatorName: str, Filters: Dict = None, GroupByKey: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Returns the resource counts across accounts and regions that are present in your AWS Config aggregator. You can request the resource counts by providing filters and GroupByKey.
        For example, if the input contains accountID 12345678910 and region us-east-1 in filters, the API returns the count of resources in account ID 12345678910 and region us-east-1. If the input contains ACCOUNT_ID as a GroupByKey, the API returns resource counts for all source accounts that are present in your aggregator.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetAggregateDiscoveredResourceCounts>`_
        
        **Request Syntax**
        ::
          response = client.get_aggregate_discovered_resource_counts(
              ConfigurationAggregatorName='string',
              Filters={
                  'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                  'AccountId': 'string',
                  'Region': 'string'
              },
              GroupByKey='RESOURCE_TYPE'|'ACCOUNT_ID'|'AWS_REGION',
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'TotalDiscoveredResources': 123,
                'GroupByKey': 'string',
                'GroupedResourceCounts': [
                    {
                        'GroupName': 'string',
                        'ResourceCount': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TotalDiscoveredResources** *(integer) --* 
              The total number of resources that are present in an aggregator with the filters that you provide.
            - **GroupByKey** *(string) --* 
              The key passed into the request object. If ``GroupByKey`` is not provided, the result will be empty.
            - **GroupedResourceCounts** *(list) --* 
              Returns a list of GroupedResourceCount objects.
              - *(dict) --* 
                The count of resources that are grouped by the group name.
                - **GroupName** *(string) --* 
                  The name of the group that can be region, account ID, or resource type. For example, region1, region2 if the region was chosen as ``GroupByKey`` .
                - **ResourceCount** *(integer) --* 
                  The number of resources in the group.
            - **NextToken** *(string) --* 
              The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type Filters: dict
        :param Filters:
          Filters the results based on the ``ResourceCountFilters`` object.
          - **ResourceType** *(string) --*
            The type of the AWS resource.
          - **AccountId** *(string) --*
            The 12-digit ID of the account.
          - **Region** *(string) --*
            The region where the account is located.
        :type GroupByKey: string
        :param GroupByKey:
          The key to group the resource counts.
        :type Limit: integer
        :param Limit:
          The maximum number of  GroupedResourceCount objects returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def get_aggregate_resource_config(self, ConfigurationAggregatorName: str, ResourceIdentifier: Dict) -> Dict:
        """
        Returns configuration item that is aggregated for your specific resource in a specific source account and region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetAggregateResourceConfig>`_
        
        **Request Syntax**
        ::
          response = client.get_aggregate_resource_config(
              ConfigurationAggregatorName='string',
              ResourceIdentifier={
                  'SourceAccountId': 'string',
                  'SourceRegion': 'string',
                  'ResourceId': 'string',
                  'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                  'ResourceName': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ConfigurationItem': {
                    'version': 'string',
                    'accountId': 'string',
                    'configurationItemCaptureTime': datetime(2015, 1, 1),
                    'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
                    'configurationStateId': 'string',
                    'configurationItemMD5Hash': 'string',
                    'arn': 'string',
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                    'resourceId': 'string',
                    'resourceName': 'string',
                    'awsRegion': 'string',
                    'availabilityZone': 'string',
                    'resourceCreationTime': datetime(2015, 1, 1),
                    'tags': {
                        'string': 'string'
                    },
                    'relatedEvents': [
                        'string',
                    ],
                    'relationships': [
                        {
                            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                            'resourceId': 'string',
                            'resourceName': 'string',
                            'relationshipName': 'string'
                        },
                    ],
                    'configuration': 'string',
                    'supplementaryConfiguration': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConfigurationItem** *(dict) --* 
              Returns a ``ConfigurationItem`` object.
              - **version** *(string) --* 
                The version number of the resource configuration.
              - **accountId** *(string) --* 
                The 12-digit AWS account ID associated with the resource.
              - **configurationItemCaptureTime** *(datetime) --* 
                The time when the configuration recording was initiated.
              - **configurationItemStatus** *(string) --* 
                The configuration item status.
              - **configurationStateId** *(string) --* 
                An identifier that indicates the ordering of the configuration items of a resource.
              - **configurationItemMD5Hash** *(string) --* 
                Unique MD5 hash that represents the configuration item's state.
                You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.
              - **arn** *(string) --* 
                accoun
              - **resourceType** *(string) --* 
                The type of AWS resource.
              - **resourceId** *(string) --* 
                The ID of the resource (for example, ``sg-xxxxxx`` ).
              - **resourceName** *(string) --* 
                The custom name of the resource, if available.
              - **awsRegion** *(string) --* 
                The region where the resource resides.
              - **availabilityZone** *(string) --* 
                The Availability Zone associated with the resource.
              - **resourceCreationTime** *(datetime) --* 
                The time stamp when the resource was created.
              - **tags** *(dict) --* 
                A mapping of key value tags associated with the resource.
                - *(string) --* 
                  - *(string) --* 
              - **relatedEvents** *(list) --* 
                A list of CloudTrail event IDs.
                A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__ .
                An empty field indicates that the current configuration was not initiated by any event.
                - *(string) --* 
              - **relationships** *(list) --* 
                A list of related AWS resources.
                - *(dict) --* 
                  The relationship of the related resource to the main resource.
                  - **resourceType** *(string) --* 
                    The resource type of the related resource.
                  - **resourceId** *(string) --* 
                    The ID of the related resource (for example, ``sg-xxxxxx`` ).
                  - **resourceName** *(string) --* 
                    The custom name of the related resource, if available.
                  - **relationshipName** *(string) --* 
                    The type of relationship with the related resource.
              - **configuration** *(string) --* 
                The description of the resource configuration.
              - **supplementaryConfiguration** *(dict) --* 
                Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the ``configuration`` parameter.
                - *(string) --* 
                  - *(string) --* 
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type ResourceIdentifier: dict
        :param ResourceIdentifier: **[REQUIRED]**
          An object that identifies aggregate resource.
          - **SourceAccountId** *(string) --* **[REQUIRED]**
            The 12-digit account ID of the source account.
          - **SourceRegion** *(string) --* **[REQUIRED]**
            The source region where data is aggregated.
          - **ResourceId** *(string) --* **[REQUIRED]**
            The ID of the AWS resource.
          - **ResourceType** *(string) --* **[REQUIRED]**
            The type of the AWS resource.
          - **ResourceName** *(string) --*
            The name of the AWS resource.
        :rtype: dict
        :returns:
        """
        pass

    def get_compliance_details_by_config_rule(self, ConfigRuleName: str, ComplianceTypes: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Returns the evaluation results for the specified AWS Config rule. The results indicate which AWS resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByConfigRule>`_
        
        **Request Syntax**
        ::
          response = client.get_compliance_details_by_config_rule(
              ConfigRuleName='string',
              ComplianceTypes=[
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              ],
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'EvaluationResults': [
                    {
                        'EvaluationResultIdentifier': {
                            'EvaluationResultQualifier': {
                                'ConfigRuleName': 'string',
                                'ResourceType': 'string',
                                'ResourceId': 'string'
                            },
                            'OrderingTimestamp': datetime(2015, 1, 1)
                        },
                        'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                        'ResultRecordedTime': datetime(2015, 1, 1),
                        'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                        'Annotation': 'string',
                        'ResultToken': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EvaluationResults** *(list) --* 
              Indicates whether the AWS resource complies with the specified AWS Config rule.
              - *(dict) --* 
                The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.
                - **EvaluationResultIdentifier** *(dict) --* 
                  Uniquely identifies the evaluation result.
                  - **EvaluationResultQualifier** *(dict) --* 
                    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.
                    - **ConfigRuleName** *(string) --* 
                      The name of the AWS Config rule that was used in the evaluation.
                    - **ResourceType** *(string) --* 
                      The type of AWS resource that was evaluated.
                    - **ResourceId** *(string) --* 
                      The ID of the evaluated AWS resource.
                  - **OrderingTimestamp** *(datetime) --* 
                    The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.
                - **ComplianceType** *(string) --* 
                  Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.
                  For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.
                - **ResultRecordedTime** *(datetime) --* 
                  The time when AWS Config recorded the evaluation result.
                - **ConfigRuleInvokedTime** *(datetime) --* 
                  The time when the AWS Config rule evaluated the AWS resource.
                - **Annotation** *(string) --* 
                  Supplementary information about how the evaluation determined the compliance.
                - **ResultToken** *(string) --* 
                  An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.
            - **NextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**
          The name of the AWS Config rule for which you want compliance information.
        :type ComplianceTypes: list
        :param ComplianceTypes:
          Filters the results by compliance.
          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .
          - *(string) --*
        :type Limit: integer
        :param Limit:
          The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def get_compliance_details_by_resource(self, ResourceType: str, ResourceId: str, ComplianceTypes: List = None, NextToken: str = None) -> Dict:
        """
        Returns the evaluation results for the specified AWS resource. The results indicate which AWS Config rules were used to evaluate the resource, when each rule was last used, and whether the resource complies with each rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByResource>`_
        
        **Request Syntax**
        ::
          response = client.get_compliance_details_by_resource(
              ResourceType='string',
              ResourceId='string',
              ComplianceTypes=[
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              ],
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'EvaluationResults': [
                    {
                        'EvaluationResultIdentifier': {
                            'EvaluationResultQualifier': {
                                'ConfigRuleName': 'string',
                                'ResourceType': 'string',
                                'ResourceId': 'string'
                            },
                            'OrderingTimestamp': datetime(2015, 1, 1)
                        },
                        'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                        'ResultRecordedTime': datetime(2015, 1, 1),
                        'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                        'Annotation': 'string',
                        'ResultToken': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EvaluationResults** *(list) --* 
              Indicates whether the specified AWS resource complies each AWS Config rule.
              - *(dict) --* 
                The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.
                - **EvaluationResultIdentifier** *(dict) --* 
                  Uniquely identifies the evaluation result.
                  - **EvaluationResultQualifier** *(dict) --* 
                    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.
                    - **ConfigRuleName** *(string) --* 
                      The name of the AWS Config rule that was used in the evaluation.
                    - **ResourceType** *(string) --* 
                      The type of AWS resource that was evaluated.
                    - **ResourceId** *(string) --* 
                      The ID of the evaluated AWS resource.
                  - **OrderingTimestamp** *(datetime) --* 
                    The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.
                - **ComplianceType** *(string) --* 
                  Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.
                  For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.
                - **ResultRecordedTime** *(datetime) --* 
                  The time when AWS Config recorded the evaluation result.
                - **ConfigRuleInvokedTime** *(datetime) --* 
                  The time when the AWS Config rule evaluated the AWS resource.
                - **Annotation** *(string) --* 
                  Supplementary information about how the evaluation determined the compliance.
                - **ResultToken** *(string) --* 
                  An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.
            - **NextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]**
          The type of the AWS resource for which you want compliance information.
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The ID of the AWS resource for which you want compliance information.
        :type ComplianceTypes: list
        :param ComplianceTypes:
          Filters the results by compliance.
          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def get_compliance_summary_by_config_rule(self) -> Dict:
        """
        Returns the number of AWS Config rules that are compliant and noncompliant, up to a maximum of 25 for each.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceSummaryByConfigRule>`_
        
        **Request Syntax**
        ::
          response = client.get_compliance_summary_by_config_rule()
        
        **Response Syntax**
        ::
            {
                'ComplianceSummary': {
                    'CompliantResourceCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    },
                    'NonCompliantResourceCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    },
                    'ComplianceSummaryTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ComplianceSummary** *(dict) --* 
              The number of AWS Config rules that are compliant and the number that are noncompliant, up to a maximum of 25 for each.
              - **CompliantResourceCount** *(dict) --* 
                The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.
                - **CappedCount** *(integer) --* 
                  The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                - **CapExceeded** *(boolean) --* 
                  Indicates whether the maximum count is reached.
              - **NonCompliantResourceCount** *(dict) --* 
                The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.
                - **CappedCount** *(integer) --* 
                  The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                - **CapExceeded** *(boolean) --* 
                  Indicates whether the maximum count is reached.
              - **ComplianceSummaryTimestamp** *(datetime) --* 
                The time that AWS Config created the compliance summary.
        :rtype: dict
        :returns:
        """
        pass

    def get_compliance_summary_by_resource_type(self, ResourceTypes: List = None) -> Dict:
        """
        Returns the number of resources that are compliant and the number that are noncompliant. You can specify one or more resource types to get these numbers for each resource type. The maximum number returned is 100.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceSummaryByResourceType>`_
        
        **Request Syntax**
        ::
          response = client.get_compliance_summary_by_resource_type(
              ResourceTypes=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ComplianceSummariesByResourceType': [
                    {
                        'ResourceType': 'string',
                        'ComplianceSummary': {
                            'CompliantResourceCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            },
                            'NonCompliantResourceCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            },
                            'ComplianceSummaryTimestamp': datetime(2015, 1, 1)
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ComplianceSummariesByResourceType** *(list) --* 
              The number of resources that are compliant and the number that are noncompliant. If one or more resource types were provided with the request, the numbers are returned for each resource type. The maximum number returned is 100.
              - *(dict) --* 
                The number of AWS resources of a specific type that are compliant or noncompliant, up to a maximum of 100 for each.
                - **ResourceType** *(string) --* 
                  The type of AWS resource.
                - **ComplianceSummary** *(dict) --* 
                  The number of AWS resources that are compliant or noncompliant, up to a maximum of 100 for each.
                  - **CompliantResourceCount** *(dict) --* 
                    The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.
                    - **CappedCount** *(integer) --* 
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                    - **CapExceeded** *(boolean) --* 
                      Indicates whether the maximum count is reached.
                  - **NonCompliantResourceCount** *(dict) --* 
                    The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.
                    - **CappedCount** *(integer) --* 
                      The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
                    - **CapExceeded** *(boolean) --* 
                      Indicates whether the maximum count is reached.
                  - **ComplianceSummaryTimestamp** *(datetime) --* 
                    The time that AWS Config created the compliance summary.
        :type ResourceTypes: list
        :param ResourceTypes:
          Specify one or more resource types to get the number of resources that are compliant and the number that are noncompliant for each resource type.
          For this request, you can specify an AWS resource type such as ``AWS::EC2::Instance`` . You can specify that the resource type is an AWS account by specifying ``AWS::::Account`` .
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def get_discovered_resource_counts(self, resourceTypes: List = None, limit: int = None, nextToken: str = None) -> Dict:
        """
        Returns the resource types, the number of each resource type, and the total number of resources that AWS Config is recording in this region for your AWS account. 
        
        **Example**
        * AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets. 
        * You make a call to the ``GetDiscoveredResourceCounts`` action and specify that you want all resource types.  
        * AWS Config returns the following: 
          * The resource types (EC2 instances, IAM users, and S3 buckets). 
          * The number of each resource type (25, 20, and 15). 
          * The total number of all resources (60). 
        The response is paginated. By default, AWS Config lists 100  ResourceCount objects on each page. You can customize this number with the ``limit`` parameter. The response includes a ``nextToken`` string. To get the next page of results, run the request again and specify the string for the ``nextToken`` parameter.
        .. note::
          If you make a call to the  GetDiscoveredResourceCounts action, you might not immediately receive resource counts in the following situations:
          * You are a new AWS Config customer. 
          * You just enabled resource recording. 
          It might take a few minutes for AWS Config to record and count your resources. Wait a few minutes and then retry the  GetDiscoveredResourceCounts action. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetDiscoveredResourceCounts>`_
        
        **Request Syntax**
        ::
          response = client.get_discovered_resource_counts(
              resourceTypes=[
                  'string',
              ],
              limit=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'totalDiscoveredResources': 123,
                'resourceCounts': [
                    {
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'count': 123
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **totalDiscoveredResources** *(integer) --* 
              The total number of resources that AWS Config is recording in the region for your account. If you specify resource types in the request, AWS Config returns only the total number of resources for those resource types.
        
        **Example**
              * AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets, for a total of 60 resources. 
              * You make a call to the ``GetDiscoveredResourceCounts`` action and specify the resource type, ``"AWS::EC2::Instances"`` , in the request. 
              * AWS Config returns 25 for ``totalDiscoveredResources`` . 
            - **resourceCounts** *(list) --* 
              The list of ``ResourceCount`` objects. Each object is listed in descending order by the number of resources.
              - *(dict) --* 
                An object that contains the resource type and the number of resources.
                - **resourceType** *(string) --* 
                  The resource type (for example, ``"AWS::EC2::Instance"`` ).
                - **count** *(integer) --* 
                  The number of resources.
            - **nextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type resourceTypes: list
        :param resourceTypes:
          The comma-separated list that specifies the resource types that you want AWS Config to return (for example, ``\"AWS::EC2::Instance\"`` , ``\"AWS::IAM::User\"`` ).
          If a value for ``resourceTypes`` is not specified, AWS Config returns all resource types that AWS Config is recording in the region for your account.
          .. note::
            If the configuration recorder is turned off, AWS Config returns an empty list of  ResourceCount objects. If the configuration recorder is not recording a specific resource type (for example, S3 buckets), that resource type is not returned in the list of  ResourceCount objects.
          - *(string) --*
        :type limit: integer
        :param limit:
          The maximum number of  ResourceCount objects returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
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

    def get_resource_config_history(self, resourceType: str, resourceId: str, laterTime: datetime = None, earlierTime: datetime = None, chronologicalOrder: str = None, limit: int = None, nextToken: str = None) -> Dict:
        """
        Returns a list of configuration items for the specified resource. The list contains details about each state of the resource during the specified time interval. If you specified a retention period to retain your ``ConfigurationItems`` between a minimum of 30 days and a maximum of 7 years (2557 days), AWS Config returns the ``ConfigurationItems`` for the specified retention period. 
        The response is paginated. By default, AWS Config returns a limit of 10 configuration items per page. You can customize this number with the ``limit`` parameter. The response includes a ``nextToken`` string. To get the next page of results, run the request again and specify the string for the ``nextToken`` parameter.
        .. note::
          Each call to the API is limited to span a duration of seven days. It is likely that the number of records returned is smaller than the specified ``limit`` . In such cases, you can make another call, using the ``nextToken`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetResourceConfigHistory>`_
        
        **Request Syntax**
        ::
          response = client.get_resource_config_history(
              resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
              resourceId='string',
              laterTime=datetime(2015, 1, 1),
              earlierTime=datetime(2015, 1, 1),
              chronologicalOrder='Reverse'|'Forward',
              limit=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'configurationItems': [
                    {
                        'version': 'string',
                        'accountId': 'string',
                        'configurationItemCaptureTime': datetime(2015, 1, 1),
                        'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
                        'configurationStateId': 'string',
                        'configurationItemMD5Hash': 'string',
                        'arn': 'string',
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'resourceId': 'string',
                        'resourceName': 'string',
                        'awsRegion': 'string',
                        'availabilityZone': 'string',
                        'resourceCreationTime': datetime(2015, 1, 1),
                        'tags': {
                            'string': 'string'
                        },
                        'relatedEvents': [
                            'string',
                        ],
                        'relationships': [
                            {
                                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                                'resourceId': 'string',
                                'resourceName': 'string',
                                'relationshipName': 'string'
                            },
                        ],
                        'configuration': 'string',
                        'supplementaryConfiguration': {
                            'string': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  GetResourceConfigHistory action.
            - **configurationItems** *(list) --* 
              A list that contains the configuration history of one or more resources.
              - *(dict) --* 
                A list that contains detailed configurations of a specified resource.
                - **version** *(string) --* 
                  The version number of the resource configuration.
                - **accountId** *(string) --* 
                  The 12-digit AWS account ID associated with the resource.
                - **configurationItemCaptureTime** *(datetime) --* 
                  The time when the configuration recording was initiated.
                - **configurationItemStatus** *(string) --* 
                  The configuration item status.
                - **configurationStateId** *(string) --* 
                  An identifier that indicates the ordering of the configuration items of a resource.
                - **configurationItemMD5Hash** *(string) --* 
                  Unique MD5 hash that represents the configuration item's state.
                  You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.
                - **arn** *(string) --* 
                  accoun
                - **resourceType** *(string) --* 
                  The type of AWS resource.
                - **resourceId** *(string) --* 
                  The ID of the resource (for example, ``sg-xxxxxx`` ).
                - **resourceName** *(string) --* 
                  The custom name of the resource, if available.
                - **awsRegion** *(string) --* 
                  The region where the resource resides.
                - **availabilityZone** *(string) --* 
                  The Availability Zone associated with the resource.
                - **resourceCreationTime** *(datetime) --* 
                  The time stamp when the resource was created.
                - **tags** *(dict) --* 
                  A mapping of key value tags associated with the resource.
                  - *(string) --* 
                    - *(string) --* 
                - **relatedEvents** *(list) --* 
                  A list of CloudTrail event IDs.
                  A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__ .
                  An empty field indicates that the current configuration was not initiated by any event.
                  - *(string) --* 
                - **relationships** *(list) --* 
                  A list of related AWS resources.
                  - *(dict) --* 
                    The relationship of the related resource to the main resource.
                    - **resourceType** *(string) --* 
                      The resource type of the related resource.
                    - **resourceId** *(string) --* 
                      The ID of the related resource (for example, ``sg-xxxxxx`` ).
                    - **resourceName** *(string) --* 
                      The custom name of the related resource, if available.
                    - **relationshipName** *(string) --* 
                      The type of relationship with the related resource.
                - **configuration** *(string) --* 
                  The description of the resource configuration.
                - **supplementaryConfiguration** *(dict) --* 
                  Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the ``configuration`` parameter.
                  - *(string) --* 
                    - *(string) --* 
            - **nextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type resourceType: string
        :param resourceType: **[REQUIRED]**
          The resource type.
        :type resourceId: string
        :param resourceId: **[REQUIRED]**
          The ID of the resource (for example., ``sg-xxxxxx`` ).
        :type laterTime: datetime
        :param laterTime:
          The time stamp that indicates a later time. If not specified, current time is taken.
        :type earlierTime: datetime
        :param earlierTime:
          The time stamp that indicates an earlier time. If not specified, the action returns paginated results that contain configuration items that start when the first configuration item was recorded.
        :type chronologicalOrder: string
        :param chronologicalOrder:
          The chronological order for configuration items listed. By default, the results are listed in reverse chronological order.
        :type limit: integer
        :param limit:
          The maximum number of configuration items returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
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

    def list_aggregate_discovered_resources(self, ConfigurationAggregatorName: str, ResourceType: str, Filters: Dict = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Accepts a resource type and returns a list of resource identifiers that are aggregated for a specific resource type across accounts and regions. A resource identifier includes the resource type, ID, (if available) the custom resource name, source account, and source region. You can narrow the results to include only resources that have specific resource IDs, or a resource name, or source account ID, or source region.
        For example, if the input consists of accountID 12345678910 and the region is us-east-1 for resource type ``AWS::EC2::Instance`` then the API returns all the EC2 instance identifiers of accountID 12345678910 and region us-east-1.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/ListAggregateDiscoveredResources>`_
        
        **Request Syntax**
        ::
          response = client.list_aggregate_discovered_resources(
              ConfigurationAggregatorName='string',
              ResourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
              Filters={
                  'AccountId': 'string',
                  'ResourceId': 'string',
                  'ResourceName': 'string',
                  'Region': 'string'
              },
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ResourceIdentifiers': [
                    {
                        'SourceAccountId': 'string',
                        'SourceRegion': 'string',
                        'ResourceId': 'string',
                        'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'ResourceName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourceIdentifiers** *(list) --* 
              Returns a list of ``ResourceIdentifiers`` objects.
              - *(dict) --* 
                The details that identify a resource that is collected by AWS Config aggregator, including the resource type, ID, (if available) the custom resource name, the source account, and source region.
                - **SourceAccountId** *(string) --* 
                  The 12-digit account ID of the source account.
                - **SourceRegion** *(string) --* 
                  The source region where data is aggregated.
                - **ResourceId** *(string) --* 
                  The ID of the AWS resource.
                - **ResourceType** *(string) --* 
                  The type of the AWS resource.
                - **ResourceName** *(string) --* 
                  The name of the AWS resource.
            - **NextToken** *(string) --* 
              The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]**
          The type of resources that you want AWS Config to list in the response.
        :type Filters: dict
        :param Filters:
          Filters the results based on the ``ResourceFilters`` object.
          - **AccountId** *(string) --*
            The 12-digit source account ID.
          - **ResourceId** *(string) --*
            The ID of the resource.
          - **ResourceName** *(string) --*
            The name of the resource.
          - **Region** *(string) --*
            The source region.
        :type Limit: integer
        :param Limit:
          The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def list_discovered_resources(self, resourceType: str, resourceIds: List = None, resourceName: str = None, limit: int = None, includeDeletedResources: bool = None, nextToken: str = None) -> Dict:
        """
        Accepts a resource type and returns a list of resource identifiers for the resources of that type. A resource identifier includes the resource type, ID, and (if available) the custom resource name. The results consist of resources that AWS Config has discovered, including those that AWS Config is not currently recording. You can narrow the results to include only resources that have specific resource IDs or a resource name.
        .. note::
          You can specify either resource IDs or a resource name, but not both, in the same request.
        The response is paginated. By default, AWS Config lists 100 resource identifiers on each page. You can customize this number with the ``limit`` parameter. The response includes a ``nextToken`` string. To get the next page of results, run the request again and specify the string for the ``nextToken`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/ListDiscoveredResources>`_
        
        **Request Syntax**
        ::
          response = client.list_discovered_resources(
              resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
              resourceIds=[
                  'string',
              ],
              resourceName='string',
              limit=123,
              includeDeletedResources=True|False,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'resourceIdentifiers': [
                    {
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'resourceId': 'string',
                        'resourceName': 'string',
                        'resourceDeletionTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **resourceIdentifiers** *(list) --* 
              The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.
              - *(dict) --* 
                The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.
                - **resourceType** *(string) --* 
                  The type of resource.
                - **resourceId** *(string) --* 
                  The ID of the resource (for example, ``sg-xxxxxx`` ).
                - **resourceName** *(string) --* 
                  The custom name of the resource (if available).
                - **resourceDeletionTime** *(datetime) --* 
                  The time that the resource was deleted.
            - **nextToken** *(string) --* 
              The string that you use in a subsequent request to get the next page of results in a paginated response.
        :type resourceType: string
        :param resourceType: **[REQUIRED]**
          The type of resources that you want AWS Config to list in the response.
        :type resourceIds: list
        :param resourceIds:
          The IDs of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.
          - *(string) --*
        :type resourceName: string
        :param resourceName:
          The custom name of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.
        :type limit: integer
        :param limit:
          The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
        :type includeDeletedResources: boolean
        :param includeDeletedResources:
          Specifies whether AWS Config includes deleted resources in the results. By default, deleted resources are not included.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str, Limit: int = None, NextToken: str = None) -> Dict:
        """
        List the tags for AWS Config resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              ResourceArn='string',
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tags** *(list) --* 
              The tags for the resource.
              - *(dict) --* 
                The tags for the resource. The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - **Key** *(string) --* 
                  One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
                - **Value** *(string) --* 
                  The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            - **NextToken** *(string) --* 
              The nextToken string returned on a previous page that you use to get the next page of results in a paginated response. 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are ``ConfigRule`` , ``ConfigurationAggregator`` and ``AggregatorAuthorization`` .
        :type Limit: integer
        :param Limit:
          The maximum number of tags returned on each page. The limit maximum is 50. You cannot specify a number greater than 50. If you specify 0, AWS Config uses the default.
        :type NextToken: string
        :param NextToken:
          The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def put_aggregation_authorization(self, AuthorizedAccountId: str, AuthorizedAwsRegion: str) -> Dict:
        """
        Authorizes the aggregator account and region to collect data from the source account and region. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutAggregationAuthorization>`_
        
        **Request Syntax**
        ::
          response = client.put_aggregation_authorization(
              AuthorizedAccountId='string',
              AuthorizedAwsRegion='string'
          )
        
        **Response Syntax**
        ::
            {
                'AggregationAuthorization': {
                    'AggregationAuthorizationArn': 'string',
                    'AuthorizedAccountId': 'string',
                    'AuthorizedAwsRegion': 'string',
                    'CreationTime': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AggregationAuthorization** *(dict) --* 
              Returns an AggregationAuthorization object. 
              - **AggregationAuthorizationArn** *(string) --* 
                The Amazon Resource Name (ARN) of the aggregation object.
              - **AuthorizedAccountId** *(string) --* 
                The 12-digit account ID of the account authorized to aggregate data.
              - **AuthorizedAwsRegion** *(string) --* 
                The region authorized to collect aggregated data.
              - **CreationTime** *(datetime) --* 
                The time stamp when the aggregation authorization was created.
        :type AuthorizedAccountId: string
        :param AuthorizedAccountId: **[REQUIRED]**
          The 12-digit account ID of the account authorized to aggregate data.
        :type AuthorizedAwsRegion: string
        :param AuthorizedAwsRegion: **[REQUIRED]**
          The region authorized to collect aggregated data.
        :rtype: dict
        :returns:
        """
        pass

    def put_config_rule(self, ConfigRule: Dict):
        """
        Adds or updates an AWS Config rule for evaluating whether your AWS resources comply with your desired configurations.
        You can use this action for custom AWS Config rules and AWS managed Config rules. A custom AWS Config rule is a rule that you develop and maintain. An AWS managed Config rule is a customizable, predefined rule that AWS Config provides.
        If you are adding a new custom AWS Config rule, you must first create the AWS Lambda function that the rule invokes to evaluate your resources. When you use the ``PutConfigRule`` action to add the rule to AWS Config, you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function. Specify the ARN for the ``SourceIdentifier`` key. This key is part of the ``Source`` object, which is part of the ``ConfigRule`` object. 
        If you are adding an AWS managed Config rule, specify the rule's identifier for the ``SourceIdentifier`` key. To reference AWS managed Config rule identifiers, see `About AWS Managed Config Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__ .
        For any new rule that you add, specify the ``ConfigRuleName`` in the ``ConfigRule`` object. Do not specify the ``ConfigRuleArn`` or the ``ConfigRuleId`` . These values are generated by AWS Config for new rules.
        If you are updating a rule that you added previously, you can specify the rule by ``ConfigRuleName`` , ``ConfigRuleId`` , or ``ConfigRuleArn`` in the ``ConfigRule`` data type that you use in this request.
        The maximum number of rules that AWS Config supports is 150.
        For information about requesting a rule limit increase, see `AWS Config Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config>`__ in the *AWS General Reference Guide* .
        For more information about developing and using AWS Config rules, see `Evaluating AWS Resource Configurations with AWS Config <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the *AWS Config Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutConfigRule>`_
        
        **Request Syntax**
        ::
          response = client.put_config_rule(
              ConfigRule={
                  'ConfigRuleName': 'string',
                  'ConfigRuleArn': 'string',
                  'ConfigRuleId': 'string',
                  'Description': 'string',
                  'Scope': {
                      'ComplianceResourceTypes': [
                          'string',
                      ],
                      'TagKey': 'string',
                      'TagValue': 'string',
                      'ComplianceResourceId': 'string'
                  },
                  'Source': {
                      'Owner': 'CUSTOM_LAMBDA'|'AWS',
                      'SourceIdentifier': 'string',
                      'SourceDetails': [
                          {
                              'EventSource': 'aws.config',
                              'MessageType': 'ConfigurationItemChangeNotification'|'ConfigurationSnapshotDeliveryCompleted'|'ScheduledNotification'|'OversizedConfigurationItemChangeNotification',
                              'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                          },
                      ]
                  },
                  'InputParameters': 'string',
                  'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                  'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING',
                  'CreatedBy': 'string'
              }
          )
        :type ConfigRule: dict
        :param ConfigRule: **[REQUIRED]**
          The rule that you want to add to your account.
          - **ConfigRuleName** *(string) --*
            The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.
          - **ConfigRuleArn** *(string) --*
            The Amazon Resource Name (ARN) of the AWS Config rule.
          - **ConfigRuleId** *(string) --*
            The ID of the AWS Config rule.
          - **Description** *(string) --*
            The description that you provide for the AWS Config rule.
          - **Scope** *(dict) --*
            Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
            - **ComplianceResourceTypes** *(list) --*
              The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .
              - *(string) --*
            - **TagKey** *(string) --*
              The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
            - **TagValue** *(string) --*
              The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .
            - **ComplianceResourceId** *(string) --*
              The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .
          - **Source** *(dict) --* **[REQUIRED]**
            Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
            - **Owner** *(string) --* **[REQUIRED]**
              Indicates whether AWS or the customer owns and manages the AWS Config rule.
            - **SourceIdentifier** *(string) --* **[REQUIRED]**
              For AWS Config managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Managed Config Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__ .
              For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule\'s AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .
            - **SourceDetails** *(list) --*
              Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.
              - *(dict) --*
                Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for ``SourceDetail`` only for custom rules.
                - **EventSource** *(string) --*
                  The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.
                - **MessageType** *(string) --*
                  The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
                  * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
                  * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
                  * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` .
                  * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.
                  If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for ``OversizedConfigurationItemChangeNotification`` .
                - **MaximumExecutionFrequency** *(string) --*
                  The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value.
                  .. note::
                    By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
                    Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once every three hours. In this case, ``Three_Hours`` is the frequency of this rule.
          - **InputParameters** *(string) --*
            A string, in JSON format, that is passed to the AWS Config rule Lambda function.
          - **MaximumExecutionFrequency** *(string) --*
            The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when:
            * You are using an AWS managed rule that is triggered at a periodic frequency.
            * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .
            .. note::
              By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
          - **ConfigRuleState** *(string) --*
            Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the AWS Config rule.
            AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the ``StartConfigRulesEvaluation`` request to evaluate your resources against the AWS Config rule.
            AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use the ``DeleteEvaluationResults`` request to delete the current evaluation results for the AWS Config rule.
            AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.
          - **CreatedBy** *(string) --*
            Service principal name of the service that created the rule.
            .. note::
              The field is populated only if the service linked rule is created by a service. The field is empty if you create your own rule.
        :returns: None
        """
        pass

    def put_configuration_aggregator(self, ConfigurationAggregatorName: str, AccountAggregationSources: List = None, OrganizationAggregationSource: Dict = None) -> Dict:
        """
        Creates and updates the configuration aggregator with the selected source accounts and regions. The source account can be individual account(s) or an organization.
        .. note::
          AWS Config should be enabled in source accounts and regions you want to aggregate.
          If your source type is an organization, you must be signed in to the master account and all features must be enabled in your organization. AWS Config calls ``EnableAwsServiceAccess`` API to enable integration between AWS Config and AWS Organizations. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutConfigurationAggregator>`_
        
        **Request Syntax**
        ::
          response = client.put_configuration_aggregator(
              ConfigurationAggregatorName='string',
              AccountAggregationSources=[
                  {
                      'AccountIds': [
                          'string',
                      ],
                      'AllAwsRegions': True|False,
                      'AwsRegions': [
                          'string',
                      ]
                  },
              ],
              OrganizationAggregationSource={
                  'RoleArn': 'string',
                  'AwsRegions': [
                      'string',
                  ],
                  'AllAwsRegions': True|False
              }
          )
        
        **Response Syntax**
        ::
            {
                'ConfigurationAggregator': {
                    'ConfigurationAggregatorName': 'string',
                    'ConfigurationAggregatorArn': 'string',
                    'AccountAggregationSources': [
                        {
                            'AccountIds': [
                                'string',
                            ],
                            'AllAwsRegions': True|False,
                            'AwsRegions': [
                                'string',
                            ]
                        },
                    ],
                    'OrganizationAggregationSource': {
                        'RoleArn': 'string',
                        'AwsRegions': [
                            'string',
                        ],
                        'AllAwsRegions': True|False
                    },
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdatedTime': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConfigurationAggregator** *(dict) --* 
              Returns a ConfigurationAggregator object.
              - **ConfigurationAggregatorName** *(string) --* 
                The name of the aggregator.
              - **ConfigurationAggregatorArn** *(string) --* 
                The Amazon Resource Name (ARN) of the aggregator.
              - **AccountAggregationSources** *(list) --* 
                Provides a list of source accounts and regions to be aggregated.
                - *(dict) --* 
                  A collection of accounts and regions.
                  - **AccountIds** *(list) --* 
                    The 12-digit account ID of the account being aggregated. 
                    - *(string) --* 
                  - **AllAwsRegions** *(boolean) --* 
                    If true, aggregate existing AWS Config regions and future regions.
                  - **AwsRegions** *(list) --* 
                    The source regions being aggregated.
                    - *(string) --* 
              - **OrganizationAggregationSource** *(dict) --* 
                Provides an organization and list of regions to be aggregated.
                - **RoleArn** *(string) --* 
                  ARN of the IAM role used to retreive AWS Organization details associated with the aggregator account.
                - **AwsRegions** *(list) --* 
                  The source regions being aggregated.
                  - *(string) --* 
                - **AllAwsRegions** *(boolean) --* 
                  If true, aggregate existing AWS Config regions and future regions.
              - **CreationTime** *(datetime) --* 
                The time stamp when the configuration aggregator was created.
              - **LastUpdatedTime** *(datetime) --* 
                The time of the last update.
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**
          The name of the configuration aggregator.
        :type AccountAggregationSources: list
        :param AccountAggregationSources:
          A list of AccountAggregationSource object.
          - *(dict) --*
            A collection of accounts and regions.
            - **AccountIds** *(list) --* **[REQUIRED]**
              The 12-digit account ID of the account being aggregated.
              - *(string) --*
            - **AllAwsRegions** *(boolean) --*
              If true, aggregate existing AWS Config regions and future regions.
            - **AwsRegions** *(list) --*
              The source regions being aggregated.
              - *(string) --*
        :type OrganizationAggregationSource: dict
        :param OrganizationAggregationSource:
          An OrganizationAggregationSource object.
          - **RoleArn** *(string) --* **[REQUIRED]**
            ARN of the IAM role used to retreive AWS Organization details associated with the aggregator account.
          - **AwsRegions** *(list) --*
            The source regions being aggregated.
            - *(string) --*
          - **AllAwsRegions** *(boolean) --*
            If true, aggregate existing AWS Config regions and future regions.
        :rtype: dict
        :returns:
        """
        pass

    def put_configuration_recorder(self, ConfigurationRecorder: Dict):
        """
        Creates a new configuration recorder to record the selected resource configurations.
        You can use this action to change the role ``roleARN`` or the ``recordingGroup`` of an existing recorder. To change the role, call the action on the existing configuration recorder and specify a role.
        .. note::
          Currently, you can specify only one configuration recorder per region in your account.
          If ``ConfigurationRecorder`` does not have the **recordingGroup** parameter specified, the default is to record all supported resource types.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutConfigurationRecorder>`_
        
        **Request Syntax**
        ::
          response = client.put_configuration_recorder(
              ConfigurationRecorder={
                  'name': 'string',
                  'roleARN': 'string',
                  'recordingGroup': {
                      'allSupported': True|False,
                      'includeGlobalResourceTypes': True|False,
                      'resourceTypes': [
                          'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                      ]
                  }
              }
          )
        :type ConfigurationRecorder: dict
        :param ConfigurationRecorder: **[REQUIRED]**
          The configuration recorder object that records each configuration change made to the resources.
          - **name** *(string) --*
            The name of the recorder. By default, AWS Config automatically assigns the name \"default\" when creating the configuration recorder. You cannot change the assigned name.
          - **roleARN** *(string) --*
            Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.
          - **recordingGroup** *(dict) --*
            Specifies the types of AWS resources for which AWS Config records configuration changes.
            - **allSupported** *(boolean) --*
              Specifies whether AWS Config records configuration changes for every supported type of regional resource.
              If you set this option to ``true`` , when AWS Config adds support for a new type of regional resource, it starts recording resources of that type automatically.
              If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .
            - **includeGlobalResourceTypes** *(boolean) --*
              Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.
              Before you can set this option to ``true`` , you must set the ``allSupported`` option to ``true`` .
              If you set this option to ``true`` , when AWS Config adds support for a new type of global resource, it starts recording resources of that type automatically.
              The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.
            - **resourceTypes** *(list) --*
              A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, ``AWS::EC2::Instance`` or ``AWS::CloudTrail::Trail`` ).
              Before you can set this option to ``true`` , you must set the ``allSupported`` option to ``false`` .
              If you set this option to ``true`` , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.
              For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in `Supported AWS Resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__ .
              - *(string) --*
        :returns: None
        """
        pass

    def put_delivery_channel(self, DeliveryChannel: Dict):
        """
        Creates a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic.
        Before you can create a delivery channel, you must create a configuration recorder.
        You can use this action to change the Amazon S3 bucket or an Amazon SNS topic of the existing delivery channel. To change the Amazon S3 bucket or an Amazon SNS topic, call this action and specify the changed values for the S3 bucket and the SNS topic. If you specify a different value for either the S3 bucket or the SNS topic, this action will keep the existing value for the parameter that is not changed.
        .. note::
          You can have only one delivery channel per region in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutDeliveryChannel>`_
        
        **Request Syntax**
        ::
          response = client.put_delivery_channel(
              DeliveryChannel={
                  'name': 'string',
                  's3BucketName': 'string',
                  's3KeyPrefix': 'string',
                  'snsTopicARN': 'string',
                  'configSnapshotDeliveryProperties': {
                      'deliveryFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                  }
              }
          )
        :type DeliveryChannel: dict
        :param DeliveryChannel: **[REQUIRED]**
          The configuration delivery channel object that delivers the configuration information to an Amazon S3 bucket and to an Amazon SNS topic.
          - **name** *(string) --*
            The name of the delivery channel. By default, AWS Config assigns the name \"default\" when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.
          - **s3BucketName** *(string) --*
            The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.
            If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`__ in the AWS Config Developer Guide.
          - **s3KeyPrefix** *(string) --*
            The prefix for the specified Amazon S3 bucket.
          - **snsTopicARN** *(string) --*
            The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.
            If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`__ in the AWS Config Developer Guide.
          - **configSnapshotDeliveryProperties** *(dict) --*
            The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.
            - **deliveryFrequency** *(string) --*
              The frequency with which AWS Config delivers configuration snapshots.
        :returns: None
        """
        pass

    def put_evaluations(self, ResultToken: str, Evaluations: List = None, TestMode: bool = None) -> Dict:
        """
        Used by an AWS Lambda function to deliver evaluation results to AWS Config. This action is required in every AWS Lambda function that is invoked by an AWS Config rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutEvaluations>`_
        
        **Request Syntax**
        ::
          response = client.put_evaluations(
              Evaluations=[
                  {
                      'ComplianceResourceType': 'string',
                      'ComplianceResourceId': 'string',
                      'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                      'Annotation': 'string',
                      'OrderingTimestamp': datetime(2015, 1, 1)
                  },
              ],
              ResultToken='string',
              TestMode=True|False
          )
        
        **Response Syntax**
        ::
            {
                'FailedEvaluations': [
                    {
                        'ComplianceResourceType': 'string',
                        'ComplianceResourceId': 'string',
                        'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                        'Annotation': 'string',
                        'OrderingTimestamp': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedEvaluations** *(list) --* 
              Requests that failed because of a client or server error.
              - *(dict) --* 
                Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.
                - **ComplianceResourceType** *(string) --* 
                  The type of AWS resource that was evaluated.
                - **ComplianceResourceId** *(string) --* 
                  The ID of the AWS resource that was evaluated.
                - **ComplianceType** *(string) --* 
                  Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.
                  For the ``Evaluation`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for this data type.
                  Similarly, AWS Config does not accept ``INSUFFICIENT_DATA`` as the value for ``ComplianceType`` from a ``PutEvaluations`` request. For example, an AWS Lambda function for a custom AWS Config rule cannot pass an ``INSUFFICIENT_DATA`` value to AWS Config.
                - **Annotation** *(string) --* 
                  Supplementary information about how the evaluation determined the compliance.
                - **OrderingTimestamp** *(datetime) --* 
                  The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).
        :type Evaluations: list
        :param Evaluations:
          The assessments that the AWS Lambda function performs. Each evaluation identifies an AWS resource and indicates whether it complies with the AWS Config rule that invokes the AWS Lambda function.
          - *(dict) --*
            Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.
            - **ComplianceResourceType** *(string) --* **[REQUIRED]**
              The type of AWS resource that was evaluated.
            - **ComplianceResourceId** *(string) --* **[REQUIRED]**
              The ID of the AWS resource that was evaluated.
            - **ComplianceType** *(string) --* **[REQUIRED]**
              Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.
              For the ``Evaluation`` data type, AWS Config supports only the ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the ``INSUFFICIENT_DATA`` value for this data type.
              Similarly, AWS Config does not accept ``INSUFFICIENT_DATA`` as the value for ``ComplianceType`` from a ``PutEvaluations`` request. For example, an AWS Lambda function for a custom AWS Config rule cannot pass an ``INSUFFICIENT_DATA`` value to AWS Config.
            - **Annotation** *(string) --*
              Supplementary information about how the evaluation determined the compliance.
            - **OrderingTimestamp** *(datetime) --* **[REQUIRED]**
              The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).
        :type ResultToken: string
        :param ResultToken: **[REQUIRED]**
          An encrypted token that associates an evaluation with an AWS Config rule. Identifies the rule and the event that triggered the evaluation.
        :type TestMode: boolean
        :param TestMode:
          Use this parameter to specify a test run for ``PutEvaluations`` . You can verify whether your AWS Lambda function will deliver evaluation results to AWS Config. No updates occur to your existing evaluations, and evaluation results are not sent to AWS Config.
          .. note::
            When ``TestMode`` is ``true`` , ``PutEvaluations`` doesn\'t require a valid value for the ``ResultToken`` parameter, but the value cannot be null.
        :rtype: dict
        :returns:
        """
        pass

    def put_remediation_configurations(self, RemediationConfigurations: List) -> Dict:
        """
        Adds or updates the remediation configuration with a specific AWS Config rule with the selected target or action. The API creates the ``RemediationConfiguration`` object for the AWS Config rule. The AWS Config rule must already exist for you to add a remediation configuration. The target (SSM document) must exist and have permissions to use the target. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutRemediationConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.put_remediation_configurations(
              RemediationConfigurations=[
                  {
                      'ConfigRuleName': 'string',
                      'TargetType': 'SSM_DOCUMENT',
                      'TargetId': 'string',
                      'TargetVersion': 'string',
                      'Parameters': {
                          'string': {
                              'ResourceValue': {
                                  'Value': 'RESOURCE_ID'
                              },
                              'StaticValue': {
                                  'Values': [
                                      'string',
                                  ]
                              }
                          }
                      },
                      'ResourceType': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedBatches': [
                    {
                        'FailureMessage': 'string',
                        'FailedItems': [
                            {
                                'ConfigRuleName': 'string',
                                'TargetType': 'SSM_DOCUMENT',
                                'TargetId': 'string',
                                'TargetVersion': 'string',
                                'Parameters': {
                                    'string': {
                                        'ResourceValue': {
                                            'Value': 'RESOURCE_ID'
                                        },
                                        'StaticValue': {
                                            'Values': [
                                                'string',
                                            ]
                                        }
                                    }
                                },
                                'ResourceType': 'string'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedBatches** *(list) --* 
              Returns a list of failed remediation batch objects.
              - *(dict) --* 
                List of each of the failed remediations with specific reasons.
                - **FailureMessage** *(string) --* 
                  Returns a failure message. For example, the resource is already compliant.
                - **FailedItems** *(list) --* 
                  Returns remediation configurations of the failed items.
                  - *(dict) --* 
                    An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.
                    - **ConfigRuleName** *(string) --* 
                      The name of the AWS Config rule.
                    - **TargetType** *(string) --* 
                      The type of the target. Target executes remediation. For example, SSM document.
                    - **TargetId** *(string) --* 
                      Target ID is the name of the public document.
                    - **TargetVersion** *(string) --* 
                      Version of the target. For example, version of the SSM document.
                    - **Parameters** *(dict) --* 
                      An object of the RemediationParameterValue.
                      - *(string) --* 
                        - *(dict) --* 
                          The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.
                          - **ResourceValue** *(dict) --* 
                            The value is dynamic and changes at run-time.
                            - **Value** *(string) --* 
                              The value is a resource ID.
                          - **StaticValue** *(dict) --* 
                            The value is static and does not change at run-time.
                            - **Values** *(list) --* 
                              A list of values. For example, the ARN of the assumed role. 
                              - *(string) --* 
                    - **ResourceType** *(string) --* 
                      The type of a resource. 
        :type RemediationConfigurations: list
        :param RemediationConfigurations: **[REQUIRED]**
          A list of remediation configuration objects.
          - *(dict) --*
            An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.
            - **ConfigRuleName** *(string) --* **[REQUIRED]**
              The name of the AWS Config rule.
            - **TargetType** *(string) --* **[REQUIRED]**
              The type of the target. Target executes remediation. For example, SSM document.
            - **TargetId** *(string) --* **[REQUIRED]**
              Target ID is the name of the public document.
            - **TargetVersion** *(string) --*
              Version of the target. For example, version of the SSM document.
            - **Parameters** *(dict) --*
              An object of the RemediationParameterValue.
              - *(string) --*
                - *(dict) --*
                  The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.
                  - **ResourceValue** *(dict) --*
                    The value is dynamic and changes at run-time.
                    - **Value** *(string) --*
                      The value is a resource ID.
                  - **StaticValue** *(dict) --*
                    The value is static and does not change at run-time.
                    - **Values** *(list) --*
                      A list of values. For example, the ARN of the assumed role.
                      - *(string) --*
            - **ResourceType** *(string) --*
              The type of a resource.
        :rtype: dict
        :returns:
        """
        pass

    def put_retention_configuration(self, RetentionPeriodInDays: int) -> Dict:
        """
        Creates and updates the retention configuration with details about retention period (number of days) that AWS Config stores your historical information. The API creates the ``RetentionConfiguration`` object and names the object as **default** . When you have a ``RetentionConfiguration`` object named **default** , calling the API modifies the default object. 
        .. note::
          Currently, AWS Config supports only one retention configuration per region in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutRetentionConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_retention_configuration(
              RetentionPeriodInDays=123
          )
        
        **Response Syntax**
        ::
            {
                'RetentionConfiguration': {
                    'Name': 'string',
                    'RetentionPeriodInDays': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RetentionConfiguration** *(dict) --* 
              Returns a retention configuration object.
              - **Name** *(string) --* 
                The name of the retention configuration object.
              - **RetentionPeriodInDays** *(integer) --* 
                Number of days AWS Config stores your historical information.
                .. note::
                  Currently, only applicable to the configuration item history.
        :type RetentionPeriodInDays: integer
        :param RetentionPeriodInDays: **[REQUIRED]**
          Number of days AWS Config stores your historical information.
          .. note::
            Currently, only applicable to the configuration item history.
        :rtype: dict
        :returns:
        """
        pass

    def select_resource_config(self, Expression: str, Limit: int = None, NextToken: str = None) -> Dict:
        """
        .. _https://docs.aws.amazon.com/config/latest/developerguide/query-components.html: https://docs.aws.amazon.com/config/latest/developerguide/query-components.html
        Accepts a structured query language (SQL) ``SELECT`` command, performs the corresponding search, and returns resource configurations matching the properties.
        For more information about query components, see the ` **Query Components** https://docs.aws.amazon.com/config/latest/developerguide/query-components.html`__ section in the AWS Config Developer Guide.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/SelectResourceConfig>`_
        
        **Request Syntax**
        ::
          response = client.select_resource_config(
              Expression='string',
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Results': [
                    'string',
                ],
                'QueryInfo': {
                    'SelectFields': [
                        {
                            'Name': 'string'
                        },
                    ]
                },
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Results** *(list) --* 
              Returns the results for the SQL query.
              - *(string) --* 
            - **QueryInfo** *(dict) --* 
              Returns the ``QueryInfo`` object.
              - **SelectFields** *(list) --* 
                Returns a ``FieldInfo`` object.
                - *(dict) --* 
                  Details about the fields such as name of the field.
                  - **Name** *(string) --* 
                    Name of the field.
            - **NextToken** *(string) --* 
              The ``nextToken`` string returned in a previous request that you use to request the next page of results in a paginated response. 
        :type Expression: string
        :param Expression: **[REQUIRED]**
          The SQL query ``SELECT`` command.
        :type Limit: integer
        :param Limit:
          The maximum number of query results returned on each page.
        :type NextToken: string
        :param NextToken:
          The ``nextToken`` string returned in a previous request that you use to request the next page of results in a paginated response.
        :rtype: dict
        :returns:
        """
        pass

    def start_config_rules_evaluation(self, ConfigRuleNames: List = None) -> Dict:
        """
        Runs an on-demand evaluation for the specified AWS Config rules against the last known configuration state of the resources. Use ``StartConfigRulesEvaluation`` when you want to test that a rule you updated is working as expected. ``StartConfigRulesEvaluation`` does not re-record the latest configuration state for your resources. It re-runs an evaluation against the last known state of your resources. 
        You can specify up to 25 AWS Config rules per request. 
        An existing ``StartConfigRulesEvaluation`` call for the specified rules must complete before you can call the API again. If you chose to have AWS Config stream to an Amazon SNS topic, you will receive a ``ConfigRuleEvaluationStarted`` notification when the evaluation starts.
        .. note::
          You don't need to call the ``StartConfigRulesEvaluation`` API to run an evaluation for a new rule. When you create a rule, AWS Config evaluates your resources against the rule automatically. 
        The ``StartConfigRulesEvaluation`` API is useful if you want to run on-demand evaluations, such as the following example:
        * You have a custom rule that evaluates your IAM resources every 24 hours. 
        * You update your Lambda function to add additional conditions to your rule. 
        * Instead of waiting for the next periodic evaluation, you call the ``StartConfigRulesEvaluation`` API. 
        * AWS Config invokes your Lambda function and evaluates your IAM resources. 
        * Your custom rule will still run periodic evaluations every 24 hours. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/StartConfigRulesEvaluation>`_
        
        **Request Syntax**
        ::
          response = client.start_config_rules_evaluation(
              ConfigRuleNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output when you start the evaluation for the specified AWS Config rule.
        :type ConfigRuleNames: list
        :param ConfigRuleNames:
          The list of names of AWS Config rules that you want to run evaluations for.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def start_configuration_recorder(self, ConfigurationRecorderName: str):
        """
        Starts recording configurations of the AWS resources you have selected to record in your AWS account.
        You must have created at least one delivery channel to successfully start the configuration recorder.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/StartConfigurationRecorder>`_
        
        **Request Syntax**
        ::
          response = client.start_configuration_recorder(
              ConfigurationRecorderName='string'
          )
        :type ConfigurationRecorderName: string
        :param ConfigurationRecorderName: **[REQUIRED]**
          The name of the recorder object that records each configuration change made to the resources.
        :returns: None
        """
        pass

    def start_remediation_execution(self, ConfigRuleName: str, ResourceKeys: List) -> Dict:
        """
        Runs an on-demand remediation for the specified AWS Config rules against the last known remediation configuration. It runs an execution against the current state of your resources. Remediation execution is asynchronous.
        You can specify up to 100 resource keys per request. An existing StartRemediationExecution call for the specified resource keys must complete before you can call the API again.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/StartRemediationExecution>`_
        
        **Request Syntax**
        ::
          response = client.start_remediation_execution(
              ConfigRuleName='string',
              ResourceKeys=[
                  {
                      'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                      'resourceId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailureMessage': 'string',
                'FailedItems': [
                    {
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::WAF::RuleGroup'|'AWS::WAFRegional::RuleGroup'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::CodePipeline::Pipeline',
                        'resourceId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailureMessage** *(string) --* 
              Returns a failure message. For example, the resource is already compliant.
            - **FailedItems** *(list) --* 
              For resources that have failed to start execution, the API returns a resource key object.
              - *(dict) --* 
                The details that identify a resource within AWS Config, including the resource type and resource ID.
                - **resourceType** *(string) --* 
                  The resource type.
                - **resourceId** *(string) --* 
                  The ID of the resource (for example., sg-xxxxxx). 
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**
          The list of names of AWS Config rules that you want to run remediation execution for.
        :type ResourceKeys: list
        :param ResourceKeys: **[REQUIRED]**
          A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.
          - *(dict) --*
            The details that identify a resource within AWS Config, including the resource type and resource ID.
            - **resourceType** *(string) --* **[REQUIRED]**
              The resource type.
            - **resourceId** *(string) --* **[REQUIRED]**
              The ID of the resource (for example., sg-xxxxxx).
        :rtype: dict
        :returns:
        """
        pass

    def stop_configuration_recorder(self, ConfigurationRecorderName: str):
        """
        Stops recording configurations of the AWS resources you have selected to record in your AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/StopConfigurationRecorder>`_
        
        **Request Syntax**
        ::
          response = client.stop_configuration_recorder(
              ConfigurationRecorderName='string'
          )
        :type ConfigurationRecorderName: string
        :param ConfigurationRecorderName: **[REQUIRED]**
          The name of the recorder object that records each configuration change made to the resources.
        :returns: None
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: List):
        """
        Associates the specified tags to a resource with the specified resourceArn. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are ``ConfigRule`` , ``ConfigurationAggregator`` and ``AggregatorAuthorization`` .
        :type Tags: list
        :param Tags: **[REQUIRED]**
          An array of tag object.
          - *(dict) --*
            The tags for the resource. The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            - **Key** *(string) --*
              One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            - **Value** *(string) --*
              The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
        :returns: None
        """
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List):
        """
        Deletes specified tags from a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are ``ConfigRule`` , ``ConfigurationAggregator`` and ``AggregatorAuthorization`` .
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          The keys of the tags to be removed.
          - *(string) --*
        :returns: None
        """
        pass
