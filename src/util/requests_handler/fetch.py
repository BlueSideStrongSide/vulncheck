#Handle making the request and returning to the class who called
#Each class will handle printing and storing results for now

import aiohttp
import asyncio
import requests
import json
import time

class FETCHREP:
    def __init__(self, vuln_api_data : dict, vuln_api_formatted_data:list):
        """
        :param vuln_api_data:
        :param vuln_api_formatted_data:
        """
        self.vuln_api_data =  vuln_api_data
        self.vuln_api_fmt_data = vuln_api_formatted_data
        self.request_session = requests.Session()

    def prepare_request(self):
        pass

    def fetch_rep(self,multiple_lookups=None):

        # the below logic should be moved outside of this method
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
                resp = fetch_url(url=c_url.get("url") or url , headers=headers, params=params, data=c_url.get("data") or data)
                # what happens for API specific errors?

                #resp to json
                response = json.loads(resp.content)

                #adding results to list
                returned_results.append([resp.status_code, resp.url, response])

                #sleep based off of API interval skipping first iteration if only one search ran
                multiple_lookups = True

                current_item +=1

        return returned_results

    # ASYNC TEMPALTE BELOW
    async def async_fetch_rep(self, multiple_lookups=None) -> list:

        # the below logic should be moved outside of this method
        url = self.vuln_api_data["url"] or None
        headers = self.vuln_api_data["headers"][0] or None
        params = self.vuln_api_data.get("params")
        data = self.vuln_api_data.get("data")
        interval = self.vuln_api_data.get("interval") or 10
        returned_results=[]
        current_item = 1

        async with aiohttp.ClientSession() as session:

            for c_url in self.vuln_api_fmt_data :
                print(f"{self.vuln_api_data.get('api')} ASynchronous Get Requests {current_item}/{len(self.vuln_api_fmt_data)}")

                async with session.get(url=c_url.get("url") or url,
                                       headers=headers,
                                       params=params,
                                       data=c_url.get("data") or data) as resp:

                    if resp.status == 200:
                        response = json.dumps(await resp.json())
                        returned_results.append(
                            {
                            "api_request_status_code":resp.status,
                            "api_url":resp.url,
                            "api_reposne":response
                            }
                        )
                        current_item+=1

        return returned_results


if __name__ == '__main__':
    print("Nothing For Now")