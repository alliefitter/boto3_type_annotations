from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def associate_device_with_placement(self, projectName: str, placementName: str, deviceId: str, deviceTemplateName: str) -> Dict:
        """
        Associates a physical device with a placement.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/AssociateDeviceWithPlacement>`_
        
        **Request Syntax**
        ::
          response = client.associate_device_with_placement(
              projectName='string',
              placementName='string',
              deviceId='string',
              deviceTemplateName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the project containing the placement in which to associate the device.
        :type placementName: string
        :param placementName: **[REQUIRED]**
          The name of the placement in which to associate the device.
        :type deviceId: string
        :param deviceId: **[REQUIRED]**
          The ID of the physical device to be associated with the given placement in the project. Note that a mandatory 4 character prefix is required for all ``deviceId`` values.
        :type deviceTemplateName: string
        :param deviceTemplateName: **[REQUIRED]**
          The device template name to associate with the device ID.
        :rtype: dict
        :returns:
        """
        pass

    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
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

    def create_placement(self, placementName: str, projectName: str, attributes: Dict = None) -> Dict:
        """
        Creates an empty placement.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/CreatePlacement>`_
        
        **Request Syntax**
        ::
          response = client.create_placement(
              placementName='string',
              projectName='string',
              attributes={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type placementName: string
        :param placementName: **[REQUIRED]**
          The name of the placement to be created.
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the project in which to create the placement.
        :type attributes: dict
        :param attributes:
          Optional user-defined key/value pairs providing contextual data (such as location or function) for the placement.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_project(self, projectName: str, description: str = None, placementTemplate: Dict = None, tags: Dict = None) -> Dict:
        """
        Creates an empty project with a placement template. A project contains zero or more placements that adhere to the placement template defined in the project.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/CreateProject>`_
        
        **Request Syntax**
        ::
          response = client.create_project(
              projectName='string',
              description='string',
              placementTemplate={
                  'defaultAttributes': {
                      'string': 'string'
                  },
                  'deviceTemplates': {
                      'string': {
                          'deviceType': 'string',
                          'callbackOverrides': {
                              'string': 'string'
                          }
                      }
                  }
              },
              tags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the project to create.
        :type description: string
        :param description:
          An optional description for the project.
        :type placementTemplate: dict
        :param placementTemplate:
          The schema defining the placement to be created. A placement template defines placement default attributes and device templates. You cannot add or remove device templates after the project has been created. However, you can update ``callbackOverrides`` for the device templates using the ``UpdateProject`` API.
          - **defaultAttributes** *(dict) --*
            The default attributes (key/value pairs) to be applied to all placements using this template.
            - *(string) --*
              - *(string) --*
          - **deviceTemplates** *(dict) --*
            An object specifying the  DeviceTemplate for all placements using this ( PlacementTemplate ) template.
            - *(string) --*
              - *(dict) --*
                An object representing a device for a placement template (see  PlacementTemplate ).
                - **deviceType** *(string) --*
                  The device type, which currently must be ``\"button\"`` .
                - **callbackOverrides** *(dict) --*
                  An optional Lambda function to invoke instead of the default Lambda function provided by the placement template.
                  - *(string) --*
                    - *(string) --*
        :type tags: dict
        :param tags:
          Optional tags (metadata key/value pairs) to be associated with the project. For example, ``{ {\"key1\": \"value1\", \"key2\": \"value2\"} }`` . For more information, see `AWS Tagging Strategies <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`__ .
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def delete_placement(self, placementName: str, projectName: str) -> Dict:
        """
        Deletes a placement. To delete a placement, it must not have any devices associated with it.
        .. note::
          When you delete a placement, all associated data becomes irretrievable.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DeletePlacement>`_
        
        **Request Syntax**
        ::
          response = client.delete_placement(
              placementName='string',
              projectName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type placementName: string
        :param placementName: **[REQUIRED]**
          The name of the empty placement to delete.
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The project containing the empty placement to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_project(self, projectName: str) -> Dict:
        """
        Deletes a project. To delete a project, it must not have any placements associated with it.
        .. note::
          When you delete a project, all associated data becomes irretrievable.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DeleteProject>`_
        
        **Request Syntax**
        ::
          response = client.delete_project(
              projectName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the empty project to delete.
        :rtype: dict
        :returns:
        """
        pass

    def describe_placement(self, placementName: str, projectName: str) -> Dict:
        """
        Describes a placement in a project.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DescribePlacement>`_
        
        **Request Syntax**
        ::
          response = client.describe_placement(
              placementName='string',
              projectName='string'
          )
        
        **Response Syntax**
        ::
            {
                'placement': {
                    'projectName': 'string',
                    'placementName': 'string',
                    'attributes': {
                        'string': 'string'
                    },
                    'createdDate': datetime(2015, 1, 1),
                    'updatedDate': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **placement** *(dict) --* 
              An object describing the placement.
              - **projectName** *(string) --* 
                The name of the project containing the placement.
              - **placementName** *(string) --* 
                The name of the placement.
              - **attributes** *(dict) --* 
                The user-defined attributes associated with the placement.
                - *(string) --* 
                  - *(string) --* 
              - **createdDate** *(datetime) --* 
                The date when the placement was initially created, in UNIX epoch time format.
              - **updatedDate** *(datetime) --* 
                The date when the placement was last updated, in UNIX epoch time format. If the placement was not updated, then ``createdDate`` and ``updatedDate`` are the same.
        :type placementName: string
        :param placementName: **[REQUIRED]**
          The name of the placement within a project.
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The project containing the placement to be described.
        :rtype: dict
        :returns:
        """
        pass

    def describe_project(self, projectName: str) -> Dict:
        """
        Returns an object describing a project.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DescribeProject>`_
        
        **Request Syntax**
        ::
          response = client.describe_project(
              projectName='string'
          )
        
        **Response Syntax**
        ::
            {
                'project': {
                    'arn': 'string',
                    'projectName': 'string',
                    'description': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'updatedDate': datetime(2015, 1, 1),
                    'placementTemplate': {
                        'defaultAttributes': {
                            'string': 'string'
                        },
                        'deviceTemplates': {
                            'string': {
                                'deviceType': 'string',
                                'callbackOverrides': {
                                    'string': 'string'
                                }
                            }
                        }
                    },
                    'tags': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **project** *(dict) --* 
              An object describing the project.
              - **arn** *(string) --* 
                The ARN of the project.
              - **projectName** *(string) --* 
                The name of the project for which to obtain information from.
              - **description** *(string) --* 
                The description of the project.
              - **createdDate** *(datetime) --* 
                The date when the project was originally created, in UNIX epoch time format.
              - **updatedDate** *(datetime) --* 
                The date when the project was last updated, in UNIX epoch time format. If the project was not updated, then ``createdDate`` and ``updatedDate`` are the same.
              - **placementTemplate** *(dict) --* 
                An object describing the project's placement specifications.
                - **defaultAttributes** *(dict) --* 
                  The default attributes (key/value pairs) to be applied to all placements using this template.
                  - *(string) --* 
                    - *(string) --* 
                - **deviceTemplates** *(dict) --* 
                  An object specifying the  DeviceTemplate for all placements using this ( PlacementTemplate ) template.
                  - *(string) --* 
                    - *(dict) --* 
                      An object representing a device for a placement template (see  PlacementTemplate ).
                      - **deviceType** *(string) --* 
                        The device type, which currently must be ``"button"`` .
                      - **callbackOverrides** *(dict) --* 
                        An optional Lambda function to invoke instead of the default Lambda function provided by the placement template.
                        - *(string) --* 
                          - *(string) --* 
              - **tags** *(dict) --* 
                The tags (metadata key/value pairs) associated with the project.
                - *(string) --* 
                  - *(string) --* 
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the project to be described.
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_device_from_placement(self, projectName: str, placementName: str, deviceTemplateName: str) -> Dict:
        """
        Removes a physical device from a placement.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DisassociateDeviceFromPlacement>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_device_from_placement(
              projectName='string',
              placementName='string',
              deviceTemplateName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the project that contains the placement.
        :type placementName: string
        :param placementName: **[REQUIRED]**
          The name of the placement that the device should be removed from.
        :type deviceTemplateName: string
        :param deviceTemplateName: **[REQUIRED]**
          The device ID that should be removed from the placement.
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
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

    def get_devices_in_placement(self, projectName: str, placementName: str) -> Dict:
        """
        Returns an object enumerating the devices in a placement.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/GetDevicesInPlacement>`_
        
        **Request Syntax**
        ::
          response = client.get_devices_in_placement(
              projectName='string',
              placementName='string'
          )
        
        **Response Syntax**
        ::
            {
                'devices': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **devices** *(dict) --* 
              An object containing the devices (zero or more) within the placement.
              - *(string) --* 
                - *(string) --* 
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the project containing the placement.
        :type placementName: string
        :param placementName: **[REQUIRED]**
          The name of the placement to get the devices from.
        :rtype: dict
        :returns:
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        Create a paginator for an operation.
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_placements(self, projectName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the placement(s) of a project.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/ListPlacements>`_
        
        **Request Syntax**
        ::
          response = client.list_placements(
              projectName='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'placements': [
                    {
                        'projectName': 'string',
                        'placementName': 'string',
                        'createdDate': datetime(2015, 1, 1),
                        'updatedDate': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **placements** *(list) --* 
              An object listing the requested placements.
              - *(dict) --* 
                An object providing summary information for a particular placement.
                - **projectName** *(string) --* 
                  The name of the project containing the placement.
                - **placementName** *(string) --* 
                  The name of the placement being summarized.
                - **createdDate** *(datetime) --* 
                  The date when the placement was originally created, in UNIX epoch time format.
                - **updatedDate** *(datetime) --* 
                  The date when the placement was last updated, in UNIX epoch time format. If the placement was not updated, then ``createdDate`` and ``updatedDate`` are the same.
            - **nextToken** *(string) --* 
              The token used to retrieve the next set of results - will be effectively empty if there are no further results.
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The project containing the placements to be listed.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return per request. If not set, a default value of 100 is used.
        :rtype: dict
        :returns:
        """
        pass

    def list_projects(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the AWS IoT 1-Click project(s) associated with your AWS account and region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/ListProjects>`_
        
        **Request Syntax**
        ::
          response = client.list_projects(
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'projects': [
                    {
                        'arn': 'string',
                        'projectName': 'string',
                        'createdDate': datetime(2015, 1, 1),
                        'updatedDate': datetime(2015, 1, 1),
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **projects** *(list) --* 
              An object containing the list of projects.
              - *(dict) --* 
                An object providing summary information for a particular project for an associated AWS account and region.
                - **arn** *(string) --* 
                  The ARN of the project.
                - **projectName** *(string) --* 
                  The name of the project being summarized.
                - **createdDate** *(datetime) --* 
                  The date when the project was originally created, in UNIX epoch time format.
                - **updatedDate** *(datetime) --* 
                  The date when the project was last updated, in UNIX epoch time format. If the project was not updated, then ``createdDate`` and ``updatedDate`` are the same.
                - **tags** *(dict) --* 
                  The tags (metadata key/value pairs) associated with the project.
                  - *(string) --* 
                    - *(string) --* 
            - **nextToken** *(string) --* 
              The token used to retrieve the next set of results - will be effectively empty if there are no further results.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return per request. If not set, a default value of 100 is used.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, resourceArn: str) -> Dict:
        """
        Lists the tags (metadata key/value pairs) which you have assigned to the resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tags** *(dict) --* 
              The tags (metadata key/value pairs) which you have assigned to the resource.
              - *(string) --* 
                - *(string) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The ARN of the resource whose tags you want to list.
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, resourceArn: str, tags: Dict) -> Dict:
        """
        Creates or modifies tags for a resource. Tags are key/value pairs (metadata) that can be used to manage a resource. For more information, see `AWS Tagging Strategies <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              resourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The ARN of the resouce for which tag(s) should be added or modified.
        :type tags: dict
        :param tags: **[REQUIRED]**
          The new or modifying tag(s) for the resource. See `AWS IoT 1-Click Service Limits <https://docs.aws.amazon.com/iot-1-click/latest/developerguide/1click-appendix.html#1click-limits>`__ for the maximum number of tags allowed per resource.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        """
        Removes one or more tags (metadata key/value pairs) from a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The ARN of the resource whose tag you want to remove.
        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**
          The keys of those tags which you want to remove.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_placement(self, placementName: str, projectName: str, attributes: Dict = None) -> Dict:
        """
        Updates a placement with the given attributes. To clear an attribute, pass an empty value (i.e., "").
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/UpdatePlacement>`_
        
        **Request Syntax**
        ::
          response = client.update_placement(
              placementName='string',
              projectName='string',
              attributes={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type placementName: string
        :param placementName: **[REQUIRED]**
          The name of the placement to update.
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the project containing the placement to be updated.
        :type attributes: dict
        :param attributes:
          The user-defined object of attributes used to update the placement. The maximum number of key/value pairs is 50.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_project(self, projectName: str, description: str = None, placementTemplate: Dict = None) -> Dict:
        """
        Updates a project associated with your AWS account and region. With the exception of device template names, you can pass just the values that need to be updated because the update request will change only the values that are provided. To clear a value, pass the empty string (i.e., ``""`` ).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/UpdateProject>`_
        
        **Request Syntax**
        ::
          response = client.update_project(
              projectName='string',
              description='string',
              placementTemplate={
                  'defaultAttributes': {
                      'string': 'string'
                  },
                  'deviceTemplates': {
                      'string': {
                          'deviceType': 'string',
                          'callbackOverrides': {
                              'string': 'string'
                          }
                      }
                  }
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type projectName: string
        :param projectName: **[REQUIRED]**
          The name of the project to be updated.
        :type description: string
        :param description:
          An optional user-defined description for the project.
        :type placementTemplate: dict
        :param placementTemplate:
          An object defining the project update. Once a project has been created, you cannot add device template names to the project. However, for a given ``placementTemplate`` , you can update the associated ``callbackOverrides`` for the device definition using this API.
          - **defaultAttributes** *(dict) --*
            The default attributes (key/value pairs) to be applied to all placements using this template.
            - *(string) --*
              - *(string) --*
          - **deviceTemplates** *(dict) --*
            An object specifying the  DeviceTemplate for all placements using this ( PlacementTemplate ) template.
            - *(string) --*
              - *(dict) --*
                An object representing a device for a placement template (see  PlacementTemplate ).
                - **deviceType** *(string) --*
                  The device type, which currently must be ``\"button\"`` .
                - **callbackOverrides** *(dict) --*
                  An optional Lambda function to invoke instead of the default Lambda function provided by the placement template.
                  - *(string) --*
                    - *(string) --*
        :rtype: dict
        :returns:
        """
        pass
