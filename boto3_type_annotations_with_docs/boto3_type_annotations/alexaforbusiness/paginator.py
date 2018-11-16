from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListSkills(Paginator):
    def paginate(self, SkillGroupArn: str = None, EnablementType: str = None, SkillType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSkills>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SkillGroupArn=\'string\',
              EnablementType=\'ENABLED\'|\'PENDING\',
              SkillType=\'PUBLIC\'|\'PRIVATE\'|\'ALL\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SkillGroupArn: string
        :param SkillGroupArn: 
        
          The ARN of the skill group for which to list enabled skills. Required.
        
        :type EnablementType: string
        :param EnablementType: 
        
          Whether the skill is enabled under the user\'s account, or if it requires linking to be used.
        
        :type SkillType: string
        :param SkillType: 
        
          Whether the skill is publicly available or is a private skill.
        
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
                \'SkillSummaries\': [
                    {
                        \'SkillId\': \'string\',
                        \'SkillName\': \'string\',
                        \'SupportsLinking\': True|False,
                        \'EnablementType\': \'ENABLED\'|\'PENDING\',
                        \'SkillType\': \'PUBLIC\'|\'PRIVATE\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SkillSummaries** *(list) --* 
        
              The list of enabled skills requested. Required.
        
              - *(dict) --* 
        
                The summary of skills.
        
                - **SkillId** *(string) --* 
        
                  The ARN of the skill summary.
        
                - **SkillName** *(string) --* 
        
                  The name of the skill.
        
                - **SupportsLinking** *(boolean) --* 
        
                  Linking support for a skill.
        
                - **EnablementType** *(string) --* 
        
                  Whether the skill is enabled under the user\'s account, or if it requires linking to be used.
        
                - **SkillType** *(string) --* 
        
                  Whether the skill is publicly available or is a private skill.
        
        """
        pass


class ListTags(Paginator):
    def paginate(self, Arn: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Arn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Arn: string
        :param Arn: **[REQUIRED]** 
        
          The ARN of the specified resource for which to list tags.
        
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
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              The tags requested for the specified resource.
        
              - *(dict) --* 
        
                A key-value pair that can be associated with a resource. 
        
                - **Key** *(string) --* 
        
                  The key of a tag. Tag keys are case-sensitive. 
        
                - **Value** *(string) --* 
        
                  The value of a tag. Tag values are case-sensitive and can be null.
        
        """
        pass


class SearchDevices(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchDevices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'ASC\'|\'DESC\'
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          The filters to use to list a specified set of devices. Supported filter keys are DeviceName, DeviceStatus, DeviceStatusDetailCode, RoomName, DeviceType, DeviceSerialNumber, UnassociatedOnly, and ConnectionStatus (ONLINE and OFFLINE).
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The values of a filter.
        
              - *(string) --* 
        
        :type SortCriteria: list
        :param SortCriteria: 
        
          The sort order to use in listing the specified set of devices. Supported sort keys are DeviceName, DeviceStatus, RoomName, DeviceType, DeviceSerialNumber, and ConnectionStatus.
        
          - *(dict) --* 
        
            An object representing a sort criteria. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The sort key of a sort object.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The sort value of a sort object.
        
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
                \'Devices\': [
                    {
                        \'DeviceArn\': \'string\',
                        \'DeviceSerialNumber\': \'string\',
                        \'DeviceType\': \'string\',
                        \'DeviceName\': \'string\',
                        \'SoftwareVersion\': \'string\',
                        \'MacAddress\': \'string\',
                        \'DeviceStatus\': \'READY\'|\'PENDING\'|\'WAS_OFFLINE\'|\'DEREGISTERED\',
                        \'RoomArn\': \'string\',
                        \'RoomName\': \'string\',
                        \'DeviceStatusInfo\': {
                            \'DeviceStatusDetails\': [
                                {
                                    \'Code\': \'DEVICE_SOFTWARE_UPDATE_NEEDED\'|\'DEVICE_WAS_OFFLINE\'
                                },
                            ],
                            \'ConnectionStatus\': \'ONLINE\'|\'OFFLINE\'
                        }
                    },
                ],
                \'TotalCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Devices** *(list) --* 
        
              The devices that meet the specified set of filter criteria, in sort order.
        
              - *(dict) --* 
        
                Device attributes.
        
                - **DeviceArn** *(string) --* 
        
                  The ARN of a device.
        
                - **DeviceSerialNumber** *(string) --* 
        
                  The serial number of a device.
        
                - **DeviceType** *(string) --* 
        
                  The type of a device.
        
                - **DeviceName** *(string) --* 
        
                  The name of a device.
        
                - **SoftwareVersion** *(string) --* 
        
                  The software version of a device.
        
                - **MacAddress** *(string) --* 
        
                  The MAC address of a device.
        
                - **DeviceStatus** *(string) --* 
        
                  The status of a device.
        
                - **RoomArn** *(string) --* 
        
                  The room ARN associated with a device.
        
                - **RoomName** *(string) --* 
        
                  The name of the room associated with a device.
        
                - **DeviceStatusInfo** *(dict) --* 
        
                  Detailed information about a device\'s status.
        
                  - **DeviceStatusDetails** *(list) --* 
        
                    One or more device status detail descriptions.
        
                    - *(dict) --* 
        
                      Details of a device’s status.
        
                      - **Code** *(string) --* 
        
                        The device status detail code.
        
                  - **ConnectionStatus** *(string) --* 
        
                    The latest available information about the connection status of a device. 
        
            - **TotalCount** *(integer) --* 
        
              The total number of devices returned.
        
        """
        pass


class SearchProfiles(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchProfiles>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'ASC\'|\'DESC\'
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          The filters to use to list a specified set of room profiles. Supported filter keys are ProfileName and Address. Required. 
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The values of a filter.
        
              - *(string) --* 
        
        :type SortCriteria: list
        :param SortCriteria: 
        
          The sort order to use in listing the specified set of room profiles. Supported sort keys are ProfileName and Address.
        
          - *(dict) --* 
        
            An object representing a sort criteria. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The sort key of a sort object.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The sort value of a sort object.
        
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
                \'Profiles\': [
                    {
                        \'ProfileArn\': \'string\',
                        \'ProfileName\': \'string\',
                        \'IsDefault\': True|False,
                        \'Address\': \'string\',
                        \'Timezone\': \'string\',
                        \'DistanceUnit\': \'METRIC\'|\'IMPERIAL\',
                        \'TemperatureUnit\': \'FAHRENHEIT\'|\'CELSIUS\',
                        \'WakeWord\': \'ALEXA\'|\'AMAZON\'|\'ECHO\'|\'COMPUTER\'
                    },
                ],
                \'TotalCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Profiles** *(list) --* 
        
              The profiles that meet the specified set of filter criteria, in sort order.
        
              - *(dict) --* 
        
                The data of a room profile.
        
                - **ProfileArn** *(string) --* 
        
                  The ARN of a room profile.
        
                - **ProfileName** *(string) --* 
        
                  The name of a room profile.
        
                - **IsDefault** *(boolean) --* 
        
                  Retrieves if the profile data is default or not.
        
                - **Address** *(string) --* 
        
                  The address of a room profile.
        
                - **Timezone** *(string) --* 
        
                  The timezone of a room profile.
        
                - **DistanceUnit** *(string) --* 
        
                  The distance unit of a room profile.
        
                - **TemperatureUnit** *(string) --* 
        
                  The temperature unit of a room profile.
        
                - **WakeWord** *(string) --* 
        
                  The wake word of a room profile.
        
            - **TotalCount** *(integer) --* 
        
              The total number of room profiles returned.
        
        """
        pass


