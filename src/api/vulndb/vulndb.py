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
        self.get_api_specific_data["data"] = "advancedsearch=vendor:Microsoft,product:Windows,version:10"
        self.get_api_specific_data["headers"][0]["X-VulDB-ApiKey"] = self.api_key
