from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_facet_to_object(self, DirectoryArn: str, SchemaFacet: Dict, ObjectReference: Dict, ObjectAttributeList: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/AddFacetToObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_facet_to_object(
              DirectoryArn=\'string\',
              SchemaFacet={
                  \'SchemaArn\': \'string\',
                  \'FacetName\': \'string\'
              },
              ObjectAttributeList=[
                  {
                      \'Key\': {
                          \'SchemaArn\': \'string\',
                          \'FacetName\': \'string\',
                          \'Name\': \'string\'
                      },
                      \'Value\': {
                          \'StringValue\': \'string\',
                          \'BinaryValue\': b\'bytes\',
                          \'BooleanValue\': True|False,
                          \'NumberValue\': \'string\',
                          \'DatetimeValue\': datetime(2015, 1, 1)
                      }
                  },
              ],
              ObjectReference={
                  \'Selector\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides. For more information, see  arns .
        
        :type SchemaFacet: dict
        :param SchemaFacet: **[REQUIRED]** 
        
          Identifiers for the facet that you are adding to the object. See  SchemaFacet for details.
        
          - **SchemaArn** *(string) --* 
        
            The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
          - **FacetName** *(string) --* 
        
            The name of the facet.
        
        :type ObjectAttributeList: list
        :param ObjectAttributeList: 
        
          Attributes on the facet that you are adding to the object.
        
          - *(dict) --* 
        
            The combination of an attribute key and an attribute value.
        
            - **Key** *(dict) --* **[REQUIRED]** 
        
              The key of the attribute.
        
              - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
              - **FacetName** *(string) --* **[REQUIRED]** 
        
                The name of the facet that the attribute exists within.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                The name of the attribute.
        
            - **Value** *(dict) --* **[REQUIRED]** 
        
              The value of the attribute.
        
              - **StringValue** *(string) --* 
        
                A string data value.
        
              - **BinaryValue** *(bytes) --* 
        
                A binary data value.
        
              - **BooleanValue** *(boolean) --* 
        
                A Boolean data value.
        
              - **NumberValue** *(string) --* 
        
                A number data value.
        
              - **DatetimeValue** *(datetime) --* 
        
                A date and time value.
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          A reference to the object you are adding the specified facet to.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def apply_schema(self, PublishedSchemaArn: str, DirectoryArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ApplySchema>`_
        
        **Request Syntax** 
        ::
        
          response = client.apply_schema(
              PublishedSchemaArn=\'string\',
              DirectoryArn=\'string\'
          )
        :type PublishedSchemaArn: string
        :param PublishedSchemaArn: **[REQUIRED]** 
        
          Published schema Amazon Resource Name (ARN) that needs to be copied. For more information, see  arns .
        
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory into which the schema is copied. For more information, see  arns .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AppliedSchemaArn\': \'string\',
                \'DirectoryArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AppliedSchemaArn** *(string) --* 
        
              The applied schema ARN that is associated with the copied schema in the  Directory . You can use this ARN to describe the schema information applied on this directory. For more information, see  arns .
        
            - **DirectoryArn** *(string) --* 
        
              The ARN that is associated with the  Directory . For more information, see  arns .
        
        """
        pass

    def attach_object(self, DirectoryArn: str, ParentReference: Dict, ChildReference: Dict, LinkName: str) -> Dict:
        """
        Attaches an existing object to another object. An object can be accessed in two ways:
        
        * Using the path 
         
        * Using ``ObjectIdentifier``   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/AttachObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_object(
              DirectoryArn=\'string\',
              ParentReference={
                  \'Selector\': \'string\'
              },
              ChildReference={
                  \'Selector\': \'string\'
              },
              LinkName=\'string\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          Amazon Resource Name (ARN) that is associated with the  Directory where both objects reside. For more information, see  arns .
        
        :type ParentReference: dict
        :param ParentReference: **[REQUIRED]** 
        
          The parent object reference.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type ChildReference: dict
        :param ChildReference: **[REQUIRED]** 
        
          The child object reference to be attached to the object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type LinkName: string
        :param LinkName: **[REQUIRED]** 
        
          The link name with which the child object is attached to the parent.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttachedObjectIdentifier\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AttachedObjectIdentifier** *(string) --* 
        
              The attached ``ObjectIdentifier`` , which is the child ``ObjectIdentifier`` .
        
        """
        pass

    def attach_policy(self, DirectoryArn: str, PolicyReference: Dict, ObjectReference: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/AttachPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_policy(
              DirectoryArn=\'string\',
              PolicyReference={
                  \'Selector\': \'string\'
              },
              ObjectReference={
                  \'Selector\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where both objects reside. For more information, see  arns .
        
        :type PolicyReference: dict
        :param PolicyReference: **[REQUIRED]** 
        
          The reference that is associated with the policy object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          The reference that identifies the object to which the policy will be attached.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def attach_to_index(self, DirectoryArn: str, IndexReference: Dict, TargetReference: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/AttachToIndex>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_to_index(
              DirectoryArn=\'string\',
              IndexReference={
                  \'Selector\': \'string\'
              },
              TargetReference={
                  \'Selector\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the directory where the object and index exist.
        
        :type IndexReference: dict
        :param IndexReference: **[REQUIRED]** 
        
          A reference to the index that you are attaching the object to.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type TargetReference: dict
        :param TargetReference: **[REQUIRED]** 
        
          A reference to the object that you are attaching to the index.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttachedObjectIdentifier\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AttachedObjectIdentifier** *(string) --* 
        
              The ``ObjectIdentifier`` of the object that was attached to the index.
        
        """
        pass

    def attach_typed_link(self, DirectoryArn: str, SourceObjectReference: Dict, TargetObjectReference: Dict, TypedLinkFacet: Dict, Attributes: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/AttachTypedLink>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_typed_link(
              DirectoryArn=\'string\',
              SourceObjectReference={
                  \'Selector\': \'string\'
              },
              TargetObjectReference={
                  \'Selector\': \'string\'
              },
              TypedLinkFacet={
                  \'SchemaArn\': \'string\',
                  \'TypedLinkName\': \'string\'
              },
              Attributes=[
                  {
                      \'AttributeName\': \'string\',
                      \'Value\': {
                          \'StringValue\': \'string\',
                          \'BinaryValue\': b\'bytes\',
                          \'BooleanValue\': True|False,
                          \'NumberValue\': \'string\',
                          \'DatetimeValue\': datetime(2015, 1, 1)
                      }
                  },
              ]
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the directory where you want to attach the typed link.
        
        :type SourceObjectReference: dict
        :param SourceObjectReference: **[REQUIRED]** 
        
          Identifies the source object that the typed link will attach to.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type TargetObjectReference: dict
        :param TargetObjectReference: **[REQUIRED]** 
        
          Identifies the target object that the typed link will attach to.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type TypedLinkFacet: dict
        :param TypedLinkFacet: **[REQUIRED]** 
        
          Identifies the typed link facet that is associated with the typed link.
        
          - **SchemaArn** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
          - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
            The unique name of the typed link facet.
        
        :type Attributes: list
        :param Attributes: **[REQUIRED]** 
        
          A set of attributes that are associated with the typed link.
        
          - *(dict) --* 
        
            Identifies the attribute name and value for a typed link.
        
            - **AttributeName** *(string) --* **[REQUIRED]** 
        
              The attribute name of the typed link.
        
            - **Value** *(dict) --* **[REQUIRED]** 
        
              The value for the typed link.
        
              - **StringValue** *(string) --* 
        
                A string data value.
        
              - **BinaryValue** *(bytes) --* 
        
                A binary data value.
        
              - **BooleanValue** *(boolean) --* 
        
                A Boolean data value.
        
              - **NumberValue** *(string) --* 
        
                A number data value.
        
              - **DatetimeValue** *(datetime) --* 
        
                A date and time value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TypedLinkSpecifier\': {
                    \'TypedLinkFacet\': {
                        \'SchemaArn\': \'string\',
                        \'TypedLinkName\': \'string\'
                    },
                    \'SourceObjectReference\': {
                        \'Selector\': \'string\'
                    },
                    \'TargetObjectReference\': {
                        \'Selector\': \'string\'
                    },
                    \'IdentityAttributeValues\': [
                        {
                            \'AttributeName\': \'string\',
                            \'Value\': {
                                \'StringValue\': \'string\',
                                \'BinaryValue\': b\'bytes\',
                                \'BooleanValue\': True|False,
                                \'NumberValue\': \'string\',
                                \'DatetimeValue\': datetime(2015, 1, 1)
                            }
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TypedLinkSpecifier** *(dict) --* 
        
              Returns a typed link specifier as output.
        
              - **TypedLinkFacet** *(dict) --* 
        
                Identifies the typed link facet that is associated with the typed link.
        
                - **SchemaArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                - **TypedLinkName** *(string) --* 
        
                  The unique name of the typed link facet.
        
              - **SourceObjectReference** *(dict) --* 
        
                Identifies the source object that the typed link will attach to.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **TargetObjectReference** *(dict) --* 
        
                Identifies the target object that the typed link will attach to.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **IdentityAttributeValues** *(list) --* 
        
                Identifies the attribute value to update.
        
                - *(dict) --* 
        
                  Identifies the attribute name and value for a typed link.
        
                  - **AttributeName** *(string) --* 
        
                    The attribute name of the typed link.
        
                  - **Value** *(dict) --* 
        
                    The value for the typed link.
        
                    - **StringValue** *(string) --* 
        
                      A string data value.
        
                    - **BinaryValue** *(bytes) --* 
        
                      A binary data value.
        
                    - **BooleanValue** *(boolean) --* 
        
                      A Boolean data value.
        
                    - **NumberValue** *(string) --* 
        
                      A number data value.
        
                    - **DatetimeValue** *(datetime) --* 
        
                      A date and time value.
        
        """
        pass

    def batch_read(self, DirectoryArn: str, Operations: List, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/BatchRead>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_read(
              DirectoryArn=\'string\',
              Operations=[
                  {
                      \'ListObjectAttributes\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123,
                          \'FacetFilter\': {
                              \'SchemaArn\': \'string\',
                              \'FacetName\': \'string\'
                          }
                      },
                      \'ListObjectChildren\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'ListAttachedIndices\': {
                          \'TargetReference\': {
                              \'Selector\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'ListObjectParentPaths\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'GetObjectInformation\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          }
                      },
                      \'GetObjectAttributes\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'SchemaFacet\': {
                              \'SchemaArn\': \'string\',
                              \'FacetName\': \'string\'
                          },
                          \'AttributeNames\': [
                              \'string\',
                          ]
                      },
                      \'ListObjectParents\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'ListObjectPolicies\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'ListPolicyAttachments\': {
                          \'PolicyReference\': {
                              \'Selector\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'LookupPolicy\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'ListIndex\': {
                          \'RangesOnIndexedValues\': [
                              {
                                  \'AttributeKey\': {
                                      \'SchemaArn\': \'string\',
                                      \'FacetName\': \'string\',
                                      \'Name\': \'string\'
                                  },
                                  \'Range\': {
                                      \'StartMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                                      \'StartValue\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      },
                                      \'EndMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                                      \'EndValue\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      }
                                  }
                              },
                          ],
                          \'IndexReference\': {
                              \'Selector\': \'string\'
                          },
                          \'MaxResults\': 123,
                          \'NextToken\': \'string\'
                      },
                      \'ListOutgoingTypedLinks\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'FilterAttributeRanges\': [
                              {
                                  \'AttributeName\': \'string\',
                                  \'Range\': {
                                      \'StartMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                                      \'StartValue\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      },
                                      \'EndMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                                      \'EndValue\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      }
                                  }
                              },
                          ],
                          \'FilterTypedLink\': {
                              \'SchemaArn\': \'string\',
                              \'TypedLinkName\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'ListIncomingTypedLinks\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'FilterAttributeRanges\': [
                              {
                                  \'AttributeName\': \'string\',
                                  \'Range\': {
                                      \'StartMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                                      \'StartValue\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      },
                                      \'EndMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                                      \'EndValue\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      }
                                  }
                              },
                          ],
                          \'FilterTypedLink\': {
                              \'SchemaArn\': \'string\',
                              \'TypedLinkName\': \'string\'
                          },
                          \'NextToken\': \'string\',
                          \'MaxResults\': 123
                      },
                      \'GetLinkAttributes\': {
                          \'TypedLinkSpecifier\': {
                              \'TypedLinkFacet\': {
                                  \'SchemaArn\': \'string\',
                                  \'TypedLinkName\': \'string\'
                              },
                              \'SourceObjectReference\': {
                                  \'Selector\': \'string\'
                              },
                              \'TargetObjectReference\': {
                                  \'Selector\': \'string\'
                              },
                              \'IdentityAttributeValues\': [
                                  {
                                      \'AttributeName\': \'string\',
                                      \'Value\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      }
                                  },
                              ]
                          },
                          \'AttributeNames\': [
                              \'string\',
                          ]
                      }
                  },
              ],
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory . For more information, see  arns .
        
        :type Operations: list
        :param Operations: **[REQUIRED]** 
        
          A list of operations that are part of the batch.
        
          - *(dict) --* 
        
            Represents the output of a ``BatchRead`` operation.
        
            - **ListObjectAttributes** *(dict) --* 
        
              Lists all attributes that are associated with an object.
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                Reference of the object whose attributes need to be listed.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                The maximum number of items to be retrieved in a single call. This is an approximate number.
        
              - **FacetFilter** *(dict) --* 
        
                Used to filter the list of object attributes that are associated with a certain facet.
        
                - **SchemaArn** *(string) --* 
        
                  The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
                - **FacetName** *(string) --* 
        
                  The name of the facet.
        
            - **ListObjectChildren** *(dict) --* 
        
              Returns a paginated list of child objects that are associated with a given object.
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                Reference of the object for which child objects are being listed.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                Maximum number of items to be retrieved in a single call. This is an approximate number.
        
            - **ListAttachedIndices** *(dict) --* 
        
              Lists indices attached to an object.
        
              - **TargetReference** *(dict) --* **[REQUIRED]** 
        
                A reference to the object that has indices attached.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                The maximum number of results to retrieve.
        
            - **ListObjectParentPaths** *(dict) --* 
        
              Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see `Directory Structure <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html>`__ .
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                The reference that identifies the object whose attributes will be listed.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                The maximum number of results to retrieve.
        
            - **GetObjectInformation** *(dict) --* 
        
              Retrieves metadata about an object.
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                A reference to the object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
            - **GetObjectAttributes** *(dict) --* 
        
              Retrieves attributes within a facet that are associated with an object.
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                Reference that identifies the object whose attributes will be retrieved.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **SchemaFacet** *(dict) --* **[REQUIRED]** 
        
                Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.
        
                - **SchemaArn** *(string) --* 
        
                  The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
                - **FacetName** *(string) --* 
        
                  The name of the facet.
        
              - **AttributeNames** *(list) --* **[REQUIRED]** 
        
                List of attribute names whose values will be retrieved.
        
                - *(string) --* 
        
            - **ListObjectParents** *(dict) --* 
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                The reference that identifies an object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **NextToken** *(string) --* 
        
              - **MaxResults** *(integer) --* 
        
            - **ListObjectPolicies** *(dict) --* 
        
              Returns policies attached to an object in pagination fashion.
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                The reference that identifies the object whose attributes will be listed.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                The maximum number of results to retrieve.
        
            - **ListPolicyAttachments** *(dict) --* 
        
              Returns all of the ``ObjectIdentifiers`` to which a given policy is attached.
        
              - **PolicyReference** *(dict) --* **[REQUIRED]** 
        
                The reference that identifies the policy object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                The maximum number of results to retrieve.
        
            - **LookupPolicy** *(dict) --* 
        
              Lists all policies from the root of the  Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don\'t have the policies attached, it returns the ``ObjectIdentifier`` for such objects. If policies are present, it returns ``ObjectIdentifier`` , ``policyId`` , and ``policyType`` . Paths that don\'t lead to the root from the target object are ignored. For more information, see `Policies <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__ .
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                Reference that identifies the object whose policies will be looked up.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                The maximum number of results to retrieve.
        
            - **ListIndex** *(dict) --* 
        
              Lists objects attached to the specified index.
        
              - **RangesOnIndexedValues** *(list) --* 
        
                Specifies the ranges of indexed values that you want to query.
        
                - *(dict) --* 
        
                  A range of attributes.
        
                  - **AttributeKey** *(dict) --* 
        
                    The key of the attribute that the attribute range covers.
        
                    - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                    - **FacetName** *(string) --* **[REQUIRED]** 
        
                      The name of the facet that the attribute exists within.
        
                    - **Name** *(string) --* **[REQUIRED]** 
        
                      The name of the attribute.
        
                  - **Range** *(dict) --* 
        
                    The range of attribute values being selected.
        
                    - **StartMode** *(string) --* **[REQUIRED]** 
        
                      The inclusive or exclusive range start.
        
                    - **StartValue** *(dict) --* 
        
                      The value to start the range at.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
                    - **EndMode** *(string) --* **[REQUIRED]** 
        
                      The inclusive or exclusive range end.
        
                    - **EndValue** *(dict) --* 
        
                      The attribute value to terminate the range at.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
              - **IndexReference** *(dict) --* **[REQUIRED]** 
        
                The reference to the index to list.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **MaxResults** *(integer) --* 
        
                The maximum number of results to retrieve.
        
              - **NextToken** *(string) --* 
        
                The pagination token.
        
            - **ListOutgoingTypedLinks** *(dict) --* 
        
              Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                The reference that identifies the object whose attributes will be listed.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **FilterAttributeRanges** *(list) --* 
        
                Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
        
                - *(dict) --* 
        
                  Identifies the range of attributes that are used by a specified filter.
        
                  - **AttributeName** *(string) --* 
        
                    The unique name of the typed link attribute.
        
                  - **Range** *(dict) --* **[REQUIRED]** 
        
                    The range of attribute values that are being selected.
        
                    - **StartMode** *(string) --* **[REQUIRED]** 
        
                      The inclusive or exclusive range start.
        
                    - **StartValue** *(dict) --* 
        
                      The value to start the range at.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
                    - **EndMode** *(string) --* **[REQUIRED]** 
        
                      The inclusive or exclusive range end.
        
                    - **EndValue** *(dict) --* 
        
                      The attribute value to terminate the range at.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
              - **FilterTypedLink** *(dict) --* 
        
                Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.
        
                - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
                  The unique name of the typed link facet.
        
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                The maximum number of results to retrieve.
        
            - **ListIncomingTypedLinks** *(dict) --* 
        
              Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                The reference that identifies the object whose attributes will be listed.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **FilterAttributeRanges** *(list) --* 
        
                Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
        
                - *(dict) --* 
        
                  Identifies the range of attributes that are used by a specified filter.
        
                  - **AttributeName** *(string) --* 
        
                    The unique name of the typed link attribute.
        
                  - **Range** *(dict) --* **[REQUIRED]** 
        
                    The range of attribute values that are being selected.
        
                    - **StartMode** *(string) --* **[REQUIRED]** 
        
                      The inclusive or exclusive range start.
        
                    - **StartValue** *(dict) --* 
        
                      The value to start the range at.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
                    - **EndMode** *(string) --* **[REQUIRED]** 
        
                      The inclusive or exclusive range end.
        
                    - **EndValue** *(dict) --* 
        
                      The attribute value to terminate the range at.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
              - **FilterTypedLink** *(dict) --* 
        
                Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.
        
                - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
                  The unique name of the typed link facet.
        
              - **NextToken** *(string) --* 
        
                The pagination token.
        
              - **MaxResults** *(integer) --* 
        
                The maximum number of results to retrieve.
        
            - **GetLinkAttributes** *(dict) --* 
        
              Retrieves attributes that are associated with a typed link.
        
              - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]** 
        
                Allows a typed link specifier to be accepted as input.
        
                - **TypedLinkFacet** *(dict) --* **[REQUIRED]** 
        
                  Identifies the typed link facet that is associated with the typed link.
        
                  - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                    The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                  - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
                    The unique name of the typed link facet.
        
                - **SourceObjectReference** *(dict) --* **[REQUIRED]** 
        
                  Identifies the source object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **TargetObjectReference** *(dict) --* **[REQUIRED]** 
        
                  Identifies the target object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **IdentityAttributeValues** *(list) --* **[REQUIRED]** 
        
                  Identifies the attribute value to update.
        
                  - *(dict) --* 
        
                    Identifies the attribute name and value for a typed link.
        
                    - **AttributeName** *(string) --* **[REQUIRED]** 
        
                      The attribute name of the typed link.
        
                    - **Value** *(dict) --* **[REQUIRED]** 
        
                      The value for the typed link.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
              - **AttributeNames** *(list) --* **[REQUIRED]** 
        
                A list of attribute names whose values will be retrieved.
        
                - *(string) --* 
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Responses\': [
                    {
                        \'SuccessfulResponse\': {
                            \'ListObjectAttributes\': {
                                \'Attributes\': [
                                    {
                                        \'Key\': {
                                            \'SchemaArn\': \'string\',
                                            \'FacetName\': \'string\',
                                            \'Name\': \'string\'
                                        },
                                        \'Value\': {
                                            \'StringValue\': \'string\',
                                            \'BinaryValue\': b\'bytes\',
                                            \'BooleanValue\': True|False,
                                            \'NumberValue\': \'string\',
                                            \'DatetimeValue\': datetime(2015, 1, 1)
                                        }
                                    },
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'ListObjectChildren\': {
                                \'Children\': {
                                    \'string\': \'string\'
                                },
                                \'NextToken\': \'string\'
                            },
                            \'GetObjectInformation\': {
                                \'SchemaFacets\': [
                                    {
                                        \'SchemaArn\': \'string\',
                                        \'FacetName\': \'string\'
                                    },
                                ],
                                \'ObjectIdentifier\': \'string\'
                            },
                            \'GetObjectAttributes\': {
                                \'Attributes\': [
                                    {
                                        \'Key\': {
                                            \'SchemaArn\': \'string\',
                                            \'FacetName\': \'string\',
                                            \'Name\': \'string\'
                                        },
                                        \'Value\': {
                                            \'StringValue\': \'string\',
                                            \'BinaryValue\': b\'bytes\',
                                            \'BooleanValue\': True|False,
                                            \'NumberValue\': \'string\',
                                            \'DatetimeValue\': datetime(2015, 1, 1)
                                        }
                                    },
                                ]
                            },
                            \'ListAttachedIndices\': {
                                \'IndexAttachments\': [
                                    {
                                        \'IndexedAttributes\': [
                                            {
                                                \'Key\': {
                                                    \'SchemaArn\': \'string\',
                                                    \'FacetName\': \'string\',
                                                    \'Name\': \'string\'
                                                },
                                                \'Value\': {
                                                    \'StringValue\': \'string\',
                                                    \'BinaryValue\': b\'bytes\',
                                                    \'BooleanValue\': True|False,
                                                    \'NumberValue\': \'string\',
                                                    \'DatetimeValue\': datetime(2015, 1, 1)
                                                }
                                            },
                                        ],
                                        \'ObjectIdentifier\': \'string\'
                                    },
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'ListObjectParentPaths\': {
                                \'PathToObjectIdentifiersList\': [
                                    {
                                        \'Path\': \'string\',
                                        \'ObjectIdentifiers\': [
                                            \'string\',
                                        ]
                                    },
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'ListObjectPolicies\': {
                                \'AttachedPolicyIds\': [
                                    \'string\',
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'ListPolicyAttachments\': {
                                \'ObjectIdentifiers\': [
                                    \'string\',
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'LookupPolicy\': {
                                \'PolicyToPathList\': [
                                    {
                                        \'Path\': \'string\',
                                        \'Policies\': [
                                            {
                                                \'PolicyId\': \'string\',
                                                \'ObjectIdentifier\': \'string\',
                                                \'PolicyType\': \'string\'
                                            },
                                        ]
                                    },
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'ListIndex\': {
                                \'IndexAttachments\': [
                                    {
                                        \'IndexedAttributes\': [
                                            {
                                                \'Key\': {
                                                    \'SchemaArn\': \'string\',
                                                    \'FacetName\': \'string\',
                                                    \'Name\': \'string\'
                                                },
                                                \'Value\': {
                                                    \'StringValue\': \'string\',
                                                    \'BinaryValue\': b\'bytes\',
                                                    \'BooleanValue\': True|False,
                                                    \'NumberValue\': \'string\',
                                                    \'DatetimeValue\': datetime(2015, 1, 1)
                                                }
                                            },
                                        ],
                                        \'ObjectIdentifier\': \'string\'
                                    },
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'ListOutgoingTypedLinks\': {
                                \'TypedLinkSpecifiers\': [
                                    {
                                        \'TypedLinkFacet\': {
                                            \'SchemaArn\': \'string\',
                                            \'TypedLinkName\': \'string\'
                                        },
                                        \'SourceObjectReference\': {
                                            \'Selector\': \'string\'
                                        },
                                        \'TargetObjectReference\': {
                                            \'Selector\': \'string\'
                                        },
                                        \'IdentityAttributeValues\': [
                                            {
                                                \'AttributeName\': \'string\',
                                                \'Value\': {
                                                    \'StringValue\': \'string\',
                                                    \'BinaryValue\': b\'bytes\',
                                                    \'BooleanValue\': True|False,
                                                    \'NumberValue\': \'string\',
                                                    \'DatetimeValue\': datetime(2015, 1, 1)
                                                }
                                            },
                                        ]
                                    },
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'ListIncomingTypedLinks\': {
                                \'LinkSpecifiers\': [
                                    {
                                        \'TypedLinkFacet\': {
                                            \'SchemaArn\': \'string\',
                                            \'TypedLinkName\': \'string\'
                                        },
                                        \'SourceObjectReference\': {
                                            \'Selector\': \'string\'
                                        },
                                        \'TargetObjectReference\': {
                                            \'Selector\': \'string\'
                                        },
                                        \'IdentityAttributeValues\': [
                                            {
                                                \'AttributeName\': \'string\',
                                                \'Value\': {
                                                    \'StringValue\': \'string\',
                                                    \'BinaryValue\': b\'bytes\',
                                                    \'BooleanValue\': True|False,
                                                    \'NumberValue\': \'string\',
                                                    \'DatetimeValue\': datetime(2015, 1, 1)
                                                }
                                            },
                                        ]
                                    },
                                ],
                                \'NextToken\': \'string\'
                            },
                            \'GetLinkAttributes\': {
                                \'Attributes\': [
                                    {
                                        \'Key\': {
                                            \'SchemaArn\': \'string\',
                                            \'FacetName\': \'string\',
                                            \'Name\': \'string\'
                                        },
                                        \'Value\': {
                                            \'StringValue\': \'string\',
                                            \'BinaryValue\': b\'bytes\',
                                            \'BooleanValue\': True|False,
                                            \'NumberValue\': \'string\',
                                            \'DatetimeValue\': datetime(2015, 1, 1)
                                        }
                                    },
                                ]
                            },
                            \'ListObjectParents\': {
                                \'ParentLinks\': [
                                    {
                                        \'ObjectIdentifier\': \'string\',
                                        \'LinkName\': \'string\'
                                    },
                                ],
                                \'NextToken\': \'string\'
                            }
                        },
                        \'ExceptionResponse\': {
                            \'Type\': \'ValidationException\'|\'InvalidArnException\'|\'ResourceNotFoundException\'|\'InvalidNextTokenException\'|\'AccessDeniedException\'|\'NotNodeException\'|\'FacetValidationException\'|\'CannotListParentOfRootException\'|\'NotIndexException\'|\'NotPolicyException\'|\'DirectoryNotEnabledException\'|\'LimitExceededException\'|\'InternalServiceException\',
                            \'Message\': \'string\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Responses** *(list) --* 
        
              A list of all the responses for each batch read.
        
              - *(dict) --* 
        
                Represents the output of a ``BatchRead`` response operation.
        
                - **SuccessfulResponse** *(dict) --* 
        
                  Identifies which operation in a batch has succeeded.
        
                  - **ListObjectAttributes** *(dict) --* 
        
                    Lists all attributes that are associated with an object.
        
                    - **Attributes** *(list) --* 
        
                      The attributes map that is associated with the object. ``AttributeArn`` is the key; attribute value is the value.
        
                      - *(dict) --* 
        
                        The combination of an attribute key and an attribute value.
        
                        - **Key** *(dict) --* 
        
                          The key of the attribute.
        
                          - **SchemaArn** *(string) --* 
        
                            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                          - **FacetName** *(string) --* 
        
                            The name of the facet that the attribute exists within.
        
                          - **Name** *(string) --* 
        
                            The name of the attribute.
        
                        - **Value** *(dict) --* 
        
                          The value of the attribute.
        
                          - **StringValue** *(string) --* 
        
                            A string data value.
        
                          - **BinaryValue** *(bytes) --* 
        
                            A binary data value.
        
                          - **BooleanValue** *(boolean) --* 
        
                            A Boolean data value.
        
                          - **NumberValue** *(string) --* 
        
                            A number data value.
        
                          - **DatetimeValue** *(datetime) --* 
        
                            A date and time value.
        
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **ListObjectChildren** *(dict) --* 
        
                    Returns a paginated list of child objects that are associated with a given object.
        
                    - **Children** *(dict) --* 
        
                      The children structure, which is a map with the key as the ``LinkName`` and ``ObjectIdentifier`` as the value.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **GetObjectInformation** *(dict) --* 
        
                    Retrieves metadata about an object.
        
                    - **SchemaFacets** *(list) --* 
        
                      The facets attached to the specified object.
        
                      - *(dict) --* 
        
                        A facet.
        
                        - **SchemaArn** *(string) --* 
        
                          The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
                        - **FacetName** *(string) --* 
        
                          The name of the facet.
        
                    - **ObjectIdentifier** *(string) --* 
        
                      The ``ObjectIdentifier`` of the specified object.
        
                  - **GetObjectAttributes** *(dict) --* 
        
                    Retrieves attributes within a facet that are associated with an object.
        
                    - **Attributes** *(list) --* 
        
                      The attribute values that are associated with an object.
        
                      - *(dict) --* 
        
                        The combination of an attribute key and an attribute value.
        
                        - **Key** *(dict) --* 
        
                          The key of the attribute.
        
                          - **SchemaArn** *(string) --* 
        
                            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                          - **FacetName** *(string) --* 
        
                            The name of the facet that the attribute exists within.
        
                          - **Name** *(string) --* 
        
                            The name of the attribute.
        
                        - **Value** *(dict) --* 
        
                          The value of the attribute.
        
                          - **StringValue** *(string) --* 
        
                            A string data value.
        
                          - **BinaryValue** *(bytes) --* 
        
                            A binary data value.
        
                          - **BooleanValue** *(boolean) --* 
        
                            A Boolean data value.
        
                          - **NumberValue** *(string) --* 
        
                            A number data value.
        
                          - **DatetimeValue** *(datetime) --* 
        
                            A date and time value.
        
                  - **ListAttachedIndices** *(dict) --* 
        
                    Lists indices attached to an object.
        
                    - **IndexAttachments** *(list) --* 
        
                      The indices attached to the specified object.
        
                      - *(dict) --* 
        
                        Represents an index and an attached object.
        
                        - **IndexedAttributes** *(list) --* 
        
                          The indexed attribute values.
        
                          - *(dict) --* 
        
                            The combination of an attribute key and an attribute value.
        
                            - **Key** *(dict) --* 
        
                              The key of the attribute.
        
                              - **SchemaArn** *(string) --* 
        
                                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                              - **FacetName** *(string) --* 
        
                                The name of the facet that the attribute exists within.
        
                              - **Name** *(string) --* 
        
                                The name of the attribute.
        
                            - **Value** *(dict) --* 
        
                              The value of the attribute.
        
                              - **StringValue** *(string) --* 
        
                                A string data value.
        
                              - **BinaryValue** *(bytes) --* 
        
                                A binary data value.
        
                              - **BooleanValue** *(boolean) --* 
        
                                A Boolean data value.
        
                              - **NumberValue** *(string) --* 
        
                                A number data value.
        
                              - **DatetimeValue** *(datetime) --* 
        
                                A date and time value.
        
                        - **ObjectIdentifier** *(string) --* 
        
                          In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to the object. This field will always contain the ``ObjectIdentifier`` of the object on the opposite side of the attachment specified in the query.
        
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **ListObjectParentPaths** *(dict) --* 
        
                    Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see `Directory Structure <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html>`__ .
        
                    - **PathToObjectIdentifiersList** *(list) --* 
        
                      Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.
        
                      - *(dict) --* 
        
                        Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.
        
                        - **Path** *(string) --* 
        
                          The path that is used to identify the object starting from directory root.
        
                        - **ObjectIdentifiers** *(list) --* 
        
                          Lists ``ObjectIdentifiers`` starting from directory root to the object in the request.
        
                          - *(string) --* 
                      
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **ListObjectPolicies** *(dict) --* 
        
                    Returns policies attached to an object in pagination fashion.
        
                    - **AttachedPolicyIds** *(list) --* 
        
                      A list of policy ``ObjectIdentifiers`` , that are attached to the object.
        
                      - *(string) --* 
                  
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **ListPolicyAttachments** *(dict) --* 
        
                    Returns all of the ``ObjectIdentifiers`` to which a given policy is attached.
        
                    - **ObjectIdentifiers** *(list) --* 
        
                      A list of ``ObjectIdentifiers`` to which the policy is attached.
        
                      - *(string) --* 
                  
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **LookupPolicy** *(dict) --* 
        
                    Lists all policies from the root of the  Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don\'t have the policies attached, it returns the ``ObjectIdentifier`` for such objects. If policies are present, it returns ``ObjectIdentifier`` , ``policyId`` , and ``policyType`` . Paths that don\'t lead to the root from the target object are ignored. For more information, see `Policies <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__ .
        
                    - **PolicyToPathList** *(list) --* 
        
                      Provides list of path to policies. Policies contain ``PolicyId`` , ``ObjectIdentifier`` , and ``PolicyType`` . For more information, see `Policies <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__ .
        
                      - *(dict) --* 
        
                        Used when a regular object exists in a  Directory and you want to find all of the policies that are associated with that object and the parent to that object.
        
                        - **Path** *(string) --* 
        
                          The path that is referenced from the root.
        
                        - **Policies** *(list) --* 
        
                          List of policy objects.
        
                          - *(dict) --* 
        
                            Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to which it is attached. For more information, see `Policies <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__ .
        
                            - **PolicyId** *(string) --* 
        
                              The ID of ``PolicyAttachment`` .
        
                            - **ObjectIdentifier** *(string) --* 
        
                              The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .
        
                            - **PolicyType** *(string) --* 
        
                              The type of policy that can be associated with ``PolicyAttachment`` .
        
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **ListIndex** *(dict) --* 
        
                    Lists objects attached to the specified index.
        
                    - **IndexAttachments** *(list) --* 
        
                      The objects and indexed values attached to the index.
        
                      - *(dict) --* 
        
                        Represents an index and an attached object.
        
                        - **IndexedAttributes** *(list) --* 
        
                          The indexed attribute values.
        
                          - *(dict) --* 
        
                            The combination of an attribute key and an attribute value.
        
                            - **Key** *(dict) --* 
        
                              The key of the attribute.
        
                              - **SchemaArn** *(string) --* 
        
                                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                              - **FacetName** *(string) --* 
        
                                The name of the facet that the attribute exists within.
        
                              - **Name** *(string) --* 
        
                                The name of the attribute.
        
                            - **Value** *(dict) --* 
        
                              The value of the attribute.
        
                              - **StringValue** *(string) --* 
        
                                A string data value.
        
                              - **BinaryValue** *(bytes) --* 
        
                                A binary data value.
        
                              - **BooleanValue** *(boolean) --* 
        
                                A Boolean data value.
        
                              - **NumberValue** *(string) --* 
        
                                A number data value.
        
                              - **DatetimeValue** *(datetime) --* 
        
                                A date and time value.
        
                        - **ObjectIdentifier** *(string) --* 
        
                          In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to the object. This field will always contain the ``ObjectIdentifier`` of the object on the opposite side of the attachment specified in the query.
        
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **ListOutgoingTypedLinks** *(dict) --* 
        
                    Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
                    - **TypedLinkSpecifiers** *(list) --* 
        
                      Returns a typed link specifier as output.
        
                      - *(dict) --* 
        
                        Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.
        
                        - **TypedLinkFacet** *(dict) --* 
        
                          Identifies the typed link facet that is associated with the typed link.
        
                          - **SchemaArn** *(string) --* 
        
                            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                          - **TypedLinkName** *(string) --* 
        
                            The unique name of the typed link facet.
        
                        - **SourceObjectReference** *(dict) --* 
        
                          Identifies the source object that the typed link will attach to.
        
                          - **Selector** *(string) --* 
        
                            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                             
                            * */some/path* - Identifies the object based on path 
                             
                            * *#SomeBatchReference* - Identifies the object in a batch call 
                             
                        - **TargetObjectReference** *(dict) --* 
        
                          Identifies the target object that the typed link will attach to.
        
                          - **Selector** *(string) --* 
        
                            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                             
                            * */some/path* - Identifies the object based on path 
                             
                            * *#SomeBatchReference* - Identifies the object in a batch call 
                             
                        - **IdentityAttributeValues** *(list) --* 
        
                          Identifies the attribute value to update.
        
                          - *(dict) --* 
        
                            Identifies the attribute name and value for a typed link.
        
                            - **AttributeName** *(string) --* 
        
                              The attribute name of the typed link.
        
                            - **Value** *(dict) --* 
        
                              The value for the typed link.
        
                              - **StringValue** *(string) --* 
        
                                A string data value.
        
                              - **BinaryValue** *(bytes) --* 
        
                                A binary data value.
        
                              - **BooleanValue** *(boolean) --* 
        
                                A Boolean data value.
        
                              - **NumberValue** *(string) --* 
        
                                A number data value.
        
                              - **DatetimeValue** *(datetime) --* 
        
                                A date and time value.
        
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **ListIncomingTypedLinks** *(dict) --* 
        
                    Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
                    - **LinkSpecifiers** *(list) --* 
        
                      Returns one or more typed link specifiers as output.
        
                      - *(dict) --* 
        
                        Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.
        
                        - **TypedLinkFacet** *(dict) --* 
        
                          Identifies the typed link facet that is associated with the typed link.
        
                          - **SchemaArn** *(string) --* 
        
                            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                          - **TypedLinkName** *(string) --* 
        
                            The unique name of the typed link facet.
        
                        - **SourceObjectReference** *(dict) --* 
        
                          Identifies the source object that the typed link will attach to.
        
                          - **Selector** *(string) --* 
        
                            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                             
                            * */some/path* - Identifies the object based on path 
                             
                            * *#SomeBatchReference* - Identifies the object in a batch call 
                             
                        - **TargetObjectReference** *(dict) --* 
        
                          Identifies the target object that the typed link will attach to.
        
                          - **Selector** *(string) --* 
        
                            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                             
                            * */some/path* - Identifies the object based on path 
                             
                            * *#SomeBatchReference* - Identifies the object in a batch call 
                             
                        - **IdentityAttributeValues** *(list) --* 
        
                          Identifies the attribute value to update.
        
                          - *(dict) --* 
        
                            Identifies the attribute name and value for a typed link.
        
                            - **AttributeName** *(string) --* 
        
                              The attribute name of the typed link.
        
                            - **Value** *(dict) --* 
        
                              The value for the typed link.
        
                              - **StringValue** *(string) --* 
        
                                A string data value.
        
                              - **BinaryValue** *(bytes) --* 
        
                                A binary data value.
        
                              - **BooleanValue** *(boolean) --* 
        
                                A Boolean data value.
        
                              - **NumberValue** *(string) --* 
        
                                A number data value.
        
                              - **DatetimeValue** *(datetime) --* 
        
                                A date and time value.
        
                    - **NextToken** *(string) --* 
        
                      The pagination token.
        
                  - **GetLinkAttributes** *(dict) --* 
        
                    The list of attributes to retrieve from the typed link.
        
                    - **Attributes** *(list) --* 
        
                      The attributes that are associated with the typed link.
        
                      - *(dict) --* 
        
                        The combination of an attribute key and an attribute value.
        
                        - **Key** *(dict) --* 
        
                          The key of the attribute.
        
                          - **SchemaArn** *(string) --* 
        
                            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                          - **FacetName** *(string) --* 
        
                            The name of the facet that the attribute exists within.
        
                          - **Name** *(string) --* 
        
                            The name of the attribute.
        
                        - **Value** *(dict) --* 
        
                          The value of the attribute.
        
                          - **StringValue** *(string) --* 
        
                            A string data value.
        
                          - **BinaryValue** *(bytes) --* 
        
                            A binary data value.
        
                          - **BooleanValue** *(boolean) --* 
        
                            A Boolean data value.
        
                          - **NumberValue** *(string) --* 
        
                            A number data value.
        
                          - **DatetimeValue** *(datetime) --* 
        
                            A date and time value.
        
                  - **ListObjectParents** *(dict) --* 
                    
                    - **ParentLinks** *(list) --* 
                      
                      - *(dict) --* 
        
                        A pair of ObjectIdentifier and LinkName.
        
                        - **ObjectIdentifier** *(string) --* 
        
                          The ID that is associated with the object.
        
                        - **LinkName** *(string) --* 
        
                          The name of the link between the parent and the child object.
        
                    - **NextToken** *(string) --* 
                
                - **ExceptionResponse** *(dict) --* 
        
                  Identifies which operation in a batch has failed.
        
                  - **Type** *(string) --* 
        
                    A type of exception, such as ``InvalidArnException`` .
        
                  - **Message** *(string) --* 
        
                    An exception message that is associated with the failure.
        
        """
        pass

    def batch_write(self, DirectoryArn: str, Operations: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/BatchWrite>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_write(
              DirectoryArn=\'string\',
              Operations=[
                  {
                      \'CreateObject\': {
                          \'SchemaFacet\': [
                              {
                                  \'SchemaArn\': \'string\',
                                  \'FacetName\': \'string\'
                              },
                          ],
                          \'ObjectAttributeList\': [
                              {
                                  \'Key\': {
                                      \'SchemaArn\': \'string\',
                                      \'FacetName\': \'string\',
                                      \'Name\': \'string\'
                                  },
                                  \'Value\': {
                                      \'StringValue\': \'string\',
                                      \'BinaryValue\': b\'bytes\',
                                      \'BooleanValue\': True|False,
                                      \'NumberValue\': \'string\',
                                      \'DatetimeValue\': datetime(2015, 1, 1)
                                  }
                              },
                          ],
                          \'ParentReference\': {
                              \'Selector\': \'string\'
                          },
                          \'LinkName\': \'string\',
                          \'BatchReferenceName\': \'string\'
                      },
                      \'AttachObject\': {
                          \'ParentReference\': {
                              \'Selector\': \'string\'
                          },
                          \'ChildReference\': {
                              \'Selector\': \'string\'
                          },
                          \'LinkName\': \'string\'
                      },
                      \'DetachObject\': {
                          \'ParentReference\': {
                              \'Selector\': \'string\'
                          },
                          \'LinkName\': \'string\',
                          \'BatchReferenceName\': \'string\'
                      },
                      \'UpdateObjectAttributes\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'AttributeUpdates\': [
                              {
                                  \'ObjectAttributeKey\': {
                                      \'SchemaArn\': \'string\',
                                      \'FacetName\': \'string\',
                                      \'Name\': \'string\'
                                  },
                                  \'ObjectAttributeAction\': {
                                      \'ObjectAttributeActionType\': \'CREATE_OR_UPDATE\'|\'DELETE\',
                                      \'ObjectAttributeUpdateValue\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      }
                                  }
                              },
                          ]
                      },
                      \'DeleteObject\': {
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          }
                      },
                      \'AddFacetToObject\': {
                          \'SchemaFacet\': {
                              \'SchemaArn\': \'string\',
                              \'FacetName\': \'string\'
                          },
                          \'ObjectAttributeList\': [
                              {
                                  \'Key\': {
                                      \'SchemaArn\': \'string\',
                                      \'FacetName\': \'string\',
                                      \'Name\': \'string\'
                                  },
                                  \'Value\': {
                                      \'StringValue\': \'string\',
                                      \'BinaryValue\': b\'bytes\',
                                      \'BooleanValue\': True|False,
                                      \'NumberValue\': \'string\',
                                      \'DatetimeValue\': datetime(2015, 1, 1)
                                  }
                              },
                          ],
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          }
                      },
                      \'RemoveFacetFromObject\': {
                          \'SchemaFacet\': {
                              \'SchemaArn\': \'string\',
                              \'FacetName\': \'string\'
                          },
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          }
                      },
                      \'AttachPolicy\': {
                          \'PolicyReference\': {
                              \'Selector\': \'string\'
                          },
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          }
                      },
                      \'DetachPolicy\': {
                          \'PolicyReference\': {
                              \'Selector\': \'string\'
                          },
                          \'ObjectReference\': {
                              \'Selector\': \'string\'
                          }
                      },
                      \'CreateIndex\': {
                          \'OrderedIndexedAttributeList\': [
                              {
                                  \'SchemaArn\': \'string\',
                                  \'FacetName\': \'string\',
                                  \'Name\': \'string\'
                              },
                          ],
                          \'IsUnique\': True|False,
                          \'ParentReference\': {
                              \'Selector\': \'string\'
                          },
                          \'LinkName\': \'string\',
                          \'BatchReferenceName\': \'string\'
                      },
                      \'AttachToIndex\': {
                          \'IndexReference\': {
                              \'Selector\': \'string\'
                          },
                          \'TargetReference\': {
                              \'Selector\': \'string\'
                          }
                      },
                      \'DetachFromIndex\': {
                          \'IndexReference\': {
                              \'Selector\': \'string\'
                          },
                          \'TargetReference\': {
                              \'Selector\': \'string\'
                          }
                      },
                      \'AttachTypedLink\': {
                          \'SourceObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'TargetObjectReference\': {
                              \'Selector\': \'string\'
                          },
                          \'TypedLinkFacet\': {
                              \'SchemaArn\': \'string\',
                              \'TypedLinkName\': \'string\'
                          },
                          \'Attributes\': [
                              {
                                  \'AttributeName\': \'string\',
                                  \'Value\': {
                                      \'StringValue\': \'string\',
                                      \'BinaryValue\': b\'bytes\',
                                      \'BooleanValue\': True|False,
                                      \'NumberValue\': \'string\',
                                      \'DatetimeValue\': datetime(2015, 1, 1)
                                  }
                              },
                          ]
                      },
                      \'DetachTypedLink\': {
                          \'TypedLinkSpecifier\': {
                              \'TypedLinkFacet\': {
                                  \'SchemaArn\': \'string\',
                                  \'TypedLinkName\': \'string\'
                              },
                              \'SourceObjectReference\': {
                                  \'Selector\': \'string\'
                              },
                              \'TargetObjectReference\': {
                                  \'Selector\': \'string\'
                              },
                              \'IdentityAttributeValues\': [
                                  {
                                      \'AttributeName\': \'string\',
                                      \'Value\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      }
                                  },
                              ]
                          }
                      },
                      \'UpdateLinkAttributes\': {
                          \'TypedLinkSpecifier\': {
                              \'TypedLinkFacet\': {
                                  \'SchemaArn\': \'string\',
                                  \'TypedLinkName\': \'string\'
                              },
                              \'SourceObjectReference\': {
                                  \'Selector\': \'string\'
                              },
                              \'TargetObjectReference\': {
                                  \'Selector\': \'string\'
                              },
                              \'IdentityAttributeValues\': [
                                  {
                                      \'AttributeName\': \'string\',
                                      \'Value\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      }
                                  },
                              ]
                          },
                          \'AttributeUpdates\': [
                              {
                                  \'AttributeKey\': {
                                      \'SchemaArn\': \'string\',
                                      \'FacetName\': \'string\',
                                      \'Name\': \'string\'
                                  },
                                  \'AttributeAction\': {
                                      \'AttributeActionType\': \'CREATE_OR_UPDATE\'|\'DELETE\',
                                      \'AttributeUpdateValue\': {
                                          \'StringValue\': \'string\',
                                          \'BinaryValue\': b\'bytes\',
                                          \'BooleanValue\': True|False,
                                          \'NumberValue\': \'string\',
                                          \'DatetimeValue\': datetime(2015, 1, 1)
                                      }
                                  }
                              },
                          ]
                      }
                  },
              ]
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory . For more information, see  arns .
        
        :type Operations: list
        :param Operations: **[REQUIRED]** 
        
          A list of operations that are part of the batch.
        
          - *(dict) --* 
        
            Represents the output of a ``BatchWrite`` operation. 
        
            - **CreateObject** *(dict) --* 
        
              Creates an object.
        
              - **SchemaFacet** *(list) --* **[REQUIRED]** 
        
                A list of ``FacetArns`` that will be associated with the object. For more information, see  arns .
        
                - *(dict) --* 
        
                  A facet.
        
                  - **SchemaArn** *(string) --* 
        
                    The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
                  - **FacetName** *(string) --* 
        
                    The name of the facet.
        
              - **ObjectAttributeList** *(list) --* **[REQUIRED]** 
        
                An attribute map, which contains an attribute ARN as the key and attribute value as the map value.
        
                - *(dict) --* 
        
                  The combination of an attribute key and an attribute value.
        
                  - **Key** *(dict) --* **[REQUIRED]** 
        
                    The key of the attribute.
        
                    - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                    - **FacetName** *(string) --* **[REQUIRED]** 
        
                      The name of the facet that the attribute exists within.
        
                    - **Name** *(string) --* **[REQUIRED]** 
        
                      The name of the attribute.
        
                  - **Value** *(dict) --* **[REQUIRED]** 
        
                    The value of the attribute.
        
                    - **StringValue** *(string) --* 
        
                      A string data value.
        
                    - **BinaryValue** *(bytes) --* 
        
                      A binary data value.
        
                    - **BooleanValue** *(boolean) --* 
        
                      A Boolean data value.
        
                    - **NumberValue** *(string) --* 
        
                      A number data value.
        
                    - **DatetimeValue** *(datetime) --* 
        
                      A date and time value.
        
              - **ParentReference** *(dict) --* 
        
                If specified, the parent reference to which this object will be attached.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **LinkName** *(string) --* 
        
                The name of the link.
        
              - **BatchReferenceName** *(string) --* 
        
                The batch reference name. See `Transaction Support <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__ for more information.
        
            - **AttachObject** *(dict) --* 
        
              Attaches an object to a  Directory .
        
              - **ParentReference** *(dict) --* **[REQUIRED]** 
        
                The parent object reference.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **ChildReference** *(dict) --* **[REQUIRED]** 
        
                The child object reference that is to be attached to the object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **LinkName** *(string) --* **[REQUIRED]** 
        
                The name of the link.
        
            - **DetachObject** *(dict) --* 
        
              Detaches an object from a  Directory .
        
              - **ParentReference** *(dict) --* **[REQUIRED]** 
        
                Parent reference from which the object with the specified link name is detached.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **LinkName** *(string) --* **[REQUIRED]** 
        
                The name of the link.
        
              - **BatchReferenceName** *(string) --* 
        
                The batch reference name. See `Transaction Support <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__ for more information.
        
            - **UpdateObjectAttributes** *(dict) --* 
        
              Updates a given object\'s attributes.
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                Reference that identifies the object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **AttributeUpdates** *(list) --* **[REQUIRED]** 
        
                Attributes update structure.
        
                - *(dict) --* 
        
                  Structure that contains attribute update information.
        
                  - **ObjectAttributeKey** *(dict) --* 
        
                    The key of the attribute being updated.
        
                    - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                    - **FacetName** *(string) --* **[REQUIRED]** 
        
                      The name of the facet that the attribute exists within.
        
                    - **Name** *(string) --* **[REQUIRED]** 
        
                      The name of the attribute.
        
                  - **ObjectAttributeAction** *(dict) --* 
        
                    The action to perform as part of the attribute update.
        
                    - **ObjectAttributeActionType** *(string) --* 
        
                      A type that can be either ``Update`` or ``Delete`` .
        
                    - **ObjectAttributeUpdateValue** *(dict) --* 
        
                      The value that you want to update to.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
            - **DeleteObject** *(dict) --* 
        
              Deletes an object in a  Directory .
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                The reference that identifies the object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
            - **AddFacetToObject** *(dict) --* 
        
              A batch operation that adds a facet to an object.
        
              - **SchemaFacet** *(dict) --* **[REQUIRED]** 
        
                Represents the facet being added to the object.
        
                - **SchemaArn** *(string) --* 
        
                  The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
                - **FacetName** *(string) --* 
        
                  The name of the facet.
        
              - **ObjectAttributeList** *(list) --* **[REQUIRED]** 
        
                The attributes to set on the object.
        
                - *(dict) --* 
        
                  The combination of an attribute key and an attribute value.
        
                  - **Key** *(dict) --* **[REQUIRED]** 
        
                    The key of the attribute.
        
                    - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                    - **FacetName** *(string) --* **[REQUIRED]** 
        
                      The name of the facet that the attribute exists within.
        
                    - **Name** *(string) --* **[REQUIRED]** 
        
                      The name of the attribute.
        
                  - **Value** *(dict) --* **[REQUIRED]** 
        
                    The value of the attribute.
        
                    - **StringValue** *(string) --* 
        
                      A string data value.
        
                    - **BinaryValue** *(bytes) --* 
        
                      A binary data value.
        
                    - **BooleanValue** *(boolean) --* 
        
                      A Boolean data value.
        
                    - **NumberValue** *(string) --* 
        
                      A number data value.
        
                    - **DatetimeValue** *(datetime) --* 
        
                      A date and time value.
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                A reference to the object being mutated.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
            - **RemoveFacetFromObject** *(dict) --* 
        
              A batch operation that removes a facet from an object.
        
              - **SchemaFacet** *(dict) --* **[REQUIRED]** 
        
                The facet to remove from the object.
        
                - **SchemaArn** *(string) --* 
        
                  The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
                - **FacetName** *(string) --* 
        
                  The name of the facet.
        
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                A reference to the object whose facet will be removed.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
            - **AttachPolicy** *(dict) --* 
        
              Attaches a policy object to a regular object. An object can have a limited number of attached policies.
        
              - **PolicyReference** *(dict) --* **[REQUIRED]** 
        
                The reference that is associated with the policy object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                The reference that identifies the object to which the policy will be attached.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
            - **DetachPolicy** *(dict) --* 
        
              Detaches a policy from a  Directory .
        
              - **PolicyReference** *(dict) --* **[REQUIRED]** 
        
                Reference that identifies the policy object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **ObjectReference** *(dict) --* **[REQUIRED]** 
        
                Reference that identifies the object whose policy object will be detached.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
            - **CreateIndex** *(dict) --* 
        
              Creates an index object. See `Indexing and search <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm>`__ for more information.
        
              - **OrderedIndexedAttributeList** *(list) --* **[REQUIRED]** 
        
                Specifies the attributes that should be indexed on. Currently only a single attribute is supported.
        
                - *(dict) --* 
        
                  A unique identifier for an attribute.
        
                  - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                    The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                  - **FacetName** *(string) --* **[REQUIRED]** 
        
                    The name of the facet that the attribute exists within.
        
                  - **Name** *(string) --* **[REQUIRED]** 
        
                    The name of the attribute.
        
              - **IsUnique** *(boolean) --* **[REQUIRED]** 
        
                Indicates whether the attribute that is being indexed has unique values or not.
        
              - **ParentReference** *(dict) --* 
        
                A reference to the parent object that contains the index object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **LinkName** *(string) --* 
        
                The name of the link between the parent object and the index object.
        
              - **BatchReferenceName** *(string) --* 
        
                The batch reference name. See `Transaction Support <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__ for more information.
        
            - **AttachToIndex** *(dict) --* 
        
              Attaches the specified object to the specified index.
        
              - **IndexReference** *(dict) --* **[REQUIRED]** 
        
                A reference to the index that you are attaching the object to.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **TargetReference** *(dict) --* **[REQUIRED]** 
        
                A reference to the object that you are attaching to the index.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
            - **DetachFromIndex** *(dict) --* 
        
              Detaches the specified object from the specified index.
        
              - **IndexReference** *(dict) --* **[REQUIRED]** 
        
                A reference to the index object.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **TargetReference** *(dict) --* **[REQUIRED]** 
        
                A reference to the object being detached from the index.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
            - **AttachTypedLink** *(dict) --* 
        
              Attaches a typed link to a specified source and target object. For more information, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
              - **SourceObjectReference** *(dict) --* **[REQUIRED]** 
        
                Identifies the source object that the typed link will attach to.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **TargetObjectReference** *(dict) --* **[REQUIRED]** 
        
                Identifies the target object that the typed link will attach to.
        
                - **Selector** *(string) --* 
        
                  A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                  * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                   
                  * */some/path* - Identifies the object based on path 
                   
                  * *#SomeBatchReference* - Identifies the object in a batch call 
                   
              - **TypedLinkFacet** *(dict) --* **[REQUIRED]** 
        
                Identifies the typed link facet that is associated with the typed link.
        
                - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
                  The unique name of the typed link facet.
        
              - **Attributes** *(list) --* **[REQUIRED]** 
        
                A set of attributes that are associated with the typed link.
        
                - *(dict) --* 
        
                  Identifies the attribute name and value for a typed link.
        
                  - **AttributeName** *(string) --* **[REQUIRED]** 
        
                    The attribute name of the typed link.
        
                  - **Value** *(dict) --* **[REQUIRED]** 
        
                    The value for the typed link.
        
                    - **StringValue** *(string) --* 
        
                      A string data value.
        
                    - **BinaryValue** *(bytes) --* 
        
                      A binary data value.
        
                    - **BooleanValue** *(boolean) --* 
        
                      A Boolean data value.
        
                    - **NumberValue** *(string) --* 
        
                      A number data value.
        
                    - **DatetimeValue** *(datetime) --* 
        
                      A date and time value.
        
            - **DetachTypedLink** *(dict) --* 
        
              Detaches a typed link from a specified source and target object. For more information, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
              - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]** 
        
                Used to accept a typed link specifier as input.
        
                - **TypedLinkFacet** *(dict) --* **[REQUIRED]** 
        
                  Identifies the typed link facet that is associated with the typed link.
        
                  - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                    The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                  - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
                    The unique name of the typed link facet.
        
                - **SourceObjectReference** *(dict) --* **[REQUIRED]** 
        
                  Identifies the source object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **TargetObjectReference** *(dict) --* **[REQUIRED]** 
        
                  Identifies the target object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **IdentityAttributeValues** *(list) --* **[REQUIRED]** 
        
                  Identifies the attribute value to update.
        
                  - *(dict) --* 
        
                    Identifies the attribute name and value for a typed link.
        
                    - **AttributeName** *(string) --* **[REQUIRED]** 
        
                      The attribute name of the typed link.
        
                    - **Value** *(dict) --* **[REQUIRED]** 
        
                      The value for the typed link.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
            - **UpdateLinkAttributes** *(dict) --* 
        
              Updates a given object\'s attributes.
        
              - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]** 
        
                Allows a typed link specifier to be accepted as input.
        
                - **TypedLinkFacet** *(dict) --* **[REQUIRED]** 
        
                  Identifies the typed link facet that is associated with the typed link.
        
                  - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                    The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                  - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
                    The unique name of the typed link facet.
        
                - **SourceObjectReference** *(dict) --* **[REQUIRED]** 
        
                  Identifies the source object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **TargetObjectReference** *(dict) --* **[REQUIRED]** 
        
                  Identifies the target object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **IdentityAttributeValues** *(list) --* **[REQUIRED]** 
        
                  Identifies the attribute value to update.
        
                  - *(dict) --* 
        
                    Identifies the attribute name and value for a typed link.
        
                    - **AttributeName** *(string) --* **[REQUIRED]** 
        
                      The attribute name of the typed link.
        
                    - **Value** *(dict) --* **[REQUIRED]** 
        
                      The value for the typed link.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
              - **AttributeUpdates** *(list) --* **[REQUIRED]** 
        
                The attributes update structure.
        
                - *(dict) --* 
        
                  Structure that contains attribute update information.
        
                  - **AttributeKey** *(dict) --* 
        
                    The key of the attribute being updated.
        
                    - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                    - **FacetName** *(string) --* **[REQUIRED]** 
        
                      The name of the facet that the attribute exists within.
        
                    - **Name** *(string) --* **[REQUIRED]** 
        
                      The name of the attribute.
        
                  - **AttributeAction** *(dict) --* 
        
                    The action to perform as part of the attribute update.
        
                    - **AttributeActionType** *(string) --* 
        
                      A type that can be either ``UPDATE_OR_CREATE`` or ``DELETE`` .
        
                    - **AttributeUpdateValue** *(dict) --* 
        
                      The value that you want to update to.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Responses\': [
                    {
                        \'CreateObject\': {
                            \'ObjectIdentifier\': \'string\'
                        },
                        \'AttachObject\': {
                            \'attachedObjectIdentifier\': \'string\'
                        },
                        \'DetachObject\': {
                            \'detachedObjectIdentifier\': \'string\'
                        },
                        \'UpdateObjectAttributes\': {
                            \'ObjectIdentifier\': \'string\'
                        },
                        \'DeleteObject\': {},
                        \'AddFacetToObject\': {},
                        \'RemoveFacetFromObject\': {},
                        \'AttachPolicy\': {},
                        \'DetachPolicy\': {},
                        \'CreateIndex\': {
                            \'ObjectIdentifier\': \'string\'
                        },
                        \'AttachToIndex\': {
                            \'AttachedObjectIdentifier\': \'string\'
                        },
                        \'DetachFromIndex\': {
                            \'DetachedObjectIdentifier\': \'string\'
                        },
                        \'AttachTypedLink\': {
                            \'TypedLinkSpecifier\': {
                                \'TypedLinkFacet\': {
                                    \'SchemaArn\': \'string\',
                                    \'TypedLinkName\': \'string\'
                                },
                                \'SourceObjectReference\': {
                                    \'Selector\': \'string\'
                                },
                                \'TargetObjectReference\': {
                                    \'Selector\': \'string\'
                                },
                                \'IdentityAttributeValues\': [
                                    {
                                        \'AttributeName\': \'string\',
                                        \'Value\': {
                                            \'StringValue\': \'string\',
                                            \'BinaryValue\': b\'bytes\',
                                            \'BooleanValue\': True|False,
                                            \'NumberValue\': \'string\',
                                            \'DatetimeValue\': datetime(2015, 1, 1)
                                        }
                                    },
                                ]
                            }
                        },
                        \'DetachTypedLink\': {},
                        \'UpdateLinkAttributes\': {}
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Responses** *(list) --* 
        
              A list of all the responses for each batch write.
        
              - *(dict) --* 
        
                Represents the output of a ``BatchWrite`` response operation.
        
                - **CreateObject** *(dict) --* 
        
                  Creates an object in a  Directory .
        
                  - **ObjectIdentifier** *(string) --* 
        
                    The ID that is associated with the object.
        
                - **AttachObject** *(dict) --* 
        
                  Attaches an object to a  Directory .
        
                  - **attachedObjectIdentifier** *(string) --* 
        
                    The ``ObjectIdentifier`` of the object that has been attached.
        
                - **DetachObject** *(dict) --* 
        
                  Detaches an object from a  Directory .
        
                  - **detachedObjectIdentifier** *(string) --* 
        
                    The ``ObjectIdentifier`` of the detached object.
        
                - **UpdateObjectAttributes** *(dict) --* 
        
                  Updates a given object’s attributes.
        
                  - **ObjectIdentifier** *(string) --* 
        
                    ID that is associated with the object.
        
                - **DeleteObject** *(dict) --* 
        
                  Deletes an object in a  Directory .
        
                - **AddFacetToObject** *(dict) --* 
        
                  The result of an add facet to object batch operation.
        
                - **RemoveFacetFromObject** *(dict) --* 
        
                  The result of a batch remove facet from object operation.
        
                - **AttachPolicy** *(dict) --* 
        
                  Attaches a policy object to a regular object. An object can have a limited number of attached policies.
        
                - **DetachPolicy** *(dict) --* 
        
                  Detaches a policy from a  Directory .
        
                - **CreateIndex** *(dict) --* 
        
                  Creates an index object. See `Indexing and search <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm>`__ for more information.
        
                  - **ObjectIdentifier** *(string) --* 
        
                    The ``ObjectIdentifier`` of the index created by this operation.
        
                - **AttachToIndex** *(dict) --* 
        
                  Attaches the specified object to the specified index.
        
                  - **AttachedObjectIdentifier** *(string) --* 
        
                    The ``ObjectIdentifier`` of the object that was attached to the index.
        
                - **DetachFromIndex** *(dict) --* 
        
                  Detaches the specified object from the specified index.
        
                  - **DetachedObjectIdentifier** *(string) --* 
        
                    The ``ObjectIdentifier`` of the object that was detached from the index.
        
                - **AttachTypedLink** *(dict) --* 
        
                  Attaches a typed link to a specified source and target object. For more information, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
                  - **TypedLinkSpecifier** *(dict) --* 
        
                    Returns a typed link specifier as output.
        
                    - **TypedLinkFacet** *(dict) --* 
        
                      Identifies the typed link facet that is associated with the typed link.
        
                      - **SchemaArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                      - **TypedLinkName** *(string) --* 
        
                        The unique name of the typed link facet.
        
                    - **SourceObjectReference** *(dict) --* 
        
                      Identifies the source object that the typed link will attach to.
        
                      - **Selector** *(string) --* 
        
                        A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                         
                        * */some/path* - Identifies the object based on path 
                         
                        * *#SomeBatchReference* - Identifies the object in a batch call 
                         
                    - **TargetObjectReference** *(dict) --* 
        
                      Identifies the target object that the typed link will attach to.
        
                      - **Selector** *(string) --* 
        
                        A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                         
                        * */some/path* - Identifies the object based on path 
                         
                        * *#SomeBatchReference* - Identifies the object in a batch call 
                         
                    - **IdentityAttributeValues** *(list) --* 
        
                      Identifies the attribute value to update.
        
                      - *(dict) --* 
        
                        Identifies the attribute name and value for a typed link.
        
                        - **AttributeName** *(string) --* 
        
                          The attribute name of the typed link.
        
                        - **Value** *(dict) --* 
        
                          The value for the typed link.
        
                          - **StringValue** *(string) --* 
        
                            A string data value.
        
                          - **BinaryValue** *(bytes) --* 
        
                            A binary data value.
        
                          - **BooleanValue** *(boolean) --* 
        
                            A Boolean data value.
        
                          - **NumberValue** *(string) --* 
        
                            A number data value.
        
                          - **DatetimeValue** *(datetime) --* 
        
                            A date and time value.
        
                - **DetachTypedLink** *(dict) --* 
        
                  Detaches a typed link from a specified source and target object. For more information, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
                - **UpdateLinkAttributes** *(dict) --* 
        
                  Represents the output of a ``BatchWrite`` response operation.
        
        """
        pass

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

    def create_directory(self, Name: str, SchemaArn: str) -> Dict:
        """
        
        You can also quickly create a directory using a managed schema, called the ``QuickStartSchema`` . For more information, see `Managed Schema <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_managed.html>`__ in the *Amazon Cloud Directory Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/CreateDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_directory(
              Name=\'string\',
              SchemaArn=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the  Directory . Should be unique per account, per region.
        
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the published schema that will be copied into the data  Directory . For more information, see  arns .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryArn\': \'string\',
                \'Name\': \'string\',
                \'ObjectIdentifier\': \'string\',
                \'AppliedSchemaArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DirectoryArn** *(string) --* 
        
              The ARN that is associated with the  Directory . For more information, see  arns .
        
            - **Name** *(string) --* 
        
              The name of the  Directory .
        
            - **ObjectIdentifier** *(string) --* 
        
              The root object node of the created directory.
        
            - **AppliedSchemaArn** *(string) --* 
        
              The ARN of the published schema in the  Directory . Once a published schema is copied into the directory, it has its own ARN, which is referred to applied schema ARN. For more information, see  arns .
        
        """
        pass

    def create_facet(self, SchemaArn: str, Name: str, Attributes: List = None, ObjectType: str = None, FacetStyle: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/CreateFacet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_facet(
              SchemaArn=\'string\',
              Name=\'string\',
              Attributes=[
                  {
                      \'Name\': \'string\',
                      \'AttributeDefinition\': {
                          \'Type\': \'STRING\'|\'BINARY\'|\'BOOLEAN\'|\'NUMBER\'|\'DATETIME\'|\'VARIANT\',
                          \'DefaultValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          },
                          \'IsImmutable\': True|False,
                          \'Rules\': {
                              \'string\': {
                                  \'Type\': \'BINARY_LENGTH\'|\'NUMBER_COMPARISON\'|\'STRING_FROM_SET\'|\'STRING_LENGTH\',
                                  \'Parameters\': {
                                      \'string\': \'string\'
                                  }
                              }
                          }
                      },
                      \'AttributeReference\': {
                          \'TargetFacetName\': \'string\',
                          \'TargetAttributeName\': \'string\'
                      },
                      \'RequiredBehavior\': \'REQUIRED_ALWAYS\'|\'NOT_REQUIRED\'
                  },
              ],
              ObjectType=\'NODE\'|\'LEAF_NODE\'|\'POLICY\'|\'INDEX\',
              FacetStyle=\'STATIC\'|\'DYNAMIC\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The schema ARN in which the new  Facet will be created. For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the  Facet , which is unique for a given schema.
        
        :type Attributes: list
        :param Attributes: 
        
          The attributes that are associated with the  Facet .
        
          - *(dict) --* 
        
            An attribute that is associated with the  Facet .
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the facet attribute.
        
            - **AttributeDefinition** *(dict) --* 
        
              A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                The type of the attribute.
        
              - **DefaultValue** *(dict) --* 
        
                The default value of the attribute (if configured).
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
              - **IsImmutable** *(boolean) --* 
        
                Whether the attribute is mutable or not.
        
              - **Rules** *(dict) --* 
        
                Validation rules attached to the attribute definition.
        
                - *(string) --* 
        
                  - *(dict) --* 
        
                    Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
        
                    - **Type** *(string) --* 
        
                      The type of attribute validation rule.
        
                    - **Parameters** *(dict) --* 
        
                      The minimum and maximum parameters that are associated with the rule.
        
                      - *(string) --* 
        
                        - *(string) --* 
        
            - **AttributeReference** *(dict) --* 
        
              An attribute reference that is associated with the attribute. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
              - **TargetFacetName** *(string) --* **[REQUIRED]** 
        
                The target facet name that is associated with the facet reference. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
              - **TargetAttributeName** *(string) --* **[REQUIRED]** 
        
                The target attribute name that is associated with the facet reference. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
            - **RequiredBehavior** *(string) --* 
        
              The required behavior of the ``FacetAttribute`` .
        
        :type ObjectType: string
        :param ObjectType: 
        
          Specifies whether a given object created from this facet is of type node, leaf node, policy or index.
        
          * Node: Can have multiple children but one parent. 
           
          * Leaf node: Cannot have children but can have multiple parents. 
           
          * Policy: Allows you to store a policy document and policy type. For more information, see `Policies <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__ . 
           
          * Index: Can be created with the Index API. 
           
        :type FacetStyle: string
        :param FacetStyle: 
        
          There are two different styles that you can define on any given facet, ``Static`` and ``Dynamic`` . For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def create_index(self, DirectoryArn: str, OrderedIndexedAttributeList: List, IsUnique: bool, ParentReference: Dict = None, LinkName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/CreateIndex>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_index(
              DirectoryArn=\'string\',
              OrderedIndexedAttributeList=[
                  {
                      \'SchemaArn\': \'string\',
                      \'FacetName\': \'string\',
                      \'Name\': \'string\'
                  },
              ],
              IsUnique=True|False,
              ParentReference={
                  \'Selector\': \'string\'
              },
              LinkName=\'string\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory where the index should be created.
        
        :type OrderedIndexedAttributeList: list
        :param OrderedIndexedAttributeList: **[REQUIRED]** 
        
          Specifies the attributes that should be indexed on. Currently only a single attribute is supported.
        
          - *(dict) --* 
        
            A unique identifier for an attribute.
        
            - **SchemaArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
            - **FacetName** *(string) --* **[REQUIRED]** 
        
              The name of the facet that the attribute exists within.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the attribute.
        
        :type IsUnique: boolean
        :param IsUnique: **[REQUIRED]** 
        
          Indicates whether the attribute that is being indexed has unique values or not.
        
        :type ParentReference: dict
        :param ParentReference: 
        
          A reference to the parent object that contains the index object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type LinkName: string
        :param LinkName: 
        
          The name of the link between the parent object and the index object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ObjectIdentifier\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ObjectIdentifier** *(string) --* 
        
              The ``ObjectIdentifier`` of the index created by this operation.
        
        """
        pass

    def create_object(self, DirectoryArn: str, SchemaFacets: List, ObjectAttributeList: List = None, ParentReference: Dict = None, LinkName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/CreateObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_object(
              DirectoryArn=\'string\',
              SchemaFacets=[
                  {
                      \'SchemaArn\': \'string\',
                      \'FacetName\': \'string\'
                  },
              ],
              ObjectAttributeList=[
                  {
                      \'Key\': {
                          \'SchemaArn\': \'string\',
                          \'FacetName\': \'string\',
                          \'Name\': \'string\'
                      },
                      \'Value\': {
                          \'StringValue\': \'string\',
                          \'BinaryValue\': b\'bytes\',
                          \'BooleanValue\': True|False,
                          \'NumberValue\': \'string\',
                          \'DatetimeValue\': datetime(2015, 1, 1)
                      }
                  },
              ],
              ParentReference={
                  \'Selector\': \'string\'
              },
              LinkName=\'string\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory in which the object will be created. For more information, see  arns .
        
        :type SchemaFacets: list
        :param SchemaFacets: **[REQUIRED]** 
        
          A list of schema facets to be associated with the object. Do not provide minor version components. See  SchemaFacet for details.
        
          - *(dict) --* 
        
            A facet.
        
            - **SchemaArn** *(string) --* 
        
              The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
            - **FacetName** *(string) --* 
        
              The name of the facet.
        
        :type ObjectAttributeList: list
        :param ObjectAttributeList: 
        
          The attribute map whose attribute ARN contains the key and attribute value as the map value.
        
          - *(dict) --* 
        
            The combination of an attribute key and an attribute value.
        
            - **Key** *(dict) --* **[REQUIRED]** 
        
              The key of the attribute.
        
              - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
              - **FacetName** *(string) --* **[REQUIRED]** 
        
                The name of the facet that the attribute exists within.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                The name of the attribute.
        
            - **Value** *(dict) --* **[REQUIRED]** 
        
              The value of the attribute.
        
              - **StringValue** *(string) --* 
        
                A string data value.
        
              - **BinaryValue** *(bytes) --* 
        
                A binary data value.
        
              - **BooleanValue** *(boolean) --* 
        
                A Boolean data value.
        
              - **NumberValue** *(string) --* 
        
                A number data value.
        
              - **DatetimeValue** *(datetime) --* 
        
                A date and time value.
        
        :type ParentReference: dict
        :param ParentReference: 
        
          If specified, the parent reference to which this object will be attached.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type LinkName: string
        :param LinkName: 
        
          The name of link that is used to attach this object to a parent.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ObjectIdentifier\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ObjectIdentifier** *(string) --* 
        
              The identifier that is associated with the object.
        
        """
        pass

    def create_schema(self, Name: str) -> Dict:
        """
        Creates a new schema in a development state. A schema can exist in three phases:
        
        * *Development:* This is a mutable phase of the schema. All new schemas are in the development phase. Once the schema is finalized, it can be published. 
         
        * *Published:* Published schemas are immutable and have a version associated with them. 
         
        * *Applied:* Applied schemas are mutable in a way that allows you to add new schema facets. You can also add new, nonrequired attributes to existing schema facets. You can apply only published schemas to directories.  
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/CreateSchema>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_schema(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name that is associated with the schema. This is unique to each account and in each region.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArn** *(string) --* 
        
              The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
        """
        pass

    def create_typed_link_facet(self, SchemaArn: str, Facet: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/CreateTypedLinkFacet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_typed_link_facet(
              SchemaArn=\'string\',
              Facet={
                  \'Name\': \'string\',
                  \'Attributes\': [
                      {
                          \'Name\': \'string\',
                          \'Type\': \'STRING\'|\'BINARY\'|\'BOOLEAN\'|\'NUMBER\'|\'DATETIME\'|\'VARIANT\',
                          \'DefaultValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          },
                          \'IsImmutable\': True|False,
                          \'Rules\': {
                              \'string\': {
                                  \'Type\': \'BINARY_LENGTH\'|\'NUMBER_COMPARISON\'|\'STRING_FROM_SET\'|\'STRING_LENGTH\',
                                  \'Parameters\': {
                                      \'string\': \'string\'
                                  }
                              }
                          },
                          \'RequiredBehavior\': \'REQUIRED_ALWAYS\'|\'NOT_REQUIRED\'
                      },
                  ],
                  \'IdentityAttributeOrder\': [
                      \'string\',
                  ]
              }
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
        :type Facet: dict
        :param Facet: **[REQUIRED]** 
        
            Facet structure that is associated with the typed link facet.
        
          - **Name** *(string) --* **[REQUIRED]** 
        
            The unique name of the typed link facet.
        
          - **Attributes** *(list) --* **[REQUIRED]** 
        
            A set of key-value pairs associated with the typed link. Typed link attributes are used when you have data values that are related to the link itself, and not to one of the two objects being linked. Identity attributes also serve to distinguish the link from others of the same type between the same objects.
        
            - *(dict) --* 
        
              A typed link attribute definition.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                The unique name of the typed link attribute.
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                The type of the attribute.
        
              - **DefaultValue** *(dict) --* 
        
                The default value of the attribute (if configured).
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
              - **IsImmutable** *(boolean) --* 
        
                Whether the attribute is mutable or not.
        
              - **Rules** *(dict) --* 
        
                Validation rules that are attached to the attribute definition.
        
                - *(string) --* 
        
                  - *(dict) --* 
        
                    Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
        
                    - **Type** *(string) --* 
        
                      The type of attribute validation rule.
        
                    - **Parameters** *(dict) --* 
        
                      The minimum and maximum parameters that are associated with the rule.
        
                      - *(string) --* 
        
                        - *(string) --* 
        
              - **RequiredBehavior** *(string) --* **[REQUIRED]** 
        
                The required behavior of the ``TypedLinkAttributeDefinition`` .
        
          - **IdentityAttributeOrder** *(list) --* **[REQUIRED]** 
        
            The set of attributes that distinguish links made from this facet from each other, in the order of significance. Listing typed links can filter on the values of these attributes. See  ListOutgoingTypedLinks and  ListIncomingTypedLinks for details.
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_directory(self, DirectoryArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DeleteDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_directory(
              DirectoryArn=\'string\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DirectoryArn** *(string) --* 
        
              The ARN of the deleted directory.
        
        """
        pass

    def delete_facet(self, SchemaArn: str, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DeleteFacet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_facet(
              SchemaArn=\'string\',
              Name=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Facet . For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the facet to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_object(self, DirectoryArn: str, ObjectReference: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DeleteObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_object(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides. For more information, see  arns .
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          A reference that identifies the object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_schema(self, SchemaArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DeleteSchema>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_schema(
              SchemaArn=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the development schema. For more information, see  arns .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArn** *(string) --* 
        
              The input ARN that is returned as part of the response. For more information, see  arns .
        
        """
        pass

    def delete_typed_link_facet(self, SchemaArn: str, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DeleteTypedLinkFacet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_typed_link_facet(
              SchemaArn=\'string\',
              Name=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The unique name of the typed link facet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def detach_from_index(self, DirectoryArn: str, IndexReference: Dict, TargetReference: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DetachFromIndex>`_
        
        **Request Syntax** 
        ::
        
          response = client.detach_from_index(
              DirectoryArn=\'string\',
              IndexReference={
                  \'Selector\': \'string\'
              },
              TargetReference={
                  \'Selector\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the directory the index and object exist in.
        
        :type IndexReference: dict
        :param IndexReference: **[REQUIRED]** 
        
          A reference to the index object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type TargetReference: dict
        :param TargetReference: **[REQUIRED]** 
        
          A reference to the object being detached from the index.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DetachedObjectIdentifier\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DetachedObjectIdentifier** *(string) --* 
        
              The ``ObjectIdentifier`` of the object that was detached from the index.
        
        """
        pass

    def detach_object(self, DirectoryArn: str, ParentReference: Dict, LinkName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DetachObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.detach_object(
              DirectoryArn=\'string\',
              ParentReference={
                  \'Selector\': \'string\'
              },
              LinkName=\'string\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where objects reside. For more information, see  arns .
        
        :type ParentReference: dict
        :param ParentReference: **[REQUIRED]** 
        
          The parent reference from which the object with the specified link name is detached.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type LinkName: string
        :param LinkName: **[REQUIRED]** 
        
          The link name associated with the object that needs to be detached.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DetachedObjectIdentifier\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DetachedObjectIdentifier** *(string) --* 
        
              The ``ObjectIdentifier`` that was detached from the object.
        
        """
        pass

    def detach_policy(self, DirectoryArn: str, PolicyReference: Dict, ObjectReference: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DetachPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.detach_policy(
              DirectoryArn=\'string\',
              PolicyReference={
                  \'Selector\': \'string\'
              },
              ObjectReference={
                  \'Selector\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where both objects reside. For more information, see  arns .
        
        :type PolicyReference: dict
        :param PolicyReference: **[REQUIRED]** 
        
          Reference that identifies the policy object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          Reference that identifies the object whose policy object will be detached.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def detach_typed_link(self, DirectoryArn: str, TypedLinkSpecifier: Dict):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DetachTypedLink>`_
        
        **Request Syntax** 
        ::
        
          response = client.detach_typed_link(
              DirectoryArn=\'string\',
              TypedLinkSpecifier={
                  \'TypedLinkFacet\': {
                      \'SchemaArn\': \'string\',
                      \'TypedLinkName\': \'string\'
                  },
                  \'SourceObjectReference\': {
                      \'Selector\': \'string\'
                  },
                  \'TargetObjectReference\': {
                      \'Selector\': \'string\'
                  },
                  \'IdentityAttributeValues\': [
                      {
                          \'AttributeName\': \'string\',
                          \'Value\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          }
                      },
                  ]
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the directory where you want to detach the typed link.
        
        :type TypedLinkSpecifier: dict
        :param TypedLinkSpecifier: **[REQUIRED]** 
        
          Used to accept a typed link specifier as input.
        
          - **TypedLinkFacet** *(dict) --* **[REQUIRED]** 
        
            Identifies the typed link facet that is associated with the typed link.
        
            - **SchemaArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
            - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
              The unique name of the typed link facet.
        
          - **SourceObjectReference** *(dict) --* **[REQUIRED]** 
        
            Identifies the source object that the typed link will attach to.
        
            - **Selector** *(string) --* 
        
              A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
              * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
               
              * */some/path* - Identifies the object based on path 
               
              * *#SomeBatchReference* - Identifies the object in a batch call 
               
          - **TargetObjectReference** *(dict) --* **[REQUIRED]** 
        
            Identifies the target object that the typed link will attach to.
        
            - **Selector** *(string) --* 
        
              A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
              * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
               
              * */some/path* - Identifies the object based on path 
               
              * *#SomeBatchReference* - Identifies the object in a batch call 
               
          - **IdentityAttributeValues** *(list) --* **[REQUIRED]** 
        
            Identifies the attribute value to update.
        
            - *(dict) --* 
        
              Identifies the attribute name and value for a typed link.
        
              - **AttributeName** *(string) --* **[REQUIRED]** 
        
                The attribute name of the typed link.
        
              - **Value** *(dict) --* **[REQUIRED]** 
        
                The value for the typed link.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
        :returns: None
        """
        pass

    def disable_directory(self, DirectoryArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/DisableDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_directory(
              DirectoryArn=\'string\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory to disable.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DirectoryArn** *(string) --* 
        
              The ARN of the directory that has been disabled.
        
        """
        pass

    def enable_directory(self, DirectoryArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/EnableDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_directory(
              DirectoryArn=\'string\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory to enable.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DirectoryArn** *(string) --* 
        
              The ARN of the enabled directory.
        
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

    def get_applied_schema_version(self, SchemaArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/GetAppliedSchemaVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_applied_schema_version(
              SchemaArn=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The ARN of the applied schema.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AppliedSchemaArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AppliedSchemaArn** *(string) --* 
        
              Current applied schema ARN, including the minor version in use if one was provided.
        
        """
        pass

    def get_directory(self, DirectoryArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/GetDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_directory(
              DirectoryArn=\'string\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Directory\': {
                    \'Name\': \'string\',
                    \'DirectoryArn\': \'string\',
                    \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                    \'CreationDateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Directory** *(dict) --* 
        
              Metadata about the directory.
        
              - **Name** *(string) --* 
        
                The name of the directory.
        
              - **DirectoryArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that is associated with the directory. For more information, see  arns .
        
              - **State** *(string) --* 
        
                The state of the directory. Can be either ``Enabled`` , ``Disabled`` , or ``Deleted`` .
        
              - **CreationDateTime** *(datetime) --* 
        
                The date and time when the directory was created.
        
        """
        pass

    def get_facet(self, SchemaArn: str, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/GetFacet>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_facet(
              SchemaArn=\'string\',
              Name=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Facet . For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the facet to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Facet\': {
                    \'Name\': \'string\',
                    \'ObjectType\': \'NODE\'|\'LEAF_NODE\'|\'POLICY\'|\'INDEX\',
                    \'FacetStyle\': \'STATIC\'|\'DYNAMIC\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Facet** *(dict) --* 
        
              The  Facet structure that is associated with the facet.
        
              - **Name** *(string) --* 
        
                The name of the  Facet .
        
              - **ObjectType** *(string) --* 
        
                The object type that is associated with the facet. See  CreateFacetRequest$ObjectType for more details.
        
              - **FacetStyle** *(string) --* 
        
                There are two different styles that you can define on any given facet, ``Static`` and ``Dynamic`` . For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.
        
        """
        pass

    def get_link_attributes(self, DirectoryArn: str, TypedLinkSpecifier: Dict, AttributeNames: List, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/GetLinkAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_link_attributes(
              DirectoryArn=\'string\',
              TypedLinkSpecifier={
                  \'TypedLinkFacet\': {
                      \'SchemaArn\': \'string\',
                      \'TypedLinkName\': \'string\'
                  },
                  \'SourceObjectReference\': {
                      \'Selector\': \'string\'
                  },
                  \'TargetObjectReference\': {
                      \'Selector\': \'string\'
                  },
                  \'IdentityAttributeValues\': [
                      {
                          \'AttributeName\': \'string\',
                          \'Value\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          }
                      },
                  ]
              },
              AttributeNames=[
                  \'string\',
              ],
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see  arns or `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
        :type TypedLinkSpecifier: dict
        :param TypedLinkSpecifier: **[REQUIRED]** 
        
          Allows a typed link specifier to be accepted as input.
        
          - **TypedLinkFacet** *(dict) --* **[REQUIRED]** 
        
            Identifies the typed link facet that is associated with the typed link.
        
            - **SchemaArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
            - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
              The unique name of the typed link facet.
        
          - **SourceObjectReference** *(dict) --* **[REQUIRED]** 
        
            Identifies the source object that the typed link will attach to.
        
            - **Selector** *(string) --* 
        
              A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
              * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
               
              * */some/path* - Identifies the object based on path 
               
              * *#SomeBatchReference* - Identifies the object in a batch call 
               
          - **TargetObjectReference** *(dict) --* **[REQUIRED]** 
        
            Identifies the target object that the typed link will attach to.
        
            - **Selector** *(string) --* 
        
              A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
              * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
               
              * */some/path* - Identifies the object based on path 
               
              * *#SomeBatchReference* - Identifies the object in a batch call 
               
          - **IdentityAttributeValues** *(list) --* **[REQUIRED]** 
        
            Identifies the attribute value to update.
        
            - *(dict) --* 
        
              Identifies the attribute name and value for a typed link.
        
              - **AttributeName** *(string) --* **[REQUIRED]** 
        
                The attribute name of the typed link.
        
              - **Value** *(dict) --* **[REQUIRED]** 
        
                The value for the typed link.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
        :type AttributeNames: list
        :param AttributeNames: **[REQUIRED]** 
        
          A list of attribute names whose values will be retrieved.
        
          - *(string) --* 
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level at which to retrieve the attributes on a typed link.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Key\': {
                            \'SchemaArn\': \'string\',
                            \'FacetName\': \'string\',
                            \'Name\': \'string\'
                        },
                        \'Value\': {
                            \'StringValue\': \'string\',
                            \'BinaryValue\': b\'bytes\',
                            \'BooleanValue\': True|False,
                            \'NumberValue\': \'string\',
                            \'DatetimeValue\': datetime(2015, 1, 1)
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              The attributes that are associated with the typed link.
        
              - *(dict) --* 
        
                The combination of an attribute key and an attribute value.
        
                - **Key** *(dict) --* 
        
                  The key of the attribute.
        
                  - **SchemaArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                  - **FacetName** *(string) --* 
        
                    The name of the facet that the attribute exists within.
        
                  - **Name** *(string) --* 
        
                    The name of the attribute.
        
                - **Value** *(dict) --* 
        
                  The value of the attribute.
        
                  - **StringValue** *(string) --* 
        
                    A string data value.
        
                  - **BinaryValue** *(bytes) --* 
        
                    A binary data value.
        
                  - **BooleanValue** *(boolean) --* 
        
                    A Boolean data value.
        
                  - **NumberValue** *(string) --* 
        
                    A number data value.
        
                  - **DatetimeValue** *(datetime) --* 
        
                    A date and time value.
        
        """
        pass

    def get_object_attributes(self, DirectoryArn: str, ObjectReference: Dict, SchemaFacet: Dict, AttributeNames: List, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/GetObjectAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_object_attributes(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\',
              SchemaFacet={
                  \'SchemaArn\': \'string\',
                  \'FacetName\': \'string\'
              },
              AttributeNames=[
                  \'string\',
              ]
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides.
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          Reference that identifies the object whose attributes will be retrieved.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level at which to retrieve the attributes on an object.
        
        :type SchemaFacet: dict
        :param SchemaFacet: **[REQUIRED]** 
        
          Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.
        
          - **SchemaArn** *(string) --* 
        
            The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
          - **FacetName** *(string) --* 
        
            The name of the facet.
        
        :type AttributeNames: list
        :param AttributeNames: **[REQUIRED]** 
        
          List of attribute names whose values will be retrieved.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Key\': {
                            \'SchemaArn\': \'string\',
                            \'FacetName\': \'string\',
                            \'Name\': \'string\'
                        },
                        \'Value\': {
                            \'StringValue\': \'string\',
                            \'BinaryValue\': b\'bytes\',
                            \'BooleanValue\': True|False,
                            \'NumberValue\': \'string\',
                            \'DatetimeValue\': datetime(2015, 1, 1)
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              The attributes that are associated with the object.
        
              - *(dict) --* 
        
                The combination of an attribute key and an attribute value.
        
                - **Key** *(dict) --* 
        
                  The key of the attribute.
        
                  - **SchemaArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                  - **FacetName** *(string) --* 
        
                    The name of the facet that the attribute exists within.
        
                  - **Name** *(string) --* 
        
                    The name of the attribute.
        
                - **Value** *(dict) --* 
        
                  The value of the attribute.
        
                  - **StringValue** *(string) --* 
        
                    A string data value.
        
                  - **BinaryValue** *(bytes) --* 
        
                    A binary data value.
        
                  - **BooleanValue** *(boolean) --* 
        
                    A Boolean data value.
        
                  - **NumberValue** *(string) --* 
        
                    A number data value.
        
                  - **DatetimeValue** *(datetime) --* 
        
                    A date and time value.
        
        """
        pass

    def get_object_information(self, DirectoryArn: str, ObjectReference: Dict, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/GetObjectInformation>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_object_information(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory being retrieved.
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          A reference to the object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level at which to retrieve the object information.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaFacets\': [
                    {
                        \'SchemaArn\': \'string\',
                        \'FacetName\': \'string\'
                    },
                ],
                \'ObjectIdentifier\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaFacets** *(list) --* 
        
              The facets attached to the specified object. Although the response does not include minor version information, the most recently applied minor version of each Facet is in effect. See  GetAppliedSchemaVersion for details.
        
              - *(dict) --* 
        
                A facet.
        
                - **SchemaArn** *(string) --* 
        
                  The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
                - **FacetName** *(string) --* 
        
                  The name of the facet.
        
            - **ObjectIdentifier** *(string) --* 
        
              The ``ObjectIdentifier`` of the specified object.
        
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

    def get_schema_as_json(self, SchemaArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/GetSchemaAsJson>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_schema_as_json(
              SchemaArn=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The ARN of the schema to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\',
                \'Document\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Name** *(string) --* 
        
              The name of the retrieved schema.
        
            - **Document** *(string) --* 
        
              The JSON representation of the schema document.
        
        """
        pass

    def get_typed_link_facet_information(self, SchemaArn: str, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/GetTypedLinkFacetInformation>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_typed_link_facet_information(
              SchemaArn=\'string\',
              Name=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The unique name of the typed link facet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityAttributeOrder\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **IdentityAttributeOrder** *(list) --* 
        
              The order of identity attributes for the facet, from most significant to least significant. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls. For more information about identity attributes, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
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

    def list_applied_schema_arns(self, DirectoryArn: str, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListAppliedSchemaArns>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_applied_schema_arns(
              DirectoryArn=\'string\',
              SchemaArn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory you are listing.
        
        :type SchemaArn: string
        :param SchemaArn: 
        
          The response for ``ListAppliedSchemaArns`` when this parameter is used will list all minor version ARNs for a major version.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArns** *(list) --* 
        
              The ARNs of schemas that are applied to the directory.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_attached_indices(self, DirectoryArn: str, TargetReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListAttachedIndices>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_attached_indices(
              DirectoryArn=\'string\',
              TargetReference={
                  \'Selector\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123,
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory.
        
        :type TargetReference: dict
        :param TargetReference: **[REQUIRED]** 
        
          A reference to the object that has indices attached.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level to use for this operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IndexAttachments\': [
                    {
                        \'IndexedAttributes\': [
                            {
                                \'Key\': {
                                    \'SchemaArn\': \'string\',
                                    \'FacetName\': \'string\',
                                    \'Name\': \'string\'
                                },
                                \'Value\': {
                                    \'StringValue\': \'string\',
                                    \'BinaryValue\': b\'bytes\',
                                    \'BooleanValue\': True|False,
                                    \'NumberValue\': \'string\',
                                    \'DatetimeValue\': datetime(2015, 1, 1)
                                }
                            },
                        ],
                        \'ObjectIdentifier\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **IndexAttachments** *(list) --* 
        
              The indices attached to the specified object.
        
              - *(dict) --* 
        
                Represents an index and an attached object.
        
                - **IndexedAttributes** *(list) --* 
        
                  The indexed attribute values.
        
                  - *(dict) --* 
        
                    The combination of an attribute key and an attribute value.
        
                    - **Key** *(dict) --* 
        
                      The key of the attribute.
        
                      - **SchemaArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                      - **FacetName** *(string) --* 
        
                        The name of the facet that the attribute exists within.
        
                      - **Name** *(string) --* 
        
                        The name of the attribute.
        
                    - **Value** *(dict) --* 
        
                      The value of the attribute.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
                - **ObjectIdentifier** *(string) --* 
        
                  In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to the object. This field will always contain the ``ObjectIdentifier`` of the object on the opposite side of the attachment specified in the query.
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_development_schema_arns(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListDevelopmentSchemaArns>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_development_schema_arns(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArns** *(list) --* 
        
              The ARNs of retrieved development schemas.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_directories(self, NextToken: str = None, MaxResults: int = None, state: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListDirectories>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_directories(
              NextToken=\'string\',
              MaxResults=123,
              state=\'ENABLED\'|\'DISABLED\'|\'DELETED\'
          )
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :type state: string
        :param state: 
        
          The state of the directories in the list. Can be either Enabled, Disabled, or Deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Directories\': [
                    {
                        \'Name\': \'string\',
                        \'DirectoryArn\': \'string\',
                        \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                        \'CreationDateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Directories** *(list) --* 
        
              Lists all directories that are associated with your account in pagination fashion.
        
              - *(dict) --* 
        
                Directory structure that includes the directory name and directory ARN.
        
                - **Name** *(string) --* 
        
                  The name of the directory.
        
                - **DirectoryArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that is associated with the directory. For more information, see  arns .
        
                - **State** *(string) --* 
        
                  The state of the directory. Can be either ``Enabled`` , ``Disabled`` , or ``Deleted`` .
        
                - **CreationDateTime** *(datetime) --* 
        
                  The date and time when the directory was created.
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_facet_attributes(self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListFacetAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_facet_attributes(
              SchemaArn=\'string\',
              Name=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The ARN of the schema where the facet resides.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the facet whose attributes will be retrieved.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Name\': \'string\',
                        \'AttributeDefinition\': {
                            \'Type\': \'STRING\'|\'BINARY\'|\'BOOLEAN\'|\'NUMBER\'|\'DATETIME\'|\'VARIANT\',
                            \'DefaultValue\': {
                                \'StringValue\': \'string\',
                                \'BinaryValue\': b\'bytes\',
                                \'BooleanValue\': True|False,
                                \'NumberValue\': \'string\',
                                \'DatetimeValue\': datetime(2015, 1, 1)
                            },
                            \'IsImmutable\': True|False,
                            \'Rules\': {
                                \'string\': {
                                    \'Type\': \'BINARY_LENGTH\'|\'NUMBER_COMPARISON\'|\'STRING_FROM_SET\'|\'STRING_LENGTH\',
                                    \'Parameters\': {
                                        \'string\': \'string\'
                                    }
                                }
                            }
                        },
                        \'AttributeReference\': {
                            \'TargetFacetName\': \'string\',
                            \'TargetAttributeName\': \'string\'
                        },
                        \'RequiredBehavior\': \'REQUIRED_ALWAYS\'|\'NOT_REQUIRED\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              The attributes attached to the facet.
        
              - *(dict) --* 
        
                An attribute that is associated with the  Facet .
        
                - **Name** *(string) --* 
        
                  The name of the facet attribute.
        
                - **AttributeDefinition** *(dict) --* 
        
                  A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
                  - **Type** *(string) --* 
        
                    The type of the attribute.
        
                  - **DefaultValue** *(dict) --* 
        
                    The default value of the attribute (if configured).
        
                    - **StringValue** *(string) --* 
        
                      A string data value.
        
                    - **BinaryValue** *(bytes) --* 
        
                      A binary data value.
        
                    - **BooleanValue** *(boolean) --* 
        
                      A Boolean data value.
        
                    - **NumberValue** *(string) --* 
        
                      A number data value.
        
                    - **DatetimeValue** *(datetime) --* 
        
                      A date and time value.
        
                  - **IsImmutable** *(boolean) --* 
        
                    Whether the attribute is mutable or not.
        
                  - **Rules** *(dict) --* 
        
                    Validation rules attached to the attribute definition.
        
                    - *(string) --* 
                      
                      - *(dict) --* 
        
                        Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
        
                        - **Type** *(string) --* 
        
                          The type of attribute validation rule.
        
                        - **Parameters** *(dict) --* 
        
                          The minimum and maximum parameters that are associated with the rule.
        
                          - *(string) --* 
                            
                            - *(string) --* 
                      
                - **AttributeReference** *(dict) --* 
        
                  An attribute reference that is associated with the attribute. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
                  - **TargetFacetName** *(string) --* 
        
                    The target facet name that is associated with the facet reference. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
                  - **TargetAttributeName** *(string) --* 
        
                    The target attribute name that is associated with the facet reference. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
                - **RequiredBehavior** *(string) --* 
        
                  The required behavior of the ``FacetAttribute`` .
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_facet_names(self, SchemaArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListFacetNames>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_facet_names(
              SchemaArn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) to retrieve facet names from.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FacetNames\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FacetNames** *(list) --* 
        
              The names of facets that exist within the schema.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_incoming_typed_links(self, DirectoryArn: str, ObjectReference: Dict, FilterAttributeRanges: List = None, FilterTypedLink: Dict = None, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListIncomingTypedLinks>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_incoming_typed_links(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              FilterAttributeRanges=[
                  {
                      \'AttributeName\': \'string\',
                      \'Range\': {
                          \'StartMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                          \'StartValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          },
                          \'EndMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                          \'EndValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          }
                      }
                  },
              ],
              FilterTypedLink={
                  \'SchemaArn\': \'string\',
                  \'TypedLinkName\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123,
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          Reference that identifies the object whose attributes will be listed.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type FilterAttributeRanges: list
        :param FilterAttributeRanges: 
        
          Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
        
          - *(dict) --* 
        
            Identifies the range of attributes that are used by a specified filter.
        
            - **AttributeName** *(string) --* 
        
              The unique name of the typed link attribute.
        
            - **Range** *(dict) --* **[REQUIRED]** 
        
              The range of attribute values that are being selected.
        
              - **StartMode** *(string) --* **[REQUIRED]** 
        
                The inclusive or exclusive range start.
        
              - **StartValue** *(dict) --* 
        
                The value to start the range at.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
              - **EndMode** *(string) --* **[REQUIRED]** 
        
                The inclusive or exclusive range end.
        
              - **EndValue** *(dict) --* 
        
                The attribute value to terminate the range at.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
        :type FilterTypedLink: dict
        :param FilterTypedLink: 
        
          Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.
        
          - **SchemaArn** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
          - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
            The unique name of the typed link facet.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level to execute the request at.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LinkSpecifiers\': [
                    {
                        \'TypedLinkFacet\': {
                            \'SchemaArn\': \'string\',
                            \'TypedLinkName\': \'string\'
                        },
                        \'SourceObjectReference\': {
                            \'Selector\': \'string\'
                        },
                        \'TargetObjectReference\': {
                            \'Selector\': \'string\'
                        },
                        \'IdentityAttributeValues\': [
                            {
                                \'AttributeName\': \'string\',
                                \'Value\': {
                                    \'StringValue\': \'string\',
                                    \'BinaryValue\': b\'bytes\',
                                    \'BooleanValue\': True|False,
                                    \'NumberValue\': \'string\',
                                    \'DatetimeValue\': datetime(2015, 1, 1)
                                }
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **LinkSpecifiers** *(list) --* 
        
              Returns one or more typed link specifiers as output.
        
              - *(dict) --* 
        
                Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.
        
                - **TypedLinkFacet** *(dict) --* 
        
                  Identifies the typed link facet that is associated with the typed link.
        
                  - **SchemaArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                  - **TypedLinkName** *(string) --* 
        
                    The unique name of the typed link facet.
        
                - **SourceObjectReference** *(dict) --* 
        
                  Identifies the source object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **TargetObjectReference** *(dict) --* 
        
                  Identifies the target object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **IdentityAttributeValues** *(list) --* 
        
                  Identifies the attribute value to update.
        
                  - *(dict) --* 
        
                    Identifies the attribute name and value for a typed link.
        
                    - **AttributeName** *(string) --* 
        
                      The attribute name of the typed link.
        
                    - **Value** *(dict) --* 
        
                      The value for the typed link.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_index(self, DirectoryArn: str, IndexReference: Dict, RangesOnIndexedValues: List = None, MaxResults: int = None, NextToken: str = None, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListIndex>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_index(
              DirectoryArn=\'string\',
              RangesOnIndexedValues=[
                  {
                      \'AttributeKey\': {
                          \'SchemaArn\': \'string\',
                          \'FacetName\': \'string\',
                          \'Name\': \'string\'
                      },
                      \'Range\': {
                          \'StartMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                          \'StartValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          },
                          \'EndMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                          \'EndValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          }
                      }
                  },
              ],
              IndexReference={
                  \'Selector\': \'string\'
              },
              MaxResults=123,
              NextToken=\'string\',
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory that the index exists in.
        
        :type RangesOnIndexedValues: list
        :param RangesOnIndexedValues: 
        
          Specifies the ranges of indexed values that you want to query.
        
          - *(dict) --* 
        
            A range of attributes.
        
            - **AttributeKey** *(dict) --* 
        
              The key of the attribute that the attribute range covers.
        
              - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
              - **FacetName** *(string) --* **[REQUIRED]** 
        
                The name of the facet that the attribute exists within.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                The name of the attribute.
        
            - **Range** *(dict) --* 
        
              The range of attribute values being selected.
        
              - **StartMode** *(string) --* **[REQUIRED]** 
        
                The inclusive or exclusive range start.
        
              - **StartValue** *(dict) --* 
        
                The value to start the range at.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
              - **EndMode** *(string) --* **[REQUIRED]** 
        
                The inclusive or exclusive range end.
        
              - **EndValue** *(dict) --* 
        
                The attribute value to terminate the range at.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
        :type IndexReference: dict
        :param IndexReference: **[REQUIRED]** 
        
          The reference to the index to list.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of objects in a single page to retrieve from the index during a request. For more information, see `Amazon Cloud Directory Limits <http://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html>`__ .
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level to execute the request at.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IndexAttachments\': [
                    {
                        \'IndexedAttributes\': [
                            {
                                \'Key\': {
                                    \'SchemaArn\': \'string\',
                                    \'FacetName\': \'string\',
                                    \'Name\': \'string\'
                                },
                                \'Value\': {
                                    \'StringValue\': \'string\',
                                    \'BinaryValue\': b\'bytes\',
                                    \'BooleanValue\': True|False,
                                    \'NumberValue\': \'string\',
                                    \'DatetimeValue\': datetime(2015, 1, 1)
                                }
                            },
                        ],
                        \'ObjectIdentifier\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **IndexAttachments** *(list) --* 
        
              The objects and indexed values attached to the index.
        
              - *(dict) --* 
        
                Represents an index and an attached object.
        
                - **IndexedAttributes** *(list) --* 
        
                  The indexed attribute values.
        
                  - *(dict) --* 
        
                    The combination of an attribute key and an attribute value.
        
                    - **Key** *(dict) --* 
        
                      The key of the attribute.
        
                      - **SchemaArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                      - **FacetName** *(string) --* 
        
                        The name of the facet that the attribute exists within.
        
                      - **Name** *(string) --* 
        
                        The name of the attribute.
        
                    - **Value** *(dict) --* 
        
                      The value of the attribute.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
                - **ObjectIdentifier** *(string) --* 
        
                  In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to the object. This field will always contain the ``ObjectIdentifier`` of the object on the opposite side of the attachment specified in the query.
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_managed_schema_arns(self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListManagedSchemaArns>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_managed_schema_arns(
              SchemaArn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type SchemaArn: string
        :param SchemaArn: 
        
          The response for ListManagedSchemaArns. When this parameter is used, all minor version ARNs for a major version are listed.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArns** *(list) --* 
        
              The ARNs for all AWS managed schemas.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_object_attributes(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None, FacetFilter: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_object_attributes(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123,
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\',
              FacetFilter={
                  \'SchemaArn\': \'string\',
                  \'FacetName\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides. For more information, see  arns .
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          The reference that identifies the object whose attributes will be listed.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to be retrieved in a single call. This is an approximate number.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
        
        :type FacetFilter: dict
        :param FacetFilter: 
        
          Used to filter the list of object attributes that are associated with a certain facet.
        
          - **SchemaArn** *(string) --* 
        
            The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
          - **FacetName** *(string) --* 
        
            The name of the facet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Key\': {
                            \'SchemaArn\': \'string\',
                            \'FacetName\': \'string\',
                            \'Name\': \'string\'
                        },
                        \'Value\': {
                            \'StringValue\': \'string\',
                            \'BinaryValue\': b\'bytes\',
                            \'BooleanValue\': True|False,
                            \'NumberValue\': \'string\',
                            \'DatetimeValue\': datetime(2015, 1, 1)
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              Attributes map that is associated with the object. ``AttributeArn`` is the key, and attribute value is the value.
        
              - *(dict) --* 
        
                The combination of an attribute key and an attribute value.
        
                - **Key** *(dict) --* 
        
                  The key of the attribute.
        
                  - **SchemaArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
                  - **FacetName** *(string) --* 
        
                    The name of the facet that the attribute exists within.
        
                  - **Name** *(string) --* 
        
                    The name of the attribute.
        
                - **Value** *(dict) --* 
        
                  The value of the attribute.
        
                  - **StringValue** *(string) --* 
        
                    A string data value.
        
                  - **BinaryValue** *(bytes) --* 
        
                    A binary data value.
        
                  - **BooleanValue** *(boolean) --* 
        
                    A Boolean data value.
        
                  - **NumberValue** *(string) --* 
        
                    A number data value.
        
                  - **DatetimeValue** *(datetime) --* 
        
                    A date and time value.
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_object_children(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectChildren>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_object_children(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123,
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides. For more information, see  arns .
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          The reference that identifies the object for which child objects are being listed.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to be retrieved in a single call. This is an approximate number.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Children\': {
                    \'string\': \'string\'
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Children** *(dict) --* 
        
              Children structure, which is a map with key as the ``LinkName`` and ``ObjectIdentifier`` as the value.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_object_parent_paths(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        Use this API to evaluate all parents for an object. The call returns all objects from the root of the directory up to the requested object. The API returns the number of paths based on user-defined ``MaxResults`` , in case there are multiple paths to the parent. The order of the paths and nodes returned is consistent among multiple API calls unless the objects are deleted or moved. Paths not leading to the directory root are ignored from the target object.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectParentPaths>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_object_parent_paths(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory to which the parent path applies.
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          The reference that identifies the object whose parent paths are listed.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to be retrieved in a single call. This is an approximate number.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PathToObjectIdentifiersList\': [
                    {
                        \'Path\': \'string\',
                        \'ObjectIdentifiers\': [
                            \'string\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PathToObjectIdentifiersList** *(list) --* 
        
              Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.
        
              - *(dict) --* 
        
                Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.
        
                - **Path** *(string) --* 
        
                  The path that is used to identify the object starting from directory root.
        
                - **ObjectIdentifiers** *(list) --* 
        
                  Lists ``ObjectIdentifiers`` starting from directory root to the object in the request.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_object_parents(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None, IncludeAllLinksToEachParent: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectParents>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_object_parents(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123,
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\',
              IncludeAllLinksToEachParent=True|False
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides. For more information, see  arns .
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          The reference that identifies the object for which parent objects are being listed.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to be retrieved in a single call. This is an approximate number.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
        
        :type IncludeAllLinksToEachParent: boolean
        :param IncludeAllLinksToEachParent: 
        
          When set to True, returns all  ListObjectParentsResponse$ParentLinks . There could be multiple links between a parent-child pair.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parents\': {
                    \'string\': \'string\'
                },
                \'NextToken\': \'string\',
                \'ParentLinks\': [
                    {
                        \'ObjectIdentifier\': \'string\',
                        \'LinkName\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Parents** *(dict) --* 
        
              The parent structure, which is a map with key as the ``ObjectIdentifier`` and LinkName as the value.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
            - **ParentLinks** *(list) --* 
        
              Returns a list of parent reference and LinkName Tuples.
        
              - *(dict) --* 
        
                A pair of ObjectIdentifier and LinkName.
        
                - **ObjectIdentifier** *(string) --* 
        
                  The ID that is associated with the object.
        
                - **LinkName** *(string) --* 
        
                  The name of the link between the parent and the child object.
        
        """
        pass

    def list_object_policies(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectPolicies>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_object_policies(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123,
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where objects reside. For more information, see  arns .
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          Reference that identifies the object for which policies will be listed.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to be retrieved in a single call. This is an approximate number.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttachedPolicyIds\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AttachedPolicyIds** *(list) --* 
        
              A list of policy ``ObjectIdentifiers`` , that are attached to the object.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_outgoing_typed_links(self, DirectoryArn: str, ObjectReference: Dict, FilterAttributeRanges: List = None, FilterTypedLink: Dict = None, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListOutgoingTypedLinks>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_outgoing_typed_links(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              FilterAttributeRanges=[
                  {
                      \'AttributeName\': \'string\',
                      \'Range\': {
                          \'StartMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                          \'StartValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          },
                          \'EndMode\': \'FIRST\'|\'LAST\'|\'LAST_BEFORE_MISSING_VALUES\'|\'INCLUSIVE\'|\'EXCLUSIVE\',
                          \'EndValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          }
                      }
                  },
              ],
              FilterTypedLink={
                  \'SchemaArn\': \'string\',
                  \'TypedLinkName\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123,
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          A reference that identifies the object whose attributes will be listed.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type FilterAttributeRanges: list
        :param FilterAttributeRanges: 
        
          Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
        
          - *(dict) --* 
        
            Identifies the range of attributes that are used by a specified filter.
        
            - **AttributeName** *(string) --* 
        
              The unique name of the typed link attribute.
        
            - **Range** *(dict) --* **[REQUIRED]** 
        
              The range of attribute values that are being selected.
        
              - **StartMode** *(string) --* **[REQUIRED]** 
        
                The inclusive or exclusive range start.
        
              - **StartValue** *(dict) --* 
        
                The value to start the range at.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
              - **EndMode** *(string) --* **[REQUIRED]** 
        
                The inclusive or exclusive range end.
        
              - **EndValue** *(dict) --* 
        
                The attribute value to terminate the range at.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
        :type FilterTypedLink: dict
        :param FilterTypedLink: 
        
          Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.
        
          - **SchemaArn** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
          - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
            The unique name of the typed link facet.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level to execute the request at.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TypedLinkSpecifiers\': [
                    {
                        \'TypedLinkFacet\': {
                            \'SchemaArn\': \'string\',
                            \'TypedLinkName\': \'string\'
                        },
                        \'SourceObjectReference\': {
                            \'Selector\': \'string\'
                        },
                        \'TargetObjectReference\': {
                            \'Selector\': \'string\'
                        },
                        \'IdentityAttributeValues\': [
                            {
                                \'AttributeName\': \'string\',
                                \'Value\': {
                                    \'StringValue\': \'string\',
                                    \'BinaryValue\': b\'bytes\',
                                    \'BooleanValue\': True|False,
                                    \'NumberValue\': \'string\',
                                    \'DatetimeValue\': datetime(2015, 1, 1)
                                }
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TypedLinkSpecifiers** *(list) --* 
        
              Returns a typed link specifier as output.
        
              - *(dict) --* 
        
                Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.
        
                - **TypedLinkFacet** *(dict) --* 
        
                  Identifies the typed link facet that is associated with the typed link.
        
                  - **SchemaArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
                  - **TypedLinkName** *(string) --* 
        
                    The unique name of the typed link facet.
        
                - **SourceObjectReference** *(dict) --* 
        
                  Identifies the source object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **TargetObjectReference** *(dict) --* 
        
                  Identifies the target object that the typed link will attach to.
        
                  - **Selector** *(string) --* 
        
                    A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
                     
                    * */some/path* - Identifies the object based on path 
                     
                    * *#SomeBatchReference* - Identifies the object in a batch call 
                     
                - **IdentityAttributeValues** *(list) --* 
        
                  Identifies the attribute value to update.
        
                  - *(dict) --* 
        
                    Identifies the attribute name and value for a typed link.
        
                    - **AttributeName** *(string) --* 
        
                      The attribute name of the typed link.
        
                    - **Value** *(dict) --* 
        
                      The value for the typed link.
        
                      - **StringValue** *(string) --* 
        
                        A string data value.
        
                      - **BinaryValue** *(bytes) --* 
        
                        A binary data value.
        
                      - **BooleanValue** *(boolean) --* 
        
                        A Boolean data value.
        
                      - **NumberValue** *(string) --* 
        
                        A number data value.
        
                      - **DatetimeValue** *(datetime) --* 
        
                        A date and time value.
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_policy_attachments(self, DirectoryArn: str, PolicyReference: Dict, NextToken: str = None, MaxResults: int = None, ConsistencyLevel: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListPolicyAttachments>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_policy_attachments(
              DirectoryArn=\'string\',
              PolicyReference={
                  \'Selector\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123,
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\'
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where objects reside. For more information, see  arns .
        
        :type PolicyReference: dict
        :param PolicyReference: **[REQUIRED]** 
        
          The reference that identifies the policy object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to be retrieved in a single call. This is an approximate number.
        
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ObjectIdentifiers\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ObjectIdentifiers** *(list) --* 
        
              A list of ``ObjectIdentifiers`` to which the policy is attached.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_published_schema_arns(self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListPublishedSchemaArns>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_published_schema_arns(
              SchemaArn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type SchemaArn: string
        :param SchemaArn: 
        
          The response for ``ListPublishedSchemaArns`` when this parameter is used will list all minor version ARNs for a major version.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArns** *(list) --* 
        
              The ARNs of published schemas.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              ResourceArn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token. This is for future use. Currently pagination is not supported for tagging.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The ``MaxResults`` parameter sets the maximum number of results returned in a single page. This is for future use and is not supported currently.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              A list of tag key value pairs that are associated with the response.
        
              - *(dict) --* 
        
                The tag structure that contains a tag key and value.
        
                - **Key** *(string) --* 
        
                  The key that is associated with the tag.
        
                - **Value** *(string) --* 
        
                  The value that is associated with the tag.
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results. This value is null when there are no more results to return.
        
        """
        pass

    def list_typed_link_facet_attributes(self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_typed_link_facet_attributes(
              SchemaArn=\'string\',
              Name=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The unique name of the typed link facet.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'STRING\'|\'BINARY\'|\'BOOLEAN\'|\'NUMBER\'|\'DATETIME\'|\'VARIANT\',
                        \'DefaultValue\': {
                            \'StringValue\': \'string\',
                            \'BinaryValue\': b\'bytes\',
                            \'BooleanValue\': True|False,
                            \'NumberValue\': \'string\',
                            \'DatetimeValue\': datetime(2015, 1, 1)
                        },
                        \'IsImmutable\': True|False,
                        \'Rules\': {
                            \'string\': {
                                \'Type\': \'BINARY_LENGTH\'|\'NUMBER_COMPARISON\'|\'STRING_FROM_SET\'|\'STRING_LENGTH\',
                                \'Parameters\': {
                                    \'string\': \'string\'
                                }
                            }
                        },
                        \'RequiredBehavior\': \'REQUIRED_ALWAYS\'|\'NOT_REQUIRED\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              An ordered set of attributes associate with the typed link.
        
              - *(dict) --* 
        
                A typed link attribute definition.
        
                - **Name** *(string) --* 
        
                  The unique name of the typed link attribute.
        
                - **Type** *(string) --* 
        
                  The type of the attribute.
        
                - **DefaultValue** *(dict) --* 
        
                  The default value of the attribute (if configured).
        
                  - **StringValue** *(string) --* 
        
                    A string data value.
        
                  - **BinaryValue** *(bytes) --* 
        
                    A binary data value.
        
                  - **BooleanValue** *(boolean) --* 
        
                    A Boolean data value.
        
                  - **NumberValue** *(string) --* 
        
                    A number data value.
        
                  - **DatetimeValue** *(datetime) --* 
        
                    A date and time value.
        
                - **IsImmutable** *(boolean) --* 
        
                  Whether the attribute is mutable or not.
        
                - **Rules** *(dict) --* 
        
                  Validation rules that are attached to the attribute definition.
        
                  - *(string) --* 
                    
                    - *(dict) --* 
        
                      Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
        
                      - **Type** *(string) --* 
        
                        The type of attribute validation rule.
        
                      - **Parameters** *(dict) --* 
        
                        The minimum and maximum parameters that are associated with the rule.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                - **RequiredBehavior** *(string) --* 
        
                  The required behavior of the ``TypedLinkAttributeDefinition`` .
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def list_typed_link_facet_names(self, SchemaArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTypedLinkFacetNames>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_typed_link_facet_names(
              SchemaArn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FacetNames\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FacetNames** *(list) --* 
        
              The names of typed link facets that exist within the schema.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def lookup_policy(self, DirectoryArn: str, ObjectReference: Dict, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/LookupPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.lookup_policy(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              NextToken=\'string\',
              MaxResults=123
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory . For more information, see  arns .
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          Reference that identifies the object whose policies will be looked up.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to be retrieved in a single call. This is an approximate number.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PolicyToPathList\': [
                    {
                        \'Path\': \'string\',
                        \'Policies\': [
                            {
                                \'PolicyId\': \'string\',
                                \'ObjectIdentifier\': \'string\',
                                \'PolicyType\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PolicyToPathList** *(list) --* 
        
              Provides list of path to policies. Policies contain ``PolicyId`` , ``ObjectIdentifier`` , and ``PolicyType`` . For more information, see `Policies <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__ .
        
              - *(dict) --* 
        
                Used when a regular object exists in a  Directory and you want to find all of the policies that are associated with that object and the parent to that object.
        
                - **Path** *(string) --* 
        
                  The path that is referenced from the root.
        
                - **Policies** *(list) --* 
        
                  List of policy objects.
        
                  - *(dict) --* 
        
                    Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to which it is attached. For more information, see `Policies <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__ .
        
                    - **PolicyId** *(string) --* 
        
                      The ID of ``PolicyAttachment`` .
        
                    - **ObjectIdentifier** *(string) --* 
        
                      The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .
        
                    - **PolicyType** *(string) --* 
        
                      The type of policy that can be associated with ``PolicyAttachment`` .
        
            - **NextToken** *(string) --* 
        
              The pagination token.
        
        """
        pass

    def publish_schema(self, DevelopmentSchemaArn: str, Version: str, MinorVersion: str = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/PublishSchema>`_
        
        **Request Syntax** 
        ::
        
          response = client.publish_schema(
              DevelopmentSchemaArn=\'string\',
              Version=\'string\',
              MinorVersion=\'string\',
              Name=\'string\'
          )
        :type DevelopmentSchemaArn: string
        :param DevelopmentSchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see  arns .
        
        :type Version: string
        :param Version: **[REQUIRED]** 
        
          The major version under which the schema will be published. Schemas have both a major and minor version associated with them.
        
        :type MinorVersion: string
        :param MinorVersion: 
        
          The minor version under which the schema will be published. This parameter is recommended. Schemas have both a major and minor version associated with them.
        
        :type Name: string
        :param Name: 
        
          The new name under which the schema will be published. If this is not provided, the development schema is considered.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PublishedSchemaArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PublishedSchemaArn** *(string) --* 
        
              The ARN that is associated with the published schema. For more information, see  arns .
        
        """
        pass

    def put_schema_from_json(self, SchemaArn: str, Document: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/PutSchemaFromJson>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_schema_from_json(
              SchemaArn=\'string\',
              Document=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The ARN of the schema to update.
        
        :type Document: string
        :param Document: **[REQUIRED]** 
        
          The replacement JSON schema.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* 
        
              The ARN of the schema to update.
        
        """
        pass

    def remove_facet_from_object(self, DirectoryArn: str, SchemaFacet: Dict, ObjectReference: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/RemoveFacetFromObject>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_facet_from_object(
              DirectoryArn=\'string\',
              SchemaFacet={
                  \'SchemaArn\': \'string\',
                  \'FacetName\': \'string\'
              },
              ObjectReference={
                  \'Selector\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory in which the object resides.
        
        :type SchemaFacet: dict
        :param SchemaFacet: **[REQUIRED]** 
        
          The facet to remove. See  SchemaFacet for details.
        
          - **SchemaArn** *(string) --* 
        
            The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place Schema Upgrade <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__ for a description of when to provide minor versions.
        
          - **FacetName** *(string) --* 
        
            The name of the facet.
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          A reference to the object to remove the facet from.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              ResourceArn=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          A list of tag key-value pairs.
        
          - *(dict) --* 
        
            The tag structure that contains a tag key and value.
        
            - **Key** *(string) --* 
        
              The key that is associated with the tag.
        
            - **Value** *(string) --* 
        
              The value that is associated with the tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              ResourceArn=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          Keys of the tag that need to be removed from the resource.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_facet(self, SchemaArn: str, Name: str, AttributeUpdates: List = None, ObjectType: str = None) -> Dict:
        """
        Does the following:
        
        * Adds new ``Attributes`` , ``Rules`` , or ``ObjectTypes`` . 
         
        * Updates existing ``Attributes`` , ``Rules`` , or ``ObjectTypes`` . 
         
        * Deletes existing ``Attributes`` , ``Rules`` , or ``ObjectTypes`` . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/UpdateFacet>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_facet(
              SchemaArn=\'string\',
              Name=\'string\',
              AttributeUpdates=[
                  {
                      \'Attribute\': {
                          \'Name\': \'string\',
                          \'AttributeDefinition\': {
                              \'Type\': \'STRING\'|\'BINARY\'|\'BOOLEAN\'|\'NUMBER\'|\'DATETIME\'|\'VARIANT\',
                              \'DefaultValue\': {
                                  \'StringValue\': \'string\',
                                  \'BinaryValue\': b\'bytes\',
                                  \'BooleanValue\': True|False,
                                  \'NumberValue\': \'string\',
                                  \'DatetimeValue\': datetime(2015, 1, 1)
                              },
                              \'IsImmutable\': True|False,
                              \'Rules\': {
                                  \'string\': {
                                      \'Type\': \'BINARY_LENGTH\'|\'NUMBER_COMPARISON\'|\'STRING_FROM_SET\'|\'STRING_LENGTH\',
                                      \'Parameters\': {
                                          \'string\': \'string\'
                                      }
                                  }
                              }
                          },
                          \'AttributeReference\': {
                              \'TargetFacetName\': \'string\',
                              \'TargetAttributeName\': \'string\'
                          },
                          \'RequiredBehavior\': \'REQUIRED_ALWAYS\'|\'NOT_REQUIRED\'
                      },
                      \'Action\': \'CREATE_OR_UPDATE\'|\'DELETE\'
                  },
              ],
              ObjectType=\'NODE\'|\'LEAF_NODE\'|\'POLICY\'|\'INDEX\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Facet . For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the facet.
        
        :type AttributeUpdates: list
        :param AttributeUpdates: 
        
          List of attributes that need to be updated in a given schema  Facet . Each attribute is followed by ``AttributeAction`` , which specifies the type of update operation to perform. 
        
          - *(dict) --* 
        
            A structure that contains information used to update an attribute.
        
            - **Attribute** *(dict) --* 
        
              The attribute to update.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                The name of the facet attribute.
        
              - **AttributeDefinition** *(dict) --* 
        
                A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of the attribute.
        
                - **DefaultValue** *(dict) --* 
        
                  The default value of the attribute (if configured).
        
                  - **StringValue** *(string) --* 
        
                    A string data value.
        
                  - **BinaryValue** *(bytes) --* 
        
                    A binary data value.
        
                  - **BooleanValue** *(boolean) --* 
        
                    A Boolean data value.
        
                  - **NumberValue** *(string) --* 
        
                    A number data value.
        
                  - **DatetimeValue** *(datetime) --* 
        
                    A date and time value.
        
                - **IsImmutable** *(boolean) --* 
        
                  Whether the attribute is mutable or not.
        
                - **Rules** *(dict) --* 
        
                  Validation rules attached to the attribute definition.
        
                  - *(string) --* 
        
                    - *(dict) --* 
        
                      Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
        
                      - **Type** *(string) --* 
        
                        The type of attribute validation rule.
        
                      - **Parameters** *(dict) --* 
        
                        The minimum and maximum parameters that are associated with the rule.
        
                        - *(string) --* 
        
                          - *(string) --* 
        
              - **AttributeReference** *(dict) --* 
        
                An attribute reference that is associated with the attribute. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
                - **TargetFacetName** *(string) --* **[REQUIRED]** 
        
                  The target facet name that is associated with the facet reference. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
                - **TargetAttributeName** *(string) --* **[REQUIRED]** 
        
                  The target attribute name that is associated with the facet reference. See `Attribute References <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__ for more information.
        
              - **RequiredBehavior** *(string) --* 
        
                The required behavior of the ``FacetAttribute`` .
        
            - **Action** *(string) --* 
        
              The action to perform when updating the attribute.
        
        :type ObjectType: string
        :param ObjectType: 
        
          The object type that is associated with the facet. See  CreateFacetRequest$ObjectType for more details.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_link_attributes(self, DirectoryArn: str, TypedLinkSpecifier: Dict, AttributeUpdates: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/UpdateLinkAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_link_attributes(
              DirectoryArn=\'string\',
              TypedLinkSpecifier={
                  \'TypedLinkFacet\': {
                      \'SchemaArn\': \'string\',
                      \'TypedLinkName\': \'string\'
                  },
                  \'SourceObjectReference\': {
                      \'Selector\': \'string\'
                  },
                  \'TargetObjectReference\': {
                      \'Selector\': \'string\'
                  },
                  \'IdentityAttributeValues\': [
                      {
                          \'AttributeName\': \'string\',
                          \'Value\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          }
                      },
                  ]
              },
              AttributeUpdates=[
                  {
                      \'AttributeKey\': {
                          \'SchemaArn\': \'string\',
                          \'FacetName\': \'string\',
                          \'Name\': \'string\'
                      },
                      \'AttributeAction\': {
                          \'AttributeActionType\': \'CREATE_OR_UPDATE\'|\'DELETE\',
                          \'AttributeUpdateValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          }
                      }
                  },
              ]
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see  arns or `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
        :type TypedLinkSpecifier: dict
        :param TypedLinkSpecifier: **[REQUIRED]** 
        
          Allows a typed link specifier to be accepted as input.
        
          - **TypedLinkFacet** *(dict) --* **[REQUIRED]** 
        
            Identifies the typed link facet that is associated with the typed link.
        
            - **SchemaArn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
            - **TypedLinkName** *(string) --* **[REQUIRED]** 
        
              The unique name of the typed link facet.
        
          - **SourceObjectReference** *(dict) --* **[REQUIRED]** 
        
            Identifies the source object that the typed link will attach to.
        
            - **Selector** *(string) --* 
        
              A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
              * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
               
              * */some/path* - Identifies the object based on path 
               
              * *#SomeBatchReference* - Identifies the object in a batch call 
               
          - **TargetObjectReference** *(dict) --* **[REQUIRED]** 
        
            Identifies the target object that the typed link will attach to.
        
            - **Selector** *(string) --* 
        
              A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
              * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
               
              * */some/path* - Identifies the object based on path 
               
              * *#SomeBatchReference* - Identifies the object in a batch call 
               
          - **IdentityAttributeValues** *(list) --* **[REQUIRED]** 
        
            Identifies the attribute value to update.
        
            - *(dict) --* 
        
              Identifies the attribute name and value for a typed link.
        
              - **AttributeName** *(string) --* **[REQUIRED]** 
        
                The attribute name of the typed link.
        
              - **Value** *(dict) --* **[REQUIRED]** 
        
                The value for the typed link.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
        :type AttributeUpdates: list
        :param AttributeUpdates: **[REQUIRED]** 
        
          The attributes update structure.
        
          - *(dict) --* 
        
            Structure that contains attribute update information.
        
            - **AttributeKey** *(dict) --* 
        
              The key of the attribute being updated.
        
              - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
              - **FacetName** *(string) --* **[REQUIRED]** 
        
                The name of the facet that the attribute exists within.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                The name of the attribute.
        
            - **AttributeAction** *(dict) --* 
        
              The action to perform as part of the attribute update.
        
              - **AttributeActionType** *(string) --* 
        
                A type that can be either ``UPDATE_OR_CREATE`` or ``DELETE`` .
        
              - **AttributeUpdateValue** *(dict) --* 
        
                The value that you want to update to.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_object_attributes(self, DirectoryArn: str, ObjectReference: Dict, AttributeUpdates: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/UpdateObjectAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_object_attributes(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              AttributeUpdates=[
                  {
                      \'ObjectAttributeKey\': {
                          \'SchemaArn\': \'string\',
                          \'FacetName\': \'string\',
                          \'Name\': \'string\'
                      },
                      \'ObjectAttributeAction\': {
                          \'ObjectAttributeActionType\': \'CREATE_OR_UPDATE\'|\'DELETE\',
                          \'ObjectAttributeUpdateValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          }
                      }
                  },
              ]
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides. For more information, see  arns .
        
        :type ObjectReference: dict
        :param ObjectReference: **[REQUIRED]** 
        
          The reference that identifies the object.
        
          - **Selector** *(string) --* 
        
            A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see `Access Objects <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__ . You can identify an object in one of the following ways:
        
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier 
             
            * */some/path* - Identifies the object based on path 
             
            * *#SomeBatchReference* - Identifies the object in a batch call 
             
        :type AttributeUpdates: list
        :param AttributeUpdates: **[REQUIRED]** 
        
          The attributes update structure.
        
          - *(dict) --* 
        
            Structure that contains attribute update information.
        
            - **ObjectAttributeKey** *(dict) --* 
        
              The key of the attribute being updated.
        
              - **SchemaArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
        
              - **FacetName** *(string) --* **[REQUIRED]** 
        
                The name of the facet that the attribute exists within.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                The name of the attribute.
        
            - **ObjectAttributeAction** *(dict) --* 
        
              The action to perform as part of the attribute update.
        
              - **ObjectAttributeActionType** *(string) --* 
        
                A type that can be either ``Update`` or ``Delete`` .
        
              - **ObjectAttributeUpdateValue** *(dict) --* 
        
                The value that you want to update to.
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ObjectIdentifier\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ObjectIdentifier** *(string) --* 
        
              The ``ObjectIdentifier`` of the updated object.
        
        """
        pass

    def update_schema(self, SchemaArn: str, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/UpdateSchema>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_schema(
              SchemaArn=\'string\',
              Name=\'string\'
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the development schema. For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the schema.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArn** *(string) --* 
        
              The ARN that is associated with the updated schema. For more information, see  arns .
        
        """
        pass

    def update_typed_link_facet(self, SchemaArn: str, Name: str, AttributeUpdates: List, IdentityAttributeOrder: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/UpdateTypedLinkFacet>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_typed_link_facet(
              SchemaArn=\'string\',
              Name=\'string\',
              AttributeUpdates=[
                  {
                      \'Attribute\': {
                          \'Name\': \'string\',
                          \'Type\': \'STRING\'|\'BINARY\'|\'BOOLEAN\'|\'NUMBER\'|\'DATETIME\'|\'VARIANT\',
                          \'DefaultValue\': {
                              \'StringValue\': \'string\',
                              \'BinaryValue\': b\'bytes\',
                              \'BooleanValue\': True|False,
                              \'NumberValue\': \'string\',
                              \'DatetimeValue\': datetime(2015, 1, 1)
                          },
                          \'IsImmutable\': True|False,
                          \'Rules\': {
                              \'string\': {
                                  \'Type\': \'BINARY_LENGTH\'|\'NUMBER_COMPARISON\'|\'STRING_FROM_SET\'|\'STRING_LENGTH\',
                                  \'Parameters\': {
                                      \'string\': \'string\'
                                  }
                              }
                          },
                          \'RequiredBehavior\': \'REQUIRED_ALWAYS\'|\'NOT_REQUIRED\'
                      },
                      \'Action\': \'CREATE_OR_UPDATE\'|\'DELETE\'
                  },
              ],
              IdentityAttributeOrder=[
                  \'string\',
              ]
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The unique name of the typed link facet.
        
        :type AttributeUpdates: list
        :param AttributeUpdates: **[REQUIRED]** 
        
          Attributes update structure.
        
          - *(dict) --* 
        
            A typed link facet attribute update.
        
            - **Attribute** *(dict) --* **[REQUIRED]** 
        
              The attribute to update.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                The unique name of the typed link attribute.
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                The type of the attribute.
        
              - **DefaultValue** *(dict) --* 
        
                The default value of the attribute (if configured).
        
                - **StringValue** *(string) --* 
        
                  A string data value.
        
                - **BinaryValue** *(bytes) --* 
        
                  A binary data value.
        
                - **BooleanValue** *(boolean) --* 
        
                  A Boolean data value.
        
                - **NumberValue** *(string) --* 
        
                  A number data value.
        
                - **DatetimeValue** *(datetime) --* 
        
                  A date and time value.
        
              - **IsImmutable** *(boolean) --* 
        
                Whether the attribute is mutable or not.
        
              - **Rules** *(dict) --* 
        
                Validation rules that are attached to the attribute definition.
        
                - *(string) --* 
        
                  - *(dict) --* 
        
                    Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.
        
                    - **Type** *(string) --* 
        
                      The type of attribute validation rule.
        
                    - **Parameters** *(dict) --* 
        
                      The minimum and maximum parameters that are associated with the rule.
        
                      - *(string) --* 
        
                        - *(string) --* 
        
              - **RequiredBehavior** *(string) --* **[REQUIRED]** 
        
                The required behavior of the ``TypedLinkAttributeDefinition`` .
        
            - **Action** *(string) --* **[REQUIRED]** 
        
              The action to perform when updating the attribute.
        
        :type IdentityAttributeOrder: list
        :param IdentityAttributeOrder: **[REQUIRED]** 
        
          The order of identity attributes for the facet, from most significant to least significant. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to a typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls. For more information about identity attributes, see `Typed Links <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__ .
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def upgrade_applied_schema(self, PublishedSchemaArn: str, DirectoryArn: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/UpgradeAppliedSchema>`_
        
        **Request Syntax** 
        ::
        
          response = client.upgrade_applied_schema(
              PublishedSchemaArn=\'string\',
              DirectoryArn=\'string\',
              DryRun=True|False
          )
        :type PublishedSchemaArn: string
        :param PublishedSchemaArn: **[REQUIRED]** 
        
          The revision of the published schema to upgrade the directory to.
        
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN for the directory to which the upgraded schema will be applied.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Used for testing whether the major version schemas are backward compatible or not. If schema compatibility fails, an exception would be thrown else the call would succeed but no changes will be saved. This parameter is optional.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UpgradedSchemaArn\': \'string\',
                \'DirectoryArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UpgradedSchemaArn** *(string) --* 
        
              The ARN of the upgraded schema that is returned as part of the response.
        
            - **DirectoryArn** *(string) --* 
        
              The ARN of the directory that is returned as part of the response.
        
        """
        pass

    def upgrade_published_schema(self, DevelopmentSchemaArn: str, PublishedSchemaArn: str, MinorVersion: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/UpgradePublishedSchema>`_
        
        **Request Syntax** 
        ::
        
          response = client.upgrade_published_schema(
              DevelopmentSchemaArn=\'string\',
              PublishedSchemaArn=\'string\',
              MinorVersion=\'string\',
              DryRun=True|False
          )
        :type DevelopmentSchemaArn: string
        :param DevelopmentSchemaArn: **[REQUIRED]** 
        
          The ARN of the development schema with the changes used for the upgrade.
        
        :type PublishedSchemaArn: string
        :param PublishedSchemaArn: **[REQUIRED]** 
        
          The ARN of the published schema to be upgraded.
        
        :type MinorVersion: string
        :param MinorVersion: **[REQUIRED]** 
        
          Identifies the minor version of the published schema that will be created. This parameter is NOT optional.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Used for testing whether the Development schema provided is backwards compatible, or not, with the publish schema provided by the user to be upgraded. If schema compatibility fails, an exception would be thrown else the call would succeed. This parameter is optional and defaults to false.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UpgradedSchemaArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UpgradedSchemaArn** *(string) --* 
        
              The ARN of the upgraded schema that is returned as part of the response.
        
        """
        pass
