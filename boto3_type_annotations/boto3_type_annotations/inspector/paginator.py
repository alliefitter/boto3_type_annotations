from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAssessmentRunAgents(Paginator):
    def paginate(self, assessmentRunArn: str, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAssessmentRuns(Paginator):
    def paginate(self, assessmentTemplateArns: List = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAssessmentTargets(Paginator):
    def paginate(self, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAssessmentTemplates(Paginator):
    def paginate(self, assessmentTargetArns: List = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEventSubscriptions(Paginator):
    def paginate(self, resourceArn: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFindings(Paginator):
    def paginate(self, assessmentRunArns: List = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRulesPackages(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class PreviewAgents(Paginator):
    def paginate(self, previewAgentsArn: str, PaginationConfig: Dict = None) -> Dict:
        pass
