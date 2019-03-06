from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAttacks(Paginator):
    def paginate(self, ResourceArns: List = None, StartTime: Dict = None, EndTime: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Shield.Client.list_attacks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/ListAttacks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceArns=[
                  'string',
              ],
              StartTime={
                  'FromInclusive': datetime(2015, 1, 1),
                  'ToExclusive': datetime(2015, 1, 1)
              },
              EndTime={
                  'FromInclusive': datetime(2015, 1, 1),
                  'ToExclusive': datetime(2015, 1, 1)
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
                'AttackSummaries': [
                    {
                        'AttackId': 'string',
                        'ResourceArn': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'AttackVectors': [
                            {
                                'VectorType': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AttackSummaries** *(list) --* 
              The attack information for the specified time range.
              - *(dict) --* 
                Summarizes all DDoS attacks for a specified time period.
                - **AttackId** *(string) --* 
                  The unique identifier (ID) of the attack.
                - **ResourceArn** *(string) --* 
                  The ARN (Amazon Resource Name) of the resource that was attacked.
                - **StartTime** *(datetime) --* 
                  The start time of the attack, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
                - **EndTime** *(datetime) --* 
                  The end time of the attack, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
                - **AttackVectors** *(list) --* 
                  The list of attacks for a specified time period.
                  - *(dict) --* 
                    Describes the attack.
                    - **VectorType** *(string) --* 
                      The attack type. Valid values:
                      * UDP_TRAFFIC 
                      * UDP_FRAGMENT 
                      * GENERIC_UDP_REFLECTION 
                      * DNS_REFLECTION 
                      * NTP_REFLECTION 
                      * CHARGEN_REFLECTION 
                      * SSDP_REFLECTION 
                      * PORT_MAPPER 
                      * RIP_REFLECTION 
                      * SNMP_REFLECTION 
                      * MSSQL_REFLECTION 
                      * NET_BIOS_REFLECTION 
                      * SYN_FLOOD 
                      * ACK_FLOOD 
                      * REQUEST_FLOOD 
        :type ResourceArns: list
        :param ResourceArns:
          The ARN (Amazon Resource Name) of the resource that was attacked. If this is left blank, all applicable resources for this account will be included.
          - *(string) --*
        :type StartTime: dict
        :param StartTime:
          The start of the time period for the attacks. This is a ``timestamp`` type. The sample request above indicates a ``number`` type because the default used by WAF is Unix time in seconds. However any valid `timestamp format <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is allowed.
          - **FromInclusive** *(datetime) --*
            The start time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
          - **ToExclusive** *(datetime) --*
            The end time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
        :type EndTime: dict
        :param EndTime:
          The end of the time period for the attacks. This is a ``timestamp`` type. The sample request above indicates a ``number`` type because the default used by WAF is Unix time in seconds. However any valid `timestamp format <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is allowed.
          - **FromInclusive** *(datetime) --*
            The start time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
          - **ToExclusive** *(datetime) --*
            The end time, in Unix time in seconds. For more information see `timestamp <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
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


class ListProtections(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Shield.Client.list_protections`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/ListProtections>`_
        
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
                'Protections': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'ResourceArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Protections** *(list) --* 
              The array of enabled  Protection objects.
              - *(dict) --* 
                An object that represents a resource that is under DDoS protection.
                - **Id** *(string) --* 
                  The unique identifier (ID) of the protection.
                - **Name** *(string) --* 
                  The friendly name of the protection. For example, ``My CloudFront distributions`` .
                - **ResourceArn** *(string) --* 
                  The ARN (Amazon Resource Name) of the AWS resource that is protected.
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
