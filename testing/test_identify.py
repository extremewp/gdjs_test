import pytest

from util.identify_data_base import IdentifyDataBase


class TestIdentify:

    def setup(self):
        self.idb = IdentifyDataBase()

    # 鉴定报告列表
    def test_identify_report_pass(self):
        res = self.idb.identify_report_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 鉴定报告列表orderid空
    def test_identify_report_orderid_none(self):
        res = self.idb.identify_report_orderid_none()
        assert res['code'] == 4000
        assert res['msg'] == '订单不存在'

    # 选择鉴定商品
    def test_identify_cats_pass(self):
        res = self.idb.identify_cats_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 选择鉴定商品page空
    def test_identify_cats_page_none(self):
        res = self.idb.identify_cats_page_none()
        assert res['code'] == 2
        assert res['msg'] == 'A non-numeric value encountered'

    # 选择鉴定商品limit空
    def test_identify_cats_limit_none(self):
        res = self.idb.identify_cats_limit_none()
        assert res['code'] == 2
        assert res['msg'] == 'A non-numeric value encountered'

    # 选择鉴定商品limit错误
    def test_identify_cats_limit_false(self):
        res = self.idb.identify_cats_limit_false()
        assert res['code'] == 2
        assert res['msg'] == 'A non-numeric value encountered'

    # 鉴定单列表pass
    def test_identify_center_pass(self):
        res = self.idb.identify_center_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 鉴定单列表status空
    def test_identify_center_status_none(self):
        res = self.idb.identify_center_status_none()
        assert res['code'] == 400
        assert res['msg'] == '状态不正确'

        # 鉴定单列表page空
    def test_identify_center_page_none(self):
        res = self.idb.identify_center_page_none()
        assert res['code'] == 2
        assert res['msg'] == 'A non-numeric value encountered'

    # 鉴定单列表status错误
    def test_identify_center_status_false(self):
        res = self.idb.identify_center_status_false()
        assert res['code'] == 400
        assert res['msg'] == '状态不正确'

        # 鉴定单列表page错误
    def test_identify_center_page_false(self):
        res = self.idb.identify_center_page_false()
        assert res['code'] == 2
        assert res['msg'] == 'A non-numeric value encountered'

    # 鉴定单详情
    def test_identify_center_detail_pass(self):
        res = self.idb.identify_center_detail_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 鉴定单详情orderid空
    def test_identify_center_detail_orderid_none(self):
        res = self.idb.identify_center_detail_orderid_none()
        assert res['code'] == 999999
        assert res['msg'] == '您不能查看他人的订单'

    # 鉴定单详情orderid错误
    def test_identify_center_detail_orderid_false(self):
        res = self.idb.identify_center_detail_orderid_false()
        assert res['code'] == 999999
        assert res['msg'] == '您不能查看他人的订单'

        # 获取商品鉴定信息
    def test_identify_records_pass(self):
        res = self.idb.identify_records_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

        # 获取商品鉴定信息orderid空
    def test_identify_records_orderid_none(self):
        res = self.idb.identify_records_orderid_none()
        assert res['code'] == 4000
        assert res['msg'] == '订单id必传'

        # 获取商品鉴定信息orderid错误
    def test_identify_records_orderid_false(self):
        res = self.idb.identify_records_orderid_false()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 鉴定报告详情pass
    def test_identify_report_detail_pass(self):
        res = self.idb.identify_report_detail_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 鉴定报告详情identifyid空
    def test_identify_report_detail_identifyid_none(self):
        res = self.idb.identify_report_detail_identifyid_none()
        assert res['code'] == 4000
        assert res['msg'] == '订单不存在'

    # 鉴定报告详情identifyid错误
    def test_identify_report_detail_identifyid_false(self):
        res = self.idb.identify_report_detail_identifyid_false()
        assert res['code'] == 4000
        assert res['msg'] == '订单不存在'

    # 商品清单
    def test_identify_center_list_pass(self):
        res = self.idb.identify_center_list_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'







if __name__ == '__main__':
    pytest.main()