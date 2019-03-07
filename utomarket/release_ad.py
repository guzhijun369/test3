from utomarket.skip_util import *

from utomarket.util import *
from selenium.webdriver.common.keys import Keys
from .personal_center_util import select_mode


# browser.find_element_by_xpath("//span[contains(text(),'获取验证码')]/..")
def release_ad_o(browser, country='中国', currency='人民币', transaction_type='固定价格', floating_ratio='99',
                 trading_price='20000',
                 payment_method='支付宝', transaction_volume='2', min_volume='100', max_volume='10,000',
                 payment_limit='10', trading_term=''):
    explicit_wait(browser, 'VOEL', ["//span[contains(text(),'广告规则')]", 'xpath'])
    time.sleep(2)
    country_btn = browser.find_element_by_xpath("//div[contains(text(),'请选择所在地')]/..")
    currency_btn = browser.find_element_by_xpath("//div[contains(text(),'请选择交易币种')]/..")
    transaction_type_button = browser.find_element_by_xpath("//div[contains(text(),'固定价格')]/..")
    trading_price_input = browser.find_element_by_xpath("//input[@placeholder='CNY/BTC']")
    payment_method_input = browser.find_element_by_xpath("//div[contains(text(),'请选择交易方式')]/..")
    transaction_volume_input = browser.find_element_by_id('max_count')
    min_volume_input = browser.find_element_by_id('min_volume')
    max_volume_input = browser.find_element_by_id('max_volume')
    payment_limit_input = browser.find_element_by_id('payment_limit')
    trading_term_input = browser.find_element_by_id('trading_term')
    release_btn = browser.find_element_by_xpath("//span[contains(text(),'确认发布')]/..")
    country_btn.click()
    select_mode(browser, country)
    currency_btn.click()
    select_mode(browser, currency)
    transaction_type_button.click()
    select_mode(browser, transaction_type)
    if transaction_type == "固定价格":
        trading_price_input.send_keys(trading_price)
    else:
        floating_ratio_btn = browser.find_element_by_id('trading_price_ratio')
        floating_ratio_btn.click()
        for _ in range(1, 4):
            floating_ratio_btn.send_keys(Keys.BACK_SPACE)
        floating_ratio_btn.send_keys(floating_ratio)
    payment_method_input.click()
    select_mode(browser, payment_method)
    transaction_volume_input.send_keys(transaction_volume)
    min_volume_input.send_keys(min_volume)
    max_volume_input.send_keys('1' + max_volume)
    payment_limit_input.send_keys(payment_limit)
    trading_term_input.send_keys(trading_term)
    release_btn.click()
    popup_o(browser, "操作成功")
    url = get_current_url(browser)
    url_true = 'https://dev.utomarket.com:9094/#/ad/my'
    list_transaction_type = browser.find_elements_by_class_name('ant-table-row-level-0')[-1]
    ad_btn = list_transaction_type.find_elements_by_tag_name("td")
    price_range_td = ad_btn[5]
    ad_type_td = ad_btn[2]
    # span_text = ad_type_td.find_elements_by_tag_name("span")[0].text
    transaction_type_text = ad_type_td.find_elements_by_tag_name("span")[1].text
    price_range_text = price_range_td.find_element_by_tag_name("span").text
    aa = '%s - %s CNY' % (min_volume, max_volume)
    assert url == url_true
    assert price_range_text == aa
    assert transaction_type_text == '(%s)' % transaction_type


def remove_ad_o(browser):
    explicit_wait(browser, 'VOEL', ["//span[contains(text(),'广告类型')]", 'xpath'])
    remove_btns = browser.find_elements_by_class_name('text-green')
    for item in remove_btns:
        item.click()
        popup_o("操作成功")
        time.sleep(2)


def delete_ad_o(browser):
    delete_btn = browser.find_elements_by_xpath("//span[contains(text(),'删除')]/..")
    for item in delete_btn:
        item.click()
        confirm_btn = browser.find_elements_by_xpath("//span[text()='确认']/..")
        confirm_btn.click()
        popup_o("操作成功")
        time.sleep(2)
