from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class DBInstanceAvailable(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBInstances>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              DBInstanceIdentifier=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: 
        
          The user-supplied instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn\'t case-sensitive.
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBInstance. 
           
        :type Filters: list
        :param Filters: 
        
          A filter that specifies one or more DB instances to describe.
        
          Supported filters:
        
          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs. 
           
          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs). The results list will only include information about the DB instances identified by these ARNs. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBInstances`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass


class DBInstanceDeleted(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBInstances>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              DBInstanceIdentifier=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: 
        
          The user-supplied instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn\'t case-sensitive.
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBInstance. 
           
        :type Filters: list
        :param Filters: 
        
          A filter that specifies one or more DB instances to describe.
        
          Supported filters:
        
          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs. 
           
          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs). The results list will only include information about the DB instances identified by these ARNs. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBInstances`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass


class DBSnapshotAvailable(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshots>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              DBInstanceIdentifier=\'string\',
              DBSnapshotIdentifier=\'string\',
              SnapshotType=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\',
              IncludeShared=True|False,
              IncludePublic=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: 
        
          The ID of the DB instance to retrieve the list of DB snapshots for. This parameter can\'t be used in conjunction with ``DBSnapshotIdentifier`` . This parameter is not case-sensitive. 
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBInstance. 
           
        :type DBSnapshotIdentifier: string
        :param DBSnapshotIdentifier: 
        
          A specific DB snapshot identifier to describe. This parameter can\'t be used in conjunction with ``DBInstanceIdentifier`` . This value is stored as a lowercase string. 
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBSnapshot. 
           
          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be specified. 
           
        :type SnapshotType: string
        :param SnapshotType: 
        
          The type of snapshots to be returned. You can specify one of the following values:
        
          * ``automated`` - Return all DB snapshots that have been automatically taken by Amazon RDS for my AWS account. 
           
          * ``manual`` - Return all DB snapshots that have been taken by my AWS account. 
           
          * ``shared`` - Return all manual DB snapshots that have been shared to my AWS account. 
           
          * ``public`` - Return all DB snapshots that have been marked as public. 
           
          If you don\'t specify a ``SnapshotType`` value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not included in the returned results by default. You can include shared snapshots with these results by setting the ``IncludeShared`` parameter to ``true`` . You can include public snapshots with these results by setting the ``IncludePublic`` parameter to ``true`` .
        
          The ``IncludeShared`` and ``IncludePublic`` parameters don\'t apply for ``SnapshotType`` values of ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn\'t apply when ``SnapshotType`` is set to ``shared`` . The ``IncludeShared`` parameter doesn\'t apply when ``SnapshotType`` is set to ``public`` .
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBSnapshots`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :type IncludeShared: boolean
        :param IncludeShared: 
        
          True to include shared manual DB snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false. The default is ``false`` .
        
          You can give an AWS account permission to restore a manual DB snapshot from another AWS account by using the  ModifyDBSnapshotAttribute API action.
        
        :type IncludePublic: boolean
        :param IncludePublic: 
        
          True to include manual DB snapshots that are public and can be copied or restored by any AWS account, and otherwise false. The default is false.
        
          You can share a manual DB snapshot as public by using the  ModifyDBSnapshotAttribute API.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass


class DBSnapshotCompleted(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshots>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              DBInstanceIdentifier=\'string\',
              DBSnapshotIdentifier=\'string\',
              SnapshotType=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\',
              IncludeShared=True|False,
              IncludePublic=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: 
        
          The ID of the DB instance to retrieve the list of DB snapshots for. This parameter can\'t be used in conjunction with ``DBSnapshotIdentifier`` . This parameter is not case-sensitive. 
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBInstance. 
           
        :type DBSnapshotIdentifier: string
        :param DBSnapshotIdentifier: 
        
          A specific DB snapshot identifier to describe. This parameter can\'t be used in conjunction with ``DBInstanceIdentifier`` . This value is stored as a lowercase string. 
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBSnapshot. 
           
          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be specified. 
           
        :type SnapshotType: string
        :param SnapshotType: 
        
          The type of snapshots to be returned. You can specify one of the following values:
        
          * ``automated`` - Return all DB snapshots that have been automatically taken by Amazon RDS for my AWS account. 
           
          * ``manual`` - Return all DB snapshots that have been taken by my AWS account. 
           
          * ``shared`` - Return all manual DB snapshots that have been shared to my AWS account. 
           
          * ``public`` - Return all DB snapshots that have been marked as public. 
           
          If you don\'t specify a ``SnapshotType`` value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not included in the returned results by default. You can include shared snapshots with these results by setting the ``IncludeShared`` parameter to ``true`` . You can include public snapshots with these results by setting the ``IncludePublic`` parameter to ``true`` .
        
          The ``IncludeShared`` and ``IncludePublic`` parameters don\'t apply for ``SnapshotType`` values of ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn\'t apply when ``SnapshotType`` is set to ``shared`` . The ``IncludeShared`` parameter doesn\'t apply when ``SnapshotType`` is set to ``public`` .
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBSnapshots`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :type IncludeShared: boolean
        :param IncludeShared: 
        
          True to include shared manual DB snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false. The default is ``false`` .
        
          You can give an AWS account permission to restore a manual DB snapshot from another AWS account by using the  ModifyDBSnapshotAttribute API action.
        
        :type IncludePublic: boolean
        :param IncludePublic: 
        
          True to include manual DB snapshots that are public and can be copied or restored by any AWS account, and otherwise false. The default is false.
        
          You can share a manual DB snapshot as public by using the  ModifyDBSnapshotAttribute API.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class DBSnapshotDeleted(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshots>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              DBInstanceIdentifier=\'string\',
              DBSnapshotIdentifier=\'string\',
              SnapshotType=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\',
              IncludeShared=True|False,
              IncludePublic=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: 
        
          The ID of the DB instance to retrieve the list of DB snapshots for. This parameter can\'t be used in conjunction with ``DBSnapshotIdentifier`` . This parameter is not case-sensitive. 
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBInstance. 
           
        :type DBSnapshotIdentifier: string
        :param DBSnapshotIdentifier: 
        
          A specific DB snapshot identifier to describe. This parameter can\'t be used in conjunction with ``DBInstanceIdentifier`` . This value is stored as a lowercase string. 
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBSnapshot. 
           
          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be specified. 
           
        :type SnapshotType: string
        :param SnapshotType: 
        
          The type of snapshots to be returned. You can specify one of the following values:
        
          * ``automated`` - Return all DB snapshots that have been automatically taken by Amazon RDS for my AWS account. 
           
          * ``manual`` - Return all DB snapshots that have been taken by my AWS account. 
           
          * ``shared`` - Return all manual DB snapshots that have been shared to my AWS account. 
           
          * ``public`` - Return all DB snapshots that have been marked as public. 
           
          If you don\'t specify a ``SnapshotType`` value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not included in the returned results by default. You can include shared snapshots with these results by setting the ``IncludeShared`` parameter to ``true`` . You can include public snapshots with these results by setting the ``IncludePublic`` parameter to ``true`` .
        
          The ``IncludeShared`` and ``IncludePublic`` parameters don\'t apply for ``SnapshotType`` values of ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn\'t apply when ``SnapshotType`` is set to ``shared`` . The ``IncludeShared`` parameter doesn\'t apply when ``SnapshotType`` is set to ``public`` .
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBSnapshots`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :type IncludeShared: boolean
        :param IncludeShared: 
        
          True to include shared manual DB snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false. The default is ``false`` .
        
          You can give an AWS account permission to restore a manual DB snapshot from another AWS account by using the  ModifyDBSnapshotAttribute API action.
        
        :type IncludePublic: boolean
        :param IncludePublic: 
        
          True to include manual DB snapshots that are public and can be copied or restored by any AWS account, and otherwise false. The default is false.
        
          You can share a manual DB snapshot as public by using the  ModifyDBSnapshotAttribute API.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass
