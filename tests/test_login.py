from utomarket.utomarket import Utomarket
from utomarket.util import get_page_title, explicit_wait


def test_login():  # 登录
    cases = [
        ('test129', '3201', 'success'),
        ('test119', '3202', '用户名密码错误'),
        ('test1120', '3202', '用户不存在')
    ]

    for case in cases:
        ins = Utomarket(case[0], case[1])
        ins.login()

        if case[2] == 'success':
            explicit_wait(ins.browser, 'TC', 'P2P交易 - 乌托市场(TEST)')
            assert get_page_title(ins.browser) == 'P2P交易 - 乌托市场(TEST)'
            ins.browser.close()
        elif case[2] == '用户名密码错误':
            span_errmsg = ins.browser.find_element_by_class_name('ant-alert-message').text
            assert span_errmsg == '用户名或密码错误'
            ins.browser.close()
        elif case[2] == '用户不存在':
            span_errmsg = ins.browser.find_element_by_class_name('ant-alert-message').text
            assert span_errmsg == '用户不存在'
            ins.browser.close()
        # def test_band_google_login():
        #     ins = Utomarket('niriliya', '3201')
        #     ins.login().my_center('个人中心').band_google('3201').logout('退出登录').login()




        # explicit_wait(ins.browser, 'TC', 'P2P交易 - 乌托市场(TEST)')
        # explicit_wait(ins.browser, 'VOEL', ['//*[@id="root"]/div/div/div[2]/div[1]/div/div/span[1]/span[1]/a/span/span', 'xpath'], timeout=5)
