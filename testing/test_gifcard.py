import pytest

from util.gifcard_data_base import GifcardDataBase


class TestGifcard:
    def setup(self):
        self.gdb = GifcardDataBase()

    # 创建礼品卡
    def test_giftcard_pass(self):
        res = self.gdb.giftcard_pass()
        print(res)
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 创建礼品卡重复创建
    def test_giftcard_pass_repeat(self):
        res = self.gdb.giftcard_pass_repeat()
        assert res['code'] == 110001
        assert res['msg'] == '该存酒已经生成礼品卡了，快去分享吧！'

    # 创建礼品卡epcode错误
    def test_giftcard_epcode_false(self):
        res = self.gdb.giftcard_epcode_false()
        assert res['code'] == 4000
        assert res['msg'] == '没有查询到对应存酒'

    # 创建礼品卡epcode空
    def test_giftcard_epcode_none(self):
        res = self.gdb.giftcard_epcode_none()
        assert res['code'] == 302
        assert res['msg'] == '参数错误'

    # 礼品卡列表（云仓）
    def test_giftcard_list_pass(self):
        res = self.gdb.giftcard_list_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 撤回礼品卡sku_id空
    def test_giftcard_delete_giftcard_none(self):
        res = self.gdb.giftcard_delete_giftcard_none()
        assert res['code'] == 100003
        assert res['msg'] == '礼品卡不存在'

    # 撤回礼品卡sku_id空
    def test_giftcard_delete_skuid_none(self):
        res = self.gdb.giftcard_delete_skuid_none()
        assert res['code'] == 101027
        assert res['msg'] == '商品不存在'

    # 分享礼品卡_pass
    def test_share_giftcard_pass(self):
        res = self.gdb.share_giftcard_pass()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    # 撤回礼品卡giftcard空
    def test_giftcard_delete_giftcard_none(self):
        res = self.gdb.giftcard_delete_giftcard_none()
        assert res['code'] == 100003
        assert res['msg'] == '礼品卡不存在'

    # 分享礼品卡_giftcard_id空
    def test_share_giftcard_giftcardid_none(self):
        res = self.gdb.share_giftcard_giftcardid_none()
        assert res['code'] == 302
        assert res['msg'] == '参数错误'

    # 分享礼品卡_giftcard_id错误
    def test_share_giftcard_giftcardid_false(self):
        res = self.gdb.share_giftcard_giftcardid_false()
        assert res['code'] == 100003
        assert res['msg'] == '礼品卡不存在'

    # 撤回礼品卡
    def test_giftcard_delete(self):
        res = self.gdb.giftcard_delete()
        assert res['code'] == 0
        assert res['msg'] == 'success'

    def test_dasd(self):
        a = [1,2,3,4,]


if __name__ == '__main__':
    pytest.main()
