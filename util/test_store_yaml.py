import yaml

from util.user_data_base import UserDataBase


class TestStore:
    def setup(self):
        self.db = UserDataBase()
        self.token = self.db.longin_pass()['data']['token']

    def test_store(self):
        data= {
            "store_goods_detail_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/goods/detail",
                "params": {
                    "bn": "BJ000041",
                    "type": 1
                }
            },
            "store_goods_detail_bn_none":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/goods/detail",
                "params": {
                    "bn": None,
                    "type": 1
                }
            },
            "store_goods_detail_type_none": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/goods/detail",
                "params": {
                    "bn": "BJ000041",
                    "type": ""
                }
            },
            "store_goods_detail_type_false": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/goods/detail",
                "params": {
                    "bn": "BJ000041",
                    "type": "asd"
                }
            },
            "store_goods_detail_bn_false": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/goods/detail",
                "params": {
                    "bn": "BJ000041asdas",
                    "type": "1"
                }
            },
            "store_bn_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/bn",
                "params": {
                    "bn": "BJ000041asdas",
                }
            },
            "store_stock_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/stock",
                "params": {
                    "cat_id": 1,
                }
            },
            "store_goods_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/goods",
                "params": {
                    "bn": "BJ000041",
                    "start":0,
                    "limit":10,
                    "type":0,

                }
            },
            "store_goods_info_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/goods_info",
                "params": {
                    "epcode": "WY22012115400000003C5",
                }
            },
            "store_goods_info_epcode_none": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/goods_info",
                "params": {
                    "epcode": None,
                }
            },
            "store2020_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store2020",
                "params": {
                    "cat_id": 1,
                    "page":1,
                    "limit":10
                }
            },
            "store_sku_detail_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/store/sku/detail",
                "params": {
                    "sku": "BJ000004",
                                 }
            }

        }
        with open('../data/store.yml','w') as f:
            yaml.safe_dump(data=data,stream=f)