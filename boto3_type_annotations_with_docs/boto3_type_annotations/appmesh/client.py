from typing import Union
from botocore.paginate import Paginator
from botocore.client import BaseClient
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict


class Client(BaseClient):
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

    def create_mesh(self, meshName: str, clientToken: str = None) -> Dict:
        """
        Creates a new service mesh. A service mesh is a logical boundary for network traffic between the services that reside within it.
        After you create your service mesh, you can create virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/CreateMesh>`_
        
        **Request Syntax**
        ::
          response = client.create_mesh(
              clientToken='string',
              meshName='string'
          )
        
        **Response Syntax**
        ::
            {
                'mesh': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **mesh** *(dict) --* 
              The full description of your service mesh following the create call.
              - **meshName** *(string) --* 
                The name of the service mesh.
              - **metadata** *(dict) --* 
                The associated metadata for the service mesh.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **status** *(dict) --* 
                The status of the service mesh.
                - **status** *(string) --* 
                  The current mesh status.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
          This field is autopopulated if not provided.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name to use for the service mesh.
        :rtype: dict
        :returns:
        """
        pass

    def create_route(self, meshName: str, routeName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        """
        Creates a new route that is associated with a virtual router.
        You can use the ``prefix`` parameter in your route specification for path-based routing of requests. For example, if your virtual router service name is ``my-service.local`` , and you want the route to match requests to ``my-service.local/metrics`` , then your prefix should be ``/metrics`` .
        If your route matches a request, you can distribute traffic to one or more target virtual nodes with relative weighting.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/CreateRoute>`_
        
        **Request Syntax**
        ::
          response = client.create_route(
              clientToken='string',
              meshName='string',
              routeName='string',
              spec={
                  'httpRoute': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      },
                      'match': {
                          'prefix': 'string'
                      }
                  }
              },
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'route': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'routeName': 'string',
                    'spec': {
                        'httpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'prefix': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **route** *(dict) --* 
              The full description of your mesh following the create call.
              - **meshName** *(string) --* 
                The name of the service mesh in which the route resides.
              - **metadata** *(dict) --* 
                The associated metadata for the route.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **routeName** *(string) --* 
                The name of the route.
              - **spec** *(dict) --* 
                The specifications of the route.
                - **httpRoute** *(dict) --* 
                  The HTTP routing information for the route.
                  - **action** *(dict) --* 
                    The action to take if a match is determined.
                    - **weightedTargets** *(list) --* 
                      The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.
                      - *(dict) --* 
                        An object representing a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10.
                        - **virtualNode** *(string) --* 
                          The virtual node to associate with the weighted target.
                        - **weight** *(integer) --* 
                          The relative weight of the weighted target.
                  - **match** *(dict) --* 
                    The criteria for determining an HTTP request match.
                    - **prefix** *(string) --* 
                      Specifies the path with which to match requests. This parameter must always start with ``/`` , which by itself matches all requests to the virtual router service name. You can also match for path-based routing of requests. For example, if your virtual router service name is ``my-service.local`` , and you want the route to match requests to ``my-service.local/metrics`` , then your prefix should be ``/metrics`` .
              - **status** *(dict) --* 
                The status of the route.
                - **status** *(string) --* 
                  The current status for the route.
              - **virtualRouterName** *(string) --* 
                The virtual router with which the route is associated.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
          This field is autopopulated if not provided.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to create the route.
        :type routeName: string
        :param routeName: **[REQUIRED]**
          The name to use for the route.
        :type spec: dict
        :param spec: **[REQUIRED]**
          The route specification to apply.
          - **httpRoute** *(dict) --*
            The HTTP routing information for the route.
            - **action** *(dict) --*
              The action to take if a match is determined.
              - **weightedTargets** *(list) --*
                The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.
                - *(dict) --*
                  An object representing a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10.
                  - **virtualNode** *(string) --*
                    The virtual node to associate with the weighted target.
                  - **weight** *(integer) --*
                    The relative weight of the weighted target.
            - **match** *(dict) --*
              The criteria for determining an HTTP request match.
              - **prefix** *(string) --*
                Specifies the path with which to match requests. This parameter must always start with ``/`` , which by itself matches all requests to the virtual router service name. You can also match for path-based routing of requests. For example, if your virtual router service name is ``my-service.local`` , and you want the route to match requests to ``my-service.local/metrics`` , then your prefix should be ``/metrics`` .
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router in which to create the route.
        :rtype: dict
        :returns:
        """
        pass

    def create_virtual_node(self, meshName: str, spec: Dict, virtualNodeName: str, clientToken: str = None) -> Dict:
        """
        Creates a new virtual node within a service mesh.
        A virtual node acts as logical pointer to a particular task group, such as an Amazon ECS service or a Kubernetes deployment. When you create a virtual node, you must specify the DNS service discovery name for your task group.
        Any inbound traffic that your virtual node expects should be specified as a ``listener`` . Any outbound traffic that your virtual node expects to reach should be specified as a ``backend`` .
        The response metadata for your new virtual node contains the ``arn`` that is associated with the virtual node. Set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
        .. note::
          If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/CreateVirtualNode>`_
        
        **Request Syntax**
        ::
          response = client.create_virtual_node(
              clientToken='string',
              meshName='string',
              spec={
                  'backends': [
                      'string',
                  ],
                  'listeners': [
                      {
                          'healthCheck': {
                              'healthyThreshold': 123,
                              'intervalMillis': 123,
                              'path': 'string',
                              'port': 123,
                              'protocol': 'http'|'tcp',
                              'timeoutMillis': 123,
                              'unhealthyThreshold': 123
                          },
                          'portMapping': {
                              'port': 123,
                              'protocol': 'http'|'tcp'
                          }
                      },
                  ],
                  'serviceDiscovery': {
                      'dns': {
                          'serviceName': 'string'
                      }
                  }
              },
              virtualNodeName='string'
          )
        
        **Response Syntax**
        ::
            {
                'virtualNode': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'backends': [
                            'string',
                        ],
                        'listeners': [
                            {
                                'healthCheck': {
                                    'healthyThreshold': 123,
                                    'intervalMillis': 123,
                                    'path': 'string',
                                    'port': 123,
                                    'protocol': 'http'|'tcp',
                                    'timeoutMillis': 123,
                                    'unhealthyThreshold': 123
                                },
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'http'|'tcp'
                                }
                            },
                        ],
                        'serviceDiscovery': {
                            'dns': {
                                'serviceName': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualNodeName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualNode** *(dict) --* 
              The full description of your virtual node following the create call.
              - **meshName** *(string) --* 
                The name of the service mesh in which the virtual node resides.
              - **metadata** *(dict) --* 
                The associated metadata for the virtual node.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **spec** *(dict) --* 
                The specifications of the virtual node.
                - **backends** *(list) --* 
                  The backends to which the virtual node is expected to send outbound traffic.
                  - *(string) --* 
                - **listeners** *(list) --* 
                  The listeners from which the virtual node is expected to receive inbound traffic.
                  - *(dict) --* 
                    An object representing a listener for a virtual node.
                    - **healthCheck** *(dict) --* 
                      The health check information for the listener.
                      - **healthyThreshold** *(integer) --* 
                        The number of consecutive successful health checks that must occur before declaring listener healthy.
                      - **intervalMillis** *(integer) --* 
                        The time period in milliseconds between each health check execution.
                      - **path** *(string) --* 
                        The destination path for the health check request. This is only required if the specified protocol is HTTP; if the protocol is TCP, then this parameter is ignored.
                      - **port** *(integer) --* 
                        The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.
                      - **protocol** *(string) --* 
                        The protocol for the health check request.
                      - **timeoutMillis** *(integer) --* 
                        The amount of time to wait when receiving a response from the health check, in milliseconds.
                      - **unhealthyThreshold** *(integer) --* 
                        The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy. 
                    - **portMapping** *(dict) --* 
                      The port mapping information for the listener.
                      - **port** *(integer) --* 
                        The port used for the port mapping.
                      - **protocol** *(string) --* 
                        The protocol used for the port mapping.
                - **serviceDiscovery** *(dict) --* 
                  The service discovery information for the virtual node.
                  - **dns** *(dict) --* 
                    Specifies the DNS service name for the virtual node.
                    - **serviceName** *(string) --* 
                      The DNS service name for your virtual node.
              - **status** *(dict) --* 
                The current status for the virtual node.
                - **status** *(string) --* 
                  The current status of the virtual node.
              - **virtualNodeName** *(string) --* 
                The name of the virtual node.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
          This field is autopopulated if not provided.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to create the virtual node.
        :type spec: dict
        :param spec: **[REQUIRED]**
          The virtual node specification to apply.
          - **backends** *(list) --*
            The backends to which the virtual node is expected to send outbound traffic.
            - *(string) --*
          - **listeners** *(list) --*
            The listeners from which the virtual node is expected to receive inbound traffic.
            - *(dict) --*
              An object representing a listener for a virtual node.
              - **healthCheck** *(dict) --*
                The health check information for the listener.
                - **healthyThreshold** *(integer) --* **[REQUIRED]**
                  The number of consecutive successful health checks that must occur before declaring listener healthy.
                - **intervalMillis** *(integer) --* **[REQUIRED]**
                  The time period in milliseconds between each health check execution.
                - **path** *(string) --*
                  The destination path for the health check request. This is only required if the specified protocol is HTTP; if the protocol is TCP, then this parameter is ignored.
                - **port** *(integer) --*
                  The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.
                - **protocol** *(string) --* **[REQUIRED]**
                  The protocol for the health check request.
                - **timeoutMillis** *(integer) --* **[REQUIRED]**
                  The amount of time to wait when receiving a response from the health check, in milliseconds.
                - **unhealthyThreshold** *(integer) --* **[REQUIRED]**
                  The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
              - **portMapping** *(dict) --*
                The port mapping information for the listener.
                - **port** *(integer) --*
                  The port used for the port mapping.
                - **protocol** *(string) --*
                  The protocol used for the port mapping.
          - **serviceDiscovery** *(dict) --*
            The service discovery information for the virtual node.
            - **dns** *(dict) --*
              Specifies the DNS service name for the virtual node.
              - **serviceName** *(string) --*
                The DNS service name for your virtual node.
        :type virtualNodeName: string
        :param virtualNodeName: **[REQUIRED]**
          The name to use for the virtual node.
        :rtype: dict
        :returns:
        """
        pass

    def create_virtual_router(self, meshName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        """
        Creates a new virtual router within a service mesh.
        Virtual routers handle traffic for one or more service names within your mesh. After you create your virtual router, create and associate routes for your virtual router that direct incoming requests to different virtual nodes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/CreateVirtualRouter>`_
        
        **Request Syntax**
        ::
          response = client.create_virtual_router(
              clientToken='string',
              meshName='string',
              spec={
                  'serviceNames': [
                      'string',
                  ]
              },
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'virtualRouter': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'serviceNames': [
                            'string',
                        ]
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualRouter** *(dict) --* 
              The full description of your virtual router following the create call.
              - **meshName** *(string) --* 
                The name of the service mesh in which the virtual router resides.
              - **metadata** *(dict) --* 
                The associated metadata for the virtual router.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **spec** *(dict) --* 
                The specifications of the virtual router.
                - **serviceNames** *(list) --* 
                  The service mesh service names to associate with the virtual router.
                  - *(string) --* 
              - **status** *(dict) --* 
                The current status of the virtual router.
                - **status** *(string) --* 
                  The current status of the virtual router.
              - **virtualRouterName** *(string) --* 
                The name of the virtual router.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
          This field is autopopulated if not provided.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to create the virtual router.
        :type spec: dict
        :param spec: **[REQUIRED]**
          The virtual router specification to apply.
          - **serviceNames** *(list) --*
            The service mesh service names to associate with the virtual router.
            - *(string) --*
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name to use for the virtual router.
        :rtype: dict
        :returns:
        """
        pass

    def delete_mesh(self, meshName: str) -> Dict:
        """
        Deletes an existing service mesh.
        You must delete all resources (routes, virtual routers, virtual nodes) in the service mesh before you can delete the mesh itself.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/DeleteMesh>`_
        
        **Request Syntax**
        ::
          response = client.delete_mesh(
              meshName='string'
          )
        
        **Response Syntax**
        ::
            {
                'mesh': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **mesh** *(dict) --* 
              The service mesh that was deleted.
              - **meshName** *(string) --* 
                The name of the service mesh.
              - **metadata** *(dict) --* 
                The associated metadata for the service mesh.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **status** *(dict) --* 
                The status of the service mesh.
                - **status** *(string) --* 
                  The current mesh status.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_route(self, meshName: str, routeName: str, virtualRouterName: str) -> Dict:
        """
        Deletes an existing route.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/DeleteRoute>`_
        
        **Request Syntax**
        ::
          response = client.delete_route(
              meshName='string',
              routeName='string',
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'route': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'routeName': 'string',
                    'spec': {
                        'httpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'prefix': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **route** *(dict) --* 
              The route that was deleted.
              - **meshName** *(string) --* 
                The name of the service mesh in which the route resides.
              - **metadata** *(dict) --* 
                The associated metadata for the route.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **routeName** *(string) --* 
                The name of the route.
              - **spec** *(dict) --* 
                The specifications of the route.
                - **httpRoute** *(dict) --* 
                  The HTTP routing information for the route.
                  - **action** *(dict) --* 
                    The action to take if a match is determined.
                    - **weightedTargets** *(list) --* 
                      The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.
                      - *(dict) --* 
                        An object representing a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10.
                        - **virtualNode** *(string) --* 
                          The virtual node to associate with the weighted target.
                        - **weight** *(integer) --* 
                          The relative weight of the weighted target.
                  - **match** *(dict) --* 
                    The criteria for determining an HTTP request match.
                    - **prefix** *(string) --* 
                      Specifies the path with which to match requests. This parameter must always start with ``/`` , which by itself matches all requests to the virtual router service name. You can also match for path-based routing of requests. For example, if your virtual router service name is ``my-service.local`` , and you want the route to match requests to ``my-service.local/metrics`` , then your prefix should be ``/metrics`` .
              - **status** *(dict) --* 
                The status of the route.
                - **status** *(string) --* 
                  The current status for the route.
              - **virtualRouterName** *(string) --* 
                The virtual router with which the route is associated.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to delete the route.
        :type routeName: string
        :param routeName: **[REQUIRED]**
          The name of the route to delete.
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router in which to delete the route.
        :rtype: dict
        :returns:
        """
        pass

    def delete_virtual_node(self, meshName: str, virtualNodeName: str) -> Dict:
        """
        Deletes an existing virtual node.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/DeleteVirtualNode>`_
        
        **Request Syntax**
        ::
          response = client.delete_virtual_node(
              meshName='string',
              virtualNodeName='string'
          )
        
        **Response Syntax**
        ::
            {
                'virtualNode': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'backends': [
                            'string',
                        ],
                        'listeners': [
                            {
                                'healthCheck': {
                                    'healthyThreshold': 123,
                                    'intervalMillis': 123,
                                    'path': 'string',
                                    'port': 123,
                                    'protocol': 'http'|'tcp',
                                    'timeoutMillis': 123,
                                    'unhealthyThreshold': 123
                                },
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'http'|'tcp'
                                }
                            },
                        ],
                        'serviceDiscovery': {
                            'dns': {
                                'serviceName': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualNodeName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualNode** *(dict) --* 
              The virtual node that was deleted.
              - **meshName** *(string) --* 
                The name of the service mesh in which the virtual node resides.
              - **metadata** *(dict) --* 
                The associated metadata for the virtual node.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **spec** *(dict) --* 
                The specifications of the virtual node.
                - **backends** *(list) --* 
                  The backends to which the virtual node is expected to send outbound traffic.
                  - *(string) --* 
                - **listeners** *(list) --* 
                  The listeners from which the virtual node is expected to receive inbound traffic.
                  - *(dict) --* 
                    An object representing a listener for a virtual node.
                    - **healthCheck** *(dict) --* 
                      The health check information for the listener.
                      - **healthyThreshold** *(integer) --* 
                        The number of consecutive successful health checks that must occur before declaring listener healthy.
                      - **intervalMillis** *(integer) --* 
                        The time period in milliseconds between each health check execution.
                      - **path** *(string) --* 
                        The destination path for the health check request. This is only required if the specified protocol is HTTP; if the protocol is TCP, then this parameter is ignored.
                      - **port** *(integer) --* 
                        The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.
                      - **protocol** *(string) --* 
                        The protocol for the health check request.
                      - **timeoutMillis** *(integer) --* 
                        The amount of time to wait when receiving a response from the health check, in milliseconds.
                      - **unhealthyThreshold** *(integer) --* 
                        The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy. 
                    - **portMapping** *(dict) --* 
                      The port mapping information for the listener.
                      - **port** *(integer) --* 
                        The port used for the port mapping.
                      - **protocol** *(string) --* 
                        The protocol used for the port mapping.
                - **serviceDiscovery** *(dict) --* 
                  The service discovery information for the virtual node.
                  - **dns** *(dict) --* 
                    Specifies the DNS service name for the virtual node.
                    - **serviceName** *(string) --* 
                      The DNS service name for your virtual node.
              - **status** *(dict) --* 
                The current status for the virtual node.
                - **status** *(string) --* 
                  The current status of the virtual node.
              - **virtualNodeName** *(string) --* 
                The name of the virtual node.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to delete the virtual node.
        :type virtualNodeName: string
        :param virtualNodeName: **[REQUIRED]**
          The name of the virtual node to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_virtual_router(self, meshName: str, virtualRouterName: str) -> Dict:
        """
        Deletes an existing virtual router.
        You must delete any routes associated with the virtual router before you can delete the router itself.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/DeleteVirtualRouter>`_
        
        **Request Syntax**
        ::
          response = client.delete_virtual_router(
              meshName='string',
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'virtualRouter': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'serviceNames': [
                            'string',
                        ]
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualRouter** *(dict) --* 
              The virtual router that was deleted.
              - **meshName** *(string) --* 
                The name of the service mesh in which the virtual router resides.
              - **metadata** *(dict) --* 
                The associated metadata for the virtual router.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **spec** *(dict) --* 
                The specifications of the virtual router.
                - **serviceNames** *(list) --* 
                  The service mesh service names to associate with the virtual router.
                  - *(string) --* 
              - **status** *(dict) --* 
                The current status of the virtual router.
                - **status** *(string) --* 
                  The current status of the virtual router.
              - **virtualRouterName** *(string) --* 
                The name of the virtual router.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to delete the virtual router.
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router to delete.
        :rtype: dict
        :returns:
        """
        pass

    def describe_mesh(self, meshName: str) -> Dict:
        """
        Describes an existing service mesh.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/DescribeMesh>`_
        
        **Request Syntax**
        ::
          response = client.describe_mesh(
              meshName='string'
          )
        
        **Response Syntax**
        ::
            {
                'mesh': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **mesh** *(dict) --* 
              The full description of your service mesh.
              - **meshName** *(string) --* 
                The name of the service mesh.
              - **metadata** *(dict) --* 
                The associated metadata for the service mesh.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **status** *(dict) --* 
                The status of the service mesh.
                - **status** *(string) --* 
                  The current mesh status.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_route(self, meshName: str, routeName: str, virtualRouterName: str) -> Dict:
        """
        Describes an existing route.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/DescribeRoute>`_
        
        **Request Syntax**
        ::
          response = client.describe_route(
              meshName='string',
              routeName='string',
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'route': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'routeName': 'string',
                    'spec': {
                        'httpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'prefix': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **route** *(dict) --* 
              The full description of your route.
              - **meshName** *(string) --* 
                The name of the service mesh in which the route resides.
              - **metadata** *(dict) --* 
                The associated metadata for the route.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **routeName** *(string) --* 
                The name of the route.
              - **spec** *(dict) --* 
                The specifications of the route.
                - **httpRoute** *(dict) --* 
                  The HTTP routing information for the route.
                  - **action** *(dict) --* 
                    The action to take if a match is determined.
                    - **weightedTargets** *(list) --* 
                      The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.
                      - *(dict) --* 
                        An object representing a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10.
                        - **virtualNode** *(string) --* 
                          The virtual node to associate with the weighted target.
                        - **weight** *(integer) --* 
                          The relative weight of the weighted target.
                  - **match** *(dict) --* 
                    The criteria for determining an HTTP request match.
                    - **prefix** *(string) --* 
                      Specifies the path with which to match requests. This parameter must always start with ``/`` , which by itself matches all requests to the virtual router service name. You can also match for path-based routing of requests. For example, if your virtual router service name is ``my-service.local`` , and you want the route to match requests to ``my-service.local/metrics`` , then your prefix should be ``/metrics`` .
              - **status** *(dict) --* 
                The status of the route.
                - **status** *(string) --* 
                  The current status for the route.
              - **virtualRouterName** *(string) --* 
                The virtual router with which the route is associated.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which the route resides.
        :type routeName: string
        :param routeName: **[REQUIRED]**
          The name of the route to describe.
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router with which the route is associated.
        :rtype: dict
        :returns:
        """
        pass

    def describe_virtual_node(self, meshName: str, virtualNodeName: str) -> Dict:
        """
        Describes an existing virtual node.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/DescribeVirtualNode>`_
        
        **Request Syntax**
        ::
          response = client.describe_virtual_node(
              meshName='string',
              virtualNodeName='string'
          )
        
        **Response Syntax**
        ::
            {
                'virtualNode': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'backends': [
                            'string',
                        ],
                        'listeners': [
                            {
                                'healthCheck': {
                                    'healthyThreshold': 123,
                                    'intervalMillis': 123,
                                    'path': 'string',
                                    'port': 123,
                                    'protocol': 'http'|'tcp',
                                    'timeoutMillis': 123,
                                    'unhealthyThreshold': 123
                                },
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'http'|'tcp'
                                }
                            },
                        ],
                        'serviceDiscovery': {
                            'dns': {
                                'serviceName': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualNodeName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualNode** *(dict) --* 
              The full description of your virtual node.
              - **meshName** *(string) --* 
                The name of the service mesh in which the virtual node resides.
              - **metadata** *(dict) --* 
                The associated metadata for the virtual node.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **spec** *(dict) --* 
                The specifications of the virtual node.
                - **backends** *(list) --* 
                  The backends to which the virtual node is expected to send outbound traffic.
                  - *(string) --* 
                - **listeners** *(list) --* 
                  The listeners from which the virtual node is expected to receive inbound traffic.
                  - *(dict) --* 
                    An object representing a listener for a virtual node.
                    - **healthCheck** *(dict) --* 
                      The health check information for the listener.
                      - **healthyThreshold** *(integer) --* 
                        The number of consecutive successful health checks that must occur before declaring listener healthy.
                      - **intervalMillis** *(integer) --* 
                        The time period in milliseconds between each health check execution.
                      - **path** *(string) --* 
                        The destination path for the health check request. This is only required if the specified protocol is HTTP; if the protocol is TCP, then this parameter is ignored.
                      - **port** *(integer) --* 
                        The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.
                      - **protocol** *(string) --* 
                        The protocol for the health check request.
                      - **timeoutMillis** *(integer) --* 
                        The amount of time to wait when receiving a response from the health check, in milliseconds.
                      - **unhealthyThreshold** *(integer) --* 
                        The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy. 
                    - **portMapping** *(dict) --* 
                      The port mapping information for the listener.
                      - **port** *(integer) --* 
                        The port used for the port mapping.
                      - **protocol** *(string) --* 
                        The protocol used for the port mapping.
                - **serviceDiscovery** *(dict) --* 
                  The service discovery information for the virtual node.
                  - **dns** *(dict) --* 
                    Specifies the DNS service name for the virtual node.
                    - **serviceName** *(string) --* 
                      The DNS service name for your virtual node.
              - **status** *(dict) --* 
                The current status for the virtual node.
                - **status** *(string) --* 
                  The current status of the virtual node.
              - **virtualNodeName** *(string) --* 
                The name of the virtual node.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which the virtual node resides.
        :type virtualNodeName: string
        :param virtualNodeName: **[REQUIRED]**
          The name of the virtual node to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_virtual_router(self, meshName: str, virtualRouterName: str) -> Dict:
        """
        Describes an existing virtual router.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/DescribeVirtualRouter>`_
        
        **Request Syntax**
        ::
          response = client.describe_virtual_router(
              meshName='string',
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'virtualRouter': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'serviceNames': [
                            'string',
                        ]
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualRouter** *(dict) --* 
              The full description of your virtual router.
              - **meshName** *(string) --* 
                The name of the service mesh in which the virtual router resides.
              - **metadata** *(dict) --* 
                The associated metadata for the virtual router.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **spec** *(dict) --* 
                The specifications of the virtual router.
                - **serviceNames** *(list) --* 
                  The service mesh service names to associate with the virtual router.
                  - *(string) --* 
              - **status** *(dict) --* 
                The current status of the virtual router.
                - **status** *(string) --* 
                  The current status of the virtual router.
              - **virtualRouterName** *(string) --* 
                The name of the virtual router.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which the virtual router resides.
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router to describe.
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

    def list_meshes(self, limit: int = None, nextToken: str = None) -> Dict:
        """
        Returns a list of existing service meshes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/ListMeshes>`_
        
        **Request Syntax**
        ::
          response = client.list_meshes(
              limit=123,
              nextToken='string'
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
                'nextToken': 'string'
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
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListMeshes`` request. When the results of a ``ListMeshes`` request exceed ``limit`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type limit: integer
        :param limit:
          The maximum number of mesh results returned by ``ListMeshes`` in paginated output. When this parameter is used, ``ListMeshes`` only returns ``limit`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListMeshes`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListMeshes`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListMeshes`` request where ``limit`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :rtype: dict
        :returns:
        """
        pass

    def list_routes(self, meshName: str, virtualRouterName: str, limit: int = None, nextToken: str = None) -> Dict:
        """
        Returns a list of existing routes in a service mesh.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/ListRoutes>`_
        
        **Request Syntax**
        ::
          response = client.list_routes(
              limit=123,
              meshName='string',
              nextToken='string',
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'nextToken': 'string',
                'routes': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'routeName': 'string',
                        'virtualRouterName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListRoutes`` request. When the results of a ``ListRoutes`` request exceed ``limit`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
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
        :type limit: integer
        :param limit:
          The maximum number of mesh results returned by ``ListRoutes`` in paginated output. When this parameter is used, ``ListRoutes`` only returns ``limit`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListRoutes`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListRoutes`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to list routes.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListRoutes`` request where ``limit`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router in which to list routes.
        :rtype: dict
        :returns:
        """
        pass

    def list_virtual_nodes(self, meshName: str, limit: int = None, nextToken: str = None) -> Dict:
        """
        Returns a list of existing virtual nodes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/ListVirtualNodes>`_
        
        **Request Syntax**
        ::
          response = client.list_virtual_nodes(
              limit=123,
              meshName='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'nextToken': 'string',
                'virtualNodes': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'virtualNodeName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListVirtualNodes`` request. When the results of a ``ListVirtualNodes`` request exceed ``limit`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
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
        :type limit: integer
        :param limit:
          The maximum number of mesh results returned by ``ListVirtualNodes`` in paginated output. When this parameter is used, ``ListVirtualNodes`` only returns ``limit`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListVirtualNodes`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListVirtualNodes`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to list virtual nodes.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListVirtualNodes`` request where ``limit`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
        :rtype: dict
        :returns:
        """
        pass

    def list_virtual_routers(self, meshName: str, limit: int = None, nextToken: str = None) -> Dict:
        """
        Returns a list of existing virtual routers in a service mesh.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/ListVirtualRouters>`_
        
        **Request Syntax**
        ::
          response = client.list_virtual_routers(
              limit=123,
              meshName='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'nextToken': 'string',
                'virtualRouters': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'virtualRouterName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListVirtualRouters`` request. When the results of a ``ListVirtualRouters`` request exceed ``limit`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
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
        :type limit: integer
        :param limit:
          The maximum number of mesh results returned by ``ListVirtualRouters`` in paginated output. When this parameter is used, ``ListVirtualRouters`` only returns ``limit`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListVirtualRouters`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListVirtualRouters`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which to list virtual routers.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListVirtualRouters`` request where ``limit`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
        :rtype: dict
        :returns:
        """
        pass

    def update_route(self, meshName: str, routeName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        """
        Updates an existing route for a specified service mesh and virtual router.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/UpdateRoute>`_
        
        **Request Syntax**
        ::
          response = client.update_route(
              clientToken='string',
              meshName='string',
              routeName='string',
              spec={
                  'httpRoute': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      },
                      'match': {
                          'prefix': 'string'
                      }
                  }
              },
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'route': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'routeName': 'string',
                    'spec': {
                        'httpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'prefix': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **route** *(dict) --* 
              A full description of the route that was updated.
              - **meshName** *(string) --* 
                The name of the service mesh in which the route resides.
              - **metadata** *(dict) --* 
                The associated metadata for the route.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **routeName** *(string) --* 
                The name of the route.
              - **spec** *(dict) --* 
                The specifications of the route.
                - **httpRoute** *(dict) --* 
                  The HTTP routing information for the route.
                  - **action** *(dict) --* 
                    The action to take if a match is determined.
                    - **weightedTargets** *(list) --* 
                      The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.
                      - *(dict) --* 
                        An object representing a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10.
                        - **virtualNode** *(string) --* 
                          The virtual node to associate with the weighted target.
                        - **weight** *(integer) --* 
                          The relative weight of the weighted target.
                  - **match** *(dict) --* 
                    The criteria for determining an HTTP request match.
                    - **prefix** *(string) --* 
                      Specifies the path with which to match requests. This parameter must always start with ``/`` , which by itself matches all requests to the virtual router service name. You can also match for path-based routing of requests. For example, if your virtual router service name is ``my-service.local`` , and you want the route to match requests to ``my-service.local/metrics`` , then your prefix should be ``/metrics`` .
              - **status** *(dict) --* 
                The status of the route.
                - **status** *(string) --* 
                  The current status for the route.
              - **virtualRouterName** *(string) --* 
                The virtual router with which the route is associated.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
          This field is autopopulated if not provided.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which the route resides.
        :type routeName: string
        :param routeName: **[REQUIRED]**
          The name of the route to update.
        :type spec: dict
        :param spec: **[REQUIRED]**
          The new route specification to apply. This overwrites the existing data.
          - **httpRoute** *(dict) --*
            The HTTP routing information for the route.
            - **action** *(dict) --*
              The action to take if a match is determined.
              - **weightedTargets** *(list) --*
                The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.
                - *(dict) --*
                  An object representing a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10.
                  - **virtualNode** *(string) --*
                    The virtual node to associate with the weighted target.
                  - **weight** *(integer) --*
                    The relative weight of the weighted target.
            - **match** *(dict) --*
              The criteria for determining an HTTP request match.
              - **prefix** *(string) --*
                Specifies the path with which to match requests. This parameter must always start with ``/`` , which by itself matches all requests to the virtual router service name. You can also match for path-based routing of requests. For example, if your virtual router service name is ``my-service.local`` , and you want the route to match requests to ``my-service.local/metrics`` , then your prefix should be ``/metrics`` .
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router with which the route is associated.
        :rtype: dict
        :returns:
        """
        pass

    def update_virtual_node(self, meshName: str, spec: Dict, virtualNodeName: str, clientToken: str = None) -> Dict:
        """
        Updates an existing virtual node in a specified service mesh.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/UpdateVirtualNode>`_
        
        **Request Syntax**
        ::
          response = client.update_virtual_node(
              clientToken='string',
              meshName='string',
              spec={
                  'backends': [
                      'string',
                  ],
                  'listeners': [
                      {
                          'healthCheck': {
                              'healthyThreshold': 123,
                              'intervalMillis': 123,
                              'path': 'string',
                              'port': 123,
                              'protocol': 'http'|'tcp',
                              'timeoutMillis': 123,
                              'unhealthyThreshold': 123
                          },
                          'portMapping': {
                              'port': 123,
                              'protocol': 'http'|'tcp'
                          }
                      },
                  ],
                  'serviceDiscovery': {
                      'dns': {
                          'serviceName': 'string'
                      }
                  }
              },
              virtualNodeName='string'
          )
        
        **Response Syntax**
        ::
            {
                'virtualNode': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'backends': [
                            'string',
                        ],
                        'listeners': [
                            {
                                'healthCheck': {
                                    'healthyThreshold': 123,
                                    'intervalMillis': 123,
                                    'path': 'string',
                                    'port': 123,
                                    'protocol': 'http'|'tcp',
                                    'timeoutMillis': 123,
                                    'unhealthyThreshold': 123
                                },
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'http'|'tcp'
                                }
                            },
                        ],
                        'serviceDiscovery': {
                            'dns': {
                                'serviceName': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualNodeName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualNode** *(dict) --* 
              A full description of the virtual node that was updated.
              - **meshName** *(string) --* 
                The name of the service mesh in which the virtual node resides.
              - **metadata** *(dict) --* 
                The associated metadata for the virtual node.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **spec** *(dict) --* 
                The specifications of the virtual node.
                - **backends** *(list) --* 
                  The backends to which the virtual node is expected to send outbound traffic.
                  - *(string) --* 
                - **listeners** *(list) --* 
                  The listeners from which the virtual node is expected to receive inbound traffic.
                  - *(dict) --* 
                    An object representing a listener for a virtual node.
                    - **healthCheck** *(dict) --* 
                      The health check information for the listener.
                      - **healthyThreshold** *(integer) --* 
                        The number of consecutive successful health checks that must occur before declaring listener healthy.
                      - **intervalMillis** *(integer) --* 
                        The time period in milliseconds between each health check execution.
                      - **path** *(string) --* 
                        The destination path for the health check request. This is only required if the specified protocol is HTTP; if the protocol is TCP, then this parameter is ignored.
                      - **port** *(integer) --* 
                        The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.
                      - **protocol** *(string) --* 
                        The protocol for the health check request.
                      - **timeoutMillis** *(integer) --* 
                        The amount of time to wait when receiving a response from the health check, in milliseconds.
                      - **unhealthyThreshold** *(integer) --* 
                        The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy. 
                    - **portMapping** *(dict) --* 
                      The port mapping information for the listener.
                      - **port** *(integer) --* 
                        The port used for the port mapping.
                      - **protocol** *(string) --* 
                        The protocol used for the port mapping.
                - **serviceDiscovery** *(dict) --* 
                  The service discovery information for the virtual node.
                  - **dns** *(dict) --* 
                    Specifies the DNS service name for the virtual node.
                    - **serviceName** *(string) --* 
                      The DNS service name for your virtual node.
              - **status** *(dict) --* 
                The current status for the virtual node.
                - **status** *(string) --* 
                  The current status of the virtual node.
              - **virtualNodeName** *(string) --* 
                The name of the virtual node.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
          This field is autopopulated if not provided.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which the virtual node resides.
        :type spec: dict
        :param spec: **[REQUIRED]**
          The new virtual node specification to apply. This overwrites the existing data.
          - **backends** *(list) --*
            The backends to which the virtual node is expected to send outbound traffic.
            - *(string) --*
          - **listeners** *(list) --*
            The listeners from which the virtual node is expected to receive inbound traffic.
            - *(dict) --*
              An object representing a listener for a virtual node.
              - **healthCheck** *(dict) --*
                The health check information for the listener.
                - **healthyThreshold** *(integer) --* **[REQUIRED]**
                  The number of consecutive successful health checks that must occur before declaring listener healthy.
                - **intervalMillis** *(integer) --* **[REQUIRED]**
                  The time period in milliseconds between each health check execution.
                - **path** *(string) --*
                  The destination path for the health check request. This is only required if the specified protocol is HTTP; if the protocol is TCP, then this parameter is ignored.
                - **port** *(integer) --*
                  The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.
                - **protocol** *(string) --* **[REQUIRED]**
                  The protocol for the health check request.
                - **timeoutMillis** *(integer) --* **[REQUIRED]**
                  The amount of time to wait when receiving a response from the health check, in milliseconds.
                - **unhealthyThreshold** *(integer) --* **[REQUIRED]**
                  The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
              - **portMapping** *(dict) --*
                The port mapping information for the listener.
                - **port** *(integer) --*
                  The port used for the port mapping.
                - **protocol** *(string) --*
                  The protocol used for the port mapping.
          - **serviceDiscovery** *(dict) --*
            The service discovery information for the virtual node.
            - **dns** *(dict) --*
              Specifies the DNS service name for the virtual node.
              - **serviceName** *(string) --*
                The DNS service name for your virtual node.
        :type virtualNodeName: string
        :param virtualNodeName: **[REQUIRED]**
          The name of the virtual node to update.
        :rtype: dict
        :returns:
        """
        pass

    def update_virtual_router(self, meshName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        """
        Updates an existing virtual router in a specified service mesh.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2018-10-01/UpdateVirtualRouter>`_
        
        **Request Syntax**
        ::
          response = client.update_virtual_router(
              clientToken='string',
              meshName='string',
              spec={
                  'serviceNames': [
                      'string',
                  ]
              },
              virtualRouterName='string'
          )
        
        **Response Syntax**
        ::
            {
                'virtualRouter': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'serviceNames': [
                            'string',
                        ]
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **virtualRouter** *(dict) --* 
              A full description of the virtual router that was updated.
              - **meshName** *(string) --* 
                The name of the service mesh in which the virtual router resides.
              - **metadata** *(dict) --* 
                The associated metadata for the virtual router.
                - **arn** *(string) --* 
                  The full Amazon Resource Name (ARN) for the resource.
                  .. note::
                    After you create a virtual node, set this value (either the full ARN or the truncated resource name, for example, ``mesh/default/virtualNode/simpleapp`` , as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.
                    If you require your Envoy stats or tracing to use a different name, you can override the ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.
                - **createdAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The Unix epoch timestamp in seconds for when the resource was last updated.
                - **uid** *(string) --* 
                  The unique identifier for the resource.
                - **version** *(integer) --* 
                  The version of the resource. Resources are created at version 1, and this version is incremented each time they are updated.
              - **spec** *(dict) --* 
                The specifications of the virtual router.
                - **serviceNames** *(list) --* 
                  The service mesh service names to associate with the virtual router.
                  - *(string) --* 
              - **status** *(dict) --* 
                The current status of the virtual router.
                - **status** *(string) --* 
                  The current status of the virtual router.
              - **virtualRouterName** *(string) --* 
                The name of the virtual router.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
          This field is autopopulated if not provided.
        :type meshName: string
        :param meshName: **[REQUIRED]**
          The name of the service mesh in which the virtual router resides.
        :type spec: dict
        :param spec: **[REQUIRED]**
          The new virtual router specification to apply. This overwrites the existing data.
          - **serviceNames** *(list) --*
            The service mesh service names to associate with the virtual router.
            - *(string) --*
        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**
          The name of the virtual router to update.
        :rtype: dict
        :returns:
        """
        pass