class SearchRooms(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchRooms>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'ASC\'|\'DESC\'
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          The filters to use to list a specified set of rooms. The supported filter keys are RoomName and ProfileName.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The values of a filter.
        
              - *(string) --* 
        
        :type SortCriteria: list
        :param SortCriteria: 
        
          The sort order to use in listing the specified set of rooms. The supported sort keys are RoomName and ProfileName.
        
          - *(dict) --* 
        
            An object representing a sort criteria. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The sort key of a sort object.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The sort value of a sort object.
        
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
                \'Rooms\': [
                    {
                        \'RoomArn\': \'string\',
                        \'RoomName\': \'string\',
                        \'Description\': \'string\',
                        \'ProviderCalendarId\': \'string\',
                        \'ProfileArn\': \'string\',
                        \'ProfileName\': \'string\'
                    },
                ],
                \'TotalCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Rooms** *(list) --* 
        
              The rooms that meet the specified set of filter criteria, in sort order.
        
              - *(dict) --* 
        
                The data of a room.
        
                - **RoomArn** *(string) --* 
        
                  The ARN of a room.
        
                - **RoomName** *(string) --* 
        
                  The name of a room.
        
                - **Description** *(string) --* 
        
                  The description of a room.
        
                - **ProviderCalendarId** *(string) --* 
        
                  The provider calendar ARN of a room.
        
                - **ProfileArn** *(string) --* 
        
                  The profile ARN of a room.
        
                - **ProfileName** *(string) --* 
        
                  The profile name of a room.
        
            - **TotalCount** *(integer) --* 
        
              The total number of rooms returned.
        
        """
        pass


class SearchSkillGroups(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchSkillGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'ASC\'|\'DESC\'
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          The filters to use to list a specified set of skill groups. The supported filter key is SkillGroupName. 
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The values of a filter.
        
              - *(string) --* 
        
        :type SortCriteria: list
        :param SortCriteria: 
        
          The sort order to use in listing the specified set of skill groups. The supported sort key is SkillGroupName. 
        
          - *(dict) --* 
        
            An object representing a sort criteria. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The sort key of a sort object.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The sort value of a sort object.
        
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
                \'SkillGroups\': [
                    {
                        \'SkillGroupArn\': \'string\',
                        \'SkillGroupName\': \'string\',
                        \'Description\': \'string\'
                    },
                ],
                \'TotalCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SkillGroups** *(list) --* 
        
              The skill groups that meet the filter criteria, in sort order.
        
              - *(dict) --* 
        
                The attributes of a skill group.
        
                - **SkillGroupArn** *(string) --* 
        
                  The skill group ARN of a skill group.
        
                - **SkillGroupName** *(string) --* 
        
                  The skill group name of a skill group.
        
                - **Description** *(string) --* 
        
                  The description of a skill group.
        
            - **TotalCount** *(integer) --* 
        
              The total number of skill groups returned.
        
        """
        pass


