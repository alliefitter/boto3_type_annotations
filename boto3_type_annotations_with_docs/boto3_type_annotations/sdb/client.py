from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def batch_delete_attributes(self, DomainName: str, Items: List) -> NoReturn:
        """
        
        The following limitations are enforced for this operation: 
        
        * 1 MB request size
         
        * 25 item limit per BatchDeleteAttributes operation
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/BatchDeleteAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_delete_attributes(
              DomainName=\'string\',
              Items=[
                  {
                      \'Name\': \'string\',
                      \'Attributes\': [
                          {
                              \'Name\': \'string\',
                              \'AlternateNameEncoding\': \'string\',
                              \'Value\': \'string\',
                              \'AlternateValueEncoding\': \'string\'
                          },
                      ]
                  },
              ]
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** The name of the domain in which the attributes are being deleted.
        
        :type Items: list
        :param Items: **[REQUIRED]** A list of items on which to perform the operation.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
            - **Attributes** *(list) --* 
        
              - *(dict) --* 
        
                - **Name** *(string) --* **[REQUIRED]** The name of the attribute.
        
                - **AlternateNameEncoding** *(string) --* 
        
                - **Value** *(string) --* **[REQUIRED]** The value of the attribute.
        
                - **AlternateValueEncoding** *(string) --* 
        
        :returns: None
        """
        pass

    def batch_put_attributes(self, DomainName: str, Items: List) -> NoReturn:
        """
        
        The client may specify the item name with the ``Item.X.ItemName`` parameter. The client may specify new attributes using a combination of the ``Item.X.Attribute.Y.Name`` and ``Item.X.Attribute.Y.Value`` parameters. The client may specify the first attribute for the first item using the parameters ``Item.0.Attribute.0.Name`` and ``Item.0.Attribute.0.Value`` , and for the second attribute for the first item by the parameters ``Item.0.Attribute.1.Name`` and ``Item.0.Attribute.1.Value`` , and so on. 
        
        Attributes are uniquely identified within an item by their name/value combination. For example, a single item can have the attributes ``{ \"first_name\", \"first_value\" }`` and ``{ \"first_name\", \"second_value\" }`` . However, it cannot have two attribute instances where both the ``Item.X.Attribute.Y.Name`` and ``Item.X.Attribute.Y.Value`` are the same. 
        
        Optionally, the requester can supply the ``Replace`` parameter for each individual value. Setting this value to ``true`` will cause the new attribute values to replace the existing attribute values. For example, if an item ``I`` has the attributes ``{ \'a\', \'1\' }, { \'b\', \'2\'}`` and ``{ \'b\', \'3\' }`` and the requester does a BatchPutAttributes of ``{\'I\', \'b\', \'4\' }`` with the Replace parameter set to true, the final attributes of the item will be ``{ \'a\', \'1\' }`` and ``{ \'b\', \'4\' }`` , replacing the previous values of the \'b\' attribute with the new value. 
        
        .. warning::
        
          This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. This operation does not support conditions using ``Expected.X.Name`` , ``Expected.X.Value`` , or ``Expected.X.Exists`` . 
        
        You can execute multiple ``BatchPutAttributes`` operations and other operations in parallel. However, large numbers of concurrent ``BatchPutAttributes`` calls can result in Service Unavailable (503) responses. 
        
        The following limitations are enforced for this operation: 
        
        * 256 attribute name-value pairs per item
         
        * 1 MB request size
         
        * 1 billion attributes per domain
         
        * 10 GB of total user data storage per domain
         
        * 25 item limit per ``BatchPutAttributes`` operation
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/BatchPutAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_put_attributes(
              DomainName=\'string\',
              Items=[
                  {
                      \'Name\': \'string\',
                      \'Attributes\': [
                          {
                              \'Name\': \'string\',
                              \'Value\': \'string\',
                              \'Replace\': True|False
                          },
                      ]
                  },
              ]
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** The name of the domain in which the attributes are being stored.
        
        :type Items: list
        :param Items: **[REQUIRED]** A list of items on which to perform the operation.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** The name of the replaceable item.
        
            - **Attributes** *(list) --* **[REQUIRED]** The list of attributes for a replaceable item.
        
              - *(dict) --* 
        
                - **Name** *(string) --* **[REQUIRED]** The name of the replaceable attribute.
        
                - **Value** *(string) --* **[REQUIRED]** The value of the replaceable attribute.
        
                - **Replace** *(boolean) --* A flag specifying whether or not to replace the attribute/value pair or to add a new attribute/value pair. The default setting is ``false`` .
        
        :returns: None
        """
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
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

    def create_domain(self, DomainName: str) -> NoReturn:
        """
        
        The client can create up to 100 domains per account. 
        
        If the client requires additional domains, go to `http\://aws.amazon.com/contact-us/simpledb-limit-request/ <http://aws.amazon.com/contact-us/simpledb-limit-request/>`__ . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/CreateDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_domain(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** The name of the domain to create. The name can range between 3 and 255 characters and can contain the following characters: a-z, A-Z, 0-9, \'_\', \'-\', and \'.\'.
        
        :returns: None
        """
        pass

    def delete_attributes(self, DomainName: str, ItemName: str, Attributes: List = None, Expected: Dict = None) -> NoReturn:
        """
        
         ``DeleteAttributes`` is an idempotent operation; running it multiple times on the same item or attribute does not result in an error response. 
        
        Because Amazon SimpleDB makes multiple copies of item data and uses an eventual consistency update model, performing a  GetAttributes or  Select operation (read) immediately after a ``DeleteAttributes`` or  PutAttributes operation (write) might not return updated item data. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/DeleteAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_attributes(
              DomainName=\'string\',
              ItemName=\'string\',
              Attributes=[
                  {
                      \'Name\': \'string\',
                      \'AlternateNameEncoding\': \'string\',
                      \'Value\': \'string\',
                      \'AlternateValueEncoding\': \'string\'
                  },
              ],
              Expected={
                  \'Name\': \'string\',
                  \'Value\': \'string\',
                  \'Exists\': True|False
              }
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** The name of the domain in which to perform the operation.
        
        :type ItemName: string
        :param ItemName: **[REQUIRED]** The name of the item. Similar to rows on a spreadsheet, items represent individual objects that contain one or more value-attribute pairs.
        
        :type Attributes: list
        :param Attributes: A list of Attributes. Similar to columns on a spreadsheet, attributes represent categories of data that can be assigned to items.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** The name of the attribute.
        
            - **AlternateNameEncoding** *(string) --* 
        
            - **Value** *(string) --* **[REQUIRED]** The value of the attribute.
        
            - **AlternateValueEncoding** *(string) --* 
        
        :type Expected: dict
        :param Expected: The update condition which, if specified, determines whether the specified attributes will be deleted or not. The update condition must be satisfied in order for this request to be processed and the attributes to be deleted.
        
          - **Name** *(string) --* 
        
            The name of the attribute involved in the condition.
        
          - **Value** *(string) --* 
        
            The value of an attribute. This value can only be specified when the ``Exists`` parameter is equal to ``true`` .
        
          - **Exists** *(boolean) --* 
        
            A value specifying whether or not the specified attribute must exist with the specified value in order for the update condition to be satisfied. Specify ``true`` if the attribute must exist for the update condition to be satisfied. Specify ``false`` if the attribute should not exist in order for the update condition to be satisfied.
        
        :returns: None
        """
        pass

    def delete_domain(self, DomainName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/DeleteDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_domain(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** The name of the domain to delete.
        
        :returns: None
        """
        pass

    def domain_metadata(self, DomainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/DomainMetadata>`_
        
        **Request Syntax** 
        ::
        
          response = client.domain_metadata(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** The name of the domain for which to display the metadata of.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ItemCount\': 123,
                \'ItemNamesSizeBytes\': 123,
                \'AttributeNameCount\': 123,
                \'AttributeNamesSizeBytes\': 123,
                \'AttributeValueCount\': 123,
                \'AttributeValuesSizeBytes\': 123,
                \'Timestamp\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ItemCount** *(integer) --* The number of all items in the domain.
            
            - **ItemNamesSizeBytes** *(integer) --* The total size of all item names in the domain, in bytes.
            
            - **AttributeNameCount** *(integer) --* The number of unique attribute names in the domain.
            
            - **AttributeNamesSizeBytes** *(integer) --* The total size of all unique attribute names in the domain, in bytes.
            
            - **AttributeValueCount** *(integer) --* The number of all attribute name/value pairs in the domain.
            
            - **AttributeValuesSizeBytes** *(integer) --* The total size of all attribute values in the domain, in bytes.
            
            - **Timestamp** *(integer) --* The data and time when metadata was calculated, in Epoch (UNIX) seconds.
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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

    def get_attributes(self, DomainName: str, ItemName: str, AttributeNames: List = None, ConsistentRead: bool = None) -> Dict:
        """
        
        If the item does not exist on the replica that was accessed for this operation, an empty set is returned. The system does not return an error as it cannot guarantee the item does not exist on other replicas. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/GetAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_attributes(
              DomainName=\'string\',
              ItemName=\'string\',
              AttributeNames=[
                  \'string\',
              ],
              ConsistentRead=True|False
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** The name of the domain in which to perform the operation.
        
        :type ItemName: string
        :param ItemName: **[REQUIRED]** The name of the item.
        
        :type AttributeNames: list
        :param AttributeNames: The names of the attributes.
        
          - *(string) --* 
        
        :type ConsistentRead: boolean
        :param ConsistentRead: Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If ``true`` , any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Name\': \'string\',
                        \'AlternateNameEncoding\': \'string\',
                        \'Value\': \'string\',
                        \'AlternateValueEncoding\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* The list of attributes returned by the operation.
              
              - *(dict) --* 
        
                - **Name** *(string) --* The name of the attribute.
                
                - **AlternateNameEncoding** *(string) --* 
        
                - **Value** *(string) --* The value of the attribute.
                
                - **AlternateValueEncoding** *(string) --* 
        
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_domains(self, MaxNumberOfDomains: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/ListDomains>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_domains(
              MaxNumberOfDomains=123,
              NextToken=\'string\'
          )
        :type MaxNumberOfDomains: integer
        :param MaxNumberOfDomains: The maximum number of domain names you want returned. The range is 1 to 100. The default setting is 100.
        
        :type NextToken: string
        :param NextToken: A string informing Amazon SimpleDB where to start the next list of domain names.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DomainNames\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DomainNames** *(list) --* A list of domain names that match the expression.
              
              - *(string) --* 
          
            - **NextToken** *(string) --* An opaque token indicating that there are more domains than the specified ``MaxNumberOfDomains`` still available.
        """
        pass

    def put_attributes(self, DomainName: str, ItemName: str, Attributes: List, Expected: Dict = None) -> NoReturn:
        """
        
        Attributes are uniquely identified in an item by their name/value combination. For example, a single item can have the attributes ``{ \"first_name\", \"first_value\" }`` and ``{ \"first_name\", second_value\" }`` . However, it cannot have two attribute instances where both the ``Attribute.X.Name`` and ``Attribute.X.Value`` are the same. 
        
        Optionally, the requestor can supply the ``Replace`` parameter for each individual attribute. Setting this value to ``true`` causes the new attribute value to replace the existing attribute value(s). For example, if an item has the attributes ``{ \'a\', \'1\' }`` , ``{ \'b\', \'2\'}`` and ``{ \'b\', \'3\' }`` and the requestor calls ``PutAttributes`` using the attributes ``{ \'b\', \'4\' }`` with the ``Replace`` parameter set to true, the final attributes of the item are changed to ``{ \'a\', \'1\' }`` and ``{ \'b\', \'4\' }`` , which replaces the previous values of the \'b\' attribute with the new value. 
        
        You cannot specify an empty string as an attribute name. 
        
        Because Amazon SimpleDB makes multiple copies of client data and uses an eventual consistency update model, an immediate  GetAttributes or  Select operation (read) immediately after a  PutAttributes or  DeleteAttributes operation (write) might not return the updated data. 
        
        The following limitations are enforced for this operation: 
        
        * 256 total attribute name-value pairs per item
         
        * One billion attributes per domain
         
        * 10 GB of total user data storage per domain
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/PutAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_attributes(
              DomainName=\'string\',
              ItemName=\'string\',
              Attributes=[
                  {
                      \'Name\': \'string\',
                      \'Value\': \'string\',
                      \'Replace\': True|False
                  },
              ],
              Expected={
                  \'Name\': \'string\',
                  \'Value\': \'string\',
                  \'Exists\': True|False
              }
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** The name of the domain in which to perform the operation.
        
        :type ItemName: string
        :param ItemName: **[REQUIRED]** The name of the item.
        
        :type Attributes: list
        :param Attributes: **[REQUIRED]** The list of attributes.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** The name of the replaceable attribute.
        
            - **Value** *(string) --* **[REQUIRED]** The value of the replaceable attribute.
        
            - **Replace** *(boolean) --* A flag specifying whether or not to replace the attribute/value pair or to add a new attribute/value pair. The default setting is ``false`` .
        
        :type Expected: dict
        :param Expected: The update condition which, if specified, determines whether the specified attributes will be updated or not. The update condition must be satisfied in order for this request to be processed and the attributes to be updated.
        
          - **Name** *(string) --* 
        
            The name of the attribute involved in the condition.
        
          - **Value** *(string) --* 
        
            The value of an attribute. This value can only be specified when the ``Exists`` parameter is equal to ``true`` .
        
          - **Exists** *(boolean) --* 
        
            A value specifying whether or not the specified attribute must exist with the specified value in order for the update condition to be satisfied. Specify ``true`` if the attribute must exist for the update condition to be satisfied. Specify ``false`` if the attribute should not exist in order for the update condition to be satisfied.
        
        :returns: None
        """
        pass

    def select(self, SelectExpression: str, NextToken: str = None, ConsistentRead: bool = None) -> Dict:
        """
        
        The total size of the response cannot exceed 1 MB in total size. Amazon SimpleDB automatically adjusts the number of items returned per page to enforce this limit. For example, if the client asks to retrieve 2500 items, but each individual item is 10 kB in size, the system returns 100 items and an appropriate ``NextToken`` so the client can access the next page of results. 
        
        For information on how to construct select expressions, see Using Select to Create Amazon SimpleDB Queries in the Developer Guide. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/Select>`_
        
        **Request Syntax** 
        ::
        
          response = client.select(
              SelectExpression=\'string\',
              NextToken=\'string\',
              ConsistentRead=True|False
          )
        :type SelectExpression: string
        :param SelectExpression: **[REQUIRED]** The expression used to query the domain.
        
        :type NextToken: string
        :param NextToken: A string informing Amazon SimpleDB where to start the next list of ``ItemNames`` .
        
        :type ConsistentRead: boolean
        :param ConsistentRead: Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If ``true`` , any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Items\': [
                    {
                        \'Name\': \'string\',
                        \'AlternateNameEncoding\': \'string\',
                        \'Attributes\': [
                            {
                                \'Name\': \'string\',
                                \'AlternateNameEncoding\': \'string\',
                                \'Value\': \'string\',
                                \'AlternateValueEncoding\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Items** *(list) --* A list of items that match the select expression.
              
              - *(dict) --* 
        
                - **Name** *(string) --* The name of the item.
                
                - **AlternateNameEncoding** *(string) --* 
        
                - **Attributes** *(list) --* A list of attributes.
                  
                  - *(dict) --* 
        
                    - **Name** *(string) --* The name of the attribute.
                    
                    - **AlternateNameEncoding** *(string) --* 
        
                    - **Value** *(string) --* The value of the attribute.
                    
                    - **AlternateValueEncoding** *(string) --* 
        
            - **NextToken** *(string) --* An opaque token indicating that more items than ``MaxNumberOfItems`` were matched, the response size exceeded 1 megabyte, or the execution time exceeded 5 seconds.
        """
        pass
