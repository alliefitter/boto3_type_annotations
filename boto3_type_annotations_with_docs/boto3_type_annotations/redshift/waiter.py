from datetime import datetime
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class ClusterAvailable(Waiter):
    def wait(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusters>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ClusterIdentifier=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: 
        
          The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.
        
          The default is that all clusters defined for an account are returned.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusters request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
          Constraints: You can specify either the **ClusterIdentifier** parameter or the **Marker** parameter, but not both. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 60
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 30
        
        :returns: None
        """
        pass


class ClusterDeleted(Waiter):
    def wait(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusters>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ClusterIdentifier=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: 
        
          The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.
        
          The default is that all clusters defined for an account are returned.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusters request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
          Constraints: You can specify either the **ClusterIdentifier** parameter or the **Marker** parameter, but not both. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 60
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 30
        
        :returns: None
        """
        pass


class ClusterRestored(Waiter):
    def wait(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusters>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ClusterIdentifier=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: 
        
          The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.
        
          The default is that all clusters defined for an account are returned.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusters request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
          Constraints: You can specify either the **ClusterIdentifier** parameter or the **Marker** parameter, but not both. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 60
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 30
        
        :returns: None
        """
        pass


class SnapshotAvailable(Waiter):
    def wait(self, ClusterIdentifier: str = None, SnapshotIdentifier: str = None, SnapshotType: str = None, StartTime: datetime = None, EndTime: datetime = None, MaxRecords: int = None, Marker: str = None, OwnerAccount: str = None, TagKeys: List = None, TagValues: List = None, ClusterExists: bool = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterSnapshots>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ClusterIdentifier=\'string\',
              SnapshotIdentifier=\'string\',
              SnapshotType=\'string\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              MaxRecords=123,
              Marker=\'string\',
              OwnerAccount=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ],
              ClusterExists=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: 
        
          The identifier of the cluster for which information about snapshots is requested.
        
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: 
        
          The snapshot identifier of the snapshot about which to return information.
        
        :type SnapshotType: string
        :param SnapshotType: 
        
          The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.
        
          Valid Values: ``automated`` | ``manual``  
        
        :type StartTime: datetime
        :param StartTime: 
        
          A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__  
        
          Example: ``2012-07-16T18:00:00Z``  
        
        :type EndTime: datetime
        :param EndTime: 
        
          A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__  
        
          Example: ``2012-07-16T18:00:00Z``  
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusterSnapshots request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :type OwnerAccount: string
        :param OwnerAccount: 
        
          The AWS customer account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your AWS customer account, or do not specify the parameter.
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :type ClusterExists: boolean
        :param ClusterExists: 
        
          A value that indicates whether to return snapshots only for an existing cluster. Table-level restore can be performed only using a snapshot of an existing cluster, that is, a cluster that has not been deleted. If ``ClusterExists`` is set to ``true`` , ``ClusterIdentifier`` is required.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 20
        
        :returns: None
        """
        pass
