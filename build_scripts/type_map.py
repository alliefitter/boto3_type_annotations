from datetime import datetime
from typing import Callable, IO, List, Dict

from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter

TYPE_MAP = {
    bytes: (
        'bytes',
        'blob'
    ),
    bool: (
        'boolean',
    ),
    Callable: (
        'function',
    ),
    BaseClient: (
        'botocore or boto3 Client',
    ),
    datetime: (
        'datetime',
        'timestamp'
    ),
    Dict: (
        'dict',
        'structure',
        'map'
    ),
    float: (
        'float',
        'double'
    ),
    int: (
        'int',
        'integer',
        'long'
    ),
    IO: (
        'a file-like object',
        'seekable file-like object'
    ),
    List: (
        'list',
    ),
    None: (
        'None',
        None
    ),
    Paginator: (
        'L{botocore.paginate.Paginator}',
    ),
    ResourceCollection: (
        ':py:class:`ResourceCollection`',
    ),
    str: (
        'JSON serializable',
        'string',
        'str'
    ),
    TransferConfig: (
        'boto3.s3.transfer.TransferConfig',
    ),
    Waiter: (
        'botocore.waiter.Waiter',
    ),
    (bytes, IO): (
        'bytes or seekable file-like object',
    ),
    (str, Dict): (
        'str or dict',
    ),
    'List[str]': (
        'list(string)',
        'list of str'
    ),
    '\'NetworkAcl\'': (
        ':py:class:`ec2.NetworkAcl`',
        ':py:class:`EC2.NetworkAcl`',
    ),
    'List[\'PlatformApplication\']': (
        'list(:py:class:`sns.PlatformApplication`)',
    ),
    'List[\'InternetGateway\']': (
        'list(:py:class:`ec2.InternetGateway`)',
    ),
    '\'UserPolicy\'': (
        ':py:class:`iam.UserPolicy`',
        ':py:class:`IAM.UserPolicy`',
    ),
    'List[\'VirtualMfaDevice\']': (
        'list(:py:class:`iam.VirtualMfaDevice`)',
    ),
    'List[\'Image\']': (
        'list(:py:class:`ec2.Image`)',
    ),
    'List[\'Alarm\']': (
        'list(:py:class:`cloudwatch.Alarm`)',
    ),
    'List[\'Layer\']': (
        'list(:py:class:`opsworks.Layer`)',
    ),
    '\'GroupPolicy\'': (
        ':py:class:`iam.GroupPolicy`',
        ':py:class:`IAM.GroupPolicy`',
    ),
    'List[\'SigningCertificate\']': (
        'list(:py:class:`iam.SigningCertificate`)',
    ),
    'List[\'Volume\']': (
        'list(:py:class:`ec2.Volume`)',
    ),
    'List[\'VpcPeeringConnection\']': (
        'list(:py:class:`ec2.VpcPeeringConnection`)',
    ),
    '\'Subnet\'': (
        ':py:class:`ec2.Subnet`',
        ':py:class:`EC2.Subnet`',
    ),
    'List[\'ServerCertificate\']': (
        'list(:py:class:`iam.ServerCertificate`)',
    ),
    'List[\'VpcAddress\']': (
        'list(:py:class:`ec2.VpcAddress`)',
    ),
    '\'PlatformEndpoint\'': (
        ':py:class:`sns.PlatformEndpoint`',
        ':py:class:`SNS.PlatformEndpoint`',
    ),
    '\'MultipartUpload\'': (
        ':py:class:`s3.MultipartUpload`',
        ':py:class:`glacier.MultipartUpload`',
        ':py:class:`Glacier.MultipartUpload`',
        ':py:class:`S3.MultipartUpload`',
    ),
    'List[\'Subnet\']': (
        'list(:py:class:`ec2.Subnet`)',
    ),
    '\'Layer\'': (
        ':py:class:`opsworks.Layer`',
        ':py:class:`OpsWorks.Layer`',
    ),
    'List[\'MfaDevice\']': (
        'list(:py:class:`iam.MfaDevice`)',
    ),
    'List[\'Job\']': (
        'list(:py:class:`glacier.Job`)',
    ),
    'List[\'RolePolicy\']': (
        'list(:py:class:`iam.RolePolicy`)',
    ),
    'List[\'InstanceProfile\']': (
        'list(:py:class:`iam.InstanceProfile`)',
    ),
    'List[\'Instance\']': (
        'list(:py:class:`ec2.Instance`)',
    ),
    '\'Vault\'': (
        ':py:class:`glacier.Vault`',
        ':py:class:`Glacier.Vault`',
    ),
    '\'SecurityGroup\'': (
        ':py:class:`ec2.SecurityGroup`',
        ':py:class:`EC2.SecurityGroup`',
    ),
    '\'RouteTable\'': (
        ':py:class:`ec2.RouteTable`',
        ':py:class:`EC2.RouteTable`',
    ),
    'List[\'Table\']': (
        'list(:py:class:`dynamodb.Table`)',
    ),
    'List[\'Snapshot\']': (
        'list(:py:class:`ec2.Snapshot`)',
    ),
    'List[\'Message\']': (
        'list(:py:class:`sqs.Message`)',
    ),
    'List[\'Role\']': (
        'list(:py:class:`iam.Role`)',
    ),
    '\'Job\'': (
        ':py:class:`glacier.Job`',
        ':py:class:`Glacier.Job`',
    ),
    'List[\'Metric\']': (
        'list(:py:class:`cloudwatch.Metric`)',
    ),
    'List[\'Policy\']': (
        'list(:py:class:`iam.Policy`)',
    ),
    'List[\'ClassicAddress\']': (
        'list(:py:class:`ec2.ClassicAddress`)',
    ),
    'List[\'User\']': (
        'list(:py:class:`iam.User`)',
    ),
    'List[\'GroupPolicy\']': (
        'list(:py:class:`iam.GroupPolicy`)',
    ),
    'List[\'PolicyVersion\']': (
        'list(:py:class:`iam.PolicyVersion`)',
    ),
    'List[\'Topic\']': (
        'list(:py:class:`sns.Topic`)',
    ),
    '\'LoginProfile\'': (
        ':py:class:`iam.LoginProfile`',
        ':py:class:`IAM.LoginProfile`',
    ),
    'List[\'UserPolicy\']': (
        'list(:py:class:`iam.UserPolicy`)',
    ),
    'List[\'Event\']': (
        'list(:py:class:`cloudformation.Event`)',
    ),
    '\'Event\'': (
        ':py:class:`cloudformation.Event`',
        ':py:class:`CloudFormation.Event`',
    ),
    'List[\'MultipartUpload\']': (
        'list(:py:class:`s3.MultipartUpload`)',
        'list(:py:class:`glacier.MultipartUpload`)',
    ),
    'List[\'Subscription\']': (
        'list(:py:class:`sns.Subscription`)',
    ),
    '\'PolicyVersion\'': (
        ':py:class:`iam.PolicyVersion`',
        ':py:class:`IAM.PolicyVersion`',
    ),
    'List[base.ServiceResource]': (
        'list(:py:class:`~boto3.resources.base.ServiceResource`)',
    ),
    'List[\'NetworkInterface\']': (
        'list(:py:class:`ec2.NetworkInterface`)',
    ),
    'List[\'ObjectVersion\']': (
        'list(:py:class:`s3.ObjectVersion`)',
    ),
    'List[\'SecurityGroup\']': (
        'list(:py:class:`ec2.SecurityGroup`)',
    ),
    'List[\'Queue\']': (
        'list(:py:class:`sqs.Queue`)',
    ),
    'List[\'PlacementGroup\']': (
        'list(:py:class:`ec2.PlacementGroup`)',
    ),
    'List[\'Vpc\']': (
        'list(:py:class:`ec2.Vpc`)',
    ),
    'List[\'RouteTable\']': (
        'list(:py:class:`ec2.RouteTable`)',
    ),
    'List[\'Vault\']': (
        'list(:py:class:`glacier.Vault`)',
    ),
    'List[\'Group\']': (
        'list(:py:class:`iam.Group`)',
        ':py:class:`iam.Group`',
    ),
    '\'Image\'': (
        ':py:class:`ec2.Image`',
        ':py:class:`EC2.Image`',
    ),
    '\'Route\'': (
        ':py:class:`ec2.Route`',
        ':py:class:`EC2.Route`',
    ),
    '\'VpcPeeringConnection\'': (
        ':py:class:`ec2.VpcPeeringConnection`',
        ':py:class:`EC2.VpcPeeringConnection`',
    ),
    'List[\'Stack\']': (
        'list(:py:class:`cloudformation.Stack`)',
        'list(:py:class:`opsworks.Stack`)',
    ),
    '\'MfaDevice\'': (
        ':py:class:`iam.MfaDevice`',
        ':py:class:`IAM.MfaDevice`',
    ),
    'List[\'Bucket\']': (
        'list(:py:class:`s3.Bucket`)',
    ),
    'List[\'PlatformEndpoint\']': (
        'list(:py:class:`sns.PlatformEndpoint`)',
    ),
    '\'Snapshot\'': (
        ':py:class:`ec2.Snapshot`',
        ':py:class:`EC2.Snapshot`',
    ),
    'List[\'DhcpOptions\']': (
        'list(:py:class:`ec2.DhcpOptions`)',
    ),
    'List[\'NetworkAcl\']': (
        'list(:py:class:`ec2.NetworkAcl`)',
    ),
    'List[\'KeyPairInfo\']': (
        'list(:py:class:`ec2.KeyPairInfo`)',
    ),
    'List[\'StackResourceSummary\']': (
        'list(:py:class:`cloudformation.StackResourceSummary`)',
    ),
    '\'Table\'': (
        ':py:class:`dynamodb.Table`',
        ':py:class:`DynamoDB.Table`',
    ),
    '\'AccessKeyPair\'': (
        ':py:class:`iam.AccessKeyPair`',
        ':py:class:`IAM.AccessKeyPair`',
    ),
    'List[\'SamlProvider\']': (
        'list(:py:class:`iam.SamlProvider`)',
    ),
    '\'Archive\'': (
        ':py:class:`glacier.Archive`',
        ':py:class:`Glacier.Archive`',
    ),
    '\'NetworkInterface\'': (
        ':py:class:`ec2.NetworkInterface`',
        ':py:class:`EC2.NetworkInterface`',
    ),
    'List[\'AccessKey\']': (
        'list(:py:class:`iam.AccessKey`)',
    ),
    '\'Subscription\'': (
        ':py:class:`sns.Subscription`',
        ':py:class:`SNS.Subscription`',
    ),
    'List[\'MultipartUploadPart\']': (
        'list(:py:class:`s3.MultipartUploadPart`)',
    ),
    '\'ServerCertificate\'': (
        ':py:class:`iam.ServerCertificate`',
        ':py:class:`IAM.ServerCertificate`',
    ),
    'List[\'ObjectSummary\']': (
        'list(:py:class:`s3.ObjectSummary`)',
    ),
    'List[\'Tag\']': (
        'list(:py:class:`ec2.Tag`)',
    ),
    '\'Alarm\'': (
        ':py:class:`cloudwatch.Alarm`',
        ':py:class:`CloudWatch.Alarm`',
    ),
    '\'PlacementGroup\'': (
        ':py:class:`EC2.PlacementGroup`',
        ':py:class:`ec2.PlacementGroup`',
    ),
    '\'Vpc\'': (
        ':py:class:`EC2.Vpc`',
        ':py:class:`ec2.Vpc`',
    ),
    '\'BucketVersioning\'': (
        ':py:class:`S3.BucketVersioning`',
    ),
    '\'User\'': (
        ':py:class:`IAM.User`',
        ':py:class:`iam.User`',
    ),
    '\'Topic\'': (
        ':py:class:`sns.Topic`',
        ':py:class:`SNS.Topic`',
    ),
    '\'Policy\'': (
        ':py:class:`iam.Policy`',
        ':py:class:`IAM.Policy`',
    ),
    '\'BucketCors\'': (
        ':py:class:`S3.BucketCors`',
    ),
    '\'Stack\'': (
        ':py:class:`OpsWorks.Stack`',
        ':py:class:`CloudFormation.Stack`',
        ':py:class:`opsworks.Stack`',
        ':py:class:`cloudformation.Stack`',
    ),
    '\'SigningCertificate\'': (
        ':py:class:`IAM.SigningCertificate`',
        ':py:class:`iam.SigningCertificate`',
    ),
    '\'ObjectVersion\'': (
        ':py:class:`S3.ObjectVersion`',
    ),
    '\'BucketPolicy\'': (
        ':py:class:`S3.BucketPolicy`',
    ),
    '\'RouteTableAssociation\'': (
        ':py:class:`EC2.RouteTableAssociation`',
        ':py:class:`ec2.RouteTableAssociation`',
    ),
    '\'RolePolicy\'': (
        ':py:class:`IAM.RolePolicy`',
    ),
    '\'CurrentUser\'': (
        ':py:class:`IAM.CurrentUser`',
    ),
    '\'InternetGateway\'': (
        ':py:class:`EC2.InternetGateway`',
        ':py:class:`ec2.InternetGateway`',
    ),
    '\'PlatformApplication\'': (
        ':py:class:`sns.PlatformApplication`',
        ':py:class:`SNS.PlatformApplication`',
    ),
    '\'Metric\'': (
        ':py:class:`CloudWatch.Metric`',
    ),
    '\'Group\'': (
        ':py:class:`IAM.Group`',
    ),
    '\'StackSummary\'': (
        ':py:class:`OpsWorks.StackSummary`',
    ),
    '\'AssumeRolePolicy\'': (
        ':py:class:`IAM.AssumeRolePolicy`',
    ),
    '\'Object\'': (
        ':py:class:`S3.Object`',
        ':py:class:`s3.Object`',
    ),
    '\'StackResourceSummary\'': (
        ':py:class:`CloudFormation.StackResourceSummary`',
    ),
    '\'BucketWebsite\'': (
        ':py:class:`S3.BucketWebsite`',
    ),
    '\'Queue\'': (
        ':py:class:`SQS.Queue`',
        ':py:class:`sqs.Queue`',
    ),
    '\'MultipartUploadPart\'': (
        ':py:class:`S3.MultipartUploadPart`',
    ),
    '\'KeyPairInfo\'': (
        ':py:class:`ec2.KeyPairInfo`',
        ':py:class:`EC2.KeyPairInfo`',
    ),
    '\'InstanceProfile\'': (
        ':py:class:`iam.InstanceProfile`',
        ':py:class:`IAM.InstanceProfile`',
    ),
    '\'AccessKey\'': (
        ':py:class:`IAM.AccessKey`',
    ),
    '\'SamlProvider\'': (
        ':py:class:`IAM.SamlProvider`',
        ':py:class:`iam.SamlProvider`',
    ),
    '\'Tag\'': (
        ':py:class:`EC2.Tag`',
    ),
    '\'BucketLifecycleConfiguration\'': (
        ':py:class:`S3.BucketLifecycleConfiguration`',
    ),
    '\'AccountPasswordPolicy\'': (
        ':py:class:`iam.AccountPasswordPolicy`',
        ':py:class:`IAM.AccountPasswordPolicy`',
    ),
    '\'BucketNotification\'': (
        ':py:class:`S3.BucketNotification`',
    ),
    '\'StackResource\'': (
        ':py:class:`CloudFormation.StackResource`',
    ),
    '\'Instance\'': (
        ':py:class:`EC2.Instance`',
    ),
    '\'BucketTagging\'': (
        ':py:class:`S3.BucketTagging`',
    ),
    '\'AccountSummary\'': (
        ':py:class:`IAM.AccountSummary`',
    ),
    '\'Volume\'': (
        ':py:class:`EC2.Volume`',
        ':py:class:`ec2.Volume`',
    ),
    '\'Message\'': (
        ':py:class:`SQS.Message`',
    ),
    '\'KeyPair\'': (
        ':py:class:`ec2.KeyPair`',
    ),
    '\'BucketAcl\'': (
        ':py:class:`S3.BucketAcl`',
    ),
    '\'BucketRequestPayment\'': (
        ':py:class:`S3.BucketRequestPayment`',
    ),
    '\'Role\'': (
        ':py:class:`IAM.Role`',
        ':py:class:`iam.Role`',
    ),
    '\'VirtualMfaDevice\'': (
        ':py:class:`IAM.VirtualMfaDevice`',
        ':py:class:`iam.VirtualMfaDevice`',
    ),
    '\'Account\'': (
        ':py:class:`Glacier.Account`',
    ),
    '\'BucketLifecycle\'': (
        ':py:class:`S3.BucketLifecycle`',
    ),
    '\'DhcpOptions\'': (
        ':py:class:`EC2.DhcpOptions`',
        ':py:class:`ec2.DhcpOptions`',
    ),
    '\'BucketLogging\'': (
        ':py:class:`S3.BucketLogging`',
    ),
    '\'Notification\'': (
        ':py:class:`Glacier.Notification`',
    ),
    '\'ClassicAddress\'': (
        ':py:class:`EC2.ClassicAddress`',
    ),
    '\'Bucket\'': (
        ':py:class:`s3.Bucket`',
        ':py:class:`S3.Bucket`',
    ),
    '\'VpcAddress\'': (
        ':py:class:`EC2.VpcAddress`',
    ),
    '\'ObjectSummary\'': (
        ':py:class:`S3.ObjectSummary`',
    ),
    '\'NetworkInterfaceAssociation\'': (
        ':py:class:`EC2.NetworkInterfaceAssociation`',
    ),
    '\'ObjectAcl\'': (
        ':py:class:`S3.ObjectAcl`',
    ),
}
