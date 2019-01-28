
def get_code(browser, code):
    captcha_xpath = browser.find_element_by_id('code') #获取图形验证码输入框
    captcha_xpath.send_keys(code)
    confirm_btn = browser.find_elements_by_css_selector('button[type="submit"]')[1]#获取弹窗确定按钮
    confirm_btn.click()