from typing import Dict
from botocore.paginate import Paginator


class ListChannels(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-2017-10-12/ListChannels>`_
        
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
                \'Channels\': [
                    {
                        \'Arn\': \'string\',
                        \'Description\': \'string\',
                        \'HlsIngest\': {
                            \'IngestEndpoints\': [
                                {
                                    \'Id\': \'string\',
                                    \'Password\': \'string\',
                                    \'Url\': \'string\',
                                    \'Username\': \'string\'
                                },
                            ]
                        },
                        \'Id\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* A collection of Channel records.
            
            - **Channels** *(list) --* A list of Channel records.
              
              - *(dict) --* A Channel resource configuration.
                
                - **Arn** *(string) --* The Amazon Resource Name (ARN) assigned to the Channel.
                
                - **Description** *(string) --* A short text description of the Channel.
                
                - **HlsIngest** *(dict) --* An HTTP Live Streaming (HLS) ingest resource configuration.
                  
                  - **IngestEndpoints** *(list) --* A list of endpoints to which the source stream should be sent.
                    
                    - *(dict) --* An endpoint for ingesting source content for a Channel.
                      
                      - **Id** *(string) --* The system generated unique identifier for the IngestEndpoint
                      
                      - **Password** *(string) --* The system generated password for ingest authentication.
                      
                      - **Url** *(string) --* The ingest URL to which the source stream should be sent.
                      
                      - **Username** *(string) --* The system generated username for ingest authentication.
                  
                - **Id** *(string) --* The ID of the Channel.
            
        """
        pass


class ListOriginEndpoints(Paginator):
    def paginate(self, ChannelId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-2017-10-12/ListOriginEndpoints>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ChannelId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ChannelId: string
        :param ChannelId: When specified, the request will return only OriginEndpoints associated with the given Channel ID.
        
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
                \'OriginEndpoints\': [
                    {
                        \'Arn\': \'string\',
                        \'ChannelId\': \'string\',
                        \'CmafPackage\': {
                            \'Encryption\': {
                                \'KeyRotationIntervalSeconds\': 123,
                                \'SpekeKeyProvider\': {
                                    \'CertificateArn\': \'string\',
                                    \'ResourceId\': \'string\',
                                    \'RoleArn\': \'string\',
                                    \'SystemIds\': [
                                        \'string\',
                                    ],
                                    \'Url\': \'string\'
                                }
                            },
                            \'HlsManifests\': [
                                {
                                    \'AdMarkers\': \'NONE\'|\'SCTE35_ENHANCED\'|\'PASSTHROUGH\',
                                    \'Id\': \'string\',
                                    \'IncludeIframeOnlyStream\': True|False,
                                    \'ManifestName\': \'string\',
                                    \'PlaylistType\': \'NONE\'|\'EVENT\'|\'VOD\',
                                    \'PlaylistWindowSeconds\': 123,
                                    \'ProgramDateTimeIntervalSeconds\': 123,
                                    \'Url\': \'string\'
                                },
                            ],
                            \'SegmentDurationSeconds\': 123,
                            \'SegmentPrefix\': \'string\',
                            \'StreamSelection\': {
                                \'MaxVideoBitsPerSecond\': 123,
                                \'MinVideoBitsPerSecond\': 123,
                                \'StreamOrder\': \'ORIGINAL\'|\'VIDEO_BITRATE_ASCENDING\'|\'VIDEO_BITRATE_DESCENDING\'
                            }
                        },
                        \'DashPackage\': {
                            \'Encryption\': {
                                \'KeyRotationIntervalSeconds\': 123,
                                \'SpekeKeyProvider\': {
                                    \'CertificateArn\': \'string\',
                                    \'ResourceId\': \'string\',
                                    \'RoleArn\': \'string\',
                                    \'SystemIds\': [
                                        \'string\',
                                    ],
                                    \'Url\': \'string\'
                                }
                            },
                            \'ManifestWindowSeconds\': 123,
                            \'MinBufferTimeSeconds\': 123,
                            \'MinUpdatePeriodSeconds\': 123,
                            \'PeriodTriggers\': [
                                \'ADS\',
                            ],
                            \'Profile\': \'NONE\'|\'HBBTV_1_5\',
                            \'SegmentDurationSeconds\': 123,
                            \'StreamSelection\': {
                                \'MaxVideoBitsPerSecond\': 123,
                                \'MinVideoBitsPerSecond\': 123,
                                \'StreamOrder\': \'ORIGINAL\'|\'VIDEO_BITRATE_ASCENDING\'|\'VIDEO_BITRATE_DESCENDING\'
                            },
                            \'SuggestedPresentationDelaySeconds\': 123
                        },
                        \'Description\': \'string\',
                        \'HlsPackage\': {
                            \'AdMarkers\': \'NONE\'|\'SCTE35_ENHANCED\'|\'PASSTHROUGH\',
                            \'Encryption\': {
                                \'ConstantInitializationVector\': \'string\',
                                \'EncryptionMethod\': \'AES_128\'|\'SAMPLE_AES\',
                                \'KeyRotationIntervalSeconds\': 123,
                                \'RepeatExtXKey\': True|False,
                                \'SpekeKeyProvider\': {
                                    \'CertificateArn\': \'string\',
                                    \'ResourceId\': \'string\',
                                    \'RoleArn\': \'string\',
                                    \'SystemIds\': [
                                        \'string\',
                                    ],
                                    \'Url\': \'string\'
                                }
                            },
                            \'IncludeIframeOnlyStream\': True|False,
                            \'PlaylistType\': \'NONE\'|\'EVENT\'|\'VOD\',
                            \'PlaylistWindowSeconds\': 123,
                            \'ProgramDateTimeIntervalSeconds\': 123,
                            \'SegmentDurationSeconds\': 123,
                            \'StreamSelection\': {
                                \'MaxVideoBitsPerSecond\': 123,
                                \'MinVideoBitsPerSecond\': 123,
                                \'StreamOrder\': \'ORIGINAL\'|\'VIDEO_BITRATE_ASCENDING\'|\'VIDEO_BITRATE_DESCENDING\'
                            },
                            \'UseAudioRenditionGroup\': True|False
                        },
                        \'Id\': \'string\',
                        \'ManifestName\': \'string\',
                        \'MssPackage\': {
                            \'Encryption\': {
                                \'SpekeKeyProvider\': {
                                    \'CertificateArn\': \'string\',
                                    \'ResourceId\': \'string\',
                                    \'RoleArn\': \'string\',
                                    \'SystemIds\': [
                                        \'string\',
                                    ],
                                    \'Url\': \'string\'
                                }
                            },
                            \'ManifestWindowSeconds\': 123,
                            \'SegmentDurationSeconds\': 123,
                            \'StreamSelection\': {
                                \'MaxVideoBitsPerSecond\': 123,
                                \'MinVideoBitsPerSecond\': 123,
                                \'StreamOrder\': \'ORIGINAL\'|\'VIDEO_BITRATE_ASCENDING\'|\'VIDEO_BITRATE_DESCENDING\'
                            }
                        },
                        \'StartoverWindowSeconds\': 123,
                        \'TimeDelaySeconds\': 123,
                        \'Url\': \'string\',
                        \'Whitelist\': [
                            \'string\',
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* A collection of OriginEndpoint records.
            
            - **OriginEndpoints** *(list) --* A list of OriginEndpoint records.
              
              - *(dict) --* An OriginEndpoint resource configuration.
                
                - **Arn** *(string) --* The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
                
                - **ChannelId** *(string) --* The ID of the Channel the OriginEndpoint is associated with.
                
                - **CmafPackage** *(dict) --* A Common Media Application Format (CMAF) packaging configuration.
                  
                  - **Encryption** *(dict) --* A Common Media Application Format (CMAF) encryption configuration.
                    
                    - **KeyRotationIntervalSeconds** *(integer) --* Time (in seconds) between each encryption key rotation.
                    
                    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
                      
                      - **CertificateArn** *(string) --* An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service. 
                      
                      - **ResourceId** *(string) --* The resource ID to include in key requests.
                      
                      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service. 
                      
                      - **SystemIds** *(list) --* The system IDs to include in key requests.
                        
                        - *(string) --* 
                    
                      - **Url** *(string) --* The URL of the external key provider service.
                  
                  - **HlsManifests** *(list) --* A list of HLS manifest configurations
                    
                    - *(dict) --* A HTTP Live Streaming (HLS) manifest configuration.
                      
                      - **AdMarkers** *(string) --* This setting controls how ad markers are included in the packaged OriginEndpoint. \"NONE\" will omit all SCTE-35 ad markers from the output. \"PASSTHROUGH\" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. \"SCTE35_ENHANCED\" generates ad markers and blackout tags based on SCTE-35 messages in the input source. 
                      
                      - **Id** *(string) --* The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
                      
                      - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream will be included in the output.
                      
                      - **ManifestName** *(string) --* An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
                      
                      - **PlaylistType** *(string) --* The HTTP Live Streaming (HLS) playlist type. When either \"EVENT\" or \"VOD\" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist. 
                      
                      - **PlaylistWindowSeconds** *(integer) --* Time window (in seconds) contained in each parent manifest.
                      
                      - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output. 
                      
                      - **Url** *(string) --* The URL of the packaged OriginEndpoint for consumption.
                  
                  - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration. 
                  
                  - **SegmentPrefix** *(string) --* An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
                  
                  - **StreamSelection** *(dict) --* A StreamSelection configuration.
                    
                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in output.
                    
                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in output.
                    
                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the output.
                
                - **DashPackage** *(dict) --* A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
                  
                  - **Encryption** *(dict) --* A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
                    
                    - **KeyRotationIntervalSeconds** *(integer) --* Time (in seconds) between each encryption key rotation.
                    
                    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
                      
                      - **CertificateArn** *(string) --* An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service. 
                      
                      - **ResourceId** *(string) --* The resource ID to include in key requests.
                      
                      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service. 
                      
                      - **SystemIds** *(list) --* The system IDs to include in key requests.
                        
                        - *(string) --* 
                    
                      - **Url** *(string) --* The URL of the external key provider service.
                  
                  - **ManifestWindowSeconds** *(integer) --* Time window (in seconds) contained in each manifest.
                  
                  - **MinBufferTimeSeconds** *(integer) --* Minimum duration (in seconds) that a player will buffer media before starting the presentation.
                  
                  - **MinUpdatePeriodSeconds** *(integer) --* Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
                  
                  - **PeriodTriggers** *(list) --* A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains \"ADS\", new periods will be created where the Channel source contains SCTE-35 ad markers. 
                    
                    - *(string) --* 
                
                  - **Profile** *(string) --* The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to \"HBBTV_1_5\", HbbTV 1.5 compliant output is enabled.
                  
                  - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration. 
                  
                  - **StreamSelection** *(dict) --* A StreamSelection configuration.
                    
                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in output.
                    
                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in output.
                    
                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the output.
                
                  - **SuggestedPresentationDelaySeconds** *(integer) --* Duration (in seconds) to delay live content before presentation.
              
                - **Description** *(string) --* A short text description of the OriginEndpoint.
                
                - **HlsPackage** *(dict) --* An HTTP Live Streaming (HLS) packaging configuration.
                  
                  - **AdMarkers** *(string) --* This setting controls how ad markers are included in the packaged OriginEndpoint. \"NONE\" will omit all SCTE-35 ad markers from the output. \"PASSTHROUGH\" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. \"SCTE35_ENHANCED\" generates ad markers and blackout tags based on SCTE-35 messages in the input source. 
                  
                  - **Encryption** *(dict) --* An HTTP Live Streaming (HLS) encryption configuration.
                    
                    - **ConstantInitializationVector** *(string) --* A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated. 
                    
                    - **EncryptionMethod** *(string) --* The encryption method to use.
                    
                    - **KeyRotationIntervalSeconds** *(integer) --* Interval (in seconds) between each encryption key rotation.
                    
                    - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated in output manifests.
                    
                    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
                      
                      - **CertificateArn** *(string) --* An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service. 
                      
                      - **ResourceId** *(string) --* The resource ID to include in key requests.
                      
                      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service. 
                      
                      - **SystemIds** *(list) --* The system IDs to include in key requests.
                        
                        - *(string) --* 
                    
                      - **Url** *(string) --* The URL of the external key provider service.
                  
                  - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream will be included in the output.
                  
                  - **PlaylistType** *(string) --* The HTTP Live Streaming (HLS) playlist type. When either \"EVENT\" or \"VOD\" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist. 
                  
                  - **PlaylistWindowSeconds** *(integer) --* Time window (in seconds) contained in each parent manifest.
                  
                  - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output. 
                  
                  - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration. 
                  
                  - **StreamSelection** *(dict) --* A StreamSelection configuration.
                    
                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in output.
                    
                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in output.
                    
                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the output.
                
                  - **UseAudioRenditionGroup** *(boolean) --* When enabled, audio streams will be placed in rendition groups in the output.
              
                - **Id** *(string) --* The ID of the OriginEndpoint.
                
                - **ManifestName** *(string) --* A short string appended to the end of the OriginEndpoint URL.
                
                - **MssPackage** *(dict) --* A Microsoft Smooth Streaming (MSS) packaging configuration.
                  
                  - **Encryption** *(dict) --* A Microsoft Smooth Streaming (MSS) encryption configuration.
                    
                    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
                      
                      - **CertificateArn** *(string) --* An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service. 
                      
                      - **ResourceId** *(string) --* The resource ID to include in key requests.
                      
                      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service. 
                      
                      - **SystemIds** *(list) --* The system IDs to include in key requests.
                        
                        - *(string) --* 
                    
                      - **Url** *(string) --* The URL of the external key provider service.
                  
                  - **ManifestWindowSeconds** *(integer) --* The time window (in seconds) contained in each manifest.
                  
                  - **SegmentDurationSeconds** *(integer) --* The duration (in seconds) of each segment.
                  
                  - **StreamSelection** *(dict) --* A StreamSelection configuration.
                    
                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in output.
                    
                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in output.
                    
                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the output.
                
                - **StartoverWindowSeconds** *(integer) --* Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint. 
                
                - **TimeDelaySeconds** *(integer) --* Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint. 
                
                - **Url** *(string) --* The URL of the packaged OriginEndpoint for consumption.
                
                - **Whitelist** *(list) --* A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
                  
                  - *(string) --* 
              
        """
        pass
