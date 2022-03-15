import yaml

from base.baseapi import BaseApi


class IdentifyDataBase:
    def __init__(self):
        self.ba = BaseApi()

    def identify_report_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_report_pass'])

    def identify_report_orderid_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_report_orderid_none'])

    def identify_cats_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_cats_pass'])

    def identify_cats_page_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_cats_page_none'])

    def identify_cats_limit_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_cats_limit_none'])

    def identify_cats_limit_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_cats_limit_false'])

    def identify_center_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_pass'])
    def identify_center_status_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_status_none'])
    def identify_center_page_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_page_none'])
    def identify_center_status_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_status_false'])
    def identify_center_page_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_page_false'])
    def identify_center_detail_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_detail_pass'])
    def identify_center_detail_orderid_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_detail_orderid_none'])
    def identify_center_detail_orderid_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_detail_orderid_false'])

    def identify_records_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_records_pass'])

    def identify_records_orderid_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_records_orderid_none'])
    def identify_records_orderid_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_records_orderid_false'])
    def identify_report_detail_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_report_detail_pass'])
    def identify_report_detail_identifyid_none(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_report_detail_identifyid_none'])
    def identify_report_detail_identifyid_false(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_report_detail_identifyid_false'])
    def identify_center_list_pass(self):
        return self.ba.request_api(**yaml.safe_load(open("../data/identify.yml"))['identify_center_list_pass'])

















