from selenium.webdriver.common.action_chains import ActionChains

from pymouse import PyMouse
from pykeyboard import PyKeyboard

from random import choice
import time

from utomarket.skip_util import *

from utomarket.util import *
from utomarket.settings import Settings


def upload_avatar_o(browser):
    upload_btns = browser.find_elements_by_class_name('ant-btn')
    upload_btn = upload_btns[0]
    upload_btn.click()
    upload('20180917154817.JPEG')
    # kk = PyKeyboard()#实例化
    # time.sleep(1)
    # kk.tap_key(kk.shift_key)  # 切换为英文，看实际情况是否需要
    # time.sleep(1)
    # kk.type_string(r'C:\Users\Apple\Desktop\photos')  # 打开文件所在目录，方便多个文件上传
    # time.sleep(1)
    # kk.tap_key(kk.enter_key)
    # time.sleep(1)
    # kk.type_string('20180917154817.JPEG')  # 多文件上传
    # time.sleep(1)
    # kk.tap_key(kk.enter_key)
    popup_o(browser, '修改头像成功')


def get_code(browser, code, btn):
    get_code_btn = browser.find_element_by_xpath("//span[contains(text(),'获取验证码')]/..")
    code_input = browser.find_element_by_xpath("//input[@placeholder='验证码']")
    next_btn = browser.find_element_by_xpath("//span[contains(text(),'%s')]//.." % btn)
    print(next_btn, '-----------------------------')
    get_code_btn.click()
    popup_o(browser, '发送成功')
    code_input.send_keys(code)
    time.sleep(4)
    next_btn.click()


def select_mode(browser, method):
    time.sleep(1)
    method_btns = browser.find_elements_by_class_name('ant-select-dropdown-menu-item')
    for item in method_btns:
        if item.text == method:
            item.click()
            time.sleep(1)
            break


def change_mail_o(browser, email, code):
    change_btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/ul')
    change_btn.click()
    explicit_wait(browser, 'VOEL', ['getCaptcha___3e6Ch', 'class'])
    get_code(browser, code, '下一步')
    explicit_wait(browser, 'VOEL', ['ant-input', 'class'])
    new_email_input = browser.find_element_by_id('email')
    new_email_input.send_keys(email)
    get_code(browser, code, '下一步')
    popup_o(browser, '操作成功')
    time.sleep(5)


def band_telephone_o(browser, phone, code, country):
    bind_btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/ul')
    bind_btn.click()
    explicit_wait(browser, 'VOEL', ['ant-modal-title', 'class'])
    country_btn = browser.find_element_by_class_name('ant-select-selection__rendered')
    country_btn.click()
    time.sleep(1)
    select_country(browser, country)
    input_phone = browser.find_element_by_id('telephone')
    input_phone.send_keys(phone)
    get_code(browser, code, '下一步')
    popup_o(browser, '操作成功')


def change_telephone_o(browser, phone, code, country):
    change_btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/ul')
    change_btn.click()
    explicit_wait(browser, 'VOEL', ['ant-modal-title', 'class'])
    get_code(browser, code, '下一步')
    explicit_wait(browser, 'VOEL', ['ant-select-selection__rendered', 'class'])
    change_country_btn = browser.find_element_by_class_name('ant-select-selection__rendered')
    change_country_btn.click()
    time.sleep(1)
    select_country(browser, country)
    input_phone = browser.find_element_by_id('telephone')
    input_phone.send_keys(phone)
    get_code(browser, code, '下一步')
    popup_o(browser, '操作成功')


def band_google_o(browser, code):
    change_btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/ul')
    change_btn.click()
    explicit_wait(browser, 'VOEL', ['ant-card-head-title', 'class'])
    copy_btn = browser.find_element_by_class_name('anticon-copy')
    input_code = browser.find_element_by_id('captcha')
    tick = browser.find_element_by_xpath("//input[@type='checkbox']//..")
    start_using_btn = browser.find_element_by_xpath("//button[@type='submit']")
    copy_btn.click()
    popup_o(browser, '复制成功')
    input_code.send_keys(code)
    tick.click()
    time.sleep(3)
    start_using_btn.click()
    popup_o(browser, '操作成功')
    url = get_current_url(browser)
    assert url == 'https://dev.utomarket.com:9094/#/user-center/index'


def stop_google_o(browser, code):
    stop_btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/ul')
    stop_btn.click()
    explicit_wait(browser, 'VOEL', ['ant-modal-title', 'class'])
    code_input = browser.find_element_by_xpath("//input[@placeholder='谷歌验证码']")
    confirm_btn = browser.find_element_by_xpath("//button[@type='submit']")
    code_input.send_keys(code)
    confirm_btn.click()
    popup_o(browser, '操作成功')


def change_pw_o(browser, code, old_pw, new_pw, method):
    change_btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/ul')
    change_btn.click()
    explicit_wait(browser, 'VOEL', ['ant-modal-title', 'class'])
    method_btn = browser.find_element_by_xpath("//div[@role='combobox']")
    method_btn.click()
    time.sleep(1)
    options = browser.find_elements_by_class_name('ant-select-dropdown-menu-item')
    for item in options:
        if method in item.text:
            item.click()
            break
    time.sleep(2)
    get_code(browser, code, '确定')
    explicit_wait(browser, 'VOEL', ["//input[@id='old_password']", 'xpath'])
    old_input = browser.find_element_by_xpath("//input[@id='old_password']")
    new_input = browser.find_element_by_xpath("//input[@id='password']")
    confirm_input = browser.find_element_by_xpath("//input[@id='confirm']")
    next_btn = browser.find_element_by_xpath("//span[contains(text(),'下一步')]/..")
    old_input.send_keys(old_pw)
    new_input.send_keys(new_pw)
    confirm_input.send_keys(new_pw)
    next_btn.click()
    popup_o(browser, '操作成功')
    time.sleep(2)


