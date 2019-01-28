from utomarket.util import explicit_wait
from utomarket.utomarket import Utomarket
import time
from utomarket.util import is_exist_element, navigator_to, get_current_url


def test_change_mail():  # 修改邮箱
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').change_mail('284468321@qq.com', '3201')
    ins.browser.close()


def test_band_telephone():  # 绑定手机号
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').band_telephone('13028857899', '3201', '中国')
    ins.browser.close()


def test_upload_avatar():  # 上传头像
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').upload_avatar()
    ins.browser.close()


def test_change_telephone():  # 修改手机号
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').change_telephone('13028718489', '3201', '中国')
    ins.browser.close()


def test_band_google():  # 绑定谷歌验证码
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').band_google('3201').stop_google('3201')
    ins.browser.close()


def test_change_pw():  # 修改密码
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').change_pw('3201', '3201', 'q5310543', '邮箱').change_pw('3201', '3201', 'q5310543',
                                                                                        '手机')
    ins.browser.close()


def test_auth():  # C1、C2认证
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').auth_c1('谷志军', '431081199103136091').auth_c2().my_center("个人中心")
    grade = ins.browser.find_element_by_xpath("//span[contains(text(),'认证等级')]/..")
    assert grade.text == '认证等级: C2'
    ins.browser.close()


def test_add_alipay():  # 添加支付方式并删除
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').payment_alipay('支付宝', '谷志军', '13028812388', 'fesdffds.jpg'). \
        payment_alipay('PayTm', '这是paytm', '13027788555812388', 'fesdffds.jpg'). \
        payment_alipay('微信支付', '这是微信支付', '13027788812388', 'fesdffds.jpg'). \
        payment_western_union("西联汇款", "谷志军", "这是西联付款详细信息大理石科技发达"
                                             "时间里凯迪拉克撒娇大厦就说的是肯定撒爱撒"
                                             "娇的萨克拉萨大家快来啊圣诞快乐就打算离开"). \
        payment_bank("银行卡", "谷志军", "兴业银行高新园支行", "55467843454546545")
    # add_btn = ins.browser.find_element_by_xpath("//span[contains(text(),'添加新的支付方式')]/..")
    status = is_exist_element(ins.browser, "xpath", "//span[contains(text(),'添加新的支付方式')]/..")
    assert not status
    for _ in range(1, 6):
        time.sleep(2)
        ins.delete_payment()
    ins.browser.close()


def test_others_information_nologin():  # 未登录状态下查看他人用户信息
    ins = Utomarket('uitest7', '3201')
    url = 'https://dev.utomarket.com:9094'
    navigator_to(ins.browser, url)
    ins.others_information()
    ins.browser.close()


def test_others_information():  # 已登录状态下查看他人用户信息
    ins = Utomarket('uitest7', '3201')
    ins.login().others_information()
    url = get_current_url(ins.browser)
    url_true = 'https://dev.utomarket.com:9094/#/personage'
    assert url_true in url
    ins.browser.close()


def test_band_google_login():  # 绑定谷歌后登录
    ins = Utomarket('uitest7', '3201')
    ins.login().my_center('个人中心').band_google('3201').logout('退出登录').login_two().my_center('个人中心').stop_google('3201')
    ins.browser.close()