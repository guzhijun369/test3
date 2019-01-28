from utomarket.util import explicit_wait
from utomarket.utomarket import Utomarket


def test_top_notice():  # 置顶公告
    ins = Utomarket('test129', '3201')
    ins.login().top_notice_internal()
    ins.browser.close()