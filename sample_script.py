# Simple interaction with the vulnerability check application
from src.vuln_check import VULNCHECK as vc


if __name__ == '__main__':
    vuln_checker = vc()
    test_list_dll = ["schannel.dll", "mylib.dll", "dbghelp.dll"]
    test_one_dll = "schannel.dll"

    vuln_checker.request_check(keyword=test_list_dll ,API=None)

    for result in vuln_checker.results:
        print(result)