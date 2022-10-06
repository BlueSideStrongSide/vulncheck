# Take keyword for now and pass to fetch module to request reputation

from src.api.nist.nist import NISTAPI
from src.api.vulndb.vulndb import VULNDBAPI

import asyncio


class VULNCHECK:
    def __init__(self):

        self.nist = NISTAPI()
        self.vulndb = VULNDBAPI()
        self.results = []


    def request_check(self, keyword: str, API: str =None):
        # Async to both modules here
        self.results.append(self.nist.keyword_search(keyword))
        self.results.append(self.vulndb.keyword_search(keyword))

        return f"We checked for {keyword}"


if __name__ == '__main__':
    test = VULNCHECK()
