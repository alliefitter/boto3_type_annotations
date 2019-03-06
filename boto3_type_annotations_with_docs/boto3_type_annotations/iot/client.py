from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from datetime import datetime
from botocore.client import BaseClient


class Client(BaseClient):
    def accept_certificate_transfer(self, certificateId: str, setAsActive: bool = None):
        """
        Accepts a pending certificate transfer. The default state of the certificate is INACTIVE.
        To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AcceptCertificateTransfer>`_
        
        **Request Syntax**
        ::
          response = client.accept_certificate_transfer(
              certificateId='string',
              setAsActive=True|False
          )
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        :type setAsActive: boolean
        :param setAsActive:
          Specifies whether the certificate is active.
        :returns: None
        """
        pass

    def add_thing_to_billing_group(self, billingGroupName: str = None, billingGroupArn: str = None, thingName: str = None, thingArn: str = None) -> Dict:
        """
        Adds a thing to a billing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AddThingToBillingGroup>`_
        
        **Request Syntax**
        ::
          response = client.add_thing_to_billing_group(
              billingGroupName='string',
              billingGroupArn='string',
              thingName='string',
              thingArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type billingGroupName: string
        :param billingGroupName:
          The name of the billing group.
        :type billingGroupArn: string
        :param billingGroupArn:
          The ARN of the billing group.
        :type thingName: string
        :param thingName:
          The name of the thing to be added to the billing group.
        :type thingArn: string
        :param thingArn:
          The ARN of the thing to be added to the billing group.
        :rtype: dict
        :returns:
        """
        pass

    def add_thing_to_thing_group(self, thingGroupName: str = None, thingGroupArn: str = None, thingName: str = None, thingArn: str = None, overrideDynamicGroups: bool = None) -> Dict:
        """
        Adds a thing to a thing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AddThingToThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.add_thing_to_thing_group(
              thingGroupName='string',
              thingGroupArn='string',
              thingName='string',
              thingArn='string',
              overrideDynamicGroups=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type thingGroupName: string
        :param thingGroupName:
          The name of the group to which you are adding a thing.
        :type thingGroupArn: string
        :param thingGroupArn:
          The ARN of the group to which you are adding a thing.
        :type thingName: string
        :param thingName:
          The name of the thing to add to a group.
        :type thingArn: string
        :param thingArn:
          The ARN of the thing to add to a group.
        :type overrideDynamicGroups: boolean
        :param overrideDynamicGroups:
          Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.
        :rtype: dict
        :returns:
        """
        pass

    def associate_targets_with_job(self, targets: List, jobId: str, comment: str = None) -> Dict:
        """
        Associates a group with a continuous job. The following criteria must be met: 
        * The job must have been created with the ``targetSelection`` field set to "CONTINUOUS". 
        * The job status must currently be "IN_PROGRESS". 
        * The total number of targets associated with a job must not exceed 100. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AssociateTargetsWithJob>`_
        
        **Request Syntax**
        ::
          response = client.associate_targets_with_job(
              targets=[
                  'string',
              ],
              jobId='string',
              comment='string'
          )
        
        **Response Syntax**
        ::
            {
                'jobArn': 'string',
                'jobId': 'string',
                'description': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **jobArn** *(string) --* 
              An ARN identifying the job.
            - **jobId** *(string) --* 
              The unique identifier you assigned to this job when it was created.
            - **description** *(string) --* 
              A short text description of the job.
        :type targets: list
        :param targets: **[REQUIRED]**
          A list of thing group ARNs that define the targets of the job.
          - *(string) --*
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The unique identifier you assigned to this job when it was created.
        :type comment: string
        :param comment:
          An optional comment string describing why the job was associated with the targets.
        :rtype: dict
        :returns:
        """
        pass

    def attach_policy(self, policyName: str, target: str):
        """
        Attaches a policy to the specified target.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AttachPolicy>`_
        
        **Request Syntax**
        ::
          response = client.attach_policy(
              policyName='string',
              target='string'
          )
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The name of the policy to attach.
        :type target: string
        :param target: **[REQUIRED]**
          The `identity <https://docs.aws.amazon.com/iot/latest/developerguide/iot-security-identity.html>`__ to which the policy is attached.
        :returns: None
        """
        pass

    def attach_principal_policy(self, policyName: str, principal: str):
        """
        Attaches the specified policy to the specified principal (certificate or other credential).
         **Note:** This API is deprecated. Please use  AttachPolicy instead.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AttachPrincipalPolicy>`_
        
        **Request Syntax**
        ::
          response = client.attach_principal_policy(
              policyName='string',
              principal='string'
          )
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
        :type principal: string
        :param principal: **[REQUIRED]**
          The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.
        :returns: None
        """
        pass

    def attach_security_profile(self, securityProfileName: str, securityProfileTargetArn: str) -> Dict:
        """
        Associates a Device Defender security profile with a thing group or with this account. Each thing group or account can have up to five security profiles associated with it.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AttachSecurityProfile>`_
        
        **Request Syntax**
        ::
          response = client.attach_security_profile(
              securityProfileName='string',
              securityProfileTargetArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type securityProfileName: string
        :param securityProfileName: **[REQUIRED]**
          The security profile that is attached.
        :type securityProfileTargetArn: string
        :param securityProfileTargetArn: **[REQUIRED]**
          The ARN of the target (thing group) to which the security profile is attached.
        :rtype: dict
        :returns:
        """
        pass

    def attach_thing_principal(self, thingName: str, principal: str) -> Dict:
        """
        Attaches the specified principal to the specified thing. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AttachThingPrincipal>`_
        
        **Request Syntax**
        ::
          response = client.attach_thing_principal(
              thingName='string',
              principal='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output from the AttachThingPrincipal operation.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing.
        :type principal: string
        :param principal: **[REQUIRED]**
          The principal, such as a certificate or other credential.
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

    def cancel_audit_task(self, taskId: str) -> Dict:
        """
        Cancels an audit that is in progress. The audit can be either scheduled or on-demand. If the audit is not in progress, an "InvalidRequestException" occurs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CancelAuditTask>`_
        
        **Request Syntax**
        ::
          response = client.cancel_audit_task(
              taskId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type taskId: string
        :param taskId: **[REQUIRED]**
          The ID of the audit you want to cancel. You can only cancel an audit that is \"IN_PROGRESS\".
        :rtype: dict
        :returns:
        """
        pass

    def cancel_certificate_transfer(self, certificateId: str):
        """
        Cancels a pending transfer for the specified certificate.
         **Note** Only the transfer source account can use this operation to cancel a transfer. (Transfer destinations can use  RejectCertificateTransfer instead.) After transfer, AWS IoT returns the certificate to the source account in the INACTIVE state. After the destination account has accepted the transfer, the transfer cannot be cancelled.
        After a certificate transfer is cancelled, the status of the certificate changes from PENDING_TRANSFER to INACTIVE.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CancelCertificateTransfer>`_
        
        **Request Syntax**
        ::
          response = client.cancel_certificate_transfer(
              certificateId='string'
          )
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        :returns: None
        """
        pass

    def cancel_job(self, jobId: str, reasonCode: str = None, comment: str = None, force: bool = None) -> Dict:
        """
        Cancels a job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CancelJob>`_
        
        **Request Syntax**
        ::
          response = client.cancel_job(
              jobId='string',
              reasonCode='string',
              comment='string',
              force=True|False
          )
        
        **Response Syntax**
        ::
            {
                'jobArn': 'string',
                'jobId': 'string',
                'description': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **jobArn** *(string) --* 
              The job ARN.
            - **jobId** *(string) --* 
              The unique identifier you assigned to this job when it was created.
            - **description** *(string) --* 
              A short text description of the job.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The unique identifier you assigned to this job when it was created.
        :type reasonCode: string
        :param reasonCode:
          (Optional)A reason code string that explains why the job was canceled.
        :type comment: string
        :param comment:
          An optional comment string describing why the job was canceled.
        :type force: boolean
        :param force:
          (Optional) If ``true`` job executions with status \"IN_PROGRESS\" and \"QUEUED\" are canceled, otherwise only job executions with status \"QUEUED\" are canceled. The default is ``false`` .
          Canceling a job which is \"IN_PROGRESS\", will cause a device which is executing the job to be unable to update the job execution status. Use caution and ensure that each device executing a job which is canceled is able to recover to a valid state.
        :rtype: dict
        :returns:
        """
        pass

    def cancel_job_execution(self, jobId: str, thingName: str, force: bool = None, expectedVersion: int = None, statusDetails: Dict = None):
        """
        Cancels the execution of a job for a given thing.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CancelJobExecution>`_
        
        **Request Syntax**
        ::
          response = client.cancel_job_execution(
              jobId='string',
              thingName='string',
              force=True|False,
              expectedVersion=123,
              statusDetails={
                  'string': 'string'
              }
          )
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The ID of the job to be canceled.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing whose execution of the job will be canceled.
        :type force: boolean
        :param force:
          (Optional) If ``true`` the job execution will be canceled if it has status IN_PROGRESS or QUEUED, otherwise the job execution will be canceled only if it has status QUEUED. If you attempt to cancel a job execution that is IN_PROGRESS, and you do not set ``force`` to ``true`` , then an ``InvalidStateTransitionException`` will be thrown. The default is ``false`` .
          Canceling a job execution which is \"IN_PROGRESS\", will cause the device to be unable to update the job execution status. Use caution and ensure that the device is able to recover to a valid state.
        :type expectedVersion: integer
        :param expectedVersion:
          (Optional) The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)
        :type statusDetails: dict
        :param statusDetails:
          A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged. You can specify at most 10 name/value pairs.
          - *(string) --*
            - *(string) --*
        :returns: None
        """
        pass

    def clear_default_authorizer(self) -> Dict:
        """
        Clears the default authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ClearDefaultAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.clear_default_authorizer()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :rtype: dict
        :returns:
        """
        pass

    def create_authorizer(self, authorizerName: str, authorizerFunctionArn: str, tokenKeyName: str, tokenSigningPublicKeys: Dict, status: str = None) -> Dict:
        """
        Creates an authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.create_authorizer(
              authorizerName='string',
              authorizerFunctionArn='string',
              tokenKeyName='string',
              tokenSigningPublicKeys={
                  'string': 'string'
              },
              status='ACTIVE'|'INACTIVE'
          )
        
        **Response Syntax**
        ::
            {
                'authorizerName': 'string',
                'authorizerArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **authorizerName** *(string) --* 
              The authorizer's name.
            - **authorizerArn** *(string) --* 
              The authorizer ARN.
        :type authorizerName: string
        :param authorizerName: **[REQUIRED]**
          The authorizer name.
        :type authorizerFunctionArn: string
        :param authorizerFunctionArn: **[REQUIRED]**
          The ARN of the authorizer\'s Lambda function.
        :type tokenKeyName: string
        :param tokenKeyName: **[REQUIRED]**
          The name of the token key used to extract the token from the HTTP headers.
        :type tokenSigningPublicKeys: dict
        :param tokenSigningPublicKeys: **[REQUIRED]**
          The public keys used to verify the digital signature returned by your custom authentication service.
          - *(string) --*
            - *(string) --*
        :type status: string
        :param status:
          The status of the create authorizer request.
        :rtype: dict
        :returns:
        """
        pass

    def create_billing_group(self, billingGroupName: str, billingGroupProperties: Dict = None, tags: List = None) -> Dict:
        """
        Creates a billing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateBillingGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_billing_group(
              billingGroupName='string',
              billingGroupProperties={
                  'billingGroupDescription': 'string'
              },
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'billingGroupName': 'string',
                'billingGroupArn': 'string',
                'billingGroupId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **billingGroupName** *(string) --* 
              The name you gave to the billing group.
            - **billingGroupArn** *(string) --* 
              The ARN of the billing group.
            - **billingGroupId** *(string) --* 
              The ID of the billing group.
        :type billingGroupName: string
        :param billingGroupName: **[REQUIRED]**
          The name you wish to give to the billing group.
        :type billingGroupProperties: dict
        :param billingGroupProperties:
          The properties of the billing group.
          - **billingGroupDescription** *(string) --*
            The description of the billing group.
        :type tags: list
        :param tags:
          Metadata which can be used to manage the billing group.
          - *(dict) --*
            A set of key/value pairs that are used to manage the resource.
            - **Key** *(string) --*
              The tag\'s key.
            - **Value** *(string) --*
              The tag\'s value.
        :rtype: dict
        :returns:
        """
        pass

    def create_certificate_from_csr(self, certificateSigningRequest: str, setAsActive: bool = None) -> Dict:
        """
        Creates an X.509 certificate using the specified certificate signing request.
         **Note:** The CSR must include a public key that is either an RSA key with a length of at least 2048 bits or an ECC key from NIST P-256 or NIST P-384 curves. 
         **Note:** Reusing the same certificate signing request (CSR) results in a distinct certificate.
        You can create multiple certificates in a batch by creating a directory, copying multiple .csr files into that directory, and then specifying that directory on the command line. The following commands show how to create a batch of certificates given a batch of CSRs.
        Assuming a set of CSRs are located inside of the directory my-csr-directory:
        On Linux and OS X, the command is:
        $ ls my-csr-directory/ | xargs -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}
        This command lists all of the CSRs in my-csr-directory and pipes each CSR file name to the aws iot create-certificate-from-csr AWS CLI command to create a certificate for the corresponding CSR.
        The aws iot create-certificate-from-csr part of the command can also be run in parallel to speed up the certificate creation process:
        $ ls my-csr-directory/ | xargs -P 10 -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}
        On Windows PowerShell, the command to create certificates for all CSRs in my-csr-directory is:
        > ls -Name my-csr-directory | %{aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/$_}
        On a Windows command prompt, the command to create certificates for all CSRs in my-csr-directory is:
        > forfiles /p my-csr-directory /c "cmd /c aws iot create-certificate-from-csr --certificate-signing-request file://@path"
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateCertificateFromCsr>`_
        
        **Request Syntax**
        ::
          response = client.create_certificate_from_csr(
              certificateSigningRequest='string',
              setAsActive=True|False
          )
        
        **Response Syntax**
        ::
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'certificatePem': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the CreateCertificateFromCsr operation.
            - **certificateArn** *(string) --* 
              The Amazon Resource Name (ARN) of the certificate. You can use the ARN as a principal for policy operations.
            - **certificateId** *(string) --* 
              The ID of the certificate. Certificate management operations only take a certificateId.
            - **certificatePem** *(string) --* 
              The certificate data, in PEM format.
        :type certificateSigningRequest: string
        :param certificateSigningRequest: **[REQUIRED]**
          The certificate signing request (CSR).
        :type setAsActive: boolean
        :param setAsActive:
          Specifies whether the certificate is active.
        :rtype: dict
        :returns:
        """
        pass

    def create_dynamic_thing_group(self, thingGroupName: str, queryString: str, thingGroupProperties: Dict = None, indexName: str = None, queryVersion: str = None, tags: List = None) -> Dict:
        """
        Creates a dynamic thing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateDynamicThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_dynamic_thing_group(
              thingGroupName='string',
              thingGroupProperties={
                  'thingGroupDescription': 'string',
                  'attributePayload': {
                      'attributes': {
                          'string': 'string'
                      },
                      'merge': True|False
                  }
              },
              indexName='string',
              queryString='string',
              queryVersion='string',
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'thingGroupName': 'string',
                'thingGroupArn': 'string',
                'thingGroupId': 'string',
                'indexName': 'string',
                'queryString': 'string',
                'queryVersion': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **thingGroupName** *(string) --* 
              The dynamic thing group name.
            - **thingGroupArn** *(string) --* 
              The dynamic thing group ARN.
            - **thingGroupId** *(string) --* 
              The dynamic thing group ID.
            - **indexName** *(string) --* 
              The dynamic thing group index name.
            - **queryString** *(string) --* 
              The dynamic thing group search query string.
            - **queryVersion** *(string) --* 
              The dynamic thing group query version.
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The dynamic thing group name to create.
        :type thingGroupProperties: dict
        :param thingGroupProperties:
          The dynamic thing group properties.
          - **thingGroupDescription** *(string) --*
            The thing group description.
          - **attributePayload** *(dict) --*
            The thing group attributes in JSON format.
            - **attributes** *(dict) --*
              A JSON string containing up to three key-value pair in JSON format. For example:
               ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``
              - *(string) --*
                - *(string) --*
            - **merge** *(boolean) --*
              Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.
              To remove an attribute, call ``UpdateThing`` with an empty attribute value.
              .. note::
                The ``merge`` attribute is only valid when calling ``UpdateThing`` .
        :type indexName: string
        :param indexName:
          The dynamic thing group index name.
          .. note::
            Currently one index is supported: \"AWS_Things\".
        :type queryString: string
        :param queryString: **[REQUIRED]**
          The dynamic thing group search query string.
          See `Query Syntax <https://docs.aws.amazon.com/iot/latest/developerguide/query-syntax.html>`__ for information about query string syntax.
        :type queryVersion: string
        :param queryVersion:
          The dynamic thing group query version.
          .. note::
            Currently one query version is supported: \"2017-09-30\". If not specified, the query version defaults to this value.
        :type tags: list
        :param tags:
          Metadata which can be used to manage the dynamic thing group.
          - *(dict) --*
            A set of key/value pairs that are used to manage the resource.
            - **Key** *(string) --*
              The tag\'s key.
            - **Value** *(string) --*
              The tag\'s value.
        :rtype: dict
        :returns:
        """
        pass

    def create_job(self, jobId: str, targets: List, documentSource: str = None, document: str = None, description: str = None, presignedUrlConfig: Dict = None, targetSelection: str = None, jobExecutionsRolloutConfig: Dict = None, abortConfig: Dict = None, timeoutConfig: Dict = None, tags: List = None) -> Dict:
        """
        Creates a job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateJob>`_
        
        **Request Syntax**
        ::
          response = client.create_job(
              jobId='string',
              targets=[
                  'string',
              ],
              documentSource='string',
              document='string',
              description='string',
              presignedUrlConfig={
                  'roleArn': 'string',
                  'expiresInSec': 123
              },
              targetSelection='CONTINUOUS'|'SNAPSHOT',
              jobExecutionsRolloutConfig={
                  'maximumPerMinute': 123,
                  'exponentialRate': {
                      'baseRatePerMinute': 123,
                      'incrementFactor': 123.0,
                      'rateIncreaseCriteria': {
                          'numberOfNotifiedThings': 123,
                          'numberOfSucceededThings': 123
                      }
                  }
              },
              abortConfig={
                  'criteriaList': [
                      {
                          'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                          'action': 'CANCEL',
                          'thresholdPercentage': 123.0,
                          'minNumberOfExecutedThings': 123
                      },
                  ]
              },
              timeoutConfig={
                  'inProgressTimeoutInMinutes': 123
              },
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'jobArn': 'string',
                'jobId': 'string',
                'description': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **jobArn** *(string) --* 
              The job ARN.
            - **jobId** *(string) --* 
              The unique identifier you assigned to this job.
            - **description** *(string) --* 
              The job description.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          A job identifier which must be unique for your AWS account. We recommend using a UUID. Alpha-numeric characters, \"-\" and \"_\" are valid for use here.
        :type targets: list
        :param targets: **[REQUIRED]**
          A list of things and thing groups to which the job should be sent.
          - *(string) --*
        :type documentSource: string
        :param documentSource:
          An S3 link to the job document.
        :type document: string
        :param document:
          The job document.
          .. note::
            If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document.
            The placeholder link is of the following form:
             ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/*bucket* /*key* }``
            where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.
        :type description: string
        :param description:
          A short text description of the job.
        :type presignedUrlConfig: dict
        :param presignedUrlConfig:
          Configuration information for pre-signed S3 URLs.
          - **roleArn** *(string) --*
            The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.
          - **expiresInSec** *(integer) --*
            How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.
        :type targetSelection: string
        :param targetSelection:
          Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.
        :type jobExecutionsRolloutConfig: dict
        :param jobExecutionsRolloutConfig:
          Allows you to create a staged rollout of the job.
          - **maximumPerMinute** *(integer) --*
            The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.
          - **exponentialRate** *(dict) --*
            The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.
            - **baseRatePerMinute** *(integer) --* **[REQUIRED]**
              The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
            - **incrementFactor** *(float) --* **[REQUIRED]**
              The exponential factor to increase the rate of rollout for a job.
            - **rateIncreaseCriteria** *(dict) --* **[REQUIRED]**
              The criteria to initiate the increase in rate of rollout for a job.
              AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).
              - **numberOfNotifiedThings** *(integer) --*
                The threshold for number of notified things that will initiate the increase in rate of rollout.
              - **numberOfSucceededThings** *(integer) --*
                The threshold for number of succeeded things that will initiate the increase in rate of rollout.
        :type abortConfig: dict
        :param abortConfig:
          Allows you to create criteria to abort a job.
          - **criteriaList** *(list) --* **[REQUIRED]**
            The list of abort criteria to define rules to abort the job.
            - *(dict) --*
              Details of abort criteria to define rules to abort the job.
              - **failureType** *(string) --* **[REQUIRED]**
                The type of job execution failure to define a rule to initiate a job abort.
              - **action** *(string) --* **[REQUIRED]**
                The type of abort action to initiate a job abort.
              - **thresholdPercentage** *(float) --* **[REQUIRED]**
                The threshold as a percentage of the total number of executed things that will initiate a job abort.
                AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
              - **minNumberOfExecutedThings** *(integer) --* **[REQUIRED]**
                Minimum number of executed things before evaluating an abort rule.
        :type timeoutConfig: dict
        :param timeoutConfig:
          Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the time expires, it will be automatically set to ``TIMED_OUT`` .
          - **inProgressTimeoutInMinutes** *(integer) --*
            Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can\'t be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal ``TIMED_OUT`` status.
        :type tags: list
        :param tags:
          Metadata which can be used to manage the job.
          - *(dict) --*
            A set of key/value pairs that are used to manage the resource.
            - **Key** *(string) --*
              The tag\'s key.
            - **Value** *(string) --*
              The tag\'s value.
        :rtype: dict
        :returns:
        """
        pass

    def create_keys_and_certificate(self, setAsActive: bool = None) -> Dict:
        """
        Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued public key.
         **Note** This is the only time AWS IoT issues the private key for this certificate, so it is important to keep it in a secure location.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateKeysAndCertificate>`_
        
        **Request Syntax**
        ::
          response = client.create_keys_and_certificate(
              setAsActive=True|False
          )
        
        **Response Syntax**
        ::
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'certificatePem': 'string',
                'keyPair': {
                    'PublicKey': 'string',
                    'PrivateKey': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the CreateKeysAndCertificate operation.
            - **certificateArn** *(string) --* 
              The ARN of the certificate.
            - **certificateId** *(string) --* 
              The ID of the certificate. AWS IoT issues a default subject name for the certificate (for example, AWS IoT Certificate).
            - **certificatePem** *(string) --* 
              The certificate data, in PEM format.
            - **keyPair** *(dict) --* 
              The generated key pair.
              - **PublicKey** *(string) --* 
                The public key.
              - **PrivateKey** *(string) --* 
                The private key.
        :type setAsActive: boolean
        :param setAsActive:
          Specifies whether the certificate is active.
        :rtype: dict
        :returns:
        """
        pass

    def create_ota_update(self, otaUpdateId: str, targets: List, files: List, roleArn: str, description: str = None, targetSelection: str = None, awsJobExecutionsRolloutConfig: Dict = None, additionalParameters: Dict = None) -> Dict:
        """
        Creates an AWS IoT OTAUpdate on a target group of things or groups.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateOTAUpdate>`_
        
        **Request Syntax**
        ::
          response = client.create_ota_update(
              otaUpdateId='string',
              description='string',
              targets=[
                  'string',
              ],
              targetSelection='CONTINUOUS'|'SNAPSHOT',
              awsJobExecutionsRolloutConfig={
                  'maximumPerMinute': 123
              },
              files=[
                  {
                      'fileName': 'string',
                      'fileVersion': 'string',
                      'fileLocation': {
                          'stream': {
                              'streamId': 'string',
                              'fileId': 123
                          },
                          's3Location': {
                              'bucket': 'string',
                              'key': 'string',
                              'version': 'string'
                          }
                      },
                      'codeSigning': {
                          'awsSignerJobId': 'string',
                          'startSigningJobParameter': {
                              'signingProfileParameter': {
                                  'certificateArn': 'string',
                                  'platform': 'string',
                                  'certificatePathOnDevice': 'string'
                              },
                              'signingProfileName': 'string',
                              'destination': {
                                  's3Destination': {
                                      'bucket': 'string',
                                      'prefix': 'string'
                                  }
                              }
                          },
                          'customCodeSigning': {
                              'signature': {
                                  'inlineDocument': b'bytes'
                              },
                              'certificateChain': {
                                  'certificateName': 'string',
                                  'inlineDocument': 'string'
                              },
                              'hashAlgorithm': 'string',
                              'signatureAlgorithm': 'string'
                          }
                      },
                      'attributes': {
                          'string': 'string'
                      }
                  },
              ],
              roleArn='string',
              additionalParameters={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'otaUpdateId': 'string',
                'awsIotJobId': 'string',
                'otaUpdateArn': 'string',
                'awsIotJobArn': 'string',
                'otaUpdateStatus': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **otaUpdateId** *(string) --* 
              The OTA update ID.
            - **awsIotJobId** *(string) --* 
              The AWS IoT job ID associated with the OTA update.
            - **otaUpdateArn** *(string) --* 
              The OTA update ARN.
            - **awsIotJobArn** *(string) --* 
              The AWS IoT job ARN associated with the OTA update.
            - **otaUpdateStatus** *(string) --* 
              The OTA update status.
        :type otaUpdateId: string
        :param otaUpdateId: **[REQUIRED]**
          The ID of the OTA update to be created.
        :type description: string
        :param description:
          The description of the OTA update.
        :type targets: list
        :param targets: **[REQUIRED]**
          The targeted devices to receive OTA updates.
          - *(string) --*
        :type targetSelection: string
        :param targetSelection:
          Specifies whether the update will continue to run (CONTINUOUS), or will be complete after all the things specified as targets have completed the update (SNAPSHOT). If continuous, the update may also be run on a thing when a change is detected in a target. For example, an update will run on a thing when the thing is added to a target group, even after the update was completed by all things originally in the group. Valid values: CONTINUOUS | SNAPSHOT.
        :type awsJobExecutionsRolloutConfig: dict
        :param awsJobExecutionsRolloutConfig:
          Configuration for the rollout of OTA updates.
          - **maximumPerMinute** *(integer) --*
            The maximum number of OTA update job executions started per minute.
        :type files: list
        :param files: **[REQUIRED]**
          The files to be streamed by the OTA update.
          - *(dict) --*
            Describes a file to be associated with an OTA update.
            - **fileName** *(string) --*
              The name of the file.
            - **fileVersion** *(string) --*
              The file version.
            - **fileLocation** *(dict) --*
              The location of the updated firmware.
              - **stream** *(dict) --*
                The stream that contains the OTA update.
                - **streamId** *(string) --*
                  The stream ID.
                - **fileId** *(integer) --*
                  The ID of a file associated with a stream.
              - **s3Location** *(dict) --*
                The location of the updated firmware in S3.
                - **bucket** *(string) --*
                  The S3 bucket.
                - **key** *(string) --*
                  The S3 key.
                - **version** *(string) --*
                  The S3 bucket version.
            - **codeSigning** *(dict) --*
              The code signing method of the file.
              - **awsSignerJobId** *(string) --*
                The ID of the AWSSignerJob which was created to sign the file.
              - **startSigningJobParameter** *(dict) --*
                Describes the code-signing job.
                - **signingProfileParameter** *(dict) --*
                  Describes the code-signing profile.
                  - **certificateArn** *(string) --*
                    Certificate ARN.
                  - **platform** *(string) --*
                    The hardware platform of your device.
                  - **certificatePathOnDevice** *(string) --*
                    The location of the code-signing certificate on your device.
                - **signingProfileName** *(string) --*
                  The code-signing profile name.
                - **destination** *(dict) --*
                  The location to write the code-signed file.
                  - **s3Destination** *(dict) --*
                    Describes the location in S3 of the updated firmware.
                    - **bucket** *(string) --*
                      The S3 bucket that contains the updated firmware.
                    - **prefix** *(string) --*
                      The S3 prefix.
              - **customCodeSigning** *(dict) --*
                A custom method for code signing a file.
                - **signature** *(dict) --*
                  The signature for the file.
                  - **inlineDocument** *(bytes) --*
                    A base64 encoded binary representation of the code signing signature.
                - **certificateChain** *(dict) --*
                  The certificate chain.
                  - **certificateName** *(string) --*
                    The name of the certificate.
                  - **inlineDocument** *(string) --*
                    A base64 encoded binary representation of the code signing certificate chain.
                - **hashAlgorithm** *(string) --*
                  The hash algorithm used to code sign the file.
                - **signatureAlgorithm** *(string) --*
                  The signature algorithm used to code sign the file.
            - **attributes** *(dict) --*
              A list of name/attribute pairs.
              - *(string) --*
                - *(string) --*
        :type roleArn: string
        :param roleArn: **[REQUIRED]**
          The IAM role that allows access to the AWS IoT Jobs service.
        :type additionalParameters: dict
        :param additionalParameters:
          A list of additional OTA update parameters which are name-value pairs.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_policy(self, policyName: str, policyDocument: str) -> Dict:
        """
        Creates an AWS IoT policy.
        The created policy is the default version for the policy. This operation creates a policy version with a version identifier of **1** and sets **1** as the policy's default version.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreatePolicy>`_
        
        **Request Syntax**
        ::
          response = client.create_policy(
              policyName='string',
              policyDocument='string'
          )
        
        **Response Syntax**
        ::
            {
                'policyName': 'string',
                'policyArn': 'string',
                'policyDocument': 'string',
                'policyVersionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the CreatePolicy operation.
            - **policyName** *(string) --* 
              The policy name.
            - **policyArn** *(string) --* 
              The policy ARN.
            - **policyDocument** *(string) --* 
              The JSON document that describes the policy.
            - **policyVersionId** *(string) --* 
              The policy version ID.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
        :type policyDocument: string
        :param policyDocument: **[REQUIRED]**
          The JSON document that describes the policy. **policyDocument** must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.
        :rtype: dict
        :returns:
        """
        pass

    def create_policy_version(self, policyName: str, policyDocument: str, setAsDefault: bool = None) -> Dict:
        """
        Creates a new version of the specified AWS IoT policy. To update a policy, create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must use  DeletePolicyVersion to delete an existing version before you create a new one.
        Optionally, you can set the new version as the policy's default version. The default version is the operative version (that is, the version that is in effect for the certificates to which the policy is attached).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreatePolicyVersion>`_
        
        **Request Syntax**
        ::
          response = client.create_policy_version(
              policyName='string',
              policyDocument='string',
              setAsDefault=True|False
          )
        
        **Response Syntax**
        ::
            {
                'policyArn': 'string',
                'policyDocument': 'string',
                'policyVersionId': 'string',
                'isDefaultVersion': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the CreatePolicyVersion operation.
            - **policyArn** *(string) --* 
              The policy ARN.
            - **policyDocument** *(string) --* 
              The JSON document that describes the policy.
            - **policyVersionId** *(string) --* 
              The policy version ID.
            - **isDefaultVersion** *(boolean) --* 
              Specifies whether the policy version is the default.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
        :type policyDocument: string
        :param policyDocument: **[REQUIRED]**
          The JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespace.
        :type setAsDefault: boolean
        :param setAsDefault:
          Specifies whether the policy version is set as the default. When this parameter is true, the new policy version becomes the operative version (that is, the version that is in effect for the certificates to which the policy is attached).
        :rtype: dict
        :returns:
        """
        pass

    def create_role_alias(self, roleAlias: str, roleArn: str, credentialDurationSeconds: int = None) -> Dict:
        """
        Creates a role alias.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateRoleAlias>`_
        
        **Request Syntax**
        ::
          response = client.create_role_alias(
              roleAlias='string',
              roleArn='string',
              credentialDurationSeconds=123
          )
        
        **Response Syntax**
        ::
            {
                'roleAlias': 'string',
                'roleAliasArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **roleAlias** *(string) --* 
              The role alias.
            - **roleAliasArn** *(string) --* 
              The role alias ARN.
        :type roleAlias: string
        :param roleAlias: **[REQUIRED]**
          The role alias that points to a role ARN. This allows you to change the role without having to update the device.
        :type roleArn: string
        :param roleArn: **[REQUIRED]**
          The role ARN.
        :type credentialDurationSeconds: integer
        :param credentialDurationSeconds:
          How long (in seconds) the credentials will be valid.
        :rtype: dict
        :returns:
        """
        pass

    def create_scheduled_audit(self, frequency: str, targetCheckNames: List, scheduledAuditName: str, dayOfMonth: str = None, dayOfWeek: str = None, tags: List = None) -> Dict:
        """
        Creates a scheduled audit that is run at a specified time interval.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateScheduledAudit>`_
        
        **Request Syntax**
        ::
          response = client.create_scheduled_audit(
              frequency='DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
              dayOfMonth='string',
              dayOfWeek='SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
              targetCheckNames=[
                  'string',
              ],
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              scheduledAuditName='string'
          )
        
        **Response Syntax**
        ::
            {
                'scheduledAuditArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **scheduledAuditArn** *(string) --* 
              The ARN of the scheduled audit.
        :type frequency: string
        :param frequency: **[REQUIRED]**
          How often the scheduled audit takes place. Can be one of \"DAILY\", \"WEEKLY\", \"BIWEEKLY\" or \"MONTHLY\". The actual start time of each audit is determined by the system.
        :type dayOfMonth: string
        :param dayOfMonth:
          The day of the month on which the scheduled audit takes place. Can be \"1\" through \"31\" or \"LAST\". This field is required if the \"frequency\" parameter is set to \"MONTHLY\". If days 29-31 are specified, and the month does not have that many days, the audit takes place on the \"LAST\" day of the month.
        :type dayOfWeek: string
        :param dayOfWeek:
          The day of the week on which the scheduled audit takes place. Can be one of \"SUN\", \"MON\", \"TUE\", \"WED\", \"THU\", \"FRI\" or \"SAT\". This field is required if the \"frequency\" parameter is set to \"WEEKLY\" or \"BIWEEKLY\".
        :type targetCheckNames: list
        :param targetCheckNames: **[REQUIRED]**
          Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
          - *(string) --*
            An audit check name. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
        :type tags: list
        :param tags:
          Metadata which can be used to manage the scheduled audit.
          - *(dict) --*
            A set of key/value pairs that are used to manage the resource.
            - **Key** *(string) --*
              The tag\'s key.
            - **Value** *(string) --*
              The tag\'s value.
        :type scheduledAuditName: string
        :param scheduledAuditName: **[REQUIRED]**
          The name you want to give to the scheduled audit. (Max. 128 chars)
        :rtype: dict
        :returns:
        """
        pass

    def create_security_profile(self, securityProfileName: str, securityProfileDescription: str = None, behaviors: List = None, alertTargets: Dict = None, additionalMetricsToRetain: List = None, tags: List = None) -> Dict:
        """
        Creates a Device Defender security profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateSecurityProfile>`_
        
        **Request Syntax**
        ::
          response = client.create_security_profile(
              securityProfileName='string',
              securityProfileDescription='string',
              behaviors=[
                  {
                      'name': 'string',
                      'metric': 'string',
                      'criteria': {
                          'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                          'value': {
                              'count': 123,
                              'cidrs': [
                                  'string',
                              ],
                              'ports': [
                                  123,
                              ]
                          },
                          'durationSeconds': 123,
                          'consecutiveDatapointsToAlarm': 123,
                          'consecutiveDatapointsToClear': 123,
                          'statisticalThreshold': {
                              'statistic': 'string'
                          }
                      }
                  },
              ],
              alertTargets={
                  'string': {
                      'alertTargetArn': 'string',
                      'roleArn': 'string'
                  }
              },
              additionalMetricsToRetain=[
                  'string',
              ],
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'securityProfileName': 'string',
                'securityProfileArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileName** *(string) --* 
              The name you gave to the security profile.
            - **securityProfileArn** *(string) --* 
              The ARN of the security profile.
        :type securityProfileName: string
        :param securityProfileName: **[REQUIRED]**
          The name you are giving to the security profile.
        :type securityProfileDescription: string
        :param securityProfileDescription:
          A description of the security profile.
        :type behaviors: list
        :param behaviors:
          Specifies the behaviors that, when violated by a device (thing), cause an alert.
          - *(dict) --*
            A Device Defender security profile behavior.
            - **name** *(string) --* **[REQUIRED]**
              The name you have given to the behavior.
            - **metric** *(string) --*
              What is measured by the behavior.
            - **criteria** *(dict) --*
              The criteria that determine if a device is behaving normally in regard to the ``metric`` .
              - **comparisonOperator** *(string) --*
                The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
              - **value** *(dict) --*
                The value to be compared with the ``metric`` .
                - **count** *(integer) --*
                  If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                - **cidrs** *(list) --*
                  If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                  - *(string) --*
                - **ports** *(list) --*
                  If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                  - *(integer) --*
              - **durationSeconds** *(integer) --*
                Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
              - **consecutiveDatapointsToAlarm** *(integer) --*
                If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
              - **consecutiveDatapointsToClear** *(integer) --*
                If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
              - **statisticalThreshold** *(dict) --*
                A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                - **statistic** *(string) --*
                  The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
        :type alertTargets: dict
        :param alertTargets:
          Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.
          - *(string) --*
            The type of alert target: one of \"SNS\".
            - *(dict) --*
              A structure containing the alert target ARN and the role ARN.
              - **alertTargetArn** *(string) --* **[REQUIRED]**
                The ARN of the notification target to which alerts are sent.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the role that grants permission to send alerts to the notification target.
        :type additionalMetricsToRetain: list
        :param additionalMetricsToRetain:
          A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s ``behaviors`` but it is also retained for any metric specified here.
          - *(string) --*
        :type tags: list
        :param tags:
          Metadata which can be used to manage the security profile.
          - *(dict) --*
            A set of key/value pairs that are used to manage the resource.
            - **Key** *(string) --*
              The tag\'s key.
            - **Value** *(string) --*
              The tag\'s value.
        :rtype: dict
        :returns:
        """
        pass

    def create_stream(self, streamId: str, files: List, roleArn: str, description: str = None) -> Dict:
        """
        Creates a stream for delivering one or more large files in chunks over MQTT. A stream transports data bytes in chunks or blocks packaged as MQTT messages from a source like S3. You can have one or more files associated with a stream. The total size of a file associated with the stream cannot exceed more than 2 MB. The stream will be created with version 0. If a stream is created with the same streamID as a stream that existed and was deleted within last 90 days, we will resurrect that old stream by incrementing the version by 1.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateStream>`_
        
        **Request Syntax**
        ::
          response = client.create_stream(
              streamId='string',
              description='string',
              files=[
                  {
                      'fileId': 123,
                      's3Location': {
                          'bucket': 'string',
                          'key': 'string',
                          'version': 'string'
                      }
                  },
              ],
              roleArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'streamId': 'string',
                'streamArn': 'string',
                'description': 'string',
                'streamVersion': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **streamId** *(string) --* 
              The stream ID.
            - **streamArn** *(string) --* 
              The stream ARN.
            - **description** *(string) --* 
              A description of the stream.
            - **streamVersion** *(integer) --* 
              The version of the stream.
        :type streamId: string
        :param streamId: **[REQUIRED]**
          The stream ID.
        :type description: string
        :param description:
          A description of the stream.
        :type files: list
        :param files: **[REQUIRED]**
          The files to stream.
          - *(dict) --*
            Represents a file to stream.
            - **fileId** *(integer) --*
              The file ID.
            - **s3Location** *(dict) --*
              The location of the file in S3.
              - **bucket** *(string) --*
                The S3 bucket.
              - **key** *(string) --*
                The S3 key.
              - **version** *(string) --*
                The S3 bucket version.
        :type roleArn: string
        :param roleArn: **[REQUIRED]**
          An IAM role that allows the IoT service principal assumes to access your S3 files.
        :rtype: dict
        :returns:
        """
        pass

    def create_thing(self, thingName: str, thingTypeName: str = None, attributePayload: Dict = None, billingGroupName: str = None) -> Dict:
        """
        Creates a thing record in the registry.
        .. note::
          This is a control plane operation. See `Authorization <https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html>`__ for information about authorizing control plane actions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateThing>`_
        
        **Request Syntax**
        ::
          response = client.create_thing(
              thingName='string',
              thingTypeName='string',
              attributePayload={
                  'attributes': {
                      'string': 'string'
                  },
                  'merge': True|False
              },
              billingGroupName='string'
          )
        
        **Response Syntax**
        ::
            {
                'thingName': 'string',
                'thingArn': 'string',
                'thingId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the CreateThing operation.
            - **thingName** *(string) --* 
              The name of the new thing.
            - **thingArn** *(string) --* 
              The ARN of the new thing.
            - **thingId** *(string) --* 
              The thing ID.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing to create.
        :type thingTypeName: string
        :param thingTypeName:
          The name of the thing type associated with the new thing.
        :type attributePayload: dict
        :param attributePayload:
          The attribute payload, which consists of up to three name/value pairs in a JSON document. For example:
           ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``
          - **attributes** *(dict) --*
            A JSON string containing up to three key-value pair in JSON format. For example:
             ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``
            - *(string) --*
              - *(string) --*
          - **merge** *(boolean) --*
            Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call ``UpdateThing`` with an empty attribute value.
            .. note::
              The ``merge`` attribute is only valid when calling ``UpdateThing`` .
        :type billingGroupName: string
        :param billingGroupName:
          The name of the billing group the thing will be added to.
        :rtype: dict
        :returns:
        """
        pass

    def create_thing_group(self, thingGroupName: str, parentGroupName: str = None, thingGroupProperties: Dict = None, tags: List = None) -> Dict:
        """
        Create a thing group.
        .. note::
          This is a control plane operation. See `Authorization <https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html>`__ for information about authorizing control plane actions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_thing_group(
              thingGroupName='string',
              parentGroupName='string',
              thingGroupProperties={
                  'thingGroupDescription': 'string',
                  'attributePayload': {
                      'attributes': {
                          'string': 'string'
                      },
                      'merge': True|False
                  }
              },
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'thingGroupName': 'string',
                'thingGroupArn': 'string',
                'thingGroupId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **thingGroupName** *(string) --* 
              The thing group name.
            - **thingGroupArn** *(string) --* 
              The thing group ARN.
            - **thingGroupId** *(string) --* 
              The thing group ID.
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The thing group name to create.
        :type parentGroupName: string
        :param parentGroupName:
          The name of the parent thing group.
        :type thingGroupProperties: dict
        :param thingGroupProperties:
          The thing group properties.
          - **thingGroupDescription** *(string) --*
            The thing group description.
          - **attributePayload** *(dict) --*
            The thing group attributes in JSON format.
            - **attributes** *(dict) --*
              A JSON string containing up to three key-value pair in JSON format. For example:
               ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``
              - *(string) --*
                - *(string) --*
            - **merge** *(boolean) --*
              Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.
              To remove an attribute, call ``UpdateThing`` with an empty attribute value.
              .. note::
                The ``merge`` attribute is only valid when calling ``UpdateThing`` .
        :type tags: list
        :param tags:
          Metadata which can be used to manage the thing group.
          - *(dict) --*
            A set of key/value pairs that are used to manage the resource.
            - **Key** *(string) --*
              The tag\'s key.
            - **Value** *(string) --*
              The tag\'s value.
        :rtype: dict
        :returns:
        """
        pass

    def create_thing_type(self, thingTypeName: str, thingTypeProperties: Dict = None, tags: List = None) -> Dict:
        """
        Creates a new thing type.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateThingType>`_
        
        **Request Syntax**
        ::
          response = client.create_thing_type(
              thingTypeName='string',
              thingTypeProperties={
                  'thingTypeDescription': 'string',
                  'searchableAttributes': [
                      'string',
                  ]
              },
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'thingTypeName': 'string',
                'thingTypeArn': 'string',
                'thingTypeId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the CreateThingType operation.
            - **thingTypeName** *(string) --* 
              The name of the thing type.
            - **thingTypeArn** *(string) --* 
              The Amazon Resource Name (ARN) of the thing type.
            - **thingTypeId** *(string) --* 
              The thing type ID.
        :type thingTypeName: string
        :param thingTypeName: **[REQUIRED]**
          The name of the thing type.
        :type thingTypeProperties: dict
        :param thingTypeProperties:
          The ThingTypeProperties for the thing type to create. It contains information about the new thing type including a description, and a list of searchable thing attribute names.
          - **thingTypeDescription** *(string) --*
            The description of the thing type.
          - **searchableAttributes** *(list) --*
            A list of searchable thing attribute names.
            - *(string) --*
        :type tags: list
        :param tags:
          Metadata which can be used to manage the thing type.
          - *(dict) --*
            A set of key/value pairs that are used to manage the resource.
            - **Key** *(string) --*
              The tag\'s key.
            - **Value** *(string) --*
              The tag\'s value.
        :rtype: dict
        :returns:
        """
        pass

    def create_topic_rule(self, ruleName: str, topicRulePayload: Dict, tags: str = None):
        """
        Creates a rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateTopicRule>`_
        
        **Request Syntax**
        ::
          response = client.create_topic_rule(
              ruleName='string',
              topicRulePayload={
                  'sql': 'string',
                  'description': 'string',
                  'actions': [
                      {
                          'dynamoDB': {
                              'tableName': 'string',
                              'roleArn': 'string',
                              'operation': 'string',
                              'hashKeyField': 'string',
                              'hashKeyValue': 'string',
                              'hashKeyType': 'STRING'|'NUMBER',
                              'rangeKeyField': 'string',
                              'rangeKeyValue': 'string',
                              'rangeKeyType': 'STRING'|'NUMBER',
                              'payloadField': 'string'
                          },
                          'dynamoDBv2': {
                              'roleArn': 'string',
                              'putItem': {
                                  'tableName': 'string'
                              }
                          },
                          'lambda': {
                              'functionArn': 'string'
                          },
                          'sns': {
                              'targetArn': 'string',
                              'roleArn': 'string',
                              'messageFormat': 'RAW'|'JSON'
                          },
                          'sqs': {
                              'roleArn': 'string',
                              'queueUrl': 'string',
                              'useBase64': True|False
                          },
                          'kinesis': {
                              'roleArn': 'string',
                              'streamName': 'string',
                              'partitionKey': 'string'
                          },
                          'republish': {
                              'roleArn': 'string',
                              'topic': 'string'
                          },
                          's3': {
                              'roleArn': 'string',
                              'bucketName': 'string',
                              'key': 'string',
                              'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                          },
                          'firehose': {
                              'roleArn': 'string',
                              'deliveryStreamName': 'string',
                              'separator': 'string'
                          },
                          'cloudwatchMetric': {
                              'roleArn': 'string',
                              'metricNamespace': 'string',
                              'metricName': 'string',
                              'metricValue': 'string',
                              'metricUnit': 'string',
                              'metricTimestamp': 'string'
                          },
                          'cloudwatchAlarm': {
                              'roleArn': 'string',
                              'alarmName': 'string',
                              'stateReason': 'string',
                              'stateValue': 'string'
                          },
                          'elasticsearch': {
                              'roleArn': 'string',
                              'endpoint': 'string',
                              'index': 'string',
                              'type': 'string',
                              'id': 'string'
                          },
                          'salesforce': {
                              'token': 'string',
                              'url': 'string'
                          },
                          'iotAnalytics': {
                              'channelArn': 'string',
                              'channelName': 'string',
                              'roleArn': 'string'
                          },
                          'iotEvents': {
                              'inputName': 'string',
                              'messageId': 'string',
                              'roleArn': 'string'
                          },
                          'stepFunctions': {
                              'executionNamePrefix': 'string',
                              'stateMachineName': 'string',
                              'roleArn': 'string'
                          }
                      },
                  ],
                  'ruleDisabled': True|False,
                  'awsIotSqlVersion': 'string',
                  'errorAction': {
                      'dynamoDB': {
                          'tableName': 'string',
                          'roleArn': 'string',
                          'operation': 'string',
                          'hashKeyField': 'string',
                          'hashKeyValue': 'string',
                          'hashKeyType': 'STRING'|'NUMBER',
                          'rangeKeyField': 'string',
                          'rangeKeyValue': 'string',
                          'rangeKeyType': 'STRING'|'NUMBER',
                          'payloadField': 'string'
                      },
                      'dynamoDBv2': {
                          'roleArn': 'string',
                          'putItem': {
                              'tableName': 'string'
                          }
                      },
                      'lambda': {
                          'functionArn': 'string'
                      },
                      'sns': {
                          'targetArn': 'string',
                          'roleArn': 'string',
                          'messageFormat': 'RAW'|'JSON'
                      },
                      'sqs': {
                          'roleArn': 'string',
                          'queueUrl': 'string',
                          'useBase64': True|False
                      },
                      'kinesis': {
                          'roleArn': 'string',
                          'streamName': 'string',
                          'partitionKey': 'string'
                      },
                      'republish': {
                          'roleArn': 'string',
                          'topic': 'string'
                      },
                      's3': {
                          'roleArn': 'string',
                          'bucketName': 'string',
                          'key': 'string',
                          'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                      },
                      'firehose': {
                          'roleArn': 'string',
                          'deliveryStreamName': 'string',
                          'separator': 'string'
                      },
                      'cloudwatchMetric': {
                          'roleArn': 'string',
                          'metricNamespace': 'string',
                          'metricName': 'string',
                          'metricValue': 'string',
                          'metricUnit': 'string',
                          'metricTimestamp': 'string'
                      },
                      'cloudwatchAlarm': {
                          'roleArn': 'string',
                          'alarmName': 'string',
                          'stateReason': 'string',
                          'stateValue': 'string'
                      },
                      'elasticsearch': {
                          'roleArn': 'string',
                          'endpoint': 'string',
                          'index': 'string',
                          'type': 'string',
                          'id': 'string'
                      },
                      'salesforce': {
                          'token': 'string',
                          'url': 'string'
                      },
                      'iotAnalytics': {
                          'channelArn': 'string',
                          'channelName': 'string',
                          'roleArn': 'string'
                      },
                      'iotEvents': {
                          'inputName': 'string',
                          'messageId': 'string',
                          'roleArn': 'string'
                      },
                      'stepFunctions': {
                          'executionNamePrefix': 'string',
                          'stateMachineName': 'string',
                          'roleArn': 'string'
                      }
                  }
              },
              tags='string'
          )
        :type ruleName: string
        :param ruleName: **[REQUIRED]**
          The name of the rule.
        :type topicRulePayload: dict
        :param topicRulePayload: **[REQUIRED]**
          The rule payload.
          - **sql** *(string) --* **[REQUIRED]**
            The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference>`__ in the *AWS IoT Developer Guide* .
          - **description** *(string) --*
            The description of the rule.
          - **actions** *(list) --* **[REQUIRED]**
            The actions associated with the rule.
            - *(dict) --*
              Describes the actions associated with a rule.
              - **dynamoDB** *(dict) --*
                Write to a DynamoDB table.
                - **tableName** *(string) --* **[REQUIRED]**
                  The name of the DynamoDB table.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access to the DynamoDB table.
                - **operation** *(string) --*
                  The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .
                - **hashKeyField** *(string) --* **[REQUIRED]**
                  The hash key name.
                - **hashKeyValue** *(string) --* **[REQUIRED]**
                  The hash key value.
                - **hashKeyType** *(string) --*
                  The hash key type. Valid values are \"STRING\" or \"NUMBER\"
                - **rangeKeyField** *(string) --*
                  The range key name.
                - **rangeKeyValue** *(string) --*
                  The range key value.
                - **rangeKeyType** *(string) --*
                  The range key type. Valid values are \"STRING\" or \"NUMBER\"
                - **payloadField** *(string) --*
                  The action payload. This name can be customized.
              - **dynamoDBv2** *(dict) --*
                Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access to the DynamoDB table.
                - **putItem** *(dict) --* **[REQUIRED]**
                  Specifies the DynamoDB table to which the message data will be written. For example:
                   ``{ \"dynamoDBv2\": { \"roleArn\": \"aws:iam:12341251:my-role\" \"putItem\": { \"tableName\": \"my-table\" } } }``
                  Each attribute in the message payload will be written to a separate column in the DynamoDB database.
                  - **tableName** *(string) --* **[REQUIRED]**
                    The table where the message data will be written
              - **lambda** *(dict) --*
                Invoke a Lambda function.
                - **functionArn** *(string) --* **[REQUIRED]**
                  The ARN of the Lambda function.
              - **sns** *(dict) --*
                Publish to an Amazon SNS topic.
                - **targetArn** *(string) --* **[REQUIRED]**
                  The ARN of the SNS topic.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access.
                - **messageFormat** *(string) --*
                  (Optional) The message format of the message to publish. Accepted values are \"JSON\" and \"RAW\". The default value of the attribute is \"RAW\". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `https\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.
              - **sqs** *(dict) --*
                Publish to an Amazon SQS queue.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access.
                - **queueUrl** *(string) --* **[REQUIRED]**
                  The URL of the Amazon SQS queue.
                - **useBase64** *(boolean) --*
                  Specifies whether to use Base64 encoding.
              - **kinesis** *(dict) --*
                Write data to an Amazon Kinesis stream.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access to the Amazon Kinesis stream.
                - **streamName** *(string) --* **[REQUIRED]**
                  The name of the Amazon Kinesis stream.
                - **partitionKey** *(string) --*
                  The partition key.
              - **republish** *(dict) --*
                Publish to another MQTT topic.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access.
                - **topic** *(string) --* **[REQUIRED]**
                  The name of the MQTT topic.
              - **s3** *(dict) --*
                Write to an Amazon S3 bucket.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access.
                - **bucketName** *(string) --* **[REQUIRED]**
                  The Amazon S3 bucket.
                - **key** *(string) --* **[REQUIRED]**
                  The object key.
                - **cannedAcl** *(string) --*
                  The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
              - **firehose** *(dict) --*
                Write to an Amazon Kinesis Firehose stream.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The IAM role that grants access to the Amazon Kinesis Firehose stream.
                - **deliveryStreamName** *(string) --* **[REQUIRED]**
                  The delivery stream name.
                - **separator** *(string) --*
                  A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'\n\' (newline), \'\t\' (tab), \'\r\n\' (Windows newline), \',\' (comma).
              - **cloudwatchMetric** *(dict) --*
                Capture a CloudWatch metric.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The IAM role that allows access to the CloudWatch metric.
                - **metricNamespace** *(string) --* **[REQUIRED]**
                  The CloudWatch metric namespace name.
                - **metricName** *(string) --* **[REQUIRED]**
                  The CloudWatch metric name.
                - **metricValue** *(string) --* **[REQUIRED]**
                  The CloudWatch metric value.
                - **metricUnit** *(string) --* **[REQUIRED]**
                  The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.
                - **metricTimestamp** *(string) --*
                  An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .
              - **cloudwatchAlarm** *(dict) --*
                Change the state of a CloudWatch alarm.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The IAM role that allows access to the CloudWatch alarm.
                - **alarmName** *(string) --* **[REQUIRED]**
                  The CloudWatch alarm name.
                - **stateReason** *(string) --* **[REQUIRED]**
                  The reason for the alarm change.
                - **stateValue** *(string) --* **[REQUIRED]**
                  The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
              - **elasticsearch** *(dict) --*
                Write data to an Amazon Elasticsearch Service domain.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The IAM role ARN that has access to Elasticsearch.
                - **endpoint** *(string) --* **[REQUIRED]**
                  The endpoint of your Elasticsearch domain.
                - **index** *(string) --* **[REQUIRED]**
                  The Elasticsearch index where you want to store your data.
                - **type** *(string) --* **[REQUIRED]**
                  The type of document you are storing.
                - **id** *(string) --* **[REQUIRED]**
                  The unique identifier for the document you are storing.
              - **salesforce** *(dict) --*
                Send a message to a Salesforce IoT Cloud Input Stream.
                - **token** *(string) --* **[REQUIRED]**
                  The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
                - **url** *(string) --* **[REQUIRED]**
                  The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
              - **iotAnalytics** *(dict) --*
                Sends message data to an AWS IoT Analytics channel.
                - **channelArn** *(string) --*
                  (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
                - **channelName** *(string) --*
                  The name of the IoT Analytics channel to which message data will be sent.
                - **roleArn** *(string) --*
                  The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
              - **iotEvents** *(dict) --*
                Sends an input to an AWS IoT Events detector.
                - **inputName** *(string) --* **[REQUIRED]**
                  The name of the AWS IoT Events input.
                - **messageId** *(string) --*
                  [Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. (\"Action\":\"iotevents:BatchPutMessage\").
              - **stepFunctions** *(dict) --*
                Starts execution of a Step Functions state machine.
                - **executionNamePrefix** *(string) --*
                  (Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
                - **stateMachineName** *(string) --* **[REQUIRED]**
                  The name of the Step Functions state machine whose execution will be started.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the role that grants IoT permission to start execution of a state machine (\"Action\":\"states:StartExecution\").
          - **ruleDisabled** *(boolean) --*
            Specifies whether the rule is disabled.
          - **awsIotSqlVersion** *(string) --*
            The version of the SQL rules engine to use when evaluating the rule.
          - **errorAction** *(dict) --*
            The action to take when an error occurs.
            - **dynamoDB** *(dict) --*
              Write to a DynamoDB table.
              - **tableName** *(string) --* **[REQUIRED]**
                The name of the DynamoDB table.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access to the DynamoDB table.
              - **operation** *(string) --*
                The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .
              - **hashKeyField** *(string) --* **[REQUIRED]**
                The hash key name.
              - **hashKeyValue** *(string) --* **[REQUIRED]**
                The hash key value.
              - **hashKeyType** *(string) --*
                The hash key type. Valid values are \"STRING\" or \"NUMBER\"
              - **rangeKeyField** *(string) --*
                The range key name.
              - **rangeKeyValue** *(string) --*
                The range key value.
              - **rangeKeyType** *(string) --*
                The range key type. Valid values are \"STRING\" or \"NUMBER\"
              - **payloadField** *(string) --*
                The action payload. This name can be customized.
            - **dynamoDBv2** *(dict) --*
              Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access to the DynamoDB table.
              - **putItem** *(dict) --* **[REQUIRED]**
                Specifies the DynamoDB table to which the message data will be written. For example:
                 ``{ \"dynamoDBv2\": { \"roleArn\": \"aws:iam:12341251:my-role\" \"putItem\": { \"tableName\": \"my-table\" } } }``
                Each attribute in the message payload will be written to a separate column in the DynamoDB database.
                - **tableName** *(string) --* **[REQUIRED]**
                  The table where the message data will be written
            - **lambda** *(dict) --*
              Invoke a Lambda function.
              - **functionArn** *(string) --* **[REQUIRED]**
                The ARN of the Lambda function.
            - **sns** *(dict) --*
              Publish to an Amazon SNS topic.
              - **targetArn** *(string) --* **[REQUIRED]**
                The ARN of the SNS topic.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access.
              - **messageFormat** *(string) --*
                (Optional) The message format of the message to publish. Accepted values are \"JSON\" and \"RAW\". The default value of the attribute is \"RAW\". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `https\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.
            - **sqs** *(dict) --*
              Publish to an Amazon SQS queue.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access.
              - **queueUrl** *(string) --* **[REQUIRED]**
                The URL of the Amazon SQS queue.
              - **useBase64** *(boolean) --*
                Specifies whether to use Base64 encoding.
            - **kinesis** *(dict) --*
              Write data to an Amazon Kinesis stream.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access to the Amazon Kinesis stream.
              - **streamName** *(string) --* **[REQUIRED]**
                The name of the Amazon Kinesis stream.
              - **partitionKey** *(string) --*
                The partition key.
            - **republish** *(dict) --*
              Publish to another MQTT topic.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access.
              - **topic** *(string) --* **[REQUIRED]**
                The name of the MQTT topic.
            - **s3** *(dict) --*
              Write to an Amazon S3 bucket.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access.
              - **bucketName** *(string) --* **[REQUIRED]**
                The Amazon S3 bucket.
              - **key** *(string) --* **[REQUIRED]**
                The object key.
              - **cannedAcl** *(string) --*
                The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
            - **firehose** *(dict) --*
              Write to an Amazon Kinesis Firehose stream.
              - **roleArn** *(string) --* **[REQUIRED]**
                The IAM role that grants access to the Amazon Kinesis Firehose stream.
              - **deliveryStreamName** *(string) --* **[REQUIRED]**
                The delivery stream name.
              - **separator** *(string) --*
                A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'\n\' (newline), \'\t\' (tab), \'\r\n\' (Windows newline), \',\' (comma).
            - **cloudwatchMetric** *(dict) --*
              Capture a CloudWatch metric.
              - **roleArn** *(string) --* **[REQUIRED]**
                The IAM role that allows access to the CloudWatch metric.
              - **metricNamespace** *(string) --* **[REQUIRED]**
                The CloudWatch metric namespace name.
              - **metricName** *(string) --* **[REQUIRED]**
                The CloudWatch metric name.
              - **metricValue** *(string) --* **[REQUIRED]**
                The CloudWatch metric value.
              - **metricUnit** *(string) --* **[REQUIRED]**
                The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.
              - **metricTimestamp** *(string) --*
                An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .
            - **cloudwatchAlarm** *(dict) --*
              Change the state of a CloudWatch alarm.
              - **roleArn** *(string) --* **[REQUIRED]**
                The IAM role that allows access to the CloudWatch alarm.
              - **alarmName** *(string) --* **[REQUIRED]**
                The CloudWatch alarm name.
              - **stateReason** *(string) --* **[REQUIRED]**
                The reason for the alarm change.
              - **stateValue** *(string) --* **[REQUIRED]**
                The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            - **elasticsearch** *(dict) --*
              Write data to an Amazon Elasticsearch Service domain.
              - **roleArn** *(string) --* **[REQUIRED]**
                The IAM role ARN that has access to Elasticsearch.
              - **endpoint** *(string) --* **[REQUIRED]**
                The endpoint of your Elasticsearch domain.
              - **index** *(string) --* **[REQUIRED]**
                The Elasticsearch index where you want to store your data.
              - **type** *(string) --* **[REQUIRED]**
                The type of document you are storing.
              - **id** *(string) --* **[REQUIRED]**
                The unique identifier for the document you are storing.
            - **salesforce** *(dict) --*
              Send a message to a Salesforce IoT Cloud Input Stream.
              - **token** *(string) --* **[REQUIRED]**
                The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
              - **url** *(string) --* **[REQUIRED]**
                The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            - **iotAnalytics** *(dict) --*
              Sends message data to an AWS IoT Analytics channel.
              - **channelArn** *(string) --*
                (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
              - **channelName** *(string) --*
                The name of the IoT Analytics channel to which message data will be sent.
              - **roleArn** *(string) --*
                The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
            - **iotEvents** *(dict) --*
              Sends an input to an AWS IoT Events detector.
              - **inputName** *(string) --* **[REQUIRED]**
                The name of the AWS IoT Events input.
              - **messageId** *(string) --*
                [Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. (\"Action\":\"iotevents:BatchPutMessage\").
            - **stepFunctions** *(dict) --*
              Starts execution of a Step Functions state machine.
              - **executionNamePrefix** *(string) --*
                (Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
              - **stateMachineName** *(string) --* **[REQUIRED]**
                The name of the Step Functions state machine whose execution will be started.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the role that grants IoT permission to start execution of a state machine (\"Action\":\"states:StartExecution\").
        :type tags: string
        :param tags:
          Metadata which can be used to manage the topic rule.
          .. note::
            For URI Request parameters use format: ...key1=value1&key2=value2...
            For the CLI command-line parameter use format: --tags \"key1=value1&key2=value2...\"
            For the cli-input-json file use format: \"tags\": \"key1=value1&key2=value2...\"
        :returns: None
        """
        pass

    def delete_account_audit_configuration(self, deleteScheduledAudits: bool = None) -> Dict:
        """
        Restores the default settings for Device Defender audits for this account. Any configuration data you entered is deleted and all audit checks are reset to disabled. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteAccountAuditConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_account_audit_configuration(
              deleteScheduledAudits=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type deleteScheduledAudits: boolean
        :param deleteScheduledAudits:
          If true, all scheduled audits are deleted.
        :rtype: dict
        :returns:
        """
        pass

    def delete_authorizer(self, authorizerName: str) -> Dict:
        """
        Deletes an authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.delete_authorizer(
              authorizerName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type authorizerName: string
        :param authorizerName: **[REQUIRED]**
          The name of the authorizer to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_billing_group(self, billingGroupName: str, expectedVersion: int = None) -> Dict:
        """
        Deletes the billing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteBillingGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_billing_group(
              billingGroupName='string',
              expectedVersion=123
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type billingGroupName: string
        :param billingGroupName: **[REQUIRED]**
          The name of the billing group.
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the ``DeleteBillingGroup`` request is rejected with a ``VersionConflictException`` .
        :rtype: dict
        :returns:
        """
        pass

    def delete_ca_certificate(self, certificateId: str) -> Dict:
        """
        Deletes a registered CA certificate.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteCACertificate>`_
        
        **Request Syntax**
        ::
          response = client.delete_ca_certificate(
              certificateId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output for the DeleteCACertificate operation.
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The ID of the certificate to delete. (The last part of the certificate ARN contains the certificate ID.)
        :rtype: dict
        :returns:
        """
        pass

    def delete_certificate(self, certificateId: str, forceDelete: bool = None):
        """
        Deletes the specified certificate.
        A certificate cannot be deleted if it has a policy attached to it or if its status is set to ACTIVE. To delete a certificate, first use the  DetachPrincipalPolicy API to detach all policies. Next, use the  UpdateCertificate API to set the certificate to the INACTIVE status.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteCertificate>`_
        
        **Request Syntax**
        ::
          response = client.delete_certificate(
              certificateId='string',
              forceDelete=True|False
          )
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        :type forceDelete: boolean
        :param forceDelete:
          Forces a certificate request to be deleted.
        :returns: None
        """
        pass

    def delete_dynamic_thing_group(self, thingGroupName: str, expectedVersion: int = None) -> Dict:
        """
        Deletes a dynamic thing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteDynamicThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_dynamic_thing_group(
              thingGroupName='string',
              expectedVersion=123
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The name of the dynamic thing group to delete.
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the dynamic thing group to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_job(self, jobId: str, force: bool = None):
        """
        Deletes a job and its related job executions.
        Deleting a job may take time, depending on the number of job executions created for the job and various other factors. While the job is being deleted, the status of the job will be shown as "DELETION_IN_PROGRESS". Attempting to delete or cancel a job whose status is already "DELETION_IN_PROGRESS" will result in an error.
        Only 10 jobs may have status "DELETION_IN_PROGRESS" at the same time, or a LimitExceededException will occur.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteJob>`_
        
        **Request Syntax**
        ::
          response = client.delete_job(
              jobId='string',
              force=True|False
          )
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The ID of the job to be deleted.
          After a job deletion is completed, you may reuse this jobId when you create a new job. However, this is not recommended, and you must ensure that your devices are not using the jobId to refer to the deleted job.
        :type force: boolean
        :param force:
          (Optional) When true, you can delete a job which is \"IN_PROGRESS\". Otherwise, you can only delete a job which is in a terminal state (\"COMPLETED\" or \"CANCELED\") or an exception will occur. The default is false.
          .. note::
            Deleting a job which is \"IN_PROGRESS\", will cause a device which is executing the job to be unable to access job information or update the job execution status. Use caution and ensure that each device executing a job which is deleted is able to recover to a valid state.
        :returns: None
        """
        pass

    def delete_job_execution(self, jobId: str, thingName: str, executionNumber: int, force: bool = None):
        """
        Deletes a job execution.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteJobExecution>`_
        
        **Request Syntax**
        ::
          response = client.delete_job_execution(
              jobId='string',
              thingName='string',
              executionNumber=123,
              force=True|False
          )
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The ID of the job whose execution on a particular device will be deleted.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing whose job execution will be deleted.
        :type executionNumber: integer
        :param executionNumber: **[REQUIRED]**
          The ID of the job execution to be deleted. The ``executionNumber`` refers to the execution of a particular job on a particular device.
          Note that once a job execution is deleted, the ``executionNumber`` may be reused by IoT, so be sure you get and use the correct value here.
        :type force: boolean
        :param force:
          (Optional) When true, you can delete a job execution which is \"IN_PROGRESS\". Otherwise, you can only delete a job execution which is in a terminal state (\"SUCCEEDED\", \"FAILED\", \"REJECTED\", \"REMOVED\" or \"CANCELED\") or an exception will occur. The default is false.
          .. note::
            Deleting a job execution which is \"IN_PROGRESS\", will cause the device to be unable to access job information or update the job execution status. Use caution and ensure that the device is able to recover to a valid state.
        :returns: None
        """
        pass

    def delete_ota_update(self, otaUpdateId: str, deleteStream: bool = None, forceDeleteAWSJob: bool = None) -> Dict:
        """
        Delete an OTA update.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteOTAUpdate>`_
        
        **Request Syntax**
        ::
          response = client.delete_ota_update(
              otaUpdateId='string',
              deleteStream=True|False,
              forceDeleteAWSJob=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type otaUpdateId: string
        :param otaUpdateId: **[REQUIRED]**
          The OTA update ID to delete.
        :type deleteStream: boolean
        :param deleteStream:
          Specifies if the stream associated with an OTA update should be deleted when the OTA update is deleted.
        :type forceDeleteAWSJob: boolean
        :param forceDeleteAWSJob:
          Specifies if the AWS Job associated with the OTA update should be deleted with the OTA update is deleted.
        :rtype: dict
        :returns:
        """
        pass

    def delete_policy(self, policyName: str):
        """
        Deletes the specified policy.
        A policy cannot be deleted if it has non-default versions or it is attached to any certificate.
        To delete a policy, use the DeletePolicyVersion API to delete all non-default versions of the policy; use the DetachPrincipalPolicy API to detach the policy from any certificate; and then use the DeletePolicy API to delete the policy.
        When a policy is deleted using DeletePolicy, its default version is deleted with it.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeletePolicy>`_
        
        **Request Syntax**
        ::
          response = client.delete_policy(
              policyName='string'
          )
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The name of the policy to delete.
        :returns: None
        """
        pass

    def delete_policy_version(self, policyName: str, policyVersionId: str):
        """
        Deletes the specified version of the specified policy. You cannot delete the default version of a policy using this API. To delete the default version of a policy, use  DeletePolicy . To find out which version of a policy is marked as the default version, use ListPolicyVersions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeletePolicyVersion>`_
        
        **Request Syntax**
        ::
          response = client.delete_policy_version(
              policyName='string',
              policyVersionId='string'
          )
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The name of the policy.
        :type policyVersionId: string
        :param policyVersionId: **[REQUIRED]**
          The policy version ID.
        :returns: None
        """
        pass

    def delete_registration_code(self) -> Dict:
        """
        Deletes a CA certificate registration code.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteRegistrationCode>`_
        
        **Request Syntax**
        ::
          response = client.delete_registration_code()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output for the DeleteRegistrationCode operation.
        :rtype: dict
        :returns:
        """
        pass

    def delete_role_alias(self, roleAlias: str) -> Dict:
        """
        Deletes a role alias
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteRoleAlias>`_
        
        **Request Syntax**
        ::
          response = client.delete_role_alias(
              roleAlias='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type roleAlias: string
        :param roleAlias: **[REQUIRED]**
          The role alias to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_scheduled_audit(self, scheduledAuditName: str) -> Dict:
        """
        Deletes a scheduled audit.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteScheduledAudit>`_
        
        **Request Syntax**
        ::
          response = client.delete_scheduled_audit(
              scheduledAuditName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type scheduledAuditName: string
        :param scheduledAuditName: **[REQUIRED]**
          The name of the scheduled audit you want to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_security_profile(self, securityProfileName: str, expectedVersion: int = None) -> Dict:
        """
        Deletes a Device Defender security profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteSecurityProfile>`_
        
        **Request Syntax**
        ::
          response = client.delete_security_profile(
              securityProfileName='string',
              expectedVersion=123
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type securityProfileName: string
        :param securityProfileName: **[REQUIRED]**
          The name of the security profile to be deleted.
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different than the actual version, a ``VersionConflictException`` is thrown.
        :rtype: dict
        :returns:
        """
        pass

    def delete_stream(self, streamId: str) -> Dict:
        """
        Deletes a stream.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteStream>`_
        
        **Request Syntax**
        ::
          response = client.delete_stream(
              streamId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type streamId: string
        :param streamId: **[REQUIRED]**
          The stream ID.
        :rtype: dict
        :returns:
        """
        pass

    def delete_thing(self, thingName: str, expectedVersion: int = None) -> Dict:
        """
        Deletes the specified thing. Returns successfully with no error if the deletion is successful or you specify a thing that doesn't exist.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteThing>`_
        
        **Request Syntax**
        ::
          response = client.delete_thing(
              thingName='string',
              expectedVersion=123
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output of the DeleteThing operation.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing to delete.
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the ``DeleteThing`` request is rejected with a ``VersionConflictException`` .
        :rtype: dict
        :returns:
        """
        pass

    def delete_thing_group(self, thingGroupName: str, expectedVersion: int = None) -> Dict:
        """
        Deletes a thing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_thing_group(
              thingGroupName='string',
              expectedVersion=123
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The name of the thing group to delete.
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the thing group to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_thing_type(self, thingTypeName: str) -> Dict:
        """
        Deletes the specified thing type. You cannot delete a thing type if it has things associated with it. To delete a thing type, first mark it as deprecated by calling  DeprecateThingType , then remove any associated things by calling  UpdateThing to change the thing type on any associated thing, and finally use  DeleteThingType to delete the thing type.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteThingType>`_
        
        **Request Syntax**
        ::
          response = client.delete_thing_type(
              thingTypeName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output for the DeleteThingType operation.
        :type thingTypeName: string
        :param thingTypeName: **[REQUIRED]**
          The name of the thing type.
        :rtype: dict
        :returns:
        """
        pass

    def delete_topic_rule(self, ruleName: str):
        """
        Deletes the rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteTopicRule>`_
        
        **Request Syntax**
        ::
          response = client.delete_topic_rule(
              ruleName='string'
          )
        :type ruleName: string
        :param ruleName: **[REQUIRED]**
          The name of the rule.
        :returns: None
        """
        pass

    def delete_v2_logging_level(self, targetType: str, targetName: str):
        """
        Deletes a logging level.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteV2LoggingLevel>`_
        
        **Request Syntax**
        ::
          response = client.delete_v2_logging_level(
              targetType='DEFAULT'|'THING_GROUP',
              targetName='string'
          )
        :type targetType: string
        :param targetType: **[REQUIRED]**
          The type of resource for which you are configuring logging. Must be ``THING_Group`` .
        :type targetName: string
        :param targetName: **[REQUIRED]**
          The name of the resource for which you are configuring logging.
        :returns: None
        """
        pass

    def deprecate_thing_type(self, thingTypeName: str, undoDeprecate: bool = None) -> Dict:
        """
        Deprecates a thing type. You can not associate new things with deprecated thing type.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeprecateThingType>`_
        
        **Request Syntax**
        ::
          response = client.deprecate_thing_type(
              thingTypeName='string',
              undoDeprecate=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output for the DeprecateThingType operation.
        :type thingTypeName: string
        :param thingTypeName: **[REQUIRED]**
          The name of the thing type to deprecate.
        :type undoDeprecate: boolean
        :param undoDeprecate:
          Whether to undeprecate a deprecated thing type. If **true** , the thing type will not be deprecated anymore and you can associate it with things.
        :rtype: dict
        :returns:
        """
        pass

    def describe_account_audit_configuration(self) -> Dict:
        """
        Gets information about the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeAccountAuditConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.describe_account_audit_configuration()
        
        **Response Syntax**
        ::
            {
                'roleArn': 'string',
                'auditNotificationTargetConfigurations': {
                    'string': {
                        'targetArn': 'string',
                        'roleArn': 'string',
                        'enabled': True|False
                    }
                },
                'auditCheckConfigurations': {
                    'string': {
                        'enabled': True|False
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **roleArn** *(string) --* 
              The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as necessary when performing an audit.
              On the first call to ``UpdateAccountAuditConfiguration`` this parameter is required.
            - **auditNotificationTargetConfigurations** *(dict) --* 
              Information about the targets to which audit notifications are sent for this account.
              - *(string) --* 
                - *(dict) --* 
                  Information about the targets to which audit notifications are sent.
                  - **targetArn** *(string) --* 
                    The ARN of the target (SNS topic) to which audit notifications are sent.
                  - **roleArn** *(string) --* 
                    The ARN of the role that grants permission to send notifications to the target.
                  - **enabled** *(boolean) --* 
                    True if notifications to the target are enabled.
            - **auditCheckConfigurations** *(dict) --* 
              Which audit checks are enabled and disabled for this account.
              - *(string) --* 
                An audit check name. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
                - *(dict) --* 
                  Which audit checks are enabled and disabled for this account.
                  - **enabled** *(boolean) --* 
                    True if this audit check is enabled for this account.
        :rtype: dict
        :returns:
        """
        pass

    def describe_audit_task(self, taskId: str) -> Dict:
        """
        Gets information about a Device Defender audit.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeAuditTask>`_
        
        **Request Syntax**
        ::
          response = client.describe_audit_task(
              taskId='string'
          )
        
        **Response Syntax**
        ::
            {
                'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
                'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK',
                'taskStartTime': datetime(2015, 1, 1),
                'taskStatistics': {
                    'totalChecks': 123,
                    'inProgressChecks': 123,
                    'waitingForDataCollectionChecks': 123,
                    'compliantChecks': 123,
                    'nonCompliantChecks': 123,
                    'failedChecks': 123,
                    'canceledChecks': 123
                },
                'scheduledAuditName': 'string',
                'auditDetails': {
                    'string': {
                        'checkRunStatus': 'IN_PROGRESS'|'WAITING_FOR_DATA_COLLECTION'|'CANCELED'|'COMPLETED_COMPLIANT'|'COMPLETED_NON_COMPLIANT'|'FAILED',
                        'checkCompliant': True|False,
                        'totalResourcesCount': 123,
                        'nonCompliantResourcesCount': 123,
                        'errorCode': 'string',
                        'message': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskStatus** *(string) --* 
              The status of the audit: one of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".
            - **taskType** *(string) --* 
              The type of audit: "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".
            - **taskStartTime** *(datetime) --* 
              The time the audit started.
            - **taskStatistics** *(dict) --* 
              Statistical information about the audit.
              - **totalChecks** *(integer) --* 
                The number of checks in this audit.
              - **inProgressChecks** *(integer) --* 
                The number of checks in progress.
              - **waitingForDataCollectionChecks** *(integer) --* 
                The number of checks waiting for data collection.
              - **compliantChecks** *(integer) --* 
                The number of checks that found compliant resources.
              - **nonCompliantChecks** *(integer) --* 
                The number of checks that found non-compliant resources.
              - **failedChecks** *(integer) --* 
                The number of checks 
              - **canceledChecks** *(integer) --* 
                The number of checks that did not run because the audit was canceled.
            - **scheduledAuditName** *(string) --* 
              The name of the scheduled audit (only if the audit was a scheduled audit).
            - **auditDetails** *(dict) --* 
              Detailed information about each check performed during this audit.
              - *(string) --* 
                An audit check name. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
                - *(dict) --* 
                  Information about the audit check.
                  - **checkRunStatus** *(string) --* 
                    The completion status of this check, one of "IN_PROGRESS", "WAITING_FOR_DATA_COLLECTION", "CANCELED", "COMPLETED_COMPLIANT", "COMPLETED_NON_COMPLIANT", or "FAILED".
                  - **checkCompliant** *(boolean) --* 
                    True if the check completed and found all resources compliant.
                  - **totalResourcesCount** *(integer) --* 
                    The number of resources on which the check was performed.
                  - **nonCompliantResourcesCount** *(integer) --* 
                    The number of resources that the check found non-compliant.
                  - **errorCode** *(string) --* 
                    The code of any error encountered when performing this check during this audit. One of "INSUFFICIENT_PERMISSIONS", or "AUDIT_CHECK_DISABLED".
                  - **message** *(string) --* 
                    The message associated with any error encountered when performing this check during this audit.
        :type taskId: string
        :param taskId: **[REQUIRED]**
          The ID of the audit whose information you want to get.
        :rtype: dict
        :returns:
        """
        pass

    def describe_authorizer(self, authorizerName: str) -> Dict:
        """
        Describes an authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.describe_authorizer(
              authorizerName='string'
          )
        
        **Response Syntax**
        ::
            {
                'authorizerDescription': {
                    'authorizerName': 'string',
                    'authorizerArn': 'string',
                    'authorizerFunctionArn': 'string',
                    'tokenKeyName': 'string',
                    'tokenSigningPublicKeys': {
                        'string': 'string'
                    },
                    'status': 'ACTIVE'|'INACTIVE',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **authorizerDescription** *(dict) --* 
              The authorizer description.
              - **authorizerName** *(string) --* 
                The authorizer name.
              - **authorizerArn** *(string) --* 
                The authorizer ARN.
              - **authorizerFunctionArn** *(string) --* 
                The authorizer's Lambda function ARN.
              - **tokenKeyName** *(string) --* 
                The key used to extract the token from the HTTP headers.
              - **tokenSigningPublicKeys** *(dict) --* 
                The public keys used to validate the token signature returned by your custom authentication service.
                - *(string) --* 
                  - *(string) --* 
              - **status** *(string) --* 
                The status of the authorizer.
              - **creationDate** *(datetime) --* 
                The UNIX timestamp of when the authorizer was created.
              - **lastModifiedDate** *(datetime) --* 
                The UNIX timestamp of when the authorizer was last updated.
        :type authorizerName: string
        :param authorizerName: **[REQUIRED]**
          The name of the authorizer to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_billing_group(self, billingGroupName: str) -> Dict:
        """
        Returns information about a billing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeBillingGroup>`_
        
        **Request Syntax**
        ::
          response = client.describe_billing_group(
              billingGroupName='string'
          )
        
        **Response Syntax**
        ::
            {
                'billingGroupName': 'string',
                'billingGroupId': 'string',
                'billingGroupArn': 'string',
                'version': 123,
                'billingGroupProperties': {
                    'billingGroupDescription': 'string'
                },
                'billingGroupMetadata': {
                    'creationDate': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **billingGroupName** *(string) --* 
              The name of the billing group.
            - **billingGroupId** *(string) --* 
              The ID of the billing group.
            - **billingGroupArn** *(string) --* 
              The ARN of the billing group.
            - **version** *(integer) --* 
              The version of the billing group.
            - **billingGroupProperties** *(dict) --* 
              The properties of the billing group.
              - **billingGroupDescription** *(string) --* 
                The description of the billing group.
            - **billingGroupMetadata** *(dict) --* 
              Additional information about the billing group.
              - **creationDate** *(datetime) --* 
                The date the billing group was created.
        :type billingGroupName: string
        :param billingGroupName: **[REQUIRED]**
          The name of the billing group.
        :rtype: dict
        :returns:
        """
        pass

    def describe_ca_certificate(self, certificateId: str) -> Dict:
        """
        Describes a registered CA certificate.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeCACertificate>`_
        
        **Request Syntax**
        ::
          response = client.describe_ca_certificate(
              certificateId='string'
          )
        
        **Response Syntax**
        ::
            {
                'certificateDescription': {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'status': 'ACTIVE'|'INACTIVE',
                    'certificatePem': 'string',
                    'ownedBy': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'autoRegistrationStatus': 'ENABLE'|'DISABLE',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'customerVersion': 123,
                    'generationId': 'string',
                    'validity': {
                        'notBefore': datetime(2015, 1, 1),
                        'notAfter': datetime(2015, 1, 1)
                    }
                },
                'registrationConfig': {
                    'templateBody': 'string',
                    'roleArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the DescribeCACertificate operation.
            - **certificateDescription** *(dict) --* 
              The CA certificate description.
              - **certificateArn** *(string) --* 
                The CA certificate ARN.
              - **certificateId** *(string) --* 
                The CA certificate ID.
              - **status** *(string) --* 
                The status of a CA certificate.
              - **certificatePem** *(string) --* 
                The CA certificate data, in PEM format.
              - **ownedBy** *(string) --* 
                The owner of the CA certificate.
              - **creationDate** *(datetime) --* 
                The date the CA certificate was created.
              - **autoRegistrationStatus** *(string) --* 
                Whether the CA certificate configured for auto registration of device certificates. Valid values are "ENABLE" and "DISABLE"
              - **lastModifiedDate** *(datetime) --* 
                The date the CA certificate was last modified.
              - **customerVersion** *(integer) --* 
                The customer version of the CA certificate.
              - **generationId** *(string) --* 
                The generation ID of the CA certificate.
              - **validity** *(dict) --* 
                When the CA certificate is valid.
                - **notBefore** *(datetime) --* 
                  The certificate is not valid before this date.
                - **notAfter** *(datetime) --* 
                  The certificate is not valid after this date.
            - **registrationConfig** *(dict) --* 
              Information about the registration configuration.
              - **templateBody** *(string) --* 
                The template body.
              - **roleArn** *(string) --* 
                The ARN of the role.
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The CA certificate identifier.
        :rtype: dict
        :returns:
        """
        pass

    def describe_certificate(self, certificateId: str) -> Dict:
        """
        Gets information about the specified certificate.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeCertificate>`_
        
        **Request Syntax**
        ::
          response = client.describe_certificate(
              certificateId='string'
          )
        
        **Response Syntax**
        ::
            {
                'certificateDescription': {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'caCertificateId': 'string',
                    'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                    'certificatePem': 'string',
                    'ownedBy': 'string',
                    'previousOwnedBy': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'customerVersion': 123,
                    'transferData': {
                        'transferMessage': 'string',
                        'rejectReason': 'string',
                        'transferDate': datetime(2015, 1, 1),
                        'acceptDate': datetime(2015, 1, 1),
                        'rejectDate': datetime(2015, 1, 1)
                    },
                    'generationId': 'string',
                    'validity': {
                        'notBefore': datetime(2015, 1, 1),
                        'notAfter': datetime(2015, 1, 1)
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the DescribeCertificate operation.
            - **certificateDescription** *(dict) --* 
              The description of the certificate.
              - **certificateArn** *(string) --* 
                The ARN of the certificate.
              - **certificateId** *(string) --* 
                The ID of the certificate.
              - **caCertificateId** *(string) --* 
                The certificate ID of the CA certificate used to sign this certificate.
              - **status** *(string) --* 
                The status of the certificate.
              - **certificatePem** *(string) --* 
                The certificate data, in PEM format.
              - **ownedBy** *(string) --* 
                The ID of the AWS account that owns the certificate.
              - **previousOwnedBy** *(string) --* 
                The ID of the AWS account of the previous owner of the certificate.
              - **creationDate** *(datetime) --* 
                The date and time the certificate was created.
              - **lastModifiedDate** *(datetime) --* 
                The date and time the certificate was last modified.
              - **customerVersion** *(integer) --* 
                The customer version of the certificate.
              - **transferData** *(dict) --* 
                The transfer data.
                - **transferMessage** *(string) --* 
                  The transfer message.
                - **rejectReason** *(string) --* 
                  The reason why the transfer was rejected.
                - **transferDate** *(datetime) --* 
                  The date the transfer took place.
                - **acceptDate** *(datetime) --* 
                  The date the transfer was accepted.
                - **rejectDate** *(datetime) --* 
                  The date the transfer was rejected.
              - **generationId** *(string) --* 
                The generation ID of the certificate.
              - **validity** *(dict) --* 
                When the certificate is valid.
                - **notBefore** *(datetime) --* 
                  The certificate is not valid before this date.
                - **notAfter** *(datetime) --* 
                  The certificate is not valid after this date.
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        :rtype: dict
        :returns:
        """
        pass

    def describe_default_authorizer(self) -> Dict:
        """
        Describes the default authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeDefaultAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.describe_default_authorizer()
        
        **Response Syntax**
        ::
            {
                'authorizerDescription': {
                    'authorizerName': 'string',
                    'authorizerArn': 'string',
                    'authorizerFunctionArn': 'string',
                    'tokenKeyName': 'string',
                    'tokenSigningPublicKeys': {
                        'string': 'string'
                    },
                    'status': 'ACTIVE'|'INACTIVE',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **authorizerDescription** *(dict) --* 
              The default authorizer's description.
              - **authorizerName** *(string) --* 
                The authorizer name.
              - **authorizerArn** *(string) --* 
                The authorizer ARN.
              - **authorizerFunctionArn** *(string) --* 
                The authorizer's Lambda function ARN.
              - **tokenKeyName** *(string) --* 
                The key used to extract the token from the HTTP headers.
              - **tokenSigningPublicKeys** *(dict) --* 
                The public keys used to validate the token signature returned by your custom authentication service.
                - *(string) --* 
                  - *(string) --* 
              - **status** *(string) --* 
                The status of the authorizer.
              - **creationDate** *(datetime) --* 
                The UNIX timestamp of when the authorizer was created.
              - **lastModifiedDate** *(datetime) --* 
                The UNIX timestamp of when the authorizer was last updated.
        :rtype: dict
        :returns:
        """
        pass

    def describe_endpoint(self, endpointType: str = None) -> Dict:
        """
        Returns a unique endpoint specific to the AWS account making the call.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeEndpoint>`_
        
        **Request Syntax**
        ::
          response = client.describe_endpoint(
              endpointType='string'
          )
        
        **Response Syntax**
        ::
            {
                'endpointAddress': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the DescribeEndpoint operation.
            - **endpointAddress** *(string) --* 
              The endpoint. The format of the endpoint is as follows: *identifier* .iot.*region* .amazonaws.com.
        :type endpointType: string
        :param endpointType:
          The endpoint type. Valid endpoint types include:
          * ``iot:Data`` - Returns a VeriSign signed data endpoint.
          * ``iot:Data-ATS`` - Returns an ATS signed data endpoint.
          * ``iot:CredentialProvider`` - Returns an AWS IoT credentials provider API endpoint.
          * ``iot:Jobs`` - Returns an AWS IoT device management Jobs API endpoint.
        :rtype: dict
        :returns:
        """
        pass

    def describe_event_configurations(self) -> Dict:
        """
        Describes event configurations.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeEventConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.describe_event_configurations()
        
        **Response Syntax**
        ::
            {
                'eventConfigurations': {
                    'string': {
                        'Enabled': True|False
                    }
                },
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **eventConfigurations** *(dict) --* 
              The event configurations.
              - *(string) --* 
                - *(dict) --* 
                  Configuration.
                  - **Enabled** *(boolean) --* 
                    True to enable the configuration.
            - **creationDate** *(datetime) --* 
              The creation date of the event configuration.
            - **lastModifiedDate** *(datetime) --* 
              The date the event configurations were last modified.
        :rtype: dict
        :returns:
        """
        pass

    def describe_index(self, indexName: str) -> Dict:
        """
        Describes a search index.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeIndex>`_
        
        **Request Syntax**
        ::
          response = client.describe_index(
              indexName='string'
          )
        
        **Response Syntax**
        ::
            {
                'indexName': 'string',
                'indexStatus': 'ACTIVE'|'BUILDING'|'REBUILDING',
                'schema': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **indexName** *(string) --* 
              The index name.
            - **indexStatus** *(string) --* 
              The index status.
            - **schema** *(string) --* 
              Contains a value that specifies the type of indexing performed. Valid values are:
              * REGISTRY – Your thing index will contain only registry data. 
              * REGISTRY_AND_SHADOW - Your thing index will contain registry data and shadow data. 
              * REGISTRY_AND_CONNECTIVITY_STATUS - Your thing index will contain registry data and thing connectivity status data. 
              * REGISTRY_AND_SHADOW_AND_CONNECTIVITY_STATUS - Your thing index will contain registry data, shadow data, and thing connectivity status data. 
        :type indexName: string
        :param indexName: **[REQUIRED]**
          The index name.
        :rtype: dict
        :returns:
        """
        pass

    def describe_job(self, jobId: str) -> Dict:
        """
        Describes a job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_job(
              jobId='string'
          )
        
        **Response Syntax**
        ::
            {
                'documentSource': 'string',
                'job': {
                    'jobArn': 'string',
                    'jobId': 'string',
                    'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
                    'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
                    'forceCanceled': True|False,
                    'reasonCode': 'string',
                    'comment': 'string',
                    'targets': [
                        'string',
                    ],
                    'description': 'string',
                    'presignedUrlConfig': {
                        'roleArn': 'string',
                        'expiresInSec': 123
                    },
                    'jobExecutionsRolloutConfig': {
                        'maximumPerMinute': 123,
                        'exponentialRate': {
                            'baseRatePerMinute': 123,
                            'incrementFactor': 123.0,
                            'rateIncreaseCriteria': {
                                'numberOfNotifiedThings': 123,
                                'numberOfSucceededThings': 123
                            }
                        }
                    },
                    'abortConfig': {
                        'criteriaList': [
                            {
                                'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                                'action': 'CANCEL',
                                'thresholdPercentage': 123.0,
                                'minNumberOfExecutedThings': 123
                            },
                        ]
                    },
                    'createdAt': datetime(2015, 1, 1),
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'completedAt': datetime(2015, 1, 1),
                    'jobProcessDetails': {
                        'processingTargets': [
                            'string',
                        ],
                        'numberOfCanceledThings': 123,
                        'numberOfSucceededThings': 123,
                        'numberOfFailedThings': 123,
                        'numberOfRejectedThings': 123,
                        'numberOfQueuedThings': 123,
                        'numberOfInProgressThings': 123,
                        'numberOfRemovedThings': 123,
                        'numberOfTimedOutThings': 123
                    },
                    'timeoutConfig': {
                        'inProgressTimeoutInMinutes': 123
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **documentSource** *(string) --* 
              An S3 link to the job document.
            - **job** *(dict) --* 
              Information about the job.
              - **jobArn** *(string) --* 
                An ARN identifying the job with format "arn:aws:iot:region:account:job/jobId".
              - **jobId** *(string) --* 
                The unique identifier you assigned to this job when it was created.
              - **targetSelection** *(string) --* 
                Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a device when the thing representing the device is added to a target group, even after the job was completed by all things originally in the group. 
              - **status** *(string) --* 
                The status of the job, one of ``IN_PROGRESS`` , ``CANCELED`` , ``DELETION_IN_PROGRESS`` or ``COMPLETED`` . 
              - **forceCanceled** *(boolean) --* 
                Will be ``true`` if the job was canceled with the optional ``force`` parameter set to ``true`` .
              - **reasonCode** *(string) --* 
                If the job was updated, provides the reason code for the update.
              - **comment** *(string) --* 
                If the job was updated, describes the reason for the update.
              - **targets** *(list) --* 
                A list of IoT things and thing groups to which the job should be sent.
                - *(string) --* 
              - **description** *(string) --* 
                A short text description of the job.
              - **presignedUrlConfig** *(dict) --* 
                Configuration for pre-signed S3 URLs.
                - **roleArn** *(string) --* 
                  The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.
                - **expiresInSec** *(integer) --* 
                  How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.
              - **jobExecutionsRolloutConfig** *(dict) --* 
                Allows you to create a staged rollout of a job.
                - **maximumPerMinute** *(integer) --* 
                  The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.
                - **exponentialRate** *(dict) --* 
                  The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.
                  - **baseRatePerMinute** *(integer) --* 
                    The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
                  - **incrementFactor** *(float) --* 
                    The exponential factor to increase the rate of rollout for a job.
                  - **rateIncreaseCriteria** *(dict) --* 
                    The criteria to initiate the increase in rate of rollout for a job.
                    AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).
                    - **numberOfNotifiedThings** *(integer) --* 
                      The threshold for number of notified things that will initiate the increase in rate of rollout.
                    - **numberOfSucceededThings** *(integer) --* 
                      The threshold for number of succeeded things that will initiate the increase in rate of rollout.
              - **abortConfig** *(dict) --* 
                Configuration for criteria to abort the job.
                - **criteriaList** *(list) --* 
                  The list of abort criteria to define rules to abort the job.
                  - *(dict) --* 
                    Details of abort criteria to define rules to abort the job.
                    - **failureType** *(string) --* 
                      The type of job execution failure to define a rule to initiate a job abort.
                    - **action** *(string) --* 
                      The type of abort action to initiate a job abort.
                    - **thresholdPercentage** *(float) --* 
                      The threshold as a percentage of the total number of executed things that will initiate a job abort.
                      AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
                    - **minNumberOfExecutedThings** *(integer) --* 
                      Minimum number of executed things before evaluating an abort rule.
              - **createdAt** *(datetime) --* 
                The time, in seconds since the epoch, when the job was created.
              - **lastUpdatedAt** *(datetime) --* 
                The time, in seconds since the epoch, when the job was last updated.
              - **completedAt** *(datetime) --* 
                The time, in seconds since the epoch, when the job was completed.
              - **jobProcessDetails** *(dict) --* 
                Details about the job process.
                - **processingTargets** *(list) --* 
                  The target devices to which the job execution is being rolled out. This value will be null after the job execution has finished rolling out to all the target devices.
                  - *(string) --* 
                - **numberOfCanceledThings** *(integer) --* 
                  The number of things that cancelled the job.
                - **numberOfSucceededThings** *(integer) --* 
                  The number of things which successfully completed the job.
                - **numberOfFailedThings** *(integer) --* 
                  The number of things that failed executing the job.
                - **numberOfRejectedThings** *(integer) --* 
                  The number of things that rejected the job.
                - **numberOfQueuedThings** *(integer) --* 
                  The number of things that are awaiting execution of the job.
                - **numberOfInProgressThings** *(integer) --* 
                  The number of things currently executing the job.
                - **numberOfRemovedThings** *(integer) --* 
                  The number of things that are no longer scheduled to execute the job because they have been deleted or have been removed from the group that was a target of the job.
                - **numberOfTimedOutThings** *(integer) --* 
                  The number of things whose job execution status is ``TIMED_OUT`` .
              - **timeoutConfig** *(dict) --* 
                Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .
                - **inProgressTimeoutInMinutes** *(integer) --* 
                  Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can't be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal ``TIMED_OUT`` status.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The unique identifier you assigned to this job when it was created.
        :rtype: dict
        :returns:
        """
        pass

    def describe_job_execution(self, jobId: str, thingName: str, executionNumber: int = None) -> Dict:
        """
        Describes a job execution.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeJobExecution>`_
        
        **Request Syntax**
        ::
          response = client.describe_job_execution(
              jobId='string',
              thingName='string',
              executionNumber=123
          )
        
        **Response Syntax**
        ::
            {
                'execution': {
                    'jobId': 'string',
                    'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                    'forceCanceled': True|False,
                    'statusDetails': {
                        'detailsMap': {
                            'string': 'string'
                        }
                    },
                    'thingArn': 'string',
                    'queuedAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'executionNumber': 123,
                    'versionNumber': 123,
                    'approximateSecondsBeforeTimedOut': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **execution** *(dict) --* 
              Information about the job execution.
              - **jobId** *(string) --* 
                The unique identifier you assigned to the job when it was created.
              - **status** *(string) --* 
                The status of the job execution (IN_PROGRESS, QUEUED, FAILED, SUCCEEDED, TIMED_OUT, CANCELED, or REJECTED).
              - **forceCanceled** *(boolean) --* 
                Will be ``true`` if the job execution was canceled with the optional ``force`` parameter set to ``true`` .
              - **statusDetails** *(dict) --* 
                A collection of name/value pairs that describe the status of the job execution.
                - **detailsMap** *(dict) --* 
                  The job execution status.
                  - *(string) --* 
                    - *(string) --* 
              - **thingArn** *(string) --* 
                The ARN of the thing on which the job execution is running.
              - **queuedAt** *(datetime) --* 
                The time, in seconds since the epoch, when the job execution was queued.
              - **startedAt** *(datetime) --* 
                The time, in seconds since the epoch, when the job execution started.
              - **lastUpdatedAt** *(datetime) --* 
                The time, in seconds since the epoch, when the job execution was last updated.
              - **executionNumber** *(integer) --* 
                A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used in commands which return or update job execution information. 
              - **versionNumber** *(integer) --* 
                The version of the job execution. Job execution versions are incremented each time they are updated by a device.
              - **approximateSecondsBeforeTimedOut** *(integer) --* 
                The estimated number of seconds that remain before the job execution status will be changed to ``TIMED_OUT`` . The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The actual job execution timeout can occur up to 60 seconds later than the estimated duration. This value will not be included if the job execution has reached a terminal status.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The unique identifier you assigned to this job when it was created.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing on which the job execution is running.
        :type executionNumber: integer
        :param executionNumber:
          A string (consisting of the digits \"0\" through \"9\" which is used to specify a particular job execution on a particular device.
        :rtype: dict
        :returns:
        """
        pass

    def describe_role_alias(self, roleAlias: str) -> Dict:
        """
        Describes a role alias.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeRoleAlias>`_
        
        **Request Syntax**
        ::
          response = client.describe_role_alias(
              roleAlias='string'
          )
        
        **Response Syntax**
        ::
            {
                'roleAliasDescription': {
                    'roleAlias': 'string',
                    'roleAliasArn': 'string',
                    'roleArn': 'string',
                    'owner': 'string',
                    'credentialDurationSeconds': 123,
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **roleAliasDescription** *(dict) --* 
              The role alias description.
              - **roleAlias** *(string) --* 
                The role alias.
              - **roleAliasArn** *(string) --* 
                The ARN of the role alias.
              - **roleArn** *(string) --* 
                The role ARN.
              - **owner** *(string) --* 
                The role alias owner.
              - **credentialDurationSeconds** *(integer) --* 
                The number of seconds for which the credential is valid.
              - **creationDate** *(datetime) --* 
                The UNIX timestamp of when the role alias was created.
              - **lastModifiedDate** *(datetime) --* 
                The UNIX timestamp of when the role alias was last modified.
        :type roleAlias: string
        :param roleAlias: **[REQUIRED]**
          The role alias to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_scheduled_audit(self, scheduledAuditName: str) -> Dict:
        """
        Gets information about a scheduled audit.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeScheduledAudit>`_
        
        **Request Syntax**
        ::
          response = client.describe_scheduled_audit(
              scheduledAuditName='string'
          )
        
        **Response Syntax**
        ::
            {
                'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
                'dayOfMonth': 'string',
                'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
                'targetCheckNames': [
                    'string',
                ],
                'scheduledAuditName': 'string',
                'scheduledAuditArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **frequency** *(string) --* 
              How often the scheduled audit takes place. One of "DAILY", "WEEKLY", "BIWEEKLY" or "MONTHLY". The actual start time of each audit is determined by the system.
            - **dayOfMonth** *(string) --* 
              The day of the month on which the scheduled audit takes place. Will be "1" through "31" or "LAST". If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
            - **dayOfWeek** *(string) --* 
              The day of the week on which the scheduled audit takes place. One of "SUN", "MON", "TUE", "WED", "THU", "FRI" or "SAT".
            - **targetCheckNames** *(list) --* 
              Which checks are performed during the scheduled audit. (Note that checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
              - *(string) --* 
                An audit check name. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
            - **scheduledAuditName** *(string) --* 
              The name of the scheduled audit.
            - **scheduledAuditArn** *(string) --* 
              The ARN of the scheduled audit.
        :type scheduledAuditName: string
        :param scheduledAuditName: **[REQUIRED]**
          The name of the scheduled audit whose information you want to get.
        :rtype: dict
        :returns:
        """
        pass

    def describe_security_profile(self, securityProfileName: str) -> Dict:
        """
        Gets information about a Device Defender security profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeSecurityProfile>`_
        
        **Request Syntax**
        ::
          response = client.describe_security_profile(
              securityProfileName='string'
          )
        
        **Response Syntax**
        ::
            {
                'securityProfileName': 'string',
                'securityProfileArn': 'string',
                'securityProfileDescription': 'string',
                'behaviors': [
                    {
                        'name': 'string',
                        'metric': 'string',
                        'criteria': {
                            'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                            'value': {
                                'count': 123,
                                'cidrs': [
                                    'string',
                                ],
                                'ports': [
                                    123,
                                ]
                            },
                            'durationSeconds': 123,
                            'consecutiveDatapointsToAlarm': 123,
                            'consecutiveDatapointsToClear': 123,
                            'statisticalThreshold': {
                                'statistic': 'string'
                            }
                        }
                    },
                ],
                'alertTargets': {
                    'string': {
                        'alertTargetArn': 'string',
                        'roleArn': 'string'
                    }
                },
                'additionalMetricsToRetain': [
                    'string',
                ],
                'version': 123,
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileName** *(string) --* 
              The name of the security profile.
            - **securityProfileArn** *(string) --* 
              The ARN of the security profile.
            - **securityProfileDescription** *(string) --* 
              A description of the security profile (associated with the security profile when it was created or updated).
            - **behaviors** *(list) --* 
              Specifies the behaviors that, when violated by a device (thing), cause an alert.
              - *(dict) --* 
                A Device Defender security profile behavior.
                - **name** *(string) --* 
                  The name you have given to the behavior.
                - **metric** *(string) --* 
                  What is measured by the behavior.
                - **criteria** *(dict) --* 
                  The criteria that determine if a device is behaving normally in regard to the ``metric`` .
                  - **comparisonOperator** *(string) --* 
                    The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
                  - **value** *(dict) --* 
                    The value to be compared with the ``metric`` .
                    - **count** *(integer) --* 
                      If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                    - **cidrs** *(list) --* 
                      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                      - *(string) --* 
                    - **ports** *(list) --* 
                      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                      - *(integer) --* 
                  - **durationSeconds** *(integer) --* 
                    Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
                  - **consecutiveDatapointsToAlarm** *(integer) --* 
                    If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
                  - **consecutiveDatapointsToClear** *(integer) --* 
                    If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
                  - **statisticalThreshold** *(dict) --* 
                    A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                    - **statistic** *(string) --* 
                      The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
            - **alertTargets** *(dict) --* 
              Where the alerts are sent. (Alerts are always sent to the console.)
              - *(string) --* 
                The type of alert target: one of "SNS".
                - *(dict) --* 
                  A structure containing the alert target ARN and the role ARN.
                  - **alertTargetArn** *(string) --* 
                    The ARN of the notification target to which alerts are sent.
                  - **roleArn** *(string) --* 
                    The ARN of the role that grants permission to send alerts to the notification target.
            - **additionalMetricsToRetain** *(list) --* 
              A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's ``behaviors`` but it is also retained for any metric specified here.
              - *(string) --* 
            - **version** *(integer) --* 
              The version of the security profile. A new version is generated whenever the security profile is updated.
            - **creationDate** *(datetime) --* 
              The time the security profile was created.
            - **lastModifiedDate** *(datetime) --* 
              The time the security profile was last modified.
        :type securityProfileName: string
        :param securityProfileName: **[REQUIRED]**
          The name of the security profile whose information you want to get.
        :rtype: dict
        :returns:
        """
        pass

    def describe_stream(self, streamId: str) -> Dict:
        """
        Gets information about a stream.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeStream>`_
        
        **Request Syntax**
        ::
          response = client.describe_stream(
              streamId='string'
          )
        
        **Response Syntax**
        ::
            {
                'streamInfo': {
                    'streamId': 'string',
                    'streamArn': 'string',
                    'streamVersion': 123,
                    'description': 'string',
                    'files': [
                        {
                            'fileId': 123,
                            's3Location': {
                                'bucket': 'string',
                                'key': 'string',
                                'version': 'string'
                            }
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'roleArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **streamInfo** *(dict) --* 
              Information about the stream.
              - **streamId** *(string) --* 
                The stream ID.
              - **streamArn** *(string) --* 
                The stream ARN.
              - **streamVersion** *(integer) --* 
                The stream version.
              - **description** *(string) --* 
                The description of the stream.
              - **files** *(list) --* 
                The files to stream.
                - *(dict) --* 
                  Represents a file to stream.
                  - **fileId** *(integer) --* 
                    The file ID.
                  - **s3Location** *(dict) --* 
                    The location of the file in S3.
                    - **bucket** *(string) --* 
                      The S3 bucket.
                    - **key** *(string) --* 
                      The S3 key.
                    - **version** *(string) --* 
                      The S3 bucket version.
              - **createdAt** *(datetime) --* 
                The date when the stream was created.
              - **lastUpdatedAt** *(datetime) --* 
                The date when the stream was last updated.
              - **roleArn** *(string) --* 
                An IAM role AWS IoT assumes to access your S3 files.
        :type streamId: string
        :param streamId: **[REQUIRED]**
          The stream ID.
        :rtype: dict
        :returns:
        """
        pass

    def describe_thing(self, thingName: str) -> Dict:
        """
        Gets information about the specified thing.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeThing>`_
        
        **Request Syntax**
        ::
          response = client.describe_thing(
              thingName='string'
          )
        
        **Response Syntax**
        ::
            {
                'defaultClientId': 'string',
                'thingName': 'string',
                'thingId': 'string',
                'thingArn': 'string',
                'thingTypeName': 'string',
                'attributes': {
                    'string': 'string'
                },
                'version': 123,
                'billingGroupName': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the DescribeThing operation.
            - **defaultClientId** *(string) --* 
              The default client ID.
            - **thingName** *(string) --* 
              The name of the thing.
            - **thingId** *(string) --* 
              The ID of the thing to describe.
            - **thingArn** *(string) --* 
              The ARN of the thing to describe.
            - **thingTypeName** *(string) --* 
              The thing type name.
            - **attributes** *(dict) --* 
              The thing attributes.
              - *(string) --* 
                - *(string) --* 
            - **version** *(integer) --* 
              The current version of the thing record in the registry.
              .. note::
                To avoid unintentional changes to the information in the registry, you can pass the version information in the ``expectedVersion`` parameter of the ``UpdateThing`` and ``DeleteThing`` calls.
            - **billingGroupName** *(string) --* 
              The name of the billing group the thing belongs to.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing.
        :rtype: dict
        :returns:
        """
        pass

    def describe_thing_group(self, thingGroupName: str) -> Dict:
        """
        Describe a thing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.describe_thing_group(
              thingGroupName='string'
          )
        
        **Response Syntax**
        ::
            {
                'thingGroupName': 'string',
                'thingGroupId': 'string',
                'thingGroupArn': 'string',
                'version': 123,
                'thingGroupProperties': {
                    'thingGroupDescription': 'string',
                    'attributePayload': {
                        'attributes': {
                            'string': 'string'
                        },
                        'merge': True|False
                    }
                },
                'thingGroupMetadata': {
                    'parentGroupName': 'string',
                    'rootToParentThingGroups': [
                        {
                            'groupName': 'string',
                            'groupArn': 'string'
                        },
                    ],
                    'creationDate': datetime(2015, 1, 1)
                },
                'indexName': 'string',
                'queryString': 'string',
                'queryVersion': 'string',
                'status': 'ACTIVE'|'BUILDING'|'REBUILDING'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **thingGroupName** *(string) --* 
              The name of the thing group.
            - **thingGroupId** *(string) --* 
              The thing group ID.
            - **thingGroupArn** *(string) --* 
              The thing group ARN.
            - **version** *(integer) --* 
              The version of the thing group.
            - **thingGroupProperties** *(dict) --* 
              The thing group properties.
              - **thingGroupDescription** *(string) --* 
                The thing group description.
              - **attributePayload** *(dict) --* 
                The thing group attributes in JSON format.
                - **attributes** *(dict) --* 
                  A JSON string containing up to three key-value pair in JSON format. For example:
                   ``{\"attributes\":{\"string1\":\"string2\"}}``  
                  - *(string) --* 
                    - *(string) --* 
                - **merge** *(boolean) --* 
                  Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.
                  To remove an attribute, call ``UpdateThing`` with an empty attribute value.
                  .. note::
                    The ``merge`` attribute is only valid when calling ``UpdateThing`` .
            - **thingGroupMetadata** *(dict) --* 
              Thing group metadata.
              - **parentGroupName** *(string) --* 
                The parent thing group name.
              - **rootToParentThingGroups** *(list) --* 
                The root parent thing group.
                - *(dict) --* 
                  The name and ARN of a group.
                  - **groupName** *(string) --* 
                    The group name.
                  - **groupArn** *(string) --* 
                    The group ARN.
              - **creationDate** *(datetime) --* 
                The UNIX timestamp of when the thing group was created.
            - **indexName** *(string) --* 
              The dynamic thing group index name.
            - **queryString** *(string) --* 
              The dynamic thing group search query string.
            - **queryVersion** *(string) --* 
              The dynamic thing group query version.
            - **status** *(string) --* 
              The dynamic thing group status.
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The name of the thing group.
        :rtype: dict
        :returns:
        """
        pass

    def describe_thing_registration_task(self, taskId: str) -> Dict:
        """
        Describes a bulk thing provisioning task.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeThingRegistrationTask>`_
        
        **Request Syntax**
        ::
          response = client.describe_thing_registration_task(
              taskId='string'
          )
        
        **Response Syntax**
        ::
            {
                'taskId': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1),
                'templateBody': 'string',
                'inputFileBucket': 'string',
                'inputFileKey': 'string',
                'roleArn': 'string',
                'status': 'InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling',
                'message': 'string',
                'successCount': 123,
                'failureCount': 123,
                'percentageProgress': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskId** *(string) --* 
              The task ID.
            - **creationDate** *(datetime) --* 
              The task creation date.
            - **lastModifiedDate** *(datetime) --* 
              The date when the task was last modified.
            - **templateBody** *(string) --* 
              The task's template.
            - **inputFileBucket** *(string) --* 
              The S3 bucket that contains the input file.
            - **inputFileKey** *(string) --* 
              The input file key.
            - **roleArn** *(string) --* 
              The role ARN that grants access to the input file bucket.
            - **status** *(string) --* 
              The status of the bulk thing provisioning task.
            - **message** *(string) --* 
              The message.
            - **successCount** *(integer) --* 
              The number of things successfully provisioned.
            - **failureCount** *(integer) --* 
              The number of things that failed to be provisioned.
            - **percentageProgress** *(integer) --* 
              The progress of the bulk provisioning task expressed as a percentage.
        :type taskId: string
        :param taskId: **[REQUIRED]**
          The task ID.
        :rtype: dict
        :returns:
        """
        pass

    def describe_thing_type(self, thingTypeName: str) -> Dict:
        """
        Gets information about the specified thing type.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeThingType>`_
        
        **Request Syntax**
        ::
          response = client.describe_thing_type(
              thingTypeName='string'
          )
        
        **Response Syntax**
        ::
            {
                'thingTypeName': 'string',
                'thingTypeId': 'string',
                'thingTypeArn': 'string',
                'thingTypeProperties': {
                    'thingTypeDescription': 'string',
                    'searchableAttributes': [
                        'string',
                    ]
                },
                'thingTypeMetadata': {
                    'deprecated': True|False,
                    'deprecationDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the DescribeThingType operation.
            - **thingTypeName** *(string) --* 
              The name of the thing type.
            - **thingTypeId** *(string) --* 
              The thing type ID.
            - **thingTypeArn** *(string) --* 
              The thing type ARN.
            - **thingTypeProperties** *(dict) --* 
              The ThingTypeProperties contains information about the thing type including description, and a list of searchable thing attribute names.
              - **thingTypeDescription** *(string) --* 
                The description of the thing type.
              - **searchableAttributes** *(list) --* 
                A list of searchable thing attribute names.
                - *(string) --* 
            - **thingTypeMetadata** *(dict) --* 
              The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.
              - **deprecated** *(boolean) --* 
                Whether the thing type is deprecated. If **true** , no new things could be associated with this type.
              - **deprecationDate** *(datetime) --* 
                The date and time when the thing type was deprecated.
              - **creationDate** *(datetime) --* 
                The date and time when the thing type was created.
        :type thingTypeName: string
        :param thingTypeName: **[REQUIRED]**
          The name of the thing type.
        :rtype: dict
        :returns:
        """
        pass

    def detach_policy(self, policyName: str, target: str):
        """
        Detaches a policy from the specified target.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DetachPolicy>`_
        
        **Request Syntax**
        ::
          response = client.detach_policy(
              policyName='string',
              target='string'
          )
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy to detach.
        :type target: string
        :param target: **[REQUIRED]**
          The target from which the policy will be detached.
        :returns: None
        """
        pass

    def detach_principal_policy(self, policyName: str, principal: str):
        """
        Removes the specified policy from the specified certificate.
         **Note:** This API is deprecated. Please use  DetachPolicy instead.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DetachPrincipalPolicy>`_
        
        **Request Syntax**
        ::
          response = client.detach_principal_policy(
              policyName='string',
              principal='string'
          )
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The name of the policy to detach.
        :type principal: string
        :param principal: **[REQUIRED]**
          The principal.
          If the principal is a certificate, specify the certificate ARN. If the principal is an Amazon Cognito identity, specify the identity ID.
        :returns: None
        """
        pass

    def detach_security_profile(self, securityProfileName: str, securityProfileTargetArn: str) -> Dict:
        """
        Disassociates a Device Defender security profile from a thing group or from this account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DetachSecurityProfile>`_
        
        **Request Syntax**
        ::
          response = client.detach_security_profile(
              securityProfileName='string',
              securityProfileTargetArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type securityProfileName: string
        :param securityProfileName: **[REQUIRED]**
          The security profile that is detached.
        :type securityProfileTargetArn: string
        :param securityProfileTargetArn: **[REQUIRED]**
          The ARN of the thing group from which the security profile is detached.
        :rtype: dict
        :returns:
        """
        pass

    def detach_thing_principal(self, thingName: str, principal: str) -> Dict:
        """
        Detaches the specified principal from the specified thing. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities.
        .. note::
          This call is asynchronous. It might take several seconds for the detachment to propagate.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DetachThingPrincipal>`_
        
        **Request Syntax**
        ::
          response = client.detach_thing_principal(
              thingName='string',
              principal='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output from the DetachThingPrincipal operation.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing.
        :type principal: string
        :param principal: **[REQUIRED]**
          If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.
        :rtype: dict
        :returns:
        """
        pass

    def disable_topic_rule(self, ruleName: str):
        """
        Disables the rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DisableTopicRule>`_
        
        **Request Syntax**
        ::
          response = client.disable_topic_rule(
              ruleName='string'
          )
        :type ruleName: string
        :param ruleName: **[REQUIRED]**
          The name of the rule to disable.
        :returns: None
        """
        pass

    def enable_topic_rule(self, ruleName: str):
        """
        Enables the rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/EnableTopicRule>`_
        
        **Request Syntax**
        ::
          response = client.enable_topic_rule(
              ruleName='string'
          )
        :type ruleName: string
        :param ruleName: **[REQUIRED]**
          The name of the topic rule to enable.
        :returns: None
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

    def get_effective_policies(self, principal: str = None, cognitoIdentityPoolId: str = None, thingName: str = None) -> Dict:
        """
        Gets a list of the policies that have an effect on the authorization behavior of the specified device when it connects to the AWS IoT device gateway.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetEffectivePolicies>`_
        
        **Request Syntax**
        ::
          response = client.get_effective_policies(
              principal='string',
              cognitoIdentityPoolId='string',
              thingName='string'
          )
        
        **Response Syntax**
        ::
            {
                'effectivePolicies': [
                    {
                        'policyName': 'string',
                        'policyArn': 'string',
                        'policyDocument': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **effectivePolicies** *(list) --* 
              The effective policies.
              - *(dict) --* 
                The policy that has the effect on the authorization results.
                - **policyName** *(string) --* 
                  The policy name.
                - **policyArn** *(string) --* 
                  The policy ARN.
                - **policyDocument** *(string) --* 
                  The IAM policy document.
        :type principal: string
        :param principal:
          The principal.
        :type cognitoIdentityPoolId: string
        :param cognitoIdentityPoolId:
          The Cognito identity pool ID.
        :type thingName: string
        :param thingName:
          The thing name.
        :rtype: dict
        :returns:
        """
        pass

    def get_indexing_configuration(self) -> Dict:
        """
        Gets the search configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetIndexingConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_indexing_configuration()
        
        **Response Syntax**
        ::
            {
                'thingIndexingConfiguration': {
                    'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW',
                    'thingConnectivityIndexingMode': 'OFF'|'STATUS'
                },
                'thingGroupIndexingConfiguration': {
                    'thingGroupIndexingMode': 'OFF'|'ON'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **thingIndexingConfiguration** *(dict) --* 
              Thing indexing configuration.
              - **thingIndexingMode** *(string) --* 
                Thing indexing mode. Valid values are:
                * REGISTRY – Your thing index will contain only registry data. 
                * REGISTRY_AND_SHADOW - Your thing index will contain registry and shadow data. 
                * OFF - Thing indexing is disabled. 
              - **thingConnectivityIndexingMode** *(string) --* 
                Thing connectivity indexing mode. Valid values are: 
                * STATUS – Your thing index will contain connectivity status. In order to enable thing connectivity indexing, thingIndexMode must not be set to OFF. 
                * OFF - Thing connectivity status indexing is disabled. 
            - **thingGroupIndexingConfiguration** *(dict) --* 
              The index configuration.
              - **thingGroupIndexingMode** *(string) --* 
                Thing group indexing mode.
        :rtype: dict
        :returns:
        """
        pass

    def get_job_document(self, jobId: str) -> Dict:
        """
        Gets a job document.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetJobDocument>`_
        
        **Request Syntax**
        ::
          response = client.get_job_document(
              jobId='string'
          )
        
        **Response Syntax**
        ::
            {
                'document': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **document** *(string) --* 
              The job document content.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The unique identifier you assigned to this job when it was created.
        :rtype: dict
        :returns:
        """
        pass

    def get_logging_options(self) -> Dict:
        """
        Gets the logging options.
        NOTE: use of this command is not recommended. Use ``GetV2LoggingOptions`` instead.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetLoggingOptions>`_
        
        **Request Syntax**
        ::
          response = client.get_logging_options()
        
        **Response Syntax**
        ::
            {
                'roleArn': 'string',
                'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the GetLoggingOptions operation.
            - **roleArn** *(string) --* 
              The ARN of the IAM role that grants access.
            - **logLevel** *(string) --* 
              The logging level.
        :rtype: dict
        :returns:
        """
        pass

    def get_ota_update(self, otaUpdateId: str) -> Dict:
        """
        Gets an OTA update.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetOTAUpdate>`_
        
        **Request Syntax**
        ::
          response = client.get_ota_update(
              otaUpdateId='string'
          )
        
        **Response Syntax**
        ::
            {
                'otaUpdateInfo': {
                    'otaUpdateId': 'string',
                    'otaUpdateArn': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'description': 'string',
                    'targets': [
                        'string',
                    ],
                    'awsJobExecutionsRolloutConfig': {
                        'maximumPerMinute': 123
                    },
                    'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
                    'otaUpdateFiles': [
                        {
                            'fileName': 'string',
                            'fileVersion': 'string',
                            'fileLocation': {
                                'stream': {
                                    'streamId': 'string',
                                    'fileId': 123
                                },
                                's3Location': {
                                    'bucket': 'string',
                                    'key': 'string',
                                    'version': 'string'
                                }
                            },
                            'codeSigning': {
                                'awsSignerJobId': 'string',
                                'startSigningJobParameter': {
                                    'signingProfileParameter': {
                                        'certificateArn': 'string',
                                        'platform': 'string',
                                        'certificatePathOnDevice': 'string'
                                    },
                                    'signingProfileName': 'string',
                                    'destination': {
                                        's3Destination': {
                                            'bucket': 'string',
                                            'prefix': 'string'
                                        }
                                    }
                                },
                                'customCodeSigning': {
                                    'signature': {
                                        'inlineDocument': b'bytes'
                                    },
                                    'certificateChain': {
                                        'certificateName': 'string',
                                        'inlineDocument': 'string'
                                    },
                                    'hashAlgorithm': 'string',
                                    'signatureAlgorithm': 'string'
                                }
                            },
                            'attributes': {
                                'string': 'string'
                            }
                        },
                    ],
                    'otaUpdateStatus': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED',
                    'awsIotJobId': 'string',
                    'awsIotJobArn': 'string',
                    'errorInfo': {
                        'code': 'string',
                        'message': 'string'
                    },
                    'additionalParameters': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **otaUpdateInfo** *(dict) --* 
              The OTA update info.
              - **otaUpdateId** *(string) --* 
                The OTA update ID.
              - **otaUpdateArn** *(string) --* 
                The OTA update ARN.
              - **creationDate** *(datetime) --* 
                The date when the OTA update was created.
              - **lastModifiedDate** *(datetime) --* 
                The date when the OTA update was last updated.
              - **description** *(string) --* 
                A description of the OTA update.
              - **targets** *(list) --* 
                The targets of the OTA update.
                - *(string) --* 
              - **awsJobExecutionsRolloutConfig** *(dict) --* 
                Configuration for the rollout of OTA updates.
                - **maximumPerMinute** *(integer) --* 
                  The maximum number of OTA update job executions started per minute.
              - **targetSelection** *(string) --* 
                Specifies whether the OTA update will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the OTA update (SNAPSHOT). If continuous, the OTA update may also be run on a thing when a change is detected in a target. For example, an OTA update will run on a thing when the thing is added to a target group, even after the OTA update was completed by all things originally in the group. 
              - **otaUpdateFiles** *(list) --* 
                A list of files associated with the OTA update.
                - *(dict) --* 
                  Describes a file to be associated with an OTA update.
                  - **fileName** *(string) --* 
                    The name of the file.
                  - **fileVersion** *(string) --* 
                    The file version.
                  - **fileLocation** *(dict) --* 
                    The location of the updated firmware.
                    - **stream** *(dict) --* 
                      The stream that contains the OTA update.
                      - **streamId** *(string) --* 
                        The stream ID.
                      - **fileId** *(integer) --* 
                        The ID of a file associated with a stream.
                    - **s3Location** *(dict) --* 
                      The location of the updated firmware in S3.
                      - **bucket** *(string) --* 
                        The S3 bucket.
                      - **key** *(string) --* 
                        The S3 key.
                      - **version** *(string) --* 
                        The S3 bucket version.
                  - **codeSigning** *(dict) --* 
                    The code signing method of the file.
                    - **awsSignerJobId** *(string) --* 
                      The ID of the AWSSignerJob which was created to sign the file.
                    - **startSigningJobParameter** *(dict) --* 
                      Describes the code-signing job.
                      - **signingProfileParameter** *(dict) --* 
                        Describes the code-signing profile.
                        - **certificateArn** *(string) --* 
                          Certificate ARN.
                        - **platform** *(string) --* 
                          The hardware platform of your device.
                        - **certificatePathOnDevice** *(string) --* 
                          The location of the code-signing certificate on your device.
                      - **signingProfileName** *(string) --* 
                        The code-signing profile name.
                      - **destination** *(dict) --* 
                        The location to write the code-signed file.
                        - **s3Destination** *(dict) --* 
                          Describes the location in S3 of the updated firmware.
                          - **bucket** *(string) --* 
                            The S3 bucket that contains the updated firmware.
                          - **prefix** *(string) --* 
                            The S3 prefix.
                    - **customCodeSigning** *(dict) --* 
                      A custom method for code signing a file.
                      - **signature** *(dict) --* 
                        The signature for the file.
                        - **inlineDocument** *(bytes) --* 
                          A base64 encoded binary representation of the code signing signature.
                      - **certificateChain** *(dict) --* 
                        The certificate chain.
                        - **certificateName** *(string) --* 
                          The name of the certificate.
                        - **inlineDocument** *(string) --* 
                          A base64 encoded binary representation of the code signing certificate chain.
                      - **hashAlgorithm** *(string) --* 
                        The hash algorithm used to code sign the file.
                      - **signatureAlgorithm** *(string) --* 
                        The signature algorithm used to code sign the file.
                  - **attributes** *(dict) --* 
                    A list of name/attribute pairs.
                    - *(string) --* 
                      - *(string) --* 
              - **otaUpdateStatus** *(string) --* 
                The status of the OTA update.
              - **awsIotJobId** *(string) --* 
                The AWS IoT job ID associated with the OTA update.
              - **awsIotJobArn** *(string) --* 
                The AWS IoT job ARN associated with the OTA update.
              - **errorInfo** *(dict) --* 
                Error information associated with the OTA update.
                - **code** *(string) --* 
                  The error code.
                - **message** *(string) --* 
                  The error message.
              - **additionalParameters** *(dict) --* 
                A collection of name/value pairs
                - *(string) --* 
                  - *(string) --* 
        :type otaUpdateId: string
        :param otaUpdateId: **[REQUIRED]**
          The OTA update ID.
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

    def get_policy(self, policyName: str) -> Dict:
        """
        Gets information about the specified policy with the policy document of the default version.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetPolicy>`_
        
        **Request Syntax**
        ::
          response = client.get_policy(
              policyName='string'
          )
        
        **Response Syntax**
        ::
            {
                'policyName': 'string',
                'policyArn': 'string',
                'policyDocument': 'string',
                'defaultVersionId': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1),
                'generationId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the GetPolicy operation.
            - **policyName** *(string) --* 
              The policy name.
            - **policyArn** *(string) --* 
              The policy ARN.
            - **policyDocument** *(string) --* 
              The JSON document that describes the policy.
            - **defaultVersionId** *(string) --* 
              The default policy version ID.
            - **creationDate** *(datetime) --* 
              The date the policy was created.
            - **lastModifiedDate** *(datetime) --* 
              The date the policy was last modified.
            - **generationId** *(string) --* 
              The generation ID of the policy.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The name of the policy.
        :rtype: dict
        :returns:
        """
        pass

    def get_policy_version(self, policyName: str, policyVersionId: str) -> Dict:
        """
        Gets information about the specified policy version.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetPolicyVersion>`_
        
        **Request Syntax**
        ::
          response = client.get_policy_version(
              policyName='string',
              policyVersionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'policyArn': 'string',
                'policyName': 'string',
                'policyDocument': 'string',
                'policyVersionId': 'string',
                'isDefaultVersion': True|False,
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1),
                'generationId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the GetPolicyVersion operation.
            - **policyArn** *(string) --* 
              The policy ARN.
            - **policyName** *(string) --* 
              The policy name.
            - **policyDocument** *(string) --* 
              The JSON document that describes the policy.
            - **policyVersionId** *(string) --* 
              The policy version ID.
            - **isDefaultVersion** *(boolean) --* 
              Specifies whether the policy version is the default.
            - **creationDate** *(datetime) --* 
              The date the policy version was created.
            - **lastModifiedDate** *(datetime) --* 
              The date the policy version was last modified.
            - **generationId** *(string) --* 
              The generation ID of the policy version.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The name of the policy.
        :type policyVersionId: string
        :param policyVersionId: **[REQUIRED]**
          The policy version ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_registration_code(self) -> Dict:
        """
        Gets a registration code used to register a CA certificate with AWS IoT.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetRegistrationCode>`_
        
        **Request Syntax**
        ::
          response = client.get_registration_code()
        
        **Response Syntax**
        ::
            {
                'registrationCode': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the GetRegistrationCode operation.
            - **registrationCode** *(string) --* 
              The CA certificate registration code.
        :rtype: dict
        :returns:
        """
        pass

    def get_topic_rule(self, ruleName: str) -> Dict:
        """
        Gets information about the rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetTopicRule>`_
        
        **Request Syntax**
        ::
          response = client.get_topic_rule(
              ruleName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ruleArn': 'string',
                'rule': {
                    'ruleName': 'string',
                    'sql': 'string',
                    'description': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'actions': [
                        {
                            'dynamoDB': {
                                'tableName': 'string',
                                'roleArn': 'string',
                                'operation': 'string',
                                'hashKeyField': 'string',
                                'hashKeyValue': 'string',
                                'hashKeyType': 'STRING'|'NUMBER',
                                'rangeKeyField': 'string',
                                'rangeKeyValue': 'string',
                                'rangeKeyType': 'STRING'|'NUMBER',
                                'payloadField': 'string'
                            },
                            'dynamoDBv2': {
                                'roleArn': 'string',
                                'putItem': {
                                    'tableName': 'string'
                                }
                            },
                            'lambda': {
                                'functionArn': 'string'
                            },
                            'sns': {
                                'targetArn': 'string',
                                'roleArn': 'string',
                                'messageFormat': 'RAW'|'JSON'
                            },
                            'sqs': {
                                'roleArn': 'string',
                                'queueUrl': 'string',
                                'useBase64': True|False
                            },
                            'kinesis': {
                                'roleArn': 'string',
                                'streamName': 'string',
                                'partitionKey': 'string'
                            },
                            'republish': {
                                'roleArn': 'string',
                                'topic': 'string'
                            },
                            's3': {
                                'roleArn': 'string',
                                'bucketName': 'string',
                                'key': 'string',
                                'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                            },
                            'firehose': {
                                'roleArn': 'string',
                                'deliveryStreamName': 'string',
                                'separator': 'string'
                            },
                            'cloudwatchMetric': {
                                'roleArn': 'string',
                                'metricNamespace': 'string',
                                'metricName': 'string',
                                'metricValue': 'string',
                                'metricUnit': 'string',
                                'metricTimestamp': 'string'
                            },
                            'cloudwatchAlarm': {
                                'roleArn': 'string',
                                'alarmName': 'string',
                                'stateReason': 'string',
                                'stateValue': 'string'
                            },
                            'elasticsearch': {
                                'roleArn': 'string',
                                'endpoint': 'string',
                                'index': 'string',
                                'type': 'string',
                                'id': 'string'
                            },
                            'salesforce': {
                                'token': 'string',
                                'url': 'string'
                            },
                            'iotAnalytics': {
                                'channelArn': 'string',
                                'channelName': 'string',
                                'roleArn': 'string'
                            },
                            'iotEvents': {
                                'inputName': 'string',
                                'messageId': 'string',
                                'roleArn': 'string'
                            },
                            'stepFunctions': {
                                'executionNamePrefix': 'string',
                                'stateMachineName': 'string',
                                'roleArn': 'string'
                            }
                        },
                    ],
                    'ruleDisabled': True|False,
                    'awsIotSqlVersion': 'string',
                    'errorAction': {
                        'dynamoDB': {
                            'tableName': 'string',
                            'roleArn': 'string',
                            'operation': 'string',
                            'hashKeyField': 'string',
                            'hashKeyValue': 'string',
                            'hashKeyType': 'STRING'|'NUMBER',
                            'rangeKeyField': 'string',
                            'rangeKeyValue': 'string',
                            'rangeKeyType': 'STRING'|'NUMBER',
                            'payloadField': 'string'
                        },
                        'dynamoDBv2': {
                            'roleArn': 'string',
                            'putItem': {
                                'tableName': 'string'
                            }
                        },
                        'lambda': {
                            'functionArn': 'string'
                        },
                        'sns': {
                            'targetArn': 'string',
                            'roleArn': 'string',
                            'messageFormat': 'RAW'|'JSON'
                        },
                        'sqs': {
                            'roleArn': 'string',
                            'queueUrl': 'string',
                            'useBase64': True|False
                        },
                        'kinesis': {
                            'roleArn': 'string',
                            'streamName': 'string',
                            'partitionKey': 'string'
                        },
                        'republish': {
                            'roleArn': 'string',
                            'topic': 'string'
                        },
                        's3': {
                            'roleArn': 'string',
                            'bucketName': 'string',
                            'key': 'string',
                            'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                        },
                        'firehose': {
                            'roleArn': 'string',
                            'deliveryStreamName': 'string',
                            'separator': 'string'
                        },
                        'cloudwatchMetric': {
                            'roleArn': 'string',
                            'metricNamespace': 'string',
                            'metricName': 'string',
                            'metricValue': 'string',
                            'metricUnit': 'string',
                            'metricTimestamp': 'string'
                        },
                        'cloudwatchAlarm': {
                            'roleArn': 'string',
                            'alarmName': 'string',
                            'stateReason': 'string',
                            'stateValue': 'string'
                        },
                        'elasticsearch': {
                            'roleArn': 'string',
                            'endpoint': 'string',
                            'index': 'string',
                            'type': 'string',
                            'id': 'string'
                        },
                        'salesforce': {
                            'token': 'string',
                            'url': 'string'
                        },
                        'iotAnalytics': {
                            'channelArn': 'string',
                            'channelName': 'string',
                            'roleArn': 'string'
                        },
                        'iotEvents': {
                            'inputName': 'string',
                            'messageId': 'string',
                            'roleArn': 'string'
                        },
                        'stepFunctions': {
                            'executionNamePrefix': 'string',
                            'stateMachineName': 'string',
                            'roleArn': 'string'
                        }
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the GetTopicRule operation.
            - **ruleArn** *(string) --* 
              The rule ARN.
            - **rule** *(dict) --* 
              The rule.
              - **ruleName** *(string) --* 
                The name of the rule.
              - **sql** *(string) --* 
                The SQL statement used to query the topic. When using a SQL query with multiple lines, be sure to escape the newline characters.
              - **description** *(string) --* 
                The description of the rule.
              - **createdAt** *(datetime) --* 
                The date and time the rule was created.
              - **actions** *(list) --* 
                The actions associated with the rule.
                - *(dict) --* 
                  Describes the actions associated with a rule.
                  - **dynamoDB** *(dict) --* 
                    Write to a DynamoDB table.
                    - **tableName** *(string) --* 
                      The name of the DynamoDB table.
                    - **roleArn** *(string) --* 
                      The ARN of the IAM role that grants access to the DynamoDB table.
                    - **operation** *(string) --* 
                      The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .
                    - **hashKeyField** *(string) --* 
                      The hash key name.
                    - **hashKeyValue** *(string) --* 
                      The hash key value.
                    - **hashKeyType** *(string) --* 
                      The hash key type. Valid values are "STRING" or "NUMBER"
                    - **rangeKeyField** *(string) --* 
                      The range key name.
                    - **rangeKeyValue** *(string) --* 
                      The range key value.
                    - **rangeKeyType** *(string) --* 
                      The range key type. Valid values are "STRING" or "NUMBER"
                    - **payloadField** *(string) --* 
                      The action payload. This name can be customized.
                  - **dynamoDBv2** *(dict) --* 
                    Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
                    - **roleArn** *(string) --* 
                      The ARN of the IAM role that grants access to the DynamoDB table.
                    - **putItem** *(dict) --* 
                      Specifies the DynamoDB table to which the message data will be written. For example:
                       ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``  
                      Each attribute in the message payload will be written to a separate column in the DynamoDB database.
                      - **tableName** *(string) --* 
                        The table where the message data will be written
                  - **lambda** *(dict) --* 
                    Invoke a Lambda function.
                    - **functionArn** *(string) --* 
                      The ARN of the Lambda function.
                  - **sns** *(dict) --* 
                    Publish to an Amazon SNS topic.
                    - **targetArn** *(string) --* 
                      The ARN of the SNS topic.
                    - **roleArn** *(string) --* 
                      The ARN of the IAM role that grants access.
                    - **messageFormat** *(string) --* 
                      (Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `https\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.
                  - **sqs** *(dict) --* 
                    Publish to an Amazon SQS queue.
                    - **roleArn** *(string) --* 
                      The ARN of the IAM role that grants access.
                    - **queueUrl** *(string) --* 
                      The URL of the Amazon SQS queue.
                    - **useBase64** *(boolean) --* 
                      Specifies whether to use Base64 encoding.
                  - **kinesis** *(dict) --* 
                    Write data to an Amazon Kinesis stream.
                    - **roleArn** *(string) --* 
                      The ARN of the IAM role that grants access to the Amazon Kinesis stream.
                    - **streamName** *(string) --* 
                      The name of the Amazon Kinesis stream.
                    - **partitionKey** *(string) --* 
                      The partition key.
                  - **republish** *(dict) --* 
                    Publish to another MQTT topic.
                    - **roleArn** *(string) --* 
                      The ARN of the IAM role that grants access.
                    - **topic** *(string) --* 
                      The name of the MQTT topic.
                  - **s3** *(dict) --* 
                    Write to an Amazon S3 bucket.
                    - **roleArn** *(string) --* 
                      The ARN of the IAM role that grants access.
                    - **bucketName** *(string) --* 
                      The Amazon S3 bucket.
                    - **key** *(string) --* 
                      The object key.
                    - **cannedAcl** *(string) --* 
                      The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
                  - **firehose** *(dict) --* 
                    Write to an Amazon Kinesis Firehose stream.
                    - **roleArn** *(string) --* 
                      The IAM role that grants access to the Amazon Kinesis Firehose stream.
                    - **deliveryStreamName** *(string) --* 
                      The delivery stream name.
                    - **separator** *(string) --* 
                      A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).
                  - **cloudwatchMetric** *(dict) --* 
                    Capture a CloudWatch metric.
                    - **roleArn** *(string) --* 
                      The IAM role that allows access to the CloudWatch metric.
                    - **metricNamespace** *(string) --* 
                      The CloudWatch metric namespace name.
                    - **metricName** *(string) --* 
                      The CloudWatch metric name.
                    - **metricValue** *(string) --* 
                      The CloudWatch metric value.
                    - **metricUnit** *(string) --* 
                      The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.
                    - **metricTimestamp** *(string) --* 
                      An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .
                  - **cloudwatchAlarm** *(dict) --* 
                    Change the state of a CloudWatch alarm.
                    - **roleArn** *(string) --* 
                      The IAM role that allows access to the CloudWatch alarm.
                    - **alarmName** *(string) --* 
                      The CloudWatch alarm name.
                    - **stateReason** *(string) --* 
                      The reason for the alarm change.
                    - **stateValue** *(string) --* 
                      The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
                  - **elasticsearch** *(dict) --* 
                    Write data to an Amazon Elasticsearch Service domain.
                    - **roleArn** *(string) --* 
                      The IAM role ARN that has access to Elasticsearch.
                    - **endpoint** *(string) --* 
                      The endpoint of your Elasticsearch domain.
                    - **index** *(string) --* 
                      The Elasticsearch index where you want to store your data.
                    - **type** *(string) --* 
                      The type of document you are storing.
                    - **id** *(string) --* 
                      The unique identifier for the document you are storing.
                  - **salesforce** *(dict) --* 
                    Send a message to a Salesforce IoT Cloud Input Stream.
                    - **token** *(string) --* 
                      The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
                    - **url** *(string) --* 
                      The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
                  - **iotAnalytics** *(dict) --* 
                    Sends message data to an AWS IoT Analytics channel.
                    - **channelArn** *(string) --* 
                      (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
                    - **channelName** *(string) --* 
                      The name of the IoT Analytics channel to which message data will be sent.
                    - **roleArn** *(string) --* 
                      The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
                  - **iotEvents** *(dict) --* 
                    Sends an input to an AWS IoT Events detector.
                    - **inputName** *(string) --* 
                      The name of the AWS IoT Events input.
                    - **messageId** *(string) --* 
                      [Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
                    - **roleArn** *(string) --* 
                      The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ("Action":"iotevents:BatchPutMessage").
                  - **stepFunctions** *(dict) --* 
                    Starts execution of a Step Functions state machine.
                    - **executionNamePrefix** *(string) --* 
                      (Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
                    - **stateMachineName** *(string) --* 
                      The name of the Step Functions state machine whose execution will be started.
                    - **roleArn** *(string) --* 
                      The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").
              - **ruleDisabled** *(boolean) --* 
                Specifies whether the rule is disabled.
              - **awsIotSqlVersion** *(string) --* 
                The version of the SQL rules engine to use when evaluating the rule.
              - **errorAction** *(dict) --* 
                The action to perform when an error occurs.
                - **dynamoDB** *(dict) --* 
                  Write to a DynamoDB table.
                  - **tableName** *(string) --* 
                    The name of the DynamoDB table.
                  - **roleArn** *(string) --* 
                    The ARN of the IAM role that grants access to the DynamoDB table.
                  - **operation** *(string) --* 
                    The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .
                  - **hashKeyField** *(string) --* 
                    The hash key name.
                  - **hashKeyValue** *(string) --* 
                    The hash key value.
                  - **hashKeyType** *(string) --* 
                    The hash key type. Valid values are "STRING" or "NUMBER"
                  - **rangeKeyField** *(string) --* 
                    The range key name.
                  - **rangeKeyValue** *(string) --* 
                    The range key value.
                  - **rangeKeyType** *(string) --* 
                    The range key type. Valid values are "STRING" or "NUMBER"
                  - **payloadField** *(string) --* 
                    The action payload. This name can be customized.
                - **dynamoDBv2** *(dict) --* 
                  Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
                  - **roleArn** *(string) --* 
                    The ARN of the IAM role that grants access to the DynamoDB table.
                  - **putItem** *(dict) --* 
                    Specifies the DynamoDB table to which the message data will be written. For example:
                     ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``  
                    Each attribute in the message payload will be written to a separate column in the DynamoDB database.
                    - **tableName** *(string) --* 
                      The table where the message data will be written
                - **lambda** *(dict) --* 
                  Invoke a Lambda function.
                  - **functionArn** *(string) --* 
                    The ARN of the Lambda function.
                - **sns** *(dict) --* 
                  Publish to an Amazon SNS topic.
                  - **targetArn** *(string) --* 
                    The ARN of the SNS topic.
                  - **roleArn** *(string) --* 
                    The ARN of the IAM role that grants access.
                  - **messageFormat** *(string) --* 
                    (Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `https\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.
                - **sqs** *(dict) --* 
                  Publish to an Amazon SQS queue.
                  - **roleArn** *(string) --* 
                    The ARN of the IAM role that grants access.
                  - **queueUrl** *(string) --* 
                    The URL of the Amazon SQS queue.
                  - **useBase64** *(boolean) --* 
                    Specifies whether to use Base64 encoding.
                - **kinesis** *(dict) --* 
                  Write data to an Amazon Kinesis stream.
                  - **roleArn** *(string) --* 
                    The ARN of the IAM role that grants access to the Amazon Kinesis stream.
                  - **streamName** *(string) --* 
                    The name of the Amazon Kinesis stream.
                  - **partitionKey** *(string) --* 
                    The partition key.
                - **republish** *(dict) --* 
                  Publish to another MQTT topic.
                  - **roleArn** *(string) --* 
                    The ARN of the IAM role that grants access.
                  - **topic** *(string) --* 
                    The name of the MQTT topic.
                - **s3** *(dict) --* 
                  Write to an Amazon S3 bucket.
                  - **roleArn** *(string) --* 
                    The ARN of the IAM role that grants access.
                  - **bucketName** *(string) --* 
                    The Amazon S3 bucket.
                  - **key** *(string) --* 
                    The object key.
                  - **cannedAcl** *(string) --* 
                    The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
                - **firehose** *(dict) --* 
                  Write to an Amazon Kinesis Firehose stream.
                  - **roleArn** *(string) --* 
                    The IAM role that grants access to the Amazon Kinesis Firehose stream.
                  - **deliveryStreamName** *(string) --* 
                    The delivery stream name.
                  - **separator** *(string) --* 
                    A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).
                - **cloudwatchMetric** *(dict) --* 
                  Capture a CloudWatch metric.
                  - **roleArn** *(string) --* 
                    The IAM role that allows access to the CloudWatch metric.
                  - **metricNamespace** *(string) --* 
                    The CloudWatch metric namespace name.
                  - **metricName** *(string) --* 
                    The CloudWatch metric name.
                  - **metricValue** *(string) --* 
                    The CloudWatch metric value.
                  - **metricUnit** *(string) --* 
                    The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.
                  - **metricTimestamp** *(string) --* 
                    An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .
                - **cloudwatchAlarm** *(dict) --* 
                  Change the state of a CloudWatch alarm.
                  - **roleArn** *(string) --* 
                    The IAM role that allows access to the CloudWatch alarm.
                  - **alarmName** *(string) --* 
                    The CloudWatch alarm name.
                  - **stateReason** *(string) --* 
                    The reason for the alarm change.
                  - **stateValue** *(string) --* 
                    The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
                - **elasticsearch** *(dict) --* 
                  Write data to an Amazon Elasticsearch Service domain.
                  - **roleArn** *(string) --* 
                    The IAM role ARN that has access to Elasticsearch.
                  - **endpoint** *(string) --* 
                    The endpoint of your Elasticsearch domain.
                  - **index** *(string) --* 
                    The Elasticsearch index where you want to store your data.
                  - **type** *(string) --* 
                    The type of document you are storing.
                  - **id** *(string) --* 
                    The unique identifier for the document you are storing.
                - **salesforce** *(dict) --* 
                  Send a message to a Salesforce IoT Cloud Input Stream.
                  - **token** *(string) --* 
                    The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
                  - **url** *(string) --* 
                    The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
                - **iotAnalytics** *(dict) --* 
                  Sends message data to an AWS IoT Analytics channel.
                  - **channelArn** *(string) --* 
                    (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
                  - **channelName** *(string) --* 
                    The name of the IoT Analytics channel to which message data will be sent.
                  - **roleArn** *(string) --* 
                    The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
                - **iotEvents** *(dict) --* 
                  Sends an input to an AWS IoT Events detector.
                  - **inputName** *(string) --* 
                    The name of the AWS IoT Events input.
                  - **messageId** *(string) --* 
                    [Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
                  - **roleArn** *(string) --* 
                    The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ("Action":"iotevents:BatchPutMessage").
                - **stepFunctions** *(dict) --* 
                  Starts execution of a Step Functions state machine.
                  - **executionNamePrefix** *(string) --* 
                    (Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
                  - **stateMachineName** *(string) --* 
                    The name of the Step Functions state machine whose execution will be started.
                  - **roleArn** *(string) --* 
                    The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").
        :type ruleName: string
        :param ruleName: **[REQUIRED]**
          The name of the rule.
        :rtype: dict
        :returns:
        """
        pass

    def get_v2_logging_options(self) -> Dict:
        """
        Gets the fine grained logging options.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetV2LoggingOptions>`_
        
        **Request Syntax**
        ::
          response = client.get_v2_logging_options()
        
        **Response Syntax**
        ::
            {
                'roleArn': 'string',
                'defaultLogLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
                'disableAllLogs': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **roleArn** *(string) --* 
              The IAM role ARN AWS IoT uses to write to your CloudWatch logs.
            - **defaultLogLevel** *(string) --* 
              The default log level.
            - **disableAllLogs** *(boolean) --* 
              Disables all logs.
        :rtype: dict
        :returns:
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

    def list_active_violations(self, thingName: str = None, securityProfileName: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the active violations for a given Device Defender security profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListActiveViolations>`_
        
        **Request Syntax**
        ::
          response = client.list_active_violations(
              thingName='string',
              securityProfileName='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'activeViolations': [
                    {
                        'violationId': 'string',
                        'thingName': 'string',
                        'securityProfileName': 'string',
                        'behavior': {
                            'name': 'string',
                            'metric': 'string',
                            'criteria': {
                                'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                                'value': {
                                    'count': 123,
                                    'cidrs': [
                                        'string',
                                    ],
                                    'ports': [
                                        123,
                                    ]
                                },
                                'durationSeconds': 123,
                                'consecutiveDatapointsToAlarm': 123,
                                'consecutiveDatapointsToClear': 123,
                                'statisticalThreshold': {
                                    'statistic': 'string'
                                }
                            }
                        },
                        'lastViolationValue': {
                            'count': 123,
                            'cidrs': [
                                'string',
                            ],
                            'ports': [
                                123,
                            ]
                        },
                        'lastViolationTime': datetime(2015, 1, 1),
                        'violationStartTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **activeViolations** *(list) --* 
              The list of active violations.
              - *(dict) --* 
                Information about an active Device Defender security profile behavior violation.
                - **violationId** *(string) --* 
                  The ID of the active violation.
                - **thingName** *(string) --* 
                  The name of the thing responsible for the active violation.
                - **securityProfileName** *(string) --* 
                  The security profile whose behavior is in violation.
                - **behavior** *(dict) --* 
                  The behavior which is being violated.
                  - **name** *(string) --* 
                    The name you have given to the behavior.
                  - **metric** *(string) --* 
                    What is measured by the behavior.
                  - **criteria** *(dict) --* 
                    The criteria that determine if a device is behaving normally in regard to the ``metric`` .
                    - **comparisonOperator** *(string) --* 
                      The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
                    - **value** *(dict) --* 
                      The value to be compared with the ``metric`` .
                      - **count** *(integer) --* 
                        If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                      - **cidrs** *(list) --* 
                        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                        - *(string) --* 
                      - **ports** *(list) --* 
                        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                        - *(integer) --* 
                    - **durationSeconds** *(integer) --* 
                      Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
                    - **consecutiveDatapointsToAlarm** *(integer) --* 
                      If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
                    - **consecutiveDatapointsToClear** *(integer) --* 
                      If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
                    - **statisticalThreshold** *(dict) --* 
                      A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                      - **statistic** *(string) --* 
                        The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
                - **lastViolationValue** *(dict) --* 
                  The value of the metric (the measurement) which caused the most recent violation.
                  - **count** *(integer) --* 
                    If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                  - **cidrs** *(list) --* 
                    If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                    - *(string) --* 
                  - **ports** *(list) --* 
                    If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                    - *(integer) --* 
                - **lastViolationTime** *(datetime) --* 
                  The time the most recent violation occurred.
                - **violationStartTime** *(datetime) --* 
                  The time the violation started.
            - **nextToken** *(string) --* 
              A token that can be used to retrieve the next set of results, or ``null`` if there are no additional results.
        :type thingName: string
        :param thingName:
          The name of the thing whose active violations are listed.
        :type securityProfileName: string
        :param securityProfileName:
          The name of the Device Defender security profile for which violations are listed.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def list_attached_policies(self, target: str, recursive: bool = None, marker: str = None, pageSize: int = None) -> Dict:
        """
        Lists the policies attached to the specified thing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAttachedPolicies>`_
        
        **Request Syntax**
        ::
          response = client.list_attached_policies(
              target='string',
              recursive=True|False,
              marker='string',
              pageSize=123
          )
        
        **Response Syntax**
        ::
            {
                'policies': [
                    {
                        'policyName': 'string',
                        'policyArn': 'string'
                    },
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **policies** *(list) --* 
              The policies.
              - *(dict) --* 
                Describes an AWS IoT policy.
                - **policyName** *(string) --* 
                  The policy name.
                - **policyArn** *(string) --* 
                  The policy ARN.
            - **nextMarker** *(string) --* 
              The token to retrieve the next set of results, or ``null`` if there are no more results.
        :type target: string
        :param target: **[REQUIRED]**
          The group for which the policies will be listed.
        :type recursive: boolean
        :param recursive:
          When true, recursively list attached policies.
        :type marker: string
        :param marker:
          The token to retrieve the next set of results.
        :type pageSize: integer
        :param pageSize:
          The maximum number of results to be returned per request.
        :rtype: dict
        :returns:
        """
        pass

    def list_audit_findings(self, taskId: str = None, checkName: str = None, resourceIdentifier: Dict = None, maxResults: int = None, nextToken: str = None, startTime: datetime = None, endTime: datetime = None) -> Dict:
        """
        Lists the findings (results) of a Device Defender audit or of the audits performed during a specified time period. (Findings are retained for 180 days.)
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuditFindings>`_
        
        **Request Syntax**
        ::
          response = client.list_audit_findings(
              taskId='string',
              checkName='string',
              resourceIdentifier={
                  'deviceCertificateId': 'string',
                  'caCertificateId': 'string',
                  'cognitoIdentityPoolId': 'string',
                  'clientId': 'string',
                  'policyVersionIdentifier': {
                      'policyName': 'string',
                      'policyVersionId': 'string'
                  },
                  'account': 'string'
              },
              maxResults=123,
              nextToken='string',
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1)
          )
        
        **Response Syntax**
        ::
            {
                'findings': [
                    {
                        'taskId': 'string',
                        'checkName': 'string',
                        'taskStartTime': datetime(2015, 1, 1),
                        'findingTime': datetime(2015, 1, 1),
                        'severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW',
                        'nonCompliantResource': {
                            'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS',
                            'resourceIdentifier': {
                                'deviceCertificateId': 'string',
                                'caCertificateId': 'string',
                                'cognitoIdentityPoolId': 'string',
                                'clientId': 'string',
                                'policyVersionIdentifier': {
                                    'policyName': 'string',
                                    'policyVersionId': 'string'
                                },
                                'account': 'string'
                            },
                            'additionalInfo': {
                                'string': 'string'
                            }
                        },
                        'relatedResources': [
                            {
                                'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS',
                                'resourceIdentifier': {
                                    'deviceCertificateId': 'string',
                                    'caCertificateId': 'string',
                                    'cognitoIdentityPoolId': 'string',
                                    'clientId': 'string',
                                    'policyVersionIdentifier': {
                                        'policyName': 'string',
                                        'policyVersionId': 'string'
                                    },
                                    'account': 'string'
                                },
                                'additionalInfo': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'reasonForNonCompliance': 'string',
                        'reasonForNonComplianceCode': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **findings** *(list) --* 
              The findings (results) of the audit.
              - *(dict) --* 
                The findings (results) of the audit.
                - **taskId** *(string) --* 
                  The ID of the audit that generated this result (finding)
                - **checkName** *(string) --* 
                  The audit check that generated this result.
                - **taskStartTime** *(datetime) --* 
                  The time the audit started.
                - **findingTime** *(datetime) --* 
                  The time the result (finding) was discovered.
                - **severity** *(string) --* 
                  The severity of the result (finding).
                - **nonCompliantResource** *(dict) --* 
                  The resource that was found to be non-compliant with the audit check.
                  - **resourceType** *(string) --* 
                    The type of the non-compliant resource.
                  - **resourceIdentifier** *(dict) --* 
                    Information identifying the non-compliant resource.
                    - **deviceCertificateId** *(string) --* 
                      The ID of the certificate attached to the resource.
                    - **caCertificateId** *(string) --* 
                      The ID of the CA certificate used to authorize the certificate.
                    - **cognitoIdentityPoolId** *(string) --* 
                      The ID of the Cognito Identity Pool.
                    - **clientId** *(string) --* 
                      The client ID.
                    - **policyVersionIdentifier** *(dict) --* 
                      The version of the policy associated with the resource.
                      - **policyName** *(string) --* 
                        The name of the policy.
                      - **policyVersionId** *(string) --* 
                        The ID of the version of the policy associated with the resource.
                    - **account** *(string) --* 
                      The account with which the resource is associated.
                  - **additionalInfo** *(dict) --* 
                    Additional information about the non-compliant resource.
                    - *(string) --* 
                      - *(string) --* 
                - **relatedResources** *(list) --* 
                  The list of related resources.
                  - *(dict) --* 
                    Information about a related resource.
                    - **resourceType** *(string) --* 
                      The type of resource.
                    - **resourceIdentifier** *(dict) --* 
                      Information identifying the resource.
                      - **deviceCertificateId** *(string) --* 
                        The ID of the certificate attached to the resource.
                      - **caCertificateId** *(string) --* 
                        The ID of the CA certificate used to authorize the certificate.
                      - **cognitoIdentityPoolId** *(string) --* 
                        The ID of the Cognito Identity Pool.
                      - **clientId** *(string) --* 
                        The client ID.
                      - **policyVersionIdentifier** *(dict) --* 
                        The version of the policy associated with the resource.
                        - **policyName** *(string) --* 
                          The name of the policy.
                        - **policyVersionId** *(string) --* 
                          The ID of the version of the policy associated with the resource.
                      - **account** *(string) --* 
                        The account with which the resource is associated.
                    - **additionalInfo** *(dict) --* 
                      Additional information about the resource.
                      - *(string) --* 
                        - *(string) --* 
                - **reasonForNonCompliance** *(string) --* 
                  The reason the resource was non-compliant.
                - **reasonForNonComplianceCode** *(string) --* 
                  A code which indicates the reason that the resource was non-compliant.
            - **nextToken** *(string) --* 
              A token that can be used to retrieve the next set of results, or ``null`` if there are no additional results.
        :type taskId: string
        :param taskId:
          A filter to limit results to the audit with the specified ID. You must specify either the taskId or the startTime and endTime, but not both.
        :type checkName: string
        :param checkName:
          A filter to limit results to the findings for the specified audit check.
        :type resourceIdentifier: dict
        :param resourceIdentifier:
          Information identifying the non-compliant resource.
          - **deviceCertificateId** *(string) --*
            The ID of the certificate attached to the resource.
          - **caCertificateId** *(string) --*
            The ID of the CA certificate used to authorize the certificate.
          - **cognitoIdentityPoolId** *(string) --*
            The ID of the Cognito Identity Pool.
          - **clientId** *(string) --*
            The client ID.
          - **policyVersionIdentifier** *(dict) --*
            The version of the policy associated with the resource.
            - **policyName** *(string) --*
              The name of the policy.
            - **policyVersionId** *(string) --*
              The ID of the version of the policy associated with the resource.
          - **account** *(string) --*
            The account with which the resource is associated.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time. The default is 25.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type startTime: datetime
        :param startTime:
          A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.
        :type endTime: datetime
        :param endTime:
          A filter to limit results to those found before the specified time. You must specify either the startTime and endTime or the taskId, but not both.
        :rtype: dict
        :returns:
        """
        pass

    def list_audit_tasks(self, startTime: datetime, endTime: datetime, taskType: str = None, taskStatus: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the Device Defender audits that have been performed during a given time period.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuditTasks>`_
        
        **Request Syntax**
        ::
          response = client.list_audit_tasks(
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              taskType='ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK',
              taskStatus='IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'tasks': [
                    {
                        'taskId': 'string',
                        'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
                        'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tasks** *(list) --* 
              The audits that were performed during the specified time period.
              - *(dict) --* 
                The audits that were performed.
                - **taskId** *(string) --* 
                  The ID of this audit.
                - **taskStatus** *(string) --* 
                  The status of this audit: one of "IN_PROGRESS", "COMPLETED", "FAILED" or "CANCELED".
                - **taskType** *(string) --* 
                  The type of this audit: one of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".
            - **nextToken** *(string) --* 
              A token that can be used to retrieve the next set of results, or ``null`` if there are no additional results.
        :type startTime: datetime
        :param startTime: **[REQUIRED]**
          The beginning of the time period. Note that audit information is retained for a limited time (180 days). Requesting a start time prior to what is retained results in an \"InvalidRequestException\".
        :type endTime: datetime
        :param endTime: **[REQUIRED]**
          The end of the time period.
        :type taskType: string
        :param taskType:
          A filter to limit the output to the specified type of audit: can be one of \"ON_DEMAND_AUDIT_TASK\" or \"SCHEDULED__AUDIT_TASK\".
        :type taskStatus: string
        :param taskStatus:
          A filter to limit the output to audits with the specified completion status: can be one of \"IN_PROGRESS\", \"COMPLETED\", \"FAILED\" or \"CANCELED\".
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time. The default is 25.
        :rtype: dict
        :returns:
        """
        pass

    def list_authorizers(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None, status: str = None) -> Dict:
        """
        Lists the authorizers registered in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuthorizers>`_
        
        **Request Syntax**
        ::
          response = client.list_authorizers(
              pageSize=123,
              marker='string',
              ascendingOrder=True|False,
              status='ACTIVE'|'INACTIVE'
          )
        
        **Response Syntax**
        ::
            {
                'authorizers': [
                    {
                        'authorizerName': 'string',
                        'authorizerArn': 'string'
                    },
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **authorizers** *(list) --* 
              The authorizers.
              - *(dict) --* 
                The authorizer summary.
                - **authorizerName** *(string) --* 
                  The authorizer name.
                - **authorizerArn** *(string) --* 
                  The authorizer ARN.
            - **nextMarker** *(string) --* 
              A marker used to get the next set of results.
        :type pageSize: integer
        :param pageSize:
          The maximum number of results to return at one time.
        :type marker: string
        :param marker:
          A marker used to get the next set of results.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Return the list of authorizers in ascending alphabetical order.
        :type status: string
        :param status:
          The status of the list authorizers request.
        :rtype: dict
        :returns:
        """
        pass

    def list_billing_groups(self, nextToken: str = None, maxResults: int = None, namePrefixFilter: str = None) -> Dict:
        """
        Lists the billing groups you have created.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListBillingGroups>`_
        
        **Request Syntax**
        ::
          response = client.list_billing_groups(
              nextToken='string',
              maxResults=123,
              namePrefixFilter='string'
          )
        
        **Response Syntax**
        ::
            {
                'billingGroups': [
                    {
                        'groupName': 'string',
                        'groupArn': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **billingGroups** *(list) --* 
              The list of billing groups.
              - *(dict) --* 
                The name and ARN of a group.
                - **groupName** *(string) --* 
                  The group name.
                - **groupArn** *(string) --* 
                  The group ARN.
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return per request.
        :type namePrefixFilter: string
        :param namePrefixFilter:
          Limit the results to billing groups whose names have the given prefix.
        :rtype: dict
        :returns:
        """
        pass

    def list_ca_certificates(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        """
        Lists the CA certificates registered for your AWS account.
        The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCACertificates>`_
        
        **Request Syntax**
        ::
          response = client.list_ca_certificates(
              pageSize=123,
              marker='string',
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'certificates': [
                    {
                        'certificateArn': 'string',
                        'certificateId': 'string',
                        'status': 'ACTIVE'|'INACTIVE',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListCACertificates operation.
            - **certificates** *(list) --* 
              The CA certificates registered in your AWS account.
              - *(dict) --* 
                A CA certificate.
                - **certificateArn** *(string) --* 
                  The ARN of the CA certificate.
                - **certificateId** *(string) --* 
                  The ID of the CA certificate.
                - **status** *(string) --* 
                  The status of the CA certificate.
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
                - **creationDate** *(datetime) --* 
                  The date the CA certificate was created.
            - **nextMarker** *(string) --* 
              The current position within the list of CA certificates.
        :type pageSize: integer
        :param pageSize:
          The result page size.
        :type marker: string
        :param marker:
          The marker for the next set of results.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Determines the order of the results.
        :rtype: dict
        :returns:
        """
        pass

    def list_certificates(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        """
        Lists the certificates registered in your AWS account.
        The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificates>`_
        
        **Request Syntax**
        ::
          response = client.list_certificates(
              pageSize=123,
              marker='string',
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'certificates': [
                    {
                        'certificateArn': 'string',
                        'certificateId': 'string',
                        'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the ListCertificates operation.
            - **certificates** *(list) --* 
              The descriptions of the certificates.
              - *(dict) --* 
                Information about a certificate.
                - **certificateArn** *(string) --* 
                  The ARN of the certificate.
                - **certificateId** *(string) --* 
                  The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
                - **status** *(string) --* 
                  The status of the certificate.
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
                - **creationDate** *(datetime) --* 
                  The date and time the certificate was created.
            - **nextMarker** *(string) --* 
              The marker for the next set of results, or null if there are no additional results.
        :type pageSize: integer
        :param pageSize:
          The result page size.
        :type marker: string
        :param marker:
          The marker for the next set of results.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
        :rtype: dict
        :returns:
        """
        pass

    def list_certificates_by_ca(self, caCertificateId: str, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        """
        List the device certificates signed by the specified CA certificate.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificatesByCA>`_
        
        **Request Syntax**
        ::
          response = client.list_certificates_by_ca(
              caCertificateId='string',
              pageSize=123,
              marker='string',
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'certificates': [
                    {
                        'certificateArn': 'string',
                        'certificateId': 'string',
                        'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the ListCertificatesByCA operation.
            - **certificates** *(list) --* 
              The device certificates signed by the specified CA certificate.
              - *(dict) --* 
                Information about a certificate.
                - **certificateArn** *(string) --* 
                  The ARN of the certificate.
                - **certificateId** *(string) --* 
                  The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
                - **status** *(string) --* 
                  The status of the certificate.
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
                - **creationDate** *(datetime) --* 
                  The date and time the certificate was created.
            - **nextMarker** *(string) --* 
              The marker for the next set of results, or null if there are no additional results.
        :type caCertificateId: string
        :param caCertificateId: **[REQUIRED]**
          The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.
        :type pageSize: integer
        :param pageSize:
          The result page size.
        :type marker: string
        :param marker:
          The marker for the next set of results.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
        :rtype: dict
        :returns:
        """
        pass

    def list_indices(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the search indices.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListIndices>`_
        
        **Request Syntax**
        ::
          response = client.list_indices(
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'indexNames': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **indexNames** *(list) --* 
              The index names.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token used to get the next set of results, or **null** if there are no additional results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def list_job_executions_for_job(self, jobId: str, status: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Lists the job executions for a job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobExecutionsForJob>`_
        
        **Request Syntax**
        ::
          response = client.list_job_executions_for_job(
              jobId='string',
              status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'executionSummaries': [
                    {
                        'thingArn': 'string',
                        'jobExecutionSummary': {
                            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                            'queuedAt': datetime(2015, 1, 1),
                            'startedAt': datetime(2015, 1, 1),
                            'lastUpdatedAt': datetime(2015, 1, 1),
                            'executionNumber': 123
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **executionSummaries** *(list) --* 
              A list of job execution summaries.
              - *(dict) --* 
                Contains a summary of information about job executions for a specific job.
                - **thingArn** *(string) --* 
                  The ARN of the thing on which the job execution is running.
                - **jobExecutionSummary** *(dict) --* 
                  Contains a subset of information about a job execution.
                  - **status** *(string) --* 
                    The status of the job execution.
                  - **queuedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution was queued.
                  - **startedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution started.
                  - **lastUpdatedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution was last updated.
                  - **executionNumber** *(integer) --* 
                    A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.
            - **nextToken** *(string) --* 
              The token for the next set of results, or **null** if there are no additional results.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The unique identifier you assigned to this job when it was created.
        :type status: string
        :param status:
          The status of the job.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to be returned per request.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def list_job_executions_for_thing(self, thingName: str, status: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Lists the job executions for the specified thing.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobExecutionsForThing>`_
        
        **Request Syntax**
        ::
          response = client.list_job_executions_for_thing(
              thingName='string',
              status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'executionSummaries': [
                    {
                        'jobId': 'string',
                        'jobExecutionSummary': {
                            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                            'queuedAt': datetime(2015, 1, 1),
                            'startedAt': datetime(2015, 1, 1),
                            'lastUpdatedAt': datetime(2015, 1, 1),
                            'executionNumber': 123
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **executionSummaries** *(list) --* 
              A list of job execution summaries.
              - *(dict) --* 
                The job execution summary for a thing.
                - **jobId** *(string) --* 
                  The unique identifier you assigned to this job when it was created.
                - **jobExecutionSummary** *(dict) --* 
                  Contains a subset of information about a job execution.
                  - **status** *(string) --* 
                    The status of the job execution.
                  - **queuedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution was queued.
                  - **startedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution started.
                  - **lastUpdatedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution was last updated.
                  - **executionNumber** *(integer) --* 
                    A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.
            - **nextToken** *(string) --* 
              The token for the next set of results, or **null** if there are no additional results.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The thing name.
        :type status: string
        :param status:
          An optional filter that lets you search for jobs that have the specified status.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to be returned per request.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def list_jobs(self, status: str = None, targetSelection: str = None, maxResults: int = None, nextToken: str = None, thingGroupName: str = None, thingGroupId: str = None) -> Dict:
        """
        Lists jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_jobs(
              status='IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
              targetSelection='CONTINUOUS'|'SNAPSHOT',
              maxResults=123,
              nextToken='string',
              thingGroupName='string',
              thingGroupId='string'
          )
        
        **Response Syntax**
        ::
            {
                'jobs': [
                    {
                        'jobArn': 'string',
                        'jobId': 'string',
                        'thingGroupId': 'string',
                        'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
                        'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'completedAt': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **jobs** *(list) --* 
              A list of jobs.
              - *(dict) --* 
                The job summary.
                - **jobArn** *(string) --* 
                  The job ARN.
                - **jobId** *(string) --* 
                  The unique identifier you assigned to this job when it was created.
                - **thingGroupId** *(string) --* 
                  The ID of the thing group.
                - **targetSelection** *(string) --* 
                  Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.
                - **status** *(string) --* 
                  The job summary status.
                - **createdAt** *(datetime) --* 
                  The time, in seconds since the epoch, when the job was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in seconds since the epoch, when the job was last updated.
                - **completedAt** *(datetime) --* 
                  The time, in seconds since the epoch, when the job completed.
            - **nextToken** *(string) --* 
              The token for the next set of results, or **null** if there are no additional results.
        :type status: string
        :param status:
          An optional filter that lets you search for jobs that have the specified status.
        :type targetSelection: string
        :param targetSelection:
          Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return per request.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type thingGroupName: string
        :param thingGroupName:
          A filter that limits the returned jobs to those for the specified group.
        :type thingGroupId: string
        :param thingGroupId:
          A filter that limits the returned jobs to those for the specified group.
        :rtype: dict
        :returns:
        """
        pass

    def list_ota_updates(self, maxResults: int = None, nextToken: str = None, otaUpdateStatus: str = None) -> Dict:
        """
        Lists OTA updates.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListOTAUpdates>`_
        
        **Request Syntax**
        ::
          response = client.list_ota_updates(
              maxResults=123,
              nextToken='string',
              otaUpdateStatus='CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
          )
        
        **Response Syntax**
        ::
            {
                'otaUpdates': [
                    {
                        'otaUpdateId': 'string',
                        'otaUpdateArn': 'string',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **otaUpdates** *(list) --* 
              A list of OTA update jobs.
              - *(dict) --* 
                An OTA update summary.
                - **otaUpdateId** *(string) --* 
                  The OTA update ID.
                - **otaUpdateArn** *(string) --* 
                  The OTA update ARN.
                - **creationDate** *(datetime) --* 
                  The date when the OTA update was created.
            - **nextToken** *(string) --* 
              A token to use to get the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :type nextToken: string
        :param nextToken:
          A token used to retrieve the next set of results.
        :type otaUpdateStatus: string
        :param otaUpdateStatus:
          The OTA update job status.
        :rtype: dict
        :returns:
        """
        pass

    def list_outgoing_certificates(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        """
        Lists certificates that are being transferred but not yet accepted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListOutgoingCertificates>`_
        
        **Request Syntax**
        ::
          response = client.list_outgoing_certificates(
              pageSize=123,
              marker='string',
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'outgoingCertificates': [
                    {
                        'certificateArn': 'string',
                        'certificateId': 'string',
                        'transferredTo': 'string',
                        'transferDate': datetime(2015, 1, 1),
                        'transferMessage': 'string',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListOutgoingCertificates operation.
            - **outgoingCertificates** *(list) --* 
              The certificates that are being transferred but not yet accepted.
              - *(dict) --* 
                A certificate that has been transferred but not yet accepted.
                - **certificateArn** *(string) --* 
                  The certificate ARN.
                - **certificateId** *(string) --* 
                  The certificate ID.
                - **transferredTo** *(string) --* 
                  The AWS account to which the transfer was made.
                - **transferDate** *(datetime) --* 
                  The date the transfer was initiated.
                - **transferMessage** *(string) --* 
                  The transfer message.
                - **creationDate** *(datetime) --* 
                  The certificate creation date.
            - **nextMarker** *(string) --* 
              The marker for the next set of results.
        :type pageSize: integer
        :param pageSize:
          The result page size.
        :type marker: string
        :param marker:
          The marker for the next set of results.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
        :rtype: dict
        :returns:
        """
        pass

    def list_policies(self, marker: str = None, pageSize: int = None, ascendingOrder: bool = None) -> Dict:
        """
        Lists your policies.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicies>`_
        
        **Request Syntax**
        ::
          response = client.list_policies(
              marker='string',
              pageSize=123,
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'policies': [
                    {
                        'policyName': 'string',
                        'policyArn': 'string'
                    },
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPolicies operation.
            - **policies** *(list) --* 
              The descriptions of the policies.
              - *(dict) --* 
                Describes an AWS IoT policy.
                - **policyName** *(string) --* 
                  The policy name.
                - **policyArn** *(string) --* 
                  The policy ARN.
            - **nextMarker** *(string) --* 
              The marker for the next set of results, or null if there are no additional results.
        :type marker: string
        :param marker:
          The marker for the next set of results.
        :type pageSize: integer
        :param pageSize:
          The result page size.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If true, the results are returned in ascending creation order.
        :rtype: dict
        :returns:
        """
        pass

    def list_policy_principals(self, policyName: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None) -> Dict:
        """
        Lists the principals associated with the specified policy.
         **Note:** This API is deprecated. Please use  ListTargetsForPolicy instead.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicyPrincipals>`_
        
        **Request Syntax**
        ::
          response = client.list_policy_principals(
              policyName='string',
              marker='string',
              pageSize=123,
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'principals': [
                    'string',
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPolicyPrincipals operation.
            - **principals** *(list) --* 
              The descriptions of the principals.
              - *(string) --* 
            - **nextMarker** *(string) --* 
              The marker for the next set of results, or null if there are no additional results.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
        :type marker: string
        :param marker:
          The marker for the next set of results.
        :type pageSize: integer
        :param pageSize:
          The result page size.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If true, the results are returned in ascending creation order.
        :rtype: dict
        :returns:
        """
        pass

    def list_policy_versions(self, policyName: str) -> Dict:
        """
        Lists the versions of the specified policy and identifies the default version.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicyVersions>`_
        
        **Request Syntax**
        ::
          response = client.list_policy_versions(
              policyName='string'
          )
        
        **Response Syntax**
        ::
            {
                'policyVersions': [
                    {
                        'versionId': 'string',
                        'isDefaultVersion': True|False,
                        'createDate': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPolicyVersions operation.
            - **policyVersions** *(list) --* 
              The policy versions.
              - *(dict) --* 
                Describes a policy version.
                - **versionId** *(string) --* 
                  The policy version ID.
                - **isDefaultVersion** *(boolean) --* 
                  Specifies whether the policy version is the default.
                - **createDate** *(datetime) --* 
                  The date and time the policy was created.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
        :rtype: dict
        :returns:
        """
        pass

    def list_principal_policies(self, principal: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None) -> Dict:
        """
        Lists the policies attached to the specified principal. If you use an Cognito identity, the ID must be in `AmazonCognito Identity format <https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html#API_GetCredentialsForIdentity_RequestSyntax>`__ .
         **Note:** This API is deprecated. Please use  ListAttachedPolicies instead.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalPolicies>`_
        
        **Request Syntax**
        ::
          response = client.list_principal_policies(
              principal='string',
              marker='string',
              pageSize=123,
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'policies': [
                    {
                        'policyName': 'string',
                        'policyArn': 'string'
                    },
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPrincipalPolicies operation.
            - **policies** *(list) --* 
              The policies.
              - *(dict) --* 
                Describes an AWS IoT policy.
                - **policyName** *(string) --* 
                  The policy name.
                - **policyArn** *(string) --* 
                  The policy ARN.
            - **nextMarker** *(string) --* 
              The marker for the next set of results, or null if there are no additional results.
        :type principal: string
        :param principal: **[REQUIRED]**
          The principal.
        :type marker: string
        :param marker:
          The marker for the next set of results.
        :type pageSize: integer
        :param pageSize:
          The result page size.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If true, results are returned in ascending creation order.
        :rtype: dict
        :returns:
        """
        pass

    def list_principal_things(self, principal: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the things associated with the specified principal. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalThings>`_
        
        **Request Syntax**
        ::
          response = client.list_principal_things(
              nextToken='string',
              maxResults=123,
              principal='string'
          )
        
        **Response Syntax**
        ::
            {
                'things': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPrincipalThings operation.
            - **things** *(list) --* 
              The things.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return in this operation.
        :type principal: string
        :param principal: **[REQUIRED]**
          The principal.
        :rtype: dict
        :returns:
        """
        pass

    def list_role_aliases(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        """
        Lists the role aliases registered in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListRoleAliases>`_
        
        **Request Syntax**
        ::
          response = client.list_role_aliases(
              pageSize=123,
              marker='string',
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'roleAliases': [
                    'string',
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **roleAliases** *(list) --* 
              The role aliases.
              - *(string) --* 
            - **nextMarker** *(string) --* 
              A marker used to get the next set of results.
        :type pageSize: integer
        :param pageSize:
          The maximum number of results to return at one time.
        :type marker: string
        :param marker:
          A marker used to get the next set of results.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Return the list of role aliases in ascending alphabetical order.
        :rtype: dict
        :returns:
        """
        pass

    def list_scheduled_audits(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists all of your scheduled audits.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListScheduledAudits>`_
        
        **Request Syntax**
        ::
          response = client.list_scheduled_audits(
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'scheduledAudits': [
                    {
                        'scheduledAuditName': 'string',
                        'scheduledAuditArn': 'string',
                        'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
                        'dayOfMonth': 'string',
                        'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **scheduledAudits** *(list) --* 
              The list of scheduled audits.
              - *(dict) --* 
                Information about the scheduled audit.
                - **scheduledAuditName** *(string) --* 
                  The name of the scheduled audit.
                - **scheduledAuditArn** *(string) --* 
                  The ARN of the scheduled audit.
                - **frequency** *(string) --* 
                  How often the scheduled audit takes place.
                - **dayOfMonth** *(string) --* 
                  The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
                - **dayOfWeek** *(string) --* 
                  The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").
            - **nextToken** *(string) --* 
              A token that can be used to retrieve the next set of results, or ``null`` if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time. The default is 25.
        :rtype: dict
        :returns:
        """
        pass

    def list_security_profiles(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the Device Defender security profiles you have created. You can use filters to list only those security profiles associated with a thing group or only those associated with your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListSecurityProfiles>`_
        
        **Request Syntax**
        ::
          response = client.list_security_profiles(
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'securityProfileIdentifiers': [
                    {
                        'name': 'string',
                        'arn': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileIdentifiers** *(list) --* 
              A list of security profile identifiers (names and ARNs).
              - *(dict) --* 
                Identifying information for a Device Defender security profile.
                - **name** *(string) --* 
                  The name you have given to the security profile.
                - **arn** *(string) --* 
                  The ARN of the security profile.
            - **nextToken** *(string) --* 
              A token that can be used to retrieve the next set of results, or ``null`` if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def list_security_profiles_for_target(self, securityProfileTargetArn: str, nextToken: str = None, maxResults: int = None, recursive: bool = None) -> Dict:
        """
        Lists the Device Defender security profiles attached to a target (thing group).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListSecurityProfilesForTarget>`_
        
        **Request Syntax**
        ::
          response = client.list_security_profiles_for_target(
              nextToken='string',
              maxResults=123,
              recursive=True|False,
              securityProfileTargetArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'securityProfileTargetMappings': [
                    {
                        'securityProfileIdentifier': {
                            'name': 'string',
                            'arn': 'string'
                        },
                        'target': {
                            'arn': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileTargetMappings** *(list) --* 
              A list of security profiles and their associated targets.
              - *(dict) --* 
                Information about a security profile and the target associated with it.
                - **securityProfileIdentifier** *(dict) --* 
                  Information that identifies the security profile.
                  - **name** *(string) --* 
                    The name you have given to the security profile.
                  - **arn** *(string) --* 
                    The ARN of the security profile.
                - **target** *(dict) --* 
                  Information about the target (thing group) associated with the security profile.
                  - **arn** *(string) --* 
                    The ARN of the security profile.
            - **nextToken** *(string) --* 
              A token that can be used to retrieve the next set of results, or ``null`` if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :type recursive: boolean
        :param recursive:
          If true, return child groups as well.
        :type securityProfileTargetArn: string
        :param securityProfileTargetArn: **[REQUIRED]**
          The ARN of the target (thing group) whose attached security profiles you want to get.
        :rtype: dict
        :returns:
        """
        pass

    def list_streams(self, maxResults: int = None, nextToken: str = None, ascendingOrder: bool = None) -> Dict:
        """
        Lists all of the streams in your AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListStreams>`_
        
        **Request Syntax**
        ::
          response = client.list_streams(
              maxResults=123,
              nextToken='string',
              ascendingOrder=True|False
          )
        
        **Response Syntax**
        ::
            {
                'streams': [
                    {
                        'streamId': 'string',
                        'streamArn': 'string',
                        'streamVersion': 123,
                        'description': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **streams** *(list) --* 
              A list of streams.
              - *(dict) --* 
                A summary of a stream.
                - **streamId** *(string) --* 
                  The stream ID.
                - **streamArn** *(string) --* 
                  The stream ARN.
                - **streamVersion** *(integer) --* 
                  The stream version.
                - **description** *(string) --* 
                  A description of the stream.
            - **nextToken** *(string) --* 
              A token used to get the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at a time.
        :type nextToken: string
        :param nextToken:
          A token used to get the next set of results.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Set to true to return the list of streams in ascending order.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, resourceArn: str, nextToken: str = None) -> Dict:
        """
        Lists the tags (metadata) you have assigned to the resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              resourceArn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tags** *(list) --* 
              The list of tags assigned to the resource.
              - *(dict) --* 
                A set of key/value pairs that are used to manage the resource.
                - **Key** *(string) --* 
                  The tag's key.
                - **Value** *(string) --* 
                  The tag's value.
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The ARN of the resource.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def list_targets_for_policy(self, policyName: str, marker: str = None, pageSize: int = None) -> Dict:
        """
        List targets for the specified policy.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTargetsForPolicy>`_
        
        **Request Syntax**
        ::
          response = client.list_targets_for_policy(
              policyName='string',
              marker='string',
              pageSize=123
          )
        
        **Response Syntax**
        ::
            {
                'targets': [
                    'string',
                ],
                'nextMarker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **targets** *(list) --* 
              The policy targets.
              - *(string) --* 
            - **nextMarker** *(string) --* 
              A marker used to get the next set of results.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
        :type marker: string
        :param marker:
          A marker used to get the next set of results.
        :type pageSize: integer
        :param pageSize:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def list_targets_for_security_profile(self, securityProfileName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the targets (thing groups) associated with a given Device Defender security profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTargetsForSecurityProfile>`_
        
        **Request Syntax**
        ::
          response = client.list_targets_for_security_profile(
              securityProfileName='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'securityProfileTargets': [
                    {
                        'arn': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileTargets** *(list) --* 
              The thing groups to which the security profile is attached.
              - *(dict) --* 
                A target to which an alert is sent when a security profile behavior is violated.
                - **arn** *(string) --* 
                  The ARN of the security profile.
            - **nextToken** *(string) --* 
              A token that can be used to retrieve the next set of results, or ``null`` if there are no additional results.
        :type securityProfileName: string
        :param securityProfileName: **[REQUIRED]**
          The security profile.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def list_thing_groups(self, nextToken: str = None, maxResults: int = None, parentGroup: str = None, namePrefixFilter: str = None, recursive: bool = None) -> Dict:
        """
        List the thing groups in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingGroups>`_
        
        **Request Syntax**
        ::
          response = client.list_thing_groups(
              nextToken='string',
              maxResults=123,
              parentGroup='string',
              namePrefixFilter='string',
              recursive=True|False
          )
        
        **Response Syntax**
        ::
            {
                'thingGroups': [
                    {
                        'groupName': 'string',
                        'groupArn': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **thingGroups** *(list) --* 
              The thing groups.
              - *(dict) --* 
                The name and ARN of a group.
                - **groupName** *(string) --* 
                  The group name.
                - **groupArn** *(string) --* 
                  The group ARN.
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :type parentGroup: string
        :param parentGroup:
          A filter that limits the results to those with the specified parent group.
        :type namePrefixFilter: string
        :param namePrefixFilter:
          A filter that limits the results to those with the specified name prefix.
        :type recursive: boolean
        :param recursive:
          If true, return child groups as well.
        :rtype: dict
        :returns:
        """
        pass

    def list_thing_groups_for_thing(self, thingName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        List the thing groups to which the specified thing belongs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingGroupsForThing>`_
        
        **Request Syntax**
        ::
          response = client.list_thing_groups_for_thing(
              thingName='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'thingGroups': [
                    {
                        'groupName': 'string',
                        'groupArn': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **thingGroups** *(list) --* 
              The thing groups.
              - *(dict) --* 
                The name and ARN of a group.
                - **groupName** *(string) --* 
                  The group name.
                - **groupArn** *(string) --* 
                  The group ARN.
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The thing name.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def list_thing_principals(self, thingName: str) -> Dict:
        """
        Lists the principals associated with the specified thing. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingPrincipals>`_
        
        **Request Syntax**
        ::
          response = client.list_thing_principals(
              thingName='string'
          )
        
        **Response Syntax**
        ::
            {
                'principals': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListThingPrincipals operation.
            - **principals** *(list) --* 
              The principals associated with the thing.
              - *(string) --* 
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing.
        :rtype: dict
        :returns:
        """
        pass

    def list_thing_registration_task_reports(self, taskId: str, reportType: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Information about the thing registration tasks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingRegistrationTaskReports>`_
        
        **Request Syntax**
        ::
          response = client.list_thing_registration_task_reports(
              taskId='string',
              reportType='ERRORS'|'RESULTS',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'resourceLinks': [
                    'string',
                ],
                'reportType': 'ERRORS'|'RESULTS',
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **resourceLinks** *(list) --* 
              Links to the task resources.
              - *(string) --* 
            - **reportType** *(string) --* 
              The type of task report.
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type taskId: string
        :param taskId: **[REQUIRED]**
          The id of the task.
        :type reportType: string
        :param reportType: **[REQUIRED]**
          The type of task report.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return per request.
        :rtype: dict
        :returns:
        """
        pass

    def list_thing_registration_tasks(self, nextToken: str = None, maxResults: int = None, status: str = None) -> Dict:
        """
        List bulk thing provisioning tasks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingRegistrationTasks>`_
        
        **Request Syntax**
        ::
          response = client.list_thing_registration_tasks(
              nextToken='string',
              maxResults=123,
              status='InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling'
          )
        
        **Response Syntax**
        ::
            {
                'taskIds': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskIds** *(list) --* 
              A list of bulk thing provisioning task IDs.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :type status: string
        :param status:
          The status of the bulk thing provisioning task.
        :rtype: dict
        :returns:
        """
        pass

    def list_thing_types(self, nextToken: str = None, maxResults: int = None, thingTypeName: str = None) -> Dict:
        """
        Lists the existing thing types.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingTypes>`_
        
        **Request Syntax**
        ::
          response = client.list_thing_types(
              nextToken='string',
              maxResults=123,
              thingTypeName='string'
          )
        
        **Response Syntax**
        ::
            {
                'thingTypes': [
                    {
                        'thingTypeName': 'string',
                        'thingTypeArn': 'string',
                        'thingTypeProperties': {
                            'thingTypeDescription': 'string',
                            'searchableAttributes': [
                                'string',
                            ]
                        },
                        'thingTypeMetadata': {
                            'deprecated': True|False,
                            'deprecationDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1)
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the ListThingTypes operation.
            - **thingTypes** *(list) --* 
              The thing types.
              - *(dict) --* 
                The definition of the thing type, including thing type name and description.
                - **thingTypeName** *(string) --* 
                  The name of the thing type.
                - **thingTypeArn** *(string) --* 
                  The thing type ARN.
                - **thingTypeProperties** *(dict) --* 
                  The ThingTypeProperties for the thing type.
                  - **thingTypeDescription** *(string) --* 
                    The description of the thing type.
                  - **searchableAttributes** *(list) --* 
                    A list of searchable thing attribute names.
                    - *(string) --* 
                - **thingTypeMetadata** *(dict) --* 
                  The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.
                  - **deprecated** *(boolean) --* 
                    Whether the thing type is deprecated. If **true** , no new things could be associated with this type.
                  - **deprecationDate** *(datetime) --* 
                    The date and time when the thing type was deprecated.
                  - **creationDate** *(datetime) --* 
                    The date and time when the thing type was created.
            - **nextToken** *(string) --* 
              The token for the next set of results, or **null** if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return in this operation.
        :type thingTypeName: string
        :param thingTypeName:
          The name of the thing type.
        :rtype: dict
        :returns:
        """
        pass

    def list_things(self, nextToken: str = None, maxResults: int = None, attributeName: str = None, attributeValue: str = None, thingTypeName: str = None) -> Dict:
        """
        Lists your things. Use the **attributeName** and **attributeValue** parameters to filter your things. For example, calling ``ListThings`` with attributeName=Color and attributeValue=Red retrieves all things in the registry that contain an attribute **Color** with the value **Red** . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThings>`_
        
        **Request Syntax**
        ::
          response = client.list_things(
              nextToken='string',
              maxResults=123,
              attributeName='string',
              attributeValue='string',
              thingTypeName='string'
          )
        
        **Response Syntax**
        ::
            {
                'things': [
                    {
                        'thingName': 'string',
                        'thingTypeName': 'string',
                        'thingArn': 'string',
                        'attributes': {
                            'string': 'string'
                        },
                        'version': 123
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListThings operation.
            - **things** *(list) --* 
              The things.
              - *(dict) --* 
                The properties of the thing, including thing name, thing type name, and a list of thing attributes.
                - **thingName** *(string) --* 
                  The name of the thing.
                - **thingTypeName** *(string) --* 
                  The name of the thing type, if the thing has been associated with a type.
                - **thingArn** *(string) --* 
                  The thing ARN.
                - **attributes** *(dict) --* 
                  A list of thing attributes which are name-value pairs.
                  - *(string) --* 
                    - *(string) --* 
                - **version** *(integer) --* 
                  The version of the thing record in the registry.
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return in this operation.
        :type attributeName: string
        :param attributeName:
          The attribute name used to search for things.
        :type attributeValue: string
        :param attributeValue:
          The attribute value used to search for things.
        :type thingTypeName: string
        :param thingTypeName:
          The name of the thing type used to search for things.
        :rtype: dict
        :returns:
        """
        pass

    def list_things_in_billing_group(self, billingGroupName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the things you have added to the given billing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingsInBillingGroup>`_
        
        **Request Syntax**
        ::
          response = client.list_things_in_billing_group(
              billingGroupName='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'things': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **things** *(list) --* 
              A list of things in the billing group.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type billingGroupName: string
        :param billingGroupName: **[REQUIRED]**
          The name of the billing group.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return per request.
        :rtype: dict
        :returns:
        """
        pass

    def list_things_in_thing_group(self, thingGroupName: str, recursive: bool = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the things in the specified group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingsInThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.list_things_in_thing_group(
              thingGroupName='string',
              recursive=True|False,
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'things': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **things** *(list) --* 
              The things in the specified thing group.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The thing group name.
        :type recursive: boolean
        :param recursive:
          When true, list things in this thing group and in all child groups as well.
        :type nextToken: string
        :param nextToken:
          The token to retrieve the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def list_topic_rules(self, topic: str = None, maxResults: int = None, nextToken: str = None, ruleDisabled: bool = None) -> Dict:
        """
        Lists the rules for the specific topic.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTopicRules>`_
        
        **Request Syntax**
        ::
          response = client.list_topic_rules(
              topic='string',
              maxResults=123,
              nextToken='string',
              ruleDisabled=True|False
          )
        
        **Response Syntax**
        ::
            {
                'rules': [
                    {
                        'ruleArn': 'string',
                        'ruleName': 'string',
                        'topicPattern': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'ruleDisabled': True|False
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListTopicRules operation.
            - **rules** *(list) --* 
              The rules.
              - *(dict) --* 
                Describes a rule.
                - **ruleArn** *(string) --* 
                  The rule ARN.
                - **ruleName** *(string) --* 
                  The name of the rule.
                - **topicPattern** *(string) --* 
                  The pattern for the topic names that apply.
                - **createdAt** *(datetime) --* 
                  The date and time the rule was created.
                - **ruleDisabled** *(boolean) --* 
                  Specifies whether the rule is disabled.
            - **nextToken** *(string) --* 
              A token used to retrieve the next value.
        :type topic: string
        :param topic:
          The topic.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return.
        :type nextToken: string
        :param nextToken:
          A token used to retrieve the next value.
        :type ruleDisabled: boolean
        :param ruleDisabled:
          Specifies whether the rule is disabled.
        :rtype: dict
        :returns:
        """
        pass

    def list_v2_logging_levels(self, targetType: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists logging levels.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListV2LoggingLevels>`_
        
        **Request Syntax**
        ::
          response = client.list_v2_logging_levels(
              targetType='DEFAULT'|'THING_GROUP',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'logTargetConfigurations': [
                    {
                        'logTarget': {
                            'targetType': 'DEFAULT'|'THING_GROUP',
                            'targetName': 'string'
                        },
                        'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **logTargetConfigurations** *(list) --* 
              The logging configuration for a target.
              - *(dict) --* 
                The target configuration.
                - **logTarget** *(dict) --* 
                  A log target
                  - **targetType** *(string) --* 
                    The target type.
                  - **targetName** *(string) --* 
                    The target name.
                - **logLevel** *(string) --* 
                  The logging level.
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
        :type targetType: string
        :param targetType:
          The type of resource for which you are configuring logging. Must be ``THING_Group`` .
        :type nextToken: string
        :param nextToken:
          The token used to get the next set of results, or **null** if there are no additional results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def list_violation_events(self, startTime: datetime, endTime: datetime, thingName: str = None, securityProfileName: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the Device Defender security profile violations discovered during the given time period. You can use filters to limit the results to those alerts issued for a particular security profile, behavior or thing (device).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListViolationEvents>`_
        
        **Request Syntax**
        ::
          response = client.list_violation_events(
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              thingName='string',
              securityProfileName='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'violationEvents': [
                    {
                        'violationId': 'string',
                        'thingName': 'string',
                        'securityProfileName': 'string',
                        'behavior': {
                            'name': 'string',
                            'metric': 'string',
                            'criteria': {
                                'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                                'value': {
                                    'count': 123,
                                    'cidrs': [
                                        'string',
                                    ],
                                    'ports': [
                                        123,
                                    ]
                                },
                                'durationSeconds': 123,
                                'consecutiveDatapointsToAlarm': 123,
                                'consecutiveDatapointsToClear': 123,
                                'statisticalThreshold': {
                                    'statistic': 'string'
                                }
                            }
                        },
                        'metricValue': {
                            'count': 123,
                            'cidrs': [
                                'string',
                            ],
                            'ports': [
                                123,
                            ]
                        },
                        'violationEventType': 'in-alarm'|'alarm-cleared'|'alarm-invalidated',
                        'violationEventTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **violationEvents** *(list) --* 
              The security profile violation alerts issued for this account during the given time frame, potentially filtered by security profile, behavior violated, or thing (device) violating.
              - *(dict) --* 
                Information about a Device Defender security profile behavior violation.
                - **violationId** *(string) --* 
                  The ID of the violation event.
                - **thingName** *(string) --* 
                  The name of the thing responsible for the violation event.
                - **securityProfileName** *(string) --* 
                  The name of the security profile whose behavior was violated.
                - **behavior** *(dict) --* 
                  The behavior which was violated.
                  - **name** *(string) --* 
                    The name you have given to the behavior.
                  - **metric** *(string) --* 
                    What is measured by the behavior.
                  - **criteria** *(dict) --* 
                    The criteria that determine if a device is behaving normally in regard to the ``metric`` .
                    - **comparisonOperator** *(string) --* 
                      The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
                    - **value** *(dict) --* 
                      The value to be compared with the ``metric`` .
                      - **count** *(integer) --* 
                        If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                      - **cidrs** *(list) --* 
                        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                        - *(string) --* 
                      - **ports** *(list) --* 
                        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                        - *(integer) --* 
                    - **durationSeconds** *(integer) --* 
                      Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
                    - **consecutiveDatapointsToAlarm** *(integer) --* 
                      If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
                    - **consecutiveDatapointsToClear** *(integer) --* 
                      If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
                    - **statisticalThreshold** *(dict) --* 
                      A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                      - **statistic** *(string) --* 
                        The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
                - **metricValue** *(dict) --* 
                  The value of the metric (the measurement).
                  - **count** *(integer) --* 
                    If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                  - **cidrs** *(list) --* 
                    If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                    - *(string) --* 
                  - **ports** *(list) --* 
                    If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                    - *(integer) --* 
                - **violationEventType** *(string) --* 
                  The type of violation event.
                - **violationEventTime** *(datetime) --* 
                  The time the violation event occurred.
            - **nextToken** *(string) --* 
              A token that can be used to retrieve the next set of results, or ``null`` if there are no additional results.
        :type startTime: datetime
        :param startTime: **[REQUIRED]**
          The start time for the alerts to be listed.
        :type endTime: datetime
        :param endTime: **[REQUIRED]**
          The end time for the alerts to be listed.
        :type thingName: string
        :param thingName:
          A filter to limit results to those alerts caused by the specified thing.
        :type securityProfileName: string
        :param securityProfileName:
          A filter to limit results to those alerts generated by the specified security profile.
        :type nextToken: string
        :param nextToken:
          The token for the next set of results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :rtype: dict
        :returns:
        """
        pass

    def register_ca_certificate(self, caCertificate: str, verificationCertificate: str, setAsActive: bool = None, allowAutoRegistration: bool = None, registrationConfig: Dict = None) -> Dict:
        """
        Registers a CA certificate with AWS IoT. This CA certificate can then be used to sign device certificates, which can be then registered with AWS IoT. You can register up to 10 CA certificates per AWS account that have the same subject field. This enables you to have up to 10 certificate authorities sign your device certificates. If you have more than one CA certificate registered, make sure you pass the CA certificate when you register your device certificates with the RegisterCertificate API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RegisterCACertificate>`_
        
        **Request Syntax**
        ::
          response = client.register_ca_certificate(
              caCertificate='string',
              verificationCertificate='string',
              setAsActive=True|False,
              allowAutoRegistration=True|False,
              registrationConfig={
                  'templateBody': 'string',
                  'roleArn': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'certificateArn': 'string',
                'certificateId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the RegisterCACertificateResponse operation.
            - **certificateArn** *(string) --* 
              The CA certificate ARN.
            - **certificateId** *(string) --* 
              The CA certificate identifier.
        :type caCertificate: string
        :param caCertificate: **[REQUIRED]**
          The CA certificate.
        :type verificationCertificate: string
        :param verificationCertificate: **[REQUIRED]**
          The private key verification certificate.
        :type setAsActive: boolean
        :param setAsActive:
          A boolean value that specifies if the CA certificate is set to active.
        :type allowAutoRegistration: boolean
        :param allowAutoRegistration:
          Allows this CA certificate to be used for auto registration of device certificates.
        :type registrationConfig: dict
        :param registrationConfig:
          Information about the registration configuration.
          - **templateBody** *(string) --*
            The template body.
          - **roleArn** *(string) --*
            The ARN of the role.
        :rtype: dict
        :returns:
        """
        pass

    def register_certificate(self, certificatePem: str, caCertificatePem: str = None, setAsActive: bool = None, status: str = None) -> Dict:
        """
        Registers a device certificate with AWS IoT. If you have more than one CA certificate that has the same subject field, you must specify the CA certificate that was used to sign the device certificate being registered.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RegisterCertificate>`_
        
        **Request Syntax**
        ::
          response = client.register_certificate(
              certificatePem='string',
              caCertificatePem='string',
              setAsActive=True|False,
              status='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
          )
        
        **Response Syntax**
        ::
            {
                'certificateArn': 'string',
                'certificateId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the RegisterCertificate operation.
            - **certificateArn** *(string) --* 
              The certificate ARN.
            - **certificateId** *(string) --* 
              The certificate identifier.
        :type certificatePem: string
        :param certificatePem: **[REQUIRED]**
          The certificate data, in PEM format.
        :type caCertificatePem: string
        :param caCertificatePem:
          The CA certificate used to sign the device certificate being registered.
        :type setAsActive: boolean
        :param setAsActive:
          A boolean value that specifies if the CA certificate is set to active.
        :type status: string
        :param status:
          The status of the register certificate request.
        :rtype: dict
        :returns:
        """
        pass

    def register_thing(self, templateBody: str, parameters: Dict = None) -> Dict:
        """
        Provisions a thing.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RegisterThing>`_
        
        **Request Syntax**
        ::
          response = client.register_thing(
              templateBody='string',
              parameters={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'certificatePem': 'string',
                'resourceArns': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **certificatePem** *(string) --* 
              .
            - **resourceArns** *(dict) --* 
              ARNs for the generated resources.
              - *(string) --* 
                - *(string) --* 
        :type templateBody: string
        :param templateBody: **[REQUIRED]**
          The provisioning template. See `Programmatic Provisioning <https://docs.aws.amazon.com/iot/latest/developerguide/programmatic-provisioning.html>`__ for more information.
        :type parameters: dict
        :param parameters:
          The parameters for provisioning a thing. See `Programmatic Provisioning <https://docs.aws.amazon.com/iot/latest/developerguide/programmatic-provisioning.html>`__ for more information.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def reject_certificate_transfer(self, certificateId: str, rejectReason: str = None):
        """
        Rejects a pending certificate transfer. After AWS IoT rejects a certificate transfer, the certificate status changes from **PENDING_TRANSFER** to **INACTIVE** .
        To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.
        This operation can only be called by the transfer destination. After it is called, the certificate will be returned to the source's account in the INACTIVE state.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RejectCertificateTransfer>`_
        
        **Request Syntax**
        ::
          response = client.reject_certificate_transfer(
              certificateId='string',
              rejectReason='string'
          )
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        :type rejectReason: string
        :param rejectReason:
          The reason the certificate transfer was rejected.
        :returns: None
        """
        pass

    def remove_thing_from_billing_group(self, billingGroupName: str = None, billingGroupArn: str = None, thingName: str = None, thingArn: str = None) -> Dict:
        """
        Removes the given thing from the billing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RemoveThingFromBillingGroup>`_
        
        **Request Syntax**
        ::
          response = client.remove_thing_from_billing_group(
              billingGroupName='string',
              billingGroupArn='string',
              thingName='string',
              thingArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type billingGroupName: string
        :param billingGroupName:
          The name of the billing group.
        :type billingGroupArn: string
        :param billingGroupArn:
          The ARN of the billing group.
        :type thingName: string
        :param thingName:
          The name of the thing to be removed from the billing group.
        :type thingArn: string
        :param thingArn:
          The ARN of the thing to be removed from the billing group.
        :rtype: dict
        :returns:
        """
        pass

    def remove_thing_from_thing_group(self, thingGroupName: str = None, thingGroupArn: str = None, thingName: str = None, thingArn: str = None) -> Dict:
        """
        Remove the specified thing from the specified group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RemoveThingFromThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.remove_thing_from_thing_group(
              thingGroupName='string',
              thingGroupArn='string',
              thingName='string',
              thingArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type thingGroupName: string
        :param thingGroupName:
          The group name.
        :type thingGroupArn: string
        :param thingGroupArn:
          The group ARN.
        :type thingName: string
        :param thingName:
          The name of the thing to remove from the group.
        :type thingArn: string
        :param thingArn:
          The ARN of the thing to remove from the group.
        :rtype: dict
        :returns:
        """
        pass

    def replace_topic_rule(self, ruleName: str, topicRulePayload: Dict):
        """
        Replaces the rule. You must specify all parameters for the new rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ReplaceTopicRule>`_
        
        **Request Syntax**
        ::
          response = client.replace_topic_rule(
              ruleName='string',
              topicRulePayload={
                  'sql': 'string',
                  'description': 'string',
                  'actions': [
                      {
                          'dynamoDB': {
                              'tableName': 'string',
                              'roleArn': 'string',
                              'operation': 'string',
                              'hashKeyField': 'string',
                              'hashKeyValue': 'string',
                              'hashKeyType': 'STRING'|'NUMBER',
                              'rangeKeyField': 'string',
                              'rangeKeyValue': 'string',
                              'rangeKeyType': 'STRING'|'NUMBER',
                              'payloadField': 'string'
                          },
                          'dynamoDBv2': {
                              'roleArn': 'string',
                              'putItem': {
                                  'tableName': 'string'
                              }
                          },
                          'lambda': {
                              'functionArn': 'string'
                          },
                          'sns': {
                              'targetArn': 'string',
                              'roleArn': 'string',
                              'messageFormat': 'RAW'|'JSON'
                          },
                          'sqs': {
                              'roleArn': 'string',
                              'queueUrl': 'string',
                              'useBase64': True|False
                          },
                          'kinesis': {
                              'roleArn': 'string',
                              'streamName': 'string',
                              'partitionKey': 'string'
                          },
                          'republish': {
                              'roleArn': 'string',
                              'topic': 'string'
                          },
                          's3': {
                              'roleArn': 'string',
                              'bucketName': 'string',
                              'key': 'string',
                              'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                          },
                          'firehose': {
                              'roleArn': 'string',
                              'deliveryStreamName': 'string',
                              'separator': 'string'
                          },
                          'cloudwatchMetric': {
                              'roleArn': 'string',
                              'metricNamespace': 'string',
                              'metricName': 'string',
                              'metricValue': 'string',
                              'metricUnit': 'string',
                              'metricTimestamp': 'string'
                          },
                          'cloudwatchAlarm': {
                              'roleArn': 'string',
                              'alarmName': 'string',
                              'stateReason': 'string',
                              'stateValue': 'string'
                          },
                          'elasticsearch': {
                              'roleArn': 'string',
                              'endpoint': 'string',
                              'index': 'string',
                              'type': 'string',
                              'id': 'string'
                          },
                          'salesforce': {
                              'token': 'string',
                              'url': 'string'
                          },
                          'iotAnalytics': {
                              'channelArn': 'string',
                              'channelName': 'string',
                              'roleArn': 'string'
                          },
                          'iotEvents': {
                              'inputName': 'string',
                              'messageId': 'string',
                              'roleArn': 'string'
                          },
                          'stepFunctions': {
                              'executionNamePrefix': 'string',
                              'stateMachineName': 'string',
                              'roleArn': 'string'
                          }
                      },
                  ],
                  'ruleDisabled': True|False,
                  'awsIotSqlVersion': 'string',
                  'errorAction': {
                      'dynamoDB': {
                          'tableName': 'string',
                          'roleArn': 'string',
                          'operation': 'string',
                          'hashKeyField': 'string',
                          'hashKeyValue': 'string',
                          'hashKeyType': 'STRING'|'NUMBER',
                          'rangeKeyField': 'string',
                          'rangeKeyValue': 'string',
                          'rangeKeyType': 'STRING'|'NUMBER',
                          'payloadField': 'string'
                      },
                      'dynamoDBv2': {
                          'roleArn': 'string',
                          'putItem': {
                              'tableName': 'string'
                          }
                      },
                      'lambda': {
                          'functionArn': 'string'
                      },
                      'sns': {
                          'targetArn': 'string',
                          'roleArn': 'string',
                          'messageFormat': 'RAW'|'JSON'
                      },
                      'sqs': {
                          'roleArn': 'string',
                          'queueUrl': 'string',
                          'useBase64': True|False
                      },
                      'kinesis': {
                          'roleArn': 'string',
                          'streamName': 'string',
                          'partitionKey': 'string'
                      },
                      'republish': {
                          'roleArn': 'string',
                          'topic': 'string'
                      },
                      's3': {
                          'roleArn': 'string',
                          'bucketName': 'string',
                          'key': 'string',
                          'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                      },
                      'firehose': {
                          'roleArn': 'string',
                          'deliveryStreamName': 'string',
                          'separator': 'string'
                      },
                      'cloudwatchMetric': {
                          'roleArn': 'string',
                          'metricNamespace': 'string',
                          'metricName': 'string',
                          'metricValue': 'string',
                          'metricUnit': 'string',
                          'metricTimestamp': 'string'
                      },
                      'cloudwatchAlarm': {
                          'roleArn': 'string',
                          'alarmName': 'string',
                          'stateReason': 'string',
                          'stateValue': 'string'
                      },
                      'elasticsearch': {
                          'roleArn': 'string',
                          'endpoint': 'string',
                          'index': 'string',
                          'type': 'string',
                          'id': 'string'
                      },
                      'salesforce': {
                          'token': 'string',
                          'url': 'string'
                      },
                      'iotAnalytics': {
                          'channelArn': 'string',
                          'channelName': 'string',
                          'roleArn': 'string'
                      },
                      'iotEvents': {
                          'inputName': 'string',
                          'messageId': 'string',
                          'roleArn': 'string'
                      },
                      'stepFunctions': {
                          'executionNamePrefix': 'string',
                          'stateMachineName': 'string',
                          'roleArn': 'string'
                      }
                  }
              }
          )
        :type ruleName: string
        :param ruleName: **[REQUIRED]**
          The name of the rule.
        :type topicRulePayload: dict
        :param topicRulePayload: **[REQUIRED]**
          The rule payload.
          - **sql** *(string) --* **[REQUIRED]**
            The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference>`__ in the *AWS IoT Developer Guide* .
          - **description** *(string) --*
            The description of the rule.
          - **actions** *(list) --* **[REQUIRED]**
            The actions associated with the rule.
            - *(dict) --*
              Describes the actions associated with a rule.
              - **dynamoDB** *(dict) --*
                Write to a DynamoDB table.
                - **tableName** *(string) --* **[REQUIRED]**
                  The name of the DynamoDB table.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access to the DynamoDB table.
                - **operation** *(string) --*
                  The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .
                - **hashKeyField** *(string) --* **[REQUIRED]**
                  The hash key name.
                - **hashKeyValue** *(string) --* **[REQUIRED]**
                  The hash key value.
                - **hashKeyType** *(string) --*
                  The hash key type. Valid values are \"STRING\" or \"NUMBER\"
                - **rangeKeyField** *(string) --*
                  The range key name.
                - **rangeKeyValue** *(string) --*
                  The range key value.
                - **rangeKeyType** *(string) --*
                  The range key type. Valid values are \"STRING\" or \"NUMBER\"
                - **payloadField** *(string) --*
                  The action payload. This name can be customized.
              - **dynamoDBv2** *(dict) --*
                Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access to the DynamoDB table.
                - **putItem** *(dict) --* **[REQUIRED]**
                  Specifies the DynamoDB table to which the message data will be written. For example:
                   ``{ \"dynamoDBv2\": { \"roleArn\": \"aws:iam:12341251:my-role\" \"putItem\": { \"tableName\": \"my-table\" } } }``
                  Each attribute in the message payload will be written to a separate column in the DynamoDB database.
                  - **tableName** *(string) --* **[REQUIRED]**
                    The table where the message data will be written
              - **lambda** *(dict) --*
                Invoke a Lambda function.
                - **functionArn** *(string) --* **[REQUIRED]**
                  The ARN of the Lambda function.
              - **sns** *(dict) --*
                Publish to an Amazon SNS topic.
                - **targetArn** *(string) --* **[REQUIRED]**
                  The ARN of the SNS topic.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access.
                - **messageFormat** *(string) --*
                  (Optional) The message format of the message to publish. Accepted values are \"JSON\" and \"RAW\". The default value of the attribute is \"RAW\". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `https\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.
              - **sqs** *(dict) --*
                Publish to an Amazon SQS queue.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access.
                - **queueUrl** *(string) --* **[REQUIRED]**
                  The URL of the Amazon SQS queue.
                - **useBase64** *(boolean) --*
                  Specifies whether to use Base64 encoding.
              - **kinesis** *(dict) --*
                Write data to an Amazon Kinesis stream.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access to the Amazon Kinesis stream.
                - **streamName** *(string) --* **[REQUIRED]**
                  The name of the Amazon Kinesis stream.
                - **partitionKey** *(string) --*
                  The partition key.
              - **republish** *(dict) --*
                Publish to another MQTT topic.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access.
                - **topic** *(string) --* **[REQUIRED]**
                  The name of the MQTT topic.
              - **s3** *(dict) --*
                Write to an Amazon S3 bucket.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the IAM role that grants access.
                - **bucketName** *(string) --* **[REQUIRED]**
                  The Amazon S3 bucket.
                - **key** *(string) --* **[REQUIRED]**
                  The object key.
                - **cannedAcl** *(string) --*
                  The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
              - **firehose** *(dict) --*
                Write to an Amazon Kinesis Firehose stream.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The IAM role that grants access to the Amazon Kinesis Firehose stream.
                - **deliveryStreamName** *(string) --* **[REQUIRED]**
                  The delivery stream name.
                - **separator** *(string) --*
                  A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'\n\' (newline), \'\t\' (tab), \'\r\n\' (Windows newline), \',\' (comma).
              - **cloudwatchMetric** *(dict) --*
                Capture a CloudWatch metric.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The IAM role that allows access to the CloudWatch metric.
                - **metricNamespace** *(string) --* **[REQUIRED]**
                  The CloudWatch metric namespace name.
                - **metricName** *(string) --* **[REQUIRED]**
                  The CloudWatch metric name.
                - **metricValue** *(string) --* **[REQUIRED]**
                  The CloudWatch metric value.
                - **metricUnit** *(string) --* **[REQUIRED]**
                  The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.
                - **metricTimestamp** *(string) --*
                  An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .
              - **cloudwatchAlarm** *(dict) --*
                Change the state of a CloudWatch alarm.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The IAM role that allows access to the CloudWatch alarm.
                - **alarmName** *(string) --* **[REQUIRED]**
                  The CloudWatch alarm name.
                - **stateReason** *(string) --* **[REQUIRED]**
                  The reason for the alarm change.
                - **stateValue** *(string) --* **[REQUIRED]**
                  The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
              - **elasticsearch** *(dict) --*
                Write data to an Amazon Elasticsearch Service domain.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The IAM role ARN that has access to Elasticsearch.
                - **endpoint** *(string) --* **[REQUIRED]**
                  The endpoint of your Elasticsearch domain.
                - **index** *(string) --* **[REQUIRED]**
                  The Elasticsearch index where you want to store your data.
                - **type** *(string) --* **[REQUIRED]**
                  The type of document you are storing.
                - **id** *(string) --* **[REQUIRED]**
                  The unique identifier for the document you are storing.
              - **salesforce** *(dict) --*
                Send a message to a Salesforce IoT Cloud Input Stream.
                - **token** *(string) --* **[REQUIRED]**
                  The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
                - **url** *(string) --* **[REQUIRED]**
                  The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
              - **iotAnalytics** *(dict) --*
                Sends message data to an AWS IoT Analytics channel.
                - **channelArn** *(string) --*
                  (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
                - **channelName** *(string) --*
                  The name of the IoT Analytics channel to which message data will be sent.
                - **roleArn** *(string) --*
                  The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
              - **iotEvents** *(dict) --*
                Sends an input to an AWS IoT Events detector.
                - **inputName** *(string) --* **[REQUIRED]**
                  The name of the AWS IoT Events input.
                - **messageId** *(string) --*
                  [Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. (\"Action\":\"iotevents:BatchPutMessage\").
              - **stepFunctions** *(dict) --*
                Starts execution of a Step Functions state machine.
                - **executionNamePrefix** *(string) --*
                  (Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
                - **stateMachineName** *(string) --* **[REQUIRED]**
                  The name of the Step Functions state machine whose execution will be started.
                - **roleArn** *(string) --* **[REQUIRED]**
                  The ARN of the role that grants IoT permission to start execution of a state machine (\"Action\":\"states:StartExecution\").
          - **ruleDisabled** *(boolean) --*
            Specifies whether the rule is disabled.
          - **awsIotSqlVersion** *(string) --*
            The version of the SQL rules engine to use when evaluating the rule.
          - **errorAction** *(dict) --*
            The action to take when an error occurs.
            - **dynamoDB** *(dict) --*
              Write to a DynamoDB table.
              - **tableName** *(string) --* **[REQUIRED]**
                The name of the DynamoDB table.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access to the DynamoDB table.
              - **operation** *(string) --*
                The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .
              - **hashKeyField** *(string) --* **[REQUIRED]**
                The hash key name.
              - **hashKeyValue** *(string) --* **[REQUIRED]**
                The hash key value.
              - **hashKeyType** *(string) --*
                The hash key type. Valid values are \"STRING\" or \"NUMBER\"
              - **rangeKeyField** *(string) --*
                The range key name.
              - **rangeKeyValue** *(string) --*
                The range key value.
              - **rangeKeyType** *(string) --*
                The range key type. Valid values are \"STRING\" or \"NUMBER\"
              - **payloadField** *(string) --*
                The action payload. This name can be customized.
            - **dynamoDBv2** *(dict) --*
              Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access to the DynamoDB table.
              - **putItem** *(dict) --* **[REQUIRED]**
                Specifies the DynamoDB table to which the message data will be written. For example:
                 ``{ \"dynamoDBv2\": { \"roleArn\": \"aws:iam:12341251:my-role\" \"putItem\": { \"tableName\": \"my-table\" } } }``
                Each attribute in the message payload will be written to a separate column in the DynamoDB database.
                - **tableName** *(string) --* **[REQUIRED]**
                  The table where the message data will be written
            - **lambda** *(dict) --*
              Invoke a Lambda function.
              - **functionArn** *(string) --* **[REQUIRED]**
                The ARN of the Lambda function.
            - **sns** *(dict) --*
              Publish to an Amazon SNS topic.
              - **targetArn** *(string) --* **[REQUIRED]**
                The ARN of the SNS topic.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access.
              - **messageFormat** *(string) --*
                (Optional) The message format of the message to publish. Accepted values are \"JSON\" and \"RAW\". The default value of the attribute is \"RAW\". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `https\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.
            - **sqs** *(dict) --*
              Publish to an Amazon SQS queue.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access.
              - **queueUrl** *(string) --* **[REQUIRED]**
                The URL of the Amazon SQS queue.
              - **useBase64** *(boolean) --*
                Specifies whether to use Base64 encoding.
            - **kinesis** *(dict) --*
              Write data to an Amazon Kinesis stream.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access to the Amazon Kinesis stream.
              - **streamName** *(string) --* **[REQUIRED]**
                The name of the Amazon Kinesis stream.
              - **partitionKey** *(string) --*
                The partition key.
            - **republish** *(dict) --*
              Publish to another MQTT topic.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access.
              - **topic** *(string) --* **[REQUIRED]**
                The name of the MQTT topic.
            - **s3** *(dict) --*
              Write to an Amazon S3 bucket.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the IAM role that grants access.
              - **bucketName** *(string) --* **[REQUIRED]**
                The Amazon S3 bucket.
              - **key** *(string) --* **[REQUIRED]**
                The object key.
              - **cannedAcl** *(string) --*
                The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
            - **firehose** *(dict) --*
              Write to an Amazon Kinesis Firehose stream.
              - **roleArn** *(string) --* **[REQUIRED]**
                The IAM role that grants access to the Amazon Kinesis Firehose stream.
              - **deliveryStreamName** *(string) --* **[REQUIRED]**
                The delivery stream name.
              - **separator** *(string) --*
                A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'\n\' (newline), \'\t\' (tab), \'\r\n\' (Windows newline), \',\' (comma).
            - **cloudwatchMetric** *(dict) --*
              Capture a CloudWatch metric.
              - **roleArn** *(string) --* **[REQUIRED]**
                The IAM role that allows access to the CloudWatch metric.
              - **metricNamespace** *(string) --* **[REQUIRED]**
                The CloudWatch metric namespace name.
              - **metricName** *(string) --* **[REQUIRED]**
                The CloudWatch metric name.
              - **metricValue** *(string) --* **[REQUIRED]**
                The CloudWatch metric value.
              - **metricUnit** *(string) --* **[REQUIRED]**
                The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.
              - **metricTimestamp** *(string) --*
                An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .
            - **cloudwatchAlarm** *(dict) --*
              Change the state of a CloudWatch alarm.
              - **roleArn** *(string) --* **[REQUIRED]**
                The IAM role that allows access to the CloudWatch alarm.
              - **alarmName** *(string) --* **[REQUIRED]**
                The CloudWatch alarm name.
              - **stateReason** *(string) --* **[REQUIRED]**
                The reason for the alarm change.
              - **stateValue** *(string) --* **[REQUIRED]**
                The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            - **elasticsearch** *(dict) --*
              Write data to an Amazon Elasticsearch Service domain.
              - **roleArn** *(string) --* **[REQUIRED]**
                The IAM role ARN that has access to Elasticsearch.
              - **endpoint** *(string) --* **[REQUIRED]**
                The endpoint of your Elasticsearch domain.
              - **index** *(string) --* **[REQUIRED]**
                The Elasticsearch index where you want to store your data.
              - **type** *(string) --* **[REQUIRED]**
                The type of document you are storing.
              - **id** *(string) --* **[REQUIRED]**
                The unique identifier for the document you are storing.
            - **salesforce** *(dict) --*
              Send a message to a Salesforce IoT Cloud Input Stream.
              - **token** *(string) --* **[REQUIRED]**
                The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
              - **url** *(string) --* **[REQUIRED]**
                The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            - **iotAnalytics** *(dict) --*
              Sends message data to an AWS IoT Analytics channel.
              - **channelArn** *(string) --*
                (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
              - **channelName** *(string) --*
                The name of the IoT Analytics channel to which message data will be sent.
              - **roleArn** *(string) --*
                The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
            - **iotEvents** *(dict) --*
              Sends an input to an AWS IoT Events detector.
              - **inputName** *(string) --* **[REQUIRED]**
                The name of the AWS IoT Events input.
              - **messageId** *(string) --*
                [Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. (\"Action\":\"iotevents:BatchPutMessage\").
            - **stepFunctions** *(dict) --*
              Starts execution of a Step Functions state machine.
              - **executionNamePrefix** *(string) --*
                (Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
              - **stateMachineName** *(string) --* **[REQUIRED]**
                The name of the Step Functions state machine whose execution will be started.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the role that grants IoT permission to start execution of a state machine (\"Action\":\"states:StartExecution\").
        :returns: None
        """
        pass

    def search_index(self, queryString: str, indexName: str = None, nextToken: str = None, maxResults: int = None, queryVersion: str = None) -> Dict:
        """
        The query search index.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SearchIndex>`_
        
        **Request Syntax**
        ::
          response = client.search_index(
              indexName='string',
              queryString='string',
              nextToken='string',
              maxResults=123,
              queryVersion='string'
          )
        
        **Response Syntax**
        ::
            {
                'nextToken': 'string',
                'things': [
                    {
                        'thingName': 'string',
                        'thingId': 'string',
                        'thingTypeName': 'string',
                        'thingGroupNames': [
                            'string',
                        ],
                        'attributes': {
                            'string': 'string'
                        },
                        'shadow': 'string',
                        'connectivity': {
                            'connected': True|False,
                            'timestamp': 123
                        }
                    },
                ],
                'thingGroups': [
                    {
                        'thingGroupName': 'string',
                        'thingGroupId': 'string',
                        'thingGroupDescription': 'string',
                        'attributes': {
                            'string': 'string'
                        },
                        'parentGroupNames': [
                            'string',
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **nextToken** *(string) --* 
              The token used to get the next set of results, or **null** if there are no additional results.
            - **things** *(list) --* 
              The things that match the search query.
              - *(dict) --* 
                The thing search index document.
                - **thingName** *(string) --* 
                  The thing name.
                - **thingId** *(string) --* 
                  The thing ID.
                - **thingTypeName** *(string) --* 
                  The thing type name.
                - **thingGroupNames** *(list) --* 
                  Thing group names.
                  - *(string) --* 
                - **attributes** *(dict) --* 
                  The attributes.
                  - *(string) --* 
                    - *(string) --* 
                - **shadow** *(string) --* 
                  The shadow.
                - **connectivity** *(dict) --* 
                  Indicates whether or not the thing is connected to the AWS IoT service.
                  - **connected** *(boolean) --* 
                    True if the thing is connected to the AWS IoT service, false if it is not connected.
                  - **timestamp** *(integer) --* 
                    The epoch time (in milliseconds) when the thing last connected or disconnected. Note that if the thing has been disconnected for more than a few weeks, the time value can be missing.
            - **thingGroups** *(list) --* 
              The thing groups that match the search query.
              - *(dict) --* 
                The thing group search index document.
                - **thingGroupName** *(string) --* 
                  The thing group name.
                - **thingGroupId** *(string) --* 
                  The thing group ID.
                - **thingGroupDescription** *(string) --* 
                  The thing group description.
                - **attributes** *(dict) --* 
                  The thing group attributes.
                  - *(string) --* 
                    - *(string) --* 
                - **parentGroupNames** *(list) --* 
                  Parent group names.
                  - *(string) --* 
        :type indexName: string
        :param indexName:
          The search index name.
        :type queryString: string
        :param queryString: **[REQUIRED]**
          The search query string.
        :type nextToken: string
        :param nextToken:
          The token used to get the next set of results, or **null** if there are no additional results.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results to return at one time.
        :type queryVersion: string
        :param queryVersion:
          The query version.
        :rtype: dict
        :returns:
        """
        pass

    def set_default_authorizer(self, authorizerName: str) -> Dict:
        """
        Sets the default authorizer. This will be used if a websocket connection is made without specifying an authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetDefaultAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.set_default_authorizer(
              authorizerName='string'
          )
        
        **Response Syntax**
        ::
            {
                'authorizerName': 'string',
                'authorizerArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **authorizerName** *(string) --* 
              The authorizer name.
            - **authorizerArn** *(string) --* 
              The authorizer ARN.
        :type authorizerName: string
        :param authorizerName: **[REQUIRED]**
          The authorizer name.
        :rtype: dict
        :returns:
        """
        pass

    def set_default_policy_version(self, policyName: str, policyVersionId: str):
        """
        Sets the specified version of the specified policy as the policy's default (operative) version. This action affects all certificates to which the policy is attached. To list the principals the policy is attached to, use the ListPrincipalPolicy API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetDefaultPolicyVersion>`_
        
        **Request Syntax**
        ::
          response = client.set_default_policy_version(
              policyName='string',
              policyVersionId='string'
          )
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
        :type policyVersionId: string
        :param policyVersionId: **[REQUIRED]**
          The policy version ID.
        :returns: None
        """
        pass

    def set_logging_options(self, loggingOptionsPayload: Dict):
        """
        Sets the logging options.
        NOTE: use of this command is not recommended. Use ``SetV2LoggingOptions`` instead.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetLoggingOptions>`_
        
        **Request Syntax**
        ::
          response = client.set_logging_options(
              loggingOptionsPayload={
                  'roleArn': 'string',
                  'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
              }
          )
        :type loggingOptionsPayload: dict
        :param loggingOptionsPayload: **[REQUIRED]**
          The logging options payload.
          - **roleArn** *(string) --* **[REQUIRED]**
            The ARN of the IAM role that grants access.
          - **logLevel** *(string) --*
            The log level.
        :returns: None
        """
        pass

    def set_v2_logging_level(self, logTarget: Dict, logLevel: str):
        """
        Sets the logging level.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetV2LoggingLevel>`_
        
        **Request Syntax**
        ::
          response = client.set_v2_logging_level(
              logTarget={
                  'targetType': 'DEFAULT'|'THING_GROUP',
                  'targetName': 'string'
              },
              logLevel='DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
          )
        :type logTarget: dict
        :param logTarget: **[REQUIRED]**
          The log target.
          - **targetType** *(string) --* **[REQUIRED]**
            The target type.
          - **targetName** *(string) --*
            The target name.
        :type logLevel: string
        :param logLevel: **[REQUIRED]**
          The log level.
        :returns: None
        """
        pass

    def set_v2_logging_options(self, roleArn: str = None, defaultLogLevel: str = None, disableAllLogs: bool = None):
        """
        Sets the logging options for the V2 logging service.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetV2LoggingOptions>`_
        
        **Request Syntax**
        ::
          response = client.set_v2_logging_options(
              roleArn='string',
              defaultLogLevel='DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
              disableAllLogs=True|False
          )
        :type roleArn: string
        :param roleArn:
          The ARN of the role that allows IoT to write to Cloudwatch logs.
        :type defaultLogLevel: string
        :param defaultLogLevel:
          The default logging level.
        :type disableAllLogs: boolean
        :param disableAllLogs:
          If true all logs are disabled. The default is false.
        :returns: None
        """
        pass

    def start_on_demand_audit_task(self, targetCheckNames: List) -> Dict:
        """
        Starts an on-demand Device Defender audit.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/StartOnDemandAuditTask>`_
        
        **Request Syntax**
        ::
          response = client.start_on_demand_audit_task(
              targetCheckNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'taskId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskId** *(string) --* 
              The ID of the on-demand audit you started.
        :type targetCheckNames: list
        :param targetCheckNames: **[REQUIRED]**
          Which checks are performed during the audit. The checks you specify must be enabled for your account or an exception occurs. Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.
          - *(string) --*
            An audit check name. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
        :rtype: dict
        :returns:
        """
        pass

    def start_thing_registration_task(self, templateBody: str, inputFileBucket: str, inputFileKey: str, roleArn: str) -> Dict:
        """
        Creates a bulk thing provisioning task.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/StartThingRegistrationTask>`_
        
        **Request Syntax**
        ::
          response = client.start_thing_registration_task(
              templateBody='string',
              inputFileBucket='string',
              inputFileKey='string',
              roleArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'taskId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskId** *(string) --* 
              The bulk thing provisioning task ID.
        :type templateBody: string
        :param templateBody: **[REQUIRED]**
          The provisioning template.
        :type inputFileBucket: string
        :param inputFileBucket: **[REQUIRED]**
          The S3 bucket that contains the input file.
        :type inputFileKey: string
        :param inputFileKey: **[REQUIRED]**
          The name of input file within the S3 bucket. This file contains a newline delimited JSON file. Each line contains the parameter values to provision one device (thing).
        :type roleArn: string
        :param roleArn: **[REQUIRED]**
          The IAM role ARN that grants permission the input file.
        :rtype: dict
        :returns:
        """
        pass

    def stop_thing_registration_task(self, taskId: str) -> Dict:
        """
        Cancels a bulk thing provisioning task.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/StopThingRegistrationTask>`_
        
        **Request Syntax**
        ::
          response = client.stop_thing_registration_task(
              taskId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type taskId: string
        :param taskId: **[REQUIRED]**
          The bulk thing provisioning task ID.
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, resourceArn: str, tags: List) -> Dict:
        """
        Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              resourceArn='string',
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The ARN of the resource.
        :type tags: list
        :param tags: **[REQUIRED]**
          The new or modified tags for the resource.
          - *(dict) --*
            A set of key/value pairs that are used to manage the resource.
            - **Key** *(string) --*
              The tag\'s key.
            - **Value** *(string) --*
              The tag\'s value.
        :rtype: dict
        :returns:
        """
        pass

    def test_authorization(self, authInfos: List, principal: str = None, cognitoIdentityPoolId: str = None, clientId: str = None, policyNamesToAdd: List = None, policyNamesToSkip: List = None) -> Dict:
        """
        Tests if a specified principal is authorized to perform an AWS IoT action on a specified resource. Use this to test and debug the authorization behavior of devices that connect to the AWS IoT device gateway.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/TestAuthorization>`_
        
        **Request Syntax**
        ::
          response = client.test_authorization(
              principal='string',
              cognitoIdentityPoolId='string',
              authInfos=[
                  {
                      'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                      'resources': [
                          'string',
                      ]
                  },
              ],
              clientId='string',
              policyNamesToAdd=[
                  'string',
              ],
              policyNamesToSkip=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'authResults': [
                    {
                        'authInfo': {
                            'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                            'resources': [
                                'string',
                            ]
                        },
                        'allowed': {
                            'policies': [
                                {
                                    'policyName': 'string',
                                    'policyArn': 'string'
                                },
                            ]
                        },
                        'denied': {
                            'implicitDeny': {
                                'policies': [
                                    {
                                        'policyName': 'string',
                                        'policyArn': 'string'
                                    },
                                ]
                            },
                            'explicitDeny': {
                                'policies': [
                                    {
                                        'policyName': 'string',
                                        'policyArn': 'string'
                                    },
                                ]
                            }
                        },
                        'authDecision': 'ALLOWED'|'EXPLICIT_DENY'|'IMPLICIT_DENY',
                        'missingContextValues': [
                            'string',
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **authResults** *(list) --* 
              The authentication results.
              - *(dict) --* 
                The authorizer result.
                - **authInfo** *(dict) --* 
                  Authorization information.
                  - **actionType** *(string) --* 
                    The type of action for which the principal is being authorized.
                  - **resources** *(list) --* 
                    The resources for which the principal is being authorized to perform the specified action.
                    - *(string) --* 
                - **allowed** *(dict) --* 
                  The policies and statements that allowed the specified action.
                  - **policies** *(list) --* 
                    A list of policies that allowed the authentication.
                    - *(dict) --* 
                      Describes an AWS IoT policy.
                      - **policyName** *(string) --* 
                        The policy name.
                      - **policyArn** *(string) --* 
                        The policy ARN.
                - **denied** *(dict) --* 
                  The policies and statements that denied the specified action.
                  - **implicitDeny** *(dict) --* 
                    Information that implicitly denies the authorization. When a policy doesn't explicitly deny or allow an action on a resource it is considered an implicit deny.
                    - **policies** *(list) --* 
                      Policies that don't contain a matching allow or deny statement for the specified action on the specified resource. 
                      - *(dict) --* 
                        Describes an AWS IoT policy.
                        - **policyName** *(string) --* 
                          The policy name.
                        - **policyArn** *(string) --* 
                          The policy ARN.
                  - **explicitDeny** *(dict) --* 
                    Information that explicitly denies the authorization. 
                    - **policies** *(list) --* 
                      The policies that denied the authorization.
                      - *(dict) --* 
                        Describes an AWS IoT policy.
                        - **policyName** *(string) --* 
                          The policy name.
                        - **policyArn** *(string) --* 
                          The policy ARN.
                - **authDecision** *(string) --* 
                  The final authorization decision of this scenario. Multiple statements are taken into account when determining the authorization decision. An explicit deny statement can override multiple allow statements.
                - **missingContextValues** *(list) --* 
                  Contains any missing context values found while evaluating policy.
                  - *(string) --* 
        :type principal: string
        :param principal:
          The principal.
        :type cognitoIdentityPoolId: string
        :param cognitoIdentityPoolId:
          The Cognito identity pool ID.
        :type authInfos: list
        :param authInfos: **[REQUIRED]**
          A list of authorization info objects. Simulating authorization will create a response for each ``authInfo`` object in the list.
          - *(dict) --*
            A collection of authorization information.
            - **actionType** *(string) --*
              The type of action for which the principal is being authorized.
            - **resources** *(list) --*
              The resources for which the principal is being authorized to perform the specified action.
              - *(string) --*
        :type clientId: string
        :param clientId:
          The MQTT client ID.
        :type policyNamesToAdd: list
        :param policyNamesToAdd:
          When testing custom authorization, the policies specified here are treated as if they are attached to the principal being authorized.
          - *(string) --*
        :type policyNamesToSkip: list
        :param policyNamesToSkip:
          When testing custom authorization, the policies specified here are treated as if they are not attached to the principal being authorized.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def test_invoke_authorizer(self, authorizerName: str, token: str, tokenSignature: str) -> Dict:
        """
        Tests a custom authorization behavior by invoking a specified custom authorizer. Use this to test and debug the custom authorization behavior of devices that connect to the AWS IoT device gateway.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/TestInvokeAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.test_invoke_authorizer(
              authorizerName='string',
              token='string',
              tokenSignature='string'
          )
        
        **Response Syntax**
        ::
            {
                'isAuthenticated': True|False,
                'principalId': 'string',
                'policyDocuments': [
                    'string',
                ],
                'refreshAfterInSeconds': 123,
                'disconnectAfterInSeconds': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **isAuthenticated** *(boolean) --* 
              True if the token is authenticated, otherwise false.
            - **principalId** *(string) --* 
              The principal ID.
            - **policyDocuments** *(list) --* 
              IAM policy documents.
              - *(string) --* 
            - **refreshAfterInSeconds** *(integer) --* 
              The number of seconds after which the temporary credentials are refreshed.
            - **disconnectAfterInSeconds** *(integer) --* 
              The number of seconds after which the connection is terminated.
        :type authorizerName: string
        :param authorizerName: **[REQUIRED]**
          The custom authorizer name.
        :type token: string
        :param token: **[REQUIRED]**
          The token returned by your custom authentication service.
        :type tokenSignature: string
        :param tokenSignature: **[REQUIRED]**
          The signature made with the token and your custom authentication service\'s private key.
        :rtype: dict
        :returns:
        """
        pass

    def transfer_certificate(self, certificateId: str, targetAwsAccount: str, transferMessage: str = None) -> Dict:
        """
        Transfers the specified certificate to the specified AWS account.
        You can cancel the transfer until it is acknowledged by the recipient.
        No notification is sent to the transfer destination's account. It is up to the caller to notify the transfer target.
        The certificate being transferred must not be in the ACTIVE state. You can use the UpdateCertificate API to deactivate it.
        The certificate must not have any policies attached to it. You can use the DetachPrincipalPolicy API to detach them.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/TransferCertificate>`_
        
        **Request Syntax**
        ::
          response = client.transfer_certificate(
              certificateId='string',
              targetAwsAccount='string',
              transferMessage='string'
          )
        
        **Response Syntax**
        ::
            {
                'transferredCertificateArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the TransferCertificate operation.
            - **transferredCertificateArn** *(string) --* 
              The ARN of the certificate.
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        :type targetAwsAccount: string
        :param targetAwsAccount: **[REQUIRED]**
          The AWS account.
        :type transferMessage: string
        :param transferMessage:
          The transfer message.
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        """
        Removes the given tags (metadata) from the resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UntagResource>`_
        
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
          The ARN of the resource.
        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**
          A list of the keys of the tags to be removed from the resource.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_account_audit_configuration(self, roleArn: str = None, auditNotificationTargetConfigurations: Dict = None, auditCheckConfigurations: Dict = None) -> Dict:
        """
        Configures or reconfigures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateAccountAuditConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.update_account_audit_configuration(
              roleArn='string',
              auditNotificationTargetConfigurations={
                  'string': {
                      'targetArn': 'string',
                      'roleArn': 'string',
                      'enabled': True|False
                  }
              },
              auditCheckConfigurations={
                  'string': {
                      'enabled': True|False
                  }
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type roleArn: string
        :param roleArn:
          The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as necessary when performing an audit.
        :type auditNotificationTargetConfigurations: dict
        :param auditNotificationTargetConfigurations:
          Information about the targets to which audit notifications are sent.
          - *(string) --*
            - *(dict) --*
              Information about the targets to which audit notifications are sent.
              - **targetArn** *(string) --*
                The ARN of the target (SNS topic) to which audit notifications are sent.
              - **roleArn** *(string) --*
                The ARN of the role that grants permission to send notifications to the target.
              - **enabled** *(boolean) --*
                True if notifications to the target are enabled.
        :type auditCheckConfigurations: dict
        :param auditCheckConfigurations:
          Specifies which audit checks are enabled and disabled for this account. Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are currently enabled.
          Note that some data collection may begin immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted.
          You cannot disable a check if it is used by any scheduled audit. You must first delete the check from the scheduled audit or delete the scheduled audit itself.
          On the first call to ``UpdateAccountAuditConfiguration`` this parameter is required and must specify at least one enabled check.
          - *(string) --*
            An audit check name. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
            - *(dict) --*
              Which audit checks are enabled and disabled for this account.
              - **enabled** *(boolean) --*
                True if this audit check is enabled for this account.
        :rtype: dict
        :returns:
        """
        pass

    def update_authorizer(self, authorizerName: str, authorizerFunctionArn: str = None, tokenKeyName: str = None, tokenSigningPublicKeys: Dict = None, status: str = None) -> Dict:
        """
        Updates an authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.update_authorizer(
              authorizerName='string',
              authorizerFunctionArn='string',
              tokenKeyName='string',
              tokenSigningPublicKeys={
                  'string': 'string'
              },
              status='ACTIVE'|'INACTIVE'
          )
        
        **Response Syntax**
        ::
            {
                'authorizerName': 'string',
                'authorizerArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **authorizerName** *(string) --* 
              The authorizer name.
            - **authorizerArn** *(string) --* 
              The authorizer ARN.
        :type authorizerName: string
        :param authorizerName: **[REQUIRED]**
          The authorizer name.
        :type authorizerFunctionArn: string
        :param authorizerFunctionArn:
          The ARN of the authorizer\'s Lambda function.
        :type tokenKeyName: string
        :param tokenKeyName:
          The key used to extract the token from the HTTP headers.
        :type tokenSigningPublicKeys: dict
        :param tokenSigningPublicKeys:
          The public keys used to verify the token signature.
          - *(string) --*
            - *(string) --*
        :type status: string
        :param status:
          The status of the update authorizer request.
        :rtype: dict
        :returns:
        """
        pass

    def update_billing_group(self, billingGroupName: str, billingGroupProperties: Dict, expectedVersion: int = None) -> Dict:
        """
        Updates information about the billing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateBillingGroup>`_
        
        **Request Syntax**
        ::
          response = client.update_billing_group(
              billingGroupName='string',
              billingGroupProperties={
                  'billingGroupDescription': 'string'
              },
              expectedVersion=123
          )
        
        **Response Syntax**
        ::
            {
                'version': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **version** *(integer) --* 
              The latest version of the billing group.
        :type billingGroupName: string
        :param billingGroupName: **[REQUIRED]**
          The name of the billing group.
        :type billingGroupProperties: dict
        :param billingGroupProperties: **[REQUIRED]**
          The properties of the billing group.
          - **billingGroupDescription** *(string) --*
            The description of the billing group.
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the ``UpdateBillingGroup`` request is rejected with a ``VersionConflictException`` .
        :rtype: dict
        :returns:
        """
        pass

    def update_ca_certificate(self, certificateId: str, newStatus: str = None, newAutoRegistrationStatus: str = None, registrationConfig: Dict = None, removeAutoRegistration: bool = None):
        """
        Updates a registered CA certificate.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateCACertificate>`_
        
        **Request Syntax**
        ::
          response = client.update_ca_certificate(
              certificateId='string',
              newStatus='ACTIVE'|'INACTIVE',
              newAutoRegistrationStatus='ENABLE'|'DISABLE',
              registrationConfig={
                  'templateBody': 'string',
                  'roleArn': 'string'
              },
              removeAutoRegistration=True|False
          )
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The CA certificate identifier.
        :type newStatus: string
        :param newStatus:
          The updated status of the CA certificate.
           **Note:** The status value REGISTER_INACTIVE is deprecated and should not be used.
        :type newAutoRegistrationStatus: string
        :param newAutoRegistrationStatus:
          The new value for the auto registration status. Valid values are: \"ENABLE\" or \"DISABLE\".
        :type registrationConfig: dict
        :param registrationConfig:
          Information about the registration configuration.
          - **templateBody** *(string) --*
            The template body.
          - **roleArn** *(string) --*
            The ARN of the role.
        :type removeAutoRegistration: boolean
        :param removeAutoRegistration:
          If true, remove auto registration.
        :returns: None
        """
        pass

    def update_certificate(self, certificateId: str, newStatus: str):
        """
        Updates the status of the specified certificate. This operation is idempotent.
        Moving a certificate from the ACTIVE state (including REVOKED) will not disconnect currently connected devices, but these devices will be unable to reconnect.
        The ACTIVE state is required to authenticate devices connecting to AWS IoT using a certificate.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateCertificate>`_
        
        **Request Syntax**
        ::
          response = client.update_certificate(
              certificateId='string',
              newStatus='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
          )
        :type certificateId: string
        :param certificateId: **[REQUIRED]**
          The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
        :type newStatus: string
        :param newStatus: **[REQUIRED]**
          The new status.
           **Note:** Setting the status to PENDING_TRANSFER will result in an exception being thrown. PENDING_TRANSFER is a status used internally by AWS IoT. It is not intended for developer use.
           **Note:** The status value REGISTER_INACTIVE is deprecated and should not be used.
        :returns: None
        """
        pass

    def update_dynamic_thing_group(self, thingGroupName: str, thingGroupProperties: Dict, expectedVersion: int = None, indexName: str = None, queryString: str = None, queryVersion: str = None) -> Dict:
        """
        Updates a dynamic thing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateDynamicThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.update_dynamic_thing_group(
              thingGroupName='string',
              thingGroupProperties={
                  'thingGroupDescription': 'string',
                  'attributePayload': {
                      'attributes': {
                          'string': 'string'
                      },
                      'merge': True|False
                  }
              },
              expectedVersion=123,
              indexName='string',
              queryString='string',
              queryVersion='string'
          )
        
        **Response Syntax**
        ::
            {
                'version': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **version** *(integer) --* 
              The dynamic thing group version.
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The name of the dynamic thing group to update.
        :type thingGroupProperties: dict
        :param thingGroupProperties: **[REQUIRED]**
          The dynamic thing group properties to update.
          - **thingGroupDescription** *(string) --*
            The thing group description.
          - **attributePayload** *(dict) --*
            The thing group attributes in JSON format.
            - **attributes** *(dict) --*
              A JSON string containing up to three key-value pair in JSON format. For example:
               ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``
              - *(string) --*
                - *(string) --*
            - **merge** *(boolean) --*
              Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.
              To remove an attribute, call ``UpdateThing`` with an empty attribute value.
              .. note::
                The ``merge`` attribute is only valid when calling ``UpdateThing`` .
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the dynamic thing group to update.
        :type indexName: string
        :param indexName:
          The dynamic thing group index to update.
          .. note::
            Currently one index is supported: \'AWS_Things\'.
        :type queryString: string
        :param queryString:
          The dynamic thing group search query string to update.
        :type queryVersion: string
        :param queryVersion:
          The dynamic thing group query version to update.
          .. note::
            Currently one query version is supported: \"2017-09-30\". If not specified, the query version defaults to this value.
        :rtype: dict
        :returns:
        """
        pass

    def update_event_configurations(self, eventConfigurations: Dict = None) -> Dict:
        """
        Updates the event configurations.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateEventConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.update_event_configurations(
              eventConfigurations={
                  'string': {
                      'Enabled': True|False
                  }
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type eventConfigurations: dict
        :param eventConfigurations:
          The new event configuration values.
          - *(string) --*
            - *(dict) --*
              Configuration.
              - **Enabled** *(boolean) --*
                True to enable the configuration.
        :rtype: dict
        :returns:
        """
        pass

    def update_indexing_configuration(self, thingIndexingConfiguration: Dict = None, thingGroupIndexingConfiguration: Dict = None) -> Dict:
        """
        Updates the search configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateIndexingConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.update_indexing_configuration(
              thingIndexingConfiguration={
                  'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW',
                  'thingConnectivityIndexingMode': 'OFF'|'STATUS'
              },
              thingGroupIndexingConfiguration={
                  'thingGroupIndexingMode': 'OFF'|'ON'
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type thingIndexingConfiguration: dict
        :param thingIndexingConfiguration:
          Thing indexing configuration.
          - **thingIndexingMode** *(string) --* **[REQUIRED]**
            Thing indexing mode. Valid values are:
            * REGISTRY – Your thing index will contain only registry data.
            * REGISTRY_AND_SHADOW - Your thing index will contain registry and shadow data.
            * OFF - Thing indexing is disabled.
          - **thingConnectivityIndexingMode** *(string) --*
            Thing connectivity indexing mode. Valid values are:
            * STATUS – Your thing index will contain connectivity status. In order to enable thing connectivity indexing, thingIndexMode must not be set to OFF.
            * OFF - Thing connectivity status indexing is disabled.
        :type thingGroupIndexingConfiguration: dict
        :param thingGroupIndexingConfiguration:
          Thing group indexing configuration.
          - **thingGroupIndexingMode** *(string) --* **[REQUIRED]**
            Thing group indexing mode.
        :rtype: dict
        :returns:
        """
        pass

    def update_job(self, jobId: str, description: str = None, presignedUrlConfig: Dict = None, jobExecutionsRolloutConfig: Dict = None, abortConfig: Dict = None, timeoutConfig: Dict = None):
        """
        Updates supported fields of the specified job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateJob>`_
        
        **Request Syntax**
        ::
          response = client.update_job(
              jobId='string',
              description='string',
              presignedUrlConfig={
                  'roleArn': 'string',
                  'expiresInSec': 123
              },
              jobExecutionsRolloutConfig={
                  'maximumPerMinute': 123,
                  'exponentialRate': {
                      'baseRatePerMinute': 123,
                      'incrementFactor': 123.0,
                      'rateIncreaseCriteria': {
                          'numberOfNotifiedThings': 123,
                          'numberOfSucceededThings': 123
                      }
                  }
              },
              abortConfig={
                  'criteriaList': [
                      {
                          'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                          'action': 'CANCEL',
                          'thresholdPercentage': 123.0,
                          'minNumberOfExecutedThings': 123
                      },
                  ]
              },
              timeoutConfig={
                  'inProgressTimeoutInMinutes': 123
              }
          )
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The ID of the job to be updated.
        :type description: string
        :param description:
          A short text description of the job.
        :type presignedUrlConfig: dict
        :param presignedUrlConfig:
          Configuration information for pre-signed S3 URLs.
          - **roleArn** *(string) --*
            The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.
          - **expiresInSec** *(integer) --*
            How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.
        :type jobExecutionsRolloutConfig: dict
        :param jobExecutionsRolloutConfig:
          Allows you to create a staged rollout of the job.
          - **maximumPerMinute** *(integer) --*
            The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.
          - **exponentialRate** *(dict) --*
            The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.
            - **baseRatePerMinute** *(integer) --* **[REQUIRED]**
              The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
            - **incrementFactor** *(float) --* **[REQUIRED]**
              The exponential factor to increase the rate of rollout for a job.
            - **rateIncreaseCriteria** *(dict) --* **[REQUIRED]**
              The criteria to initiate the increase in rate of rollout for a job.
              AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).
              - **numberOfNotifiedThings** *(integer) --*
                The threshold for number of notified things that will initiate the increase in rate of rollout.
              - **numberOfSucceededThings** *(integer) --*
                The threshold for number of succeeded things that will initiate the increase in rate of rollout.
        :type abortConfig: dict
        :param abortConfig:
          Allows you to create criteria to abort a job.
          - **criteriaList** *(list) --* **[REQUIRED]**
            The list of abort criteria to define rules to abort the job.
            - *(dict) --*
              Details of abort criteria to define rules to abort the job.
              - **failureType** *(string) --* **[REQUIRED]**
                The type of job execution failure to define a rule to initiate a job abort.
              - **action** *(string) --* **[REQUIRED]**
                The type of abort action to initiate a job abort.
              - **thresholdPercentage** *(float) --* **[REQUIRED]**
                The threshold as a percentage of the total number of executed things that will initiate a job abort.
                AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
              - **minNumberOfExecutedThings** *(integer) --* **[REQUIRED]**
                Minimum number of executed things before evaluating an abort rule.
        :type timeoutConfig: dict
        :param timeoutConfig:
          Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the time expires, it will be automatically set to ``TIMED_OUT`` .
          - **inProgressTimeoutInMinutes** *(integer) --*
            Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can\'t be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal ``TIMED_OUT`` status.
        :returns: None
        """
        pass

    def update_role_alias(self, roleAlias: str, roleArn: str = None, credentialDurationSeconds: int = None) -> Dict:
        """
        Updates a role alias.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateRoleAlias>`_
        
        **Request Syntax**
        ::
          response = client.update_role_alias(
              roleAlias='string',
              roleArn='string',
              credentialDurationSeconds=123
          )
        
        **Response Syntax**
        ::
            {
                'roleAlias': 'string',
                'roleAliasArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **roleAlias** *(string) --* 
              The role alias.
            - **roleAliasArn** *(string) --* 
              The role alias ARN.
        :type roleAlias: string
        :param roleAlias: **[REQUIRED]**
          The role alias to update.
        :type roleArn: string
        :param roleArn:
          The role ARN.
        :type credentialDurationSeconds: integer
        :param credentialDurationSeconds:
          The number of seconds the credential will be valid.
        :rtype: dict
        :returns:
        """
        pass

    def update_scheduled_audit(self, scheduledAuditName: str, frequency: str = None, dayOfMonth: str = None, dayOfWeek: str = None, targetCheckNames: List = None) -> Dict:
        """
        Updates a scheduled audit, including what checks are performed and how often the audit takes place.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateScheduledAudit>`_
        
        **Request Syntax**
        ::
          response = client.update_scheduled_audit(
              frequency='DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
              dayOfMonth='string',
              dayOfWeek='SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
              targetCheckNames=[
                  'string',
              ],
              scheduledAuditName='string'
          )
        
        **Response Syntax**
        ::
            {
                'scheduledAuditArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **scheduledAuditArn** *(string) --* 
              The ARN of the scheduled audit.
        :type frequency: string
        :param frequency:
          How often the scheduled audit takes place. Can be one of \"DAILY\", \"WEEKLY\", \"BIWEEKLY\" or \"MONTHLY\". The actual start time of each audit is determined by the system.
        :type dayOfMonth: string
        :param dayOfMonth:
          The day of the month on which the scheduled audit takes place. Can be \"1\" through \"31\" or \"LAST\". This field is required if the \"frequency\" parameter is set to \"MONTHLY\". If days 29-31 are specified, and the month does not have that many days, the audit takes place on the \"LAST\" day of the month.
        :type dayOfWeek: string
        :param dayOfWeek:
          The day of the week on which the scheduled audit takes place. Can be one of \"SUN\", \"MON\", \"TUE\", \"WED\", \"THU\", \"FRI\" or \"SAT\". This field is required if the \"frequency\" parameter is set to \"WEEKLY\" or \"BIWEEKLY\".
        :type targetCheckNames: list
        :param targetCheckNames:
          Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
          - *(string) --*
            An audit check name. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks including those that are enabled or ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)
        :type scheduledAuditName: string
        :param scheduledAuditName: **[REQUIRED]**
          The name of the scheduled audit. (Max. 128 chars)
        :rtype: dict
        :returns:
        """
        pass

    def update_security_profile(self, securityProfileName: str, securityProfileDescription: str = None, behaviors: List = None, alertTargets: Dict = None, additionalMetricsToRetain: List = None, deleteBehaviors: bool = None, deleteAlertTargets: bool = None, deleteAdditionalMetricsToRetain: bool = None, expectedVersion: int = None) -> Dict:
        """
        Updates a Device Defender security profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateSecurityProfile>`_
        
        **Request Syntax**
        ::
          response = client.update_security_profile(
              securityProfileName='string',
              securityProfileDescription='string',
              behaviors=[
                  {
                      'name': 'string',
                      'metric': 'string',
                      'criteria': {
                          'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                          'value': {
                              'count': 123,
                              'cidrs': [
                                  'string',
                              ],
                              'ports': [
                                  123,
                              ]
                          },
                          'durationSeconds': 123,
                          'consecutiveDatapointsToAlarm': 123,
                          'consecutiveDatapointsToClear': 123,
                          'statisticalThreshold': {
                              'statistic': 'string'
                          }
                      }
                  },
              ],
              alertTargets={
                  'string': {
                      'alertTargetArn': 'string',
                      'roleArn': 'string'
                  }
              },
              additionalMetricsToRetain=[
                  'string',
              ],
              deleteBehaviors=True|False,
              deleteAlertTargets=True|False,
              deleteAdditionalMetricsToRetain=True|False,
              expectedVersion=123
          )
        
        **Response Syntax**
        ::
            {
                'securityProfileName': 'string',
                'securityProfileArn': 'string',
                'securityProfileDescription': 'string',
                'behaviors': [
                    {
                        'name': 'string',
                        'metric': 'string',
                        'criteria': {
                            'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                            'value': {
                                'count': 123,
                                'cidrs': [
                                    'string',
                                ],
                                'ports': [
                                    123,
                                ]
                            },
                            'durationSeconds': 123,
                            'consecutiveDatapointsToAlarm': 123,
                            'consecutiveDatapointsToClear': 123,
                            'statisticalThreshold': {
                                'statistic': 'string'
                            }
                        }
                    },
                ],
                'alertTargets': {
                    'string': {
                        'alertTargetArn': 'string',
                        'roleArn': 'string'
                    }
                },
                'additionalMetricsToRetain': [
                    'string',
                ],
                'version': 123,
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileName** *(string) --* 
              The name of the security profile that was updated.
            - **securityProfileArn** *(string) --* 
              The ARN of the security profile that was updated.
            - **securityProfileDescription** *(string) --* 
              The description of the security profile.
            - **behaviors** *(list) --* 
              Specifies the behaviors that, when violated by a device (thing), cause an alert.
              - *(dict) --* 
                A Device Defender security profile behavior.
                - **name** *(string) --* 
                  The name you have given to the behavior.
                - **metric** *(string) --* 
                  What is measured by the behavior.
                - **criteria** *(dict) --* 
                  The criteria that determine if a device is behaving normally in regard to the ``metric`` .
                  - **comparisonOperator** *(string) --* 
                    The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
                  - **value** *(dict) --* 
                    The value to be compared with the ``metric`` .
                    - **count** *(integer) --* 
                      If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                    - **cidrs** *(list) --* 
                      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                      - *(string) --* 
                    - **ports** *(list) --* 
                      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                      - *(integer) --* 
                  - **durationSeconds** *(integer) --* 
                    Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
                  - **consecutiveDatapointsToAlarm** *(integer) --* 
                    If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
                  - **consecutiveDatapointsToClear** *(integer) --* 
                    If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
                  - **statisticalThreshold** *(dict) --* 
                    A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                    - **statistic** *(string) --* 
                      The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
            - **alertTargets** *(dict) --* 
              Where the alerts are sent. (Alerts are always sent to the console.)
              - *(string) --* 
                The type of alert target: one of "SNS".
                - *(dict) --* 
                  A structure containing the alert target ARN and the role ARN.
                  - **alertTargetArn** *(string) --* 
                    The ARN of the notification target to which alerts are sent.
                  - **roleArn** *(string) --* 
                    The ARN of the role that grants permission to send alerts to the notification target.
            - **additionalMetricsToRetain** *(list) --* 
              A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the security profile's ``behaviors`` but it is also retained for any metric specified here.
              - *(string) --* 
            - **version** *(integer) --* 
              The updated version of the security profile.
            - **creationDate** *(datetime) --* 
              The time the security profile was created.
            - **lastModifiedDate** *(datetime) --* 
              The time the security profile was last modified.
        :type securityProfileName: string
        :param securityProfileName: **[REQUIRED]**
          The name of the security profile you want to update.
        :type securityProfileDescription: string
        :param securityProfileDescription:
          A description of the security profile.
        :type behaviors: list
        :param behaviors:
          Specifies the behaviors that, when violated by a device (thing), cause an alert.
          - *(dict) --*
            A Device Defender security profile behavior.
            - **name** *(string) --* **[REQUIRED]**
              The name you have given to the behavior.
            - **metric** *(string) --*
              What is measured by the behavior.
            - **criteria** *(dict) --*
              The criteria that determine if a device is behaving normally in regard to the ``metric`` .
              - **comparisonOperator** *(string) --*
                The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
              - **value** *(dict) --*
                The value to be compared with the ``metric`` .
                - **count** *(integer) --*
                  If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                - **cidrs** *(list) --*
                  If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                  - *(string) --*
                - **ports** *(list) --*
                  If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                  - *(integer) --*
              - **durationSeconds** *(integer) --*
                Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
              - **consecutiveDatapointsToAlarm** *(integer) --*
                If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
              - **consecutiveDatapointsToClear** *(integer) --*
                If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
              - **statisticalThreshold** *(dict) --*
                A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                - **statistic** *(string) --*
                  The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
        :type alertTargets: dict
        :param alertTargets:
          Where the alerts are sent. (Alerts are always sent to the console.)
          - *(string) --*
            The type of alert target: one of \"SNS\".
            - *(dict) --*
              A structure containing the alert target ARN and the role ARN.
              - **alertTargetArn** *(string) --* **[REQUIRED]**
                The ARN of the notification target to which alerts are sent.
              - **roleArn** *(string) --* **[REQUIRED]**
                The ARN of the role that grants permission to send alerts to the notification target.
        :type additionalMetricsToRetain: list
        :param additionalMetricsToRetain:
          A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s ``behaviors`` but it is also retained for any metric specified here.
          - *(string) --*
        :type deleteBehaviors: boolean
        :param deleteBehaviors:
          If true, delete all ``behaviors`` defined for this security profile. If any ``behaviors`` are defined in the current invocation an exception occurs.
        :type deleteAlertTargets: boolean
        :param deleteAlertTargets:
          If true, delete all ``alertTargets`` defined for this security profile. If any ``alertTargets`` are defined in the current invocation an exception occurs.
        :type deleteAdditionalMetricsToRetain: boolean
        :param deleteAdditionalMetricsToRetain:
          If true, delete all ``additionalMetricsToRetain`` defined for this security profile. If any ``additionalMetricsToRetain`` are defined in the current invocation an exception occurs.
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different than the actual version, a ``VersionConflictException`` is thrown.
        :rtype: dict
        :returns:
        """
        pass

    def update_stream(self, streamId: str, description: str = None, files: List = None, roleArn: str = None) -> Dict:
        """
        Updates an existing stream. The stream version will be incremented by one.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateStream>`_
        
        **Request Syntax**
        ::
          response = client.update_stream(
              streamId='string',
              description='string',
              files=[
                  {
                      'fileId': 123,
                      's3Location': {
                          'bucket': 'string',
                          'key': 'string',
                          'version': 'string'
                      }
                  },
              ],
              roleArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'streamId': 'string',
                'streamArn': 'string',
                'description': 'string',
                'streamVersion': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **streamId** *(string) --* 
              The stream ID.
            - **streamArn** *(string) --* 
              The stream ARN.
            - **description** *(string) --* 
              A description of the stream.
            - **streamVersion** *(integer) --* 
              The stream version.
        :type streamId: string
        :param streamId: **[REQUIRED]**
          The stream ID.
        :type description: string
        :param description:
          The description of the stream.
        :type files: list
        :param files:
          The files associated with the stream.
          - *(dict) --*
            Represents a file to stream.
            - **fileId** *(integer) --*
              The file ID.
            - **s3Location** *(dict) --*
              The location of the file in S3.
              - **bucket** *(string) --*
                The S3 bucket.
              - **key** *(string) --*
                The S3 key.
              - **version** *(string) --*
                The S3 bucket version.
        :type roleArn: string
        :param roleArn:
          An IAM role that allows the IoT service principal assumes to access your S3 files.
        :rtype: dict
        :returns:
        """
        pass

    def update_thing(self, thingName: str, thingTypeName: str = None, attributePayload: Dict = None, expectedVersion: int = None, removeThingType: bool = None) -> Dict:
        """
        Updates the data for a thing.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateThing>`_
        
        **Request Syntax**
        ::
          response = client.update_thing(
              thingName='string',
              thingTypeName='string',
              attributePayload={
                  'attributes': {
                      'string': 'string'
                  },
                  'merge': True|False
              },
              expectedVersion=123,
              removeThingType=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The output from the UpdateThing operation.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The name of the thing to update.
        :type thingTypeName: string
        :param thingTypeName:
          The name of the thing type.
        :type attributePayload: dict
        :param attributePayload:
          A list of thing attributes, a JSON string containing name-value pairs. For example:
           ``{\\"attributes\\":{\\"name1\\":\\"value2\\"}}``
          This data is used to add new attributes or update existing attributes.
          - **attributes** *(dict) --*
            A JSON string containing up to three key-value pair in JSON format. For example:
             ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``
            - *(string) --*
              - *(string) --*
          - **merge** *(boolean) --*
            Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call ``UpdateThing`` with an empty attribute value.
            .. note::
              The ``merge`` attribute is only valid when calling ``UpdateThing`` .
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the ``UpdateThing`` request is rejected with a ``VersionConflictException`` .
        :type removeThingType: boolean
        :param removeThingType:
          Remove a thing type association. If **true** , the association is removed.
        :rtype: dict
        :returns:
        """
        pass

    def update_thing_group(self, thingGroupName: str, thingGroupProperties: Dict, expectedVersion: int = None) -> Dict:
        """
        Update a thing group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateThingGroup>`_
        
        **Request Syntax**
        ::
          response = client.update_thing_group(
              thingGroupName='string',
              thingGroupProperties={
                  'thingGroupDescription': 'string',
                  'attributePayload': {
                      'attributes': {
                          'string': 'string'
                      },
                      'merge': True|False
                  }
              },
              expectedVersion=123
          )
        
        **Response Syntax**
        ::
            {
                'version': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **version** *(integer) --* 
              The version of the updated thing group.
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The thing group to update.
        :type thingGroupProperties: dict
        :param thingGroupProperties: **[REQUIRED]**
          The thing group properties.
          - **thingGroupDescription** *(string) --*
            The thing group description.
          - **attributePayload** *(dict) --*
            The thing group attributes in JSON format.
            - **attributes** *(dict) --*
              A JSON string containing up to three key-value pair in JSON format. For example:
               ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``
              - *(string) --*
                - *(string) --*
            - **merge** *(boolean) --*
              Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.
              To remove an attribute, call ``UpdateThing`` with an empty attribute value.
              .. note::
                The ``merge`` attribute is only valid when calling ``UpdateThing`` .
        :type expectedVersion: integer
        :param expectedVersion:
          The expected version of the thing group. If this does not match the version of the thing group being updated, the update will fail.
        :rtype: dict
        :returns:
        """
        pass

    def update_thing_groups_for_thing(self, thingName: str = None, thingGroupsToAdd: List = None, thingGroupsToRemove: List = None, overrideDynamicGroups: bool = None) -> Dict:
        """
        Updates the groups to which the thing belongs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateThingGroupsForThing>`_
        
        **Request Syntax**
        ::
          response = client.update_thing_groups_for_thing(
              thingName='string',
              thingGroupsToAdd=[
                  'string',
              ],
              thingGroupsToRemove=[
                  'string',
              ],
              overrideDynamicGroups=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type thingName: string
        :param thingName:
          The thing whose group memberships will be updated.
        :type thingGroupsToAdd: list
        :param thingGroupsToAdd:
          The groups to which the thing will be added.
          - *(string) --*
        :type thingGroupsToRemove: list
        :param thingGroupsToRemove:
          The groups from which the thing will be removed.
          - *(string) --*
        :type overrideDynamicGroups: boolean
        :param overrideDynamicGroups:
          Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.
        :rtype: dict
        :returns:
        """
        pass

    def validate_security_profile_behaviors(self, behaviors: List) -> Dict:
        """
        Validates a Device Defender security profile behaviors specification.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ValidateSecurityProfileBehaviors>`_
        
        **Request Syntax**
        ::
          response = client.validate_security_profile_behaviors(
              behaviors=[
                  {
                      'name': 'string',
                      'metric': 'string',
                      'criteria': {
                          'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                          'value': {
                              'count': 123,
                              'cidrs': [
                                  'string',
                              ],
                              'ports': [
                                  123,
                              ]
                          },
                          'durationSeconds': 123,
                          'consecutiveDatapointsToAlarm': 123,
                          'consecutiveDatapointsToClear': 123,
                          'statisticalThreshold': {
                              'statistic': 'string'
                          }
                      }
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'valid': True|False,
                'validationErrors': [
                    {
                        'errorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **valid** *(boolean) --* 
              True if the behaviors were valid.
            - **validationErrors** *(list) --* 
              The list of any errors found in the behaviors.
              - *(dict) --* 
                Information about an error found in a behavior specification.
                - **errorMessage** *(string) --* 
                  The description of an error found in the behaviors.
        :type behaviors: list
        :param behaviors: **[REQUIRED]**
          Specifies the behaviors that, when violated by a device (thing), cause an alert.
          - *(dict) --*
            A Device Defender security profile behavior.
            - **name** *(string) --* **[REQUIRED]**
              The name you have given to the behavior.
            - **metric** *(string) --*
              What is measured by the behavior.
            - **criteria** *(dict) --*
              The criteria that determine if a device is behaving normally in regard to the ``metric`` .
              - **comparisonOperator** *(string) --*
                The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
              - **value** *(dict) --*
                The value to be compared with the ``metric`` .
                - **count** *(integer) --*
                  If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                - **cidrs** *(list) --*
                  If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                  - *(string) --*
                - **ports** *(list) --*
                  If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                  - *(integer) --*
              - **durationSeconds** *(integer) --*
                Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
              - **consecutiveDatapointsToAlarm** *(integer) --*
                If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
              - **consecutiveDatapointsToClear** *(integer) --*
                If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
              - **statisticalThreshold** *(dict) --*
                A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                - **statistic** *(string) --*
                  The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
        :rtype: dict
        :returns:
        """
        pass
