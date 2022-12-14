# Take keyword for now and pass to fetch module to request reputation

from src.api.nist.nist import NISTAPI
from src.api.vulndb.vulndb import VULNDBAPI

import asyncio
import time


class VULNCHECK:
    def __init__(self):

        self.results = []
        self.keyword = []
        self.prepared_keyword = []

        #Enum use would clean this up a bit and let the user decide which API's to call.
        self.nist = NISTAPI()
        self.vulndb = VULNDBAPI()

    def _convert_keyword_to_list(self):
        self.prepared_keyword.append(self.keyword)

    def request_check(self, keyword: str|list, API: str =None):
        self.keyword = keyword

        if isinstance(self.keyword,str):
            self._convert_keyword_to_list()

        for keyword in self.prepared_keyword:
            self.results.append(self.nist.keyword_search(keyword))
            self.results.append(self.vulndb.keyword_search(keyword))
            time.sleep(7)

        return f"We checked for {''.join(self.prepared_keyword)}"


if __name__ == '__main__':
    test = VULNCHECK()
