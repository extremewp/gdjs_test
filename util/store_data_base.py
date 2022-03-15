import yaml

from base.baseapi import BaseApi


class StoreDataBase:
    def __init__(self):
        self.ba = BaseApi()

    def store_goods_detail_pass(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_goods_detail_pass'])

    def store_goods_detail_bn_none(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_goods_detail_bn_none'])

    def store_goods_detail_type_none(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_goods_detail_type_none'])

    def store_goods_detail_bn_false(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_goods_detail_bn_false'])

    def store_goods_detail_type_false(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_goods_detail_type_false'])

    def store_bn_pass(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_bn_pass'])

    def store_stock_pass(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_stock_pass'])

    def store_goods_pass(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_goods_pass'])

    def store_goods_info_pass(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_goods_info_pass'])

    def store_goods_info_epcode_none(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_goods_info_epcode_none'])

    def store2020_pass(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store2020_pass'])

    def store_sku_detail_pass(self):
        return self.ba.request_api(**yaml.safe_load((open("../data/store.yml")))['store_sku_detail_pass'])
