import yaml

from util.user_data_base import UserDataBase


class TestOrderUtilYaml:
    def __init__(self):
        self.db = UserDataBase()
        self.token = self.db.longin_pass()['data']['token']
    def test_order_util_yaml(self,ids):
        data = {
            "order_cancel": {
                "method": "post",
                "url": "http://192.168.50.102:886/order/cancel",
                "data": {
                    "id":ids,
                    "order_type": "goods",

                },
                "headers": {"token": self.token}

            }
        }
        with open("../data/order_util.yml",'w') as f:
            yaml.safe_dump(stream=f,data=data)