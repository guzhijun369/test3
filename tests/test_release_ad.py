from utomarket.utomarket import Utomarket
from utomarket.util import explicit_wait, get_current_url
from utomarket.settings import Settings
import time


def test_release_buy_ad():  # 发布购买广告，浮动价格
    ins = Utomarket('test129', '3201')
    ins.login().ad_btn('购买').release_ad(transaction_type='浮动价格')
    ins.browser.close()


def test_release_shell_ad():  # 发布出售广告，固定价格
    ins = Utomarket('test129', '3201')
    ins.login().ad_btn('出售').release_ad(transaction_type='固定价格', payment_method='微信支付',
                                        transaction_volume='1.8887', min_volume='100',
                                        max_volume='20,000', payment_limit='11', trading_term
                                        ='这是自动化的出售广告的交易条款')
    ins.browser.close()

# def test_delete_ad():  # 清空账号广告
#     ins = Utomarket('test129', '3201')
#     ins.login().enter_menu('广告管理').remove_ad().delete_ad()