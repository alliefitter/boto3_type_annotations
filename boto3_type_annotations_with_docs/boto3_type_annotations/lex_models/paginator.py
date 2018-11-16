from typing import Dict
from botocore.paginate import Paginator


class GetBotAliases(Paginator):
    def paginate(self, botName: str, nameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotAliases>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              botName=\'string\',
              nameContains=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type botName: string
        :param botName: **[REQUIRED]** 
        
          The name of the bot.
        
        :type nameContains: string
        :param nameContains: 
        
          Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
        
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
                \'BotAliases\': [
                    {
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'botVersion\': \'string\',
                        \'botName\': \'string\',
                        \'lastUpdatedDate\': datetime(2015, 1, 1),
                        \'createdDate\': datetime(2015, 1, 1),
                        \'checksum\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BotAliases** *(list) --* 
        
              An array of ``BotAliasMetadata`` objects, each describing a bot alias.
        
              - *(dict) --* 
        
                Provides information about a bot alias.
        
                - **name** *(string) --* 
        
                  The name of the bot alias.
        
                - **description** *(string) --* 
        
                  A description of the bot alias.
        
                - **botVersion** *(string) --* 
        
                  The version of the Amazon Lex bot to which the alias points.
        
                - **botName** *(string) --* 
        
                  The name of the bot to which the alias points.
        
                - **lastUpdatedDate** *(datetime) --* 
        
                  The date that the bot alias was updated. When you create a resource, the creation date and last updated date are the same.
        
                - **createdDate** *(datetime) --* 
        
                  The date that the bot alias was created.
        
                - **checksum** *(string) --* 
        
                  Checksum of the bot alias.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetBotChannelAssociations(Paginator):
    def paginate(self, botName: str, botAlias: str, nameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotChannelAssociations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              botName=\'string\',
              botAlias=\'string\',
              nameContains=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type botName: string
        :param botName: **[REQUIRED]** 
        
          The name of the Amazon Lex bot in the association.
        
        :type botAlias: string
        :param botAlias: **[REQUIRED]** 
        
          An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
        
        :type nameContains: string
        :param nameContains: 
        
          Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\" To return all bot channel associations, use a hyphen (\"-\") as the ``nameContains`` parameter.
        
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
                \'botChannelAssociations\': [
                    {
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'botAlias\': \'string\',
                        \'botName\': \'string\',
                        \'createdDate\': datetime(2015, 1, 1),
                        \'type\': \'Facebook\'|\'Slack\'|\'Twilio-Sms\'|\'Kik\',
                        \'botConfiguration\': {
                            \'string\': \'string\'
                        },
                        \'status\': \'IN_PROGRESS\'|\'CREATED\'|\'FAILED\',
                        \'failureReason\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **botChannelAssociations** *(list) --* 
        
              An array of objects, one for each association, that provides information about the Amazon Lex bot and its association with the channel. 
        
              - *(dict) --* 
        
                Represents an association between an Amazon Lex bot and an external messaging platform.
        
                - **name** *(string) --* 
        
                  The name of the association between the bot and the channel. 
        
                - **description** *(string) --* 
        
                  A text description of the association you are creating. 
        
                - **botAlias** *(string) --* 
        
                  An alias pointing to the specific version of the Amazon Lex bot to which this association is being made. 
        
                - **botName** *(string) --* 
        
                  The name of the Amazon Lex bot to which this association is being made. 
        
                  .. note::
        
                    Currently, Amazon Lex supports associations with Facebook and Slack, and Twilio.
        
                - **createdDate** *(datetime) --* 
        
                  The date that the association between the Amazon Lex bot and the channel was created. 
        
                - **type** *(string) --* 
        
                  Specifies the type of association by indicating the type of channel being established between the Amazon Lex bot and the external messaging platform.
        
                - **botConfiguration** *(dict) --* 
        
                  Provides information necessary to communicate with the messaging platform. 
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **status** *(string) --* 
        
                  The status of the bot channel. 
        
                  * ``CREATED`` - The channel has been created and is ready for use. 
                   
                  * ``IN_PROGRESS`` - Channel creation is in progress. 
                   
                  * ``FAILED`` - There was an error creating the channel. For information about the reason for the failure, see the ``failureReason`` field. 
                   
                - **failureReason** *(string) --* 
        
                  If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to create the association.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetBotVersions(Paginator):
    def paginate(self, name: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              name=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the bot for which versions should be returned.
        
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
                \'bots\': [
                    {
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'status\': \'BUILDING\'|\'READY\'|\'READY_BASIC_TESTING\'|\'FAILED\'|\'NOT_BUILT\',
                        \'lastUpdatedDate\': datetime(2015, 1, 1),
                        \'createdDate\': datetime(2015, 1, 1),
                        \'version\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **bots** *(list) --* 
        
              An array of ``BotMetadata`` objects, one for each numbered version of the bot plus one for the ``$LATEST`` version.
        
              - *(dict) --* 
        
                Provides information about a bot. .
        
                - **name** *(string) --* 
        
                  The name of the bot. 
        
                - **description** *(string) --* 
        
                  A description of the bot.
        
                - **status** *(string) --* 
        
                  The status of the bot.
        
                - **lastUpdatedDate** *(datetime) --* 
        
                  The date that the bot was updated. When you create a bot, the creation date and last updated date are the same. 
        
                - **createdDate** *(datetime) --* 
        
                  The date that the bot was created.
        
                - **version** *(string) --* 
        
                  The version of the bot. For a new bot, the version is always ``$LATEST`` .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetBots(Paginator):
    def paginate(self, nameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBots>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              nameContains=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type nameContains: string
        :param nameContains: 
        
          Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
        
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
                \'bots\': [
                    {
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'status\': \'BUILDING\'|\'READY\'|\'READY_BASIC_TESTING\'|\'FAILED\'|\'NOT_BUILT\',
                        \'lastUpdatedDate\': datetime(2015, 1, 1),
                        \'createdDate\': datetime(2015, 1, 1),
                        \'version\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **bots** *(list) --* 
        
              An array of ``botMetadata`` objects, with one entry for each bot. 
        
              - *(dict) --* 
        
                Provides information about a bot. .
        
                - **name** *(string) --* 
        
                  The name of the bot. 
        
                - **description** *(string) --* 
        
                  A description of the bot.
        
                - **status** *(string) --* 
        
                  The status of the bot.
        
                - **lastUpdatedDate** *(datetime) --* 
        
                  The date that the bot was updated. When you create a bot, the creation date and last updated date are the same. 
        
                - **createdDate** *(datetime) --* 
        
                  The date that the bot was created.
        
                - **version** *(string) --* 
        
                  The version of the bot. For a new bot, the version is always ``$LATEST`` .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetBuiltinIntents(Paginator):
    def paginate(self, locale: str = None, signatureContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBuiltinIntents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              locale=\'en-US\'|\'en-GB\'|\'de-DE\',
              signatureContains=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type locale: string
        :param locale: 
        
          A list of locales that the intent supports.
        
        :type signatureContains: string
        :param signatureContains: 
        
          Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\" To find the signature for an intent, see `Standard Built-in Intents <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__ in the *Alexa Skills Kit* .
        
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
                \'intents\': [
                    {
                        \'signature\': \'string\',
                        \'supportedLocales\': [
                            \'en-US\'|\'en-GB\'|\'de-DE\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **intents** *(list) --* 
        
              An array of ``builtinIntentMetadata`` objects, one for each intent in the response.
        
              - *(dict) --* 
        
                Provides metadata for a built-in intent.
        
                - **signature** *(string) --* 
        
                  A unique identifier for the built-in intent. To find the signature for an intent, see `Standard Built-in Intents <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__ in the *Alexa Skills Kit* .
        
                - **supportedLocales** *(list) --* 
        
                  A list of identifiers for the locales that the intent supports.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetBuiltinSlotTypes(Paginator):
    def paginate(self, locale: str = None, signatureContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBuiltinSlotTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              locale=\'en-US\'|\'en-GB\'|\'de-DE\',
              signatureContains=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type locale: string
        :param locale: 
        
          A list of locales that the slot type supports.
        
        :type signatureContains: string
        :param signatureContains: 
        
          Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
        
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
                \'slotTypes\': [
                    {
                        \'signature\': \'string\',
                        \'supportedLocales\': [
                            \'en-US\'|\'en-GB\'|\'de-DE\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **slotTypes** *(list) --* 
        
              An array of ``BuiltInSlotTypeMetadata`` objects, one entry for each slot type returned.
        
              - *(dict) --* 
        
                Provides information about a built in slot type.
        
                - **signature** *(string) --* 
        
                  A unique identifier for the built-in slot type. To find the signature for a slot type, see `Slot Type Reference <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__ in the *Alexa Skills Kit* .
        
                - **supportedLocales** *(list) --* 
        
                  A list of target locales for the slot. 
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetIntentVersions(Paginator):
    def paginate(self, name: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetIntentVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              name=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the intent for which versions should be returned.
        
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
                \'intents\': [
                    {
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'lastUpdatedDate\': datetime(2015, 1, 1),
                        \'createdDate\': datetime(2015, 1, 1),
                        \'version\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **intents** *(list) --* 
        
              An array of ``IntentMetadata`` objects, one for each numbered version of the intent plus one for the ``$LATEST`` version.
        
              - *(dict) --* 
        
                Provides information about an intent.
        
                - **name** *(string) --* 
        
                  The name of the intent.
        
                - **description** *(string) --* 
        
                  A description of the intent.
        
                - **lastUpdatedDate** *(datetime) --* 
        
                  The date that the intent was updated. When you create an intent, the creation date and last updated date are the same.
        
                - **createdDate** *(datetime) --* 
        
                  The date that the intent was created.
        
                - **version** *(string) --* 
        
                  The version of the intent.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetIntents(Paginator):
    def paginate(self, nameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetIntents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              nameContains=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type nameContains: string
        :param nameContains: 
        
          Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
        
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
                \'intents\': [
                    {
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'lastUpdatedDate\': datetime(2015, 1, 1),
                        \'createdDate\': datetime(2015, 1, 1),
                        \'version\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **intents** *(list) --* 
        
              An array of ``Intent`` objects. For more information, see  PutBot .
        
              - *(dict) --* 
        
                Provides information about an intent.
        
                - **name** *(string) --* 
        
                  The name of the intent.
        
                - **description** *(string) --* 
        
                  A description of the intent.
        
                - **lastUpdatedDate** *(datetime) --* 
        
                  The date that the intent was updated. When you create an intent, the creation date and last updated date are the same.
        
                - **createdDate** *(datetime) --* 
        
                  The date that the intent was created.
        
                - **version** *(string) --* 
        
                  The version of the intent.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetSlotTypeVersions(Paginator):
    def paginate(self, name: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetSlotTypeVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              name=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the slot type for which versions should be returned.
        
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
                \'slotTypes\': [
                    {
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'lastUpdatedDate\': datetime(2015, 1, 1),
                        \'createdDate\': datetime(2015, 1, 1),
                        \'version\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **slotTypes** *(list) --* 
        
              An array of ``SlotTypeMetadata`` objects, one for each numbered version of the slot type plus one for the ``$LATEST`` version.
        
              - *(dict) --* 
        
                Provides information about a slot type..
        
                - **name** *(string) --* 
        
                  The name of the slot type.
        
                - **description** *(string) --* 
        
                  A description of the slot type.
        
                - **lastUpdatedDate** *(datetime) --* 
        
                  The date that the slot type was updated. When you create a resource, the creation date and last updated date are the same. 
        
                - **createdDate** *(datetime) --* 
        
                  The date that the slot type was created.
        
                - **version** *(string) --* 
        
                  The version of the slot type.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetSlotTypes(Paginator):
    def paginate(self, nameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetSlotTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              nameContains=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type nameContains: string
        :param nameContains: 
        
          Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
        
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
                \'slotTypes\': [
                    {
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'lastUpdatedDate\': datetime(2015, 1, 1),
                        \'createdDate\': datetime(2015, 1, 1),
                        \'version\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **slotTypes** *(list) --* 
        
              An array of objects, one for each slot type, that provides information such as the name of the slot type, the version, and a description.
        
              - *(dict) --* 
        
                Provides information about a slot type..
        
                - **name** *(string) --* 
        
                  The name of the slot type.
        
                - **description** *(string) --* 
        
                  A description of the slot type.
        
                - **lastUpdatedDate** *(datetime) --* 
        
                  The date that the slot type was updated. When you create a resource, the creation date and last updated date are the same. 
        
                - **createdDate** *(datetime) --* 
        
                  The date that the slot type was created.
        
                - **version** *(string) --* 
        
                  The version of the slot type.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
