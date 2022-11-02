# https://vuldb.com/?kb.api

from dotenv import dotenv_values,load_dotenv, find_dotenv
from pathlib import Path
from src.api.base.api_base import VULNBASEAPI as vulnbaseapi

import os


class VULNDBAPI(vulnbaseapi):
    def __init__(self):
        super().__init__()


    def prepare_request(self, requested_keyword: list =None):
        """
        :param requested_keyword: The list of keyword term(s) requested.
        """
        self.get_api_specific_data["headers"][0]["X-VulDB-ApiKey"] = self.api_key

        for keyword in requested_keyword:
            temp_dict = {}
            temp_dict["url"] = self.get_api_specific_data["url"]
            temp_dict["data"] = f"search={keyword}"
            self.format_api_requested_data.append(temp_dict)