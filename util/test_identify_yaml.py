import yaml

from util.user_data_base import UserDataBase


class TestIdentifyYaml:
    def setup(self):
        self.db = UserDataBase()
        self.token = self.db.longin_pass()['data']['token']


    def test_identify_yaml(self):
        data = {
            "identify_report_pass":{
                "method": "get",
                "url": "http://192.168.50.102:886/identify/report",
                "params": {
                    "order_id": 126,
                },
                "headers": {"token": self.token}
            },
            "identify_report_orderid_none":{

                    "method": "get",
                    "url": "http://192.168.50.102:886/identify/report",
                    "params": {
                        "order_id": None,
                    },
                "headers": {"token": self.token}
            },
            "identify_cats_pass":{
                "method": "get",
                "url": "http://192.168.50.102:886/identify/cats",
                "params": {
                    "page": 1,
                    "limit":10
                },
                "headers": {"token": self.token}
            },
            "identify_cats_page_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/cats",
                "params": {
                    "page":"",
                    "limit": 10
                },
                "headers": {"token": self.token}
            },
                "identify_cats_limit_none": {
                    "method": "get",
                    "url": "http://192.168.50.102:886/identify/cats",
                    "params": {
                        "page": 1,
                        "limit": ""
                    },
                "headers": {"token": self.token}
                },
                    "identify_cats_limit_false": {
                        "method": "get",
                        "url": "http://192.168.50.102:886/identify/cats",
                        "params": {
                            "page": 1,
                            "limit": "a123"
                        },
                "headers": {"token": self.token}

                    },
            "identify_center_status_none":{
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center",
                "params": {
                    "status":None,
                    "page": 1,
                    "per_page": "6"
                },
                "headers": {"token": self.token}

            },
            "identify_center_page_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center",
                "params": {
                    "status": "waiting_evaluate",
                    "page": "",
                    "per_page": "6"
                },
                "headers": {"token": self.token}

            },
            "identify_center_status_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center",
                "params": {
                    "status": "asdasdq",
                    "page": 1,
                    "per_page": "6"
                },
                "headers": {"token": self.token}

            },
            "identify_center_page_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center",
                "params": {
                    "status": "waiting_evaluate",
                    "page": "asdasd123",
                    "per_page": "6"
                },
                "headers": {"token": self.token}

            },
            "identify_center_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center",
                "params": {
                    "status": "waiting_evaluate",
                    "page": 1,
                    "per_page": "6"
                },
                "headers": {"token": self.token}

            },
            "identify_center_detail_orderid_none":{
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center/detail",
                "params": {
                    "order_id": None,

                },
                "headers": {"token": self.token}
            },
            "identify_center_detail_pass": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center/detail",
                "params": {
                    "order_id": 126,

                },
                "headers": {"token": self.token}
            },
            "identify_center_detail_orderid_false":{
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center/detail",
                "params": {
                    "order_id": "asdasfsd132",

                },
                "headers": {"token": self.token}
            },
            "identify_records_pass":{
                "method": "get",
                "url": "http://192.168.50.102:886/identify/records",
                "params": {
                    "order_id": 126,

                },
                "headers": {"token": self.token}
            },
            "identify_records_orderid_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/records",
                "params": {
                    "order_id": None,

                },
                "headers": {"token": self.token}
            },
            "identify_records_orderid_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/records",
                "params": {
                    "order_id": "dasd123",

                },
                "headers": {"token": self.token}
            },
            "identify_report_detail_pass":{
                "method": "get",
                "url": "http://192.168.50.102:886/identify/report-detail",
                "params": {
                    "identify_id": "801",

                },
                "headers": {"token": self.token}
            },
            "identify_report_detail_identifyid_false": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/report-detail",
                "params": {
                    "identify_id": "asd801asd",

                },
                "headers": {"token": self.token}
            },
            "identify_report_detail_identifyid_none": {
                "method": "get",
                "url": "http://192.168.50.102:886/identify/report-detail",
                "params": {
                    "identify_id": None,

                },
                "headers": {"token": self.token}
            },
            "identify_center_list_pass":{
                "method": "get",
                "url": "http://192.168.50.102:886/identify/center/list",
                "params": {
                    "order_id": 126,

                },
                "headers": {"token": self.token}
            }
        }
        with open("../data/identify.yml","w") as f:
            yaml.safe_dump(stream=f,data=data)