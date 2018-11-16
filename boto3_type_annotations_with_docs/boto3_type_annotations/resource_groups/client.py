from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
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

    def create_group(self, Name: str, ResourceQuery: Dict, Description: str = None, Tags: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/CreateGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_group(
              Name=\'string\',
              Description=\'string\',
              ResourceQuery={
                  \'Type\': \'TAG_FILTERS_1_0\',
                  \'Query\': \'string\'
              },
              Tags={
                  \'string\': \'string\'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the group, which is the identifier of the group in other operations. A resource group name cannot be updated after it is created. A resource group name can have a maximum of 128 characters, including letters, numbers, hyphens, dots, and underscores. The name cannot start with ``AWS`` or ``aws`` ; these are reserved. A resource group name must be unique within your account.
        
        :type Description: string
        :param Description: 
        
          The description of the resource group. Descriptions can have a maximum of 511 characters, including letters, numbers, hyphens, underscores, punctuation, and spaces.
        
        :type ResourceQuery: dict
        :param ResourceQuery: **[REQUIRED]** 
        
          The resource query that determines which AWS resources are members of this group.
        
          - **Type** *(string) --* **[REQUIRED]** 
        
            The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .
        
             * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
        
          - **Query** *(string) --* **[REQUIRED]** 
        
            The query that defines a group or a search.
        
        :type Tags: dict
        :param Tags: 
        
          The tags to add to the group. A tag is a string-to-string map of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Group\': {
                    \'GroupArn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\'
                },
                \'ResourceQuery\': {
                    \'Type\': \'TAG_FILTERS_1_0\',
                    \'Query\': \'string\'
                },
                \'Tags\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Group** *(dict) --* 
        
              A full description of the resource group after it is created.
        
              - **GroupArn** *(string) --* 
        
                The ARN of a resource group.
        
              - **Name** *(string) --* 
        
                The name of a resource group.
        
              - **Description** *(string) --* 
        
                The description of the resource group.
        
            - **ResourceQuery** *(dict) --* 
        
              The resource query associated with the group.
        
              - **Type** *(string) --* 
        
                The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .
        
                 * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
        
              - **Query** *(string) --* 
        
                The query that defines a group or a search.
        
            - **Tags** *(dict) --* 
        
              The tags associated with the group.
        
              - *(string) --* 
                
                - *(string) --* 
          
        """
        pass

    def delete_group(self, GroupName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/DeleteGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_group(
              GroupName=\'string\'
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the resource group to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Group\': {
                    \'GroupArn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Group** *(dict) --* 
        
              A full description of the deleted resource group.
        
              - **GroupArn** *(string) --* 
        
                The ARN of a resource group.
        
              - **Name** *(string) --* 
        
                The name of a resource group.
        
              - **Description** *(string) --* 
        
                The description of the resource group.
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
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

    def get_group(self, GroupName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/GetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_group(
              GroupName=\'string\'
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the resource group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Group\': {
                    \'GroupArn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Group** *(dict) --* 
        
              A full description of the resource group.
        
              - **GroupArn** *(string) --* 
        
                The ARN of a resource group.
        
              - **Name** *(string) --* 
        
                The name of a resource group.
        
              - **Description** *(string) --* 
        
                The description of the resource group.
        
        """
        pass

    def get_group_query(self, GroupName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/GetGroupQuery>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_group_query(
              GroupName=\'string\'
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the resource group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupQuery\': {
                    \'GroupName\': \'string\',
                    \'ResourceQuery\': {
                        \'Type\': \'TAG_FILTERS_1_0\',
                        \'Query\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **GroupQuery** *(dict) --* 
        
              The resource query associated with the specified group.
        
              - **GroupName** *(string) --* 
        
                The name of a resource group that is associated with a specific resource query.
        
              - **ResourceQuery** *(dict) --* 
        
                The resource query which determines which AWS resources are members of the associated resource group.
        
                - **Type** *(string) --* 
        
                  The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .
        
                   * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
        
                - **Query** *(string) --* 
        
                  The query that defines a group or a search.
        
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

    def get_tags(self, Arn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/GetTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_tags(
              Arn=\'string\'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]** 
        
          The ARN of the resource for which you want a list of tags. The resource must exist within the account you are using.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'Tags\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* 
        
              The ARN of the tagged resource.
        
            - **Tags** *(dict) --* 
        
              The tags associated with the specified resource.
        
              - *(string) --* 
                
                - *(string) --* 
          
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

    def list_group_resources(self, GroupName: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroupResources>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_group_resources(
              GroupName=\'string\',
              Filters=[
                  {
                      \'Name\': \'resource-type\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of group member ARNs that are returned in a single call by ListGroupResources, in paginated output. By default, this number is 50.
        
        :type NextToken: string
        :param NextToken: 
        
          The NextToken value that is returned in a paginated ListGroupResources request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The NextToken value to include in a subsequent ``ListGroupResources`` request, to get more results.
        
        """
        pass

    def list_groups(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_groups(
              Filters=[
                  {
                      \'Name\': \'resource-type\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of resource group results that are returned by ListGroups in paginated output. By default, this number is 50.
        
        :type NextToken: string
        :param NextToken: 
        
          The NextToken value that is returned in a paginated ``ListGroups`` request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The NextToken value to include in a subsequent ``ListGroups`` request, to get more results.
        
        """
        pass

    def search_resources(self, ResourceQuery: Dict, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/SearchResources>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_resources(
              ResourceQuery={
                  \'Type\': \'TAG_FILTERS_1_0\',
                  \'Query\': \'string\'
              },
              MaxResults=123,
              NextToken=\'string\'
          )
        :type ResourceQuery: dict
        :param ResourceQuery: **[REQUIRED]** 
        
          The search query, using the same formats that are supported for resource group definition.
        
          - **Type** *(string) --* **[REQUIRED]** 
        
            The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .
        
             * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
        
          - **Query** *(string) --* **[REQUIRED]** 
        
            The query that defines a group or a search.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of group member ARNs returned by ``SearchResources`` in paginated output. By default, this number is 50.
        
        :type NextToken: string
        :param NextToken: 
        
          The NextToken value that is returned in a paginated ``SearchResources`` request. To get the next page of results, run the call again, add the NextToken parameter, and specify the NextToken value.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The NextToken value to include in a subsequent ``SearchResources`` request, to get more results.
        
        """
        pass

    def tag(self, Arn: str, Tags: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/Tag>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag(
              Arn=\'string\',
              Tags={
                  \'string\': \'string\'
              }
          )
        :type Arn: string
        :param Arn: **[REQUIRED]** 
        
          The ARN of the resource to which to add tags.
        
        :type Tags: dict
        :param Tags: **[REQUIRED]** 
        
          The tags to add to the specified resource. A tag is a string-to-string map of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'Tags\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* 
        
              The ARN of the tagged resource.
        
            - **Tags** *(dict) --* 
        
              The tags that have been added to the specified resource.
        
              - *(string) --* 
                
                - *(string) --* 
          
        """
        pass

    def untag(self, Arn: str, Keys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/Untag>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag(
              Arn=\'string\',
              Keys=[
                  \'string\',
              ]
          )
        :type Arn: string
        :param Arn: **[REQUIRED]** 
        
          The ARN of the resource from which to remove tags.
        
        :type Keys: list
        :param Keys: **[REQUIRED]** 
        
          The keys of the tags to be removed.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'Keys\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* 
        
              The ARN of the resource from which tags have been removed.
        
            - **Keys** *(list) --* 
        
              The keys of tags that have been removed.
        
              - *(string) --* 
          
        """
        pass

    def update_group(self, GroupName: str, Description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/UpdateGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_group(
              GroupName=\'string\',
              Description=\'string\'
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the resource group for which you want to update its description.
        
        :type Description: string
        :param Description: 
        
          The description of the resource group. Descriptions can have a maximum of 511 characters, including letters, numbers, hyphens, underscores, punctuation, and spaces.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Group\': {
                    \'GroupArn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Group** *(dict) --* 
        
              The full description of the resource group after it has been updated.
        
              - **GroupArn** *(string) --* 
        
                The ARN of a resource group.
        
              - **Name** *(string) --* 
        
                The name of a resource group.
        
              - **Description** *(string) --* 
        
                The description of the resource group.
        
        """
        pass

    def update_group_query(self, GroupName: str, ResourceQuery: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/UpdateGroupQuery>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_group_query(
              GroupName=\'string\',
              ResourceQuery={
                  \'Type\': \'TAG_FILTERS_1_0\',
                  \'Query\': \'string\'
              }
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the resource group for which you want to edit the query.
        
        :type ResourceQuery: dict
        :param ResourceQuery: **[REQUIRED]** 
        
          The resource query that determines which AWS resources are members of the resource group.
        
          - **Type** *(string) --* **[REQUIRED]** 
        
            The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .
        
             * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
        
          - **Query** *(string) --* **[REQUIRED]** 
        
            The query that defines a group or a search.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupQuery\': {
                    \'GroupName\': \'string\',
                    \'ResourceQuery\': {
                        \'Type\': \'TAG_FILTERS_1_0\',
                        \'Query\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **GroupQuery** *(dict) --* 
        
              The resource query associated with the resource group after the update.
        
              - **GroupName** *(string) --* 
        
                The name of a resource group that is associated with a specific resource query.
        
              - **ResourceQuery** *(dict) --* 
        
                The resource query which determines which AWS resources are members of the associated resource group.
        
                - **Type** *(string) --* 
        
                  The type of the query. The valid value in this release is ``TAG_FILTERS_1_0`` .
        
                   * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag filters for resource types and tags, as supported by the AWS Tagging API GetResources operation. When more than one element is present, only resources that match all filters are part of the result. If a filter specifies more than one value for a key, a resource matches the filter if its tag value matches any of the specified values.
        
                - **Query** *(string) --* 
        
                  The query that defines a group or a search.
        
        """
        pass
