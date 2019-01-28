import time
import random
from contextlib import contextmanager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException

from pymouse import PyMouse
from pykeyboard import PyKeyboard

def get_current_url(browser):#获取url
    try:
        current_url = browser.execute_script("return window.location.href")
    except WebDriverException:
        try:
            current_url = browser.current_url
        except WebDriverException:
            current_url = None

    return current_url


def explicit_wait(browser, track, ec_params, logger=None, timeout=30):#等待
    if not isinstance(ec_params, list):
        ec_params = [ec_params]

    if track == "VOEL":
        elem_address, find_method = ec_params
        ec_name = "visibility of element located"

        m = {
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'id': By.ID,
            'class': By.CLASS_NAME,
        }

        find_by = m.get(find_method)
        if not find_by:
            return False

        locator = (find_by, elem_address)
        condition = ec.visibility_of_element_located(locator)

    elif track == "TC":
        expect_in_title = ec_params[0]
        ec_name = "title contains '{}'".format(expect_in_title)
        condition = ec.title_contains(expect_in_title)

    elif track == "PFL":
        ec_name = "page fully loaded"
        condition = (lambda browser: browser.execute_script("return document.readyState") in ["complete" or "loaded"])

    try:
        wait = WebDriverWait(browser, timeout)
        result = wait.until(condition)
    except TimeoutException:
        if logger:
            logger.info("timeout with failure while explicitly waiting until {}!".format(ec_name))

        return False

    return result

# def explicit_wait_not(browser, track, ec_params, logger=None, timeout=30):#等待
#     if not isinstance(ec_params, list):
#         ec_params = [ec_params]
#
#     if track == "VOEL":
#         elem_address, find_method = ec_params
#         ec_name = "visibility of element located"
#
#         find_by = (By.XPATH if find_method == "xpath" else
#                    By.CSS_SELECTOR if find_method == "css" else
#                    By.CLASS_NAME if find_method == "id" else
#                    By.ID)
#         locator = (find_by, elem_address)
#         condition = ec.visibility_of_element_located(locator)
#     try:
#         wait = WebDriverWait(browser, timeout)
#         result = wait.until_not(condition)
#     except TimeoutException:
#         if logger:
#             logger.info("timeout with failure while explicitly waiting until {}!".format(ec_name))
#
#         return False
#
#     return result

# def find(browser, track, ec_params):
#     if track == 'class':
#         pass
#     elif track == 'xpath':
#         pass
#     elif track == 'id':
#         pass
#     elif track == 'tag_name':

def reload_webpage(browser): #刷新页面
    browser.execute_script("location.reload()")


def get_page_title(browser, logger=None):#获取title
    explicit_wait(browser, "PFL", [], logger, 10)

    try:
        page_title = browser.title
    except WebDriverException:
        try:
            page_title = browser.execute_script("return document.title")
        except WebDriverException:
            try:
                page_title = browser.execute_script("return document.getElementsByTagName('title')[0].text")
            except WebDriverException:
                if logger:
                    logger.info("Unable to find the title of the page")

                return None

    return page_title


def smart_input(element, text):#输入间隔
    for c in text:
        element.send_keys(c)
        time.sleep(0.2)


def click_element(browser, element, try_times=0):#点击事件
    try:
        element.click()
    except Exception:
        if try_times == 0:
            browser.execute_script("document.getElementsByClassName('" + element.get_attribute(
                "class") + "')[0].scrollIntoView({ inline: 'center' });")
        elif try_times == 1:
            browser.execute_script("window.scrollTo(0,0);")
        elif try_times == 2:
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        else:
            browser.execute_script(
                "document.getElementsByClassName('" + element.get_attribute("class") + "')[0].click()")
            return

        time.sleep(1)
        try_times += 1
        click_element(browser, element, try_times)


@contextmanager
def new_tab(browser):
    try:
        browser.execute_script("window.open()")
        time.sleep(2)

        browser.switch_to.window(browser.window_handles[1])
        time.sleep(1)
        yield
    finally:
        browser.execute_script("window.close()")
        time.sleep(1)

        browser.switch_to.window(browser.window_handles[0])
        time.sleep(1)


def navigator_to(browser, url):
    browser.maximize_window()
    current_url = get_current_url(browser)
    if current_url and current_url.endswith('/'):
        current_url = current_url[:-1]

    if url and url.endswith('/'):
        url = url[:-1]

    retry_times = 0
    new_navigation = (current_url != url)
    if current_url is None or new_navigation:
        while True:
            try:
                browser.get(url)
                break
            except TimeoutException as e:
                if retry_times >= 3:
                    raise TimeoutException("Retried {} times to GET '{}' webpage "
                                           "but failed out of a timeout!\n\t{}".format(retry_times, str(url), str(e)))
                retry_times += 1
                time.sleep(1)


def is_exist_element(browser, track, keyword):  # 判断元素是否存在
    if track == 'class':
        s = browser.find_elements_by_class_name(keyword)
    elif track == 'css':
        s = browser.find_elements_by_css_selector(keyword)
    elif track == 'xpath':
        s = browser.find_elements_by_xpath(keyword)
    elif track == 'id':
        s = browser.find_elements_by_id(keyword)
    else:
        return False
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True
    else:
        return False

def upload(file_name, path=r'C:\Users\Administrator\Desktop\ui\photos'):
    kk = PyKeyboard()  # 实例化
    time.sleep(1)
    kk.tap_key(kk.shift_key)  # 切换为英文，看实际情况是否需要
    # kk.tap_key(kk.shift_key)
    time.sleep(4)
    kk.type_string(path)  # 打开文件所在目录，方便多个文件上传
    time.sleep(1)
    kk.tap_key(kk.enter_key)
    time.sleep(1)
    kk.type_string(file_name)  # 多文件上传
    time.sleep(1)
    kk.tap_key(kk.enter_key)