class SearchUsers(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchUsers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'ASC\'|\'DESC\'
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          The filters to use for listing a specific set of users. Required. Supported filter keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The values of a filter.
        
              - *(string) --* 
        
        :type SortCriteria: list
        :param SortCriteria: 
        
          The sort order to use in listing the filtered set of users. Required. Supported sort keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.
        
          - *(dict) --* 
        
            An object representing a sort criteria. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The sort key of a sort object.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The sort value of a sort object.
        
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
                \'Users\': [
                    {
                        \'UserArn\': \'string\',
                        \'FirstName\': \'string\',
                        \'LastName\': \'string\',
                        \'Email\': \'string\',
                        \'EnrollmentStatus\': \'INITIALIZED\'|\'PENDING\'|\'REGISTERED\'|\'DISASSOCIATING\'|\'DEREGISTERING\',
                        \'EnrollmentId\': \'string\'
                    },
                ],
                \'TotalCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Users** *(list) --* 
        
              The users that meet the specified set of filter criteria, in sort order.
        
              - *(dict) --* 
        
                Information related to a user.
        
                - **UserArn** *(string) --* 
        
                  The ARN of a user.
        
                - **FirstName** *(string) --* 
        
                  The first name of a user.
        
                - **LastName** *(string) --* 
        
                  The last name of a user.
        
                - **Email** *(string) --* 
        
                  The email of a user.
        
                - **EnrollmentStatus** *(string) --* 
        
                  The enrollment status of a user.
        
                - **EnrollmentId** *(string) --* 
        
                  The enrollment ARN of a user.
        
            - **TotalCount** *(integer) --* 
        
              The total number of users returned.
        
        """
        pass
