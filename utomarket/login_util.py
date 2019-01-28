from selenium.webdriver.common.action_chains import ActionChains
from utomarket.personal_center_util import band_google_o
from utomarket.util import *
from utomarket.settings import Settings


def login_user(browser, username, password, logger):
    logger.debug('开始登陆，用户名：{}，密码：{}'.format(username, password))

    navigator_to(browser, Settings.login_url)

    btn_login_xpath = '//*[@id="root"]/div/div[1]/div[2]/div/form/div[4]/div/div/span/button'

    input_username = browser.find_element_by_id('account')
    input_password = browser.find_element_by_id('password')
    input_captcha = browser.find_element_by_id('captcha')
    btn_login = browser.find_element_by_xpath(btn_login_xpath)

    explicit_wait(browser, "VOEL", [btn_login_xpath, "xpath"], logger)

    (ActionChains(browser).
     move_to_element(input_username).
     click().
     send_keys(username).
     move_to_element(input_password).
     click().
     send_keys(password).
     move_to_element(input_captcha).
     click().
     send_keys('3201').
     move_to_element(btn_login).
     click().
     perform())


def login_user_two(browser, username, password, logger):
    logger.debug('开始登陆，用户名：{}，密码：{}'.format(username, password))
    btn_login_xpath = '//*[@id="root"]/div/div[1]/div[2]/div/form/div[4]/div/div/span/button'
    input_username = browser.find_element_by_id('account')
    input_password = browser.find_element_by_id('password')
    input_captcha = browser.find_element_by_id('captcha')
    btn_login = browser.find_element_by_xpath(btn_login_xpath)
    explicit_wait(browser, "VOEL", [btn_login_xpath, "xpath"], logger)
    input_username.send_keys(username)
    input_password.send_keys(password)
    input_captcha.send_keys('3201')
    btn_login.click()
    explicit_wait(browser, "VOEL", ["//span[contains(text(),'确定')]", "xpath"])
    time.sleep(2)
    google_code_input = browser.find_element_by_id("code")
    print(google_code_input,'---------------------')
    submit_btn = browser.find_element_by_xpath("//span[contains(text(),'确定')]//..")
    google_code_input.send_keys('3201')
    submit_btn.click()
    time.sleep(3)



# def google_login(browser):
#     explicit_wait(browser, "VOEL", ['ant-modal-header', "xpath"])
#     google_input = browser.find_element_by_xpath('//input[@placeholder="谷歌验证码"]')
#     submit_btn = browser.find_element_by_xpath("//span[contains(text(),'确定')]//..")
#     google_input.send_keys('3201')
#     submit_btn.click()
#     explicit_wait(browser, 'TC', 'P2P交易 - 乌托市场(TEST)')
#     assert get_page_title(browser) == 'P2P交易 - 乌托市场(TEST)'
#     time.sleep(5)

#
#
#
# def register_user(email, username, password, country, invite_code=None):
#     pass
