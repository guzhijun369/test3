from utomarket.utomarket import Utomarket
from utomarket.util import explicit_wait, get_current_url
from utomarket.settings import Settings
import time


def test_register():  # 注册
    username = 'uitest7'
    pw = 'q5310543'
    ins = Utomarket(username, pw)
    email = 'testui7@qq.com'
    ins.register(email, '3201', '中国', '3201')
    explicit_wait(ins.browser, 'VOEL', ["[//button[@type='button']", 'xpath'])
    btn = ins.browser.find_element_by_xpath("//div[contains(text(),'注册成功')]").text
    assert btn == '你的账户：%s 注册成功' % email
    ins.browser.close()


def test_forget():  # 忘记密码
    ins = Utomarket()
    accounts = [('email', '281878321@qq.com'),
                ('phone', '13028812388')
                ]
    code = '3201'
    pass_wd = 'q5310543'
    for way in accounts:
        ins.forget(way[0], way[1], code, pass_wd)
        explicit_wait(ins.browser, 'VOEL', ['title___17w4b', 'class'])
        txt = ins.browser.find_element_by_class_name('title___17w4b').text
        assert txt == '密码修改成功'
    login_btn = ins.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[3]/div/a[1]/button')
    login_btn.click()
    assert get_current_url(ins.browser) == Settings.login_url
    ins.browser.back()
    home_btn = ins.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[3]/div/a[2]/button')
    home_btn.click()
    url = 'https://dev.utomarket.com:9094/#/'
    url_true = get_current_url(ins.browser)
    assert url in url_true
    ins.browser.close()
