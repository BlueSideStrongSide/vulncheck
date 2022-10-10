# https://vuldb.com/?kb.api

from dotenv import dotenv_values,load_dotenv, find_dotenv
from pathlib import Path
from src.api.base.api_base import VULNBASEAPI as vulnbaseapi

import os


class VULNDBAPI(vulnbaseapi):
    def __init__(self, ):
        self.api_key = None
        super().__init__()


    def prepare_request(self, requested_keyword=None):
        self.get_api_specific_data["headers"][0]["X-VulDB-ApiKey"] = self.api_key

        self.get_api_specific_data["data"] = f"search={requested_keyword}"

        # for keyword in requested_keyword:
        #     temp_dict = {}
        #     temp_dict["url"] = f'{self.get_api_specific_data["url"]}{keyword}'
        #     self.format_api_requested_data.append(temp_dict)

    # def prepare_request(self, requested_keyword: list =None):
    #     #Updates Needed
    #     # self.get_api_specific_data["url"] = self.get_api_specific_data["url"] + requested_keyword
    #     self.get_api_specific_data["headers"][0]["apiKey"] = self.api_key
    #
    #     for keyword in requested_keyword:
    #         temp_dict = {}
    #         temp_dict["url"] = f'{self.get_api_specific_data["url"]}{keyword}'
    #         self.format_api_requested_data.append(temp_dict)