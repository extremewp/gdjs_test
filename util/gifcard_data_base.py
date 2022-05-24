import yaml

from base.baseapi import BaseApi
from util.test_order_util_yaml import TestOrderUtilYaml


class GifcardDataBase:
    def __init__(self):
        self.ba = BaseApi()
        self.touy = TestOrderUtilYaml()

    def giftcard_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_pass'])

    def giftcard_pass_repeat(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_pass_repeat'])

    def giftcard_epcode_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_epcode_false'])

    def giftcard_epcode_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_epcode_none'])

    def giftcard_list_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_list_pass'])

    def giftcard_delete(self):
        data = self.giftcard_list_pass()
        self.touy.test_giftcard_util_yaml(data=data)
        return self.ba.request_api(**yaml.safe_load(open("../data/giftcard_util.yml"))['giftcard_delete'])

    def giftcard_delete_giftcard_none(self):
        data = self.giftcard_list_pass()
        self.touy.test_giftcard_util_yaml(data=data)
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_delete_giftcard_none'])

    def giftcard_delete_skuid_none(self):
        data = self.giftcard_list_pass()
        self.touy.test_giftcard_util_yaml(data=data)
        return self.ba.request_api(**yaml.safe_load(open("../data/giftcard_util.yml"))['giftcard_delete_skuid_none'])

    def share_giftcard_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['share_giftcard_pass'])

    def share_giftcard_giftcardid_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['share_giftcard_giftcardid_none'])

    def share_giftcard_giftcardid_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['share_giftcard_giftcardid_false'])
