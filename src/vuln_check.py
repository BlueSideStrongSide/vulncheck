# Take keyword for now and pass to fetch module to request reputation

from src.api.nist.nist import NISTAPI
from src.api.vulndb.vulndb import VULNDBAPI
from src.util.results_handler.vuln_results import VulnCheckResults as h_vuln_results
import asyncio


class VULNCHECK:
    """
    Class to handle dispatching commands to the supported API's
    """
    def __init__(self):

        self.results = [] # Attribute will store results from the APIs use this to view them in your calling code
        self.realtime_results = None
        self._h_vuln_results = h_vuln_results()
        self.keyword = None # Storage of the requested keyword
        self.prepared_keyword = [] # Formatted keywords, everything is converted to a list type for processing.

        #Enum use would clean this up a bit and let the user decide which API's to call.
        self.nist = NISTAPI() # Create an instance of the NISTAPI handler
        self.vulndb = VULNDBAPI() # Create an instance of the NISTAPI handler

    def _convert_keyword_to_list(self,keyword):
        self.prepared_keyword.append(keyword)

    def request_check(self, keyword: str|list, API: str =None, realtime: bool=False) -> str:
        """
        ASynchronous request method to interact with the supported API's

        :param keyword: a list of dll's or a string of one dll to be checked
        :param API: Currently not used but will determine which API is used
        :return: string with status of the requested operations
        """
        if isinstance(keyword,str):
            self._convert_keyword_to_list(keyword)
        else:
            self.prepared_keyword = keyword



        test = asyncio.get_event_loop().run_until_complete(self.submit_request())

    async def submit_request(self):
        #self.nist.keyword_search(keyword_list=self.prepared_keyword, result_handler=self._h_vuln_results)
        #self.vulndb.keyword_search(keyword_list=self.prepared_keyword, result_handler=self._h_vuln_results)

        api_dispath = [self.nist.keyword_search(keyword_list=self.prepared_keyword, result_handler=self._h_vuln_results)]

        await asyncio.gather(*api_dispath) # <-- results are stored in the handler from within each coro

        #gather all results from coro handler
        self.results = await self._h_vuln_results.gather_all_resutls

        return f"We checked for {''.join(self.prepared_keyword)}"

    def return_all_results(self):
        # we can do some pretty print stuff here...
        # or should send this request to the result handler
        pass

if __name__ == '__main__':
    test = VULNCHECK()
