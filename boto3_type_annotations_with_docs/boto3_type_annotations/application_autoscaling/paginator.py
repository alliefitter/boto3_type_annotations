from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeScalableTargets(Paginator):
    def paginate(self, ServiceNamespace: str, ResourceIds: List = None, ScalableDimension: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DescribeScalableTargets>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ServiceNamespace=\'ecs\'|\'elasticmapreduce\'|\'ec2\'|\'appstream\'|\'dynamodb\'|\'rds\'|\'sagemaker\'|\'custom-resource\',
              ResourceIds=[
                  \'string\',
              ],
              ScalableDimension=\'ecs:service:DesiredCount\'|\'ec2:spot-fleet-request:TargetCapacity\'|\'elasticmapreduce:instancegroup:InstanceCount\'|\'appstream:fleet:DesiredCapacity\'|\'dynamodb:table:ReadCapacityUnits\'|\'dynamodb:table:WriteCapacityUnits\'|\'dynamodb:index:ReadCapacityUnits\'|\'dynamodb:index:WriteCapacityUnits\'|\'rds:cluster:ReadReplicaCount\'|\'sagemaker:variant:DesiredInstanceCount\'|\'custom-resource:ResourceType:Property\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]** 
        
          The namespace of the AWS service that provides the resource or ``custom-resource`` for a resource provided by your own application or service. For more information, see `AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__ in the *Amazon Web Services General Reference* .
        
        :type ResourceIds: list
        :param ResourceIds: 
        
          The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.
        
          * ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . 
           
          * Spot fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . 
           
          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . 
           
          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . 
           
          * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . 
           
          * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . 
           
          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . 
           
          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . 
           
          * Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. 
           
          - *(string) --* 
        
        :type ScalableDimension: string
        :param ScalableDimension: 
        
          The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.
        
          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service. 
           
          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot fleet request. 
           
          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. 
           
          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. 
           
          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. 
           
          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. 
           
          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. 
           
          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. 
           
          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition. 
           
          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon SageMaker model endpoint variant. 
           
          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. 
           
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
                \'ScalableTargets\': [
                    {
                        \'ServiceNamespace\': \'ecs\'|\'elasticmapreduce\'|\'ec2\'|\'appstream\'|\'dynamodb\'|\'rds\'|\'sagemaker\'|\'custom-resource\',
                        \'ResourceId\': \'string\',
                        \'ScalableDimension\': \'ecs:service:DesiredCount\'|\'ec2:spot-fleet-request:TargetCapacity\'|\'elasticmapreduce:instancegroup:InstanceCount\'|\'appstream:fleet:DesiredCapacity\'|\'dynamodb:table:ReadCapacityUnits\'|\'dynamodb:table:WriteCapacityUnits\'|\'dynamodb:index:ReadCapacityUnits\'|\'dynamodb:index:WriteCapacityUnits\'|\'rds:cluster:ReadReplicaCount\'|\'sagemaker:variant:DesiredInstanceCount\'|\'custom-resource:ResourceType:Property\',
                        \'MinCapacity\': 123,
                        \'MaxCapacity\': 123,
                        \'RoleARN\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ScalableTargets** *(list) --* 
        
              The scalable targets that match the request parameters.
        
              - *(dict) --* 
        
                Represents a scalable target.
        
                - **ServiceNamespace** *(string) --* 
        
                  The namespace of the AWS service that provides the resource or ``custom-resource`` for a resource provided by your own application or service. For more information, see `AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__ in the *Amazon Web Services General Reference* .
        
                - **ResourceId** *(string) --* 
        
                  The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.
        
                  * ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . 
                   
                  * Spot fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . 
                   
                  * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . 
                   
                  * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . 
                   
                  * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . 
                   
                  * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . 
                   
                  * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . 
                   
                  * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . 
                   
                  * Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. 
                   
                - **ScalableDimension** *(string) --* 
        
                  The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.
        
                  * ``ecs:service:DesiredCount`` - The desired task count of an ECS service. 
                   
                  * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot fleet request. 
                   
                  * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. 
                   
                  * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. 
                   
                  * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. 
                   
                  * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. 
                   
                  * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. 
                   
                  * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. 
                   
                  * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition. 
                   
                  * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon SageMaker model endpoint variant. 
                   
                  * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. 
                   
                - **MinCapacity** *(integer) --* 
        
                  The minimum value to scale to in response to a scale in event.
        
                - **MaxCapacity** *(integer) --* 
        
                  The maximum value to scale to in response to a scale out event.
        
                - **RoleARN** *(string) --* 
        
                  The ARN of an IAM role that allows Application Auto Scaling to modify the scalable target on your behalf.
        
                - **CreationTime** *(datetime) --* 
        
                  The Unix timestamp for when the scalable target was created.
        
        """
        pass


class DescribeScalingActivities(Paginator):
    def paginate(self, ServiceNamespace: str, ResourceId: str = None, ScalableDimension: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DescribeScalingActivities>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ServiceNamespace=\'ecs\'|\'elasticmapreduce\'|\'ec2\'|\'appstream\'|\'dynamodb\'|\'rds\'|\'sagemaker\'|\'custom-resource\',
              ResourceId=\'string\',
              ScalableDimension=\'ecs:service:DesiredCount\'|\'ec2:spot-fleet-request:TargetCapacity\'|\'elasticmapreduce:instancegroup:InstanceCount\'|\'appstream:fleet:DesiredCapacity\'|\'dynamodb:table:ReadCapacityUnits\'|\'dynamodb:table:WriteCapacityUnits\'|\'dynamodb:index:ReadCapacityUnits\'|\'dynamodb:index:WriteCapacityUnits\'|\'rds:cluster:ReadReplicaCount\'|\'sagemaker:variant:DesiredInstanceCount\'|\'custom-resource:ResourceType:Property\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]** 
        
          The namespace of the AWS service that provides the resource or ``custom-resource`` for a resource provided by your own application or service. For more information, see `AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__ in the *Amazon Web Services General Reference* .
        
        :type ResourceId: string
        :param ResourceId: 
        
          The identifier of the resource associated with the scaling activity. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.
        
          * ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . 
           
          * Spot fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . 
           
          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . 
           
          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . 
           
          * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . 
           
          * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . 
           
          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . 
           
          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . 
           
          * Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. 
           
        :type ScalableDimension: string
        :param ScalableDimension: 
        
          The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.
        
          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service. 
           
          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot fleet request. 
           
          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. 
           
          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. 
           
          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. 
           
          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. 
           
          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. 
           
          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. 
           
          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition. 
           
          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon SageMaker model endpoint variant. 
           
          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. 
           
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
                \'ScalingActivities\': [
                    {
                        \'ActivityId\': \'string\',
                        \'ServiceNamespace\': \'ecs\'|\'elasticmapreduce\'|\'ec2\'|\'appstream\'|\'dynamodb\'|\'rds\'|\'sagemaker\'|\'custom-resource\',
                        \'ResourceId\': \'string\',
                        \'ScalableDimension\': \'ecs:service:DesiredCount\'|\'ec2:spot-fleet-request:TargetCapacity\'|\'elasticmapreduce:instancegroup:InstanceCount\'|\'appstream:fleet:DesiredCapacity\'|\'dynamodb:table:ReadCapacityUnits\'|\'dynamodb:table:WriteCapacityUnits\'|\'dynamodb:index:ReadCapacityUnits\'|\'dynamodb:index:WriteCapacityUnits\'|\'rds:cluster:ReadReplicaCount\'|\'sagemaker:variant:DesiredInstanceCount\'|\'custom-resource:ResourceType:Property\',
                        \'Description\': \'string\',
                        \'Cause\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'StatusCode\': \'Pending\'|\'InProgress\'|\'Successful\'|\'Overridden\'|\'Unfulfilled\'|\'Failed\',
                        \'StatusMessage\': \'string\',
                        \'Details\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ScalingActivities** *(list) --* 
        
              A list of scaling activity objects.
        
              - *(dict) --* 
        
                Represents a scaling activity.
        
                - **ActivityId** *(string) --* 
        
                  The unique identifier of the scaling activity.
        
                - **ServiceNamespace** *(string) --* 
        
                  The namespace of the AWS service that provides the resource or ``custom-resource`` for a resource provided by your own application or service. For more information, see `AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__ in the *Amazon Web Services General Reference* .
        
                - **ResourceId** *(string) --* 
        
                  The identifier of the resource associated with the scaling activity. This string consists of the resource type and unique identifier.
        
                  * ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . 
                   
                  * Spot fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . 
                   
                  * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . 
                   
                  * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . 
                   
                  * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . 
                   
                  * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . 
                   
                  * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . 
                   
                  * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . 
                   
                  * Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. 
                   
                - **ScalableDimension** *(string) --* 
        
                  The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
        
                  * ``ecs:service:DesiredCount`` - The desired task count of an ECS service. 
                   
                  * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot fleet request. 
                   
                  * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. 
                   
                  * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. 
                   
                  * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. 
                   
                  * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. 
                   
                  * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. 
                   
                  * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. 
                   
                  * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition. 
                   
                  * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon SageMaker model endpoint variant. 
                   
                  * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. 
                   
                - **Description** *(string) --* 
        
                  A simple description of what action the scaling activity intends to accomplish.
        
                - **Cause** *(string) --* 
        
                  A simple description of what caused the scaling activity to happen.
        
                - **StartTime** *(datetime) --* 
        
                  The Unix timestamp for when the scaling activity began.
        
                - **EndTime** *(datetime) --* 
        
                  The Unix timestamp for when the scaling activity ended.
        
                - **StatusCode** *(string) --* 
        
                  Indicates the status of the scaling activity.
        
                - **StatusMessage** *(string) --* 
        
                  A simple message about the current status of the scaling activity.
        
                - **Details** *(string) --* 
        
                  The details about the scaling activity.
        
        """
        pass


class DescribeScalingPolicies(Paginator):
    def paginate(self, ServiceNamespace: str, PolicyNames: List = None, ResourceId: str = None, ScalableDimension: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DescribeScalingPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PolicyNames=[
                  \'string\',
              ],
              ServiceNamespace=\'ecs\'|\'elasticmapreduce\'|\'ec2\'|\'appstream\'|\'dynamodb\'|\'rds\'|\'sagemaker\'|\'custom-resource\',
              ResourceId=\'string\',
              ScalableDimension=\'ecs:service:DesiredCount\'|\'ec2:spot-fleet-request:TargetCapacity\'|\'elasticmapreduce:instancegroup:InstanceCount\'|\'appstream:fleet:DesiredCapacity\'|\'dynamodb:table:ReadCapacityUnits\'|\'dynamodb:table:WriteCapacityUnits\'|\'dynamodb:index:ReadCapacityUnits\'|\'dynamodb:index:WriteCapacityUnits\'|\'rds:cluster:ReadReplicaCount\'|\'sagemaker:variant:DesiredInstanceCount\'|\'custom-resource:ResourceType:Property\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PolicyNames: list
        :param PolicyNames: 
        
          The names of the scaling policies to describe.
        
          - *(string) --* 
        
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]** 
        
          The namespace of the AWS service that provides the resource or ``custom-resource`` for a resource provided by your own application or service. For more information, see `AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__ in the *Amazon Web Services General Reference* .
        
        :type ResourceId: string
        :param ResourceId: 
        
          The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.
        
          * ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . 
           
          * Spot fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . 
           
          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . 
           
          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . 
           
          * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . 
           
          * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . 
           
          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . 
           
          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . 
           
          * Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. 
           
        :type ScalableDimension: string
        :param ScalableDimension: 
        
          The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.
        
          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service. 
           
          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot fleet request. 
           
          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. 
           
          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. 
           
          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. 
           
          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. 
           
          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. 
           
          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. 
           
          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition. 
           
          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon SageMaker model endpoint variant. 
           
          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. 
           
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
                \'ScalingPolicies\': [
                    {
                        \'PolicyARN\': \'string\',
                        \'PolicyName\': \'string\',
                        \'ServiceNamespace\': \'ecs\'|\'elasticmapreduce\'|\'ec2\'|\'appstream\'|\'dynamodb\'|\'rds\'|\'sagemaker\'|\'custom-resource\',
                        \'ResourceId\': \'string\',
                        \'ScalableDimension\': \'ecs:service:DesiredCount\'|\'ec2:spot-fleet-request:TargetCapacity\'|\'elasticmapreduce:instancegroup:InstanceCount\'|\'appstream:fleet:DesiredCapacity\'|\'dynamodb:table:ReadCapacityUnits\'|\'dynamodb:table:WriteCapacityUnits\'|\'dynamodb:index:ReadCapacityUnits\'|\'dynamodb:index:WriteCapacityUnits\'|\'rds:cluster:ReadReplicaCount\'|\'sagemaker:variant:DesiredInstanceCount\'|\'custom-resource:ResourceType:Property\',
                        \'PolicyType\': \'StepScaling\'|\'TargetTrackingScaling\',
                        \'StepScalingPolicyConfiguration\': {
                            \'AdjustmentType\': \'ChangeInCapacity\'|\'PercentChangeInCapacity\'|\'ExactCapacity\',
                            \'StepAdjustments\': [
                                {
                                    \'MetricIntervalLowerBound\': 123.0,
                                    \'MetricIntervalUpperBound\': 123.0,
                                    \'ScalingAdjustment\': 123
                                },
                            ],
                            \'MinAdjustmentMagnitude\': 123,
                            \'Cooldown\': 123,
                            \'MetricAggregationType\': \'Average\'|\'Minimum\'|\'Maximum\'
                        },
                        \'TargetTrackingScalingPolicyConfiguration\': {
                            \'TargetValue\': 123.0,
                            \'PredefinedMetricSpecification\': {
                                \'PredefinedMetricType\': \'DynamoDBReadCapacityUtilization\'|\'DynamoDBWriteCapacityUtilization\'|\'ALBRequestCountPerTarget\'|\'RDSReaderAverageCPUUtilization\'|\'RDSReaderAverageDatabaseConnections\'|\'EC2SpotFleetRequestAverageCPUUtilization\'|\'EC2SpotFleetRequestAverageNetworkIn\'|\'EC2SpotFleetRequestAverageNetworkOut\'|\'SageMakerVariantInvocationsPerInstance\'|\'ECSServiceAverageCPUUtilization\'|\'ECSServiceAverageMemoryUtilization\',
                                \'ResourceLabel\': \'string\'
                            },
                            \'CustomizedMetricSpecification\': {
                                \'MetricName\': \'string\',
                                \'Namespace\': \'string\',
                                \'Dimensions\': [
                                    {
                                        \'Name\': \'string\',
                                        \'Value\': \'string\'
                                    },
                                ],
                                \'Statistic\': \'Average\'|\'Minimum\'|\'Maximum\'|\'SampleCount\'|\'Sum\',
                                \'Unit\': \'string\'
                            },
                            \'ScaleOutCooldown\': 123,
                            \'ScaleInCooldown\': 123,
                            \'DisableScaleIn\': True|False
                        },
                        \'Alarms\': [
                            {
                                \'AlarmName\': \'string\',
                                \'AlarmARN\': \'string\'
                            },
                        ],
                        \'CreationTime\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ScalingPolicies** *(list) --* 
        
              Information about the scaling policies.
        
              - *(dict) --* 
        
                Represents a scaling policy.
        
                - **PolicyARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the scaling policy.
        
                - **PolicyName** *(string) --* 
        
                  The name of the scaling policy.
        
                - **ServiceNamespace** *(string) --* 
        
                  The namespace of the AWS service that provides the resource or ``custom-resource`` for a resource provided by your own application or service. For more information, see `AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__ in the *Amazon Web Services General Reference* .
        
                - **ResourceId** *(string) --* 
        
                  The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.
        
                  * ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . 
                   
                  * Spot fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . 
                   
                  * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . 
                   
                  * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . 
                   
                  * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . 
                   
                  * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . 
                   
                  * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . 
                   
                  * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . 
                   
                  * Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. 
                   
                - **ScalableDimension** *(string) --* 
        
                  The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
        
                  * ``ecs:service:DesiredCount`` - The desired task count of an ECS service. 
                   
                  * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot fleet request. 
                   
                  * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. 
                   
                  * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. 
                   
                  * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. 
                   
                  * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. 
                   
                  * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. 
                   
                  * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. 
                   
                  * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition. 
                   
                  * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon SageMaker model endpoint variant. 
                   
                  * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. 
                   
                - **PolicyType** *(string) --* 
        
                  The scaling policy type.
        
                - **StepScalingPolicyConfiguration** *(dict) --* 
        
                  A step scaling policy.
        
                  - **AdjustmentType** *(string) --* 
        
                    The adjustment type, which specifies how the ``ScalingAdjustment`` parameter in a  StepAdjustment is interpreted.
        
                  - **StepAdjustments** *(list) --* 
        
                    A set of adjustments that enable you to scale based on the size of the alarm breach.
        
                    - *(dict) --* 
        
                      Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you\'ve defined for the alarm. 
        
                      For the following examples, suppose that you have an alarm with a breach threshold of 50:
        
                      * To trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10. 
                       
                      * To trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0. 
                       
                      There are a few rules for the step adjustments for your step policy:
        
                      * The ranges of your step adjustments can\'t overlap or have a gap. 
                       
                      * At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound. 
                       
                      * At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound. 
                       
                      * The upper and lower bound can\'t be null in the same step adjustment. 
                       
                      - **MetricIntervalLowerBound** *(float) --* 
        
                        The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.
        
                      - **MetricIntervalUpperBound** *(float) --* 
        
                        The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
        
                        The upper bound must be greater than the lower bound.
        
                      - **ScalingAdjustment** *(integer) --* 
        
                        The amount by which to scale, based on the specified adjustment type. A positive value adds to the current scalable dimension while a negative number removes from the current scalable dimension.
        
                  - **MinAdjustmentMagnitude** *(integer) --* 
        
                    The minimum number to adjust your scalable dimension as a result of a scaling activity. If the adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the scalable dimension of the scalable target by this amount.
        
                  - **Cooldown** *(integer) --* 
        
                    The amount of time, in seconds, after a scaling activity completes where previous trigger-related scaling activities can influence future scaling events.
        
                    For scale out policies, while the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out. For example, an alarm triggers a step scaling policy to scale out an Amazon ECS service by 2 tasks, the scaling activity completes successfully, and a cooldown period of 5 minutes starts. During the Cooldown period, if the alarm triggers the same policy again but at a more aggressive step adjustment to scale out the service by 3 tasks, the 2 tasks that were added in the previous scale out event are considered part of that capacity and only 1 additional task is added to the desired count.
        
                    For scale in policies, the cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, Application Auto Scaling scales out your scalable target immediately.
        
                  - **MetricAggregationType** *(string) --* 
        
                    The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` , ``Maximum`` , and ``Average`` .
        
                - **TargetTrackingScalingPolicyConfiguration** *(dict) --* 
        
                  A target tracking policy.
        
                  - **TargetValue** *(float) --* 
        
                    The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
        
                  - **PredefinedMetricSpecification** *(dict) --* 
        
                    A predefined metric.
        
                    - **PredefinedMetricType** *(string) --* 
        
                      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot fleet requests and ECS services.
        
                    - **ResourceLabel** *(string) --* 
        
                      Identifies the resource associated with the metric type. You can\'t specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached to the Spot fleet request or ECS service.
        
                      The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:
        
                      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN 
                       
                      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN. 
                       
                  - **CustomizedMetricSpecification** *(dict) --* 
        
                    A customized metric.
        
                    - **MetricName** *(string) --* 
        
                      The name of the metric.
        
                    - **Namespace** *(string) --* 
        
                      The namespace of the metric.
        
                    - **Dimensions** *(list) --* 
        
                      The dimensions of the metric.
        
                      - *(dict) --* 
        
                        Describes the dimension of a metric.
        
                        - **Name** *(string) --* 
        
                          The name of the dimension.
        
                        - **Value** *(string) --* 
        
                          The value of the dimension.
        
                    - **Statistic** *(string) --* 
        
                      The statistic of the metric.
        
                    - **Unit** *(string) --* 
        
                      The unit of the metric.
        
                  - **ScaleOutCooldown** *(integer) --* 
        
                    The amount of time, in seconds, after a scale out activity completes before another scale out activity can start.
        
                    While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out.
        
                  - **ScaleInCooldown** *(integer) --* 
        
                    The amount of time, in seconds, after a scale in activity completes before another scale in activity can start.
        
                    The cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, Application Auto Scaling scales out your scalable target immediately.
        
                  - **DisableScaleIn** *(boolean) --* 
        
                    Indicates whether scale in by the target tracking policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is ``false`` .
        
                - **Alarms** *(list) --* 
        
                  The CloudWatch alarms associated with the scaling policy.
        
                  - *(dict) --* 
        
                    Represents a CloudWatch alarm associated with a scaling policy.
        
                    - **AlarmName** *(string) --* 
        
                      The name of the alarm.
        
                    - **AlarmARN** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the alarm.
        
                - **CreationTime** *(datetime) --* 
        
                  The Unix timestamp for when the scaling policy was created.
        
        """
        pass
