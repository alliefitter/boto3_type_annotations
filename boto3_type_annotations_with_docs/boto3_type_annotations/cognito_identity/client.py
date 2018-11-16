from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
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

    def create_identity_pool(self, IdentityPoolName: str, AllowUnauthenticatedIdentities: bool, SupportedLoginProviders: Dict = None, DeveloperProviderName: str = None, OpenIdConnectProviderARNs: List = None, CognitoIdentityProviders: List = None, SamlProviderARNs: List = None) -> Dict:
        """
        Creates a new identity pool. The identity pool is a store of user identity information that is specific to your AWS account. The limit on identity pools is 60 per account. The keys for ``SupportedLoginProviders`` are as follows:
        
        * Facebook: ``graph.facebook.com``   
         
        * Google: ``accounts.google.com``   
         
        * Amazon: ``www.amazon.com``   
         
        * Twitter: ``api.twitter.com``   
         
        * Digits: ``www.digits.com``   
         
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/CreateIdentityPool>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_identity_pool(
              IdentityPoolName=\'string\',
              AllowUnauthenticatedIdentities=True|False,
              SupportedLoginProviders={
                  \'string\': \'string\'
              },
              DeveloperProviderName=\'string\',
              OpenIdConnectProviderARNs=[
                  \'string\',
              ],
              CognitoIdentityProviders=[
                  {
                      \'ProviderName\': \'string\',
                      \'ClientId\': \'string\',
                      \'ServerSideTokenCheck\': True|False
                  },
              ],
              SamlProviderARNs=[
                  \'string\',
              ]
          )
        :type IdentityPoolName: string
        :param IdentityPoolName: **[REQUIRED]** 
        
          A string that you provide.
        
        :type AllowUnauthenticatedIdentities: boolean
        :param AllowUnauthenticatedIdentities: **[REQUIRED]** 
        
          TRUE if the identity pool supports unauthenticated logins.
        
        :type SupportedLoginProviders: dict
        :param SupportedLoginProviders: 
        
          Optional key:value pairs mapping provider names to provider app IDs.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type DeveloperProviderName: string
        :param DeveloperProviderName: 
        
          The \"domain\" by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the ``DeveloperProviderName`` , you can use letters as well as period (``.`` ), underscore (``_`` ), and dash (``-`` ).
        
          Once you have set a developer provider name, you cannot change it. Please take care in setting this parameter.
        
        :type OpenIdConnectProviderARNs: list
        :param OpenIdConnectProviderARNs: 
        
          A list of OpendID Connect provider ARNs.
        
          - *(string) --* 
        
        :type CognitoIdentityProviders: list
        :param CognitoIdentityProviders: 
        
          An array of Amazon Cognito Identity user pools and their client IDs.
        
          - *(dict) --* 
        
            A provider representing an Amazon Cognito Identity User Pool and its client ID.
        
            - **ProviderName** *(string) --* 
        
              The provider name for an Amazon Cognito Identity User Pool. For example, ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .
        
            - **ClientId** *(string) --* 
        
              The client ID for the Amazon Cognito Identity User Pool.
        
            - **ServerSideTokenCheck** *(boolean) --* 
        
              TRUE if server-side token validation is enabled for the identity provider’s token.
        
        :type SamlProviderARNs: list
        :param SamlProviderARNs: 
        
          An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\',
                \'IdentityPoolName\': \'string\',
                \'AllowUnauthenticatedIdentities\': True|False,
                \'SupportedLoginProviders\': {
                    \'string\': \'string\'
                },
                \'DeveloperProviderName\': \'string\',
                \'OpenIdConnectProviderARNs\': [
                    \'string\',
                ],
                \'CognitoIdentityProviders\': [
                    {
                        \'ProviderName\': \'string\',
                        \'ClientId\': \'string\',
                        \'ServerSideTokenCheck\': True|False
                    },
                ],
                \'SamlProviderARNs\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            An object representing an Amazon Cognito identity pool.
        
            - **IdentityPoolId** *(string) --* 
        
              An identity pool ID in the format REGION:GUID.
        
            - **IdentityPoolName** *(string) --* 
        
              A string that you provide.
        
            - **AllowUnauthenticatedIdentities** *(boolean) --* 
        
              TRUE if the identity pool supports unauthenticated logins.
        
            - **SupportedLoginProviders** *(dict) --* 
        
              Optional key:value pairs mapping provider names to provider app IDs.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **DeveloperProviderName** *(string) --* 
        
              The \"domain\" by which Cognito will refer to your users.
        
            - **OpenIdConnectProviderARNs** *(list) --* 
        
              A list of OpendID Connect provider ARNs.
        
              - *(string) --* 
          
            - **CognitoIdentityProviders** *(list) --* 
        
              A list representing an Amazon Cognito Identity User Pool and its client ID.
        
              - *(dict) --* 
        
                A provider representing an Amazon Cognito Identity User Pool and its client ID.
        
                - **ProviderName** *(string) --* 
        
                  The provider name for an Amazon Cognito Identity User Pool. For example, ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .
        
                - **ClientId** *(string) --* 
        
                  The client ID for the Amazon Cognito Identity User Pool.
        
                - **ServerSideTokenCheck** *(boolean) --* 
        
                  TRUE if server-side token validation is enabled for the identity provider’s token.
        
            - **SamlProviderARNs** *(list) --* 
        
              An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
        
              - *(string) --* 
          
        """
        pass

    def delete_identities(self, IdentityIdsToDelete: List) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/DeleteIdentities>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_identities(
              IdentityIdsToDelete=[
                  \'string\',
              ]
          )
        :type IdentityIdsToDelete: list
        :param IdentityIdsToDelete: **[REQUIRED]** 
        
          A list of 1-60 identities that you want to delete.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedIdentityIds\': [
                    {
                        \'IdentityId\': \'string\',
                        \'ErrorCode\': \'AccessDenied\'|\'InternalServerError\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returned in response to a successful ``DeleteIdentities`` operation.
        
            - **UnprocessedIdentityIds** *(list) --* 
        
              An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.
        
              - *(dict) --* 
        
                An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.
        
                - **IdentityId** *(string) --* 
        
                  A unique identifier in the format REGION:GUID.
        
                - **ErrorCode** *(string) --* 
        
                  The error code indicating the type of error that occurred.
        
        """
        pass

    def delete_identity_pool(self, IdentityPoolId: str) -> NoReturn:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/DeleteIdentityPool>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_identity_pool(
              IdentityPoolId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :returns: None
        """
        pass

    def describe_identity(self, IdentityId: str) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/DescribeIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_identity(
              IdentityId=\'string\'
          )
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** 
        
          A unique identifier in the format REGION:GUID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityId\': \'string\',
                \'Logins\': [
                    \'string\',
                ],
                \'CreationDate\': datetime(2015, 1, 1),
                \'LastModifiedDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A description of the identity.
        
            - **IdentityId** *(string) --* 
        
              A unique identifier in the format REGION:GUID.
        
            - **Logins** *(list) --* 
        
              A set of optional name-value pairs that map provider names to provider tokens.
        
              - *(string) --* 
          
            - **CreationDate** *(datetime) --* 
        
              Date on which the identity was created.
        
            - **LastModifiedDate** *(datetime) --* 
        
              Date on which the identity was last modified.
        
        """
        pass

    def describe_identity_pool(self, IdentityPoolId: str) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/DescribeIdentityPool>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_identity_pool(
              IdentityPoolId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\',
                \'IdentityPoolName\': \'string\',
                \'AllowUnauthenticatedIdentities\': True|False,
                \'SupportedLoginProviders\': {
                    \'string\': \'string\'
                },
                \'DeveloperProviderName\': \'string\',
                \'OpenIdConnectProviderARNs\': [
                    \'string\',
                ],
                \'CognitoIdentityProviders\': [
                    {
                        \'ProviderName\': \'string\',
                        \'ClientId\': \'string\',
                        \'ServerSideTokenCheck\': True|False
                    },
                ],
                \'SamlProviderARNs\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            An object representing an Amazon Cognito identity pool.
        
            - **IdentityPoolId** *(string) --* 
        
              An identity pool ID in the format REGION:GUID.
        
            - **IdentityPoolName** *(string) --* 
        
              A string that you provide.
        
            - **AllowUnauthenticatedIdentities** *(boolean) --* 
        
              TRUE if the identity pool supports unauthenticated logins.
        
            - **SupportedLoginProviders** *(dict) --* 
        
              Optional key:value pairs mapping provider names to provider app IDs.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **DeveloperProviderName** *(string) --* 
        
              The \"domain\" by which Cognito will refer to your users.
        
            - **OpenIdConnectProviderARNs** *(list) --* 
        
              A list of OpendID Connect provider ARNs.
        
              - *(string) --* 
          
            - **CognitoIdentityProviders** *(list) --* 
        
              A list representing an Amazon Cognito Identity User Pool and its client ID.
        
              - *(dict) --* 
        
                A provider representing an Amazon Cognito Identity User Pool and its client ID.
        
                - **ProviderName** *(string) --* 
        
                  The provider name for an Amazon Cognito Identity User Pool. For example, ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .
        
                - **ClientId** *(string) --* 
        
                  The client ID for the Amazon Cognito Identity User Pool.
        
                - **ServerSideTokenCheck** *(boolean) --* 
        
                  TRUE if server-side token validation is enabled for the identity provider’s token.
        
            - **SamlProviderARNs** *(list) --* 
        
              An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
        
              - *(string) --* 
          
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

    def get_credentials_for_identity(self, IdentityId: str, Logins: Dict = None, CustomRoleArn: str = None) -> Dict:
        """
        
        This is a public API. You do not need any credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/GetCredentialsForIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_credentials_for_identity(
              IdentityId=\'string\',
              Logins={
                  \'string\': \'string\'
              },
              CustomRoleArn=\'string\'
          )
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** 
        
          A unique identifier in the format REGION:GUID.
        
        :type Logins: dict
        :param Logins: 
        
          A set of optional name-value pairs that map provider names to provider tokens.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type CustomRoleArn: string
        :param CustomRoleArn: 
        
          The Amazon Resource Name (ARN) of the role to be assumed when multiple roles were received in the token from the identity provider. For example, a SAML-based identity provider. This parameter is optional for identity providers that do not support role customization.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityId\': \'string\',
                \'Credentials\': {
                    \'AccessKeyId\': \'string\',
                    \'SecretKey\': \'string\',
                    \'SessionToken\': \'string\',
                    \'Expiration\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returned in response to a successful ``GetCredentialsForIdentity`` operation.
        
            - **IdentityId** *(string) --* 
        
              A unique identifier in the format REGION:GUID.
        
            - **Credentials** *(dict) --* 
        
              Credentials for the provided identity ID.
        
              - **AccessKeyId** *(string) --* 
        
                The Access Key portion of the credentials.
        
              - **SecretKey** *(string) --* 
        
                The Secret Access Key portion of the credentials
        
              - **SessionToken** *(string) --* 
        
                The Session Token portion of the credentials
        
              - **Expiration** *(datetime) --* 
        
                The date at which these credentials will expire.
        
        """
        pass

    def get_id(self, IdentityPoolId: str, AccountId: str = None, Logins: Dict = None) -> Dict:
        """
        
        This is a public API. You do not need any credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/GetId>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_id(
              AccountId=\'string\',
              IdentityPoolId=\'string\',
              Logins={
                  \'string\': \'string\'
              }
          )
        :type AccountId: string
        :param AccountId: 
        
          A standard AWS account ID (9+ digits).
        
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :type Logins: dict
        :param Logins: 
        
          A set of optional name-value pairs that map provider names to provider tokens. The available provider names for ``Logins`` are as follows:
        
          * Facebook: ``graph.facebook.com``   
           
          * Amazon Cognito Identity Provider: ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789``   
           
          * Google: ``accounts.google.com``   
           
          * Amazon: ``www.amazon.com``   
           
          * Twitter: ``api.twitter.com``   
           
          * Digits: ``www.digits.com``   
           
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returned in response to a GetId request.
        
            - **IdentityId** *(string) --* 
        
              A unique identifier in the format REGION:GUID.
        
        """
        pass

    def get_identity_pool_roles(self, IdentityPoolId: str) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/GetIdentityPoolRoles>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_identity_pool_roles(
              IdentityPoolId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\',
                \'Roles\': {
                    \'string\': \'string\'
                },
                \'RoleMappings\': {
                    \'string\': {
                        \'Type\': \'Token\'|\'Rules\',
                        \'AmbiguousRoleResolution\': \'AuthenticatedRole\'|\'Deny\',
                        \'RulesConfiguration\': {
                            \'Rules\': [
                                {
                                    \'Claim\': \'string\',
                                    \'MatchType\': \'Equals\'|\'Contains\'|\'StartsWith\'|\'NotEqual\',
                                    \'Value\': \'string\',
                                    \'RoleARN\': \'string\'
                                },
                            ]
                        }
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returned in response to a successful ``GetIdentityPoolRoles`` operation.
        
            - **IdentityPoolId** *(string) --* 
        
              An identity pool ID in the format REGION:GUID.
        
            - **Roles** *(dict) --* 
        
              The map of roles associated with this pool. Currently only authenticated and unauthenticated roles are supported.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **RoleMappings** *(dict) --* 
        
              How users for a specific identity provider are to mapped to roles. This is a String-to- RoleMapping object map. The string identifies the identity provider, for example, \"graph.facebook.com\" or \"cognito-idp-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id\".
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  A role mapping.
        
                  - **Type** *(string) --* 
        
                    The role mapping type. Token will use ``cognito:roles`` and ``cognito:preferred_role`` claims from the Cognito identity provider token to map groups to roles. Rules will attempt to match claims from the token to map to a role.
        
                  - **AmbiguousRoleResolution** *(string) --* 
        
                    If you specify Token or Rules as the ``Type`` , ``AmbiguousRoleResolution`` is required.
        
                    Specifies the action to be taken if either no rules match the claim value for the ``Rules`` type, or there is no ``cognito:preferred_role`` claim and there are multiple ``cognito:roles`` matches for the ``Token`` type.
        
                  - **RulesConfiguration** *(dict) --* 
        
                    The rules to be used for mapping users to roles.
        
                    If you specify Rules as the role mapping type, ``RulesConfiguration`` is required.
        
                    - **Rules** *(list) --* 
        
                      An array of rules. You can specify up to 25 rules per identity provider.
        
                      Rules are evaluated in order. The first one to match specifies the role.
        
                      - *(dict) --* 
        
                        A rule that maps a claim name, a claim value, and a match type to a role ARN.
        
                        - **Claim** *(string) --* 
        
                          The claim name that must be present in the token, for example, \"isAdmin\" or \"paid\".
        
                        - **MatchType** *(string) --* 
        
                          The match condition that specifies how closely the claim value in the IdP token must match ``Value`` .
        
                        - **Value** *(string) --* 
        
                          A brief string that the claim must match, for example, \"paid\" or \"yes\".
        
                        - **RoleARN** *(string) --* 
        
                          The role ARN.
        
        """
        pass

    def get_open_id_token(self, IdentityId: str, Logins: Dict = None) -> Dict:
        """
        
        The OpenId token is valid for 15 minutes.
        
        This is a public API. You do not need any credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/GetOpenIdToken>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_open_id_token(
              IdentityId=\'string\',
              Logins={
                  \'string\': \'string\'
              }
          )
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** 
        
          A unique identifier in the format REGION:GUID.
        
        :type Logins: dict
        :param Logins: 
        
          A set of optional name-value pairs that map provider names to provider tokens. When using graph.facebook.com and www.amazon.com, supply the access_token returned from the provider\'s authflow. For accounts.google.com, an Amazon Cognito Identity Provider, or any other OpenId Connect provider, always include the ``id_token`` .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityId\': \'string\',
                \'Token\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returned in response to a successful GetOpenIdToken request.
        
            - **IdentityId** *(string) --* 
        
              A unique identifier in the format REGION:GUID. Note that the IdentityId returned may not match the one passed on input.
        
            - **Token** *(string) --* 
        
              An OpenID token, valid for 15 minutes.
        
        """
        pass

    def get_open_id_token_for_developer_identity(self, IdentityPoolId: str, Logins: Dict, IdentityId: str = None, TokenDuration: int = None) -> Dict:
        """
        
        You can use ``GetOpenIdTokenForDeveloperIdentity`` to create a new identity and to link new logins (that is, user credentials issued by a public provider or developer provider) to an existing identity. When you want to create a new identity, the ``IdentityId`` should be null. When you want to associate a new login with an existing authenticated/unauthenticated identity, you can do so by providing the existing ``IdentityId`` . This API will create the identity in the specified ``IdentityPoolId`` .
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/GetOpenIdTokenForDeveloperIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_open_id_token_for_developer_identity(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              Logins={
                  \'string\': \'string\'
              },
              TokenDuration=123
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :type IdentityId: string
        :param IdentityId: 
        
          A unique identifier in the format REGION:GUID.
        
        :type Logins: dict
        :param Logins: **[REQUIRED]** 
        
          A set of optional name-value pairs that map provider names to provider tokens. Each name-value pair represents a user from a public provider or developer provider. If the user is from a developer provider, the name-value pair will follow the syntax ``\"developer_provider_name\": \"developer_user_identifier\"`` . The developer provider is the \"domain\" by which Cognito will refer to your users; you provided this domain while creating/updating the identity pool. The developer user identifier is an identifier from your backend that uniquely identifies a user. When you create an identity pool, you can specify the supported logins.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type TokenDuration: integer
        :param TokenDuration: 
        
          The expiration time of the token, in seconds. You can specify a custom expiration time for the token so that you can cache it. If you don\'t provide an expiration time, the token is valid for 15 minutes. You can exchange the token with Amazon STS for temporary AWS credentials, which are valid for a maximum of one hour. The maximum token duration you can set is 24 hours. You should take care in setting the expiration time for a token, as there are significant security implications: an attacker could use a leaked token to access your AWS resources for the token\'s duration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityId\': \'string\',
                \'Token\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returned in response to a successful ``GetOpenIdTokenForDeveloperIdentity`` request.
        
            - **IdentityId** *(string) --* 
        
              A unique identifier in the format REGION:GUID.
        
            - **Token** *(string) --* 
        
              An OpenID token.
        
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

    def list_identities(self, IdentityPoolId: str, MaxResults: int, NextToken: str = None, HideDisabled: bool = None) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/ListIdentities>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_identities(
              IdentityPoolId=\'string\',
              MaxResults=123,
              NextToken=\'string\',
              HideDisabled=True|False
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :type MaxResults: integer
        :param MaxResults: **[REQUIRED]** 
        
          The maximum number of identities to return.
        
        :type NextToken: string
        :param NextToken: 
        
          A pagination token.
        
        :type HideDisabled: boolean
        :param HideDisabled: 
        
          An optional boolean parameter that allows you to hide disabled identities. If omitted, the ListIdentities API will include disabled identities in the response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\',
                \'Identities\': [
                    {
                        \'IdentityId\': \'string\',
                        \'Logins\': [
                            \'string\',
                        ],
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'LastModifiedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The response to a ListIdentities request.
        
            - **IdentityPoolId** *(string) --* 
        
              An identity pool ID in the format REGION:GUID.
        
            - **Identities** *(list) --* 
        
              An object containing a set of identities and associated mappings.
        
              - *(dict) --* 
        
                A description of the identity.
        
                - **IdentityId** *(string) --* 
        
                  A unique identifier in the format REGION:GUID.
        
                - **Logins** *(list) --* 
        
                  A set of optional name-value pairs that map provider names to provider tokens.
        
                  - *(string) --* 
              
                - **CreationDate** *(datetime) --* 
        
                  Date on which the identity was created.
        
                - **LastModifiedDate** *(datetime) --* 
        
                  Date on which the identity was last modified.
        
            - **NextToken** *(string) --* 
        
              A pagination token.
        
        """
        pass

    def list_identity_pools(self, MaxResults: int, NextToken: str = None) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/ListIdentityPools>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_identity_pools(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: **[REQUIRED]** 
        
          The maximum number of identities to return.
        
        :type NextToken: string
        :param NextToken: 
        
          A pagination token.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPools\': [
                    {
                        \'IdentityPoolId\': \'string\',
                        \'IdentityPoolName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a successful ListIdentityPools action.
        
            - **IdentityPools** *(list) --* 
        
              The identity pools returned by the ListIdentityPools action.
        
              - *(dict) --* 
        
                A description of the identity pool.
        
                - **IdentityPoolId** *(string) --* 
        
                  An identity pool ID in the format REGION:GUID.
        
                - **IdentityPoolName** *(string) --* 
        
                  A string that you provide.
        
            - **NextToken** *(string) --* 
        
              A pagination token.
        
        """
        pass

    def lookup_developer_identity(self, IdentityPoolId: str, IdentityId: str = None, DeveloperUserIdentifier: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/LookupDeveloperIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.lookup_developer_identity(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              DeveloperUserIdentifier=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :type IdentityId: string
        :param IdentityId: 
        
          A unique identifier in the format REGION:GUID.
        
        :type DeveloperUserIdentifier: string
        :param DeveloperUserIdentifier: 
        
          A unique ID used by your backend authentication process to identify a user. Typically, a developer identity provider would issue many developer user identifiers, in keeping with the number of users.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of identities to return.
        
        :type NextToken: string
        :param NextToken: 
        
          A pagination token. The first call you make will have ``NextToken`` set to null. After that the service will return ``NextToken`` values as needed. For example, let\'s say you make a request with ``MaxResults`` set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityId\': \'string\',
                \'DeveloperUserIdentifierList\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returned in response to a successful ``LookupDeveloperIdentity`` action.
        
            - **IdentityId** *(string) --* 
        
              A unique identifier in the format REGION:GUID.
        
            - **DeveloperUserIdentifierList** *(list) --* 
        
              This is the list of developer user identifiers associated with an identity ID. Cognito supports the association of multiple developer user identifiers with an identity ID.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A pagination token. The first call you make will have ``NextToken`` set to null. After that the service will return ``NextToken`` values as needed. For example, let\'s say you make a request with ``MaxResults`` set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.
        
        """
        pass

    def merge_developer_identities(self, SourceUserIdentifier: str, DestinationUserIdentifier: str, DeveloperProviderName: str, IdentityPoolId: str) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/MergeDeveloperIdentities>`_
        
        **Request Syntax** 
        ::
        
          response = client.merge_developer_identities(
              SourceUserIdentifier=\'string\',
              DestinationUserIdentifier=\'string\',
              DeveloperProviderName=\'string\',
              IdentityPoolId=\'string\'
          )
        :type SourceUserIdentifier: string
        :param SourceUserIdentifier: **[REQUIRED]** 
        
          User identifier for the source user. The value should be a ``DeveloperUserIdentifier`` .
        
        :type DestinationUserIdentifier: string
        :param DestinationUserIdentifier: **[REQUIRED]** 
        
          User identifier for the destination user. The value should be a ``DeveloperUserIdentifier`` .
        
        :type DeveloperProviderName: string
        :param DeveloperProviderName: **[REQUIRED]** 
        
          The \"domain\" by which Cognito will refer to your users. This is a (pseudo) domain name that you provide while creating an identity pool. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the ``DeveloperProviderName`` , you can use letters as well as period (.), underscore (_), and dash (-).
        
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returned in response to a successful ``MergeDeveloperIdentities`` action.
        
            - **IdentityId** *(string) --* 
        
              A unique identifier in the format REGION:GUID.
        
        """
        pass

    def set_identity_pool_roles(self, IdentityPoolId: str, Roles: Dict, RoleMappings: Dict = None) -> NoReturn:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/SetIdentityPoolRoles>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_identity_pool_roles(
              IdentityPoolId=\'string\',
              Roles={
                  \'string\': \'string\'
              },
              RoleMappings={
                  \'string\': {
                      \'Type\': \'Token\'|\'Rules\',
                      \'AmbiguousRoleResolution\': \'AuthenticatedRole\'|\'Deny\',
                      \'RulesConfiguration\': {
                          \'Rules\': [
                              {
                                  \'Claim\': \'string\',
                                  \'MatchType\': \'Equals\'|\'Contains\'|\'StartsWith\'|\'NotEqual\',
                                  \'Value\': \'string\',
                                  \'RoleARN\': \'string\'
                              },
                          ]
                      }
                  }
              }
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :type Roles: dict
        :param Roles: **[REQUIRED]** 
        
          The map of roles associated with this pool. For a given role, the key will be either \"authenticated\" or \"unauthenticated\" and the value will be the Role ARN.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type RoleMappings: dict
        :param RoleMappings: 
        
          How users for a specific identity provider are to mapped to roles. This is a string to  RoleMapping object map. The string identifies the identity provider, for example, \"graph.facebook.com\" or \"cognito-idp-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id\".
        
          Up to 25 rules can be specified per identity provider.
        
          - *(string) --* 
        
            - *(dict) --* 
        
              A role mapping.
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                The role mapping type. Token will use ``cognito:roles`` and ``cognito:preferred_role`` claims from the Cognito identity provider token to map groups to roles. Rules will attempt to match claims from the token to map to a role.
        
              - **AmbiguousRoleResolution** *(string) --* 
        
                If you specify Token or Rules as the ``Type`` , ``AmbiguousRoleResolution`` is required.
        
                Specifies the action to be taken if either no rules match the claim value for the ``Rules`` type, or there is no ``cognito:preferred_role`` claim and there are multiple ``cognito:roles`` matches for the ``Token`` type.
        
              - **RulesConfiguration** *(dict) --* 
        
                The rules to be used for mapping users to roles.
        
                If you specify Rules as the role mapping type, ``RulesConfiguration`` is required.
        
                - **Rules** *(list) --* **[REQUIRED]** 
        
                  An array of rules. You can specify up to 25 rules per identity provider.
        
                  Rules are evaluated in order. The first one to match specifies the role.
        
                  - *(dict) --* 
        
                    A rule that maps a claim name, a claim value, and a match type to a role ARN.
        
                    - **Claim** *(string) --* **[REQUIRED]** 
        
                      The claim name that must be present in the token, for example, \"isAdmin\" or \"paid\".
        
                    - **MatchType** *(string) --* **[REQUIRED]** 
        
                      The match condition that specifies how closely the claim value in the IdP token must match ``Value`` .
        
                    - **Value** *(string) --* **[REQUIRED]** 
        
                      A brief string that the claim must match, for example, \"paid\" or \"yes\".
        
                    - **RoleARN** *(string) --* **[REQUIRED]** 
        
                      The role ARN.
        
        :returns: None
        """
        pass

    def unlink_developer_identity(self, IdentityId: str, IdentityPoolId: str, DeveloperProviderName: str, DeveloperUserIdentifier: str) -> NoReturn:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/UnlinkDeveloperIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.unlink_developer_identity(
              IdentityId=\'string\',
              IdentityPoolId=\'string\',
              DeveloperProviderName=\'string\',
              DeveloperUserIdentifier=\'string\'
          )
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** 
        
          A unique identifier in the format REGION:GUID.
        
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :type DeveloperProviderName: string
        :param DeveloperProviderName: **[REQUIRED]** 
        
          The \"domain\" by which Cognito will refer to your users.
        
        :type DeveloperUserIdentifier: string
        :param DeveloperUserIdentifier: **[REQUIRED]** 
        
          A unique ID used by your backend authentication process to identify a user.
        
        :returns: None
        """
        pass

    def unlink_identity(self, IdentityId: str, Logins: Dict, LoginsToRemove: List) -> NoReturn:
        """
        
        This is a public API. You do not need any credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/UnlinkIdentity>`_
        
        **Request Syntax** 
        ::
        
          response = client.unlink_identity(
              IdentityId=\'string\',
              Logins={
                  \'string\': \'string\'
              },
              LoginsToRemove=[
                  \'string\',
              ]
          )
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** 
        
          A unique identifier in the format REGION:GUID.
        
        :type Logins: dict
        :param Logins: **[REQUIRED]** 
        
          A set of optional name-value pairs that map provider names to provider tokens.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type LoginsToRemove: list
        :param LoginsToRemove: **[REQUIRED]** 
        
          Provider names to unlink from this identity.
        
          - *(string) --* 
        
        :returns: None
        """
        pass

    def update_identity_pool(self, IdentityPoolId: str, IdentityPoolName: str, AllowUnauthenticatedIdentities: bool, SupportedLoginProviders: Dict = None, DeveloperProviderName: str = None, OpenIdConnectProviderARNs: List = None, CognitoIdentityProviders: List = None, SamlProviderARNs: List = None) -> Dict:
        """
        
        You must use AWS Developer credentials to call this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/UpdateIdentityPool>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_identity_pool(
              IdentityPoolId=\'string\',
              IdentityPoolName=\'string\',
              AllowUnauthenticatedIdentities=True|False,
              SupportedLoginProviders={
                  \'string\': \'string\'
              },
              DeveloperProviderName=\'string\',
              OpenIdConnectProviderARNs=[
                  \'string\',
              ],
              CognitoIdentityProviders=[
                  {
                      \'ProviderName\': \'string\',
                      \'ClientId\': \'string\',
                      \'ServerSideTokenCheck\': True|False
                  },
              ],
              SamlProviderARNs=[
                  \'string\',
              ]
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          An identity pool ID in the format REGION:GUID.
        
        :type IdentityPoolName: string
        :param IdentityPoolName: **[REQUIRED]** 
        
          A string that you provide.
        
        :type AllowUnauthenticatedIdentities: boolean
        :param AllowUnauthenticatedIdentities: **[REQUIRED]** 
        
          TRUE if the identity pool supports unauthenticated logins.
        
        :type SupportedLoginProviders: dict
        :param SupportedLoginProviders: 
        
          Optional key:value pairs mapping provider names to provider app IDs.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type DeveloperProviderName: string
        :param DeveloperProviderName: 
        
          The \"domain\" by which Cognito will refer to your users.
        
        :type OpenIdConnectProviderARNs: list
        :param OpenIdConnectProviderARNs: 
        
          A list of OpendID Connect provider ARNs.
        
          - *(string) --* 
        
        :type CognitoIdentityProviders: list
        :param CognitoIdentityProviders: 
        
          A list representing an Amazon Cognito Identity User Pool and its client ID.
        
          - *(dict) --* 
        
            A provider representing an Amazon Cognito Identity User Pool and its client ID.
        
            - **ProviderName** *(string) --* 
        
              The provider name for an Amazon Cognito Identity User Pool. For example, ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .
        
            - **ClientId** *(string) --* 
        
              The client ID for the Amazon Cognito Identity User Pool.
        
            - **ServerSideTokenCheck** *(boolean) --* 
        
              TRUE if server-side token validation is enabled for the identity provider’s token.
        
        :type SamlProviderARNs: list
        :param SamlProviderARNs: 
        
          An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\',
                \'IdentityPoolName\': \'string\',
                \'AllowUnauthenticatedIdentities\': True|False,
                \'SupportedLoginProviders\': {
                    \'string\': \'string\'
                },
                \'DeveloperProviderName\': \'string\',
                \'OpenIdConnectProviderARNs\': [
                    \'string\',
                ],
                \'CognitoIdentityProviders\': [
                    {
                        \'ProviderName\': \'string\',
                        \'ClientId\': \'string\',
                        \'ServerSideTokenCheck\': True|False
                    },
                ],
                \'SamlProviderARNs\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            An object representing an Amazon Cognito identity pool.
        
            - **IdentityPoolId** *(string) --* 
        
              An identity pool ID in the format REGION:GUID.
        
            - **IdentityPoolName** *(string) --* 
        
              A string that you provide.
        
            - **AllowUnauthenticatedIdentities** *(boolean) --* 
        
              TRUE if the identity pool supports unauthenticated logins.
        
            - **SupportedLoginProviders** *(dict) --* 
        
              Optional key:value pairs mapping provider names to provider app IDs.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **DeveloperProviderName** *(string) --* 
        
              The \"domain\" by which Cognito will refer to your users.
        
            - **OpenIdConnectProviderARNs** *(list) --* 
        
              A list of OpendID Connect provider ARNs.
        
              - *(string) --* 
          
            - **CognitoIdentityProviders** *(list) --* 
        
              A list representing an Amazon Cognito Identity User Pool and its client ID.
        
              - *(dict) --* 
        
                A provider representing an Amazon Cognito Identity User Pool and its client ID.
        
                - **ProviderName** *(string) --* 
        
                  The provider name for an Amazon Cognito Identity User Pool. For example, ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .
        
                - **ClientId** *(string) --* 
        
                  The client ID for the Amazon Cognito Identity User Pool.
        
                - **ServerSideTokenCheck** *(boolean) --* 
        
                  TRUE if server-side token validation is enabled for the identity provider’s token.
        
            - **SamlProviderARNs** *(list) --* 
        
              An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
        
              - *(string) --* 
          
        """
        pass
