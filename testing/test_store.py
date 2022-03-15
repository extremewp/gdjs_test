import pytest
import requests

from util.store_data_base import StoreDataBase


class TestStore:
    def setup(self):
        self.sdb=StoreDataBase()

    # 酒库详情页pass
    def test_store_goods_detail_pass(self):
        res = self.sdb.store_goods_detail_pass()
        assert res['code']==0
        assert res['msg']=='success'

        # 酒库详情页bn空
    def test_store_goods_detail_bn_none(self):
        res = self.sdb.store_goods_detail_bn_none()
        assert res['code'] == 999999
        assert res['msg'] == '网络异常~'

     # 酒库详情页type空
    def test_store_goods_detail_type_none(self):
        res = self.sdb.store_goods_detail_type_none()
        assert res['code'] == 999999
        assert res['msg'] == 'Argument 3 passed to app\\modules\\repository\\controllers\\RepositoryController::actionSkuInfo() must be of the type integer or null, string given'
        # data ={
        #         "method": "get",
        #         "headers": {"token": "j40union_cdb554e4e3aa5ac30cbe752e423f3959"},
        #         "url": "http://192.168.50.102:886/store/goods/detail",
        #         "params": {
        #             "bn": "BJ000041",
        #             "type":"" ,
        #         }}
        # res = requests.request(**data)
        # print(res.json())
    # 酒库详情页bn错误
    def test_store_goods_detail_bn_false(self):
        res = self.sdb.store_goods_detail_bn_false()
        assert res['code'] == 999999
        assert res['msg'] == '商品无库存'

    # 酒库详情页type错误
    def test_store_goods_detail_type_false(self):
        res = self.sdb.store_goods_detail_type_false()
        assert res['code'] == 999999
        assert res['msg'] == 'Argument 3 passed to app\\modules\\repository\\controllers\\RepositoryController::actionSkuInfo() must be of the type integer or null, string given'

    # 商品详细pass
    def test_store_bn_pass(self):
        res = self.sdb.store_bn_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'
    # 用户酒库库存接口pass
    def test_store_stock_pass(self):
        res = self.sdb.store_stock_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 酒库详情列表 - SKU
    def test_store_goods_pass(self):
        res = self.sdb.store_goods_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'


    # 酒库详情根据epcode
    def test_store_goods_info_pass(self):
        res = self.sdb.store_goods_info_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 酒库详情根据epcode空
    def test_store_goods_info_epcode_none(self):
        res = self.sdb.store_goods_info_epcode_none()
        assert res['code'] == 4000
        assert res['msg'] == 'epcode不能为空'

    # 我的酒库列表
    def test_store2020_pass(self):
        res = self.sdb.store2020_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 酒库sku详情
    def test_store_sku_detail_pass(self):
        res = self.sdb.store_sku_detail_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'
if __name__ == '__main__':
    pytest.main()