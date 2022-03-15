import yaml

from base.baseapi import BaseApi


class GoodsDataBase:
    def __init__(self):
        self.ba = BaseApi()

    def goods_stock_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_stock_pass'])

    def goods_rapid_recovery_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_rapid_recovery_pass'])

    def goods_send_self_deliver(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_send_self_deliver'])

    def goods_switchyeargoods_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_switchyeargoods_pass'])

    def goods_switchyeargoods_goodsid_none(self):
        return self.ba.request_api(
            **yaml.safe_load(open("../data/goods_data.yml"))['goods_switchyeargoods_goodsid_none'])

    def goods_switchyeargoods_goodsid_false(self):
        return self.ba.request_api(
            **yaml.safe_load(open("../data/goods_data.yml"))['goods_switchyeargoods_goodsid_false'])

    def goods_send_list(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_send_list'])

    def order_get_express_fee_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['order_get_express_fee_pass'])

    def order_get_express_fee_goodsid_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['order_get_express_fee_goodsid_none'])

    def order_get_express_fee_num_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['order_get_express_fee_num_none'])

    def order_get_express_fee_num_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['order_get_express_fee_num_false'])

    def goods_confirm_order_v3_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_confirm_order_v3_pass'])

    def goods_confirm_order_v3_goodsid_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_confirm_order_v3_goodsid_none'])

    def goods_confirm_order_v3_num_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_confirm_order_v3_num_none'])

    def goods_confirm_order_v3_num_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/goods_data.yml"))['goods_confirm_order_v3_num_false'])
