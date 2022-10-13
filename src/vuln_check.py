# Take keyword for now and pass to fetch module to request reputation

from src.api.nist.nist import NISTAPI
from src.api.vulndb.vulndb import VULNDBAPI

import asyncio


class VULNCHECK:
    """
    Class to handle dispatching commands to the supported API's
    """
    def __init__(self):

        self.results = [] # Attribute will sore results from the APIs use this to view them in your calling code
        self.keyword = None # Storage of the requested keyword
        self.prepared_keyword = [] # Formatted keywords, everything is converted to a list type for processing.

        #Enum use would clean this up a bit and let the user decide which API's to call.
        self.nist = NISTAPI() # Create an instance of the NISTAPI handler
        self.vulndb = VULNDBAPI() # Create an instance of the NISTAPI handler



    def _convert_keyword_to_list(self,keyword):
        self.prepared_keyword.append(keyword)

    def request_check(self, keyword: str|list, API: str =None) -> str:
        """
        Synchronous request method to interact with the supported API's

        :param keyword: a list of dll's or a string of one dll to be checked
        :param API: Currently not used but will determine which API is used
        :return: string with status of the requested operations
        """
        if isinstance(keyword,str):
            self._convert_keyword_to_list(keyword)
        else:
            self.prepared_keyword = keyword

        asyncio.get_event_loop().run_until_complete(self.submit_request())


    async def submit_request(self):
        #
        results = await asyncio.gather(self.nist.keyword_search(keyword_list=self.prepared_keyword),
                                       (self.vulndb.keyword_search(keyword_list=self.prepared_keyword)))
        print(results)
        return f"We checked for {''.join(self.prepared_keyword)}"

if __name__ == '__main__':
    test = VULNCHECK()
