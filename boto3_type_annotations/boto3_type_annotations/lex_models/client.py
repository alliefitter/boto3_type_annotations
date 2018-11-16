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
        pass

    def create_bot_version(self, name: str, checksum: str = None) -> Dict:
        pass

    def create_intent_version(self, name: str, checksum: str = None) -> Dict:
        pass

    def create_slot_type_version(self, name: str, checksum: str = None) -> Dict:
        pass

    def delete_bot(self, name: str) -> NoReturn:
        pass

    def delete_bot_alias(self, name: str, botName: str) -> NoReturn:
        pass

    def delete_bot_channel_association(self, name: str, botName: str, botAlias: str) -> NoReturn:
        pass

    def delete_bot_version(self, name: str, version: str) -> NoReturn:
        pass

    def delete_intent(self, name: str) -> NoReturn:
        pass

    def delete_intent_version(self, name: str, version: str) -> NoReturn:
        pass

    def delete_slot_type(self, name: str) -> NoReturn:
        pass

    def delete_slot_type_version(self, name: str, version: str) -> NoReturn:
        pass

    def delete_utterances(self, botName: str, userId: str) -> NoReturn:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_bot(self, name: str, versionOrAlias: str) -> Dict:
        pass

    def get_bot_alias(self, name: str, botName: str) -> Dict:
        pass

    def get_bot_aliases(self, botName: str, nextToken: str = None, maxResults: int = None, nameContains: str = None) -> Dict:
        pass

    def get_bot_channel_association(self, name: str, botName: str, botAlias: str) -> Dict:
        pass

    def get_bot_channel_associations(self, botName: str, botAlias: str, nextToken: str = None, maxResults: int = None, nameContains: str = None) -> Dict:
        pass

    def get_bot_versions(self, name: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_bots(self, nextToken: str = None, maxResults: int = None, nameContains: str = None) -> Dict:
        pass

    def get_builtin_intent(self, signature: str) -> Dict:
        pass

    def get_builtin_intents(self, locale: str = None, signatureContains: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_builtin_slot_types(self, locale: str = None, signatureContains: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_export(self, name: str, version: str, resourceType: str, exportType: str) -> Dict:
        pass

    def get_import(self, importId: str) -> Dict:
        pass

    def get_intent(self, name: str, version: str) -> Dict:
        pass

    def get_intent_versions(self, name: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_intents(self, nextToken: str = None, maxResults: int = None, nameContains: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_slot_type(self, name: str, version: str) -> Dict:
        pass

    def get_slot_type_versions(self, name: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_slot_types(self, nextToken: str = None, maxResults: int = None, nameContains: str = None) -> Dict:
        pass

    def get_utterances_view(self, botName: str, botVersions: List, statusType: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def put_bot(self, name: str, locale: str, childDirected: bool, description: str = None, intents: List = None, clarificationPrompt: Dict = None, abortStatement: Dict = None, idleSessionTTLInSeconds: int = None, voiceId: str = None, checksum: str = None, processBehavior: str = None, createVersion: bool = None) -> Dict:
        pass

    def put_bot_alias(self, name: str, botVersion: str, botName: str, description: str = None, checksum: str = None) -> Dict:
        pass

    def put_intent(self, name: str, description: str = None, slots: List = None, sampleUtterances: List = None, confirmationPrompt: Dict = None, rejectionStatement: Dict = None, followUpPrompt: Dict = None, conclusionStatement: Dict = None, dialogCodeHook: Dict = None, fulfillmentActivity: Dict = None, parentIntentSignature: str = None, checksum: str = None, createVersion: bool = None) -> Dict:
        pass

    def put_slot_type(self, name: str, description: str = None, enumerationValues: List = None, checksum: str = None, valueSelectionStrategy: str = None, createVersion: bool = None) -> Dict:
        pass

    def start_import(self, payload: bytes, resourceType: str, mergeStrategy: str) -> Dict:
        pass
