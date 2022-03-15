import pytest
import requests
import yaml

from util.user_data_base import UserDataBase


class TestUser:
    def setup(self):
        self.ut = UserDataBase()

    # 登录正确
    def test_login_pass(self):
        res = self.ut.longin_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 登录错误
    def test_login_file(self):
        res = self.ut.login_file()
        assert res['code'] == 4000
        assert res['msg'] == "验证码无效"

    # 登录空
    def test_login_none(self):
        res = self.ut.login_none()
        assert res['code'] == 4000
        assert res['msg'] == "登录类型和授权码不能为空"

    #    我卖出的
    def test_shell(self):
        res = self.ut.shell()
        assert res['code'] == 0
        assert res['msg'] == "success"

    #  用户信息
    def test_user(self):
        res = self.ut.user()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 用户销售数据统计
    def test_user_dashboard(self):
        res = self.ut.user_dashboard()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 获取上传头像oss授权
    def test_upload_avatar_auth(self):
        res = self.ut.upload_avatar_auth()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 修改用户信息
    def test_user_update_pass(self):
        res = self.ut.user_update_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 修改用户信息type为空
    def test_user_update_type_none(self):
        res = self.ut.user_update_type_none()
        assert res['code'] == 4000
        assert res['msg'] == "入参错误"

    # 修改用户信息value为空
    def test_user_update_value_none(self):
        res = self.ut.user_update_value_none()
        assert res['code'] == 999999
        assert res['msg'] == "value不能为空"

    # 查看地址列表
    def test_user_address(self):
        res = self.ut.user_address()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 添加收货地址pass
    def test_user_address_pass(self):
        res = self.ut.user_address_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 添加收货地址name空
    def test_user_address_name_none(self):
        res = self.ut.user_address_name_none()
        assert res['code'] == 4000
        assert res['msg'] == "保存失败"

    # 添加收货地址mobile空
    def test_user_address_mobile_none(self):
        res = self.ut.user_address_mobile_none()
        assert res['code'] == 4000
        assert res['msg'] == "保存失败"

    # 更新收货地址
    def test_user_address_update_pass(self):
        res = self.ut.user_address_update_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 更新收货地址name空·
    def test_user_address_update_name_none(self):
        res = self.ut.user_address_update_name_none()
        assert res['code'] == 4000
        assert res['msg'] == "保存失败"

    # 删除地址
    def test_user_address_delect_pass(self):
        res = self.ut.user_address_delect_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 删除地址id错误
    def test_user_address_delect_file(self):
        res = self.ut.user_address_delect_file()
        assert res['code'] == 4000
        assert res['msg'] == "当前用户无此ID"

        # 收货地址详情

    def test_user_address_detail_pass(self):
        res = self.ut.user_address_detail_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 收货地址详情id空
    def test_user_address_detail_id_none(self):
        res = self.ut.user_address_detail_id_none()
        assert res['code'] == 4000
        assert res['msg'] == "addresId不能为空"

    # 收货地址详情id错误
    def test_user_address_detail_id_file(self):
        res = self.ut.user_address_detail_id_file()
        assert res['code'] == 4000
        assert res['msg'] == "地址不存在"

    # 交易流水(我买的|我卖的)_pass
    def test_order_detail_filter_pass(self):
        res = self.ut.order_detail_filter_pass()
        print(res)
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 交易流水(我买的|我卖的)_page空
    def test_order_detail_filter_page_none(self):
        res = self.ut.order_detail_filter_page_none()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 交易流水(我买的|我卖的)_page错误
    def test_order_detail_filter_page_file(self):
        res = self.ut.order_detail_filter_page_file()
        assert res['code'] == 8
        assert res['msg'] == "Undefined variable: data"

    # 交易流水，我的取货pass
    def test_order_take_detail_filter_pass(self):
        res = self.ut.order_take_detail_filter_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 交易流水，我的取货pass
    def test_order_take_detail_filter_pass(self):
        res = self.ut.order_take_detail_filter_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 交易流水，我的取货page空
    def test_order_take_detail_filter_page_none(self):
        res = self.ut.order_take_detail_filter_page_none()
        assert res['code'] == 0
        assert res['msg'] == "success"

        # 交易流水，我的取货page错误

    def test_order_take_detail_filter_page_false(self):
        res = self.ut.order_take_detail_filter_page_false()
        assert res['code'] == 8
        assert res['msg'] == "A non well formed numeric value encountered"

    # 我的资产pass
    def test_user_coupon_pass(self):
        res = self.ut.user_coupon_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 我的资产page错误
    def test_user_coupon_page_false(self):
        res = self.ut.user_coupon_page_false()
        assert res['code'] == 8
        assert res['msg'] == "A non well formed numeric value encountered"

    #    默认地址
    def test_user_default_address(self):
        res = self.ut.user_default_address()
        assert res['code'] == 0
        assert res['msg'] == "success"



if __name__ == '__main__':
    pytest.main()
