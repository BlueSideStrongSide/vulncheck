from src.util.requests_handler.fetch import FETCHREP as fetchrep
from src.util.results_handler.vuln_results import VulnCheckResults as h_vuln_results
from dotenv import dotenv_values,load_dotenv, find_dotenv
from abc import ABC, abstractmethod
from pathlib import Path
import asyncio
import os

#This data structure will be moved to an external configuration
supported_api_data = {
    "NISTAPI": {
        "headers": [{"User-Agent":"User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
                     "apiKey":"*****"}],
        "url": "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=",
        "http_method": "GET",
        "interval":4,
        "api":"NISTAPI"
    },
    "VULNDBAPI": {
        "headers": [{"User-Agent":"User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
                     "X-VulDB-ApiKey":"*****"}],
        "data":"*****",
        "url": "https://vuldb.com/?api",
        "http_method": "POST",
        "interval":7,
        "api":"VULNDBAPI"
    }
}

class VULNBASEAPI(ABC):
    def __init__(self):

        (load_dotenv(find_dotenv()))

        self.api_key = os.getenv(self.__class__.__name__)
        self.get_api_specific_data = supported_api_data.get(self.__class__.__name__)

        self.result = None
        self.formatted_result = None
        self.format_api_requested_data = []

    async def keyword_search(self, keyword_list: list, result_handler=None): #<-- add typing

        self.prepare_request(requested_keyword=keyword_list)

        self.result = await fetchrep(vuln_api_data=self.get_api_specific_data,
                                     vuln_api_formatted_data=self.format_api_requested_data).async_fetch_rep() #async_fetch_rep make this an param

        #initial implementation of the result handler
        await result_handler.send_result(api_result=self.result)

        return f'{self.__class__.__name__},returned from fetch {len(self.result)}'

    @abstractmethod
    def prepare_request(self, requested_keyword: list =None):
        """
        This method is required to be overwritten with all child classes.
        Place any logic required to create a working request to the desired API.
        Review the provided API's for examples

        :param requested_keyword: this will be the keyword terms requested.
        """
        pass


if __name__ == "__main__":
    print("Nothing For Now")