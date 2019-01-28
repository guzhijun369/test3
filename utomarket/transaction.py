from utomarket.skip_util import *

from utomarket.util import *
from selenium.webdriver.common.keys import Keys
from .personal_center_util import select_mode


def ad_detail_o(browser, name):  # 进入广告详情
    ad_div = browser.find_element_by_xpath("//a[contains(text(),'%s')]/../../.." % name)
    click_btn = ad_div.find_elements_by_tag_name('td')[-1]
    click_btn.click()
    explicit_wait(browser, 'VOEL', ["ant-card-meta-avatar", 'class'])
    url = get_current_url(browser)
    url_true = 'https://dev.utomarket.com:9094/#/trade/detail'
    name_text = browser.find_element_by_class_name('ant-card-meta-title').text
    assert url_true in url
    assert name_text == name


def create_buy_o(browser, type='法币计价', trading_volume='1,234.24',
                     trading_count='0.2345871', trading_note='这是交易备注'):
    type_button = browser.find_element_by_xpath("//div[@title='法币计价']/..")
    trading_note_input = browser.find_element_by_id('trading_notes')  #创建购买订单
    submit_button = browser.find_elements_by_tag_name('button')[1]
    type_button.click()
    select_mode(browser, type)
    if type == '法币计价':
        trading_input = browser.find_element_by_id('trading_volume')
        trading_input.send_keys(trading_volume)
    else:
        trading_input = browser.find_element_by_id('trading_count')
        trading_input.send_keys(trading_count)
    trading_note_input.send_keys(trading_note)
    submit_button.click()
    popup_o(browser, '操作成功')
    explicit_wait(browser, 'VOEL', ["ant-list-item-content", 'class'])
    url = 'https://dev.utomarket.com:9094/#/trade/step'
    url_true = get_current_url(browser)
    if type == '法币计价':
        verify_div = is_exist_element(browser, 'xpath', "//span[text()='%s CNY ']" % trading_volume)
    else:
        verify_div = is_exist_element(browser, 'xpath', "//span[text()=' %s BTC']" % trading_count)
    assert url in url_true
    assert verify_div


def send_massege_o(browser, massege_content):  # 发送消息
    time.sleep(2)
    explicit_wait(browser, 'VOEL', ["ant-list-item-meta-content", 'class'])
    massege_input = browser.find_element_by_id('message')
    send_button = browser.find_element_by_xpath("//span[text()='发送']/..")
    smart_input(massege_input, massege_content)
    send_button.click()
    explicit_wait(browser, 'VOEL', ["//div[contains(text(),'%s')]" % massege_content, 'xpath'])
    judge_massege_result_o(browser, massege_content)


def judge_massege_result_o(browser, massege_content):  # 判断消息是否在聊天框显示
    result = is_exist_element(browser, 'xpath', "//div[contains(text(),'%s')]" % massege_content)
    assert result


def cancel_order_buyer_o(browser):  # 买家取消订单
    cancel_button = browser.find_element_by_xpath("//span[text()='取消订单']/..")
    cancel_button.click()
    explicit_wait(browser, 'VOEL', ["//textarea[@placeholder='请填写原因']", 'xpath'])
    reason_input = browser.find_element_by_xpath("//textarea[@placeholder='请填写原因']")
    confirm_btn = browser.find_element_by_xpath("//span[text()='确定']/..")
    smart_input(reason_input, '这是取消订单原因')
    confirm_btn.click()
    explicit_wait(browser, 'VOEL', ["//div[text()='买家已取消交易，订单已关闭。']", 'xpath'])
    m = is_exist_element(browser, 'xpath', "//span[text()='已取消']")  # 判断已取消状态的span有没有出现
    assert m


def cancel_order_seller_o(browser):  # 取消订单判断卖家页面
    explicit_wait(browser, 'VOEL', ["//div[text()='买家已取消交易，订单已关闭。']", 'xpath'])
    m = is_exist_element(browser, 'xpath', "//span[text()='已取消']")  # 判断已取消状态的span有没有出现
    assert m


def confirm_payment_buyer_o(browser):  # 买家确认支付
    confirm_payment_btn = browser.find_element_by_xpath("//span[text()='确认支付']/..")
    confirm_payment_btn.click()
    # explicit_wait(browser, 'VOEL', ["//span[text()='确 定']", 'xpath'])
    time.sleep(2)
    confirm_btn = browser.find_element_by_xpath("//span[text()='确 定']/..")
    print(confirm_btn, 'confirm_btn---------------')
    confirm_btn.click()
    explicit_wait(browser, 'VOEL', ["//div[text()='买家已付款，等待卖家确认']", 'xpath'])
    m = is_exist_element(browser, 'xpath', "//span[text()='申述']")  # 判断申述按钮有没有出现
    assert m


def confirm_payment_seller_o(browser):  # 确认支付后卖家页面判断
    explicit_wait(browser, 'VOEL', ["//div[text()='买家已付款，等待卖家确认']", 'xpath'])
    time.sleep(2)
    cancel_btn = is_exist_element(browser, 'xpath', "//span[text()='申述']")  # 判断申述按钮有没有出现
    confirm_release_btn = is_exist_element(browser, 'xpath', "//span[text()='确认释放']")  # 判断释放按钮有没有出现
    assert cancel_btn
    assert confirm_release_btn


def confirm_release_buyer_o(browser):  # 卖家确认释放
    confirm_release_btn = browser.find_element_by_xpath("//span[text()='确认释放']/..")
    confirm_release_btn.click()
    time.sleep(2)
    confirm_btn = browser.find_element_by_xpath("//span[text()='确 定']/..")
    confirm_btn.click()
    explicit_wait(browser, 'VOEL', ["//div[text()='卖家已释放托管BTC，请留意资产到账。']", 'xpath'])
    released_btn = is_exist_element(browser, 'xpath', "//span[text()='已释放']")
    good_rating_btn = is_exist_element(browser, 'xpath', "//span[text()='好评']")
    assert released_btn
    assert good_rating_btn


def confirm_release_seller_o(browser):  # 释放后卖家页面判断
    explicit_wait(browser, 'VOEL', ["//div[text()='卖家已释放托管BTC，请留意资产到账。']", 'xpath'])
    released_btn = is_exist_element(browser, 'xpath', "//span[text()='已释放']")
    rating_btn = is_exist_element(browser, 'xpath', "//span[text()='好评']")
    assert released_btn
    assert rating_btn


def order_rating_o(browser, content='和你合作真是太愉快了'):
    good_rating_btn = browser.find_element_by_xpath("//img[@alt='good']/..")
    print(good_rating_btn, 'good_rating_btn-----')
    rating_input = browser.find_element_by_id('content')
    submit_btn = browser.find_elements_by_class_name('ant-btn-primary')[0]
    print(submit_btn, 'submit_btn----')
    good_rating_btn.click()
    rating_input.clear()
    rating_input.send_keys(content)
    submit_btn.click()
    popup_o(browser, '操作成功')

