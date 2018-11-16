from typing import Dict
from botocore.paginate import Paginator


class DescribeSchedule(Paginator):
    def paginate(self, ChannelId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeSchedule>`_
        
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
        :param ChannelId: **[REQUIRED]** Id of the channel whose schedule is being updated.
        
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
                \'ScheduleActions\': [
                    {
                        \'ActionName\': \'string\',
                        \'ScheduleActionSettings\': {
                            \'InputSwitchSettings\': {
                                \'InputAttachmentNameReference\': \'string\'
                            },
                            \'Scte35ReturnToNetworkSettings\': {
                                \'SpliceEventId\': 123
                            },
                            \'Scte35SpliceInsertSettings\': {
                                \'Duration\': 123,
                                \'SpliceEventId\': 123
                            },
                            \'Scte35TimeSignalSettings\': {
                                \'Scte35Descriptors\': [
                                    {
                                        \'Scte35DescriptorSettings\': {
                                            \'SegmentationDescriptorScte35DescriptorSettings\': {
                                                \'DeliveryRestrictions\': {
                                                    \'ArchiveAllowedFlag\': \'ARCHIVE_NOT_ALLOWED\'|\'ARCHIVE_ALLOWED\',
                                                    \'DeviceRestrictions\': \'NONE\'|\'RESTRICT_GROUP0\'|\'RESTRICT_GROUP1\'|\'RESTRICT_GROUP2\',
                                                    \'NoRegionalBlackoutFlag\': \'REGIONAL_BLACKOUT\'|\'NO_REGIONAL_BLACKOUT\',
                                                    \'WebDeliveryAllowedFlag\': \'WEB_DELIVERY_NOT_ALLOWED\'|\'WEB_DELIVERY_ALLOWED\'
                                                },
                                                \'SegmentNum\': 123,
                                                \'SegmentationCancelIndicator\': \'SEGMENTATION_EVENT_NOT_CANCELED\'|\'SEGMENTATION_EVENT_CANCELED\',
                                                \'SegmentationDuration\': 123,
                                                \'SegmentationEventId\': 123,
                                                \'SegmentationTypeId\': 123,
                                                \'SegmentationUpid\': \'string\',
                                                \'SegmentationUpidType\': 123,
                                                \'SegmentsExpected\': 123,
                                                \'SubSegmentNum\': 123,
                                                \'SubSegmentsExpected\': 123
                                            }
                                        }
                                    },
                                ]
                            },
                            \'StaticImageActivateSettings\': {
                                \'Duration\': 123,
                                \'FadeIn\': 123,
                                \'FadeOut\': 123,
                                \'Height\': 123,
                                \'Image\': {
                                    \'PasswordParam\': \'string\',
                                    \'Uri\': \'string\',
                                    \'Username\': \'string\'
                                },
                                \'ImageX\': 123,
                                \'ImageY\': 123,
                                \'Layer\': 123,
                                \'Opacity\': 123,
                                \'Width\': 123
                            },
                            \'StaticImageDeactivateSettings\': {
                                \'FadeOut\': 123,
                                \'Layer\': 123
                            }
                        },
                        \'ScheduleActionStartSettings\': {
                            \'FixedModeScheduleActionStartSettings\': {
                                \'Time\': \'string\'
                            },
                            \'FollowModeScheduleActionStartSettings\': {
                                \'FollowPoint\': \'END\'|\'START\',
                                \'ReferenceActionName\': \'string\'
                            }
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* An array of channel schedule actions.
            
            - **ScheduleActions** *(list) --* The list of actions in the schedule.
              
              - *(dict) --* Contains information on a single schedule action.
                
                - **ActionName** *(string) --* The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused.
                
                - **ScheduleActionSettings** *(dict) --* Settings for this schedule action.
                  
                  - **InputSwitchSettings** *(dict) --* Settings to switch an input
                    
                    - **InputAttachmentNameReference** *(string) --* The name of the input attachment that should be switched to by this action.
                
                  - **Scte35ReturnToNetworkSettings** *(dict) --* Settings for SCTE-35 return_to_network message
                    
                    - **SpliceEventId** *(integer) --* The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
                
                  - **Scte35SpliceInsertSettings** *(dict) --* Settings for SCTE-35 splice_insert message
                    
                    - **Duration** *(integer) --* Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time.
                    
                    - **SpliceEventId** *(integer) --* The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
                
                  - **Scte35TimeSignalSettings** *(dict) --* Settings for SCTE-35 time_signal message
                    
                    - **Scte35Descriptors** *(list) --* The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.
                      
                      - *(dict) --* Holds one set of SCTE-35 Descriptor Settings.
                        
                        - **Scte35DescriptorSettings** *(dict) --* SCTE-35 Descriptor Settings.
                          
                          - **SegmentationDescriptorScte35DescriptorSettings** *(dict) --* SCTE-35 Segmentation Descriptor.
                            
                            - **DeliveryRestrictions** *(dict) --* Holds the four SCTE-35 delivery restriction parameters.
                              
                              - **ArchiveAllowedFlag** *(string) --* Corresponds to SCTE-35 archive_allowed_flag.
                              
                              - **DeviceRestrictions** *(string) --* Corresponds to SCTE-35 device_restrictions parameter.
                              
                              - **NoRegionalBlackoutFlag** *(string) --* Corresponds to SCTE-35 no_regional_blackout_flag parameter.
                              
                              - **WebDeliveryAllowedFlag** *(string) --* Corresponds to SCTE-35 web_delivery_allowed_flag parameter.
                          
                            - **SegmentNum** *(integer) --* Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id.
                            
                            - **SegmentationCancelIndicator** *(string) --* Corresponds to SCTE-35 segmentation_event_cancel_indicator.
                            
                            - **SegmentationDuration** *(integer) --* Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message.
                            
                            - **SegmentationEventId** *(integer) --* Corresponds to SCTE-35 segmentation_event_id. 
                            
                            - **SegmentationTypeId** *(integer) --* Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, \"52\"). In the CLI, API, or an SDK, enter the ID in hex (for example, \"0x34\") or decimal (for example, \"52\").
                            
                            - **SegmentationUpid** *(string) --* Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII \"ADS Information\" becomes hex \"41445320496e666f726d6174696f6e.
                            
                            - **SegmentationUpidType** *(integer) --* Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, \"0x0C\" hex from the specification is \"12\" in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, \"0x0C\" ) or in decimal (for example, \"12\").
                            
                            - **SegmentsExpected** *(integer) --* Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id.
                            
                            - **SubSegmentNum** *(integer) --* Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id.
                            
                            - **SubSegmentsExpected** *(integer) --* Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id.
                        
                  - **StaticImageActivateSettings** *(dict) --* Settings to activate a static image overlay
                    
                    - **Duration** *(integer) --* The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.
                    
                    - **FadeIn** *(integer) --* The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).
                    
                    - **FadeOut** *(integer) --* Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).
                    
                    - **Height** *(integer) --* The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.
                    
                    - **Image** *(dict) --* The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.
                      
                      - **PasswordParam** *(string) --* key used to extract the password from EC2 Parameter store
                      
                      - **Uri** *(string) --* Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: \"rtmp://fmsserver/live\".
                      
                      - **Username** *(string) --* Documentation update needed
                  
                    - **ImageX** *(integer) --* Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.
                    
                    - **ImageY** *(integer) --* Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.
                    
                    - **Layer** *(integer) --* The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.
                    
                    - **Opacity** *(integer) --* Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.
                    
                    - **Width** *(integer) --* The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.
                
                  - **StaticImageDeactivateSettings** *(dict) --* Settings to deactivate a static image overlay
                    
                    - **FadeOut** *(integer) --* The time in milliseconds for the image to fade out. Default is 0 (no fade-out).
                    
                    - **Layer** *(integer) --* The image overlay layer to deactivate, 0 to 7. Default is 0.
                
                - **ScheduleActionStartSettings** *(dict) --* The time for the action to start in the channel.
                  
                  - **FixedModeScheduleActionStartSettings** *(dict) --* Holds the start time for the action.
                    
                    - **Time** *(string) --* Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants \"T\" for time and \"Z\" for \"UTC format\".
                
                  - **FollowModeScheduleActionStartSettings** *(dict) --* Specifies an action to follow for scheduling this action.
                    
                    - **FollowPoint** *(string) --* Identifies whether this action starts relative to the start or relative to the end of the reference action.
                    
                    - **ReferenceActionName** *(string) --* The action name of another action that this one refers to.
                
        """
        pass


class ListChannels(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListChannels>`_
        
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
                        \'Destinations\': [
                            {
                                \'Id\': \'string\',
                                \'Settings\': [
                                    {
                                        \'PasswordParam\': \'string\',
                                        \'StreamName\': \'string\',
                                        \'Url\': \'string\',
                                        \'Username\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'EgressEndpoints\': [
                            {
                                \'SourceIp\': \'string\'
                            },
                        ],
                        \'Id\': \'string\',
                        \'InputAttachments\': [
                            {
                                \'InputAttachmentName\': \'string\',
                                \'InputId\': \'string\',
                                \'InputSettings\': {
                                    \'AudioSelectors\': [
                                        {
                                            \'Name\': \'string\',
                                            \'SelectorSettings\': {
                                                \'AudioLanguageSelection\': {
                                                    \'LanguageCode\': \'string\',
                                                    \'LanguageSelectionPolicy\': \'LOOSE\'|\'STRICT\'
                                                },
                                                \'AudioPidSelection\': {
                                                    \'Pid\': 123
                                                }
                                            }
                                        },
                                    ],
                                    \'CaptionSelectors\': [
                                        {
                                            \'LanguageCode\': \'string\',
                                            \'Name\': \'string\',
                                            \'SelectorSettings\': {
                                                \'AribSourceSettings\': {},
                                                \'DvbSubSourceSettings\': {
                                                    \'Pid\': 123
                                                },
                                                \'EmbeddedSourceSettings\': {
                                                    \'Convert608To708\': \'DISABLED\'|\'UPCONVERT\',
                                                    \'Scte20Detection\': \'AUTO\'|\'OFF\',
                                                    \'Source608ChannelNumber\': 123,
                                                    \'Source608TrackNumber\': 123
                                                },
                                                \'Scte20SourceSettings\': {
                                                    \'Convert608To708\': \'DISABLED\'|\'UPCONVERT\',
                                                    \'Source608ChannelNumber\': 123
                                                },
                                                \'Scte27SourceSettings\': {
                                                    \'Pid\': 123
                                                },
                                                \'TeletextSourceSettings\': {
                                                    \'PageNumber\': \'string\'
                                                }
                                            }
                                        },
                                    ],
                                    \'DeblockFilter\': \'DISABLED\'|\'ENABLED\',
                                    \'DenoiseFilter\': \'DISABLED\'|\'ENABLED\',
                                    \'FilterStrength\': 123,
                                    \'InputFilter\': \'AUTO\'|\'DISABLED\'|\'FORCED\',
                                    \'NetworkInputSettings\': {
                                        \'HlsInputSettings\': {
                                            \'Bandwidth\': 123,
                                            \'BufferSegments\': 123,
                                            \'Retries\': 123,
                                            \'RetryInterval\': 123
                                        },
                                        \'ServerValidation\': \'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME\'|\'CHECK_CRYPTOGRAPHY_ONLY\'
                                    },
                                    \'SourceEndBehavior\': \'CONTINUE\'|\'LOOP\',
                                    \'VideoSelector\': {
                                        \'ColorSpace\': \'FOLLOW\'|\'REC_601\'|\'REC_709\',
                                        \'ColorSpaceUsage\': \'FALLBACK\'|\'FORCE\',
                                        \'SelectorSettings\': {
                                            \'VideoSelectorPid\': {
                                                \'Pid\': 123
                                            },
                                            \'VideoSelectorProgramId\': {
                                                \'ProgramId\': 123
                                            }
                                        }
                                    }
                                }
                            },
                        ],
                        \'InputSpecification\': {
                            \'Codec\': \'MPEG2\'|\'AVC\'|\'HEVC\',
                            \'MaximumBitrate\': \'MAX_10_MBPS\'|\'MAX_20_MBPS\'|\'MAX_50_MBPS\',
                            \'Resolution\': \'SD\'|\'HD\'|\'UHD\'
                        },
                        \'LogLevel\': \'ERROR\'|\'WARNING\'|\'INFO\'|\'DEBUG\'|\'DISABLED\',
                        \'Name\': \'string\',
                        \'PipelinesRunningCount\': 123,
                        \'RoleArn\': \'string\',
                        \'State\': \'CREATING\'|\'CREATE_FAILED\'|\'IDLE\'|\'STARTING\'|\'RUNNING\'|\'RECOVERING\'|\'STOPPING\'|\'DELETING\'|\'DELETED\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* An array of channels
            
            - **Channels** *(list) --* Placeholder documentation for __listOfChannelSummary
              
              - *(dict) --* Placeholder documentation for ChannelSummary
                
                - **Arn** *(string) --* The unique arn of the channel.
                
                - **Destinations** *(list) --* A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager. 
                  
                  - *(dict) --* Placeholder documentation for OutputDestination
                    
                    - **Id** *(string) --* User-specified id. This is used in an output group or an output.
                    
                    - **Settings** *(list) --* Destination settings for output; one for each redundant encoder.
                      
                      - *(dict) --* Placeholder documentation for OutputDestinationSettings
                        
                        - **PasswordParam** *(string) --* key used to extract the password from EC2 Parameter store
                        
                        - **StreamName** *(string) --* Stream name for RTMP destinations (URLs of type rtmp://)
                        
                        - **Url** *(string) --* A URL specifying a destination
                        
                        - **Username** *(string) --* username for destination
                    
                - **EgressEndpoints** *(list) --* The endpoints where outgoing connections initiate from
                  
                  - *(dict) --* Placeholder documentation for ChannelEgressEndpoint
                    
                    - **SourceIp** *(string) --* Public IP of where a channel\'s output comes from
                
                - **Id** *(string) --* The unique id of the channel.
                
                - **InputAttachments** *(list) --* List of input attachments for channel.
                  
                  - *(dict) --* Placeholder documentation for InputAttachment
                    
                    - **InputAttachmentName** *(string) --* User-specified name for the attachment. This is required if the user wants to use this input in an input switch action.
                    
                    - **InputId** *(string) --* The ID of the input
                    
                    - **InputSettings** *(dict) --* Settings of an input (caption selector, etc.)
                      
                      - **AudioSelectors** *(list) --* Used to select the audio stream to decode for inputs that have multiple available.
                        
                        - *(dict) --* Placeholder documentation for AudioSelector
                          
                          - **Name** *(string) --* The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input.
                          
                          - **SelectorSettings** *(dict) --* The audio selector settings.
                            
                            - **AudioLanguageSelection** *(dict) --* Placeholder documentation for AudioLanguageSelection
                              
                              - **LanguageCode** *(string) --* Selects a specific three-letter language code from within an audio source.
                              
                              - **LanguageSelectionPolicy** *(string) --* When set to \"strict\", the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If \"loose\", then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can\'t find one with the same language.
                          
                            - **AudioPidSelection** *(dict) --* Placeholder documentation for AudioPidSelection
                              
                              - **Pid** *(integer) --* Selects a specific PID from within a source.
                          
                      - **CaptionSelectors** *(list) --* Used to select the caption input to use for inputs that have multiple available.
                        
                        - *(dict) --* Output groups for this Live Event. Output groups contain information about where streams should be distributed.
                          
                          - **LanguageCode** *(string) --* When specified this field indicates the three letter language code of the caption track to extract from the source.
                          
                          - **Name** *(string) --* Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event.
                          
                          - **SelectorSettings** *(dict) --* Caption selector settings.
                            
                            - **AribSourceSettings** *(dict) --* Placeholder documentation for AribSourceSettings
                          
                            - **DvbSubSourceSettings** *(dict) --* Placeholder documentation for DvbSubSourceSettings
                              
                              - **Pid** *(integer) --* When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
                          
                            - **EmbeddedSourceSettings** *(dict) --* Placeholder documentation for EmbeddedSourceSettings
                              
                              - **Convert608To708** *(string) --* If upconvert, 608 data is both passed through via the \"608 compatibility bytes\" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
                              
                              - **Scte20Detection** *(string) --* Set to \"auto\" to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions.
                              
                              - **Source608ChannelNumber** *(integer) --* Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
                              
                              - **Source608TrackNumber** *(integer) --* This field is unused and deprecated.
                          
                            - **Scte20SourceSettings** *(dict) --* Placeholder documentation for Scte20SourceSettings
                              
                              - **Convert608To708** *(string) --* If upconvert, 608 data is both passed through via the \"608 compatibility bytes\" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
                              
                              - **Source608ChannelNumber** *(integer) --* Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
                          
                            - **Scte27SourceSettings** *(dict) --* Placeholder documentation for Scte27SourceSettings
                              
                              - **Pid** *(integer) --* The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is \"informational\". - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through.
                          
                            - **TeletextSourceSettings** *(dict) --* Placeholder documentation for TeletextSourceSettings
                              
                              - **PageNumber** *(string) --* Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no \"0x\" prefix.
                          
                      - **DeblockFilter** *(string) --* Enable or disable the deblock filter when filtering.
                      
                      - **DenoiseFilter** *(string) --* Enable or disable the denoise filter when filtering.
                      
                      - **FilterStrength** *(integer) --* Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).
                      
                      - **InputFilter** *(string) --* Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type
                      
                      - **NetworkInputSettings** *(dict) --* Input settings.
                        
                        - **HlsInputSettings** *(dict) --* Specifies HLS input settings when the uri is for a HLS manifest.
                          
                          - **Bandwidth** *(integer) --* When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest.
                          
                          - **BufferSegments** *(integer) --* When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8.
                          
                          - **Retries** *(integer) --* The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable.
                          
                          - **RetryInterval** *(integer) --* The number of seconds between retries when an attempt to read a manifest or segment fails.
                      
                        - **ServerValidation** *(string) --* Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server\'s name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate\'s wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https.
                    
                      - **SourceEndBehavior** *(string) --* Loop input if it is a file. This allows a file input to be streamed indefinitely.
                      
                      - **VideoSelector** *(dict) --* Informs which video elementary stream to decode for input types that have multiple available.
                        
                        - **ColorSpace** *(string) --* Specifies the colorspace of an input. This setting works in tandem with colorSpaceConversion to determine if any conversion will be performed.
                        
                        - **ColorSpaceUsage** *(string) --* Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data.
                        
                        - **SelectorSettings** *(dict) --* The video selector settings.
                          
                          - **VideoSelectorPid** *(dict) --* Placeholder documentation for VideoSelectorPid
                            
                            - **Pid** *(integer) --* Selects a specific PID from within a video source.
                        
                          - **VideoSelectorProgramId** *(dict) --* Placeholder documentation for VideoSelectorProgramId
                            
                            - **ProgramId** *(integer) --* Selects a specific program from within a multi-program transport stream. If the program doesn\'t exist, the first program within the transport stream will be selected by default.
                        
                - **InputSpecification** *(dict) --* Placeholder documentation for InputSpecification
                  
                  - **Codec** *(string) --* Input codec
                  
                  - **MaximumBitrate** *(string) --* Maximum input bitrate, categorized coarsely
                  
                  - **Resolution** *(string) --* Input resolution, categorized coarsely
              
                - **LogLevel** *(string) --* The log level being written to CloudWatch Logs.
                
                - **Name** *(string) --* The name of the channel. (user-mutable)
                
                - **PipelinesRunningCount** *(integer) --* The number of currently healthy pipelines.
                
                - **RoleArn** *(string) --* The Amazon Resource Name (ARN) of the role assumed when running the Channel.
                
                - **State** *(string) --* Placeholder documentation for ChannelState
            
        """
        pass


class ListInputSecurityGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListInputSecurityGroups>`_
        
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
                \'InputSecurityGroups\': [
                    {
                        \'Arn\': \'string\',
                        \'Id\': \'string\',
                        \'Inputs\': [
                            \'string\',
                        ],
                        \'State\': \'IDLE\'|\'IN_USE\'|\'UPDATING\'|\'DELETED\',
                        \'WhitelistRules\': [
                            {
                                \'Cidr\': \'string\'
                            },
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* An array of Input Security Groups
            
            - **InputSecurityGroups** *(list) --* List of input security groups
              
              - *(dict) --* An Input Security Group
                
                - **Arn** *(string) --* Unique ARN of Input Security Group
                
                - **Id** *(string) --* The Id of the Input Security Group
                
                - **Inputs** *(list) --* The list of inputs currently using this Input Security Group.
                  
                  - *(string) --* Placeholder documentation for __string
              
                - **State** *(string) --* The current state of the Input Security Group.
                
                - **WhitelistRules** *(list) --* Whitelist rules and their sync status
                  
                  - *(dict) --* Whitelist rule
                    
                    - **Cidr** *(string) --* The IPv4 CIDR that\'s whitelisted.
                
        """
        pass


