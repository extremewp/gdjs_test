import yaml

from util.user_data_base import UserDataBase


class TestOrderYaml:
    def setup(self):
        self.db = UserDataBase()
        self.token = self.db.longin_pass()['data']['token']

    def test_order_yaml(self):
        data={

            "order_detail_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/detail",
                "params": {"id": 207
                           },
                "headers": {"token": self.token}
            },
            "order_detail_id_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/detail",
                "params": {"id": None
                           },
                "headers": {"token": self.token}
            },
            "order_detail_id_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/detail",
                "params": {"id": "asd"
                           },
                "headers": {"token": self.token}
            },
            "order_all_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order",
                "params": {
                    "status": "all",
                    "page": 1,
                    "limit": 10,

                },
                "headers": {"token": self.token}
            },
            "order_wait_pay_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order",
                "params": {
                    "status": "wait_pay",
                    "page": 1,
                    "limit": 10,
                },
                "headers": {"token": self.token}
            },
            "order_wait_send_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order",
                "params": {
                    "status": "wait_send",
                    "page": 1,
                    "limit": 10,
                },
                "headers": {"token": self.token}
            },
            "order_wait_received_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order",
                "params": {
                    "status": "wait_received",
                    "page": 1,
                    "limit": 10,
                },
                "headers": {"token": self.token}
            },
            "order_ok_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order",
                "params": {
                    "status": "ok",
                    "page": 1,
                    "limit": 10,
                },
                "headers": {"token": self.token}
            },
            "order_fail_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order",
                "params": {
                    "status": "fail",
                    "page": 1,
                    "limit": 10,
                },
                "headers": {"token": self.token}
            },

            "order_status_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/order",
                "params": {
                    "status": None,
                    "page": 1,
                    "limit": 10,
                },
                "headers": {"token": self.token}
            },
            "order_status_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/order",
                "params": {
                    "status": "asdasd",
                    "page": 1,
                    "limit": 10,
                },
                "headers": {"token": self.token}
            },
            "createorder_pass": {
                "method": "post",
                "url": "http://192.168.50.102:886/order",
                "data": {
                    "goods_id": 48,
                    "type": 3,
                    "num": 1,
                    "buy_type": 2,
                    "unit_price": 19900,
                    "mail_type": 1,
                },
                "headers": {"token": self.token}

            },
            "createorder_maxmun_false": {
                "method": "post",
                "url": "http://192.168.50.102:886/order",
                "data": {
                    "goods_id": 48,
                    "type": 3,
                    "num": 1111,
                    "buy_type": 2,
                    "unit_price": 19900,
                    "mail_type": 1,
                },
                "headers": {"token": self.token}

            },
            "order_get_order_info_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/get-order-info",
                "params": {
                    "goods_id": 48,

                },
                "headers": {"token": self.token}
            },
            "order_get_order_info_id_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/get-order-info",
                "params": {
                    "goods_id": None,

                },
                "headers": {"token": self.token}
            },
            "order_get_order_info_id_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/get-order-info",
                "params": {
                    "goods_id": "asd",

                },
                "headers": {"token": self.token}
            },
            "order_is_can_stock_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/is-can-stock",
                "params": {
                    "goods_id": 48,

                },
                "headers": {"token": self.token}
            },
            "order_is_can_stock_goodsid_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/is-can-stock",
                "params": {
                    "goods_id": None,

                },
                "headers": {"token": self.token}
            },
            "order_is_can_stock_goodsid_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/order/is-can-stock",
                "params": {
                    "goods_id": "asda",

                },
                "headers": {"token": self.token}
            },
            "ipaynow_index_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/ipaynow/index",
                "params": {
                    "version": "1.0.1",

                },
                "headers": {"token": self.token}
            },

        }
        with open('../data/order.yml','w') as f:
            yaml.safe_dump(stream=f,data=data)