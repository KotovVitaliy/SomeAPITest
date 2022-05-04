import requests
from enironment import environment


class Request:
    def do(self, method, uri, data, headers=None, cookies=None):
        url = environment.get_domain() + uri

        if not headers:
            headers = {}

        if not cookies:
            cookies = {}

        if method in ["GET", "PATCH"]:
            r = requests.request(method=method, url=url, params=data, headers=headers, cookies=cookies)
        else:
            r = requests.request(method=method, url=url, data=data, headers=headers, cookies=cookies)

        return r


request = Request()
