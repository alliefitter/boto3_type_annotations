from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_device_with_placement(self, projectName: str, placementName: str, deviceId: str, deviceTemplateName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/AssociateDeviceWithPlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_device_with_placement(
              projectName=\'string\',
              placementName=\'string\',
              deviceId=\'string\',
              deviceTemplateName=\'string\'
          )
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
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def can_paginate(self, operation_name: str = None):
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

    def create_placement(self, placementName: str, projectName: str, attributes: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/CreatePlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_placement(
              placementName=\'string\',
              projectName=\'string\',
              attributes={
                  \'string\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def create_project(self, projectName: str, description: str = None, placementTemplate: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/CreateProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_project(
              projectName=\'string\',
              description=\'string\',
              placementTemplate={
                  \'defaultAttributes\': {
                      \'string\': \'string\'
                  },
                  \'deviceTemplates\': {
                      \'string\': {
                          \'deviceType\': \'string\',
                          \'callbackOverrides\': {
                              \'string\': \'string\'
                          }
                      }
                  }
              }
          )
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_placement(self, placementName: str, projectName: str) -> Dict:
        """
        
        .. note::
        
          When you delete a placement, all associated data becomes irretrievable.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DeletePlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_placement(
              placementName=\'string\',
              projectName=\'string\'
          )
        :type placementName: string
        :param placementName: **[REQUIRED]** 
        
          The name of the empty placement to delete.
        
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The project containing the empty placement to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_project(self, projectName: str) -> Dict:
        """
        
        .. note::
        
          When you delete a project, all associated data becomes irretrievable.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DeleteProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_project(
              projectName=\'string\'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the empty project to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_placement(self, placementName: str, projectName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DescribePlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_placement(
              placementName=\'string\',
              projectName=\'string\'
          )
        :type placementName: string
        :param placementName: **[REQUIRED]** 
        
          The name of the placement within a project.
        
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The project containing the placement to be described.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'placement\': {
                    \'projectName\': \'string\',
                    \'placementName\': \'string\',
                    \'attributes\': {
                        \'string\': \'string\'
                    },
                    \'createdDate\': datetime(2015, 1, 1),
                    \'updatedDate\': datetime(2015, 1, 1)
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
        
        """
        pass

    def describe_project(self, projectName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DescribeProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_project(
              projectName=\'string\'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the project to be described.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'project\': {
                    \'projectName\': \'string\',
                    \'description\': \'string\',
                    \'createdDate\': datetime(2015, 1, 1),
                    \'updatedDate\': datetime(2015, 1, 1),
                    \'placementTemplate\': {
                        \'defaultAttributes\': {
                            \'string\': \'string\'
                        },
                        \'deviceTemplates\': {
                            \'string\': {
                                \'deviceType\': \'string\',
                                \'callbackOverrides\': {
                                    \'string\': \'string\'
                                }
                            }
                        }
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **project** *(dict) --* 
        
              An object describing the project.
        
              - **projectName** *(string) --* 
        
                The name of the project for which to obtain information from.
        
              - **description** *(string) --* 
        
                The description of the project.
        
              - **createdDate** *(datetime) --* 
        
                The date when the project was originally created, in UNIX epoch time format.
        
              - **updatedDate** *(datetime) --* 
        
                The date when the project was last updated, in UNIX epoch time format. If the project was not updated, then ``createdDate`` and ``updatedDate`` are the same.
        
              - **placementTemplate** *(dict) --* 
        
                An object describing the project\'s placement specifications.
        
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
                    
        """
        pass

    def disassociate_device_from_placement(self, projectName: str, placementName: str, deviceTemplateName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/DisassociateDeviceFromPlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_device_from_placement(
              projectName=\'string\',
              placementName=\'string\',
              deviceTemplateName=\'string\'
          )
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
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
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

    def get_devices_in_placement(self, projectName: str, placementName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/GetDevicesInPlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_devices_in_placement(
              projectName=\'string\',
              placementName=\'string\'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]** 
        
          The name of the project containing the placement.
        
        :type placementName: string
        :param placementName: **[REQUIRED]** 
        
          The name of the placement to get the devices from.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'devices\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **devices** *(dict) --* 
        
              An object containing the devices (zero or more) within the placement.
        
              - *(string) --* 
                
                - *(string) --* 
          
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_placements(self, projectName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/ListPlacements>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_placements(
              projectName=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'placements\': [
                    {
                        \'projectName\': \'string\',
                        \'placementName\': \'string\',
                        \'createdDate\': datetime(2015, 1, 1),
                        \'updatedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'nextToken\': \'string\'
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
        
        """
        pass

    def list_projects(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/ListProjects>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_projects(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          The token to retrieve the next set of results.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return per request. If not set, a default value of 100 is used.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'projects\': [
                    {
                        \'projectName\': \'string\',
                        \'createdDate\': datetime(2015, 1, 1),
                        \'updatedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **projects** *(list) --* 
        
              An object containing the list of projects.
        
              - *(dict) --* 
        
                An object providing summary information for a particular project for an associated AWS account and region.
        
                - **projectName** *(string) --* 
        
                  The name of the project being summarized.
        
                - **createdDate** *(datetime) --* 
        
                  The date when the project was originally created, in UNIX epoch time format.
        
                - **updatedDate** *(datetime) --* 
        
                  The date when the project was last updated, in UNIX epoch time format. If the project was not updated, then ``createdDate`` and ``updatedDate`` are the same.
        
            - **nextToken** *(string) --* 
        
              The token used to retrieve the next set of results - will be effectively empty if there are no further results.
        
        """
        pass

    def update_placement(self, placementName: str, projectName: str, attributes: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/UpdatePlacement>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_placement(
              placementName=\'string\',
              projectName=\'string\',
              attributes={
                  \'string\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_project(self, projectName: str, description: str = None, placementTemplate: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot1click-projects-2018-05-14/UpdateProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_project(
              projectName=\'string\',
              description=\'string\',
              placementTemplate={
                  \'defaultAttributes\': {
                      \'string\': \'string\'
                  },
                  \'deviceTemplates\': {
                      \'string\': {
                          \'deviceType\': \'string\',
                          \'callbackOverrides\': {
                              \'string\': \'string\'
                          }
                      }
                  }
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
