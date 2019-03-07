from utomarket.util import *
# from utomarket.logout_util import *
from selenium.webdriver.common.action_chains import ActionChains
import re


def user_info(browser, menu):  # 移到头像显示下拉菜单点击菜单
    btn_info = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/div/span[1]/span[4]/span')
    ActionChains(browser).move_to_element(btn_info).perform()
    time.sleep(2)
    btc_item = browser.find_element_by_xpath("//span[contains(text(),'%s')]/.." % menu)
    btc_item.click()


def ad_management(browser, menu):  # 移动到广告管理
    time.sleep(2)
    btn_ad = browser.find_element_by_xpath('//div[@title="广告中心"]/..')
    ActionChains(browser).move_to_element(btn_ad).perform()
    # explicit_wait(browser, 'VOEL', ["//span[contains(text(),'广告管理')]", 'xpath'])
    time.sleep(2)
    btc_item = browser.find_element_by_xpath("//span[text()='%s']/../.." % menu)
    btc_item.click()


def enter_menu_o(browser, menu):
    ad_management(browser, menu)
    if menu == '购买':
        assert get_current_url(browser) == 'https://dev.utomarket.com:9094/#/ad/buy'
    elif menu == '出售':
        assert get_current_url(browser) == 'https://dev.utomarket.com:9094/#/ad/sell'
    else:
        assert get_current_url(browser) == 'https://dev.utomarket.com:9094/#/ad/my'


def top_notice_o(browser):  # 置顶公告
    info_btn = browser.find_element_by_class_name('system_notice___3cCZX')
    info_text = info_btn.find_element_by_tag_name('a').text
    info_btn.click()
    title_text = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]').text
    time.sleep(1)
    back_btn = browser.find_element_by_xpath("//a[contains(text(),'返回')]")
    back_btn.click()
    time.sleep(1)
    result = is_exist_element(browser, 'xpath', '//*[@id="root"]/div/div/div/div[2]/div/div/div[2]')
    assert info_text == title_text
    assert result


def popup_o(browser, text):  # 判断操作结果弹窗
    explicit_wait(browser, 'VOEL', ['ant-message-custom-content', 'class'])
    notice = browser.find_element_by_class_name('ant-message-custom-content').find_element_by_tag_name('span').text
    assert notice == text


def select_country(browser, country):  # 下拉列表选择
    time.sleep(2)
    country_text = browser.find_elements_by_class_name('ant-select-dropdown-menu-item')  # 获取国家列表
    for itme in country_text:
        if itme.text == country:
            itme.click()
            time.sleep(1)
            break


def switch_language_o(browser, language):
    language_btn = browser.find_elements_by_class_name('ant-dropdown-trigger')[0]
    ActionChains(browser).move_to_element(language_btn).perform()
    time.sleep(2)
    zh_btn = browser.find_element_by_xpath("//li[contains(text(),'%s')]" % language)
    zh_btn.click()
    browser.implicitly_wait(20)
    ad_btn = browser.find_element_by_class_name('ant-menu-submenu-title')
    assert ad_btn.text == 'Advertisement Center'


# def choice_button(browser, target):#筛选下拉框选择元素
#     time.sleep(2)
#     elements = browser.find_elements_by_class_name('ant-select-dropdown-menu-item')
#     for item in elements:
#         if item.text == target:
#             item.click()
#             break

def ad_screen_o(browser, country, currency, payment_method):
    explicit_wait(browser, 'VOEL', ["search_box___2kIFM", 'class'])
    screen_btn = browser.find_element_by_class_name("search_box___2kIFM")
    screen_btn.click()
    time.sleep(2)
    # btns = browser.find_elements_by_class_name('ant-select-selection__rendered')
    # country_btn = btns[0]
    # currency_btn = btns[1]
    # payment_method_btn = btns[2]
    country_btn = browser.find_element_by_xpath("//div[@title='全部国家']/..")
    currency_btn = browser.find_element_by_xpath("//div[@title='全部币种']/..")
    payment_method_btn = browser.find_element_by_xpath("//div[@title='全部支付方式']/..")
    submit_btn = browser.find_element_by_xpath("//span[contains(text(),'查询')]/..")
    country_btn.click()
    select_country(browser, country)
    time.sleep(1)
    currency_btn.click()
    select_country(browser, currency)
    time.sleep(1)
    payment_method_btn.click()
    select_country(browser, payment_method)
    time.sleep(1)
    submit_btn.click()
    time.sleep(2)
    status = is_exist_element(browser, "xpath", "//span[contains(text(),'查询')]/..")
    assert not status


def cut_type_o(browser, btn):
    explicit_wait(browser, 'VOEL', ["//button[contains(text(),'%s')]" % btn, 'xpath'])
    cut_btn = browser.find_element_by_xpath("//button[contains(text(),'%s')]" % btn)
    cut_btn.click()
    # url = get_current_url(browser)
    # if btn == "出售":
    #     assert url == 'https://dev.utomarket.com:9094/#/trade/index?ad_type=1'
    # else:
    #     assert url == 'https://dev.utomarket.com:9094/#/trade/index?ad_type=2'
    # rgb = cut_btn.value_of_css_property('color')
    # print(rgb, '-----------------')
    # r, g, b = map(int, re.search(
    #     r'rgba\((\d+),\s*(\d+),\s*(\d+)', rgb).groups())
    # color = '#%02x%02x%02x' % (r, g, b)
    # print(color)
    # assert color == '#ffffff'
    active = cut_btn.get_attribute('class')
    print(active)
    class_name = 'bt_trade_tabs_active'
    assert class_name in active

def progress_order_o(browser):
    clock_button = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/div/span[1]/span[2]/span')
    clock_button.click()
    explicit_wait(browser, 'VOEL', ["ant-list-item-meta-content", 'class'])
    order_list = browser.find_element_by_class_name('ant-list-item-meta-content')
    order_list.click()
    explicit_wait(browser, 'VOEL', ["ant-list-item-content", 'class'])
    url = 'https://dev.utomarket.com:9094/#/trade/step'
    url_true = get_current_url(browser)
    assert url in url_true


