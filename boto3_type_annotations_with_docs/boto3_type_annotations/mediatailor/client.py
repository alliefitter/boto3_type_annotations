from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


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

    def delete_playback_configuration(self, Name: str) -> Dict:
        """
        Deletes the playback configuration for the specified name. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/DeletePlaybackConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_playback_configuration(
              Name='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The request was successful and there is no content in the response. 
        :type Name: string
        :param Name: **[REQUIRED]**
          The identifier for the playback configuration.
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

    def get_playback_configuration(self, Name: str) -> Dict:
        """
        Returns the playback configuration for the specified name. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/GetPlaybackConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_playback_configuration(
              Name='string'
          )
        
        **Response Syntax**
        ::
            {
                'AdDecisionServerUrl': 'string',
                'CdnConfiguration': {
                    'AdSegmentUrlPrefix': 'string',
                    'ContentSegmentUrlPrefix': 'string'
                },
                'DashConfiguration': {
                    'ManifestEndpointPrefix': 'string',
                    'MpdLocation': 'string',
                    'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
                },
                'HlsConfiguration': {
                    'ManifestEndpointPrefix': 'string'
                },
                'Name': 'string',
                'PlaybackConfigurationArn': 'string',
                'PlaybackEndpointPrefix': 'string',
                'SessionInitializationEndpointPrefix': 'string',
                'SlateAdUrl': 'string',
                'Tags': {
                    'string': 'string'
                },
                'TranscodeProfileName': 'string',
                'VideoContentSourceUrl': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success.
            - **AdDecisionServerUrl** *(string) --* 
              The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
            - **CdnConfiguration** *(dict) --* 
              The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management. 
              - **AdSegmentUrlPrefix** *(string) --* 
                A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
              - **ContentSegmentUrlPrefix** *(string) --* 
                A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
            - **DashConfiguration** *(dict) --* 
              The configuration for DASH content. 
              - **ManifestEndpointPrefix** *(string) --* 
                The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations. 
              - **MpdLocation** *(string) --* 
                The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value. 
              - **OriginManifestType** *(string) --* 
                The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD. 
            - **HlsConfiguration** *(dict) --* 
              The configuration for HLS content. 
              - **ManifestEndpointPrefix** *(string) --* 
                The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.
            - **Name** *(string) --* 
              The identifier for the playback configuration.
            - **PlaybackConfigurationArn** *(string) --* 
              The Amazon Resource Name (ARN) for the playback configuration. 
            - **PlaybackEndpointPrefix** *(string) --* 
              The URL that the player accesses to get a manifest from AWS Elemental MediaTailor. This session will use server-side reporting. 
            - **SessionInitializationEndpointPrefix** *(string) --* 
              The URL that the player uses to initialize a session that uses client-side reporting. 
            - **SlateAdUrl** *(string) --* 
              The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video. 
            - **Tags** *(dict) --* 
              The tags assigned to the playback configuration. 
              - *(string) --* 
                - *(string) --* 
            - **TranscodeProfileName** *(string) --* 
              The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
            - **VideoContentSourceUrl** *(string) --* 
              The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.
        :type Name: string
        :param Name: **[REQUIRED]**
          The identifier for the playback configuration.
        :rtype: dict
        :returns:
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

    def list_playback_configurations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of the playback configurations defined in AWS Elemental MediaTailor. You can specify a maximum number of configurations to return at a time. The default maximum is 50. Results are returned in pagefuls. If MediaTailor has more configurations than the specified maximum, it provides parameters in the response that you can use to retrieve the next pageful. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListPlaybackConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.list_playback_configurations(
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'AdDecisionServerUrl': 'string',
                        'CdnConfiguration': {
                            'AdSegmentUrlPrefix': 'string',
                            'ContentSegmentUrlPrefix': 'string'
                        },
                        'DashConfiguration': {
                            'ManifestEndpointPrefix': 'string',
                            'MpdLocation': 'string',
                            'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
                        },
                        'HlsConfiguration': {
                            'ManifestEndpointPrefix': 'string'
                        },
                        'Name': 'string',
                        'PlaybackConfigurationArn': 'string',
                        'PlaybackEndpointPrefix': 'string',
                        'SessionInitializationEndpointPrefix': 'string',
                        'SlateAdUrl': 'string',
                        'Tags': {
                            'string': 'string'
                        },
                        'TranscodeProfileName': 'string',
                        'VideoContentSourceUrl': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success.
            - **Items** *(list) --* 
              Array of playback configurations. This might be all the available configurations or a subset, depending on the settings that you provide and the total number of configurations stored. 
              - *(dict) --* 
                The AWSMediaTailor configuration.
                - **AdDecisionServerUrl** *(string) --* 
                  The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
                - **CdnConfiguration** *(dict) --* 
                  The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management. 
                  - **AdSegmentUrlPrefix** *(string) --* 
                    A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
                  - **ContentSegmentUrlPrefix** *(string) --* 
                    A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
                - **DashConfiguration** *(dict) --* 
                  The configuration for DASH content. 
                  - **ManifestEndpointPrefix** *(string) --* 
                    The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations. 
                  - **MpdLocation** *(string) --* 
                    The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value. 
                  - **OriginManifestType** *(string) --* 
                    The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD. 
                - **HlsConfiguration** *(dict) --* 
                  The configuration for HLS content. 
                  - **ManifestEndpointPrefix** *(string) --* 
                    The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.
                - **Name** *(string) --* 
                  The identifier for the playback configuration.
                - **PlaybackConfigurationArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the playback configuration. 
                - **PlaybackEndpointPrefix** *(string) --* 
                  The URL that the player accesses to get a manifest from AWS Elemental MediaTailor. This session will use server-side reporting. 
                - **SessionInitializationEndpointPrefix** *(string) --* 
                  The URL that the player uses to initialize a session that uses client-side reporting. 
                - **SlateAdUrl** *(string) --* 
                  The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video. 
                - **Tags** *(dict) --* 
                  The tags assigned to the playback configuration. 
                  - *(string) --* 
                    - *(string) --* 
                - **TranscodeProfileName** *(string) --* 
                  The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
                - **VideoContentSourceUrl** *(string) --* 
                  The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.
            - **NextToken** *(string) --* 
              Pagination token returned by the GET list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
        :type MaxResults: integer
        :param MaxResults:
          Maximum number of records to return.
        :type NextToken: string
        :param NextToken:
          Pagination token returned by the GET list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        """
        Returns a list of the tags assigned to the specified playback configuration resource. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Success. 
            - **Tags** *(dict) --* 
              A comma-separated list of tag key:value pairs. For example: { "Key1": "Value1", "Key2": "Value2" } 
              - *(string) --* 
                - *(string) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the playback configuration. You can get this from the response to any playback configuration request.
        :rtype: dict
        :returns:
        """
        pass

    def put_playback_configuration(self, AdDecisionServerUrl: str = None, CdnConfiguration: Dict = None, DashConfiguration: Dict = None, Name: str = None, SlateAdUrl: str = None, Tags: Dict = None, TranscodeProfileName: str = None, VideoContentSourceUrl: str = None) -> Dict:
        """
        Adds a new playback configuration to AWS Elemental MediaTailor. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/PutPlaybackConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_playback_configuration(
              AdDecisionServerUrl='string',
              CdnConfiguration={
                  'AdSegmentUrlPrefix': 'string',
                  'ContentSegmentUrlPrefix': 'string'
              },
              DashConfiguration={
                  'MpdLocation': 'string',
                  'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
              },
              Name='string',
              SlateAdUrl='string',
              Tags={
                  'string': 'string'
              },
              TranscodeProfileName='string',
              VideoContentSourceUrl='string'
          )
        
        **Response Syntax**
        ::
            {
                'AdDecisionServerUrl': 'string',
                'CdnConfiguration': {
                    'AdSegmentUrlPrefix': 'string',
                    'ContentSegmentUrlPrefix': 'string'
                },
                'DashConfiguration': {
                    'ManifestEndpointPrefix': 'string',
                    'MpdLocation': 'string',
                    'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
                },
                'HlsConfiguration': {
                    'ManifestEndpointPrefix': 'string'
                },
                'Name': 'string',
                'PlaybackConfigurationArn': 'string',
                'PlaybackEndpointPrefix': 'string',
                'SessionInitializationEndpointPrefix': 'string',
                'SlateAdUrl': 'string',
                'Tags': {
                    'string': 'string'
                },
                'TranscodeProfileName': 'string',
                'VideoContentSourceUrl': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success.
            - **AdDecisionServerUrl** *(string) --* 
              The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
            - **CdnConfiguration** *(dict) --* 
              The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management. 
              - **AdSegmentUrlPrefix** *(string) --* 
                A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
              - **ContentSegmentUrlPrefix** *(string) --* 
                A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
            - **DashConfiguration** *(dict) --* 
              The configuration for DASH content. 
              - **ManifestEndpointPrefix** *(string) --* 
                The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations. 
              - **MpdLocation** *(string) --* 
                The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value. 
              - **OriginManifestType** *(string) --* 
                The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD. 
            - **HlsConfiguration** *(dict) --* 
              The configuration for HLS content. 
              - **ManifestEndpointPrefix** *(string) --* 
                The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.
            - **Name** *(string) --* 
              The identifier for the playback configuration.
            - **PlaybackConfigurationArn** *(string) --* 
              The Amazon Resource Name (ARN) for the playback configuration. 
            - **PlaybackEndpointPrefix** *(string) --* 
              The URL that the player accesses to get a manifest from AWS Elemental MediaTailor. This session will use server-side reporting. 
            - **SessionInitializationEndpointPrefix** *(string) --* 
              The URL that the player uses to initialize a session that uses client-side reporting. 
            - **SlateAdUrl** *(string) --* 
              The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video. 
            - **Tags** *(dict) --* 
              The tags assigned to the playback configuration. 
              - *(string) --* 
                - *(string) --* 
            - **TranscodeProfileName** *(string) --* 
              The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
            - **VideoContentSourceUrl** *(string) --* 
              The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.
        :type AdDecisionServerUrl: string
        :param AdDecisionServerUrl:
          The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
        :type CdnConfiguration: dict
        :param CdnConfiguration:
          The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
          - **AdSegmentUrlPrefix** *(string) --*
            A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
          - **ContentSegmentUrlPrefix** *(string) --*
            A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
        :type DashConfiguration: dict
        :param DashConfiguration:
          The configuration for DASH content.
          - **MpdLocation** *(string) --*
            The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don\'t support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.
          - **OriginManifestType** *(string) --*
            The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD.
        :type Name: string
        :param Name:
          The identifier for the playback configuration.
        :type SlateAdUrl: string
        :param SlateAdUrl:
          The URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
        :type Tags: dict
        :param Tags:
          The tags to assign to the playback configuration.
          - *(string) --*
            - *(string) --*
        :type TranscodeProfileName: string
        :param TranscodeProfileName:
          The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
        :type VideoContentSourceUrl: string
        :param VideoContentSourceUrl:
          The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict):
        """
        Adds tags to the specified playback configuration resource. You can specify one or more tags to add. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              ResourceArn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the playback configuration. You can get this from the response to any playback configuration request.
        :type Tags: dict
        :param Tags: **[REQUIRED]**
          A comma-separated list of tag key:value pairs. For example: { \"Key1\": \"Value1\", \"Key2\": \"Value2\" }
          - *(string) --*
            - *(string) --*
        :returns: None
        """
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List):
        """
        Removes tags from the specified playback configuration resource. You can specify one or more tags to remove. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the playback configuration. You can get this from the response to any playback configuration request.
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          A comma-separated list of the tag keys to remove from the playback configuration.
          - *(string) --*
        :returns: None
        """
        pass
