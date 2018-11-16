from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def approve_skill(self, SkillId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ApproveSkill>`_
        
        **Request Syntax** 
        ::
        
          response = client.approve_skill(
              SkillId=\'string\'
          )
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The unique identifier of the skill.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def associate_contact_with_address_book(self, ContactArn: str, AddressBookArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/AssociateContactWithAddressBook>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_contact_with_address_book(
              ContactArn=\'string\',
              AddressBookArn=\'string\'
          )
        :type ContactArn: string
        :param ContactArn: **[REQUIRED]** 
        
          The ARN of the contact to associate with an address book.
        
        :type AddressBookArn: string
        :param AddressBookArn: **[REQUIRED]** 
        
          The ARN of the address book with which to associate the contact.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def associate_device_with_room(self, DeviceArn: str = None, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/AssociateDeviceWithRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_device_with_room(
              DeviceArn=\'string\',
              RoomArn=\'string\'
          )
        :type DeviceArn: string
        :param DeviceArn: 
        
          The ARN of the device to associate to a room. Required.
        
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room with which to associate the device. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def associate_skill_group_with_room(self, SkillGroupArn: str = None, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/AssociateSkillGroupWithRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_skill_group_with_room(
              SkillGroupArn=\'string\',
              RoomArn=\'string\'
          )
        :type SkillGroupArn: string
        :param SkillGroupArn: 
        
          The ARN of the skill group to associate with a room. Required.
        
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room with which to associate the skill group. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def associate_skill_with_skill_group(self, SkillId: str, SkillGroupArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/AssociateSkillWithSkillGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_skill_with_skill_group(
              SkillGroupArn=\'string\',
              SkillId=\'string\'
          )
        :type SkillGroupArn: string
        :param SkillGroupArn: 
        
          The ARN of the skill group to associate the skill to. Required.
        
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The unique identifier of the skill.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        """
        
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def create_address_book(self, Name: str, Description: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateAddressBook>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_address_book(
              Name=\'string\',
              Description=\'string\',
              ClientRequestToken=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the address book.
        
        :type Description: string
        :param Description: 
        
          The description of the address book.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique, user-specified identifier for the request that ensures idempotency.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AddressBookArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AddressBookArn** *(string) --* 
        
              The ARN of the newly created address book.
        
        """
        pass

    def create_conference_provider(self, ConferenceProviderName: str, ConferenceProviderType: str, MeetingSetting: Dict, IPDialIn: Dict = None, PSTNDialIn: Dict = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateConferenceProvider>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_conference_provider(
              ConferenceProviderName=\'string\',
              ConferenceProviderType=\'CHIME\'|\'BLUEJEANS\'|\'FUZE\'|\'GOOGLE_HANGOUTS\'|\'POLYCOM\'|\'RINGCENTRAL\'|\'SKYPE_FOR_BUSINESS\'|\'WEBEX\'|\'ZOOM\'|\'CUSTOM\',
              IPDialIn={
                  \'Endpoint\': \'string\',
                  \'CommsProtocol\': \'SIP\'|\'SIPS\'|\'H323\'
              },
              PSTNDialIn={
                  \'CountryCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'OneClickIdDelay\': \'string\',
                  \'OneClickPinDelay\': \'string\'
              },
              MeetingSetting={
                  \'RequirePin\': \'YES\'|\'NO\'|\'OPTIONAL\'
              },
              ClientRequestToken=\'string\'
          )
        :type ConferenceProviderName: string
        :param ConferenceProviderName: **[REQUIRED]** 
        
          The name of the conference provider.
        
        :type ConferenceProviderType: string
        :param ConferenceProviderType: **[REQUIRED]** 
        
          Represents a type within a list of predefined types.
        
        :type IPDialIn: dict
        :param IPDialIn: 
        
          The IP endpoint and protocol for calling.
        
          - **Endpoint** *(string) --* **[REQUIRED]** 
        
            The IP address.
        
          - **CommsProtocol** *(string) --* **[REQUIRED]** 
        
            The protocol, including SIP, SIPS, and H323.
        
        :type PSTNDialIn: dict
        :param PSTNDialIn: 
        
          The information for PSTN conferencing.
        
          - **CountryCode** *(string) --* **[REQUIRED]** 
        
            The zip code.
        
          - **PhoneNumber** *(string) --* **[REQUIRED]** 
        
            The phone number to call to join the conference.
        
          - **OneClickIdDelay** *(string) --* **[REQUIRED]** 
        
            The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
        
          - **OneClickPinDelay** *(string) --* **[REQUIRED]** 
        
            The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
        
        :type MeetingSetting: dict
        :param MeetingSetting: **[REQUIRED]** 
        
          The meeting settings for the conference provider.
        
          - **RequirePin** *(string) --* **[REQUIRED]** 
        
            The values that indicate whether the pin is always required.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          The request token of the client.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ConferenceProviderArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ConferenceProviderArn** *(string) --* 
        
              The ARN of the newly-created conference provider.
        
        """
        pass

    def create_contact(self, FirstName: str, PhoneNumber: str, DisplayName: str = None, LastName: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateContact>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_contact(
              DisplayName=\'string\',
              FirstName=\'string\',
              LastName=\'string\',
              PhoneNumber=\'string\',
              ClientRequestToken=\'string\'
          )
        :type DisplayName: string
        :param DisplayName: 
        
          The name of the contact to display on the console.
        
        :type FirstName: string
        :param FirstName: **[REQUIRED]** 
        
          The first name of the contact that is used to call the contact on the device.
        
        :type LastName: string
        :param LastName: 
        
          The last name of the contact that is used to call the contact on the device.
        
        :type PhoneNumber: string
        :param PhoneNumber: **[REQUIRED]** 
        
          The phone number of the contact in E.164 format.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique, user-specified identifier for this request that ensures idempotency.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ContactArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ContactArn** *(string) --* 
        
              The ARN of the newly created address book.
        
        """
        pass

    def create_profile(self, ProfileName: str, Timezone: str, Address: str, DistanceUnit: str, TemperatureUnit: str, WakeWord: str, ClientRequestToken: str = None, SetupModeDisabled: bool = None, MaxVolumeLimit: int = None, PSTNEnabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_profile(
              ProfileName=\'string\',
              Timezone=\'string\',
              Address=\'string\',
              DistanceUnit=\'METRIC\'|\'IMPERIAL\',
              TemperatureUnit=\'FAHRENHEIT\'|\'CELSIUS\',
              WakeWord=\'ALEXA\'|\'AMAZON\'|\'ECHO\'|\'COMPUTER\',
              ClientRequestToken=\'string\',
              SetupModeDisabled=True|False,
              MaxVolumeLimit=123,
              PSTNEnabled=True|False
          )
        :type ProfileName: string
        :param ProfileName: **[REQUIRED]** 
        
          The name of a room profile.
        
        :type Timezone: string
        :param Timezone: **[REQUIRED]** 
        
          The time zone used by a room profile.
        
        :type Address: string
        :param Address: **[REQUIRED]** 
        
          The valid address for the room.
        
        :type DistanceUnit: string
        :param DistanceUnit: **[REQUIRED]** 
        
          The distance unit to be used by devices in the profile.
        
        :type TemperatureUnit: string
        :param TemperatureUnit: **[REQUIRED]** 
        
          The temperature unit to be used by devices in the profile.
        
        :type WakeWord: string
        :param WakeWord: **[REQUIRED]** 
        
          A wake word for Alexa, Echo, Amazon, or a computer.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          The user-specified token that is used during the creation of a profile.
        
          This field is autopopulated if not provided.
        
        :type SetupModeDisabled: boolean
        :param SetupModeDisabled: 
        
          Whether room profile setup is enabled.
        
        :type MaxVolumeLimit: integer
        :param MaxVolumeLimit: 
        
          The maximum volume limit for a room profile.
        
        :type PSTNEnabled: boolean
        :param PSTNEnabled: 
        
          Whether PSTN calling is enabled.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ProfileArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ProfileArn** *(string) --* 
        
              The ARN of the newly created room profile in the response.
        
        """
        pass

    def create_room(self, RoomName: str, Description: str = None, ProfileArn: str = None, ProviderCalendarId: str = None, ClientRequestToken: str = None, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_room(
              RoomName=\'string\',
              Description=\'string\',
              ProfileArn=\'string\',
              ProviderCalendarId=\'string\',
              ClientRequestToken=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type RoomName: string
        :param RoomName: **[REQUIRED]** 
        
          The name for the room.
        
        :type Description: string
        :param Description: 
        
          The description for the room.
        
        :type ProfileArn: string
        :param ProfileArn: 
        
          The profile ARN for the room.
        
        :type ProviderCalendarId: string
        :param ProviderCalendarId: 
        
          The calendar ARN for the room.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique, user-specified identifier for this request that ensures idempotency. 
        
          This field is autopopulated if not provided.
        
        :type Tags: list
        :param Tags: 
        
          The tags for the room.
        
          - *(dict) --* 
        
            A key-value pair that can be associated with a resource. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a tag. Tag keys are case-sensitive. 
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The value of a tag. Tag values are case-sensitive and can be null.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RoomArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RoomArn** *(string) --* 
        
              The ARN of the newly created room in the response.
        
        """
        pass

    def create_skill_group(self, SkillGroupName: str, Description: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateSkillGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_skill_group(
              SkillGroupName=\'string\',
              Description=\'string\',
              ClientRequestToken=\'string\'
          )
        :type SkillGroupName: string
        :param SkillGroupName: **[REQUIRED]** 
        
          The name for the skill group.
        
        :type Description: string
        :param Description: 
        
          The description for the skill group.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique, user-specified identifier for this request that ensures idempotency. 
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SkillGroupArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SkillGroupArn** *(string) --* 
        
              The ARN of the newly created skill group in the response.
        
        """
        pass

    def create_user(self, UserId: str, FirstName: str = None, LastName: str = None, Email: str = None, ClientRequestToken: str = None, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/CreateUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_user(
              UserId=\'string\',
              FirstName=\'string\',
              LastName=\'string\',
              Email=\'string\',
              ClientRequestToken=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The ARN for the user.
        
        :type FirstName: string
        :param FirstName: 
        
          The first name for the user.
        
        :type LastName: string
        :param LastName: 
        
          The last name for the user.
        
        :type Email: string
        :param Email: 
        
          The email address for the user.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique, user-specified identifier for this request that ensures idempotency. 
        
          This field is autopopulated if not provided.
        
        :type Tags: list
        :param Tags: 
        
          The tags for the user.
        
          - *(dict) --* 
        
            A key-value pair that can be associated with a resource. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a tag. Tag keys are case-sensitive. 
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The value of a tag. Tag values are case-sensitive and can be null.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UserArn** *(string) --* 
        
              The ARN of the newly created user in the response.
        
        """
        pass

    def delete_address_book(self, AddressBookArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteAddressBook>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_address_book(
              AddressBookArn=\'string\'
          )
        :type AddressBookArn: string
        :param AddressBookArn: **[REQUIRED]** 
        
          The ARN of the address book to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_conference_provider(self, ConferenceProviderArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteConferenceProvider>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_conference_provider(
              ConferenceProviderArn=\'string\'
          )
        :type ConferenceProviderArn: string
        :param ConferenceProviderArn: **[REQUIRED]** 
        
          The ARN of the conference provider.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_contact(self, ContactArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteContact>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_contact(
              ContactArn=\'string\'
          )
        :type ContactArn: string
        :param ContactArn: **[REQUIRED]** 
        
          The ARN of the contact to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_device(self, DeviceArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteDevice>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_device(
              DeviceArn=\'string\'
          )
        :type DeviceArn: string
        :param DeviceArn: **[REQUIRED]** 
        
          The ARN of the device for which to request details.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_profile(self, ProfileArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_profile(
              ProfileArn=\'string\'
          )
        :type ProfileArn: string
        :param ProfileArn: 
        
          The ARN of the room profile to delete. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_room(self, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_room(
              RoomArn=\'string\'
          )
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room to delete. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_room_skill_parameter(self, SkillId: str, ParameterKey: str, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteRoomSkillParameter>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_room_skill_parameter(
              RoomArn=\'string\',
              SkillId=\'string\',
              ParameterKey=\'string\'
          )
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room from which to remove the room skill parameter details.
        
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The ID of the skill from which to remove the room skill parameter details.
        
        :type ParameterKey: string
        :param ParameterKey: **[REQUIRED]** 
        
          The room skill parameter key for which to remove details.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_skill_authorization(self, SkillId: str, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteSkillAuthorization>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_skill_authorization(
              SkillId=\'string\',
              RoomArn=\'string\'
          )
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The unique identifier of a skill.
        
        :type RoomArn: string
        :param RoomArn: 
        
          The room that the skill is authorized for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_skill_group(self, SkillGroupArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteSkillGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_skill_group(
              SkillGroupArn=\'string\'
          )
        :type SkillGroupArn: string
        :param SkillGroupArn: 
        
          The ARN of the skill group to delete. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_user(self, EnrollmentId: str, UserArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DeleteUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_user(
              UserArn=\'string\',
              EnrollmentId=\'string\'
          )
        :type UserArn: string
        :param UserArn: 
        
          The ARN of the user to delete in the organization. Required.
        
        :type EnrollmentId: string
        :param EnrollmentId: **[REQUIRED]** 
        
          The ARN of the user\'s enrollment in the organization. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_contact_from_address_book(self, ContactArn: str, AddressBookArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DisassociateContactFromAddressBook>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_contact_from_address_book(
              ContactArn=\'string\',
              AddressBookArn=\'string\'
          )
        :type ContactArn: string
        :param ContactArn: **[REQUIRED]** 
        
          The ARN of the contact to disassociate from an address book.
        
        :type AddressBookArn: string
        :param AddressBookArn: **[REQUIRED]** 
        
          The ARN of the address from which to disassociate the contact.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_device_from_room(self, DeviceArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DisassociateDeviceFromRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_device_from_room(
              DeviceArn=\'string\'
          )
        :type DeviceArn: string
        :param DeviceArn: 
        
          The ARN of the device to disassociate from a room. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_skill_from_skill_group(self, SkillId: str, SkillGroupArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DisassociateSkillFromSkillGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_skill_from_skill_group(
              SkillGroupArn=\'string\',
              SkillId=\'string\'
          )
        :type SkillGroupArn: string
        :param SkillGroupArn: 
        
          The unique identifier of a skill. Required.
        
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The ARN of a skill group to associate to a skill.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_skill_group_from_room(self, SkillGroupArn: str = None, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/DisassociateSkillGroupFromRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_skill_group_from_room(
              SkillGroupArn=\'string\',
              RoomArn=\'string\'
          )
        :type SkillGroupArn: string
        :param SkillGroupArn: 
        
          The ARN of the skill group to disassociate from a room. Required.
        
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room from which the skill group is to be disassociated. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def forget_smart_home_appliances(self, RoomArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ForgetSmartHomeAppliances>`_
        
        **Request Syntax** 
        ::
        
          response = client.forget_smart_home_appliances(
              RoomArn=\'string\'
          )
        :type RoomArn: string
        :param RoomArn: **[REQUIRED]** 
        
          The room that the appliances are associated with.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        """
        
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        
        :returns: The presigned url
        """
        pass

    def get_address_book(self, AddressBookArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetAddressBook>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_address_book(
              AddressBookArn=\'string\'
          )
        :type AddressBookArn: string
        :param AddressBookArn: **[REQUIRED]** 
        
          The ARN of the address book for which to request details.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AddressBook\': {
                    \'AddressBookArn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AddressBook** *(dict) --* 
        
              The details of the requested address book.
        
              - **AddressBookArn** *(string) --* 
        
                The ARN of the address book.
        
              - **Name** *(string) --* 
        
                The name of the address book.
        
              - **Description** *(string) --* 
        
                The description of the address book.
        
        """
        pass

    def get_conference_preference(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetConferencePreference>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_conference_preference()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Preference\': {
                    \'DefaultConferenceProviderArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Preference** *(dict) --* 
        
              The conference preference.
        
              - **DefaultConferenceProviderArn** *(string) --* 
        
                The ARN of the default conference provider.
        
        """
        pass

    def get_conference_provider(self, ConferenceProviderArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetConferenceProvider>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_conference_provider(
              ConferenceProviderArn=\'string\'
          )
        :type ConferenceProviderArn: string
        :param ConferenceProviderArn: **[REQUIRED]** 
        
          The ARN of the newly created conference provider.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ConferenceProvider\': {
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'Type\': \'CHIME\'|\'BLUEJEANS\'|\'FUZE\'|\'GOOGLE_HANGOUTS\'|\'POLYCOM\'|\'RINGCENTRAL\'|\'SKYPE_FOR_BUSINESS\'|\'WEBEX\'|\'ZOOM\'|\'CUSTOM\',
                    \'IPDialIn\': {
                        \'Endpoint\': \'string\',
                        \'CommsProtocol\': \'SIP\'|\'SIPS\'|\'H323\'
                    },
                    \'PSTNDialIn\': {
                        \'CountryCode\': \'string\',
                        \'PhoneNumber\': \'string\',
                        \'OneClickIdDelay\': \'string\',
                        \'OneClickPinDelay\': \'string\'
                    },
                    \'MeetingSetting\': {
                        \'RequirePin\': \'YES\'|\'NO\'|\'OPTIONAL\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ConferenceProvider** *(dict) --* 
        
              The conference provider.
        
              - **Arn** *(string) --* 
        
                The ARN of the newly created conference provider.
        
              - **Name** *(string) --* 
        
                The name of the conference provider.
        
              - **Type** *(string) --* 
        
                The type of conference providers.
        
              - **IPDialIn** *(dict) --* 
        
                The IP endpoint and protocol for calling.
        
                - **Endpoint** *(string) --* 
        
                  The IP address.
        
                - **CommsProtocol** *(string) --* 
        
                  The protocol, including SIP, SIPS, and H323.
        
              - **PSTNDialIn** *(dict) --* 
        
                The information for PSTN conferencing.
        
                - **CountryCode** *(string) --* 
        
                  The zip code.
        
                - **PhoneNumber** *(string) --* 
        
                  The phone number to call to join the conference.
        
                - **OneClickIdDelay** *(string) --* 
        
                  The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
        
                - **OneClickPinDelay** *(string) --* 
        
                  The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
        
              - **MeetingSetting** *(dict) --* 
        
                The meeting settings for the conference provider.
        
                - **RequirePin** *(string) --* 
        
                  The values that indicate whether the pin is always required.
        
        """
        pass

    def get_contact(self, ContactArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetContact>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_contact(
              ContactArn=\'string\'
          )
        :type ContactArn: string
        :param ContactArn: **[REQUIRED]** 
        
          The ARN of the contact for which to request details.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Contact\': {
                    \'ContactArn\': \'string\',
                    \'DisplayName\': \'string\',
                    \'FirstName\': \'string\',
                    \'LastName\': \'string\',
                    \'PhoneNumber\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Contact** *(dict) --* 
        
              The details of the requested contact.
        
              - **ContactArn** *(string) --* 
        
                The ARN of the contact.
        
              - **DisplayName** *(string) --* 
        
                The name of the contact to display on the console.
        
              - **FirstName** *(string) --* 
        
                The first name of the contact, used to call the contact on the device.
        
              - **LastName** *(string) --* 
        
                The last name of the contact, used to call the contact on the device.
        
              - **PhoneNumber** *(string) --* 
        
                The phone number of the contact.
        
        """
        pass

    def get_device(self, DeviceArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetDevice>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_device(
              DeviceArn=\'string\'
          )
        :type DeviceArn: string
        :param DeviceArn: 
        
          The ARN of the device for which to request details. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Device\': {
                    \'DeviceArn\': \'string\',
                    \'DeviceSerialNumber\': \'string\',
                    \'DeviceType\': \'string\',
                    \'DeviceName\': \'string\',
                    \'SoftwareVersion\': \'string\',
                    \'MacAddress\': \'string\',
                    \'RoomArn\': \'string\',
                    \'DeviceStatus\': \'READY\'|\'PENDING\'|\'WAS_OFFLINE\'|\'DEREGISTERED\',
                    \'DeviceStatusInfo\': {
                        \'DeviceStatusDetails\': [
                            {
                                \'Code\': \'DEVICE_SOFTWARE_UPDATE_NEEDED\'|\'DEVICE_WAS_OFFLINE\'
                            },
                        ],
                        \'ConnectionStatus\': \'ONLINE\'|\'OFFLINE\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Device** *(dict) --* 
        
              The details of the device requested. Required.
        
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
        
              - **RoomArn** *(string) --* 
        
                The room ARN of a device.
        
              - **DeviceStatus** *(string) --* 
        
                The status of a device. If the status is not READY, check the DeviceStatusInfo value for details.
        
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
        
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_profile(self, ProfileArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_profile(
              ProfileArn=\'string\'
          )
        :type ProfileArn: string
        :param ProfileArn: 
        
          The ARN of the room profile for which to request details. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Profile\': {
                    \'ProfileArn\': \'string\',
                    \'ProfileName\': \'string\',
                    \'IsDefault\': True|False,
                    \'Address\': \'string\',
                    \'Timezone\': \'string\',
                    \'DistanceUnit\': \'METRIC\'|\'IMPERIAL\',
                    \'TemperatureUnit\': \'FAHRENHEIT\'|\'CELSIUS\',
                    \'WakeWord\': \'ALEXA\'|\'AMAZON\'|\'ECHO\'|\'COMPUTER\',
                    \'SetupModeDisabled\': True|False,
                    \'MaxVolumeLimit\': 123,
                    \'PSTNEnabled\': True|False,
                    \'AddressBookArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Profile** *(dict) --* 
        
              The details of the room profile requested. Required.
        
              - **ProfileArn** *(string) --* 
        
                The ARN of a room profile.
        
              - **ProfileName** *(string) --* 
        
                The name of a room profile.
        
              - **IsDefault** *(boolean) --* 
        
                Retrieves if the profile is default or not.
        
              - **Address** *(string) --* 
        
                The address of a room profile.
        
              - **Timezone** *(string) --* 
        
                The time zone of a room profile.
        
              - **DistanceUnit** *(string) --* 
        
                The distance unit of a room profile.
        
              - **TemperatureUnit** *(string) --* 
        
                The temperature unit of a room profile.
        
              - **WakeWord** *(string) --* 
        
                The wake word of a room profile.
        
              - **SetupModeDisabled** *(boolean) --* 
        
                The setup mode of a room profile.
        
              - **MaxVolumeLimit** *(integer) --* 
        
                The max volume limit of a room profile.
        
              - **PSTNEnabled** *(boolean) --* 
        
                The PSTN setting of a room profile.
        
              - **AddressBookArn** *(string) --* 
        
                The ARN of the address book.
        
        """
        pass

    def get_room(self, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_room(
              RoomArn=\'string\'
          )
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room for which to request details. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Room\': {
                    \'RoomArn\': \'string\',
                    \'RoomName\': \'string\',
                    \'Description\': \'string\',
                    \'ProviderCalendarId\': \'string\',
                    \'ProfileArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Room** *(dict) --* 
        
              The details of the room requested.
        
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
        
        """
        pass

    def get_room_skill_parameter(self, SkillId: str, ParameterKey: str, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetRoomSkillParameter>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_room_skill_parameter(
              RoomArn=\'string\',
              SkillId=\'string\',
              ParameterKey=\'string\'
          )
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room from which to get the room skill parameter details. 
        
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The ARN of the skill from which to get the room skill parameter details. Required.
        
        :type ParameterKey: string
        :param ParameterKey: **[REQUIRED]** 
        
          The room skill parameter key for which to get details. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RoomSkillParameter\': {
                    \'ParameterKey\': \'string\',
                    \'ParameterValue\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RoomSkillParameter** *(dict) --* 
        
              The details of the room skill parameter requested. Required.
        
              - **ParameterKey** *(string) --* 
        
                The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes “DEFAULT” or “SCOPE” as valid values.
        
              - **ParameterValue** *(string) --* 
        
                The parameter value of a room skill parameter.
        
        """
        pass

    def get_skill_group(self, SkillGroupArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/GetSkillGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_skill_group(
              SkillGroupArn=\'string\'
          )
        :type SkillGroupArn: string
        :param SkillGroupArn: 
        
          The ARN of the skill group for which to get details. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SkillGroup\': {
                    \'SkillGroupArn\': \'string\',
                    \'SkillGroupName\': \'string\',
                    \'Description\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SkillGroup** *(dict) --* 
        
              The details of the skill group requested. Required.
        
              - **SkillGroupArn** *(string) --* 
        
                The ARN of a skill group.
        
              - **SkillGroupName** *(string) --* 
        
                The name of a skill group.
        
              - **Description** *(string) --* 
        
                The description of a skill group.
        
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_conference_providers(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListConferenceProviders>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_conference_providers(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          The tokens used for pagination.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of conference providers to be returned, per paginated calls.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ConferenceProviders\': [
                    {
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Type\': \'CHIME\'|\'BLUEJEANS\'|\'FUZE\'|\'GOOGLE_HANGOUTS\'|\'POLYCOM\'|\'RINGCENTRAL\'|\'SKYPE_FOR_BUSINESS\'|\'WEBEX\'|\'ZOOM\'|\'CUSTOM\',
                        \'IPDialIn\': {
                            \'Endpoint\': \'string\',
                            \'CommsProtocol\': \'SIP\'|\'SIPS\'|\'H323\'
                        },
                        \'PSTNDialIn\': {
                            \'CountryCode\': \'string\',
                            \'PhoneNumber\': \'string\',
                            \'OneClickIdDelay\': \'string\',
                            \'OneClickPinDelay\': \'string\'
                        },
                        \'MeetingSetting\': {
                            \'RequirePin\': \'YES\'|\'NO\'|\'OPTIONAL\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ConferenceProviders** *(list) --* 
        
              The conference providers.
        
              - *(dict) --* 
        
                An entity that provides a conferencing solution. Alexa for Business acts as the voice interface and mediator that connects users to their preferred conference provider. Examples of conference providers include Amazon Chime, Zoom, Cisco, and Polycom. 
        
                - **Arn** *(string) --* 
        
                  The ARN of the newly created conference provider.
        
                - **Name** *(string) --* 
        
                  The name of the conference provider.
        
                - **Type** *(string) --* 
        
                  The type of conference providers.
        
                - **IPDialIn** *(dict) --* 
        
                  The IP endpoint and protocol for calling.
        
                  - **Endpoint** *(string) --* 
        
                    The IP address.
        
                  - **CommsProtocol** *(string) --* 
        
                    The protocol, including SIP, SIPS, and H323.
        
                - **PSTNDialIn** *(dict) --* 
        
                  The information for PSTN conferencing.
        
                  - **CountryCode** *(string) --* 
        
                    The zip code.
        
                  - **PhoneNumber** *(string) --* 
        
                    The phone number to call to join the conference.
        
                  - **OneClickIdDelay** *(string) --* 
        
                    The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
        
                  - **OneClickPinDelay** *(string) --* 
        
                    The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
        
                - **MeetingSetting** *(dict) --* 
        
                  The meeting settings for the conference provider.
        
                  - **RequirePin** *(string) --* 
        
                    The values that indicate whether the pin is always required.
        
            - **NextToken** *(string) --* 
        
              The tokens used for pagination.
        
        """
        pass

    def list_device_events(self, DeviceArn: str, EventType: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListDeviceEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_device_events(
              DeviceArn=\'string\',
              EventType=\'CONNECTION_STATUS\'|\'DEVICE_STATUS\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type DeviceArn: string
        :param DeviceArn: **[REQUIRED]** 
        
          The ARN of a device.
        
        :type EventType: string
        :param EventType: 
        
          The event type to filter device events. If EventType isn\'t specified, this returns a list of all device events in reverse chronological order. If EventType is specified, this returns a list of device events for that EventType in reverse chronological order. 
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults. When the end of results is reached, the response has a value of null.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. The default value is 50. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeviceEvents\': [
                    {
                        \'Type\': \'CONNECTION_STATUS\'|\'DEVICE_STATUS\',
                        \'Value\': \'string\',
                        \'Timestamp\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeviceEvents** *(list) --* 
        
              The device events requested for the device ARN.
        
              - *(dict) --* 
        
                The list of device events.
        
                - **Type** *(string) --* 
        
                  The type of device event.
        
                - **Value** *(string) --* 
        
                  The value of the event.
        
                - **Timestamp** *(datetime) --* 
        
                  The time (in epoch) when the event occurred. 
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
        """
        pass

    def list_skills(self, SkillGroupArn: str = None, EnablementType: str = None, SkillType: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSkills>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_skills(
              SkillGroupArn=\'string\',
              EnablementType=\'ENABLED\'|\'PENDING\',
              SkillType=\'PUBLIC\'|\'PRIVATE\'|\'ALL\',
              NextToken=\'string\',
              MaxResults=123
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
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` . Required.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved. Required.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
        """
        pass

    def list_skills_store_categories(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSkillsStoreCategories>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_skills_store_categories(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          The tokens used for pagination.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of categories returned, per paginated calls.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CategoryList\': [
                    {
                        \'CategoryId\': 123,
                        \'CategoryName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CategoryList** *(list) --* 
        
              The list of categories.
        
              - *(dict) --* 
        
                The skill store category that is shown. Alexa skills are assigned a specific skill category during creation, such as News, Social, and Sports.
        
                - **CategoryId** *(integer) --* 
        
                  The ID of the skill store category.
        
                - **CategoryName** *(string) --* 
        
                  The name of the skill store category.
        
            - **NextToken** *(string) --* 
        
              The tokens used for pagination.
        
        """
        pass

    def list_skills_store_skills_by_category(self, CategoryId: int, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSkillsStoreSkillsByCategory>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_skills_store_skills_by_category(
              CategoryId=123,
              NextToken=\'string\',
              MaxResults=123
          )
        :type CategoryId: integer
        :param CategoryId: **[REQUIRED]** 
        
          The category ID for which the skills are being retrieved from the skill store.
        
        :type NextToken: string
        :param NextToken: 
        
          The tokens used for pagination.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of skills returned per paginated calls.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SkillsStoreSkills\': [
                    {
                        \'SkillId\': \'string\',
                        \'SkillName\': \'string\',
                        \'ShortDescription\': \'string\',
                        \'IconUrl\': \'string\',
                        \'SampleUtterances\': [
                            \'string\',
                        ],
                        \'SkillDetails\': {
                            \'ProductDescription\': \'string\',
                            \'InvocationPhrase\': \'string\',
                            \'ReleaseDate\': \'string\',
                            \'EndUserLicenseAgreement\': \'string\',
                            \'GenericKeywords\': [
                                \'string\',
                            ],
                            \'BulletPoints\': [
                                \'string\',
                            ],
                            \'NewInThisVersionBulletPoints\': [
                                \'string\',
                            ],
                            \'SkillTypes\': [
                                \'string\',
                            ],
                            \'Reviews\': {
                                \'string\': \'string\'
                            },
                            \'DeveloperInfo\': {
                                \'DeveloperName\': \'string\',
                                \'PrivacyPolicy\': \'string\',
                                \'Email\': \'string\',
                                \'Url\': \'string\'
                            }
                        },
                        \'SupportsLinking\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SkillsStoreSkills** *(list) --* 
        
              The skill store skills.
        
              - *(dict) --* 
        
                The detailed information about an Alexa skill.
        
                - **SkillId** *(string) --* 
        
                  The ARN of the skill.
        
                - **SkillName** *(string) --* 
        
                  The name of the skill.
        
                - **ShortDescription** *(string) --* 
        
                  Short description about the skill.
        
                - **IconUrl** *(string) --* 
        
                  The URL where the skill icon resides.
        
                - **SampleUtterances** *(list) --* 
        
                  Sample utterances that interact with the skill.
        
                  - *(string) --* 
              
                - **SkillDetails** *(dict) --* 
        
                  Information about the skill.
        
                  - **ProductDescription** *(string) --* 
        
                    The description of the product.
        
                  - **InvocationPhrase** *(string) --* 
        
                    The phrase used to trigger the skill.
        
                  - **ReleaseDate** *(string) --* 
        
                    The date when the skill was released.
        
                  - **EndUserLicenseAgreement** *(string) --* 
        
                    The URL of the end user license agreement.
        
                  - **GenericKeywords** *(list) --* 
        
                    The generic keywords associated with the skill that can be used to find a skill.
        
                    - *(string) --* 
                
                  - **BulletPoints** *(list) --* 
        
                    The details about what the skill supports organized as bullet points.
        
                    - *(string) --* 
                
                  - **NewInThisVersionBulletPoints** *(list) --* 
        
                    The updates added in bullet points.
        
                    - *(string) --* 
                
                  - **SkillTypes** *(list) --* 
        
                    The types of skills.
        
                    - *(string) --* 
                
                  - **Reviews** *(dict) --* 
        
                    The list of reviews for the skill, including Key and Value pair.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **DeveloperInfo** *(dict) --* 
        
                    The details about the developer that published the skill.
        
                    - **DeveloperName** *(string) --* 
        
                      The name of the developer.
        
                    - **PrivacyPolicy** *(string) --* 
        
                      The URL of the privacy policy.
        
                    - **Email** *(string) --* 
        
                      The email of the developer.
        
                    - **Url** *(string) --* 
        
                      The website of the developer.
        
                - **SupportsLinking** *(boolean) --* 
        
                  Linking support for a skill.
        
            - **NextToken** *(string) --* 
        
              The tokens used for pagination.
        
        """
        pass

    def list_smart_home_appliances(self, RoomArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSmartHomeAppliances>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_smart_home_appliances(
              RoomArn=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type RoomArn: string
        :param RoomArn: **[REQUIRED]** 
        
          The room that the appliances are associated with.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of appliances to be returned, per paginated calls.
        
        :type NextToken: string
        :param NextToken: 
        
          The tokens used for pagination.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SmartHomeAppliances\': [
                    {
                        \'FriendlyName\': \'string\',
                        \'Description\': \'string\',
                        \'ManufacturerName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SmartHomeAppliances** *(list) --* 
        
              The smart home appliances.
        
              - *(dict) --* 
        
                A smart home appliance that can connect to a central system. Any domestic device can be a smart appliance. 
        
                - **FriendlyName** *(string) --* 
        
                  The friendly name of the smart home appliance.
        
                - **Description** *(string) --* 
        
                  The description of the smart home appliance.
        
                - **ManufacturerName** *(string) --* 
        
                  The name of the manufacturer of the smart home appliance.
        
            - **NextToken** *(string) --* 
        
              The tokens used for pagination.
        
        """
        pass

    def list_tags(self, Arn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags(
              Arn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type Arn: string
        :param Arn: **[REQUIRED]** 
        
          The ARN of the specified resource for which to list tags.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` . 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
        """
        pass

    def put_conference_preference(self, ConferencePreference: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/PutConferencePreference>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_conference_preference(
              ConferencePreference={
                  \'DefaultConferenceProviderArn\': \'string\'
              }
          )
        :type ConferencePreference: dict
        :param ConferencePreference: **[REQUIRED]** 
        
          The conference preference of a specific conference provider.
        
          - **DefaultConferenceProviderArn** *(string) --* 
        
            The ARN of the default conference provider.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def put_room_skill_parameter(self, SkillId: str, RoomSkillParameter: Dict, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/PutRoomSkillParameter>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_room_skill_parameter(
              RoomArn=\'string\',
              SkillId=\'string\',
              RoomSkillParameter={
                  \'ParameterKey\': \'string\',
                  \'ParameterValue\': \'string\'
              }
          )
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room associated with the room skill parameter. Required.
        
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The ARN of the skill associated with the room skill parameter. Required.
        
        :type RoomSkillParameter: dict
        :param RoomSkillParameter: **[REQUIRED]** 
        
          The updated room skill parameter. Required.
        
          - **ParameterKey** *(string) --* **[REQUIRED]** 
        
            The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes “DEFAULT” or “SCOPE” as valid values.
        
          - **ParameterValue** *(string) --* **[REQUIRED]** 
        
            The parameter value of a room skill parameter.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def put_skill_authorization(self, AuthorizationResult: Dict, SkillId: str, RoomArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/PutSkillAuthorization>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_skill_authorization(
              AuthorizationResult={
                  \'string\': \'string\'
              },
              SkillId=\'string\',
              RoomArn=\'string\'
          )
        :type AuthorizationResult: dict
        :param AuthorizationResult: **[REQUIRED]** 
        
          The authorization result specific to OAUTH code grant output. \"Code” must be populated in the AuthorizationResult map to establish the authorization.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The unique identifier of a skill.
        
        :type RoomArn: string
        :param RoomArn: 
        
          The room that the skill is authorized for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def register_avs_device(self, ClientId: str, UserCode: str, ProductId: str, DeviceSerialNumber: str, AmazonId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/RegisterAVSDevice>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_avs_device(
              ClientId=\'string\',
              UserCode=\'string\',
              ProductId=\'string\',
              DeviceSerialNumber=\'string\',
              AmazonId=\'string\'
          )
        :type ClientId: string
        :param ClientId: **[REQUIRED]** 
        
          The client ID of the OEM used for code-based linking authorization on an AVS device.
        
        :type UserCode: string
        :param UserCode: **[REQUIRED]** 
        
          The code that is obtained after your AVS device has made a POST request to LWA as a part of the Device Authorization Request component of the OAuth code-based linking specification.
        
        :type ProductId: string
        :param ProductId: **[REQUIRED]** 
        
          The product ID used to identify your AVS device during authorization.
        
        :type DeviceSerialNumber: string
        :param DeviceSerialNumber: **[REQUIRED]** 
        
          The key generated by the OEM that uniquely identifies a specified instance of your AVS device.
        
        :type AmazonId: string
        :param AmazonId: **[REQUIRED]** 
        
          The device type ID for your AVS device generated by Amazon when the OEM creates a new product on Amazon\'s Developer Console.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeviceArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeviceArn** *(string) --* 
        
              The ARN of the device.
        
        """
        pass

    def reject_skill(self, SkillId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/RejectSkill>`_
        
        **Request Syntax** 
        ::
        
          response = client.reject_skill(
              SkillId=\'string\'
          )
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The unique identifier of the skill.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def resolve_room(self, UserId: str, SkillId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ResolveRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.resolve_room(
              UserId=\'string\',
              SkillId=\'string\'
          )
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The ARN of the user. Required.
        
        :type SkillId: string
        :param SkillId: **[REQUIRED]** 
        
          The ARN of the skill that was requested. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RoomArn\': \'string\',
                \'RoomName\': \'string\',
                \'RoomSkillParameters\': [
                    {
                        \'ParameterKey\': \'string\',
                        \'ParameterValue\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RoomArn** *(string) --* 
        
              The ARN of the room from which the skill request was invoked.
        
            - **RoomName** *(string) --* 
        
              The name of the room from which the skill request was invoked.
        
            - **RoomSkillParameters** *(list) --* 
        
              Response to get the room profile request. Required.
        
              - *(dict) --* 
        
                A skill parameter associated with a room.
        
                - **ParameterKey** *(string) --* 
        
                  The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes “DEFAULT” or “SCOPE” as valid values.
        
                - **ParameterValue** *(string) --* 
        
                  The parameter value of a room skill parameter.
        
        """
        pass

    def revoke_invitation(self, UserArn: str = None, EnrollmentId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/RevokeInvitation>`_
        
        **Request Syntax** 
        ::
        
          response = client.revoke_invitation(
              UserArn=\'string\',
              EnrollmentId=\'string\'
          )
        :type UserArn: string
        :param UserArn: 
        
          The ARN of the user for whom to revoke an enrollment invitation. Required.
        
        :type EnrollmentId: string
        :param EnrollmentId: 
        
          The ARN of the enrollment invitation to revoke. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def search_address_books(self, Filters: List = None, SortCriteria: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchAddressBooks>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_address_books(
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
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filters: list
        :param Filters: 
        
          The filters to use to list a specified set of address books. The supported filter key is AddressBookName.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The values of a filter.
        
              - *(string) --* 
        
        :type SortCriteria: list
        :param SortCriteria: 
        
          The sort order to use in listing the specified set of address books. The supported sort key is AddressBookName.
        
          - *(dict) --* 
        
            An object representing a sort criteria. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The sort key of a sort object.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The sort value of a sort object.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AddressBooks\': [
                    {
                        \'AddressBookArn\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\',
                \'TotalCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AddressBooks** *(list) --* 
        
              The address books that meet the specified set of filter criteria, in sort order.
        
              - *(dict) --* 
        
                Information related to an address book.
        
                - **AddressBookArn** *(string) --* 
        
                  The ARN of the address book.
        
                - **Name** *(string) --* 
        
                  The name of the address book.
        
                - **Description** *(string) --* 
        
                  The description of the address book.
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
            - **TotalCount** *(integer) --* 
        
              The total number of address books returned.
        
        """
        pass

    def search_contacts(self, Filters: List = None, SortCriteria: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchContacts>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_contacts(
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
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filters: list
        :param Filters: 
        
          The filters to use to list a specified set of address books. The supported filter keys are DisplayName, FirstName, LastName, and AddressBookArns.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The values of a filter.
        
              - *(string) --* 
        
        :type SortCriteria: list
        :param SortCriteria: 
        
          The sort order to use in listing the specified set of contacts. The supported sort keys are DisplayName, FirstName, and LastName.
        
          - *(dict) --* 
        
            An object representing a sort criteria. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The sort key of a sort object.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The sort value of a sort object.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Contacts\': [
                    {
                        \'ContactArn\': \'string\',
                        \'DisplayName\': \'string\',
                        \'FirstName\': \'string\',
                        \'LastName\': \'string\',
                        \'PhoneNumber\': \'string\'
                    },
                ],
                \'NextToken\': \'string\',
                \'TotalCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Contacts** *(list) --* 
        
              The contacts that meet the specified set of filter criteria, in sort order.
        
              - *(dict) --* 
        
                Information related to a contact.
        
                - **ContactArn** *(string) --* 
        
                  The ARN of the contact.
        
                - **DisplayName** *(string) --* 
        
                  The name of the contact to display on the console.
        
                - **FirstName** *(string) --* 
        
                  The first name of the contact, used to call the contact on the device.
        
                - **LastName** *(string) --* 
        
                  The last name of the contact, used to call the contact on the device.
        
                - **PhoneNumber** *(string) --* 
        
                  The phone number of the contact.
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
            - **TotalCount** *(integer) --* 
        
              The total number of contacts returned.
        
        """
        pass

    def search_devices(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchDevices>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_devices(
              NextToken=\'string\',
              MaxResults=123,
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
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
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
                \'NextToken\': \'string\',
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
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
            - **TotalCount** *(integer) --* 
        
              The total number of devices returned.
        
        """
        pass

    def search_profiles(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchProfiles>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_profiles(
              NextToken=\'string\',
              MaxResults=123,
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
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
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
                \'NextToken\': \'string\',
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
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
            - **TotalCount** *(integer) --* 
        
              The total number of room profiles returned.
        
        """
        pass

    def search_rooms(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchRooms>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_rooms(
              NextToken=\'string\',
              MaxResults=123,
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
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved. 
        
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
                \'NextToken\': \'string\',
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
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
            - **TotalCount** *(integer) --* 
        
              The total number of rooms returned.
        
        """
        pass

    def search_skill_groups(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchSkillGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_skill_groups(
              NextToken=\'string\',
              MaxResults=123,
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
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` . Required.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved. 
        
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
                \'NextToken\': \'string\',
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
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
            - **TotalCount** *(integer) --* 
        
              The total number of skill groups returned.
        
        """
        pass

    def search_users(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchUsers>`_
        
        **Request Syntax** 
        ::
        
          response = client.search_users(
              NextToken=\'string\',
              MaxResults=123,
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
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` . Required.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved. Required.
        
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
                \'NextToken\': \'string\',
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
        
            - **NextToken** *(string) --* 
        
              The token returned to indicate that there is more data available.
        
            - **TotalCount** *(integer) --* 
        
              The total number of users returned.
        
        """
        pass

    def send_invitation(self, UserArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SendInvitation>`_
        
        **Request Syntax** 
        ::
        
          response = client.send_invitation(
              UserArn=\'string\'
          )
        :type UserArn: string
        :param UserArn: 
        
          The ARN of the user to whom to send an invitation. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def start_device_sync(self, Features: List, RoomArn: str = None, DeviceArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/StartDeviceSync>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_device_sync(
              RoomArn=\'string\',
              DeviceArn=\'string\',
              Features=[
                  \'BLUETOOTH\'|\'VOLUME\'|\'NOTIFICATIONS\'|\'LISTS\'|\'SKILLS\'|\'ALL\',
              ]
          )
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room with which the device to sync is associated. Required.
        
        :type DeviceArn: string
        :param DeviceArn: 
        
          The ARN of the device to sync. Required.
        
        :type Features: list
        :param Features: **[REQUIRED]** 
        
          Request structure to start the device sync. Required.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def start_smart_home_appliance_discovery(self, RoomArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/StartSmartHomeApplianceDiscovery>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_smart_home_appliance_discovery(
              RoomArn=\'string\'
          )
        :type RoomArn: string
        :param RoomArn: **[REQUIRED]** 
        
          The room where smart home appliance discovery was initiated.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def tag_resource(self, Arn: str, Tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              Arn=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type Arn: string
        :param Arn: **[REQUIRED]** 
        
          The ARN of the resource to which to add metadata tags. Required. 
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tags to be added to the specified resource. Do not provide system tags. Required. 
        
          - *(dict) --* 
        
            A key-value pair that can be associated with a resource. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of a tag. Tag keys are case-sensitive. 
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The value of a tag. Tag values are case-sensitive and can be null.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def untag_resource(self, Arn: str, TagKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              Arn=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type Arn: string
        :param Arn: **[REQUIRED]** 
        
          The ARN of the resource from which to remove metadata tags. Required. 
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The tags to be removed from the specified resource. Do not provide system tags. Required. 
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_address_book(self, AddressBookArn: str, Name: str = None, Description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateAddressBook>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_address_book(
              AddressBookArn=\'string\',
              Name=\'string\',
              Description=\'string\'
          )
        :type AddressBookArn: string
        :param AddressBookArn: **[REQUIRED]** 
        
          The ARN of the room to update.
        
        :type Name: string
        :param Name: 
        
          The updated name of the room.
        
        :type Description: string
        :param Description: 
        
          The updated description of the room.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_conference_provider(self, ConferenceProviderArn: str, ConferenceProviderType: str, MeetingSetting: Dict, IPDialIn: Dict = None, PSTNDialIn: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateConferenceProvider>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_conference_provider(
              ConferenceProviderArn=\'string\',
              ConferenceProviderType=\'CHIME\'|\'BLUEJEANS\'|\'FUZE\'|\'GOOGLE_HANGOUTS\'|\'POLYCOM\'|\'RINGCENTRAL\'|\'SKYPE_FOR_BUSINESS\'|\'WEBEX\'|\'ZOOM\'|\'CUSTOM\',
              IPDialIn={
                  \'Endpoint\': \'string\',
                  \'CommsProtocol\': \'SIP\'|\'SIPS\'|\'H323\'
              },
              PSTNDialIn={
                  \'CountryCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'OneClickIdDelay\': \'string\',
                  \'OneClickPinDelay\': \'string\'
              },
              MeetingSetting={
                  \'RequirePin\': \'YES\'|\'NO\'|\'OPTIONAL\'
              }
          )
        :type ConferenceProviderArn: string
        :param ConferenceProviderArn: **[REQUIRED]** 
        
          The ARN of the conference provider.
        
        :type ConferenceProviderType: string
        :param ConferenceProviderType: **[REQUIRED]** 
        
          The type of the conference provider.
        
        :type IPDialIn: dict
        :param IPDialIn: 
        
          The IP endpoint and protocol for calling.
        
          - **Endpoint** *(string) --* **[REQUIRED]** 
        
            The IP address.
        
          - **CommsProtocol** *(string) --* **[REQUIRED]** 
        
            The protocol, including SIP, SIPS, and H323.
        
        :type PSTNDialIn: dict
        :param PSTNDialIn: 
        
          The information for PSTN conferencing.
        
          - **CountryCode** *(string) --* **[REQUIRED]** 
        
            The zip code.
        
          - **PhoneNumber** *(string) --* **[REQUIRED]** 
        
            The phone number to call to join the conference.
        
          - **OneClickIdDelay** *(string) --* **[REQUIRED]** 
        
            The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
        
          - **OneClickPinDelay** *(string) --* **[REQUIRED]** 
        
            The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
        
        :type MeetingSetting: dict
        :param MeetingSetting: **[REQUIRED]** 
        
          The meeting settings for the conference provider.
        
          - **RequirePin** *(string) --* **[REQUIRED]** 
        
            The values that indicate whether the pin is always required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_contact(self, ContactArn: str, DisplayName: str = None, FirstName: str = None, LastName: str = None, PhoneNumber: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateContact>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_contact(
              ContactArn=\'string\',
              DisplayName=\'string\',
              FirstName=\'string\',
              LastName=\'string\',
              PhoneNumber=\'string\'
          )
        :type ContactArn: string
        :param ContactArn: **[REQUIRED]** 
        
          The ARN of the contact to update.
        
        :type DisplayName: string
        :param DisplayName: 
        
          The updated display name of the contact.
        
        :type FirstName: string
        :param FirstName: 
        
          The updated first name of the contact.
        
        :type LastName: string
        :param LastName: 
        
          The updated last name of the contact.
        
        :type PhoneNumber: string
        :param PhoneNumber: 
        
          The updated phone number of the contact.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_device(self, DeviceArn: str = None, DeviceName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateDevice>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_device(
              DeviceArn=\'string\',
              DeviceName=\'string\'
          )
        :type DeviceArn: string
        :param DeviceArn: 
        
          The ARN of the device to update. Required.
        
        :type DeviceName: string
        :param DeviceName: 
        
          The updated device name. Required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_profile(self, ProfileArn: str = None, ProfileName: str = None, IsDefault: bool = None, Timezone: str = None, Address: str = None, DistanceUnit: str = None, TemperatureUnit: str = None, WakeWord: str = None, SetupModeDisabled: bool = None, MaxVolumeLimit: int = None, PSTNEnabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_profile(
              ProfileArn=\'string\',
              ProfileName=\'string\',
              IsDefault=True|False,
              Timezone=\'string\',
              Address=\'string\',
              DistanceUnit=\'METRIC\'|\'IMPERIAL\',
              TemperatureUnit=\'FAHRENHEIT\'|\'CELSIUS\',
              WakeWord=\'ALEXA\'|\'AMAZON\'|\'ECHO\'|\'COMPUTER\',
              SetupModeDisabled=True|False,
              MaxVolumeLimit=123,
              PSTNEnabled=True|False
          )
        :type ProfileArn: string
        :param ProfileArn: 
        
          The ARN of the room profile to update. Required.
        
        :type ProfileName: string
        :param ProfileName: 
        
          The updated name for the room profile.
        
        :type IsDefault: boolean
        :param IsDefault: 
        
          Sets the profile as default if selected. If this is missing, no update is done to the default status.
        
        :type Timezone: string
        :param Timezone: 
        
          The updated timezone for the room profile.
        
        :type Address: string
        :param Address: 
        
          The updated address for the room profile.
        
        :type DistanceUnit: string
        :param DistanceUnit: 
        
          The updated distance unit for the room profile.
        
        :type TemperatureUnit: string
        :param TemperatureUnit: 
        
          The updated temperature unit for the room profile.
        
        :type WakeWord: string
        :param WakeWord: 
        
          The updated wake word for the room profile.
        
        :type SetupModeDisabled: boolean
        :param SetupModeDisabled: 
        
          Whether the setup mode of the profile is enabled.
        
        :type MaxVolumeLimit: integer
        :param MaxVolumeLimit: 
        
          The updated maximum volume limit for the room profile.
        
        :type PSTNEnabled: boolean
        :param PSTNEnabled: 
        
          Whether the PSTN setting of the room profile is enabled.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_room(self, RoomArn: str = None, RoomName: str = None, Description: str = None, ProviderCalendarId: str = None, ProfileArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateRoom>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_room(
              RoomArn=\'string\',
              RoomName=\'string\',
              Description=\'string\',
              ProviderCalendarId=\'string\',
              ProfileArn=\'string\'
          )
        :type RoomArn: string
        :param RoomArn: 
        
          The ARN of the room to update. 
        
        :type RoomName: string
        :param RoomName: 
        
          The updated name for the room.
        
        :type Description: string
        :param Description: 
        
          The updated description for the room.
        
        :type ProviderCalendarId: string
        :param ProviderCalendarId: 
        
          The updated provider calendar ARN for the room.
        
        :type ProfileArn: string
        :param ProfileArn: 
        
          The updated profile ARN for the room.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_skill_group(self, SkillGroupArn: str = None, SkillGroupName: str = None, Description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/UpdateSkillGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_skill_group(
              SkillGroupArn=\'string\',
              SkillGroupName=\'string\',
              Description=\'string\'
          )
        :type SkillGroupArn: string
        :param SkillGroupArn: 
        
          The ARN of the skill group to update. 
        
        :type SkillGroupName: string
        :param SkillGroupName: 
        
          The updated name for the skill group.
        
        :type Description: string
        :param Description: 
        
          The updated description for the skill group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
