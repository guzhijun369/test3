from utomarket.utomarket import Utomarket
from utomarket.util import *
from utomarket.settings import Settings
import time


def test_get_current_url():
    ins = Utomarket('test129', '3201')
    ins.login()

    assert get_current_url(ins.browser) == Settings.login_url
    time.sleep(2)
    ins.browser.close()


def test_reload_webpage():
    ins = Utomarket('test129', '3201')
    ins.login()

    for _ in range(3):
        reload_webpage(ins.browser)
    time.sleep(2)
    ins.browser.close()


def test_get_page_title():
    ins = Utomarket('test129', '3201')
    ins.login()
    assert ins.browser.title == '乌托市场(TEST)'
    time.sleep(2)
    ins.browser.close()


def test_center():  # 进入个人中心
    ins = Utomarket('test129', '3201')
    ins.login()
    ins.my_center('个人中心')
    assert get_current_url(ins.browser) == 'https://dev.utomarket.com:9094/#/user-center/index'
    time.sleep(2)
    ins.browser.close()


def test_order():  # 进入我的订单
    ins = Utomarket('test129', '3201')
    ins.login()
    ins.my_center('我的订单')
    assert get_current_url(ins.browser) == 'https://dev.utomarket.com:9094/#/order/my'
    time.sleep(2)
    ins.browser.close()


def test_buy_btn():  # 导航栏购买
    ins = Utomarket('test129', '3201')
    ins.login()
    ins.enter_menu('购买')
    time.sleep(2)
    ins.browser.close()


def test_sell_btn():  # 导航栏出售
    ins = Utomarket('test129', '3201')
    ins.login()
    ins.enter_menu('出售')
    time.sleep(2)
    ins.browser.close()


def test_ad_home_btn():  # 导航栏广告管理
    ins = Utomarket('test129', '3201')
    ins.login()
    ins.enter_menu('广告管理')
    time.sleep(2)
    ins.browser.close()


def test_switch_language():  # 切换语言
    ins = Utomarket('test129', '3201')
    ins.login().switch_language("English")
    ins.browser.close()


def test_ad_screen():  # 首页筛选
    ins = Utomarket('test129', '3201')
    ins.login().ad_screen("全部国家", "全部币种", "全部支付方式")
    ins.browser.close()


def test_cut_type():  # 首页切换广告
    ins = Utomarket('test129', '3201')
    ins.login().cut_type("出售")
    ins.browser.close()