from typing import Dict
from botocore.paginate import Paginator


class ListCACertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCACertificates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ascendingOrder: boolean
        :param ascendingOrder: 
        
          Determines the order of the results.
        
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
                \'certificates\': [
                    {
                        \'certificateArn\': \'string\',
                        \'certificateId\': \'string\',
                        \'status\': \'ACTIVE\'|\'INACTIVE\',
                        \'creationDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the ListCACertificates operation.
        
            - **certificates** *(list) --* 
        
              The CA certificates registered in your AWS account.
        
              - *(dict) --* 
        
                A CA certificate.
        
                - **certificateArn** *(string) --* 
        
                  The ARN of the CA certificate.
        
                - **certificateId** *(string) --* 
        
                  The ID of the CA certificate.
        
                - **status** *(string) --* 
        
                  The status of the CA certificate.
        
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
        
                - **creationDate** *(datetime) --* 
        
                  The date the CA certificate was created.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListCertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ascendingOrder: boolean
        :param ascendingOrder: 
        
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
        
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
                \'certificates\': [
                    {
                        \'certificateArn\': \'string\',
                        \'certificateId\': \'string\',
                        \'status\': \'ACTIVE\'|\'INACTIVE\'|\'REVOKED\'|\'PENDING_TRANSFER\'|\'REGISTER_INACTIVE\'|\'PENDING_ACTIVATION\',
                        \'creationDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output of the ListCertificates operation.
        
            - **certificates** *(list) --* 
        
              The descriptions of the certificates.
        
              - *(dict) --* 
        
                Information about a certificate.
        
                - **certificateArn** *(string) --* 
        
                  The ARN of the certificate.
        
                - **certificateId** *(string) --* 
        
                  The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        
                - **status** *(string) --* 
        
                  The status of the certificate.
        
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
        
                - **creationDate** *(datetime) --* 
        
                  The date and time the certificate was created.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListCertificatesByCA(Paginator):
    def paginate(self, caCertificateId: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificatesByCA>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              caCertificateId=\'string\',
              ascendingOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type caCertificateId: string
        :param caCertificateId: **[REQUIRED]** 
        
          The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.
        
        :type ascendingOrder: boolean
        :param ascendingOrder: 
        
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
        
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
                \'certificates\': [
                    {
                        \'certificateArn\': \'string\',
                        \'certificateId\': \'string\',
                        \'status\': \'ACTIVE\'|\'INACTIVE\'|\'REVOKED\'|\'PENDING_TRANSFER\'|\'REGISTER_INACTIVE\'|\'PENDING_ACTIVATION\',
                        \'creationDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output of the ListCertificatesByCA operation.
        
            - **certificates** *(list) --* 
        
              The device certificates signed by the specified CA certificate.
        
              - *(dict) --* 
        
                Information about a certificate.
        
                - **certificateArn** *(string) --* 
        
                  The ARN of the certificate.
        
                - **certificateId** *(string) --* 
        
                  The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        
                - **status** *(string) --* 
        
                  The status of the certificate.
        
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
        
                - **creationDate** *(datetime) --* 
        
                  The date and time the certificate was created.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListOutgoingCertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListOutgoingCertificates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ascendingOrder: boolean
        :param ascendingOrder: 
        
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
        
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
                \'outgoingCertificates\': [
                    {
                        \'certificateArn\': \'string\',
                        \'certificateId\': \'string\',
                        \'transferredTo\': \'string\',
                        \'transferDate\': datetime(2015, 1, 1),
                        \'transferMessage\': \'string\',
                        \'creationDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the ListOutgoingCertificates operation.
        
            - **outgoingCertificates** *(list) --* 
        
              The certificates that are being transferred but not yet accepted.
        
              - *(dict) --* 
        
                A certificate that has been transferred but not yet accepted.
        
                - **certificateArn** *(string) --* 
        
                  The certificate ARN.
        
                - **certificateId** *(string) --* 
        
                  The certificate ID.
        
                - **transferredTo** *(string) --* 
        
                  The AWS account to which the transfer was made.
        
                - **transferDate** *(datetime) --* 
        
                  The date the transfer was initiated.
        
                - **transferMessage** *(string) --* 
        
                  The transfer message.
        
                - **creationDate** *(datetime) --* 
        
                  The certificate creation date.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPolicies(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ascendingOrder: boolean
        :param ascendingOrder: 
        
          Specifies the order for results. If true, the results are returned in ascending creation order.
        
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
                \'policies\': [
                    {
                        \'policyName\': \'string\',
                        \'policyArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the ListPolicies operation.
        
            - **policies** *(list) --* 
        
              The descriptions of the policies.
        
              - *(dict) --* 
        
                Describes an AWS IoT policy.
        
                - **policyName** *(string) --* 
        
                  The policy name.
        
                - **policyArn** *(string) --* 
        
                  The policy ARN.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPolicyPrincipals(Paginator):
    def paginate(self, policyName: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        .. danger::
        
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicyPrincipals>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              policyName=\'string\',
              ascendingOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type policyName: string
        :param policyName: **[REQUIRED]** 
        
          The policy name.
        
        :type ascendingOrder: boolean
        :param ascendingOrder: 
        
          Specifies the order for results. If true, the results are returned in ascending creation order.
        
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
                \'principals\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the ListPolicyPrincipals operation.
        
            - **principals** *(list) --* 
        
              The descriptions of the principals.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPrincipalPolicies(Paginator):
    def paginate(self, principal: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        .. danger::
        
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              principal=\'string\',
              ascendingOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type principal: string
        :param principal: **[REQUIRED]** 
        
          The principal.
        
        :type ascendingOrder: boolean
        :param ascendingOrder: 
        
          Specifies the order for results. If true, results are returned in ascending creation order.
        
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
                \'policies\': [
                    {
                        \'policyName\': \'string\',
                        \'policyArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the ListPrincipalPolicies operation.
        
            - **policies** *(list) --* 
        
              The policies.
        
              - *(dict) --* 
        
                Describes an AWS IoT policy.
        
                - **policyName** *(string) --* 
        
                  The policy name.
        
                - **policyArn** *(string) --* 
        
                  The policy ARN.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPrincipalThings(Paginator):
    def paginate(self, principal: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalThings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              principal=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type principal: string
        :param principal: **[REQUIRED]** 
        
          The principal.
        
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
                \'things\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the ListPrincipalThings operation.
        
            - **things** *(list) --* 
        
              The things.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListThingTypes(Paginator):
    def paginate(self, thingTypeName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              thingTypeName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type thingTypeName: string
        :param thingTypeName: 
        
          The name of the thing type.
        
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
                \'thingTypes\': [
                    {
                        \'thingTypeName\': \'string\',
                        \'thingTypeArn\': \'string\',
                        \'thingTypeProperties\': {
                            \'thingTypeDescription\': \'string\',
                            \'searchableAttributes\': [
                                \'string\',
                            ]
                        },
                        \'thingTypeMetadata\': {
                            \'deprecated\': True|False,
                            \'deprecationDate\': datetime(2015, 1, 1),
                            \'creationDate\': datetime(2015, 1, 1)
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the ListThingTypes operation.
        
            - **thingTypes** *(list) --* 
        
              The thing types.
        
              - *(dict) --* 
        
                The definition of the thing type, including thing type name and description.
        
                - **thingTypeName** *(string) --* 
        
                  The name of the thing type.
        
                - **thingTypeArn** *(string) --* 
        
                  The thing type ARN.
        
                - **thingTypeProperties** *(dict) --* 
        
                  The ThingTypeProperties for the thing type.
        
                  - **thingTypeDescription** *(string) --* 
        
                    The description of the thing type.
        
                  - **searchableAttributes** *(list) --* 
        
                    A list of searchable thing attribute names.
        
                    - *(string) --* 
                
                - **thingTypeMetadata** *(dict) --* 
        
                  The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.
        
                  - **deprecated** *(boolean) --* 
        
                    Whether the thing type is deprecated. If **true** , no new things could be associated with this type.
        
                  - **deprecationDate** *(datetime) --* 
        
                    The date and time when the thing type was deprecated.
        
                  - **creationDate** *(datetime) --* 
        
                    The date and time when the thing type was created.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListThings(Paginator):
    def paginate(self, attributeName: str = None, attributeValue: str = None, thingTypeName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              attributeName=\'string\',
              attributeValue=\'string\',
              thingTypeName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type attributeName: string
        :param attributeName: 
        
          The attribute name used to search for things.
        
        :type attributeValue: string
        :param attributeValue: 
        
          The attribute value used to search for things.
        
        :type thingTypeName: string
        :param thingTypeName: 
        
          The name of the thing type used to search for things.
        
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
                \'things\': [
                    {
                        \'thingName\': \'string\',
                        \'thingTypeName\': \'string\',
                        \'thingArn\': \'string\',
                        \'attributes\': {
                            \'string\': \'string\'
                        },
                        \'version\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the ListThings operation.
        
            - **things** *(list) --* 
        
              The things.
        
              - *(dict) --* 
        
                The properties of the thing, including thing name, thing type name, and a list of thing attributes.
        
                - **thingName** *(string) --* 
        
                  The name of the thing.
        
                - **thingTypeName** *(string) --* 
        
                  The name of the thing type, if the thing has been associated with a type.
        
                - **thingArn** *(string) --* 
        
                  The thing ARN.
        
                - **attributes** *(dict) --* 
        
                  A list of thing attributes which are name-value pairs.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **version** *(integer) --* 
        
                  The version of the thing record in the registry.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListTopicRules(Paginator):
    def paginate(self, topic: str = None, ruleDisabled: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTopicRules>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              topic=\'string\',
              ruleDisabled=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type topic: string
        :param topic: 
        
          The topic.
        
        :type ruleDisabled: boolean
        :param ruleDisabled: 
        
          Specifies whether the rule is disabled.
        
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
                \'rules\': [
                    {
                        \'ruleArn\': \'string\',
                        \'ruleName\': \'string\',
                        \'topicPattern\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'ruleDisabled\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output from the ListTopicRules operation.
        
            - **rules** *(list) --* 
        
              The rules.
        
              - *(dict) --* 
        
                Describes a rule.
        
                - **ruleArn** *(string) --* 
        
                  The rule ARN.
        
                - **ruleName** *(string) --* 
        
                  The name of the rule.
        
                - **topicPattern** *(string) --* 
        
                  The pattern for the topic names that apply.
        
                - **createdAt** *(datetime) --* 
        
                  The date and time the rule was created.
        
                - **ruleDisabled** *(boolean) --* 
        
                  Specifies whether the rule is disabled.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
