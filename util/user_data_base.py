import yaml
import json
from base.baseapi import BaseApi


class UserDataBase:
    def __init__(self):
        self.ba = BaseApi()

    def longin_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['login_pass'])

    def login_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['login_none'])

    def login_file(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['login_file'])

    def shell(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['shell'])

    def user(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user'])

    def user_dashboard(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_dashboard'])

    def upload_avatar_auth(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['upload_avatar_auth'])

    def user_update_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_update'])

    def user_update_type_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_update_type_none'])

    def user_update_value_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_update_value_none'])

    def user_address(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address'])

    def user_address_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_pass'])

    def user_address_name_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_name_none'])

    def user_address_mobile_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_mobile_none'])

    def user_address_update_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_update_pass'])

    def user_address_update_name_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_update_name_none'])

    def user_address_delect_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_delect_pass'])

    def user_address_delect_file(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_delect_file'])

    def user_address_detail_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_detail_pass'])

    def user_address_detail_id_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_detail_id_none'])

    def user_address_detail_id_file(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_address_detail_id_file'])

    def order_detail_filter_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['order_detail_filter_pass'])

    def order_detail_filter_page_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['order_detail_filter_page_none'])

    def order_detail_filter_page_file(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['order_detail_filter_page_file'])

    def order_take_detail_filter_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['order_take_detail_filter_pass'])

    def order_take_detail_filter_page_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['order_take_detail_filter_page_none'])

    def order_take_detail_filter_page_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['order_take_detail_filter_page_false'])

    def user_coupon_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_coupon_pass'])

    def user_coupon_page_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_coupon_page_false'])

    def user_default_address(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/data.yml"))['user_default_address'])


if __name__ == '__main__':
    db = UserDataBase()
    db.shell()
