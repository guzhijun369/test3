from selenium.webdriver.common.action_chains import ActionChains
from utomarket.skip_util import select_country
from utomarket.util import *
from utomarket.settings import Settings
import time
from utomarket.get_code_util import *


def register_test(browser, email, code, username, pass_wd, country, invitation_code=None):  # 注册方法
    navigator_to(browser, Settings.login_url)  # 进入网站
    sign_btn = browser.find_element_by_xpath("//a[contains(text(),'注册账户')]")  # 获取注册按钮
    sign_btn.click()
    # logger.debug('注册开始')
    # btn_login_xpath = '//*[@id="root"]/div/div[1]/div[2]/form/div[9]/div/div/span/button'
    time.sleep(3)
    input_email = browser.find_element_by_id('email')  # 获取邮箱输入框
    input_code = browser.find_element_by_id('verify_code')  # 获取验证码输入框
    get_code_btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[1]/div[2]/form/div[2]/div[2]/div/span/div/div[2]/button')  # 获取验证码点击按钮
    input_username = browser.find_element_by_id('nickname')  # 获取昵称输入框
    input_pass_wd = browser.find_element_by_id('password')  # 获取密码输入框
    input_pass_wd_two = browser.find_element_by_id('confirm')  # 获取确认密码输入框
    input_country = browser.find_element_by_class_name('ant-select-selection--single')  # 获取国家选择输入框
    input_invitation_code = browser.find_element_by_id('invite_code')  # 获取邀请码输入框
    tick = browser.find_element_by_class_name('ant-checkbox-input')  # 获取勾选框
    register_btn = browser.find_element_by_xpath("//span[contains(text(),'注 册')]/..")  # 注册按钮
    input_email.send_keys(email)
    get_code_btn.click()
    time.sleep(1)
    get_code(browser, code)
    time.sleep(2)
    input_code.send_keys(code)
    input_username.send_keys(username)
    input_pass_wd.send_keys(pass_wd)
    input_pass_wd_two.send_keys(pass_wd)
    input_country.click()
    select_country(browser, country)
    input_invitation_code.send_keys(invitation_code)
    tick.click()
    register_btn.click()


def forget_pw(browser, verification_mode, account, code, new_pw, country='中国'):  # 忘记密码
    navigator_to(browser, Settings.login_url)  # 进入网站
    forget_btn = browser.find_element_by_link_text("忘记密码")  # 获取忘记密码按钮
    forget_btn.click()
    get_code_btn = browser.find_element_by_xpath("//span[contains(text(),'获取验证码')]/..")  # 获取验证码按钮
    input_country = browser.find_element_by_class_name('ant-select-selection--single')  # 获取验证方式框
    input_country.click()
    options = browser.find_elements_by_class_name('ant-select-dropdown-menu-item')
    if verification_mode == 'email':  # 邮箱验证
        options[1].click()
        time.sleep(1)
        input_email = browser.find_element_by_id('mail')  # 获取邮箱输入框
        print(account)
        input_email.send_keys(account)
    elif verification_mode == 'phone':  # 手机验证
        options[0].click()
        time.sleep(1)
        country_btn = browser.find_element_by_xpath('//*[@id="nation_code"]/div/div')
        country_btn.click()
        time.sleep(1)
        country_text = browser.find_elements_by_class_name('ant-select-dropdown-menu-item')  # 获取国家列表
        for itme in country_text:
            if itme.text == country:
                itme.click()
        input_phone = browser.find_element_by_id('phone')  # 获取手机输入框
        input_phone.send_keys(account)
    get_code_btn.click()
    captcha_xpaths = browser.find_elements_by_css_selector('input[placeholder="验证码"]')  # 获取图形验证码输入框
    captcha_xpaths[1].send_keys(code)
    confirm_btn = browser.find_elements_by_css_selector('button[type="submit"]')[1]  # 获取弹窗确定按钮
    confirm_btn.click()
    time.sleep(2)
    input_code = browser.find_element_by_id('code')  # 获取验证码输入框
    input_code.send_keys(code)

    next_btn = browser.find_element_by_xpath("//span[text()='下一步']/..")  # 获取下一步按钮
    # explicit_wait(ins.browser, 'VOEL', ['submit___B1_-n', 'class'])
    next_btn.click()
    time.sleep(1)
    input_new_pw = browser.find_element_by_id('new_password')  # 获取新密码输入框
    input_confirm_pw = browser.find_element_by_id('confirm')  # 获取确认密码输入框
    input_new_pw.send_keys(new_pw)
    input_confirm_pw.send_keys(new_pw)
    submit_btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[1]/div[2]/form/div[3]/div/div/span/button')  # 获取提交按钮
    submit_btn.click()
