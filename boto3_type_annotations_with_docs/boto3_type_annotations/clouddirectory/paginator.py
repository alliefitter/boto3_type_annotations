from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAppliedSchemaArns(Paginator):
    def paginate(self, DirectoryArn: str, SchemaArn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListAppliedSchemaArns>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryArn=\'string\',
              SchemaArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DirectoryArn: string
        :param DirectoryArn: **[REQUIRED]** 
        
          The ARN of the directory you are listing.
        
        :type SchemaArn: string
        :param SchemaArn: 
        
          The response for ``ListAppliedSchemaArns`` when this parameter is used will list all minor version ARNs for a major version.
        
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
                \'SchemaArns\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArns** *(list) --* 
        
              The ARNs of schemas that are applied to the directory.
        
              - *(string) --* 
          
        """
        pass


class ListAttachedIndices(Paginator):
    def paginate(self, DirectoryArn: str, TargetReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListAttachedIndices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryArn=\'string\',
              TargetReference={
                  \'Selector\': \'string\'
              },
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
             
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level to use for this operation.
        
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
        
        """
        pass


class ListDevelopmentSchemaArns(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListDevelopmentSchemaArns>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'SchemaArns\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArns** *(list) --* 
        
              The ARNs of retrieved development schemas.
        
              - *(string) --* 
          
        """
        pass


class ListDirectories(Paginator):
    def paginate(self, state: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListDirectories>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              state=\'ENABLED\'|\'DISABLED\'|\'DELETED\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type state: string
        :param state: 
        
          The state of the directories in the list. Can be either Enabled, Disabled, or Deleted.
        
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
                \'Directories\': [
                    {
                        \'Name\': \'string\',
                        \'DirectoryArn\': \'string\',
                        \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                        \'CreationDateTime\': datetime(2015, 1, 1)
                    },
                ],
                
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
        
        """
        pass


class ListFacetAttributes(Paginator):
    def paginate(self, SchemaArn: str, Name: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListFacetAttributes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SchemaArn=\'string\',
              Name=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The ARN of the schema where the facet resides.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the facet whose attributes will be retrieved.
        
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
        
        """
        pass


class ListFacetNames(Paginator):
    def paginate(self, SchemaArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListFacetNames>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SchemaArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) to retrieve facet names from.
        
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
                \'FacetNames\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FacetNames** *(list) --* 
        
              The names of facets that exist within the schema.
        
              - *(string) --* 
          
        """
        pass


class ListIndex(Paginator):
    def paginate(self, DirectoryArn: str, IndexReference: Dict, RangesOnIndexedValues: List = None, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListIndex>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
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
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
             
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          The consistency level to execute the request at.
        
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
        
        """
        pass


class ListObjectAttributes(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, ConsistencyLevel: str = None, FacetFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectAttributes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\',
              FacetFilter={
                  \'SchemaArn\': \'string\',
                  \'FacetName\': \'string\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
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
        
        """
        pass


class ListObjectParentPaths(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectParentPaths>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
                \'PathToObjectIdentifiersList\': [
                    {
                        \'Path\': \'string\',
                        \'ObjectIdentifiers\': [
                            \'string\',
                        ]
                    },
                ],
                
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
              
        """
        pass


class ListObjectPolicies(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
             
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
        
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
                \'AttachedPolicyIds\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AttachedPolicyIds** *(list) --* 
        
              A list of policy ``ObjectIdentifiers`` , that are attached to the object.
        
              - *(string) --* 
          
        """
        pass


class ListPolicyAttachments(Paginator):
    def paginate(self, DirectoryArn: str, PolicyReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListPolicyAttachments>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryArn=\'string\',
              PolicyReference={
                  \'Selector\': \'string\'
              },
              ConsistencyLevel=\'SERIALIZABLE\'|\'EVENTUAL\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
             
        :type ConsistencyLevel: string
        :param ConsistencyLevel: 
        
          Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
        
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
                \'ObjectIdentifiers\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ObjectIdentifiers** *(list) --* 
        
              A list of ``ObjectIdentifiers`` to which the policy is attached.
        
              - *(string) --* 
          
        """
        pass


class ListPublishedSchemaArns(Paginator):
    def paginate(self, SchemaArn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListPublishedSchemaArns>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SchemaArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SchemaArn: string
        :param SchemaArn: 
        
          The response for ``ListPublishedSchemaArns`` when this parameter is used will list all minor version ARNs for a major version.
        
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
                \'SchemaArns\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaArns** *(list) --* 
        
              The ARNs of published schemas.
        
              - *(string) --* 
          
        """
        pass


class ListTagsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ResourceArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.
        
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
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                
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
        
        """
        pass


class ListTypedLinkFacetAttributes(Paginator):
    def paginate(self, SchemaArn: str, Name: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SchemaArn=\'string\',
              Name=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The unique name of the typed link facet.
        
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
        
        """
        pass


class ListTypedLinkFacetNames(Paginator):
    def paginate(self, SchemaArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTypedLinkFacetNames>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SchemaArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SchemaArn: string
        :param SchemaArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
        
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
                \'FacetNames\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FacetNames** *(list) --* 
        
              The names of typed link facets that exist within the schema.
        
              - *(string) --* 
          
        """
        pass


class LookupPolicy(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/LookupPolicy>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryArn=\'string\',
              ObjectReference={
                  \'Selector\': \'string\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
        
        """
        pass
