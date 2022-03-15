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


if __name__ == '__main__':
    pytest.main()
