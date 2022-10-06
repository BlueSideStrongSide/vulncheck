# ALl APIS should inheret from this class

from src.util.requests_handler.fetch import FETCHREP as fetchrep
from dotenv import dotenv_values,load_dotenv, find_dotenv
from pathlib import Path
from abc import ABC, abstractmethod
import asyncio
import os

#This data structure will be moved to an external configuration
supported_api_data = {
    "NISTAPI": {
        "headers": [{"User-Agent":"User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
                     "apiKey":"*****"}],
        "url": "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=",
        "http_method": "GET"
    },
    "VULNDBAPI": {
        "headers": [{"User-Agent":"User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
                     "X-VulDB-ApiKey":"*****"}],
        "data":"*****",
        "url": "https://vuldb.com/?api",
        "http_method": "POST"
    }
}

class VULNBASEAPI(ABC):
    def __init__(self):

        (load_dotenv(find_dotenv()))

        self.api_key = os.getenv(self.__class__.__name__)
        self.get_api_specific_data = supported_api_data.get(self.__class__.__name__)
        self.result = None

    def keyword_search(self, keyword: str):
        self.prepare_request(requested_keyword=keyword)
        result_fr = fetchrep(vuln_api_data=self.get_api_specific_data).fetch_rep()
        self.result = result_fr

        return self.__class__.__name__,"returned from fetch",self.result

    @abstractmethod
    def prepare_request(self, requested_keyword=None):
        pass


if __name__ == "__main__":
    print("Nothing For Now")