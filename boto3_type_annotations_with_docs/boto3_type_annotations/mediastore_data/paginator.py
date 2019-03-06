from typing import Dict
from botocore.paginate import Paginator


class ListItems(Paginator):
    def paginate(self, Path: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MediaStoreData.Client.list_items`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/ListItems>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Path='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'Name': 'string',
                        'Type': 'OBJECT'|'FOLDER',
                        'ETag': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'ContentType': 'string',
                        'ContentLength': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Items** *(list) --* 
              The metadata entries for the folders and objects at the requested path.
              - *(dict) --* 
                A metadata entry for a folder or object.
                - **Name** *(string) --* 
                  The name of the item.
                - **Type** *(string) --* 
                  The item type (folder or object).
                - **ETag** *(string) --* 
                  The ETag that represents a unique instance of the item.
                - **LastModified** *(datetime) --* 
                  The date and time that the item was last modified.
                - **ContentType** *(string) --* 
                  The content type of the item.
                - **ContentLength** *(integer) --* 
                  The length of the item in bytes.
        :type Path: string
        :param Path:
          The path in the container from which to retrieve items. Format: <folder name>/<folder name>/<file name>
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
