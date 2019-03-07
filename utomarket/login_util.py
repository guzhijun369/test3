from selenium.webdriver.common.action_chains import ActionChains
# from utomarket.personal_center_util import band_google_o
from utomarket.util import *
from utomarket.settings import Settings


def login_user(browser, username, password, logger):
    logger.debug('开始登陆，用户名：{}，密码：{}'.format(username, password))

    navigator_to(browser, Settings.login_url)

    btn_login_xpath = '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div/form/div[3]/div/div/span/button'

    input_username = browser.find_element_by_id('account')
    input_password = browser.find_element_by_id('password')
    # input_captcha = browser.find_element_by_id('captcha')
    btn_login = browser.find_element_by_xpath(btn_login_xpath)

    explicit_wait(browser, "VOEL", [btn_login_xpath, "xpath"], logger)
    input_username.send_keys(username)
    input_password.send_keys(password)
    time.sleep(2)
    btn_login.click()
    # (ActionChains(browser).
    #  move_to_element(input_username).
    #  click().
    #  send_keys(username).
    #  move_to_element(input_password).
    #  click().
    #  send_keys(password).
    #  move_to_element(btn_login).
    #  click().
    #  perform())


def get_track(distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.2
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track



def sliding_verification_o(browser):
    explicit_wait(browser, 'VOEL', ["tcaptcha_iframe", 'id'])
    iframe = browser.find_element_by_id("tcaptcha_iframe")
    browser.switch_to.frame(iframe)
    time.sleep(3)
    explicit_wait(browser, 'VOEL', ["tcaptcha_drag_thumb", 'id'])
    distance = 185
    offset = 6
    times = 0
    slide_btn = browser.find_element_by_id('tcaptcha_drag_thumb')
    while True:
        action = ActionChains(browser)  # 实例化一个action对象
        action.click_and_hold(slide_btn).perform()  # perform()用来执行ActionChains中存储的行为
        action.reset_actions()
        track = get_track(distance)[6:] # 生成运动轨迹的列表
        print(sum(track))
        for i in track:
            action.move_by_offset(xoffset=i, yoffset=0).perform()
            action.reset_actions()
        time.sleep(0.5)
        ActionChains(browser).release().perform()
        time.sleep(3)
        try:
            alert = browser.find_element_by_id('tcaptcha_note').text
        except Exception as e:
            print('get alert error: %s' % e)
            alert=''
        if alert:
            print('滑块位移需要调整: %s' % alert)
            distance += offset
            times += 1
            time.sleep(5)
        else:
            print('滑块验证通过')
            browser.switch_to_default_content() # 验证成功后跳回最外层页面
            break


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
    print(google_code_input, '---------------------')
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
