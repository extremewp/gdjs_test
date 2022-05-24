import random

import yaml

from util.user_data_base import UserDataBase


class TestYaml:
    def setup(self):
        self.db = UserDataBase()
        self.token = self.db.longin_pass()['data']['token']

    def test_yaml(self):
        data = {"login_pass": {
            "method": "post",
            "url": "http://192.168.50.102:886/session",
            "data": {
                "phone": 19520409998,
                "verify": 111000,
                "type": "phone",
            }
        },
            "login_none": {
                "method": "post",
                "url": "http://192.168.50.102:886/session",
                "data": {
                    "phone": None,
                    "verify": None,
                    "type": "phone",
                }
            },
            "login_file": {
                "method": "post",
                "url": "http://192.168.50.102:886/session",
                "data": {
                    "phone": 19520409998,
                    "verify": 123124124311,
                    "type": "phone",
                }
            },
            "shell": {
                "method": "get",
                "url": "http://192.168.50.102:886/user/sell",
                "params": {"page": 1,
                           "limit": 10
                           },
                "headers": {"token": self.token}
            },
            "user": {
                "method": "get",
                "url": "http://192.168.50.102:886/user",
                "params": {"version": "1.0.1"
                           },
                "headers": {"token": self.token}
            },
            "user_dashboard": {
                "method": "get",
                "url": "http://192.168.50.102:886/user",
                "params": {"version": "1.0.1"
                           },
                "headers": {"token": self.token}
            },
            "upload_avatar_auth": {
                "method": "get",
                "url": "http://192.168.50.102:886/user/upload-avatar-auth",
                "params": {
                    "ex": "https://www.baidu.com/link?url=M1k15lO4STfQcswSbqmDx58aF1RyD7p8mxbmPPsHpKM14L8L31mPuiGW9RFYqFnQ71H0JfSyCTYyHFx0hDpOvqJ3Ycr-Yrrik1qtzqRXxGBEek_b_Zmtri4uzPoz5OgbzdKop-3VD96Z-GxB4om7re4qdKwchZsDSXlAR8aLQym3qSWzzDAiRRcRTHb0WU8S9DiK8eZLBk76ODgVEA-xG95RFRW3JkGj7EwXJqF3Lw9Zs94Hd-eoN9shOptEUeLQaYGE614MwOMK3zd01_hSUc40PDiLg3-XqbW7bXMxVkzhOHng7dyyqYvFiH6joPVsSjlwikatvl82458eepGn0bcg-y1KvGTbLlKbkWbAy5bk8rh63KEMqKNOCMFDmGVeCks83GoVVQ9tH782mAK6YoaAcEEO2CQsy65c6h2VWecVrk-YteFYVJEm5aLLbVRNar1x-pYD2zaxAgC9ksgatrMrXBYBe5InF8skDzk64JwYrjO9YenI6942UgXPDf8-YyPXRWMCaV5fUOXYsirAbYNqhM0pcvmxR0oRY1ZarFk1R6c2t4UbArJm9XX8tijjV9PkUvc1-mNvSXxAQS8vwFy6w7PEYgtEEVXiAxgxi6c2A8IbIfzLwjzW8EDpbRmiwHQSOHwE4ecHkeBrvG17sK&wd=&eqid=f1f04be9000acec40000000262271bb7",
                    "num": 1
                    },
                "headers": {"token": self.token}
            },
            "user_update": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/update",
                "method": "put",
                "data": {
                    "type": "name",
                    "value": "wss",
                    "werify": 111000
                }
            },
            "user_update_type_none": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/update",
                "method": "put",
                "data": {
                    "type": None,
                    "value": "wss",
                    "werify": 111000
                }
            },
            "user_update_value_none": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/update",
                "method": "put",
                "data": {
                    "type": "name",
                    "value": None,
                    "werify": 111000
                }
            },
            "user_address": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address",
                "method": "get"

            },
            "user_address_pass": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address",
                "method": "post",
                "data": {
                    "name": "张三",
                    "mobile": 19520409998,
                    "province_id": 19,
                    "province": 12,
                    "city_id": 12,
                    "city": 12,
                    "district_id": 12,
                    "district": 12,
                    "detail": 12,
                    "is_default": 0,
                }
            },
            "user_address_name_none": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address",
                "method": "post",
                "data": {
                    "name": None,
                    "mobile": 19520409998,
                    "province_id": 19,
                    "province": 12,
                    "city_id": 12,
                    "city": 12,
                    "district_id": 12,
                    "district": 12,
                    "detail": 12,
                    "is_default": 0,
                }
            },
            "user_address_mobile_none": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address",
                "method": "post",
                "data": {
                    "name": "张三",
                    "mobile": None,
                    "province_id": 19,
                    "province": 12,
                    "city_id": 12,
                    "city": 12,
                    "district_id": 12,
                    "district": 12,
                    "detail": 12,
                    "is_default": 0,
                }
            },
            "user_address_update_pass": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address",
                "method": "put",
                "data": {
                    "id": self.db.user_address()['data'][3]['id'],
                    "name": "张三",
                    "mobile": 1952040998,
                    "province_id": 19,
                    "province": 12,
                    "city_id": 12,
                    "city": 12,
                    "district_id": 12,
                    "district": 12,
                    "detail": 12,
                    "is_default": 0,
                }
            },
            "user_address_update_name_none": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address",
                "method": "put",
                "data": {
                    "id": self.db.user_address()['data'][3]['id'],
                    "name": None,
                    "mobile": 1952040998,
                    "province_id": 19,
                    "province": 12,
                    "city_id": 12,
                    "city": 12,
                    "district_id": 12,
                    "district": 12,
                    "detail": 12,
                    "is_default": 0,
                }
            },
            "user_address_delect_pass": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address",
                "method": "delete",
                "params": {
                    "id": self.db.user_address()['data'][4]['id']
                }
            },

            "user_address_delect_file": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address",
                "method": "delete",
                "params": {
                    "id": 1000000
                }
            },
            "user_address_detail_pass": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address/detail",
                "method": "get",
                "params": {
                    "address_id": self.db.user_address()['data'][1]['id']
                }
            },
            "user_address_detail_id_none": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address/detail",
                "method": "get",
                "params": {
                    "address_id": None
                }
            },
            "user_address_detail_id_file": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/user/address/detail",
                "method": "get",
                "params": {
                    "address_id": "张三"
                }
            },
            "order_detail_filter_pass": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/order/detail/filter",
                "method": "get",
                "params": {
                    "page": 1,
                    "limit": 10,
                    "type": "payment",
                }
            },
            "order_detail_filter_page_file": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/order/detail/filter",
                "method": "get",
                "params": {
                    "page": 1,
                    "limit": 10,
                    "type": "asd"
                }
            },
            "order_detail_filter_page_none": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/order/detail/filter",
                "method": "get",
                "params": {
                    "page": 1,
                    "limit": 10,
                    "type": None
                }
            },
            "order_take_detail_filter_pass": {
                "headers": {"token": self.token},
                "url": "http://192.168.50.102:886/order/take/detail/filter",
                "method": "get",
                "params": {
                    "page": 1,
                    "limit": 10,
                }
            },
            "order_take_detail_filter_page_none": {
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/order/take/detail/filter",
                "method": "get",
                "params": {
                    "page": None,
                    "limit": 10,
                }
            },
            "order_take_detail_filter_page_false": {
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/order/take/detail/filter",
                "method": "get",
                "params": {
                    "page": "1aasd",
                    "limit": 10,
                }
            },
            "user_coupon_pass": {
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/user/coupon?",
                "method": "get",
                "params": {
                    "page": 50,
                    "limit": 10,
                }
            },
            "user_coupon_page_false": {
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/user/coupon?",
                "method": "get",
                "params": {
                    "page": "3asd",
                    "limit": 10,
                }
            },
            "user_default_address": {
                "headers": {"token": self.db.longin_pass()['data']['token']},
                "url": "http://192.168.50.102:886/user/default-address",
                "method": "get",

            }

        }

        with open("../data/data.yml", "w") as f:
            yaml.dump(data=data, stream=f)
