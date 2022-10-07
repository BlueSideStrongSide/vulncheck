# https://nvd.nist.gov/developers/start-here
# https://nvd.nist.gov/developers/vulnerabilities

from dotenv import dotenv_values,load_dotenv, find_dotenv
from pathlib import Path
from src.api.base.api_base import VULNBASEAPI as vulnbaseapi

import os


(load_dotenv(find_dotenv())) # <-- can remove and grab on init


class NISTAPI(vulnbaseapi):

    def __init__(self):
        super().__init__()

    def prepare_request(self, requested_keyword: list =None):
        #Updates Needed
        # self.get_api_specific_data["url"] = self.get_api_specific_data["url"] + requested_keyword
        self.get_api_specific_data["headers"][0]["apiKey"] = self.api_key

        for keyword in requested_keyword:
            temp_dict = {}
            temp_dict["url"] = f'{self.get_api_specific_data["url"]}{keyword}'
            self.format_api_requested_data.append(temp_dict)



if __name__ == '__main__':
    print("Nothing For Now")
