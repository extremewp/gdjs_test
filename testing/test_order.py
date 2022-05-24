import pytest

from util.order_data_base import OrderDataBase


class TestOrder:
    def setup(self):
        self.odb = OrderDataBase()

    # 订单详细pass
    def test_order_detail_pass(self):
        res = self.odb.order_detail_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'
        # res['']

    # 订单详细id 空
    def test_order_detail_id_none(self):
        res = self.odb.order_detail_id_none()
        assert res['code'] == 1
        assert res['msg'] == '请求失败~'

    # 订单详细id错误
    def test_order_detail_id_false(self):
        res = self.odb.order_detail_id_false()
        assert res['code'] == 4000
        assert res['msg'] == '订单不存在'

    # 我的订单_all_pass
    def test_order_all_pass(self):
        res = self.odb.order_all_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 我的订单待付款_pass
    def test_order_wait_pay_pass(self):
        res = self.odb.order_wait_pay_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 我的订单待发货_pass
    def test_order_wait_send_pass(self):
        res = self.odb.order_wait_send_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 我的订单待收货_pass
    def test_order_wait_received_pass(self):
        res = self.odb.order_wait_received_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 我的订单交易成功_pass
    def test_order_ok_pass(self):
        res = self.odb.order_ok_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 我的订单交易关闭_pass
    def test_order_fail_pass(self):
        res = self.odb.order_fail_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 我的订单status空
    def test_order_status_none(self):
        res = self.odb.order_status_none()
        assert res['code'] == 4000
        assert res['msg'] == '订单类型不存在'

    # 我的订单status错误
    def test_order_status_false(self):
        res = self.odb.order_status_false()
        assert res['code'] == 4000
        assert res['msg'] == '订单类型不存在'

    # 创建订单-pass
    def test_createorder_pass(self):
        res = self.odb.createorder_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 创建订单-超出最大数量
    def test_createorder_maxmun_false(self):
        res = self.odb.createorder_maxmun_false()
        assert res['code'] == 1
        assert res['msg'] == '库存不足~'

    # 获取下单详情pass
    def test_order_get_order_info_pass(self):
        res = self.odb.order_get_order_info_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 获取下单详情id空
    def test_order_get_order_info_id_none(self):
        res = self.odb.order_get_order_info_id_none()
        print(res)
        assert res['code'] == 4000
        assert res['msg'] == '商品id不能为空'

    # 获取下单详情id空
    def test_order_get_order_info_id_false(self):
        res = self.odb.order_get_order_info_id_false()
        assert res['code'] == 40000
        assert res['msg'] == '商品信息不存在'

    def test_order_is_can_stock_pass(self):
        res = self.odb.order_is_can_stock_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    def test_order_is_can_stock_goodsid_none(self):
        res = self.odb.order_is_can_stock_goodsid_none()
        assert res['code'] == 4000
        assert res['msg'] == '商品id不能为空'

    def test_order_is_can_stock_goodsid_false(self):
        res = self.odb.order_is_can_stock_goodsid_false()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 账户信息
    def test_ipaynow_index_pass(self):
        res = self.odb.ipaynow_index_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    #     取消订单
    def test_order_cancel(self):
        res = self.odb.order_cancel()
        assert res['code'] == 0
        assert res['msg'] == 'success'



if __name__ == '__main__':
    pytest.main()
