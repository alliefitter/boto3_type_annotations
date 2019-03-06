from typing import Dict
from botocore.paginate import Paginator


class ListTagsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Route53Resolver.Client.list_tags_for_resource`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53resolver-2018-04-01/ListTagsForResource>`_
        
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
              The tags that are associated with the resource that you specified in the ``ListTagsForResource`` request.
              - *(dict) --* 
                One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name for the tag) and a ``Value`` .
                - **Key** *(string) --* 
                  The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of ``Key`` might be ``account-id`` .
                - **Value** *(string) --* 
                  The value for the tag. For example, if ``Key`` is ``account-id`` , then ``Value`` might be the ID of the customer account that you're creating the resource for.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the resource that you want to list tags for.
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
