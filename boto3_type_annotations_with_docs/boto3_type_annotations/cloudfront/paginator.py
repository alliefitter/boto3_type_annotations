from typing import Dict
from botocore.paginate import Paginator


class ListCloudFrontOriginAccessIdentities(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2018-06-18/ListCloudFrontOriginAccessIdentities>`_
        
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
                \'CloudFrontOriginAccessIdentityList\': {
                    \'Marker\': \'string\',
                    \'NextMarker\': \'string\',
                    \'MaxItems\': 123,
                    \'IsTruncated\': True|False,
                    \'Quantity\': 123,
                    \'Items\': [
                        {
                            \'Id\': \'string\',
                            \'S3CanonicalUserId\': \'string\',
                            \'Comment\': \'string\'
                        },
                    ]
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The returned result of the corresponding request. 
        
            - **CloudFrontOriginAccessIdentityList** *(dict) --* 
        
              The ``CloudFrontOriginAccessIdentityList`` type. 
        
              - **Marker** *(string) --* 
        
                Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the ``Marker`` to the value of the ``NextMarker`` from the current page\'s response (which is also the ID of the last identity on that page). 
        
              - **NextMarker** *(string) --* 
        
                If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use for the ``Marker`` request parameter to continue listing your origin access identities where they left off. 
        
              - **MaxItems** *(integer) --* 
        
                The maximum number of origin access identities you want in the response body. 
        
              - **IsTruncated** *(boolean) --* 
        
                A flag that indicates whether more origin access identities remain to be listed. If your results were truncated, you can make a follow-up pagination request using the ``Marker`` request parameter to retrieve more items in the list.
        
              - **Quantity** *(integer) --* 
        
                The number of CloudFront origin access identities that were created by the current AWS account. 
        
              - **Items** *(list) --* 
        
                A complex type that contains one ``CloudFrontOriginAccessIdentitySummary`` element for each origin access identity that was created by the current AWS account.
        
                - *(dict) --* 
        
                  Summary of the information about a CloudFront origin access identity.
        
                  - **Id** *(string) --* 
        
                    The ID for the origin access identity. For example: ``E74FTE3AJFJ256A`` .
        
                  - **S3CanonicalUserId** *(string) --* 
        
                    The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.
        
                  - **Comment** *(string) --* 
        
                    The comment for this origin access identity, as originally specified when created.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListDistributions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2018-06-18/ListDistributions>`_
        
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
                \'DistributionList\': {
                    \'Marker\': \'string\',
                    \'NextMarker\': \'string\',
                    \'MaxItems\': 123,
                    \'IsTruncated\': True|False,
                    \'Quantity\': 123,
                    \'Items\': [
                        {
                            \'Id\': \'string\',
                            \'ARN\': \'string\',
                            \'Status\': \'string\',
                            \'LastModifiedTime\': datetime(2015, 1, 1),
                            \'DomainName\': \'string\',
                            \'Aliases\': {
                                \'Quantity\': 123,
                                \'Items\': [
                                    \'string\',
                                ]
                            },
                            \'Origins\': {
                                \'Quantity\': 123,
                                \'Items\': [
                                    {
                                        \'Id\': \'string\',
                                        \'DomainName\': \'string\',
                                        \'OriginPath\': \'string\',
                                        \'CustomHeaders\': {
                                            \'Quantity\': 123,
                                            \'Items\': [
                                                {
                                                    \'HeaderName\': \'string\',
                                                    \'HeaderValue\': \'string\'
                                                },
                                            ]
                                        },
                                        \'S3OriginConfig\': {
                                            \'OriginAccessIdentity\': \'string\'
                                        },
                                        \'CustomOriginConfig\': {
                                            \'HTTPPort\': 123,
                                            \'HTTPSPort\': 123,
                                            \'OriginProtocolPolicy\': \'http-only\'|\'match-viewer\'|\'https-only\',
                                            \'OriginSslProtocols\': {
                                                \'Quantity\': 123,
                                                \'Items\': [
                                                    \'SSLv3\'|\'TLSv1\'|\'TLSv1.1\'|\'TLSv1.2\',
                                                ]
                                            },
                                            \'OriginReadTimeout\': 123,
                                            \'OriginKeepaliveTimeout\': 123
                                        }
                                    },
                                ]
                            },
                            \'DefaultCacheBehavior\': {
                                \'TargetOriginId\': \'string\',
                                \'ForwardedValues\': {
                                    \'QueryString\': True|False,
                                    \'Cookies\': {
                                        \'Forward\': \'none\'|\'whitelist\'|\'all\',
                                        \'WhitelistedNames\': {
                                            \'Quantity\': 123,
                                            \'Items\': [
                                                \'string\',
                                            ]
                                        }
                                    },
                                    \'Headers\': {
                                        \'Quantity\': 123,
                                        \'Items\': [
                                            \'string\',
                                        ]
                                    },
                                    \'QueryStringCacheKeys\': {
                                        \'Quantity\': 123,
                                        \'Items\': [
                                            \'string\',
                                        ]
                                    }
                                },
                                \'TrustedSigners\': {
                                    \'Enabled\': True|False,
                                    \'Quantity\': 123,
                                    \'Items\': [
                                        \'string\',
                                    ]
                                },
                                \'ViewerProtocolPolicy\': \'allow-all\'|\'https-only\'|\'redirect-to-https\',
                                \'MinTTL\': 123,
                                \'AllowedMethods\': {
                                    \'Quantity\': 123,
                                    \'Items\': [
                                        \'GET\'|\'HEAD\'|\'POST\'|\'PUT\'|\'PATCH\'|\'OPTIONS\'|\'DELETE\',
                                    ],
                                    \'CachedMethods\': {
                                        \'Quantity\': 123,
                                        \'Items\': [
                                            \'GET\'|\'HEAD\'|\'POST\'|\'PUT\'|\'PATCH\'|\'OPTIONS\'|\'DELETE\',
                                        ]
                                    }
                                },
                                \'SmoothStreaming\': True|False,
                                \'DefaultTTL\': 123,
                                \'MaxTTL\': 123,
                                \'Compress\': True|False,
                                \'LambdaFunctionAssociations\': {
                                    \'Quantity\': 123,
                                    \'Items\': [
                                        {
                                            \'LambdaFunctionARN\': \'string\',
                                            \'EventType\': \'viewer-request\'|\'viewer-response\'|\'origin-request\'|\'origin-response\',
                                            \'IncludeBody\': True|False
                                        },
                                    ]
                                },
                                \'FieldLevelEncryptionId\': \'string\'
                            },
                            \'CacheBehaviors\': {
                                \'Quantity\': 123,
                                \'Items\': [
                                    {
                                        \'PathPattern\': \'string\',
                                        \'TargetOriginId\': \'string\',
                                        \'ForwardedValues\': {
                                            \'QueryString\': True|False,
                                            \'Cookies\': {
                                                \'Forward\': \'none\'|\'whitelist\'|\'all\',
                                                \'WhitelistedNames\': {
                                                    \'Quantity\': 123,
                                                    \'Items\': [
                                                        \'string\',
                                                    ]
                                                }
                                            },
                                            \'Headers\': {
                                                \'Quantity\': 123,
                                                \'Items\': [
                                                    \'string\',
                                                ]
                                            },
                                            \'QueryStringCacheKeys\': {
                                                \'Quantity\': 123,
                                                \'Items\': [
                                                    \'string\',
                                                ]
                                            }
                                        },
                                        \'TrustedSigners\': {
                                            \'Enabled\': True|False,
                                            \'Quantity\': 123,
                                            \'Items\': [
                                                \'string\',
                                            ]
                                        },
                                        \'ViewerProtocolPolicy\': \'allow-all\'|\'https-only\'|\'redirect-to-https\',
                                        \'MinTTL\': 123,
                                        \'AllowedMethods\': {
                                            \'Quantity\': 123,
                                            \'Items\': [
                                                \'GET\'|\'HEAD\'|\'POST\'|\'PUT\'|\'PATCH\'|\'OPTIONS\'|\'DELETE\',
                                            ],
                                            \'CachedMethods\': {
                                                \'Quantity\': 123,
                                                \'Items\': [
                                                    \'GET\'|\'HEAD\'|\'POST\'|\'PUT\'|\'PATCH\'|\'OPTIONS\'|\'DELETE\',
                                                ]
                                            }
                                        },
                                        \'SmoothStreaming\': True|False,
                                        \'DefaultTTL\': 123,
                                        \'MaxTTL\': 123,
                                        \'Compress\': True|False,
                                        \'LambdaFunctionAssociations\': {
                                            \'Quantity\': 123,
                                            \'Items\': [
                                                {
                                                    \'LambdaFunctionARN\': \'string\',
                                                    \'EventType\': \'viewer-request\'|\'viewer-response\'|\'origin-request\'|\'origin-response\',
                                                    \'IncludeBody\': True|False
                                                },
                                            ]
                                        },
                                        \'FieldLevelEncryptionId\': \'string\'
                                    },
                                ]
                            },
                            \'CustomErrorResponses\': {
                                \'Quantity\': 123,
                                \'Items\': [
                                    {
                                        \'ErrorCode\': 123,
                                        \'ResponsePagePath\': \'string\',
                                        \'ResponseCode\': \'string\',
                                        \'ErrorCachingMinTTL\': 123
                                    },
                                ]
                            },
                            \'Comment\': \'string\',
                            \'PriceClass\': \'PriceClass_100\'|\'PriceClass_200\'|\'PriceClass_All\',
                            \'Enabled\': True|False,
                            \'ViewerCertificate\': {
                                \'CloudFrontDefaultCertificate\': True|False,
                                \'IAMCertificateId\': \'string\',
                                \'ACMCertificateArn\': \'string\',
                                \'SSLSupportMethod\': \'sni-only\'|\'vip\',
                                \'MinimumProtocolVersion\': \'SSLv3\'|\'TLSv1\'|\'TLSv1_2016\'|\'TLSv1.1_2016\'|\'TLSv1.2_2018\',
                                \'Certificate\': \'string\',
                                \'CertificateSource\': \'cloudfront\'|\'iam\'|\'acm\'
                            },
                            \'Restrictions\': {
                                \'GeoRestriction\': {
                                    \'RestrictionType\': \'blacklist\'|\'whitelist\'|\'none\',
                                    \'Quantity\': 123,
                                    \'Items\': [
                                        \'string\',
                                    ]
                                }
                            },
                            \'WebACLId\': \'string\',
                            \'HttpVersion\': \'http1.1\'|\'http2\',
                            \'IsIPV6Enabled\': True|False
                        },
                    ]
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The returned result of the corresponding request. 
        
            - **DistributionList** *(dict) --* 
        
              The ``DistributionList`` type. 
        
              - **Marker** *(string) --* 
        
                The value you provided for the ``Marker`` request parameter.
        
              - **NextMarker** *(string) --* 
        
                If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use for the ``Marker`` request parameter to continue listing your distributions where they left off. 
        
              - **MaxItems** *(integer) --* 
        
                The value you provided for the ``MaxItems`` request parameter.
        
              - **IsTruncated** *(boolean) --* 
        
                A flag that indicates whether more distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the ``Marker`` request parameter to retrieve more distributions in the list.
        
              - **Quantity** *(integer) --* 
        
                The number of distributions that were created by the current AWS account. 
        
              - **Items** *(list) --* 
        
                A complex type that contains one ``DistributionSummary`` element for each distribution that was created by the current AWS account.
        
                - *(dict) --* 
        
                  A summary of the information about a CloudFront distribution.
        
                  - **Id** *(string) --* 
        
                    The identifier for the distribution. For example: ``EDFDVBD632BHDS5`` .
        
                  - **ARN** *(string) --* 
        
                    The ARN (Amazon Resource Name) for the distribution. For example: ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012`` is your AWS account ID.
        
                  - **Status** *(string) --* 
        
                    The current status of the distribution. When the status is ``Deployed`` , the distribution\'s information is propagated to all CloudFront edge locations.
        
                  - **LastModifiedTime** *(datetime) --* 
        
                    The date and time the distribution was last modified.
        
                  - **DomainName** *(string) --* 
        
                    The domain name that corresponds to the distribution, for example, ``d111111abcdef8.cloudfront.net`` .
        
                  - **Aliases** *(dict) --* 
        
                    A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
        
                    - **Quantity** *(integer) --* 
        
                      The number of CNAME aliases, if any, that you want to associate with this distribution.
        
                    - **Items** *(list) --* 
        
                      A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
        
                      - *(string) --* 
                  
                  - **Origins** *(dict) --* 
        
                    A complex type that contains information about origins for this distribution.
        
                    - **Quantity** *(integer) --* 
        
                      The number of origins for this distribution.
        
                    - **Items** *(list) --* 
        
                      A complex type that contains origins for this distribution.
        
                      - *(dict) --* 
        
                        A complex type that describes the Amazon S3 bucket or the HTTP server (for example, a web server) from which CloudFront gets your files. You must create at least one origin.
        
                        For the current limit on the number of origins that you can create for a distribution, see `Amazon CloudFront Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__ in the *AWS General Reference* .
        
                        - **Id** *(string) --* 
        
                          A unique identifier for the origin. The value of ``Id`` must be unique within the distribution.
        
                          When you specify the value of ``TargetOriginId`` for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the ``Id`` element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see `Cache Behavior Settings <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **DomainName** *(string) --* 
        
                           **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, ``myawsbucket.s3.amazonaws.com`` . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.
        
                          Constraints for Amazon S3 origins: 
        
                          * If you configured Amazon S3 Transfer Acceleration for your bucket, don\'t specify the ``s3-accelerate`` endpoint for ``DomainName`` . 
                           
                          * The bucket name must be between 3 and 63 characters long (inclusive). 
                           
                          * The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes. 
                           
                          * The bucket name must not contain adjacent periods. 
                           
                           **Custom Origins** : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, ``www.example.com`` . 
        
                          Constraints for custom origins:
        
                          * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters. 
                           
                          * The name cannot exceed 128 characters. 
                           
                        - **OriginPath** *(string) --* 
        
                          An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the ``OriginPath`` element, specify the directory name, beginning with a ``/`` . CloudFront appends the directory name to the value of ``DomainName`` , for example, ``example.com/production`` . Do not include a ``/`` at the end of the directory name.
        
                          For example, suppose you\'ve specified the following values for your distribution:
        
                          * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` . 
                           
                          * ``OriginPath`` : ``/production``   
                           
                          * ``CNAME`` : ``example.com``   
                           
                          When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request to Amazon S3 for ``myawsbucket/production/index.html`` .
        
                          When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .
        
                        - **CustomHeaders** *(dict) --* 
        
                          A complex type that contains names and values for the custom headers that you want.
        
                          - **Quantity** *(integer) --* 
        
                            The number of custom headers, if any, for this distribution.
        
                          - **Items** *(list) --* 
        
                             **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit ``Items`` .
        
                            - *(dict) --* 
        
                              A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for this distribution. 
        
                              - **HeaderName** *(string) --* 
        
                                The name of a header that you want CloudFront to forward to your origin. For more information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__ in the *Amazon Amazon CloudFront Developer Guide* .
        
                              - **HeaderValue** *(string) --* 
        
                                The value for the header that you specified in the ``HeaderName`` field.
        
                        - **S3OriginConfig** *(dict) --* 
        
                          A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the ``CustomOriginConfig`` element instead.
        
                          - **OriginAccessIdentity** *(string) --* 
        
                            The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can *only* access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
        
                            origin-access-identity/cloudfront/*ID-of-origin-access-identity*  
        
                            where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the ``ID`` element when you created the origin access identity.
        
                            If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.
        
                            To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty ``OriginAccessIdentity`` element.
        
                            To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
        
                            For more information about the origin access identity, see `Serving Private Content through CloudFront <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **CustomOriginConfig** *(dict) --* 
        
                          A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the ``S3OriginConfig`` element instead.
        
                          - **HTTPPort** *(integer) --* 
        
                            The HTTP port the custom origin listens on.
        
                          - **HTTPSPort** *(integer) --* 
        
                            The HTTPS port the custom origin listens on.
        
                          - **OriginProtocolPolicy** *(string) --* 
        
                            The origin protocol policy to apply to your origin.
        
                          - **OriginSslProtocols** *(dict) --* 
        
                            The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
        
                            - **Quantity** *(integer) --* 
        
                              The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin. 
        
                            - **Items** *(list) --* 
        
                              A list that contains allowed SSL/TLS protocols for this distribution.
        
                              - *(string) --* 
                          
                          - **OriginReadTimeout** *(integer) --* 
        
                            You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
        
                            If you need to increase the maximum time limit, contact the `AWS Support Center <https://console.aws.amazon.com/support/home#/>`__ .
        
                          - **OriginKeepaliveTimeout** *(integer) --* 
        
                            You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
        
                            If you need to increase the maximum time limit, contact the `AWS Support Center <https://console.aws.amazon.com/support/home#/>`__ .
        
                  - **DefaultCacheBehavior** *(dict) --* 
        
                    A complex type that describes the default cache behavior if you don\'t specify a ``CacheBehavior`` element or if files don\'t match any of the values of ``PathPattern`` in ``CacheBehavior`` elements. You must create exactly one default cache behavior.
        
                    - **TargetOriginId** *(string) --* 
        
                      The value of ``ID`` for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.
        
                    - **ForwardedValues** *(dict) --* 
        
                      A complex type that specifies how CloudFront handles query strings and cookies.
        
                      - **QueryString** *(boolean) --* 
        
                        Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of ``QueryString`` and on the values that you specify for ``QueryStringCacheKeys`` , if any:
        
                        If you specify true for ``QueryString`` and you don\'t specify any values for ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
        
                        If you specify true for ``QueryString`` and you specify one or more values for ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
        
                        If you specify false for ``QueryString`` , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
        
                        For more information, see `Configuring CloudFront to Cache Based on Query String Parameters <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                      - **Cookies** *(dict) --* 
        
                        A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see `How CloudFront Forwards, Caches, and Logs Cookies <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **Forward** *(string) --* 
        
                          Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the ``WhitelistedNames`` complex type.
        
                          Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the ``Forward`` element. 
        
                        - **WhitelistedNames** *(dict) --* 
        
                          Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
        
                          If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` . If you change the value of ``Forward`` from ``whitelist`` to all or none and you don\'t delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them automatically.
        
                          For the current limit on the number of cookie names that you can whitelist for each cache behavior, see `Amazon CloudFront Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__ in the *AWS General Reference* .
        
                          - **Quantity** *(integer) --* 
        
                            The number of different cookies that you want CloudFront to forward to the origin for this cache behavior.
        
                          - **Items** *(list) --* 
        
                            A complex type that contains one ``Name`` element for each cookie that you want CloudFront to forward to the origin for this cache behavior.
        
                            - *(string) --* 
                        
                      - **Headers** *(dict) --* 
        
                        A complex type that specifies the ``Headers`` , if any, that you want CloudFront to base caching on for this cache behavior. 
        
                        - **Quantity** *(integer) --* 
        
                          The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:
        
                          * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for ``Name`` . 
        
                          .. warning::
        
                             CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.  
        
                          * **Forward a whitelist of headers you specify** : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in ``Name`` elements. CloudFront caches your objects based on the values in the specified headers. 
                           
                          * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit ``Items`` . In this configuration, CloudFront doesn\'t cache based on the values in the request headers. 
                           
                          Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:
        
                          * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__   
                           
                          * **Custom origin** : See `HTTP Request Headers and CloudFront Behavior <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-headers-behavior>`__   
                           
                        - **Items** *(list) --* 
        
                          A list that contains one ``Name`` element for each header that you want CloudFront to use for caching in this cache behavior. If ``Quantity`` is ``0`` , omit ``Items`` .
        
                          - *(string) --* 
                      
                      - **QueryStringCacheKeys** *(dict) --* 
        
                        A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
        
                        - **Quantity** *(integer) --* 
        
                          The number of ``whitelisted`` query string parameters for this cache behavior.
        
                        - **Items** *(list) --* 
        
                          (Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If ``Quantity`` is 0, you can omit ``Items`` . 
        
                          - *(string) --* 
                      
                    - **TrustedSigners** *(dict) --* 
        
                      A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
        
                      If you want to require signed URLs in requests for objects in the target origin that match the ``PathPattern`` for this cache behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for ``Quantity`` and ``Items`` . For more information, see `Serving Private Content through CloudFront <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__ in the *Amazon Amazon CloudFront Developer Guide* .
        
                      If you don\'t want to require signed URLs in requests for objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for ``Quantity`` . Omit ``Items`` .
        
                      To add, change, or remove one or more trusted signers, change ``Enabled`` to ``true`` (if it\'s currently ``false`` ), change ``Quantity`` as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
        
                      - **Enabled** *(boolean) --* 
        
                        Specifies whether you want to require viewers to use signed URLs to access the files specified by ``PathPattern`` and ``TargetOriginId`` .
        
                      - **Quantity** *(integer) --* 
        
                        The number of trusted signers for this cache behavior.
        
                      - **Items** *(list) --* 
        
                         **Optional** : A complex type that contains trusted signers for this cache behavior. If ``Quantity`` is ``0`` , you can omit ``Items`` .
        
                        - *(string) --* 
                    
                    - **ViewerProtocolPolicy** *(string) --* 
        
                      The protocol that viewers can use to access the files in the origin specified by ``TargetOriginId`` when a request matches the path pattern in ``PathPattern`` . You can specify the following options:
        
                      * ``allow-all`` : Viewers can use HTTP or HTTPS. 
                       
                      * ``redirect-to-https`` : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL. 
                       
                      * ``https-only`` : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden). 
                       
                      For more information about requiring the HTTPS protocol, see `Using an HTTPS Connection to Access Your Objects <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                      .. note::
        
                        The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see `Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                    - **MinTTL** *(integer) --* 
        
                      The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see `Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html>`__ in the *Amazon Amazon CloudFront Developer Guide* .
        
                      You must specify ``0`` for ``MinTTL`` if you configure CloudFront to forward all headers to your origin (under ``Headers`` , if you specify ``1`` for ``Quantity`` and ``*`` for ``Name`` ).
        
                    - **AllowedMethods** *(dict) --* 
        
                      A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
        
                      * CloudFront forwards only ``GET`` and ``HEAD`` requests. 
                       
                      * CloudFront forwards only ``GET`` , ``HEAD`` , and ``OPTIONS`` requests. 
                       
                      * CloudFront forwards ``GET, HEAD, OPTIONS, PUT, PATCH, POST`` , and ``DELETE`` requests. 
                       
                      If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.
        
                      - **Quantity** *(integer) --* 
        
                        The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for ``GET`` and ``HEAD`` requests), 3 (for ``GET`` , ``HEAD`` , and ``OPTIONS`` requests) and 7 (for ``GET, HEAD, OPTIONS, PUT, PATCH, POST`` , and ``DELETE`` requests).
        
                      - **Items** *(list) --* 
        
                        A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
        
                        - *(string) --* 
                    
                      - **CachedMethods** *(dict) --* 
        
                        A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
        
                        * CloudFront caches responses to ``GET`` and ``HEAD`` requests. 
                         
                        * CloudFront caches responses to ``GET`` , ``HEAD`` , and ``OPTIONS`` requests. 
                         
                        If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly. 
        
                        - **Quantity** *(integer) --* 
        
                          The number of HTTP methods for which you want CloudFront to cache responses. Valid values are ``2`` (for caching responses to ``GET`` and ``HEAD`` requests) and ``3`` (for caching responses to ``GET`` , ``HEAD`` , and ``OPTIONS`` requests).
        
                        - **Items** *(list) --* 
        
                          A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
        
                          - *(string) --* 
                      
                    - **SmoothStreaming** *(boolean) --* 
        
                      Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify ``true`` ; if not, specify ``false`` . If you specify ``true`` for ``SmoothStreaming`` , you can still distribute other content using this cache behavior if the content matches the value of ``PathPattern`` . 
        
                    - **DefaultTTL** *(integer) --* 
        
                      The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as ``Cache-Control max-age`` , ``Cache-Control s-maxage`` , and ``Expires`` to objects. For more information, see `Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                    - **MaxTTL** *(integer) --* 
                    
                    - **Compress** *(boolean) --* 
        
                      Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify ``true`` ; if not, specify ``false`` . For more information, see `Serving Compressed Files <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                    - **LambdaFunctionAssociations** *(dict) --* 
        
                      A complex type that contains zero or more Lambda function associations for a cache behavior.
        
                      - **Quantity** *(integer) --* 
        
                        The number of Lambda function associations for this cache behavior.
        
                      - **Items** *(list) --* 
        
                         **Optional** : A complex type that contains ``LambdaFunctionAssociation`` items for this cache behavior. If ``Quantity`` is ``0`` , you can omit ``Items`` .
        
                        - *(dict) --* 
        
                          A complex type that contains a Lambda function association.
        
                          - **LambdaFunctionARN** *(string) --* 
        
                            The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.
        
                          - **EventType** *(string) --* 
        
                            Specifies the event type that triggers a Lambda function invocation. You can specify the following values:
        
                            * ``viewer-request`` : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.  
                             
                            * ``origin-request`` : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute. 
                             
                            * ``origin-response`` : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute. 
                             
                            * ``viewer-response`` : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute. 
                             
                          - **IncludeBody** *(boolean) --* 
        
                            A flag that allows a Lambda function to have read access to the body content. For more information, see `Accessing the Request Body by Choosing the Include Body Option <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-include-body-access.html>`__ in the Amazon CloudFront Developer Guide.
        
                    - **FieldLevelEncryptionId** *(string) --* 
        
                      The value of ``ID`` for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.
        
                  - **CacheBehaviors** *(dict) --* 
        
                    A complex type that contains zero or more ``CacheBehavior`` elements.
        
                    - **Quantity** *(integer) --* 
        
                      The number of cache behaviors for this distribution. 
        
                    - **Items** *(list) --* 
        
                      Optional: A complex type that contains cache behaviors for this distribution. If ``Quantity`` is ``0`` , you can omit ``Items`` .
        
                      - *(dict) --* 
        
                        A complex type that describes how CloudFront processes requests.
        
                        You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
        
                        For the current limit on the number of cache behaviors that you can add to a distribution, see `Amazon CloudFront Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__ in the *AWS General Reference* .
        
                        If you don\'t want to specify any cache behaviors, include only an empty ``CacheBehaviors`` element. Don\'t include an empty ``CacheBehavior`` element, or CloudFront returns a ``MalformedXML`` error.
        
                        To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty ``CacheBehaviors`` element.
        
                        To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
        
                        For more information about cache behaviors, see `Cache Behaviors <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **PathPattern** *(string) --* 
        
                          The pattern (for example, ``images/*.jpg`` ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.
        
                          .. note::
        
                            You can optionally include a slash (``/`` ) at the beginning of the path pattern. For example, ``/images/*.jpg`` . CloudFront behavior is the same with or without the leading ``/`` .
        
                          The path pattern for the default cache behavior is ``*`` and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
        
                          For more information, see `Path Pattern <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesPathPattern>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **TargetOriginId** *(string) --* 
        
                          The value of ``ID`` for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.
        
                        - **ForwardedValues** *(dict) --* 
        
                          A complex type that specifies how CloudFront handles query strings and cookies.
        
                          - **QueryString** *(boolean) --* 
        
                            Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of ``QueryString`` and on the values that you specify for ``QueryStringCacheKeys`` , if any:
        
                            If you specify true for ``QueryString`` and you don\'t specify any values for ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
        
                            If you specify true for ``QueryString`` and you specify one or more values for ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
        
                            If you specify false for ``QueryString`` , CloudFront doesn\'t forward any query string parameters to the origin, and doesn\'t cache based on query string parameters.
        
                            For more information, see `Configuring CloudFront to Cache Based on Query String Parameters <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                          - **Cookies** *(dict) --* 
        
                            A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see `How CloudFront Forwards, Caches, and Logs Cookies <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                            - **Forward** *(string) --* 
        
                              Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the ``WhitelistedNames`` complex type.
        
                              Amazon S3 doesn\'t process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the ``Forward`` element. 
        
                            - **WhitelistedNames** *(dict) --* 
        
                              Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
        
                              If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` . If you change the value of ``Forward`` from ``whitelist`` to all or none and you don\'t delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them automatically.
        
                              For the current limit on the number of cookie names that you can whitelist for each cache behavior, see `Amazon CloudFront Limits <http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__ in the *AWS General Reference* .
        
                              - **Quantity** *(integer) --* 
        
                                The number of different cookies that you want CloudFront to forward to the origin for this cache behavior.
        
                              - **Items** *(list) --* 
        
                                A complex type that contains one ``Name`` element for each cookie that you want CloudFront to forward to the origin for this cache behavior.
        
                                - *(string) --* 
                            
                          - **Headers** *(dict) --* 
        
                            A complex type that specifies the ``Headers`` , if any, that you want CloudFront to base caching on for this cache behavior. 
        
                            - **Quantity** *(integer) --* 
        
                              The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:
        
                              * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for ``Name`` . 
        
                              .. warning::
        
                                 CloudFront doesn\'t cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.  
        
                              * **Forward a whitelist of headers you specify** : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in ``Name`` elements. CloudFront caches your objects based on the values in the specified headers. 
                               
                              * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit ``Items`` . In this configuration, CloudFront doesn\'t cache based on the values in the request headers. 
                               
                              Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:
        
                              * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__   
                               
                              * **Custom origin** : See `HTTP Request Headers and CloudFront Behavior <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-headers-behavior>`__   
                               
                            - **Items** *(list) --* 
        
                              A list that contains one ``Name`` element for each header that you want CloudFront to use for caching in this cache behavior. If ``Quantity`` is ``0`` , omit ``Items`` .
        
                              - *(string) --* 
                          
                          - **QueryStringCacheKeys** *(dict) --* 
        
                            A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
        
                            - **Quantity** *(integer) --* 
        
                              The number of ``whitelisted`` query string parameters for this cache behavior.
        
                            - **Items** *(list) --* 
        
                              (Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If ``Quantity`` is 0, you can omit ``Items`` . 
        
                              - *(string) --* 
                          
                        - **TrustedSigners** *(dict) --* 
        
                          A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
        
                          If you want to require signed URLs in requests for objects in the target origin that match the ``PathPattern`` for this cache behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for ``Quantity`` and ``Items`` . For more information, see `Serving Private Content through CloudFront <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__ in the *Amazon Amazon CloudFront Developer Guide* .
        
                          If you don\'t want to require signed URLs in requests for objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for ``Quantity`` . Omit ``Items`` .
        
                          To add, change, or remove one or more trusted signers, change ``Enabled`` to ``true`` (if it\'s currently ``false`` ), change ``Quantity`` as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
        
                          - **Enabled** *(boolean) --* 
        
                            Specifies whether you want to require viewers to use signed URLs to access the files specified by ``PathPattern`` and ``TargetOriginId`` .
        
                          - **Quantity** *(integer) --* 
        
                            The number of trusted signers for this cache behavior.
        
                          - **Items** *(list) --* 
        
                             **Optional** : A complex type that contains trusted signers for this cache behavior. If ``Quantity`` is ``0`` , you can omit ``Items`` .
        
                            - *(string) --* 
                        
                        - **ViewerProtocolPolicy** *(string) --* 
        
                          The protocol that viewers can use to access the files in the origin specified by ``TargetOriginId`` when a request matches the path pattern in ``PathPattern`` . You can specify the following options:
        
                          * ``allow-all`` : Viewers can use HTTP or HTTPS. 
                           
                          * ``redirect-to-https`` : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.  
                           
                          * ``https-only`` : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).  
                           
                          For more information about requiring the HTTPS protocol, see `Using an HTTPS Connection to Access Your Objects <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                          .. note::
        
                            The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see `Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **MinTTL** *(integer) --* 
        
                          The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see `Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html>`__ in the *Amazon Amazon CloudFront Developer Guide* .
        
                          You must specify ``0`` for ``MinTTL`` if you configure CloudFront to forward all headers to your origin (under ``Headers`` , if you specify ``1`` for ``Quantity`` and ``*`` for ``Name`` ).
        
                        - **AllowedMethods** *(dict) --* 
        
                          A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
        
                          * CloudFront forwards only ``GET`` and ``HEAD`` requests. 
                           
                          * CloudFront forwards only ``GET`` , ``HEAD`` , and ``OPTIONS`` requests. 
                           
                          * CloudFront forwards ``GET, HEAD, OPTIONS, PUT, PATCH, POST`` , and ``DELETE`` requests. 
                           
                          If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can\'t perform operations that you don\'t want them to. For example, you might not want users to have permissions to delete objects from your origin.
        
                          - **Quantity** *(integer) --* 
        
                            The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for ``GET`` and ``HEAD`` requests), 3 (for ``GET`` , ``HEAD`` , and ``OPTIONS`` requests) and 7 (for ``GET, HEAD, OPTIONS, PUT, PATCH, POST`` , and ``DELETE`` requests).
        
                          - **Items** *(list) --* 
        
                            A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
        
                            - *(string) --* 
                        
                          - **CachedMethods** *(dict) --* 
        
                            A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
        
                            * CloudFront caches responses to ``GET`` and ``HEAD`` requests. 
                             
                            * CloudFront caches responses to ``GET`` , ``HEAD`` , and ``OPTIONS`` requests. 
                             
                            If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly. 
        
                            - **Quantity** *(integer) --* 
        
                              The number of HTTP methods for which you want CloudFront to cache responses. Valid values are ``2`` (for caching responses to ``GET`` and ``HEAD`` requests) and ``3`` (for caching responses to ``GET`` , ``HEAD`` , and ``OPTIONS`` requests).
        
                            - **Items** *(list) --* 
        
                              A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
        
                              - *(string) --* 
                          
                        - **SmoothStreaming** *(boolean) --* 
        
                          Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify ``true`` ; if not, specify ``false`` . If you specify ``true`` for ``SmoothStreaming`` , you can still distribute other content using this cache behavior if the content matches the value of ``PathPattern`` . 
        
                        - **DefaultTTL** *(integer) --* 
        
                          The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as ``Cache-Control max-age`` , ``Cache-Control s-maxage`` , and ``Expires`` to objects. For more information, see `Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **MaxTTL** *(integer) --* 
        
                          The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as ``Cache-Control max-age`` , ``Cache-Control s-maxage`` , and ``Expires`` to objects. For more information, see `Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **Compress** *(boolean) --* 
        
                          Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see `Serving Compressed Files <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **LambdaFunctionAssociations** *(dict) --* 
        
                          A complex type that contains zero or more Lambda function associations for a cache behavior.
        
                          - **Quantity** *(integer) --* 
        
                            The number of Lambda function associations for this cache behavior.
        
                          - **Items** *(list) --* 
        
                             **Optional** : A complex type that contains ``LambdaFunctionAssociation`` items for this cache behavior. If ``Quantity`` is ``0`` , you can omit ``Items`` .
        
                            - *(dict) --* 
        
                              A complex type that contains a Lambda function association.
        
                              - **LambdaFunctionARN** *(string) --* 
        
                                The ARN of the Lambda function. You must specify the ARN of a function version; you can\'t specify a Lambda alias or $LATEST.
        
                              - **EventType** *(string) --* 
        
                                Specifies the event type that triggers a Lambda function invocation. You can specify the following values:
        
                                * ``viewer-request`` : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.  
                                 
                                * ``origin-request`` : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn\'t execute. 
                                 
                                * ``origin-response`` : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn\'t execute. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute. 
                                 
                                * ``viewer-response`` : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn\'t execute. 
                                 
                              - **IncludeBody** *(boolean) --* 
        
                                A flag that allows a Lambda function to have read access to the body content. For more information, see `Accessing the Request Body by Choosing the Include Body Option <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-include-body-access.html>`__ in the Amazon CloudFront Developer Guide.
        
                        - **FieldLevelEncryptionId** *(string) --* 
        
                          The value of ``ID`` for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.
        
                  - **CustomErrorResponses** *(dict) --* 
        
                    A complex type that contains zero or more ``CustomErrorResponses`` elements.
        
                    - **Quantity** *(integer) --* 
        
                      The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If ``Quantity`` is ``0`` , you can omit ``Items`` .
        
                    - **Items** *(list) --* 
        
                      A complex type that contains a ``CustomErrorResponse`` element for each HTTP status code for which you want to specify a custom error page and/or a caching duration. 
        
                      - *(dict) --* 
        
                        A complex type that controls:
        
                        * Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.  
                         
                        * How long CloudFront caches HTTP status codes in the 4xx and 5xx range. 
                         
                        For more information about custom error pages, see `Customizing Error Responses <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                        - **ErrorCode** *(integer) --* 
        
                          The HTTP status code for which you want to specify a custom error page and/or a caching duration.
        
                        - **ResponsePagePath** *(string) --* 
        
                          The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ``ErrorCode`` , for example, ``/4xx-errors/403-forbidden.html`` . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:
        
                          * The value of ``PathPattern`` matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named ``/4xx-errors`` . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, ``/4xx-errors/*`` .  
                           
                          * The value of ``TargetOriginId`` specifies the value of the ``ID`` element for the origin that contains your custom error pages. 
                           
                          If you specify a value for ``ResponsePagePath`` , you must also specify a value for ``ResponseCode`` . If you don\'t want to specify a value, include an empty element, ``<ResponsePagePath>`` , in the XML document.
        
                          We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can\'t get the files that you want to return to viewers because the origin server is unavailable.
        
                        - **ResponseCode** *(string) --* 
        
                          The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:
        
                          * Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute ``200`` , the response typically won\'t be intercepted. 
                           
                          * If you don\'t care about distinguishing among different client errors or server errors, you can specify ``400`` or ``500`` as the ``ResponseCode`` for all 4xx or 5xx errors. 
                           
                          * You might want to return a ``200`` status code (OK) and static website so your customers don\'t know that your website is down. 
                           
                          If you specify a value for ``ResponseCode`` , you must also specify a value for ``ResponsePagePath`` . If you don\'t want to specify a value, include an empty element, ``<ResponseCode>`` , in the XML document.
        
                        - **ErrorCachingMinTTL** *(integer) --* 
        
                          The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ``ErrorCode`` . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
        
                          If you don\'t want to specify a value, include an empty element, ``<ErrorCachingMinTTL>`` , in the XML document.
        
                          For more information, see `Customizing Error Responses <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                  - **Comment** *(string) --* 
        
                    The comment originally specified when this distribution was created.
        
                  - **PriceClass** *(string) --* 
                  
                  - **Enabled** *(boolean) --* 
        
                    Whether the distribution is enabled to accept user requests for content.
        
                  - **ViewerCertificate** *(dict) --* 
        
                    A complex type that specifies the following:
        
                    * Whether you want viewers to use HTTP or HTTPS to request your objects. 
                     
                    * If you want viewers to use HTTPS, whether you\'re using an alternate domain name such as ``example.com`` or the CloudFront domain name for your distribution, such as ``d111111abcdef8.cloudfront.net`` . 
                     
                    * If you\'re using an alternate domain name, whether AWS Certificate Manager (ACM) provided the certificate, or you purchased a certificate from a third-party certificate authority and imported it into ACM or uploaded it to the IAM certificate store. 
                     
                    You must specify only one of the following values: 
        
                    *  ViewerCertificate$ACMCertificateArn   
                     
                    *  ViewerCertificate$IAMCertificateId   
                     
                    *  ViewerCertificate$CloudFrontDefaultCertificate   
                     
                    Don\'t specify ``false`` for ``CloudFrontDefaultCertificate`` .
        
                     **If you want viewers to use HTTP instead of HTTPS to request your objects** : Specify the following value:
        
                     ``<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate>``  
        
                    In addition, specify ``allow-all`` for ``ViewerProtocolPolicy`` for all of your cache behaviors.
        
                     **If you want viewers to use HTTPS to request your objects** : Choose the type of certificate that you want to use based on whether you\'re using an alternate domain name for your objects or the CloudFront domain name:
        
                    * **If you\'re using an alternate domain name, such as example.com** : Specify one of the following values, depending on whether ACM provided your certificate or you purchased your certificate from third-party certificate authority: 
        
                      * ``<ACMCertificateArn>*ARN for ACM SSL/TLS certificate* <ACMCertificateArn>`` where `` *ARN for ACM SSL/TLS certificate* `` is the ARN for the ACM SSL/TLS certificate that you want to use for this distribution. 
                       
                      * ``<IAMCertificateId>*IAM certificate ID* <IAMCertificateId>`` where `` *IAM certificate ID* `` is the ID that IAM returned when you added the certificate to the IAM certificate store. 
                       
                    If you specify ``ACMCertificateArn`` or ``IAMCertificateId`` , you must also specify a value for ``SSLSupportMethod`` .
        
                    If you choose to use an ACM certificate or a certificate in the IAM certificate store, we recommend that you use only an alternate domain name in your object URLs (``https://example.com/logo.jpg`` ). If you use the domain name that is associated with your CloudFront distribution (such as ``https://d111111abcdef8.cloudfront.net/logo.jpg`` ) and the viewer supports ``SNI`` , then CloudFront behaves normally. However, if the browser does not support SNI, the user\'s experience depends on the value that you choose for ``SSLSupportMethod`` :
        
                      * ``vip`` : The viewer displays a warning because there is a mismatch between the CloudFront domain name and the domain name in your SSL/TLS certificate. 
                       
                      * ``sni-only`` : CloudFront drops the connection with the browser without returning the object. 
                       
                    * **If you\'re using the CloudFront domain name for your distribution, such as ``d111111abcdef8.cloudfront.net`` ** : Specify the following value:  ``<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate>``   
                     
                    If you want viewers to use HTTPS, you must also specify one of the following values in your cache behaviors:
        
                    * ``<ViewerProtocolPolicy>https-only<ViewerProtocolPolicy>``   
                     
                    * ``<ViewerProtocolPolicy>redirect-to-https<ViewerProtocolPolicy>``   
                     
                    You can also optionally require that CloudFront use HTTPS to communicate with your origin by specifying one of the following values for the applicable origins:
        
                    * ``<OriginProtocolPolicy>https-only<OriginProtocolPolicy>``   
                     
                    * ``<OriginProtocolPolicy>match-viewer<OriginProtocolPolicy>``   
                     
                    For more information, see `Using Alternate Domain Names and HTTPS <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS>`__ in the *Amazon CloudFront Developer Guide* .
        
                    - **CloudFrontDefaultCertificate** *(boolean) --* 
        
                      For information about how and when to use ``CloudFrontDefaultCertificate`` , see  ViewerCertificate .
        
                    - **IAMCertificateId** *(string) --* 
        
                      For information about how and when to use ``IAMCertificateId`` , see  ViewerCertificate .
        
                    - **ACMCertificateArn** *(string) --* 
        
                      For information about how and when to use ``ACMCertificateArn`` , see  ViewerCertificate .
        
                    - **SSLSupportMethod** *(string) --* 
        
                      If you specify a value for  ViewerCertificate$ACMCertificateArn or for  ViewerCertificate$IAMCertificateId , you must also specify how you want CloudFront to serve HTTPS requests: using a method that works for all clients or one that works for most clients:
        
                      * ``vip`` : CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you will incur additional monthly charges. 
                       
                      * ``sni-only`` : CloudFront can respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don\'t support SNI. If some of your users\' browsers don\'t support SNI, we recommend that you do one of the following: 
        
                        * Use the ``vip`` option (dedicated IP addresses) instead of ``sni-only`` . 
                         
                        * Use the CloudFront SSL/TLS certificate instead of a custom certificate. This requires that you use the CloudFront domain name of your distribution in the URLs for your objects, for example, ``https://d111111abcdef8.cloudfront.net/logo.png`` . 
                         
                        * If you can control which browser your users use, upgrade the browser to one that supports SNI. 
                         
                        * Use HTTP instead of HTTPS. 
                         
                      Don\'t specify a value for ``SSLSupportMethod`` if you specified ``<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate>`` .
        
                      For more information, see `Using Alternate Domain Names and HTTPS <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                    - **MinimumProtocolVersion** *(string) --* 
        
                      Specify the security policy that you want CloudFront to use for HTTPS connections. A security policy determines two settings:
        
                      * The minimum SSL/TLS protocol that CloudFront uses to communicate with viewers 
                       
                      * The cipher that CloudFront uses to encrypt the content that it returns to viewers 
                       
                      .. note::
        
                        On the CloudFront console, this setting is called **Security policy** .
        
                      We recommend that you specify ``TLSv1.1_2016`` unless your users are using browsers or devices that do not support TLSv1.1 or later.
        
                      When both of the following are true, you must specify ``TLSv1`` or later for the security policy: 
        
                      * You\'re using a custom certificate: you specified a value for ``ACMCertificateArn`` or for ``IAMCertificateId``   
                       
                      * You\'re using SNI: you specified ``sni-only`` for ``SSLSupportMethod``   
                       
                      If you specify ``true`` for ``CloudFrontDefaultCertificate`` , CloudFront automatically sets the security policy to ``TLSv1`` regardless of the value that you specify for ``MinimumProtocolVersion`` .
        
                      For information about the relationship between the security policy that you choose and the protocols and ciphers that CloudFront uses to communicate with viewers, see `Supported SSL/TLS Protocols and Ciphers for Communication Between Viewers and CloudFront <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html#secure-connections-supported-ciphers>`__ in the *Amazon CloudFront Developer Guide* .
        
                    - **Certificate** *(string) --* 
        
                      This field has been deprecated. Use one of the following fields instead:
        
                      *  ViewerCertificate$ACMCertificateArn   
                       
                      *  ViewerCertificate$IAMCertificateId   
                       
                      *  ViewerCertificate$CloudFrontDefaultCertificate   
                       
                    - **CertificateSource** *(string) --* 
        
                      This field has been deprecated. Use one of the following fields instead:
        
                      *  ViewerCertificate$ACMCertificateArn   
                       
                      *  ViewerCertificate$IAMCertificateId   
                       
                      *  ViewerCertificate$CloudFrontDefaultCertificate   
                       
                  - **Restrictions** *(dict) --* 
        
                    A complex type that identifies ways in which you want to restrict distribution of your content.
        
                    - **GeoRestriction** *(dict) --* 
        
                      A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using ``MaxMind`` GeoIP databases. 
        
                      - **RestrictionType** *(string) --* 
        
                        The method that you want to use to restrict distribution of your content by country:
        
                        * ``none`` : No geo restriction is enabled, meaning access to content is not restricted by client geo location. 
                         
                        * ``blacklist`` : The ``Location`` elements specify the countries in which you don\'t want CloudFront to distribute your content. 
                         
                        * ``whitelist`` : The ``Location`` elements specify the countries in which you want CloudFront to distribute your content. 
                         
                      - **Quantity** *(integer) --* 
        
                        When geo restriction is ``enabled`` , this is the number of countries in your ``whitelist`` or ``blacklist`` . Otherwise, when it is not enabled, ``Quantity`` is ``0`` , and you can omit ``Items`` .
        
                      - **Items** *(list) --* 
        
                        A complex type that contains a ``Location`` element for each country in which you want CloudFront either to distribute your content (``whitelist`` ) or not distribute your content (``blacklist`` ).
        
                        The ``Location`` element is a two-letter, uppercase country code for a country that you want to include in your ``blacklist`` or ``whitelist`` . Include one ``Location`` element for each country.
        
                        CloudFront and ``MaxMind`` both use ``ISO 3166`` country codes. For the current list of countries and the corresponding codes, see ``ISO 3166-1-alpha-2`` code on the *International Organization for Standardization* website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.
        
                        - *(string) --* 
                    
                  - **WebACLId** *(string) --* 
        
                    The Web ACL Id (if any) associated with the distribution.
        
                  - **HttpVersion** *(string) --* 
        
                    Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is ``http2`` . Viewers that don\'t support ``HTTP/2`` will automatically use an earlier version.
        
                  - **IsIPV6Enabled** *(boolean) --* 
        
                    Whether CloudFront responds to IPv6 DNS requests with an IPv6 address for your distribution.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListInvalidations(Paginator):
    def paginate(self, DistributionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2018-06-18/ListInvalidations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DistributionId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DistributionId: string
        :param DistributionId: **[REQUIRED]** 
        
          The distribution\'s ID.
        
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
                \'InvalidationList\': {
                    \'Marker\': \'string\',
                    \'NextMarker\': \'string\',
                    \'MaxItems\': 123,
                    \'IsTruncated\': True|False,
                    \'Quantity\': 123,
                    \'Items\': [
                        {
                            \'Id\': \'string\',
                            \'CreateTime\': datetime(2015, 1, 1),
                            \'Status\': \'string\'
                        },
                    ]
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The returned result of the corresponding request. 
        
            - **InvalidationList** *(dict) --* 
        
              Information about invalidation batches. 
        
              - **Marker** *(string) --* 
        
                The value that you provided for the ``Marker`` request parameter.
        
              - **NextMarker** *(string) --* 
        
                If ``IsTruncated`` is ``true`` , this element is present and contains the value that you can use for the ``Marker`` request parameter to continue listing your invalidation batches where they left off.
        
              - **MaxItems** *(integer) --* 
        
                The value that you provided for the ``MaxItems`` request parameter.
        
              - **IsTruncated** *(boolean) --* 
        
                A flag that indicates whether more invalidation batch requests remain to be listed. If your results were truncated, you can make a follow-up pagination request using the ``Marker`` request parameter to retrieve more invalidation batches in the list.
        
              - **Quantity** *(integer) --* 
        
                The number of invalidation batches that were created by the current AWS account. 
        
              - **Items** *(list) --* 
        
                A complex type that contains one ``InvalidationSummary`` element for each invalidation batch created by the current AWS account.
        
                - *(dict) --* 
        
                  A summary of an invalidation request.
        
                  - **Id** *(string) --* 
        
                    The unique ID for an invalidation request.
        
                  - **CreateTime** *(datetime) --* 
                  
                  - **Status** *(string) --* 
        
                    The status of an invalidation request.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListStreamingDistributions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2018-06-18/ListStreamingDistributions>`_
        
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
                \'StreamingDistributionList\': {
                    \'Marker\': \'string\',
                    \'NextMarker\': \'string\',
                    \'MaxItems\': 123,
                    \'IsTruncated\': True|False,
                    \'Quantity\': 123,
                    \'Items\': [
                        {
                            \'Id\': \'string\',
                            \'ARN\': \'string\',
                            \'Status\': \'string\',
                            \'LastModifiedTime\': datetime(2015, 1, 1),
                            \'DomainName\': \'string\',
                            \'S3Origin\': {
                                \'DomainName\': \'string\',
                                \'OriginAccessIdentity\': \'string\'
                            },
                            \'Aliases\': {
                                \'Quantity\': 123,
                                \'Items\': [
                                    \'string\',
                                ]
                            },
                            \'TrustedSigners\': {
                                \'Enabled\': True|False,
                                \'Quantity\': 123,
                                \'Items\': [
                                    \'string\',
                                ]
                            },
                            \'Comment\': \'string\',
                            \'PriceClass\': \'PriceClass_100\'|\'PriceClass_200\'|\'PriceClass_All\',
                            \'Enabled\': True|False
                        },
                    ]
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The returned result of the corresponding request. 
        
            - **StreamingDistributionList** *(dict) --* 
        
              The ``StreamingDistributionList`` type. 
        
              - **Marker** *(string) --* 
        
                The value you provided for the ``Marker`` request parameter. 
        
              - **NextMarker** *(string) --* 
        
                If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use for the ``Marker`` request parameter to continue listing your RTMP distributions where they left off. 
        
              - **MaxItems** *(integer) --* 
        
                The value you provided for the ``MaxItems`` request parameter. 
        
              - **IsTruncated** *(boolean) --* 
        
                A flag that indicates whether more streaming distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the ``Marker`` request parameter to retrieve more distributions in the list. 
        
              - **Quantity** *(integer) --* 
        
                The number of streaming distributions that were created by the current AWS account. 
        
              - **Items** *(list) --* 
        
                A complex type that contains one ``StreamingDistributionSummary`` element for each distribution that was created by the current AWS account.
        
                - *(dict) --* 
        
                  A summary of the information for an Amazon CloudFront streaming distribution.
        
                  - **Id** *(string) --* 
        
                    The identifier for the distribution, for example, ``EDFDVBD632BHDS5`` .
        
                  - **ARN** *(string) --* 
        
                    The ARN (Amazon Resource Name) for the streaming distribution. For example: ``arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`` , where ``123456789012`` is your AWS account ID.
        
                  - **Status** *(string) --* 
        
                    Indicates the current status of the distribution. When the status is ``Deployed`` , the distribution\'s information is fully propagated throughout the Amazon CloudFront system.
        
                  - **LastModifiedTime** *(datetime) --* 
        
                    The date and time the distribution was last modified.
        
                  - **DomainName** *(string) --* 
        
                    The domain name corresponding to the distribution, for example, ``d111111abcdef8.cloudfront.net`` .
        
                  - **S3Origin** *(dict) --* 
        
                    A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
        
                    - **DomainName** *(string) --* 
        
                      The DNS name of the Amazon S3 origin. 
        
                    - **OriginAccessIdentity** *(string) --* 
        
                      The CloudFront origin access identity to associate with the RTMP distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
        
                      If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.
        
                      To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty ``OriginAccessIdentity`` element.
        
                      To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
        
                      For more information, see `Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__ in the *Amazon Amazon CloudFront Developer Guide* .
        
                  - **Aliases** *(dict) --* 
        
                    A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
        
                    - **Quantity** *(integer) --* 
        
                      The number of CNAME aliases, if any, that you want to associate with this distribution.
        
                    - **Items** *(list) --* 
        
                      A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
        
                      - *(string) --* 
                  
                  - **TrustedSigners** *(dict) --* 
        
                    A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the ``PathPattern`` for this cache behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for ``Quantity`` and ``Items`` .If you don\'t want to require signed URLs in requests for objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers, change ``Enabled`` to ``true`` (if it\'s currently ``false`` ), change ``Quantity`` as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
        
                    - **Enabled** *(boolean) --* 
        
                      Specifies whether you want to require viewers to use signed URLs to access the files specified by ``PathPattern`` and ``TargetOriginId`` .
        
                    - **Quantity** *(integer) --* 
        
                      The number of trusted signers for this cache behavior.
        
                    - **Items** *(list) --* 
        
                       **Optional** : A complex type that contains trusted signers for this cache behavior. If ``Quantity`` is ``0`` , you can omit ``Items`` .
        
                      - *(string) --* 
                  
                  - **Comment** *(string) --* 
        
                    The comment originally specified when this distribution was created.
        
                  - **PriceClass** *(string) --* 
                  
                  - **Enabled** *(boolean) --* 
        
                    Whether the distribution is enabled to accept end user requests for content.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
