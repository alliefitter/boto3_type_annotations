from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListInstances(Paginator):
    def paginate(self, ServiceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ServiceId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]** 
        
          The ID of the service that you want to list instances for.
        
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
                \'Instances\': [
                    {
                        \'Id\': \'string\',
                        \'Attributes\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Instances** *(list) --* 
        
              Summary information about the instances that are associated with the specified service.
        
              - *(dict) --* 
        
                A complex type that contains information about the instances that you registered by using a specified service.
        
                - **Id** *(string) --* 
        
                  The ID for an instance that you created by using a specified service.
        
                - **Attributes** *(dict) --* 
        
                  A string map that contains the following information:
        
                  * The attributes that are associate with the instance.  
                   
                  * For each attribute, the applicable value. 
                   
                  Supported attribute keys include the following:
        
                  * ``AWS_ALIAS_DNS_NAME`` : For an alias record that routes traffic to an Elastic Load Balancing load balancer, the DNS name that is associated with the load balancer.  
                   
                  * ``AWS_INSTANCE_CNAME`` : For a CNAME record, the domain name that Route 53 returns in response to DNS queries, for example, ``example.com`` . 
                   
                  * ``AWS_INSTANCE_IPV4`` : For an A record, the IPv4 address that Route 53 returns in response to DNS queries, for example, ``192.0.2.44`` . 
                   
                  * ``AWS_INSTANCE_IPV6`` : For an AAAA record, the IPv6 address that Route 53 returns in response to DNS queries, for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . 
                   
                  * ``AWS_INSTANCE_PORT`` : For an SRV record, the value that Route 53 returns for the port. In addition, if the service includes ``HealthCheckConfig`` , the port on the endpoint that Route 53 sends requests to. 
                   
                  - *(string) --* 
                    
                    - *(string) --* 
              
        """
        pass


class ListNamespaces(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListNamespaces>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'TYPE\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Condition\': \'EQ\'|\'IN\'|\'BETWEEN\'
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
        
          A complex type that contains specifications for the namespaces that you want to list.
        
          If you specify more than one filter, a namespace must match all filters to be returned by ``ListNamespaces`` .
        
          - *(dict) --* 
        
            A complex type that identifies the namespaces that you want to list. You can choose to list public or private namespaces.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              Specify ``TYPE`` .
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              If you specify ``EQ`` for ``Condition`` , specify either ``DNS_PUBLIC`` or ``DNS_PRIVATE`` .
        
              If you specify ``IN`` for ``Condition`` , you can specify ``DNS_PUBLIC`` , ``DNS_PRIVATE`` , or both.
        
              - *(string) --* 
        
            - **Condition** *(string) --* 
        
              The operator that you want to use to determine whether ``ListNamespaces`` returns a namespace. Valid values for ``condition`` include:
        
              * ``EQ`` : When you specify ``EQ`` for the condition, you can choose to list only public namespaces or private namespaces, but not both. ``EQ`` is the default condition and can be omitted. 
               
              * ``IN`` : When you specify ``IN`` for the condition, you can choose to list public namespaces, private namespaces, or both.  
               
              * ``BETWEEN`` : Not applicable 
               
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
                \'Namespaces\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Type\': \'DNS_PUBLIC\'|\'DNS_PRIVATE\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Namespaces** *(list) --* 
        
              An array that contains one ``NamespaceSummary`` object for each namespace that matches the specified filter criteria.
        
              - *(dict) --* 
        
                A complex type that contains information about a namespace.
        
                - **Id** *(string) --* 
        
                  The ID of the namespace.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that Route 53 assigns to the namespace when you create it.
        
                - **Name** *(string) --* 
        
                  The name of the namespace. When you create a namespace, Route 53 automatically creates a hosted zone that has the same name as the namespace.
        
                - **Type** *(string) --* 
        
                  The type of the namespace, either public or private.
        
        """
        pass


class ListOperations(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListOperations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'NAMESPACE_ID\'|\'SERVICE_ID\'|\'STATUS\'|\'TYPE\'|\'UPDATE_DATE\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Condition\': \'EQ\'|\'IN\'|\'BETWEEN\'
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
        
          A complex type that contains specifications for the operations that you want to list, for example, operations that you started between a specified start date and end date.
        
          If you specify more than one filter, an operation must match all filters to be returned by ``ListOperations`` .
        
          - *(dict) --* 
        
            A complex type that lets you select the operations that you want to list.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              Specify the operations that you want to get:
        
              * **NAMESPACE_ID** : Gets operations related to specified namespaces. 
               
              * **SERVICE_ID** : Gets operations related to specified services. 
               
              * **STATUS** : Gets operations based on the status of the operations: ``SUBMITTED`` , ``PENDING`` , ``SUCCEED`` , or ``FAIL`` . 
               
              * **TYPE** : Gets specified types of operation. 
               
              * **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.  
               
            - **Values** *(list) --* **[REQUIRED]** 
        
              Specify values that are applicable to the value that you specify for ``Name`` : 
        
              * **NAMESPACE_ID** : Specify one namespace ID. 
               
              * **SERVICE_ID** : Specify one service ID. 
               
              * **STATUS** : Specify one or more statuses: ``SUBMITTED`` , ``PENDING`` , ``SUCCEED`` , or ``FAIL`` . 
               
              * **TYPE** : Specify one or more of the following types: ``CREATE_NAMESPACE`` , ``DELETE_NAMESPACE`` , ``UPDATE_SERVICE`` , ``REGISTER_INSTANCE`` , or ``DEREGISTER_INSTANCE`` . 
               
              * **UPDATE_DATE** : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. 
               
              - *(string) --* 
        
            - **Condition** *(string) --* 
        
              The operator that you want to use to determine whether an operation matches the specified value. Valid values for condition include:
        
              * ``EQ`` : When you specify ``EQ`` for the condition, you can specify only one value. ``EQ`` is supported for ``NAMESPACE_ID`` , ``SERVICE_ID`` , ``STATUS`` , and ``TYPE`` . ``EQ`` is the default condition and can be omitted. 
               
              * ``IN`` : When you specify ``IN`` for the condition, you can specify a list of one or more values. ``IN`` is supported for ``STATUS`` and ``TYPE`` . An operation must match one of the specified values to be returned in the response. 
               
              * ``BETWEEN`` : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. ``BETWEEN`` is supported for ``UPDATE_DATE`` .  
               
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
                \'Operations\': [
                    {
                        \'Id\': \'string\',
                        \'Status\': \'SUBMITTED\'|\'PENDING\'|\'SUCCESS\'|\'FAIL\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Operations** *(list) --* 
        
              Summary information about the operations that match the specified criteria.
        
              - *(dict) --* 
        
                A complex type that contains information about an operation that matches the criteria that you specified in a  ListOperations request.
        
                - **Id** *(string) --* 
        
                  The ID for an operation.
        
                - **Status** *(string) --* 
        
                  The status of the operation. Values include the following:
        
                  * **SUBMITTED** : This is the initial state immediately after you submit a request. 
                   
                  * **PENDING** : Route 53 is performing the operation. 
                   
                  * **SUCCESS** : The operation succeeded. 
                   
                  * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` . 
                   
        """
        pass


class ListServices(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListServices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'NAMESPACE_ID\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Condition\': \'EQ\'|\'IN\'|\'BETWEEN\'
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
        
          A complex type that contains specifications for the namespaces that you want to list services for. 
        
          If you specify more than one filter, an operation must match all filters to be returned by ``ListServices`` .
        
          - *(dict) --* 
        
            A complex type that lets you specify the namespaces that you want to list services for.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              Specify ``NAMESPACE_ID`` .
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The values that are applicable to the value that you specify for ``Condition`` to filter the list of services.
        
              - *(string) --* 
        
            - **Condition** *(string) --* 
        
              The operator that you want to use to determine whether a service is returned by ``ListServices`` . Valid values for ``Condition`` include the following:
        
              * ``EQ`` : When you specify ``EQ`` , specify one namespace ID for ``Values`` . ``EQ`` is the default condition and can be omitted. 
               
              * ``IN`` : When you specify ``IN`` , specify a list of the IDs for the namespaces that you want ``ListServices`` to return a list of services for. 
               
              * ``BETWEEN`` : Not applicable. 
               
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
                \'Services\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'InstanceCount\': 123
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Services** *(list) --* 
        
              An array that contains one ``ServiceSummary`` object for each service that matches the specified filter criteria.
        
              - *(dict) --* 
        
                A complex type that contains information about a specified service.
        
                - **Id** *(string) --* 
        
                  The ID that Route 53 assigned to the service when you created it.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that Route 53 assigns to the service when you create it.
        
                - **Name** *(string) --* 
        
                  The name of the service.
        
                - **Description** *(string) --* 
        
                  The description that you specify when you create the service.
        
                - **InstanceCount** *(integer) --* 
        
                  The number of instances that are currently associated with the service. Instances that were previously associated with the service but that have been deleted are not included in the count.
        
        """
        pass
