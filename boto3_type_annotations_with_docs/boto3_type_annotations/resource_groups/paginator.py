from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListGroupResources(Paginator):
    def paginate(self, GroupName: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ResourceGroups.Client.list_group_resources`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroupResources>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              GroupName='string',
              Filters=[
                  {
                      'Name': 'resource-type',
                      'Values': [
                          'string',
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
                'ResourceIdentifiers': [
                    {
                        'ResourceArn': 'string',
                        'ResourceType': 'string'
                    },
                ],
                'QueryErrors': [
                    {
                        'ErrorCode': 'CLOUDFORMATION_STACK_INACTIVE'|'CLOUDFORMATION_STACK_NOT_EXISTING',
                        'Message': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourceIdentifiers** *(list) --* 
              The ARNs and resource types of resources that are members of the group that you specified.
              - *(dict) --* 
                The ARN of a resource, and its resource type.
                - **ResourceArn** *(string) --* 
                  The ARN of a resource.
                - **ResourceType** *(string) --* 
                  The resource type of a resource, such as ``AWS::EC2::Instance`` .
            - **QueryErrors** *(list) --* 
              A list of ``QueryError`` objects. Each error is an object that contains ``ErrorCode`` and ``Message`` structures. Possible values for ``ErrorCode`` are ``CLOUDFORMATION_STACK_INACTIVE`` and ``CLOUDFORMATION_STACK_NOT_EXISTING`` .
              - *(dict) --* 
                A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources`` operations on CloudFormation stack-based queries. The error occurs if the CloudFormation stack on which the query is based either does not exist, or has a status that renders the stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource Groups could not complete the operation, but the resulting group might have no member resources.
                - **ErrorCode** *(string) --* 
                  Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and ``CLOUDFORMATION_STACK_NOT_EXISTING`` .
                - **Message** *(string) --* 
                  A message that explains the ``ErrorCode`` value. Messages might state that the specified CloudFormation stack does not exist (or no longer exists). For ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          The name of the resource group.
        :type Filters: list
        :param Filters:
          Filters, formatted as ResourceFilter objects, that you want to apply to a ListGroupResources operation.
          * ``resource-type`` - Filter resources by their type. Specify up to five resource types in the format AWS::ServiceCode::ResourceType. For example, AWS::EC2::Instance, or AWS::S3::Bucket.
          - *(dict) --*
            A filter name and value pair that is used to obtain more specific results from a list of resources.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case-sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Allowed filter values vary by resource filter name, and are case-sensitive.
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


class ListGroups(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ResourceGroups.Client.list_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'resource-type',
                      'Values': [
                          'string',
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
                'GroupIdentifiers': [
                    {
                        'GroupName': 'string',
                        'GroupArn': 'string'
                    },
                ],
                'Groups': [
                    {
                        'GroupArn': 'string',
                        'Name': 'string',
                        'Description': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GroupIdentifiers** *(list) --* 
              A list of GroupIdentifier objects. Each identifier is an object that contains both the GroupName and the GroupArn.
              - *(dict) --* 
                The ARN and group name of a group.
                - **GroupName** *(string) --* 
                  The name of a resource group.
                - **GroupArn** *(string) --* 
                  The ARN of a resource group.
            - **Groups** *(list) --* 
              A list of resource groups.
              - *(dict) --* 
                A resource group.
                - **GroupArn** *(string) --* 
                  The ARN of a resource group.
                - **Name** *(string) --* 
                  The name of a resource group.
                - **Description** *(string) --* 
                  The description of the resource group.
        :type Filters: list
        :param Filters:
          Filters, formatted as GroupFilter objects, that you want to apply to a ListGroups operation.
          * ``resource-type`` - Filter groups by resource type. Specify up to five resource types in the format AWS::ServiceCode::ResourceType. For example, AWS::EC2::Instance, or AWS::S3::Bucket.
          - *(dict) --*
            A filter name and value pair that is used to obtain more specific results from a list of groups.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case-sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Allowed filter values vary by group filter name, and are case-sensitive.
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


class SearchResources(Paginator):
    def paginate(self, ResourceQuery: Dict, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ResourceGroups.Client.search_resources`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/SearchResources>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceQuery={
                  'Type': 'TAG_FILTERS_1_0'|'CLOUDFORMATION_STACK_1_0',
                  'Query': 'string'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ResourceIdentifiers': [
                    {
                        'ResourceArn': 'string',
                        'ResourceType': 'string'
                    },
                ],
                'QueryErrors': [
                    {
                        'ErrorCode': 'CLOUDFORMATION_STACK_INACTIVE'|'CLOUDFORMATION_STACK_NOT_EXISTING',
                        'Message': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourceIdentifiers** *(list) --* 
              The ARNs and resource types of resources that are members of the group that you specified.
              - *(dict) --* 
                The ARN of a resource, and its resource type.
                - **ResourceArn** *(string) --* 
                  The ARN of a resource.
                - **ResourceType** *(string) --* 
                  The resource type of a resource, such as ``AWS::EC2::Instance`` .
            - **QueryErrors** *(list) --* 
              A list of ``QueryError`` objects. Each error is an object that contains ``ErrorCode`` and ``Message`` structures. Possible values for ``ErrorCode`` are ``CLOUDFORMATION_STACK_INACTIVE`` and ``CLOUDFORMATION_STACK_NOT_EXISTING`` .
              - *(dict) --* 
                A two-part error structure that can occur in ``ListGroupResources`` or ``SearchResources`` operations on CloudFormation stack-based queries. The error occurs if the CloudFormation stack on which the query is based either does not exist, or has a status that renders the stack inactive. A ``QueryError`` occurrence does not necessarily mean that AWS Resource Groups could not complete the operation, but the resulting group might have no member resources.
                - **ErrorCode** *(string) --* 
                  Possible values are ``CLOUDFORMATION_STACK_INACTIVE`` and ``CLOUDFORMATION_STACK_NOT_EXISTING`` .
                - **Message** *(string) --* 
                  A message that explains the ``ErrorCode`` value. Messages might state that the specified CloudFormation stack does not exist (or no longer exists). For ``CLOUDFORMATION_STACK_INACTIVE`` , the message typically states that the CloudFormation stack has a status that is not (or no longer) active, such as ``CREATE_FAILED`` .
        :type ResourceQuery: dict
        :param ResourceQuery: **[REQUIRED]**
          The search query, using the same formats that are supported for resource group definition.
          - **Type** *(string) --* **[REQUIRED]**
            The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and ``CLOUDFORMATION_STACK_1_0`` .
             * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API `GetResources <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__ operation. If you specify more than one tag key, only resources that match all tag keys, and at least one value of each specified tag key, are returned in your query. If you specify more than one value for a tag key, a resource matches the filter if it has a tag key value that matches *any* of the specified values.
            For example, consider the following sample query for resources that have two tags, ``Stage`` and ``Version`` , with two values each. (``[{\"Key\":\"Stage\",\"Values\":[\"Test\",\"Deploy\"]},{\"Key\":\"Version\",\"Values\":[\"1\",\"2\"]}]`` ) The results of this query might include the following.
            * An EC2 instance that has the following two tags: ``{\"Key\":\"Stage\",\"Values\":[\"Deploy\"]}`` , and ``{\"Key\":\"Version\",\"Values\":[\"2\"]}``
            * An S3 bucket that has the following two tags: {\"Key\":\"Stage\",\"Values\":[\"Test\",\"Deploy\"]}, and {\"Key\":\"Version\",\"Values\":[\"1\"]}
            The query would not return the following results, however. The following EC2 instance does not have all tag keys specified in the filter, so it is rejected. The RDS database has all of the tag keys, but no values that match at least one of the specified tag key values in the filter.
            * An EC2 instance that has only the following tag: ``{\"Key\":\"Stage\",\"Values\":[\"Deploy\"]}`` .
            * An RDS database that has the following two tags: ``{\"Key\":\"Stage\",\"Values\":[\"Archived\"]}`` , and ``{\"Key\":\"Version\",\"Values\":[\"4\"]}``
             * ``CLOUDFORMATION_STACK_1_0:`` * A JSON syntax that lets you specify a CloudFormation stack ARN.
          - **Query** *(string) --* **[REQUIRED]**
            The query that defines a group or a search.
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
