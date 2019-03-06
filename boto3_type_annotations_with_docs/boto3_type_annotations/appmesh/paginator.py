from typing import Dict
from botocore.paginate import Paginator


class ListMeshes(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppMesh.Client.list_meshes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/ListMeshes>`_
        
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/ListRoutes>`_
        
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
                  The name of the service mesh in which the route resides.
                - **routeName** *(string) --* 
                  The name of the route.
                - **virtualRouterName** *(string) --* 
                  The virtual router with which the route is associated.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to list routes.
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router in which to list routes.
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/ListVirtualNodes>`_
        
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
                  The name of the service mesh in which the virtual node resides.
                - **virtualNodeName** *(string) --* 
                  The name of the virtual node.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to list virtual nodes.
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/ListVirtualRouters>`_
        
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
                  The name of the service mesh in which the virtual router resides.
                - **virtualRouterName** *(string) --* 
                  The name of the virtual router.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to list virtual routers.
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
