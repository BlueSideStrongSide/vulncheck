#Handle making the request and returning to the class who called
#Each class will handle printing and storing results for now

import aiohttp
import asyncio
import requests
import json

class FETCHREP:
    def __init__(self, vuln_api_data : dict =None ):
        self.vuln_api_data =  vuln_api_data
        self.request_session = requests.Session()

    async def async_fetch_rep(self, vuln_api_data : dict =None):
        #Need logic to handle subsuqent request
        async with aiohttp.ClientSession() as session:
            async with session.get("BE A VARIABLE") as resp:
                if resp.status == 200:
                    return await resp.text()
                else:
                    return 1

    def fetch_rep(self):
        print("Synchronous Get Requests")

        url = self.vuln_api_data["url"]
        headers = self.vuln_api_data["headers"][0] or None
        params = self.vuln_api_data.get("params")
        data = self.vuln_api_data.get("data")

        returned_results=[]
        with self.request_session as s:
            fetch_url = getattr(s, self.vuln_api_data["http_method"].lower())
            resp = fetch_url(url=url, headers=headers, params=params, data=data)
            response = json.loads(resp.text)


        return [resp.status_code, resp.url, response]



if __name__ == '__main__':
    print("Nothing For Now")