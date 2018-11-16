from typing import Optional
from typing import Union
from boto3.resources.collection import ResourceCollection
from typing import List
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    stacks: 'stacks'

    def Layer(self, id: str = None) -> 'Layer':
        """
        Creates a Layer resource.::
        
          layer = opsworks.Layer(\'id\')
        
        :type id: string
        :param id: The Layer\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`OpsWorks.Layer`
        :returns: A Layer resource
        """
        pass

    def Stack(self, id: str = None) -> 'Stack':
        """
        Creates a Stack resource.::
        
          stack = opsworks.Stack(\'id\')
        
        :type id: string
        :param id: The Stack\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`OpsWorks.Stack`
        :returns: A Stack resource
        """
        pass

    def StackSummary(self, stack_id: str = None) -> 'StackSummary':
        """
        Creates a StackSummary resource.::
        
          stack_summary = opsworks.StackSummary(\'stack_id\')
        
        :type stack_id: string
        :param stack_id: The StackSummary\'s stack_id identifier. This **must** be set.
        
        :rtype: :py:class:`OpsWorks.StackSummary`
        :returns: A StackSummary resource
        """
        pass

    def create_stack(self, Name: str, Region: str, ServiceRoleArn: str, DefaultInstanceProfileArn: str, VpcId: str = None, Attributes: Dict = None, DefaultOs: str = None, HostnameTheme: str = None, DefaultAvailabilityZone: str = None, DefaultSubnetId: str = None, CustomJson: str = None, ConfigurationManager: Dict = None, ChefConfiguration: Dict = None, UseCustomCookbooks: bool = None, UseOpsworksSecurityGroups: bool = None, CustomCookbooksSource: Dict = None, DefaultSshKeyName: str = None, DefaultRootDeviceType: str = None, AgentVersion: str = None) -> 'Stack':
        """
        
         **Required Permissions** : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information about user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateStack>`_
        
        **Request Syntax** 
        ::
        
          stack = opsworks.create_stack(
              Name=\'string\',
              Region=\'string\',
              VpcId=\'string\',
              Attributes={
                  \'string\': \'string\'
              },
              ServiceRoleArn=\'string\',
              DefaultInstanceProfileArn=\'string\',
              DefaultOs=\'string\',
              HostnameTheme=\'string\',
              DefaultAvailabilityZone=\'string\',
              DefaultSubnetId=\'string\',
              CustomJson=\'string\',
              ConfigurationManager={
                  \'Name\': \'string\',
                  \'Version\': \'string\'
              },
              ChefConfiguration={
                  \'ManageBerkshelf\': True|False,
                  \'BerkshelfVersion\': \'string\'
              },
              UseCustomCookbooks=True|False,
              UseOpsworksSecurityGroups=True|False,
              CustomCookbooksSource={
                  \'Type\': \'git\'|\'svn\'|\'archive\'|\'s3\',
                  \'Url\': \'string\',
                  \'Username\': \'string\',
                  \'Password\': \'string\',
                  \'SshKey\': \'string\',
                  \'Revision\': \'string\'
              },
              DefaultSshKeyName=\'string\',
              DefaultRootDeviceType=\'ebs\'|\'instance-store\',
              AgentVersion=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The stack name.
        
        :type Region: string
        :param Region: **[REQUIRED]** 
        
          The stack\'s AWS region, such as ``ap-south-1`` . For more information about Amazon regions, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .
        
          .. note::
        
            In the AWS CLI, this API maps to the ``--stack-region`` parameter. If the ``--stack-region`` parameter and the AWS CLI common parameter ``--region`` are set to the same value, the stack uses a *regional* endpoint. If the ``--stack-region`` parameter is not set, but the AWS CLI ``--region`` parameter is, this also results in a stack with a *regional* endpoint. However, if the ``--region`` parameter is set to ``us-east-1`` , and the ``--stack-region`` parameter is set to one of the following, then the stack uses a legacy or *classic* region: ``us-west-1, us-west-2, sa-east-1, eu-central-1, eu-west-1, ap-northeast-1, ap-southeast-1, ap-southeast-2`` . In this case, the actual API endpoint of the stack is in ``us-east-1`` . Only the preceding regions are supported as classic regions in the ``us-east-1`` API endpoint. Because it is a best practice to choose the regional endpoint that is closest to where you manage AWS, we recommend that you use regional endpoints for new stacks. The AWS CLI common ``--region`` parameter always specifies a regional API endpoint; it cannot be used to specify a classic AWS OpsWorks Stacks region.
        
        :type VpcId: string
        :param VpcId: 
        
          The ID of the VPC that the stack is to be launched into. The VPC must be in the stack\'s region. All instances are launched into this VPC. You cannot change the ID later.
        
          * If your account supports EC2-Classic, the default value is ``no VPC`` . 
           
          * If your account does not support EC2-Classic, the default value is the default VPC for the specified region. 
           
          If the VPC ID corresponds to a default VPC and you have specified either the ``DefaultAvailabilityZone`` or the ``DefaultSubnetId`` parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively.
        
          If you specify a nondefault VPC ID, note the following:
        
          * It must belong to a VPC in your account that is in the specified region. 
           
          * You must specify a value for ``DefaultSubnetId`` . 
           
          For more information about how to use AWS OpsWorks Stacks with a VPC, see `Running a Stack in a VPC <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-vpc.html>`__ . For more information about default VPC and EC2-Classic, see `Supported Platforms <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`__ . 
        
        :type Attributes: dict
        :param Attributes: 
        
          One or more user-defined key-value pairs to be added to the stack attributes.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type ServiceRoleArn: string
        :param ServiceRoleArn: **[REQUIRED]** 
        
          The stack\'s AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .
        
        :type DefaultInstanceProfileArn: string
        :param DefaultInstanceProfileArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack\'s EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .
        
        :type DefaultOs: string
        :param DefaultOs: 
        
          The stack\'s default operating system, which is installed on every instance unless you specify a different operating system when you create the instance. You can specify one of the following.
        
          * A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2017.09`` , ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . 
           
          * A supported Ubuntu operating system, such as ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . 
           
          * ``CentOS Linux 7``   
           
          * ``Red Hat Enterprise Linux 7``   
           
          * A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . 
           
          * A custom AMI: ``Custom`` . You specify the custom AMI you want to use when you create instances. For more information, see `Using Custom AMIs <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__ . 
           
          The default option is the current Amazon Linux version. For more information about supported operating systems, see `AWS OpsWorks Stacks Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ .
        
        :type HostnameTheme: string
        :param HostnameTheme: 
        
          The stack\'s host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack\'s instances. By default, ``HostnameTheme`` is set to ``Layer_Dependent`` , which creates host names by appending integers to the layer\'s short name. The other themes are:
        
          * ``Baked_Goods``   
           
          * ``Clouds``   
           
          * ``Europe_Cities``   
           
          * ``Fruits``   
           
          * ``Greek_Deities``   
           
          * ``Legendary_creatures_from_Japan``   
           
          * ``Planets_and_Moons``   
           
          * ``Roman_Deities``   
           
          * ``Scottish_Islands``   
           
          * ``US_Cities``   
           
          * ``Wild_Cats``   
           
          To obtain a generated host name, call ``GetHostNameSuggestion`` , which returns a host name based on the current theme.
        
        :type DefaultAvailabilityZone: string
        :param DefaultAvailabilityZone: 
        
          The stack\'s default Availability Zone, which must be in the specified region. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ . If you also specify a value for ``DefaultSubnetId`` , the subnet must be in the same zone. For more information, see the ``VpcId`` parameter description. 
        
        :type DefaultSubnetId: string
        :param DefaultSubnetId: 
        
          The stack\'s default VPC subnet ID. This parameter is required if you specify a value for the ``VpcId`` parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for ``DefaultAvailabilityZone`` , the subnet must be in that zone. For information on default values and when this parameter is required, see the ``VpcId`` parameter description. 
        
        :type CustomJson: string
        :param CustomJson: 
        
          A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:
        
           ``\"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}\"``  
        
          For more information about custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .
        
        :type ConfigurationManager: dict
        :param ConfigurationManager: 
        
          The configuration manager. When you create a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.
        
          - **Name** *(string) --* 
        
            The name. This parameter must be set to \"Chef\".
        
          - **Version** *(string) --* 
        
            The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
        
        :type ChefConfiguration: dict
        :param ChefConfiguration: 
        
          A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .
        
          - **ManageBerkshelf** *(boolean) --* 
        
            Whether to enable Berkshelf.
        
          - **BerkshelfVersion** *(string) --* 
        
            The Berkshelf version.
        
        :type UseCustomCookbooks: boolean
        :param UseCustomCookbooks: 
        
          Whether the stack uses custom cookbooks.
        
        :type UseOpsworksSecurityGroups: boolean
        :param UseOpsworksSecurityGroups: 
        
          Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack\'s layers.
        
          AWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With ``UseOpsworksSecurityGroups`` you can instead provide your own custom security groups. ``UseOpsworksSecurityGroups`` has the following settings: 
        
          * True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group. 
           
          * False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings. 
           
          For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .
        
        :type CustomCookbooksSource: dict
        :param CustomCookbooksSource: 
        
          Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Creating Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or `Custom Recipes and Cookbooks <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .
        
          - **Type** *(string) --* 
        
            The repository type.
        
          - **Url** *(string) --* 
        
            The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .
        
          - **Username** *(string) --* 
        
            This parameter depends on the repository type.
        
            * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
             
            * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
             
          - **Password** *(string) --* 
        
            When included in a request, the parameter depends on the repository type.
        
            * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
             
            * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
             
            For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .
        
            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.
        
          - **SshKey** *(string) --* 
        
            In requests, the repository\'s SSH key.
        
            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.
        
          - **Revision** *(string) --* 
        
            The application\'s version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
        
        :type DefaultSshKeyName: string
        :param DefaultSshKeyName: 
        
          A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see `Using SSH to Communicate with an Instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html>`__ and `Managing SSH Access <http://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html>`__ . You can override this setting by specifying a different key pair, or no key pair, when you `create an instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`__ . 
        
        :type DefaultRootDeviceType: string
        :param DefaultRootDeviceType: 
        
          The default root device type. This value is the default for all instances in the stack, but you can override it when you create an instance. The default option is ``instance-store`` . For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .
        
        :type AgentVersion: string
        :param AgentVersion: 
        
          The default AWS OpsWorks Stacks agent version. You have the following options:
        
          * Auto-update - Set this parameter to ``LATEST`` . AWS OpsWorks Stacks automatically installs new agent versions on the stack\'s instances as soon as they are available. 
           
          * Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack\'s instances. 
           
          The default setting is the most recent release of the agent. To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.
        
          .. note::
        
            You can also specify an agent version when you create or update an instance, which overrides the stack\'s default setting.
        
        :rtype: :py:class:`opsworks.Stack`
        :returns: Stack resource
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass


class Layer(base.ServiceResource):
    arn: str
    stack_id: str
    layer_id: str
    type: str
    name: str
    shortname: str
    attributes: Dict
    cloud_watch_logs_configuration: Dict
    custom_instance_profile_arn: str
    custom_json: str
    custom_security_group_ids: List
    default_security_group_names: List
    packages: List
    volume_configurations: List
    enable_auto_healing: bool
    auto_assign_elastic_ips: bool
    auto_assign_public_ips: bool
    default_recipes: Dict
    custom_recipes: Dict
    created_at: str
    install_updates_on_boot: bool
    use_ebs_optimized_instances: bool
    lifecycle_event_configuration: Dict
    id: str

    def delete(self):
        """
        
         **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteLayer>`_
        
        **Request Syntax** 
        ::
        
          response = layer.delete()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_
        
        **Request Syntax** 
        
        ::
        
          layer.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_
        
        **Request Syntax** 
        
        ::
        
          layer.load()
        :returns: None
        """
        pass


class Stack(base.ServiceResource):
    stack_id: str
    name: str
    arn: str
    region: str
    vpc_id: str
    attributes: Dict
    service_role_arn: str
    default_instance_profile_arn: str
    default_os: str
    hostname_theme: str
    default_availability_zone: str
    default_subnet_id: str
    custom_json: str
    configuration_manager: Dict
    chef_configuration: Dict
    use_custom_cookbooks: bool
    use_opsworks_security_groups: bool
    custom_cookbooks_source: Dict
    default_ssh_key_name: str
    created_at: str
    default_root_device_type: str
    agent_version: str
    id: str
    layers: 'layers'

    def create_layer(self, Type: str, Name: str, Shortname: str, Attributes: Dict = None, CloudWatchLogsConfiguration: Dict = None, CustomInstanceProfileArn: str = None, CustomJson: str = None, CustomSecurityGroupIds: List = None, Packages: List = None, VolumeConfigurations: List = None, EnableAutoHealing: bool = None, AutoAssignElasticIps: bool = None, AutoAssignPublicIps: bool = None, CustomRecipes: Dict = None, InstallUpdatesOnBoot: bool = None, UseEbsOptimizedInstances: bool = None, LifecycleEventConfiguration: Dict = None) -> 'Layer':
        """
        
        .. note::
        
          You should use **CreateLayer** for noncustom layer types such as PHP App Server only if the stack does not have an existing layer of that type. A stack can have at most one instance of each noncustom layer; if you attempt to create a second instance, **CreateLayer** fails. A stack can have an arbitrary number of custom layers, so you can call **CreateLayer** as many times as you like for that layer type.
        
         **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateLayer>`_
        
        **Request Syntax** 
        ::
        
          layer = stack.create_layer(
              Type=\'aws-flow-ruby\'|\'ecs-cluster\'|\'java-app\'|\'lb\'|\'web\'|\'php-app\'|\'rails-app\'|\'nodejs-app\'|\'memcached\'|\'db-master\'|\'monitoring-master\'|\'custom\',
              Name=\'string\',
              Shortname=\'string\',
              Attributes={
                  \'string\': \'string\'
              },
              CloudWatchLogsConfiguration={
                  \'Enabled\': True|False,
                  \'LogStreams\': [
                      {
                          \'LogGroupName\': \'string\',
                          \'DatetimeFormat\': \'string\',
                          \'TimeZone\': \'LOCAL\'|\'UTC\',
                          \'File\': \'string\',
                          \'FileFingerprintLines\': \'string\',
                          \'MultiLineStartPattern\': \'string\',
                          \'InitialPosition\': \'start_of_file\'|\'end_of_file\',
                          \'Encoding\': \'ascii\'|\'big5\'|\'big5hkscs\'|\'cp037\'|\'cp424\'|\'cp437\'|\'cp500\'|\'cp720\'|\'cp737\'|\'cp775\'|\'cp850\'|\'cp852\'|\'cp855\'|\'cp856\'|\'cp857\'|\'cp858\'|\'cp860\'|\'cp861\'|\'cp862\'|\'cp863\'|\'cp864\'|\'cp865\'|\'cp866\'|\'cp869\'|\'cp874\'|\'cp875\'|\'cp932\'|\'cp949\'|\'cp950\'|\'cp1006\'|\'cp1026\'|\'cp1140\'|\'cp1250\'|\'cp1251\'|\'cp1252\'|\'cp1253\'|\'cp1254\'|\'cp1255\'|\'cp1256\'|\'cp1257\'|\'cp1258\'|\'euc_jp\'|\'euc_jis_2004\'|\'euc_jisx0213\'|\'euc_kr\'|\'gb2312\'|\'gbk\'|\'gb18030\'|\'hz\'|\'iso2022_jp\'|\'iso2022_jp_1\'|\'iso2022_jp_2\'|\'iso2022_jp_2004\'|\'iso2022_jp_3\'|\'iso2022_jp_ext\'|\'iso2022_kr\'|\'latin_1\'|\'iso8859_2\'|\'iso8859_3\'|\'iso8859_4\'|\'iso8859_5\'|\'iso8859_6\'|\'iso8859_7\'|\'iso8859_8\'|\'iso8859_9\'|\'iso8859_10\'|\'iso8859_13\'|\'iso8859_14\'|\'iso8859_15\'|\'iso8859_16\'|\'johab\'|\'koi8_r\'|\'koi8_u\'|\'mac_cyrillic\'|\'mac_greek\'|\'mac_iceland\'|\'mac_latin2\'|\'mac_roman\'|\'mac_turkish\'|\'ptcp154\'|\'shift_jis\'|\'shift_jis_2004\'|\'shift_jisx0213\'|\'utf_32\'|\'utf_32_be\'|\'utf_32_le\'|\'utf_16\'|\'utf_16_be\'|\'utf_16_le\'|\'utf_7\'|\'utf_8\'|\'utf_8_sig\',
                          \'BufferDuration\': 123,
                          \'BatchCount\': 123,
                          \'BatchSize\': 123
                      },
                  ]
              },
              CustomInstanceProfileArn=\'string\',
              CustomJson=\'string\',
              CustomSecurityGroupIds=[
                  \'string\',
              ],
              Packages=[
                  \'string\',
              ],
              VolumeConfigurations=[
                  {
                      \'MountPoint\': \'string\',
                      \'RaidLevel\': 123,
                      \'NumberOfDisks\': 123,
                      \'Size\': 123,
                      \'VolumeType\': \'string\',
                      \'Iops\': 123,
                      \'Encrypted\': True|False
                  },
              ],
              EnableAutoHealing=True|False,
              AutoAssignElasticIps=True|False,
              AutoAssignPublicIps=True|False,
              CustomRecipes={
                  \'Setup\': [
                      \'string\',
                  ],
                  \'Configure\': [
                      \'string\',
                  ],
                  \'Deploy\': [
                      \'string\',
                  ],
                  \'Undeploy\': [
                      \'string\',
                  ],
                  \'Shutdown\': [
                      \'string\',
                  ]
              },
              InstallUpdatesOnBoot=True|False,
              UseEbsOptimizedInstances=True|False,
              LifecycleEventConfiguration={
                  \'Shutdown\': {
                      \'ExecutionTimeout\': 123,
                      \'DelayUntilElbConnectionsDrained\': True|False
                  }
              }
          )
        :type Type: string
        :param Type: **[REQUIRED]** 
        
          The layer type. A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The layer name, which is used by the console.
        
        :type Shortname: string
        :param Shortname: **[REQUIRED]** 
        
          For custom layers only, use this parameter to specify the layer\'s short name, which is used internally by AWS OpsWorks Stacks and by Chef recipes. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 200 characters, which are limited to the alphanumeric characters, \'-\', \'_\', and \'.\'.
        
          The built-in layers\' short names are defined by AWS OpsWorks Stacks. For more information, see the `Layer Reference <http://docs.aws.amazon.com/opsworks/latest/userguide/layers.html>`__ .
        
        :type Attributes: dict
        :param Attributes: 
        
          One or more user-defined key-value pairs to be added to the stack attributes.
        
          To create a cluster layer, set the ``EcsClusterArn`` attribute to the cluster\'s ARN.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type CloudWatchLogsConfiguration: dict
        :param CloudWatchLogsConfiguration: 
        
          Specifies CloudWatch Logs configuration options for the layer. For more information, see  CloudWatchLogsLogStream .
        
          - **Enabled** *(boolean) --* 
        
            Whether CloudWatch Logs is enabled for a layer.
        
          - **LogStreams** *(list) --* 
        
            A list of configuration options for CloudWatch Logs.
        
            - *(dict) --* 
        
              Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .
        
              - **LogGroupName** *(string) --* 
        
                Specifies the destination log group. A log group is created automatically if it doesn\'t already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (hyphen), \'/\' (forward slash), and \'.\' (period).
        
              - **DatetimeFormat** *(string) --* 
        
                Specifies how the time stamp is extracted from logs. For more information, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .
        
              - **TimeZone** *(string) --* 
        
                Specifies the time zone of log event time stamps.
        
              - **File** *(string) --* 
        
                Specifies log files that you want to push to CloudWatch Logs.
        
                 ``File`` can point to a specific file or multiple files (by using wild card characters such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as ``access_log.2014-06-01-01`` , ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don\'t use a wildcard to match multiple file types, such as ``access_log_80`` and ``access_log_443`` . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.
        
                Zipped files are not supported.
        
              - **FileFingerprintLines** *(string) --* 
        
                Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as \'1\', \'2-5\'. The default value is \'1\', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.
        
              - **MultiLineStartPattern** *(string) --* 
        
                Specifies the pattern for identifying the start of a log message.
        
              - **InitialPosition** *(string) --* 
        
                Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.
        
              - **Encoding** *(string) --* 
        
                Specifies the encoding of the log file so that the file can be read correctly. The default is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.
        
              - **BufferDuration** *(integer) --* 
        
                Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.
        
              - **BatchCount** *(integer) --* 
        
                Specifies the max number of log events in a batch, up to 10000. The default value is 1000.
        
              - **BatchSize** *(integer) --* 
        
                Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.
        
        :type CustomInstanceProfileArn: string
        :param CustomInstanceProfileArn: 
        
          The ARN of an IAM profile to be used for the layer\'s EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .
        
        :type CustomJson: string
        :param CustomJson: 
        
          A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer\'s instances. For more information, see `Using Custom JSON <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html>`__ . This feature is supported as of version 1.7.42 of the AWS CLI. 
        
        :type CustomSecurityGroupIds: list
        :param CustomSecurityGroupIds: 
        
          An array containing the layer custom security group IDs.
        
          - *(string) --* 
        
        :type Packages: list
        :param Packages: 
        
          An array of ``Package`` objects that describes the layer packages.
        
          - *(string) --* 
        
        :type VolumeConfigurations: list
        :param VolumeConfigurations: 
        
          A ``VolumeConfigurations`` object that describes the layer\'s Amazon EBS volumes.
        
          - *(dict) --* 
        
            Describes an Amazon EBS volume configuration.
        
            - **MountPoint** *(string) --* **[REQUIRED]** 
        
              The volume mount point. For example \"/dev/sdh\".
        
            - **RaidLevel** *(integer) --* 
        
              The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .
        
            - **NumberOfDisks** *(integer) --* **[REQUIRED]** 
        
              The number of disks in the volume.
        
            - **Size** *(integer) --* **[REQUIRED]** 
        
              The volume size.
        
            - **VolumeType** *(string) --* 
        
              The volume type. For more information, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ .
        
              * ``standard`` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB. 
               
              * ``io1`` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB. 
               
              * ``gp2`` - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB. 
               
              * ``st1`` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB. 
               
              * ``sc1`` - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB. 
               
            - **Iops** *(integer) --* 
        
              For PIOPS volumes, the IOPS per disk.
        
            - **Encrypted** *(boolean) --* 
        
              Specifies whether an Amazon EBS volume is encrypted. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ .
        
        :type EnableAutoHealing: boolean
        :param EnableAutoHealing: 
        
          Whether to disable auto healing for the layer.
        
        :type AutoAssignElasticIps: boolean
        :param AutoAssignElasticIps: 
        
          Whether to automatically assign an `Elastic IP address <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ to the layer\'s instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .
        
        :type AutoAssignPublicIps: boolean
        :param AutoAssignPublicIps: 
        
          For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer\'s instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .
        
        :type CustomRecipes: dict
        :param CustomRecipes: 
        
          A ``LayerCustomRecipes`` object that specifies the layer custom recipes.
        
          - **Setup** *(list) --* 
        
            An array of custom recipe names to be run following a ``setup`` event.
        
            - *(string) --* 
        
          - **Configure** *(list) --* 
        
            An array of custom recipe names to be run following a ``configure`` event.
        
            - *(string) --* 
        
          - **Deploy** *(list) --* 
        
            An array of custom recipe names to be run following a ``deploy`` event.
        
            - *(string) --* 
        
          - **Undeploy** *(list) --* 
        
            An array of custom recipe names to be run following a ``undeploy`` event.
        
            - *(string) --* 
        
          - **Shutdown** *(list) --* 
        
            An array of custom recipe names to be run following a ``shutdown`` event.
        
            - *(string) --* 
        
        :type InstallUpdatesOnBoot: boolean
        :param InstallUpdatesOnBoot: 
        
          Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 
        
          .. note::
        
            To ensure that your instances have the latest security updates, we strongly recommend using the default value of ``true`` .
        
        :type UseEbsOptimizedInstances: boolean
        :param UseEbsOptimizedInstances: 
        
          Whether to use Amazon EBS-optimized instances.
        
        :type LifecycleEventConfiguration: dict
        :param LifecycleEventConfiguration: 
        
          A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.
        
          - **Shutdown** *(dict) --* 
        
            A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.
        
            - **ExecutionTimeout** *(integer) --* 
        
              The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.
        
            - **DelayUntilElbConnectionsDrained** *(boolean) --* 
        
              Whether to enable Elastic Load Balancing connection draining. For more information, see `Connection Draining <http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__  
        
        :rtype: :py:class:`opsworks.Layer`
        :returns: Layer resource
        """
        pass

    def delete(self):
        """
        
         **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteStack>`_
        
        **Request Syntax** 
        ::
        
          response = stack.delete()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_
        
        **Request Syntax** 
        
        ::
        
          stack.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_
        
        **Request Syntax** 
        
        ::
        
          stack.load()
        :returns: None
        """
        pass


class StackSummary(base.ServiceResource):
    name: str
    arn: str
    layers_count: int
    apps_count: int
    instances_count: Dict
    stack_id: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_
        
        **Request Syntax** 
        
        ::
        
          stack_summary.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_
        
        **Request Syntax** 
        
        ::
        
          stack_summary.load()
        :returns: None
        """
        pass


class stacks(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Stack']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          stack_iterator = opsworks.stacks.all()
          
        :rtype: list(:py:class:`opsworks.Stack`)
        :returns: A list of Stack resources
        """
        pass

    
    @classmethod
    def filter(cls, StackIds: List = None) -> List['Stack']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          stack_iterator = opsworks.stacks.filter(
              StackIds=[
                  \'string\',
              ]
          )
        :type StackIds: list
        :param StackIds: 
        
          An array of stack IDs that specify the stacks to be described. If you omit this parameter, ``DescribeStacks`` returns a description of every stack.
        
          - *(string) --* 
        
        :rtype: list(:py:class:`opsworks.Stack`)
        :returns: A list of Stack resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Stack']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          stack_iterator = opsworks.stacks.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`opsworks.Stack`)
        :returns: A list of Stack resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Stack']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          stack_iterator = opsworks.stacks.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`opsworks.Stack`)
        :returns: A list of Stack resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass
