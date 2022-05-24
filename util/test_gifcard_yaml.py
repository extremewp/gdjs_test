

import yaml

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
            },
            "giftcard_list_pass":{
                "method": "get",
                "url": "http://192.168.50.102:886/giftcard/list",
                "params": {
                    "bn": "BJ000041",
                    "page": 1,
                    "per_page": 10,
                },
                "headers": {"token": self.token}
            },
            "giftcard_delete_giftcard_none":{
                "method": "delete",
                "url": "http://192.168.50.102:886/giftcard",
                "params": {
                    "giftcard_id": "",
                    "sku_id": "1",
                },
                "headers": {"token": self.token}
            },
            "share_giftcard_pass":{
                "method": "get",
                "url": "http://192.168.50.102:886/share/giftcard",
                "params": {
                    "giftcard_id": "282",
                },
                "headers": {"token": self.token}
            },
            "share_giftcard_giftcardid_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/share/giftcard",
                "params": {
                    "giftcard_id": "",
                },
                "headers": {"token": self.token}
            },
            "share_giftcard_giftcardid_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/share/giftcard",
                "params": {
                    "giftcard_id": "asd1",
                },
                "headers": {"token": self.token}
            }
        }


        with open("../data/gifcard.yml","w") as f :
            yaml.dump(data=data , stream=f)