
import random

import yaml

from testing.test_store import TestStore
from util.store_data_base import StoreDataBase
from util.user_data_base import UserDataBase


class TestGifcard:
    def setup(self):
        self.db = UserDataBase()
        self.token = self.db.longin_pass()['data']['token']
        self.sdb = StoreDataBase()
        self.jkwym = self.sdb.store_goods_pass()['data'][2]['epcode']
        print(self.sdb.store_goods_pass())
    def test_yaml(self):
        data = {
            "giftcard_pass": {
                "method": "post",
                "url": "http://192.168.50.102:886/giftcard",
                "data": {
                    "epcode": self.jkwym,
                    "content": "asdas",
                    "type": "phone",
                },
                "headers": {"token": self.token}
            },
            "giftcard_pass_repeat":{
                "method": "post",
                "url": "http://192.168.50.102:886/giftcard",
                "data": {
                    "epcode": self.jkwym,
                    "content": "asdas",
                    "type": "phone",
                },
                "headers": {"token": self.token}
            },
            "giftcard_epcode_false":{
                "method": "post",
                "url": "http://192.168.50.102:886/giftcard",
                "data": {
                    "epcode": self.jkwym+"asd",
                    "content": "asdas",
                    "type": "phone",
                },
                "headers": {"token": self.token}
            },
            "giftcard_epcode_none":{
                "method": "post",
                "url": "http://192.168.50.102:886/giftcard",
                "data": {
                    "epcode": "",
                    "content": "asdas",
                    "type": "phone",
                },
                "headers": {"token": self.token}
            }
        }


        with open("../data/gifcard.yml","w") as f :
            yaml.dump(data=data , stream=f)