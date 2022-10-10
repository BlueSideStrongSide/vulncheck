#Handle making the request and returning to the class who called
#Each class will handle printing and storing results for now

import aiohttp
import asyncio
import requests
import json
import time

class FETCHREP:
    def __init__(self, vuln_api_data : dict =None, vuln_api_formatted_data:list =None ):
        self.vuln_api_data =  vuln_api_data
        self.vuln_api_fmt_data = vuln_api_formatted_data
        self.request_session = requests.Session()

    def fetch_rep(self,multiple_lookups=None):

        url = self.vuln_api_data["url"] or None
        headers = self.vuln_api_data["headers"][0] or None
        params = self.vuln_api_data.get("params")
        data = self.vuln_api_data.get("data")
        interval = self.vuln_api_data.get("interval") or 10

        returned_results=[]
        current_item = 1
        with self.request_session as s:
            fetch_url = getattr(s, self.vuln_api_data["http_method"].lower())

            for c_url in self.vuln_api_fmt_data :
                print(f"Synchronous Get Requests {current_item}/{len(self.vuln_api_fmt_data)}")

                if multiple_lookups:
                    time.sleep(interval)

                # print(f'{c_url.get("url") or url},{headers},{params},{c_url.get("data") or data}')
                # test_value = c_url.get("data") or data
                # print(type(test_value))
                resp = fetch_url(url=c_url.get("url") or url , headers=headers, params=params, data=c_url.get("data") or data)

                response = json.loads(resp.text)

                returned_results.append([resp.status_code, resp.url, response])

                #sleep based off of API interval skipping first iteration if only one search ran
                multiple_lookups = True

                current_item +=1

        return returned_results

    # ASYNC TEMPALTE BELOW
    # async def async_fetch_rep(self, vuln_api_data : dict =None):
    #     #Need logic to handle subsuqent request
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get("BE A VARIABLE") as resp:
    #             if resp.status == 200:
    #                 return await resp.text()
    #             else:
    #                 return 1


if __name__ == '__main__':
    print("Nothing For Now")