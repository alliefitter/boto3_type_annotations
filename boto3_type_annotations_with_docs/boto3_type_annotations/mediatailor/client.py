from typing import Optional
from typing import Union
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
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

    def delete_playback_configuration(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/DeletePlaybackConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_playback_configuration(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The identifier for the configuration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
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

    def get_playback_configuration(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/GetPlaybackConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_playback_configuration(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The identifier for the configuration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AdDecisionServerUrl\': \'string\',
                \'CdnConfiguration\': {
                    \'AdSegmentUrlPrefix\': \'string\',
                    \'ContentSegmentUrlPrefix\': \'string\'
                },
                \'HlsConfiguration\': {
                    \'ManifestEndpointPrefix\': \'string\'
                },
                \'Name\': \'string\',
                \'PlaybackEndpointPrefix\': \'string\',
                \'SessionInitializationEndpointPrefix\': \'string\',
                \'SlateAdUrl\': \'string\',
                \'VideoContentSourceUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AdDecisionServerUrl** *(string) --* 
        
              The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25000 characters.
        
            - **CdnConfiguration** *(dict) --* 
        
              The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management. 
        
              - **AdSegmentUrlPrefix** *(string) --* 
        
                A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
        
              - **ContentSegmentUrlPrefix** *(string) --* 
        
                A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
        
            - **HlsConfiguration** *(dict) --* 
        
              The configuration for HLS content. 
        
              - **ManifestEndpointPrefix** *(string) --* 
        
                The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.
        
            - **Name** *(string) --* 
        
              The identifier for the configuration.
        
            - **PlaybackEndpointPrefix** *(string) --* 
        
              The URL that the player accesses to get a manifest from AWS Elemental MediaTailor. This session will use server-side reporting. 
        
            - **SessionInitializationEndpointPrefix** *(string) --* 
        
              The URL that the player uses to initialize a session that uses client-side reporting. 
        
            - **SlateAdUrl** *(string) --* 
        
              URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because AWS Elemental MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video. 
        
            - **VideoContentSourceUrl** *(string) --* 
        
              The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.
        
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

    def list_playback_configurations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListPlaybackConfigurations>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_playback_configurations(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          Maximum number of records to return. 
        
        :type NextToken: string
        :param NextToken: 
        
          Pagination token returned by the GET list request when results overrun the meximum allowed. Use the token to fetch the next page of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Items\': [
                    {
                        \'AdDecisionServerUrl\': \'string\',
                        \'CdnConfiguration\': {
                            \'AdSegmentUrlPrefix\': \'string\',
                            \'ContentSegmentUrlPrefix\': \'string\'
                        },
                        \'Name\': \'string\',
                        \'SlateAdUrl\': \'string\',
                        \'VideoContentSourceUrl\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Items** *(list) --* 
        
              Array of playback configurations. This may be all of the available configurations or a subset, depending on the settings you provide and on the total number of configurations stored. 
        
              - *(dict) --* 
        
                The AWSMediaTailor configuration.
        
                - **AdDecisionServerUrl** *(string) --* 
        
                  The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25000 characters.
        
                - **CdnConfiguration** *(dict) --* 
        
                  The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management. 
        
                  - **AdSegmentUrlPrefix** *(string) --* 
        
                    A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
        
                  - **ContentSegmentUrlPrefix** *(string) --* 
        
                    A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
        
                - **Name** *(string) --* 
        
                  The identifier for the configuration.
        
                - **SlateAdUrl** *(string) --* 
        
                  URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because AWS Elemental MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video. 
        
                - **VideoContentSourceUrl** *(string) --* 
        
                  The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.
        
            - **NextToken** *(string) --* 
        
              Pagination token returned by the GET list request when results overrun the meximum allowed. Use the token to fetch the next page of results.
        
        """
        pass

    def put_playback_configuration(self, AdDecisionServerUrl: str = None, CdnConfiguration: Dict = None, Name: str = None, SlateAdUrl: str = None, VideoContentSourceUrl: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/PutPlaybackConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_playback_configuration(
              AdDecisionServerUrl=\'string\',
              CdnConfiguration={
                  \'AdSegmentUrlPrefix\': \'string\',
                  \'ContentSegmentUrlPrefix\': \'string\'
              },
              Name=\'string\',
              SlateAdUrl=\'string\',
              VideoContentSourceUrl=\'string\'
          )
        :type AdDecisionServerUrl: string
        :param AdDecisionServerUrl: 
        
          The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25000 characters.
        
        :type CdnConfiguration: dict
        :param CdnConfiguration: 
        
          The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management. 
        
          - **AdSegmentUrlPrefix** *(string) --* 
        
            A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
        
          - **ContentSegmentUrlPrefix** *(string) --* 
        
            A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
        
        :type Name: string
        :param Name: 
        
          The identifier for the configuration.
        
        :type SlateAdUrl: string
        :param SlateAdUrl: 
        
          The URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because AWS Elemental MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video. 
        
        :type VideoContentSourceUrl: string
        :param VideoContentSourceUrl: 
        
          The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AdDecisionServerUrl\': \'string\',
                \'CdnConfiguration\': {
                    \'AdSegmentUrlPrefix\': \'string\',
                    \'ContentSegmentUrlPrefix\': \'string\'
                },
                \'HlsConfiguration\': {
                    \'ManifestEndpointPrefix\': \'string\'
                },
                \'Name\': \'string\',
                \'PlaybackEndpointPrefix\': \'string\',
                \'SessionInitializationEndpointPrefix\': \'string\',
                \'SlateAdUrl\': \'string\',
                \'VideoContentSourceUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AdDecisionServerUrl** *(string) --* 
        
              The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25000 characters.
        
            - **CdnConfiguration** *(dict) --* 
        
              The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management. 
        
              - **AdSegmentUrlPrefix** *(string) --* 
        
                A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
        
              - **ContentSegmentUrlPrefix** *(string) --* 
        
                A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
        
            - **HlsConfiguration** *(dict) --* 
        
              The configuration for HLS content. 
        
              - **ManifestEndpointPrefix** *(string) --* 
        
                The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.
        
            - **Name** *(string) --* 
        
              The identifier for the configuration.
        
            - **PlaybackEndpointPrefix** *(string) --* 
        
              The URL that the player accesses to get a manifest from AWS Elemental MediaTailor. This session will use server-side reporting. 
        
            - **SessionInitializationEndpointPrefix** *(string) --* 
        
              The URL that the player uses to initialize a session that uses client-side reporting. 
        
            - **SlateAdUrl** *(string) --* 
        
              URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because AWS Elemental MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video. 
        
            - **VideoContentSourceUrl** *(string) --* 
        
              The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.
        
        """
        pass
