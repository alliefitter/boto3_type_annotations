from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
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

    def cancel_job(self, JobId: str, APIVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/CancelJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_job(
              JobId=\'string\',
              APIVersion=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** A unique identifier which refers to a particular job.
        
        :type APIVersion: string
        :param APIVersion: Specifies the version of the client tool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Success\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* Output structure for the CancelJob operation.
            
            - **Success** *(boolean) --* Specifies whether (true) or not (false) AWS Import/Export updated your job.
        """
        pass

    def create_job(self, JobType: str, Manifest: str, ValidateOnly: bool, ManifestAddendum: str = None, APIVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/CreateJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_job(
              JobType=\'Import\'|\'Export\',
              Manifest=\'string\',
              ManifestAddendum=\'string\',
              ValidateOnly=True|False,
              APIVersion=\'string\'
          )
        :type JobType: string
        :param JobType: **[REQUIRED]** Specifies whether the job to initiate is an import or export job.
        
        :type Manifest: string
        :param Manifest: **[REQUIRED]** The UTF-8 encoded text of the manifest file.
        
        :type ManifestAddendum: string
        :param ManifestAddendum: For internal use only.
        
        :type ValidateOnly: boolean
        :param ValidateOnly: **[REQUIRED]** Validate the manifest and parameter values in the request but do not actually create a job.
        
        :type APIVersion: string
        :param APIVersion: Specifies the version of the client tool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobType\': \'Import\'|\'Export\',
                \'Signature\': \'string\',
                \'SignatureFileContents\': \'string\',
                \'WarningMessage\': \'string\',
                \'ArtifactList\': [
                    {
                        \'Description\': \'string\',
                        \'URL\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* Output structure for the CreateJob operation.
            
            - **JobId** *(string) --* A unique identifier which refers to a particular job.
            
            - **JobType** *(string) --* Specifies whether the job to initiate is an import or export job.
            
            - **Signature** *(string) --* An encrypted code used to authenticate the request and response, for example, \"DV+TpDfx1/TdSE9ktyK9k/bDTVI=\". Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value.
            
            - **SignatureFileContents** *(string) --* The actual text of the SIGNATURE file to be written to disk.
            
            - **WarningMessage** *(string) --* An optional message notifying you of non-fatal issues with the job, such as use of an incompatible Amazon S3 bucket name.
            
            - **ArtifactList** *(list) --* A collection of artifacts.
              
              - *(dict) --* A discrete item that contains the description and URL of an artifact (such as a PDF).
                
                - **Description** *(string) --* The associated description for this object.
                
                - **URL** *(string) --* The URL for a given Artifact.
            
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

    def get_shipping_label(self, jobIds: List, name: str = None, company: str = None, phoneNumber: str = None, country: str = None, stateOrProvince: str = None, city: str = None, postalCode: str = None, street1: str = None, street2: str = None, street3: str = None, APIVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/GetShippingLabel>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_shipping_label(
              jobIds=[
                  \'string\',
              ],
              name=\'string\',
              company=\'string\',
              phoneNumber=\'string\',
              country=\'string\',
              stateOrProvince=\'string\',
              city=\'string\',
              postalCode=\'string\',
              street1=\'string\',
              street2=\'string\',
              street3=\'string\',
              APIVersion=\'string\'
          )
        :type jobIds: list
        :param jobIds: **[REQUIRED]** 
        
          - *(string) --* 
        
        :type name: string
        :param name: Specifies the name of the person responsible for shipping this package.
        
        :type company: string
        :param company: Specifies the name of the company that will ship this package.
        
        :type phoneNumber: string
        :param phoneNumber: Specifies the phone number of the person responsible for shipping this package.
        
        :type country: string
        :param country: Specifies the name of your country for the return address.
        
        :type stateOrProvince: string
        :param stateOrProvince: Specifies the name of your state or your province for the return address.
        
        :type city: string
        :param city: Specifies the name of your city for the return address.
        
        :type postalCode: string
        :param postalCode: Specifies the postal code for the return address.
        
        :type street1: string
        :param street1: Specifies the first part of the street address for the return address, for example 1234 Main Street.
        
        :type street2: string
        :param street2: Specifies the optional second part of the street address for the return address, for example Suite 100.
        
        :type street3: string
        :param street3: Specifies the optional third part of the street address for the return address, for example c/o Jane Doe.
        
        :type APIVersion: string
        :param APIVersion: Specifies the version of the client tool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ShippingLabelURL\': \'string\',
                \'Warning\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ShippingLabelURL** *(string) --* 
            
            - **Warning** *(string) --* 
        """
        pass

    def get_status(self, JobId: str, APIVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/GetStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_status(
              JobId=\'string\',
              APIVersion=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** A unique identifier which refers to a particular job.
        
        :type APIVersion: string
        :param APIVersion: Specifies the version of the client tool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobId\': \'string\',
                \'JobType\': \'Import\'|\'Export\',
                \'LocationCode\': \'string\',
                \'LocationMessage\': \'string\',
                \'ProgressCode\': \'string\',
                \'ProgressMessage\': \'string\',
                \'Carrier\': \'string\',
                \'TrackingNumber\': \'string\',
                \'LogBucket\': \'string\',
                \'LogKey\': \'string\',
                \'ErrorCount\': 123,
                \'Signature\': \'string\',
                \'SignatureFileContents\': \'string\',
                \'CurrentManifest\': \'string\',
                \'CreationDate\': datetime(2015, 1, 1),
                \'ArtifactList\': [
                    {
                        \'Description\': \'string\',
                        \'URL\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* Output structure for the GetStatus operation.
            
            - **JobId** *(string) --* A unique identifier which refers to a particular job.
            
            - **JobType** *(string) --* Specifies whether the job to initiate is an import or export job.
            
            - **LocationCode** *(string) --* A token representing the location of the storage device, such as \"AtAWS\".
            
            - **LocationMessage** *(string) --* A more human readable form of the physical location of the storage device.
            
            - **ProgressCode** *(string) --* A token representing the state of the job, such as \"Started\".
            
            - **ProgressMessage** *(string) --* A more human readable form of the job status.
            
            - **Carrier** *(string) --* Name of the shipping company. This value is included when the LocationCode is \"Returned\".
            
            - **TrackingNumber** *(string) --* The shipping tracking number assigned by AWS Import/Export to the storage device when it\'s returned to you. We return this value when the LocationCode is \"Returned\".
            
            - **LogBucket** *(string) --* Amazon S3 bucket for user logs.
            
            - **LogKey** *(string) --* The key where the user logs were stored.
            
            - **ErrorCount** *(integer) --* Number of errors. We return this value when the ProgressCode is Success or SuccessWithErrors.
            
            - **Signature** *(string) --* An encrypted code used to authenticate the request and response, for example, \"DV+TpDfx1/TdSE9ktyK9k/bDTVI=\". Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value.
            
            - **SignatureFileContents** *(string) --* An encrypted code used to authenticate the request and response, for example, \"DV+TpDfx1/TdSE9ktyK9k/bDTVI=\". Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value.
            
            - **CurrentManifest** *(string) --* The last manifest submitted, which will be used to process the job.
            
            - **CreationDate** *(datetime) --* Timestamp of the CreateJob request in ISO8601 date format. For example \"2010-03-28T20:27:35Z\".
            
            - **ArtifactList** *(list) --* A collection of artifacts.
              
              - *(dict) --* A discrete item that contains the description and URL of an artifact (such as a PDF).
                
                - **Description** *(string) --* The associated description for this object.
                
                - **URL** *(string) --* The URL for a given Artifact.
            
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

    def list_jobs(self, MaxJobs: int = None, Marker: str = None, APIVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/ListJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_jobs(
              MaxJobs=123,
              Marker=\'string\',
              APIVersion=\'string\'
          )
        :type MaxJobs: integer
        :param MaxJobs: Sets the maximum number of jobs returned in the response. If there are additional jobs that were not returned because MaxJobs was exceeded, the response contains <IsTruncated>true</IsTruncated>. To return the additional jobs, see Marker.
        
        :type Marker: string
        :param Marker: Specifies the JOBID to start after when listing the jobs created with your account. AWS Import/Export lists your jobs in reverse chronological order. See MaxJobs.
        
        :type APIVersion: string
        :param APIVersion: Specifies the version of the client tool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Jobs\': [
                    {
                        \'JobId\': \'string\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'IsCanceled\': True|False,
                        \'JobType\': \'Import\'|\'Export\'
                    },
                ],
                \'IsTruncated\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* Output structure for the ListJobs operation.
            
            - **Jobs** *(list) --* A list container for Jobs returned by the ListJobs operation.
              
              - *(dict) --* Representation of a job returned by the ListJobs operation.
                
                - **JobId** *(string) --* A unique identifier which refers to a particular job.
                
                - **CreationDate** *(datetime) --* Timestamp of the CreateJob request in ISO8601 date format. For example \"2010-03-28T20:27:35Z\".
                
                - **IsCanceled** *(boolean) --* Indicates whether the job was canceled.
                
                - **JobType** *(string) --* Specifies whether the job to initiate is an import or export job.
            
            - **IsTruncated** *(boolean) --* Indicates whether the list of jobs was truncated. If true, then call ListJobs again using the last JobId element as the marker.
        """
        pass

    def update_job(self, JobId: str, Manifest: str, JobType: str, ValidateOnly: bool, APIVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/UpdateJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_job(
              JobId=\'string\',
              Manifest=\'string\',
              JobType=\'Import\'|\'Export\',
              ValidateOnly=True|False,
              APIVersion=\'string\'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]** A unique identifier which refers to a particular job.
        
        :type Manifest: string
        :param Manifest: **[REQUIRED]** The UTF-8 encoded text of the manifest file.
        
        :type JobType: string
        :param JobType: **[REQUIRED]** Specifies whether the job to initiate is an import or export job.
        
        :type ValidateOnly: boolean
        :param ValidateOnly: **[REQUIRED]** Validate the manifest and parameter values in the request but do not actually create a job.
        
        :type APIVersion: string
        :param APIVersion: Specifies the version of the client tool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Success\': True|False,
                \'WarningMessage\': \'string\',
                \'ArtifactList\': [
                    {
                        \'Description\': \'string\',
                        \'URL\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* Output structure for the UpateJob operation.
            
            - **Success** *(boolean) --* Specifies whether (true) or not (false) AWS Import/Export updated your job.
            
            - **WarningMessage** *(string) --* An optional message notifying you of non-fatal issues with the job, such as use of an incompatible Amazon S3 bucket name.
            
            - **ArtifactList** *(list) --* A collection of artifacts.
              
              - *(dict) --* A discrete item that contains the description and URL of an artifact (such as a PDF).
                
                - **Description** *(string) --* The associated description for this object.
                
                - **URL** *(string) --* The URL for a given Artifact.
            
        """
        pass
