# Simple interaction with the vulnerability check application
from src.vuln_check import VULNCHECK as vc


if __name__ == '__main__':
    vuln_checker = vc()

    vuln_checker.request_check(keyword="schannel.dll", API=None) #we need a result handler

    for result in vuln_checker.results:
        print(result ,end='\n')
