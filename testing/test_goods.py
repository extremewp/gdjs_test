import pytest
import requests
import yaml

from util.goods_data_base import GoodsDataBase


class TestGoods:
    def setup(self):
        self.gdb = GoodsDataBase()

    def test_goods_stock_pass(self):
        res = self.gdb.goods_stock_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 极速卖列表pass
    def test_goods_rapid_recovery_pass(self):
        res = self.gdb.goods_rapid_recovery_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 卖家送货上门时间
    def test_goods_send_self_deliver(self):
        res = self.gdb.goods_send_self_deliver()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 切换商品年份pass
    def test_goods_switchyeargoods_pass(self):
        res = self.gdb.goods_switchyeargoods_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

        # 切换商品年份goodsid空
    def test_goods_switchyeargoods_goodsid_none(self):
        res = self.gdb.goods_switchyeargoods_goodsid_none()
        res['code'] == 0
        assert res['msg'] == 'success'
        assert res['data']['stock'] == None


    # 切换商品年份goodsid错误
    def test_goods_switchyeargoods_goodsid_false(self):
        res = self.gdb.goods_switchyeargoods_goodsid_false()
        assert res['code'] == 0
        assert res['msg'] == 'success'
        assert res['data']['stock'] == None

    # 自提时间选择
    def test_goods_send_list(self):
        res = self.gdb.goods_send_list()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 获取邮寄运费pass
    def test_order_get_express_fee_pass(self):
        res = self.gdb.order_get_express_fee_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 获取邮寄运费goodsid空
    def test_order_get_express_fee_goodsid_none(self):
        res = self.gdb.order_get_express_fee_goodsid_none()
        assert res['code'] == 4000
        assert res['msg'] == '商品id不能为空'

    # 获取邮寄运费num空
    def test_order_get_express_fee_num_none(self):
        res = self.gdb.order_get_express_fee_num_none()
        assert res['code'] == 4000
        assert res['msg'] == '商品数量不能为空'

    # 获取邮寄运费num错误
    def test_order_get_express_fee_num_false(self):
        res = self.gdb.order_get_express_fee_num_false()
        assert res['code'] == 4000
        assert res['msg'] == "商品数量不能为空"

    # 确认订单v3pass
    def test_oods_confirm_order_v3_pass(self):
        res = self.gdb.goods_confirm_order_v3_pass()
        assert res['code'] == 0
        assert res['msg'] == "success"

    # 确认订单v3goodsid空
    def test_oods_confirm_order_v3_goodsid_none(self):
        res = self.gdb.goods_confirm_order_v3_goodsid_none()
        assert res['code'] == 40000
        assert res['msg'] == "商品ID或数量不能为空"

    # 确认订单v3num空
    def test_oods_confirm_order_v3_num_none(self):
        res = self.gdb.goods_confirm_order_v3_num_none()
        assert res['code'] == 40000
        assert res['msg'] == '商品ID或数量不能为空'

    # 确认订单v3num错误
    def test_oods_confirm_order_v3_num_false(self):
        res = self.gdb.goods_confirm_order_v3_num_false()
        assert res['code'] == 2
        assert res['msg'] == "A non-numeric value encountered"


if __name__ == '__main__':
    pytest.main()