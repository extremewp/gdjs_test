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
                "headers": {"token":self.token}

            }
        }
        with open("../data/order_util.yml",'w') as f:
            yaml.safe_dump(stream=f,data=data)

    def test_giftcard_util_yaml(self,data):
        epcode = yaml.safe_load(open("../data/gifcard.yml"))['giftcard_pass']['data']["epcode"]
        for i in data['data']:
           if epcode == i['epcode']:
               ids = i["id"]
               sku_id =i['repositpry_sku_id']
               data = {
                   "giftcard_delete": {
                       "method": "delete",
                       "url": "http://192.168.50.102:886/giftcard",
                       "data": {
                           "giftcard_id": ids,
                           "sku_id": sku_id,

                       },
                       "headers": {"token": self.token}

                   }
               }
               with open("../data/giftcard_util.yml", 'w') as f:
                   yaml.safe_dump(stream=f, data=data)




