from typing import Dict
from botocore.paginate import Paginator


class ListFragments(Paginator):
    def paginate(self, StreamName: str, FragmentSelector: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`KinesisVideoArchivedMedia.Client.list_fragments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/ListFragments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StreamName='string',
              FragmentSelector={
                  'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
                  'TimestampRange': {
                      'StartTimestamp': datetime(2015, 1, 1),
                      'EndTimestamp': datetime(2015, 1, 1)
                  }
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
                'Fragments': [
                    {
                        'FragmentNumber': 'string',
                        'FragmentSizeInBytes': 123,
                        'ProducerTimestamp': datetime(2015, 1, 1),
                        'ServerTimestamp': datetime(2015, 1, 1),
                        'FragmentLengthInMilliseconds': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Fragments** *(list) --* 
              A list of archived  Fragment objects from the stream that meet the selector criteria. Results are in no specific order, even across pages.
              - *(dict) --* 
                Represents a segment of video or other time-delimited data.
                - **FragmentNumber** *(string) --* 
                  The index value of the fragment.
                - **FragmentSizeInBytes** *(integer) --* 
                  The total fragment size, including information about the fragment and contained media data.
                - **ProducerTimestamp** *(datetime) --* 
                  The timestamp from the producer corresponding to the fragment.
                - **ServerTimestamp** *(datetime) --* 
                  The timestamp from the AWS server corresponding to the fragment.
                - **FragmentLengthInMilliseconds** *(integer) --* 
                  The playback duration or other time value associated with the fragment.
        :type StreamName: string
        :param StreamName: **[REQUIRED]**
          The name of the stream from which to retrieve a fragment list.
        :type FragmentSelector: dict
        :param FragmentSelector:
          Describes the timestamp range and timestamp origin for the range of fragments to return.
          - **FragmentSelectorType** *(string) --* **[REQUIRED]**
            The origin of the timestamps to use (Server or Producer).
          - **TimestampRange** *(dict) --* **[REQUIRED]**
            The range of timestamps to return.
            - **StartTimestamp** *(datetime) --* **[REQUIRED]**
              The starting timestamp in the range of timestamps for which to return fragments.
            - **EndTimestamp** *(datetime) --* **[REQUIRED]**
              The ending timestamp in the range of timestamps for which to return fragments.
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
