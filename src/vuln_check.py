# Take keyword for now and pass to fetch module to request reputation

from src.api.nist.nist import NISTAPI
from src.api.vulndb.vulndb import VULNDBAPI

import asyncio


class VULNCHECK:
    def __init__(self):
        """
        Class to handle dispatching commands to the supported API's

        """
        self.results = []
        self.keyword = None
        self.prepared_keyword = []

        #Enum use would clean this up a bit and let the user decide which API's to call.
        self.nist = NISTAPI()
        self.vulndb = VULNDBAPI()

    def _convert_keyword_to_list(self,keyword):
        self.prepared_keyword.append(keyword)

    def request_check(self, keyword: str|list, API: str =None):
        """

        :param keyword: a list of dll's or a string of one dll to be checked
        :param API: Currently not used but will determine which API is used
        :return: string with status of the requested operations
        """
        if isinstance(keyword,str):
            self._convert_keyword_to_list(keyword)
        else:
            self.prepared_keyword = keyword

        self.results.append(self.nist.keyword_search(self.prepared_keyword))
        self.results.append(self.vulndb.keyword_search(keyword))

        return f"We checked for {''.join(self.prepared_keyword)}"

    # ASYNC TEMPALTE BELOW
    # async def request_check(self, keyword: str|list, API: str =None):
    #     self.keyword = keyword
    #
    #     if isinstance(self.keyword,str):
    #         self._convert_keyword_to_list()
    #
    #     for keyword in self.prepared_keyword:
    #         self.results.append(self.nist.keyword_search(keyword))
    #         # self.results.append(self.vulndb.keyword_search(keyword))
    #
    #     return f"We checked for {''.join(self.prepared_keyword)}"


if __name__ == '__main__':
    test = VULNCHECK()
