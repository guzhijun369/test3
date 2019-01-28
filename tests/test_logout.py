from utomarket.utomarket import Utomarket
import time


def test_logout():  # 退出登录
    ins = Utomarket('test129', '3201')
    ins.login()
    time.sleep(3)
    ins.logout('退出登录')
    now_url = ins.get_url()
    assert now_url == 'https://dev.utomarket.com:9094/#/user/login'
    ins.browser.close()
