from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeScalingPlanResources(Paginator):
    def paginate(self, ScalingPlanName: str, ScalingPlanVersion: int, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScalingPlans.Client.describe_scaling_plan_resources`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-plans-2018-01-06/DescribeScalingPlanResources>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ScalingPlanName='string',
              ScalingPlanVersion=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ScalingPlanResources': [
                    {
                        'ScalingPlanName': 'string',
                        'ScalingPlanVersion': 123,
                        'ServiceNamespace': 'autoscaling'|'ecs'|'ec2'|'rds'|'dynamodb',
                        'ResourceId': 'string',
                        'ScalableDimension': 'autoscaling:autoScalingGroup:DesiredCapacity'|'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'rds:cluster:ReadReplicaCount'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'PolicyType': 'TargetTrackingScaling',
                                'TargetTrackingConfiguration': {
                                    'PredefinedScalingMetricSpecification': {
                                        'PredefinedScalingMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut',
                                        'ResourceLabel': 'string'
                                    },
                                    'CustomizedScalingMetricSpecification': {
                                        'MetricName': 'string',
                                        'Namespace': 'string',
                                        'Dimensions': [
                                            {
                                                'Name': 'string',
                                                'Value': 'string'
                                            },
                                        ],
                                        'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                                        'Unit': 'string'
                                    },
                                    'TargetValue': 123.0,
                                    'DisableScaleIn': True|False,
                                    'ScaleOutCooldown': 123,
                                    'ScaleInCooldown': 123,
                                    'EstimatedInstanceWarmup': 123
                                }
                            },
                        ],
                        'ScalingStatusCode': 'Inactive'|'PartiallyActive'|'Active',
                        'ScalingStatusMessage': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ScalingPlanResources** *(list) --* 
              Information about the scalable resources.
              - *(dict) --* 
                Represents a scalable resource.
                - **ScalingPlanName** *(string) --* 
                  The name of the scaling plan.
                - **ScalingPlanVersion** *(integer) --* 
                  The version number of the scaling plan.
                - **ServiceNamespace** *(string) --* 
                  The namespace of the AWS service.
                - **ResourceId** *(string) --* 
                  The ID of the resource. This string consists of the resource type and unique identifier.
                  * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique identifier is the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` . 
                  * ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . 
                  * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . 
                  * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . 
                  * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . 
                  * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . 
                - **ScalableDimension** *(string) --* 
                  The scalable dimension for the resource.
                  * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto Scaling group. 
                  * ``ecs:service:DesiredCount`` - The desired task count of an ECS service. 
                  * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request. 
                  * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. 
                  * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. 
                  * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. 
                  * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. 
                  * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition. 
                - **ScalingPolicies** *(list) --* 
                  The scaling policies.
                  - *(dict) --* 
                    Represents a scaling policy.
                    - **PolicyName** *(string) --* 
                      The name of the scaling policy.
                    - **PolicyType** *(string) --* 
                      The type of scaling policy.
                    - **TargetTrackingConfiguration** *(dict) --* 
                      The target tracking scaling policy. 
                      - **PredefinedScalingMetricSpecification** *(dict) --* 
                        A predefined metric.
                        - **PredefinedScalingMetricType** *(string) --* 
                          The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto Scaling groups, Spot Fleet requests, and ECS services.
                        - **ResourceLabel** *(string) --* 
                          Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet request, or ECS service.
                          The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:
                          * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN. 
                          * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN. 
                      - **CustomizedScalingMetricSpecification** *(dict) --* 
                        A customized metric.
                        - **MetricName** *(string) --* 
                          The name of the metric.
                        - **Namespace** *(string) --* 
                          The namespace of the metric.
                        - **Dimensions** *(list) --* 
                          The dimensions of the metric.
                          - *(dict) --* 
                            Represents a dimension for a customized metric.
                            - **Name** *(string) --* 
                              The name of the dimension.
                            - **Value** *(string) --* 
                              The value of the dimension.
                        - **Statistic** *(string) --* 
                          The statistic of the metric.
                        - **Unit** *(string) --* 
                          The unit of the metric. 
                      - **TargetValue** *(float) --* 
                        The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
                      - **DisableScaleIn** *(boolean) --* 
                        Indicates whether scale in by the target tracking scaling policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking scaling policy doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable resource. 
                        The default value is ``false`` .
                      - **ScaleOutCooldown** *(integer) --* 
                        The amount of time, in seconds, after a scale-out activity completes before another scale-out activity can start. This value is not used if the scalable resource is an Auto Scaling group.
                        While the cooldown period is in effect, the capacity that has been added by the previous scale-out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out.
                      - **ScaleInCooldown** *(integer) --* 
                        The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. This value is not used if the scalable resource is an Auto Scaling group.
                        The cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application's availability. However, if another alarm triggers a scale-out policy during the cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target immediately.
                      - **EstimatedInstanceWarmup** *(integer) --* 
                        The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.
                - **ScalingStatusCode** *(string) --* 
                  The scaling status of the resource.
                  * ``Active`` - The scaling configuration is active. 
                  * ``Inactive`` - The scaling configuration is not active because the scaling plan is being created or the scaling configuration could not be applied. Check the status message for more information. 
                  * ``PartiallyActive`` - The scaling configuration is partially active because the scaling plan is being created or deleted or the scaling configuration could not be fully applied. Check the status message for more information. 
                - **ScalingStatusMessage** *(string) --* 
                  A simple message about the current scaling status of the resource.
        :type ScalingPlanName: string
        :param ScalingPlanName: **[REQUIRED]**
          The name of the scaling plan.
        :type ScalingPlanVersion: integer
        :param ScalingPlanVersion: **[REQUIRED]**
          The version number of the scaling plan.
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


class DescribeScalingPlans(Paginator):
    def paginate(self, ScalingPlanNames: List = None, ScalingPlanVersion: int = None, ApplicationSources: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScalingPlans.Client.describe_scaling_plans`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-plans-2018-01-06/DescribeScalingPlans>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ScalingPlanNames=[
                  'string',
              ],
              ScalingPlanVersion=123,
              ApplicationSources=[
                  {
                      'CloudFormationStackARN': 'string',
                      'TagFilters': [
                          {
                              'Key': 'string',
                              'Values': [
                                  'string',
                              ]
                          },
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ScalingPlans': [
                    {
                        'ScalingPlanName': 'string',
                        'ScalingPlanVersion': 123,
                        'ApplicationSource': {
                            'CloudFormationStackARN': 'string',
                            'TagFilters': [
                                {
                                    'Key': 'string',
                                    'Values': [
                                        'string',
                                    ]
                                },
                            ]
                        },
                        'ScalingInstructions': [
                            {
                                'ServiceNamespace': 'autoscaling'|'ecs'|'ec2'|'rds'|'dynamodb',
                                'ResourceId': 'string',
                                'ScalableDimension': 'autoscaling:autoScalingGroup:DesiredCapacity'|'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'rds:cluster:ReadReplicaCount'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits',
                                'MinCapacity': 123,
                                'MaxCapacity': 123,
                                'TargetTrackingConfigurations': [
                                    {
                                        'PredefinedScalingMetricSpecification': {
                                            'PredefinedScalingMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut',
                                            'ResourceLabel': 'string'
                                        },
                                        'CustomizedScalingMetricSpecification': {
                                            'MetricName': 'string',
                                            'Namespace': 'string',
                                            'Dimensions': [
                                                {
                                                    'Name': 'string',
                                                    'Value': 'string'
                                                },
                                            ],
                                            'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                                            'Unit': 'string'
                                        },
                                        'TargetValue': 123.0,
                                        'DisableScaleIn': True|False,
                                        'ScaleOutCooldown': 123,
                                        'ScaleInCooldown': 123,
                                        'EstimatedInstanceWarmup': 123
                                    },
                                ],
                                'PredefinedLoadMetricSpecification': {
                                    'PredefinedLoadMetricType': 'ASGTotalCPUUtilization'|'ASGTotalNetworkIn'|'ASGTotalNetworkOut'|'ALBTargetGroupRequestCount',
                                    'ResourceLabel': 'string'
                                },
                                'CustomizedLoadMetricSpecification': {
                                    'MetricName': 'string',
                                    'Namespace': 'string',
                                    'Dimensions': [
                                        {
                                            'Name': 'string',
                                            'Value': 'string'
                                        },
                                    ],
                                    'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                                    'Unit': 'string'
                                },
                                'ScheduledActionBufferTime': 123,
                                'PredictiveScalingMaxCapacityBehavior': 'SetForecastCapacityToMaxCapacity'|'SetMaxCapacityToForecastCapacity'|'SetMaxCapacityAboveForecastCapacity',
                                'PredictiveScalingMaxCapacityBuffer': 123,
                                'PredictiveScalingMode': 'ForecastAndScale'|'ForecastOnly',
                                'ScalingPolicyUpdateBehavior': 'KeepExternalPolicies'|'ReplaceExternalPolicies',
                                'DisableDynamicScaling': True|False
                            },
                        ],
                        'StatusCode': 'Active'|'ActiveWithProblems'|'CreationInProgress'|'CreationFailed'|'DeletionInProgress'|'DeletionFailed'|'UpdateInProgress'|'UpdateFailed',
                        'StatusMessage': 'string',
                        'StatusStartTime': datetime(2015, 1, 1),
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ScalingPlans** *(list) --* 
              Information about the scaling plans.
              - *(dict) --* 
                Represents a scaling plan.
                - **ScalingPlanName** *(string) --* 
                  The name of the scaling plan.
                - **ScalingPlanVersion** *(integer) --* 
                  The version number of the scaling plan.
                - **ApplicationSource** *(dict) --* 
                  The application source.
                  - **CloudFormationStackARN** *(string) --* 
                    The Amazon Resource Name (ARN) of a AWS CloudFormation stack.
                  - **TagFilters** *(list) --* 
                    A set of tags (up to 50).
                    - *(dict) --* 
                      Represents a tag.
                      - **Key** *(string) --* 
                        The tag key.
                      - **Values** *(list) --* 
                        The tag values (0 to 20).
                        - *(string) --* 
                - **ScalingInstructions** *(list) --* 
                  The scaling instructions.
                  - *(dict) --* 
                    Describes a scaling instruction for a scalable resource.
                    The scaling instruction is used in combination with a scaling plan, which is a set of instructions for configuring dynamic scaling and predictive scaling for the scalable resources in your application. Each scaling instruction applies to one resource.
                    AWS Auto Scaling creates target tracking scaling policies based on the scaling instructions. Target tracking scaling policies adjust the capacity of your scalable resource as required to maintain resource utilization at the target value that you specified. 
                    AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling groups using a subset of parameters, including the load metric, the scaling metric, the target value for the scaling metric, the predictive scaling mode (forecast and scale or forecast only), and the desired behavior when the forecast capacity exceeds the maximum capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts with traffic predictions for the two days ahead and schedules scaling actions that proactively add and remove resource capacity to match the forecast. 
                    For more information, see the `AWS Auto Scaling User Guide <http://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html>`__ .
                    - **ServiceNamespace** *(string) --* 
                      The namespace of the AWS service.
                    - **ResourceId** *(string) --* 
                      The ID of the resource. This string consists of the resource type and unique identifier.
                      * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique identifier is the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` . 
                      * ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . 
                      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . 
                      * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . 
                      * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . 
                      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . 
                    - **ScalableDimension** *(string) --* 
                      The scalable dimension associated with the resource.
                      * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto Scaling group. 
                      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service. 
                      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request. 
                      * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. 
                      * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. 
                      * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. 
                      * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. 
                      * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition. 
                    - **MinCapacity** *(integer) --* 
                      The minimum capacity of the resource. 
                    - **MaxCapacity** *(integer) --* 
                      The maximum capacity of the resource. The exception to this upper limit is if you specify a non-default setting for **PredictiveScalingMaxCapacityBehavior** . 
                    - **TargetTrackingConfigurations** *(list) --* 
                      The structure that defines new target tracking configurations (up to 10). Each of these structures includes a specific scaling metric and a target value for the metric, along with various parameters to use with dynamic scaling. 
                      With predictive scaling and dynamic scaling, the resource scales based on the target tracking configuration that provides the largest capacity for both scale in and scale out. 
                      Condition: The scaling metric must be unique across target tracking configurations.
                      - *(dict) --* 
                        Describes a target tracking configuration. Used with  ScalingInstruction and  ScalingPolicy .
                        - **PredefinedScalingMetricSpecification** *(dict) --* 
                          A predefined metric.
                          - **PredefinedScalingMetricType** *(string) --* 
                            The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto Scaling groups, Spot Fleet requests, and ECS services.
                          - **ResourceLabel** *(string) --* 
                            Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet request, or ECS service.
                            The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:
                            * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN. 
                            * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN. 
                        - **CustomizedScalingMetricSpecification** *(dict) --* 
                          A customized metric.
                          - **MetricName** *(string) --* 
                            The name of the metric.
                          - **Namespace** *(string) --* 
                            The namespace of the metric.
                          - **Dimensions** *(list) --* 
                            The dimensions of the metric.
                            - *(dict) --* 
                              Represents a dimension for a customized metric.
                              - **Name** *(string) --* 
                                The name of the dimension.
                              - **Value** *(string) --* 
                                The value of the dimension.
                          - **Statistic** *(string) --* 
                            The statistic of the metric.
                          - **Unit** *(string) --* 
                            The unit of the metric. 
                        - **TargetValue** *(float) --* 
                          The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
                        - **DisableScaleIn** *(boolean) --* 
                          Indicates whether scale in by the target tracking scaling policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking scaling policy doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable resource. 
                          The default value is ``false`` .
                        - **ScaleOutCooldown** *(integer) --* 
                          The amount of time, in seconds, after a scale-out activity completes before another scale-out activity can start. This value is not used if the scalable resource is an Auto Scaling group.
                          While the cooldown period is in effect, the capacity that has been added by the previous scale-out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out.
                        - **ScaleInCooldown** *(integer) --* 
                          The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. This value is not used if the scalable resource is an Auto Scaling group.
                          The cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application's availability. However, if another alarm triggers a scale-out policy during the cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target immediately.
                        - **EstimatedInstanceWarmup** *(integer) --* 
                          The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.
                    - **PredefinedLoadMetricSpecification** *(dict) --* 
                      The predefined load metric to use for predictive scaling. This parameter or a **CustomizedLoadMetricSpecification** is required when configuring predictive scaling, and cannot be used otherwise. 
                      - **PredefinedLoadMetricType** *(string) --* 
                        The metric type.
                      - **ResourceLabel** *(string) --* 
                        Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an Application Load Balancer attached to the Auto Scaling group.
                        The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:
                        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN. 
                        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN. 
                    - **CustomizedLoadMetricSpecification** *(dict) --* 
                      The customized load metric to use for predictive scaling. This parameter or a **PredefinedLoadMetricSpecification** is required when configuring predictive scaling, and cannot be used otherwise. 
                      - **MetricName** *(string) --* 
                        The name of the metric.
                      - **Namespace** *(string) --* 
                        The namespace of the metric.
                      - **Dimensions** *(list) --* 
                        The dimensions of the metric.
                        - *(dict) --* 
                          Represents a dimension for a customized metric.
                          - **Name** *(string) --* 
                            The name of the dimension.
                          - **Value** *(string) --* 
                            The value of the dimension.
                      - **Statistic** *(string) --* 
                        The statistic of the metric. Currently, the value must always be ``Sum`` . 
                      - **Unit** *(string) --* 
                        The unit of the metric.
                    - **ScheduledActionBufferTime** *(integer) --* 
                      The amount of time, in seconds, to buffer the run time of scheduled scaling actions when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and the buffer time is 5 minutes, then the run time of the corresponding scheduled scaling action will be 9:55 AM. The intention is to give resources time to be provisioned. For example, it can take a few minutes to launch an EC2 instance. The actual amount of time required depends on several factors, such as the size of the instance and whether there are startup scripts to complete. 
                      The value must be less than the forecast interval duration of 3600 seconds (60 minutes). The default is 300 seconds. 
                      Only valid when configuring predictive scaling. 
                    - **PredictiveScalingMaxCapacityBehavior** *(string) --* 
                      Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity specified for the resource. The default value is ``SetForecastCapacityToMaxCapacity`` .
                      The following are possible values:
                      * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource capacity higher than the maximum capacity. The maximum capacity is enforced as a hard limit.  
                      * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity higher than the maximum capacity to equal but not exceed forecast capacity. 
                      * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource capacity higher than the maximum capacity by a specified buffer value. The intention is to give the target tracking scaling policy extra capacity if unexpected traffic occurs.  
                      Only valid when configuring predictive scaling.
                    - **PredictiveScalingMaxCapacityBuffer** *(integer) --* 
                      The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.
                      Only valid when configuring predictive scaling. Required if the **PredictiveScalingMaxCapacityBehavior** is set to ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise.
                      The range is 1-100.
                    - **PredictiveScalingMode** *(string) --* 
                      The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise, AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions based on the capacity forecast. 
                    - **ScalingPolicyUpdateBehavior** *(string) --* 
                      Controls whether a resource's externally created scaling policies are kept or replaced. 
                      The default value is ``KeepExternalPolicies`` . If the parameter is set to ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto Scaling are deleted and new target tracking scaling policies created. 
                      Only valid when configuring dynamic scaling. 
                      Condition: The number of existing policies to be replaced must be less than or equal to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all existing policies and does not create new ones.
                    - **DisableDynamicScaling** *(boolean) --* 
                      Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based on the specified target tracking configurations. 
                      The default is enabled (``false`` ). 
                - **StatusCode** *(string) --* 
                  The status of the scaling plan.
                  * ``Active`` - The scaling plan is active. 
                  * ``ActiveWithProblems`` - The scaling plan is active, but the scaling configuration for one or more resources could not be applied. 
                  * ``CreationInProgress`` - The scaling plan is being created. 
                  * ``CreationFailed`` - The scaling plan could not be created. 
                  * ``DeletionInProgress`` - The scaling plan is being deleted. 
                  * ``DeletionFailed`` - The scaling plan could not be deleted. 
                  * ``UpdateInProgress`` - The scaling plan is being updated. 
                  * ``UpdateFailed`` - The scaling plan could not be updated. 
                - **StatusMessage** *(string) --* 
                  A simple message about the current status of the scaling plan.
                - **StatusStartTime** *(datetime) --* 
                  The Unix time stamp when the scaling plan entered the current status.
                - **CreationTime** *(datetime) --* 
                  The Unix time stamp when the scaling plan was created.
        :type ScalingPlanNames: list
        :param ScalingPlanNames:
          The names of the scaling plans (up to 10). If you specify application sources, you cannot specify scaling plan names.
          - *(string) --*
        :type ScalingPlanVersion: integer
        :param ScalingPlanVersion:
          The version number of the scaling plan. If you specify a scaling plan version, you must also specify a scaling plan name.
        :type ApplicationSources: list
        :param ApplicationSources:
          The sources for the applications (up to 10). If you specify scaling plan names, you cannot specify application sources.
          - *(dict) --*
            Represents an application source.
            - **CloudFormationStackARN** *(string) --*
              The Amazon Resource Name (ARN) of a AWS CloudFormation stack.
            - **TagFilters** *(list) --*
              A set of tags (up to 50).
              - *(dict) --*
                Represents a tag.
                - **Key** *(string) --*
                  The tag key.
                - **Values** *(list) --*
                  The tag values (0 to 20).
                  - *(string) --*
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
