from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAppliedSchemaArns(Paginator):
    def paginate(self, DirectoryArn: str, SchemaArn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_applied_schema_arns`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListAppliedSchemaArns>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              SchemaArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SchemaArns': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SchemaArns** *(list) --* 
              The ARNs of schemas that are applied to the directory.
              - *(string) --* 
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
        """
        pass


class ListAttachedIndices(Paginator):
    def paginate(self, DirectoryArn: str, TargetReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_attached_indices`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListAttachedIndices>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              TargetReference={
                  'Selector': 'string'
              },
              ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'IndexAttachments': [
                    {
                        'IndexedAttributes': [
                            {
                                'Key': {
                                    'SchemaArn': 'string',
                                    'FacetName': 'string',
                                    'Name': 'string'
                                },
                                'Value': {
                                    'StringValue': 'string',
                                    'BinaryValue': b'bytes',
                                    'BooleanValue': True|False,
                                    'NumberValue': 'string',
                                    'DatetimeValue': datetime(2015, 1, 1)
                                }
                            },
                        ],
                        'ObjectIdentifier': 'string'
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
        """
        pass


class ListDevelopmentSchemaArns(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_development_schema_arns`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListDevelopmentSchemaArns>`_
        
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
                'SchemaArns': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SchemaArns** *(list) --* 
              The ARNs of retrieved development schemas.
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


class ListDirectories(Paginator):
    def paginate(self, state: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_directories`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListDirectories>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              state='ENABLED'|'DISABLED'|'DELETED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Directories': [
                    {
                        'Name': 'string',
                        'DirectoryArn': 'string',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'CreationDateTime': datetime(2015, 1, 1)
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
        """
        pass


class ListFacetAttributes(Paginator):
    def paginate(self, SchemaArn: str, Name: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_facet_attributes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListFacetAttributes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SchemaArn='string',
              Name='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Attributes': [
                    {
                        'Name': 'string',
                        'AttributeDefinition': {
                            'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
                            'DefaultValue': {
                                'StringValue': 'string',
                                'BinaryValue': b'bytes',
                                'BooleanValue': True|False,
                                'NumberValue': 'string',
                                'DatetimeValue': datetime(2015, 1, 1)
                            },
                            'IsImmutable': True|False,
                            'Rules': {
                                'string': {
                                    'Type': 'BINARY_LENGTH'|'NUMBER_COMPARISON'|'STRING_FROM_SET'|'STRING_LENGTH',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                }
                            }
                        },
                        'AttributeReference': {
                            'TargetFacetName': 'string',
                            'TargetAttributeName': 'string'
                        },
                        'RequiredBehavior': 'REQUIRED_ALWAYS'|'NOT_REQUIRED'
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
        """
        pass


class ListFacetNames(Paginator):
    def paginate(self, SchemaArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_facet_names`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListFacetNames>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SchemaArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'FacetNames': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FacetNames** *(list) --* 
              The names of facets that exist within the schema.
              - *(string) --* 
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
        """
        pass


class ListIncomingTypedLinks(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, FilterAttributeRanges: List = None, FilterTypedLink: Dict = None, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_incoming_typed_links`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListIncomingTypedLinks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              ObjectReference={
                  'Selector': 'string'
              },
              FilterAttributeRanges=[
                  {
                      'AttributeName': 'string',
                      'Range': {
                          'StartMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                          'StartValue': {
                              'StringValue': 'string',
                              'BinaryValue': b'bytes',
                              'BooleanValue': True|False,
                              'NumberValue': 'string',
                              'DatetimeValue': datetime(2015, 1, 1)
                          },
                          'EndMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                          'EndValue': {
                              'StringValue': 'string',
                              'BinaryValue': b'bytes',
                              'BooleanValue': True|False,
                              'NumberValue': 'string',
                              'DatetimeValue': datetime(2015, 1, 1)
                          }
                      }
                  },
              ],
              FilterTypedLink={
                  'SchemaArn': 'string',
                  'TypedLinkName': 'string'
              },
              ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LinkSpecifiers': [
                    {
                        'TypedLinkFacet': {
                            'SchemaArn': 'string',
                            'TypedLinkName': 'string'
                        },
                        'SourceObjectReference': {
                            'Selector': 'string'
                        },
                        'TargetObjectReference': {
                            'Selector': 'string'
                        },
                        'IdentityAttributeValues': [
                            {
                                'AttributeName': 'string',
                                'Value': {
                                    'StringValue': 'string',
                                    'BinaryValue': b'bytes',
                                    'BooleanValue': True|False,
                                    'NumberValue': 'string',
                                    'DatetimeValue': datetime(2015, 1, 1)
                                }
                            },
                        ]
                    },
                ],
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
        """
        pass


class ListIndex(Paginator):
    def paginate(self, DirectoryArn: str, IndexReference: Dict, RangesOnIndexedValues: List = None, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_index`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListIndex>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              RangesOnIndexedValues=[
                  {
                      'AttributeKey': {
                          'SchemaArn': 'string',
                          'FacetName': 'string',
                          'Name': 'string'
                      },
                      'Range': {
                          'StartMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                          'StartValue': {
                              'StringValue': 'string',
                              'BinaryValue': b'bytes',
                              'BooleanValue': True|False,
                              'NumberValue': 'string',
                              'DatetimeValue': datetime(2015, 1, 1)
                          },
                          'EndMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                          'EndValue': {
                              'StringValue': 'string',
                              'BinaryValue': b'bytes',
                              'BooleanValue': True|False,
                              'NumberValue': 'string',
                              'DatetimeValue': datetime(2015, 1, 1)
                          }
                      }
                  },
              ],
              IndexReference={
                  'Selector': 'string'
              },
              ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'IndexAttachments': [
                    {
                        'IndexedAttributes': [
                            {
                                'Key': {
                                    'SchemaArn': 'string',
                                    'FacetName': 'string',
                                    'Name': 'string'
                                },
                                'Value': {
                                    'StringValue': 'string',
                                    'BinaryValue': b'bytes',
                                    'BooleanValue': True|False,
                                    'NumberValue': 'string',
                                    'DatetimeValue': datetime(2015, 1, 1)
                                }
                            },
                        ],
                        'ObjectIdentifier': 'string'
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
        """
        pass


class ListManagedSchemaArns(Paginator):
    def paginate(self, SchemaArn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_managed_schema_arns`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListManagedSchemaArns>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SchemaArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SchemaArns': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SchemaArns** *(list) --* 
              The ARNs for all AWS managed schemas.
              - *(string) --* 
        :type SchemaArn: string
        :param SchemaArn:
          The response for ListManagedSchemaArns. When this parameter is used, all minor version ARNs for a major version are listed.
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


class ListObjectAttributes(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, ConsistencyLevel: str = None, FacetFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_object_attributes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectAttributes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              ObjectReference={
                  'Selector': 'string'
              },
              ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
              FacetFilter={
                  'SchemaArn': 'string',
                  'FacetName': 'string'
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
                'Attributes': [
                    {
                        'Key': {
                            'SchemaArn': 'string',
                            'FacetName': 'string',
                            'Name': 'string'
                        },
                        'Value': {
                            'StringValue': 'string',
                            'BinaryValue': b'bytes',
                            'BooleanValue': True|False,
                            'NumberValue': 'string',
                            'DatetimeValue': datetime(2015, 1, 1)
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
        """
        pass


class ListObjectParentPaths(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_object_parent_paths`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectParentPaths>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              ObjectReference={
                  'Selector': 'string'
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
                'PathToObjectIdentifiersList': [
                    {
                        'Path': 'string',
                        'ObjectIdentifiers': [
                            'string',
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
        """
        pass


class ListObjectPolicies(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_object_policies`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListObjectPolicies>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              ObjectReference={
                  'Selector': 'string'
              },
              ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AttachedPolicyIds': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AttachedPolicyIds** *(list) --* 
              A list of policy ``ObjectIdentifiers`` , that are attached to the object.
              - *(string) --* 
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
        """
        pass


class ListOutgoingTypedLinks(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, FilterAttributeRanges: List = None, FilterTypedLink: Dict = None, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_outgoing_typed_links`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListOutgoingTypedLinks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              ObjectReference={
                  'Selector': 'string'
              },
              FilterAttributeRanges=[
                  {
                      'AttributeName': 'string',
                      'Range': {
                          'StartMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                          'StartValue': {
                              'StringValue': 'string',
                              'BinaryValue': b'bytes',
                              'BooleanValue': True|False,
                              'NumberValue': 'string',
                              'DatetimeValue': datetime(2015, 1, 1)
                          },
                          'EndMode': 'FIRST'|'LAST'|'LAST_BEFORE_MISSING_VALUES'|'INCLUSIVE'|'EXCLUSIVE',
                          'EndValue': {
                              'StringValue': 'string',
                              'BinaryValue': b'bytes',
                              'BooleanValue': True|False,
                              'NumberValue': 'string',
                              'DatetimeValue': datetime(2015, 1, 1)
                          }
                      }
                  },
              ],
              FilterTypedLink={
                  'SchemaArn': 'string',
                  'TypedLinkName': 'string'
              },
              ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TypedLinkSpecifiers': [
                    {
                        'TypedLinkFacet': {
                            'SchemaArn': 'string',
                            'TypedLinkName': 'string'
                        },
                        'SourceObjectReference': {
                            'Selector': 'string'
                        },
                        'TargetObjectReference': {
                            'Selector': 'string'
                        },
                        'IdentityAttributeValues': [
                            {
                                'AttributeName': 'string',
                                'Value': {
                                    'StringValue': 'string',
                                    'BinaryValue': b'bytes',
                                    'BooleanValue': True|False,
                                    'NumberValue': 'string',
                                    'DatetimeValue': datetime(2015, 1, 1)
                                }
                            },
                        ]
                    },
                ],
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
        """
        pass


class ListPolicyAttachments(Paginator):
    def paginate(self, DirectoryArn: str, PolicyReference: Dict, ConsistencyLevel: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_policy_attachments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListPolicyAttachments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              PolicyReference={
                  'Selector': 'string'
              },
              ConsistencyLevel='SERIALIZABLE'|'EVENTUAL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ObjectIdentifiers': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ObjectIdentifiers** *(list) --* 
              A list of ``ObjectIdentifiers`` to which the policy is attached.
              - *(string) --* 
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
        """
        pass


class ListPublishedSchemaArns(Paginator):
    def paginate(self, SchemaArn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_published_schema_arns`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListPublishedSchemaArns>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SchemaArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SchemaArns': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SchemaArns** *(list) --* 
              The ARNs of published schemas.
              - *(string) --* 
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
        """
        pass


class ListTagsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_tags_for_resource`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
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
        """
        pass


class ListTypedLinkFacetAttributes(Paginator):
    def paginate(self, SchemaArn: str, Name: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_typed_link_facet_attributes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTypedLinkFacetAttributes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SchemaArn='string',
              Name='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Attributes': [
                    {
                        'Name': 'string',
                        'Type': 'STRING'|'BINARY'|'BOOLEAN'|'NUMBER'|'DATETIME'|'VARIANT',
                        'DefaultValue': {
                            'StringValue': 'string',
                            'BinaryValue': b'bytes',
                            'BooleanValue': True|False,
                            'NumberValue': 'string',
                            'DatetimeValue': datetime(2015, 1, 1)
                        },
                        'IsImmutable': True|False,
                        'Rules': {
                            'string': {
                                'Type': 'BINARY_LENGTH'|'NUMBER_COMPARISON'|'STRING_FROM_SET'|'STRING_LENGTH',
                                'Parameters': {
                                    'string': 'string'
                                }
                            }
                        },
                        'RequiredBehavior': 'REQUIRED_ALWAYS'|'NOT_REQUIRED'
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
        """
        pass


class ListTypedLinkFacetNames(Paginator):
    def paginate(self, SchemaArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.list_typed_link_facet_names`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListTypedLinkFacetNames>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SchemaArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'FacetNames': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FacetNames** *(list) --* 
              The names of typed link facets that exist within the schema.
              - *(string) --* 
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
        """
        pass


class LookupPolicy(Paginator):
    def paginate(self, DirectoryArn: str, ObjectReference: Dict, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudDirectory.Client.lookup_policy`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/LookupPolicy>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryArn='string',
              ObjectReference={
                  'Selector': 'string'
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
                'PolicyToPathList': [
                    {
                        'Path': 'string',
                        'Policies': [
                            {
                                'PolicyId': 'string',
                                'ObjectIdentifier': 'string',
                                'PolicyType': 'string'
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
        """
        pass
