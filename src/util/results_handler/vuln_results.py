import pprint
import asyncio

class VulnCheckResults:
    """
    VulnCheck result handler this class will handle storing, formatting, and printing results if asked.
    """
    def __init__(self, cache_enabled:bool =True, realtime_results:bool =True):
        self.cache_enabled = cache_enabled
        self.realtime_result = realtime_results
        self._recieved_result = []

    @property
    def remove_result(self):
        pass

    @property
    async def gather_all_resutls(self):
        # need to unpack to format results correctly
        # print(self._recieved_result)
        return self._recieved_result

    async def send_result(self, api_result:list =None):
        self._recieved_result.append(api_result)

    def store_results(self):
        pass

    def print_results(self):
        pass