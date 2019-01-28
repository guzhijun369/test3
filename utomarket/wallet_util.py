from selenium.webdriver.common.action_chains import ActionChains

from utomarket.util import *


def enter_wallet_home(browser):
    btn_wallet_xpath = '//*[@id="root"]/div/div/div/div[1]/div/div/span[1]/span[1]/a/span/span'
    explicit_wait(browser, 'VOEL', [btn_wallet_xpath, 'xpath'])

    btn_wallet = browser.find_element_by_xpath(btn_wallet_xpath)
    click_element(browser, btn_wallet)


def do_withdraw_internal(browser, address, amount):
    tab_withdraw_xpath = '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[1]'
    explicit_wait(browser, 'VOEL', [tab_withdraw_xpath, 'xpath'])

    tab_withdraw = browser.find_element_by_xpath(tab_withdraw_xpath)
    input_address = browser.find_element_by_id('address')
    input_amount= browser.find_element_by_id('amount')
    btn_commit = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/form/div[4]/div/div/span/button')

    (ActionChains(browser).
        move_to_element(tab_withdraw).
        click().
        move_to_element(input_address).
        click().
        send_keys(address).
        move_to_element(input_amount).
        click().
        send_keys(amount).
        move_to_element(btn_commit).
        click().
        perform())

def after_withdraw(browser, address, amount, method):
    trading_record_xpath = '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]'
    explicit_wait(browser, 'VOEL', [trading_record_xpath, 'xpath'])
    frozen_money = browser.find_elements_by_class_name('text-blue')
    stutas_btn = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[4]')
    fee_btn = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[3]')
    amount_list = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[2]')
    address_list = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]')
    if method == '内部':
        assert frozen_money[1].text == '0 BTC'
        assert stutas_btn.text == '已完成'
        assert fee_btn.text == '-'
        assert amount_list.text == '- %s'%amount
        assert address_list.text == address
    elif method == '外部':
        assert frozen_money[1].text == '%s BTC'%amount
        assert stutas_btn.text == '待审核'
        assert fee_btn.text == '0.00005'
        assert amount_list.text == '- %s'%amount
        assert address_list.text == address