def auth_c1_o(browser, name, id_number):
    certification_btn = browser.find_element_by_xpath("//span[contains(text(),'立即认证')]/..")
    certification_btn.click()
    explicit_wait(browser, 'VOEL', ["//input[@id='name']", 'xpath'])
    assert get_current_url(browser) == 'https://dev.utomarket.com:9094/#/authentication'
    name_input = browser.find_element_by_id('name')
    id_number_input = browser.find_element_by_id('number')
    submit_btn = browser.find_element_by_xpath("//span[contains(text(),'提交审核')]/..")
    name_input.send_keys(name)
    id_number_input.send_keys(id_number)
    submit_btn.click()


def auth_c2_o(browser):
    explicit_wait(browser, 'VOEL', ["anticon-check", 'class'])
    upload_btns = browser.find_elements_by_class_name('ant-form-item-control-wrapper')
    upload_btns[0].click()
    upload('0642.png')
    time.sleep(4)
    upload_btns[1].click()
    upload('160704.PNG')
    time.sleep(4)
    submit_btn = browser.find_element_by_class_name('ant-btn-primary')
    submit_btn.click()
    # explicit_wait(browser, 'VOEL', ["ant-alert-info", 'class'])
    time.sleep(15)
    browser.implicitly_wait(20)
    iframe = browser.find_element_by_tag_name("iframe")
    print(iframe, '---------------------------')
    browser.switch_to_frame(iframe)
    time.sleep(5)
    explicit_wait(browser, 'VOEL', ["jr-qrcode", 'id'])
    QR_code = browser.find_element_by_id('jr-qrcode')
    print(QR_code, '-----------------------')
    assert QR_code != None
    browser.switch_to_default_content()


def payment_alipay_o(browser, method, name, account, receipt_code):  # 支付宝、微信、paytm共用
    add_btn = browser.find_element_by_xpath("//span[contains(text(),'添加新的支付方式')]/..")
    add_btn.click()
    time.sleep(1)
    choose_input = browser.find_element_by_xpath("//div[contains(text(),'请选择支付方式')]/..")
    choose_input.click()
    time.sleep(2)
    select_mode(browser, method)
    explicit_wait(browser, 'VOEL', ['payment_detail.name', 'id'])
    name_input = browser.find_element_by_id('payment_detail.name')
    account_input = browser.find_element_by_id('payment_detail.account')
    code_btn = browser.find_element_by_class_name('ant-upload-drag')
    confirm_btn = browser.find_element_by_xpath("//span[contains(text(),'确定')]/..")
    name_input.send_keys(name)
    account_input.send_keys(account)
    code_btn.click()
    upload(receipt_code)
    time.sleep(4)
    confirm_btn.click()
    popup_o(browser, '操作成功')
    time.sleep(2)


def payment_bank_o(browser, method, name, account, card_number):
    add_btn = browser.find_element_by_xpath("//span[contains(text(),'添加新的支付方式')]/..")
    add_btn.click()
    time.sleep(1)
    choose_input = browser.find_element_by_xpath("//div[contains(text(),'请选择支付方式')]/..")
    choose_input.click()
    time.sleep(2)
    select_mode(browser, method)
    explicit_wait(browser, 'VOEL', ['payment_detail.name', 'id'])
    name_input = browser.find_element_by_id('payment_detail.name')
    account_input = browser.find_element_by_id('payment_detail.bank_name')
    card_number_input = browser.find_element_by_id('payment_detail.bank_account')
    confirm_btn = browser.find_element_by_xpath("//span[contains(text(),'确定')]/..")
    name_input.send_keys(name)
    account_input.send_keys(account)
    card_number_input.send_keys(card_number)
    confirm_btn.click()
    popup_o(browser, '操作成功')
    time.sleep(2)


def payment_western_union_o(browser, method, name, transfer_information):
    add_btn = browser.find_element_by_xpath("//span[contains(text(),'添加新的支付方式')]/..")
    add_btn.click()
    time.sleep(1)
    choose_input = browser.find_element_by_xpath("//div[contains(text(),'请选择支付方式')]/..")
    choose_input.click()
    time.sleep(2)
    select_mode(browser, method)
    explicit_wait(browser, 'VOEL', ['payment_detail.name', 'id'])
    name_input = browser.find_element_by_id('payment_detail.name')
    confirm_btn = browser.find_element_by_xpath("//span[contains(text(),'确定')]/..")
    transfer_information_input = browser.find_element_by_id('payment_detail.account')
    name_input.send_keys(name)
    transfer_information_input.send_keys(transfer_information)
    confirm_btn.click()
    popup_o(browser, '操作成功')
    time.sleep(2)


def delete_payment_o(browser):
    delete_btns = browser.find_elements_by_class_name('text-red')
    choice(delete_btns).click()
    confirm_btn = browser.find_element_by_xpath("//span[contains(text(),'确 定')]/..")
    print(confirm_btn, '-----------------------------')
    time.sleep(1)
    confirm_btn.click()
    popup_o(browser, '操作成功')


def others_information_o(browser):
    name_a = browser.find_elements_by_xpath('//a[contains(@href,"#/personage")]')
    choice(name_a).click()
