import requests
import yaml


class BaseApi:
    def request_api(self,**data):
        res = requests.request(**data)
        return res.json()

