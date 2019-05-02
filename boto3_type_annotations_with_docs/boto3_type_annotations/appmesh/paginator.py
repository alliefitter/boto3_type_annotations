from typing import Dict
from botocore.paginate import Paginator


class ListMeshes(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppMesh.Client.list_meshes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListMeshes>`_
        
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
                'meshes': [
                    {
                        'arn': 'string',
                        'meshName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **meshes** *(list) --* 
              The list of existing service meshes.
              - *(dict) --* 
                An object representing a service mesh returned by a list operation.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) of the service mesh.
                - **meshName** *(string) --* 
                  The name of the service mesh.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListRoutes(Paginator):
    def paginate(self, meshName: str, virtualRouterName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppMesh.Client.list_routes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListRoutes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              meshName='string',
              virtualRouterName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'routes': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'routeName': 'string',
                        'virtualRouterName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **routes** *(list) --* 
              The list of existing routes for the specified service mesh and virtual router.
              - *(dict) --* 
                An object representing a route returned by a list operation.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the route.
                - **meshName** *(string) --* 
                  The name of the service mesh that the route resides in.
                - **routeName** *(string) --* 
                  The name of the route.
                - **virtualRouterName** *(string) --* 
                  The virtual router that the route is associated with.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh to list routes in.
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router to list routes in.
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


class ListTagsForResource(Paginator):
    def paginate(self, resourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppMesh.Client.list_tags_for_resource`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              resourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tags** *(list) --* 
              The tags for the resource.
              - *(dict) --* 
                Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - **key** *(string) --* 
                  One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                - **value** *(string) --* 
                  The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that identifies the resource to list the tags for.
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


class ListVirtualNodes(Paginator):
    def paginate(self, meshName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppMesh.Client.list_virtual_nodes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListVirtualNodes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              meshName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'virtualNodes': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'virtualNodeName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualNodes** *(list) --* 
              The list of existing virtual nodes for the specified service mesh.
              - *(dict) --* 
                An object representing a virtual node returned by a list operation.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the virtual node.
                - **meshName** *(string) --* 
                  The name of the service mesh that the virtual node resides in.
                - **virtualNodeName** *(string) --* 
                  The name of the virtual node.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh to list virtual nodes in.
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


class ListVirtualRouters(Paginator):
    def paginate(self, meshName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppMesh.Client.list_virtual_routers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListVirtualRouters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              meshName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'virtualRouters': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'virtualRouterName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualRouters** *(list) --* 
              The list of existing virtual routers for the specified service mesh.
              - *(dict) --* 
                An object representing a virtual router returned by a list operation.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the virtual router.
                - **meshName** *(string) --* 
                  The name of the service mesh that the virtual router resides in.
                - **virtualRouterName** *(string) --* 
                  The name of the virtual router.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh to list virtual routers in.
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


class ListVirtualServices(Paginator):
    def paginate(self, meshName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppMesh.Client.list_virtual_services`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListVirtualServices>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              meshName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'virtualServices': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'virtualServiceName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualServices** *(list) --* 
              The list of existing virtual services for the specified service mesh.
              - *(dict) --* 
                An object representing a virtual service returned by a list operation.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the virtual service.
                - **meshName** *(string) --* 
                  The name of the service mesh that the virtual service resides in.
                - **virtualServiceName** *(string) --* 
                  The name of the virtual service.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh to list virtual services in.
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
