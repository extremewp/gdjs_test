import yaml

from util.user_data_base import UserDataBase


class TestGoodsYaml:
    def setup(self):
        self.db = UserDataBase()
    def test_goods_ymal(self):
        data = {
            "goods_stock_pass":{
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url":"http://192.168.50.102:886/goods/stock",
                "params":{
                    "goods_id":49,
                    "page":1,
                    "limit":10
                },
                "method": "get"
            },
            "goods_rapid_recovery_pass":{
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/rapid-recovery",
                "params": {
                    "curpage": 1,
                    "page": 5,
                    "keyword": "茅台"
                },
                "method": "get"
            },
            "goods_send_self_deliver":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/send/self-deliver",
                "params": {
                    "version": "1.0.1",
                }
            },
            "goods_switchyeargoods_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/switchyeargoods",
                "params":{
                    "goods_id":41,
                }
            },
            "goods_switchyeargoods_goodsid_none":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/switchyeargoods",
                "data": {
                    "goods_id": "",
                }
            },
            "goods_switchyeargoods_goodsid_false": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/switchyeargoods",
                "params": {
                    "goods_id": "13212adasd",
                }
            },
            "goods_send_list":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/switchyeargoods",
            },
            "order_get_express_fee_pass":{
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/switchyeargoods",
                "params":{
                    "goods_id":48,
                    "num":4
                }
            },
            "order_get_express_fee_goodsid_none": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/order/get-express-fee",
                "params": {
                    "goods_id": None,
                    "num": 4
                }
            },
            "order_get_express_fee_num_none": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/order/get-express-fee",
                "params": {
                    "goods_id": 48,
                    "num": None
                }
            },
            "order_get_express_fee_num_false": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/order/get-express-fee",
                "params": {
                    "goods_id": 48,
                    "num": "asd"
                }
            },
            "goods_confirm_order_v3_goodsid_none": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/confirm-order-v3",
                "params": {
                    "goods_id": None,
                    "num": 1
                }
            },
            "goods_confirm_order_v3_num_none": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/confirm-order-v3",
                "params": {
                    "goods_id": 48,
                    "num": None
                }
            },
            "goods_confirm_order_v3_num_false": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/confirm-order-v3",
                "params": {
                    "goods_id": 48,
                    "num": "asd1"
                }
            },
            "goods_confirm_order_v3_pass": {
                "method": "get",
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/goods/confirm-order-v3",
                "params": {
                    "goods_id": 48,
                    "num": 1
                }
            },

        }
        with open("../data/goods_data.yml","w") as f:
            yaml.safe_dump(data=data,stream=f)