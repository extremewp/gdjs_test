import yaml

from base.baseapi import BaseApi
from util.test_order_util_yaml import TestOrderUtilYaml


class OrderDataBase:
    def __init__(self):
        self.ba = BaseApi()
        self.touy = TestOrderUtilYaml()

    def order_detail_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_detail_pass'])

    def order_detail_id_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_detail_id_none'])

    def order_detail_id_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_detail_id_false'])

    def order_all_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_all_pass'])

    def order_wait_pay_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_wait_pay_pass'])

    def order_wait_send_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_wait_send_pass'])

    def order_wait_received_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_wait_received_pass'])

    def order_ok_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_ok_pass'])

    def order_fail_pass(self):
        self.res_order_fail_pass=self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_fail_pass'])
        return self.res_order_fail_pass

    def order_status_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_status_none'])

    def order_status_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_status_false'])

    def createorder_pass(self):
        res = self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['createorder_pass'])
        ids = res['data']['id']
        self.touy.test_order_util_yaml(ids)
        return res


    def createorder_maxmun_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['createorder_maxmun_false'])

    def order_get_order_info_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_get_order_info_pass'])

    def order_get_order_info_id_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_get_order_info_id_none'])

    def order_get_order_info_id_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_get_order_info_id_false'])

    def order_is_can_stock_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_is_can_stock_pass'])

    def order_is_can_stock_goodsid_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_is_can_stock_goodsid_none'])

    def order_is_can_stock_goodsid_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['order_is_can_stock_goodsid_false'])

    def ipaynow_index_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order.yml"))['ipaynow_index_pass'])

    def order_cancel(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/order_util.yml"))['order_cancel'])
