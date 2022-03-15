import yaml

from base.baseapi import BaseApi


class GifcardDataBase:
    def __init__(self):
        self.ba = BaseApi()

    def giftcard_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_pass'])

    def giftcard_pass_repeat(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_pass_repeat'])

    def giftcard_epcode_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_epcode_false'])

    def giftcard_epcode_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/gifcard.yml"))['giftcard_epcode_none'])
