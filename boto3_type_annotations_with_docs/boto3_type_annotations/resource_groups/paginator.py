from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListGroupResources(Paginator):
    def paginate(self, GroupName: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroupResources>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              GroupName=\'string\',
              Filters=[
                  {
                      \'Name\': \'resource-type\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResourceIdentifiers\': [
                    {
                        \'ResourceArn\': \'string\',
                        \'ResourceType\': \'string\'
                    },
                ],
                
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
        
        """
        pass


class ListGroups(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'resource-type\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          Filters, formatted as GroupFilter objects, that you want to apply to a ListGroups operation.
        
          * ``group-type`` - Filter groups by resource type. Specify up to five group types in the format AWS::ServiceCode::ResourceType. For example, AWS::EC2::Instance, or AWS::S3::Bucket. 
           
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupIdentifiers\': [
                    {
                        \'GroupName\': \'string\',
                        \'GroupArn\': \'string\'
                    },
                ],
                \'Groups\': [
                    {
                        \'GroupArn\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\'
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
        
        """
        pass


class SearchResources(Paginator):
    def paginate(self, ResourceQuery: Dict, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/SearchResources>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ResourceQuery={
                  \'Type\': \'TAG_FILTERS_1_0\',
                  \'Query\': \'string\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ResourceQuery: dict
        :param ResourceQuery: **[REQUIRED]** 
        
          The search query, using the same formats that are supported for resource group definition.
        
          - **Type** *(string) --* **[REQUIRED]** 
        
            The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .
        
             * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResourceIdentifiers\': [
                    {
                        \'ResourceArn\': \'string\',
                        \'ResourceType\': \'string\'
                    },
                ],
                
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
        
        """
        pass
