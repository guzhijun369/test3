

from utomarket.util import *

from .skip_util import *


def logout_o(browser, logger, menu):
    logger.debug("退出登录")
    user_info(browser, menu)
    btn_login_xpath = '//*[@id="root"]/div/div[1]/div[2]/div/form/div[4]/div/div/span/button'
    explicit_wait(browser, "VOEL", [btn_login_xpath, "xpath"], logger)

