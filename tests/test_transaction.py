from utomarket.utomarket import Utomarket
from utomarket.util import explicit_wait, get_current_url
from utomarket.settings import Settings
import time


def test_ad_detail():  # 出售广告详情
    # ins_owner = Utomarket('test129', '3201')  # 广告主
    ins_trader = Utomarket('test128', '3201')  # 交易对象
    ins_trader.login().ad_detail('test129')
    ins_trader.browser.close()


def test_cancel_order():  # 取消订单
    # ins_owner = Utomarket('test129', '3201')  # 广告主
    ins_trader = Utomarket('test128', '3201')  # 交易对象
    massege_content = '你是傻逼斯达克警方扩大解放开绿灯顺'
    ins_trader.login().ad_detail('test129').create_buy(type='交易数量').send_massege(massege_content)
    ins_owner = Utomarket('test129', '3201')  # 广告主
    ins_owner.login().progress_order()
    ins_owner.judge_massege_result(massege_content)
    ins_trader.cancel_order_buyer()
    ins_owner.cancel_order_seller()
    ins_trader.browser.close()
    ins_owner.browser.close()


def test_buy_process():  # 主动购买全流程
    ins_trader = Utomarket('test128', '3201')  # 买家
    massege_content = '你是傻逼斯达克警方扩大解放开绿灯顺丰快递副书记撒大陆军撒'
    ins_trader.login().ad_detail('test129').create_buy(type='交易数量').send_massege(massege_content)
    ins_owner = Utomarket('test129', '3201')  # 卖家
    ins_owner.login().progress_order()
    ins_owner.judge_massege_result(massege_content)
    ins_trader.confirm_payment_buyer()
    ins_owner.confirm_payment_seller().send_massege("你好，我已经支付了")
    ins_trader.judge_massege_result("你好，我已经支付了")
    ins_owner.confirm_release_buyer()
    ins_trader.confirm_release_seller()
    ins_owner.order_rating(content='这是卖家的交易评价')
    ins_trader.order_rating(content='这是买家的交易评价')
    ins_trader.browser.close()
    ins_owner.browser.close()
