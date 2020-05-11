from os import getenv
from enum import Enum

from utilities import ParseData


class ValidateAttribute(Enum):
    success = "SUCCESSFUL"
    branch = getenv("BRANCH", "master")
    fullname = getenv("REPOSITORY", "dexterisdiwap/cicd_test")

class ValidateResponse:
    def __init__(self, response):
        self.response = response

    def is_valid(self):
        parsed_data = ParseData(self.response).get_data()

        if not parsed_data.get("commit_state") == ValidateAttribute.success.value:
            return False
        else:
            if parsed_data.get("commit_branch") == ValidateAttribute.branch.value \
                and parsed_data.get("commit_full_name") == ValidateAttribute.fullname.value:
                return True

        return False