class ListInputs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListInputs>`_
        
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
                \'Inputs\': [
                    {
                        \'Arn\': \'string\',
                        \'AttachedChannels\': [
                            \'string\',
                        ],
                        \'Destinations\': [
                            {
                                \'Ip\': \'string\',
                                \'Port\': \'string\',
                                \'Url\': \'string\'
                            },
                        ],
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'SecurityGroups\': [
                            \'string\',
                        ],
                        \'Sources\': [
                            {
                                \'PasswordParam\': \'string\',
                                \'Url\': \'string\',
                                \'Username\': \'string\'
                            },
                        ],
                        \'State\': \'CREATING\'|\'DETACHED\'|\'ATTACHED\'|\'DELETING\'|\'DELETED\',
                        \'Type\': \'UDP_PUSH\'|\'RTP_PUSH\'|\'RTMP_PUSH\'|\'RTMP_PULL\'|\'URL_PULL\'|\'MP4_FILE\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* An array of inputs
            
            - **Inputs** *(list) --* Placeholder documentation for __listOfInput
              
              - *(dict) --* Placeholder documentation for Input
                
                - **Arn** *(string) --* The Unique ARN of the input (generated, immutable).
                
                - **AttachedChannels** *(list) --* A list of channel IDs that that input is attached to (currently an input can only be attached to one channel).
                  
                  - *(string) --* Placeholder documentation for __string
              
                - **Destinations** *(list) --* A list of the destinations of the input (PUSH-type).
                  
                  - *(dict) --* The settings for a PUSH type input.
                    
                    - **Ip** *(string) --* The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input. 
                    
                    - **Port** *(string) --* The port number for the input.
                    
                    - **Url** *(string) --* This represents the endpoint that the customer stream will be pushed to. 
                
                - **Id** *(string) --* The generated ID of the input (unique for user account, immutable).
                
                - **Name** *(string) --* The user-assigned name (This is a mutable value).
                
                - **SecurityGroups** *(list) --* A list of IDs for all the security groups attached to the input.
                  
                  - *(string) --* Placeholder documentation for __string
              
                - **Sources** *(list) --* A list of the sources of the input (PULL-type).
                  
                  - *(dict) --* The settings for a PULL type input.
                    
                    - **PasswordParam** *(string) --* The key used to extract the password from EC2 Parameter store.
                    
                    - **Url** *(string) --* This represents the customer\'s source URL where stream is pulled from. 
                    
                    - **Username** *(string) --* The username for the input source.
                
                - **State** *(string) --* Placeholder documentation for InputState
                
                - **Type** *(string) --* Placeholder documentation for InputType
            
        """
        pass


class ListOfferings(Paginator):
    def paginate(self, ChannelConfiguration: str = None, Codec: str = None, MaximumBitrate: str = None, MaximumFramerate: str = None, Resolution: str = None, ResourceType: str = None, SpecialFeature: str = None, VideoQuality: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListOfferings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ChannelConfiguration=\'string\',
              Codec=\'string\',
              MaximumBitrate=\'string\',
              MaximumFramerate=\'string\',
              Resolution=\'string\',
              ResourceType=\'string\',
              SpecialFeature=\'string\',
              VideoQuality=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ChannelConfiguration: string
        :param ChannelConfiguration: Filter to offerings that match the configuration of an existing channel, e.g. \'2345678\' (a channel ID) 
        
        :type Codec: string
        :param Codec: Filter by codec, \'AVC\', \'HEVC\', \'MPEG2\', or \'AUDIO\'
        
        :type MaximumBitrate: string
        :param MaximumBitrate: Filter by bitrate, \'MAX_10_MBPS\', \'MAX_20_MBPS\', or \'MAX_50_MBPS\' 
        
        :type MaximumFramerate: string
        :param MaximumFramerate: Filter by framerate, \'MAX_30_FPS\' or \'MAX_60_FPS\'
        
        :type Resolution: string
        :param Resolution: Filter by resolution, \'SD\', \'HD\', or \'UHD\'
        
        :type ResourceType: string
        :param ResourceType: Filter by resource type, \'INPUT\', \'OUTPUT\', or \'CHANNEL\'
        
        :type SpecialFeature: string
        :param SpecialFeature: Filter by special feature, \'ADVANCED_AUDIO\' or \'AUDIO_NORMALIZATION\' 
        
        :type VideoQuality: string
        :param VideoQuality: Filter by video quality, \'STANDARD\', \'ENHANCED\', or \'PREMIUM\' 
        
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
                \'Offerings\': [
                    {
                        \'Arn\': \'string\',
                        \'CurrencyCode\': \'string\',
                        \'Duration\': 123,
                        \'DurationUnits\': \'MONTHS\',
                        \'FixedPrice\': 123.0,
                        \'OfferingDescription\': \'string\',
                        \'OfferingId\': \'string\',
                        \'OfferingType\': \'NO_UPFRONT\',
                        \'Region\': \'string\',
                        \'ResourceSpecification\': {
                            \'Codec\': \'MPEG2\'|\'AVC\'|\'HEVC\'|\'AUDIO\',
                            \'MaximumBitrate\': \'MAX_10_MBPS\'|\'MAX_20_MBPS\'|\'MAX_50_MBPS\',
                            \'MaximumFramerate\': \'MAX_30_FPS\'|\'MAX_60_FPS\',
                            \'Resolution\': \'SD\'|\'HD\'|\'UHD\',
                            \'ResourceType\': \'INPUT\'|\'OUTPUT\'|\'CHANNEL\',
                            \'SpecialFeature\': \'ADVANCED_AUDIO\'|\'AUDIO_NORMALIZATION\',
                            \'VideoQuality\': \'STANDARD\'|\'ENHANCED\'|\'PREMIUM\'
                        },
                        \'UsagePrice\': 123.0
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* List of offerings
            
            - **Offerings** *(list) --* List of offerings
              
              - *(dict) --* Reserved resources available for purchase
                
                - **Arn** *(string) --* Unique offering ARN, e.g. \'arn:aws:medialive:us-west-2:123456789012:offering:87654321\'
                
                - **CurrencyCode** *(string) --* Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. \'USD\'
                
                - **Duration** *(integer) --* Lease duration, e.g. \'12\'
                
                - **DurationUnits** *(string) --* Units for duration, e.g. \'MONTHS\'
                
                - **FixedPrice** *(float) --* One-time charge for each reserved resource, e.g. \'0.0\' for a NO_UPFRONT offering
                
                - **OfferingDescription** *(string) --* Offering description, e.g. \'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)\'
                
                - **OfferingId** *(string) --* Unique offering ID, e.g. \'87654321\'
                
                - **OfferingType** *(string) --* Offering type, e.g. \'NO_UPFRONT\'
                
                - **Region** *(string) --* AWS region, e.g. \'us-west-2\'
                
                - **ResourceSpecification** *(dict) --* Resource configuration details
                  
                  - **Codec** *(string) --* Codec, e.g. \'AVC\'
                  
                  - **MaximumBitrate** *(string) --* Maximum bitrate, e.g. \'MAX_20_MBPS\'
                  
                  - **MaximumFramerate** *(string) --* Maximum framerate, e.g. \'MAX_30_FPS\' (Outputs only)
                  
                  - **Resolution** *(string) --* Resolution, e.g. \'HD\'
                  
                  - **ResourceType** *(string) --* Resource type, \'INPUT\', \'OUTPUT\', or \'CHANNEL\'
                  
                  - **SpecialFeature** *(string) --* Special feature, e.g. \'AUDIO_NORMALIZATION\' (Channels only)
                  
                  - **VideoQuality** *(string) --* Video quality, e.g. \'STANDARD\' (Outputs only)
              
                - **UsagePrice** *(float) --* Recurring usage charge for each reserved resource, e.g. \'157.0\'
            
        """
        pass


class ListReservations(Paginator):
    def paginate(self, Codec: str = None, MaximumBitrate: str = None, MaximumFramerate: str = None, Resolution: str = None, ResourceType: str = None, SpecialFeature: str = None, VideoQuality: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListReservations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Codec=\'string\',
              MaximumBitrate=\'string\',
              MaximumFramerate=\'string\',
              Resolution=\'string\',
              ResourceType=\'string\',
              SpecialFeature=\'string\',
              VideoQuality=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Codec: string
        :param Codec: Filter by codec, \'AVC\', \'HEVC\', \'MPEG2\', or \'AUDIO\'
        
        :type MaximumBitrate: string
        :param MaximumBitrate: Filter by bitrate, \'MAX_10_MBPS\', \'MAX_20_MBPS\', or \'MAX_50_MBPS\' 
        
        :type MaximumFramerate: string
        :param MaximumFramerate: Filter by framerate, \'MAX_30_FPS\' or \'MAX_60_FPS\'
        
        :type Resolution: string
        :param Resolution: Filter by resolution, \'SD\', \'HD\', or \'UHD\'
        
        :type ResourceType: string
        :param ResourceType: Filter by resource type, \'INPUT\', \'OUTPUT\', or \'CHANNEL\'
        
        :type SpecialFeature: string
        :param SpecialFeature: Filter by special feature, \'ADVANCED_AUDIO\' or \'AUDIO_NORMALIZATION\' 
        
        :type VideoQuality: string
        :param VideoQuality: Filter by video quality, \'STANDARD\', \'ENHANCED\', or \'PREMIUM\' 
        
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
                \'Reservations\': [
                    {
                        \'Arn\': \'string\',
                        \'Count\': 123,
                        \'CurrencyCode\': \'string\',
                        \'Duration\': 123,
                        \'DurationUnits\': \'MONTHS\',
                        \'End\': \'string\',
                        \'FixedPrice\': 123.0,
                        \'Name\': \'string\',
                        \'OfferingDescription\': \'string\',
                        \'OfferingId\': \'string\',
                        \'OfferingType\': \'NO_UPFRONT\',
                        \'Region\': \'string\',
                        \'ReservationId\': \'string\',
                        \'ResourceSpecification\': {
                            \'Codec\': \'MPEG2\'|\'AVC\'|\'HEVC\'|\'AUDIO\',
                            \'MaximumBitrate\': \'MAX_10_MBPS\'|\'MAX_20_MBPS\'|\'MAX_50_MBPS\',
                            \'MaximumFramerate\': \'MAX_30_FPS\'|\'MAX_60_FPS\',
                            \'Resolution\': \'SD\'|\'HD\'|\'UHD\',
                            \'ResourceType\': \'INPUT\'|\'OUTPUT\'|\'CHANNEL\',
                            \'SpecialFeature\': \'ADVANCED_AUDIO\'|\'AUDIO_NORMALIZATION\',
                            \'VideoQuality\': \'STANDARD\'|\'ENHANCED\'|\'PREMIUM\'
                        },
                        \'Start\': \'string\',
                        \'State\': \'ACTIVE\'|\'EXPIRED\'|\'CANCELED\'|\'DELETED\',
                        \'UsagePrice\': 123.0
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* List of reservations
            
            - **Reservations** *(list) --* List of reservations
              
              - *(dict) --* Reserved resources available to use
                
                - **Arn** *(string) --* Unique reservation ARN, e.g. \'arn:aws:medialive:us-west-2:123456789012:reservation:1234567\'
                
                - **Count** *(integer) --* Number of reserved resources
                
                - **CurrencyCode** *(string) --* Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. \'USD\'
                
                - **Duration** *(integer) --* Lease duration, e.g. \'12\'
                
                - **DurationUnits** *(string) --* Units for duration, e.g. \'MONTHS\'
                
                - **End** *(string) --* Reservation UTC end date and time in ISO-8601 format, e.g. \'2019-03-01T00:00:00\'
                
                - **FixedPrice** *(float) --* One-time charge for each reserved resource, e.g. \'0.0\' for a NO_UPFRONT offering
                
                - **Name** *(string) --* User specified reservation name
                
                - **OfferingDescription** *(string) --* Offering description, e.g. \'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)\'
                
                - **OfferingId** *(string) --* Unique offering ID, e.g. \'87654321\'
                
                - **OfferingType** *(string) --* Offering type, e.g. \'NO_UPFRONT\'
                
                - **Region** *(string) --* AWS region, e.g. \'us-west-2\'
                
                - **ReservationId** *(string) --* Unique reservation ID, e.g. \'1234567\'
                
                - **ResourceSpecification** *(dict) --* Resource configuration details
                  
                  - **Codec** *(string) --* Codec, e.g. \'AVC\'
                  
                  - **MaximumBitrate** *(string) --* Maximum bitrate, e.g. \'MAX_20_MBPS\'
                  
                  - **MaximumFramerate** *(string) --* Maximum framerate, e.g. \'MAX_30_FPS\' (Outputs only)
                  
                  - **Resolution** *(string) --* Resolution, e.g. \'HD\'
                  
                  - **ResourceType** *(string) --* Resource type, \'INPUT\', \'OUTPUT\', or \'CHANNEL\'
                  
                  - **SpecialFeature** *(string) --* Special feature, e.g. \'AUDIO_NORMALIZATION\' (Channels only)
                  
                  - **VideoQuality** *(string) --* Video quality, e.g. \'STANDARD\' (Outputs only)
              
                - **Start** *(string) --* Reservation UTC start date and time in ISO-8601 format, e.g. \'2018-03-01T00:00:00\'
                
                - **State** *(string) --* Current state of reservation, e.g. \'ACTIVE\'
                
                - **UsagePrice** *(float) --* Recurring usage charge for each reserved resource, e.g. \'157.0\'
            
        """
        pass
