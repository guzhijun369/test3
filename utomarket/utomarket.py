import os
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import WebDriverException

from .settings import Settings
from .login_util import login_user, login_user_two
from .wallet_util import enter_wallet_home, do_withdraw_internal, after_withdraw
from .logout_util import *
from .release_ad import *
from .register_util import *
from .personal_center_util import *
from .transaction import *


class UtomarketError(Exception):
    pass


class Utomarket:
    def __init__(self,
                 username=None,
                 password=None,
                 headless_browser=False,
                 disable_image_load=False,
                 proxy_address=None,
                 proxy_port=None,
                 browser_profile_path=None,
                 page_delay=25,
                 multi_logs=True,
                 show_log_in_console=True,
                 ):

        self.username = username
        self.password = password
        self.browser = None
        self.headless_browser = headless_browser
        self.disable_image_load = disable_image_load
        self.proxy_address = proxy_address
        self.proxy_port = proxy_port
        self.browser_profile_path = browser_profile_path
        self.page_delay = page_delay
        self.multi_logs = multi_logs
        self.show_log_in_console = show_log_in_console

        self._init_logger()
        self._init_browser()

    def _init_logger(self):
        self.log_folder = Settings.log_location + os.path.sep
        if self.multi_logs:
            self.log_folder = '{0}{1}{2}{1}'.format(Settings.log_location, os.path.sep, self.username)

        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

        self.logger = self._get_logger(self.show_log_in_console)

    def _init_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--disable-setuid-sandbox')

        if self.headless_browser:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')

            if self.disable_image_load:
                chrome_options.add_argument('--blink-settings=imagesEnabled=false')

            # Replaces browser User Agent from "HeadlessChrome".
            user_agent = "Chrome"
            chrome_options.add_argument('user-agent={user_agent}'.format(user_agent=user_agent))

        capabilities = DesiredCapabilities.CHROME

        if self.proxy_address and self.proxy_port:
            prox = Proxy()
            proxy = ":".join([self.proxy_address, str(self.proxy_port)])
            prox.proxy_type = ProxyType.MANUAL
            prox.http_proxy = proxy
            prox.socks_proxy = proxy
            prox.ssl_proxy = proxy
            prox.add_to_capabilities(capabilities)

        if self.browser_profile_path is not None:
            chrome_options.add_argument('user-data-dir={}'.format(self.browser_profile_path))

        chrome_prefs = {
            'intl.accept_languages': Settings.browser_language,
        }

        if self.disable_image_load:
            chrome_prefs['profile.managed_default_content_settings.images'] = 2

        chrome_options.add_experimental_option('prefs', chrome_prefs)
        try:
            self.browser = webdriver.Chrome(desired_capabilities=capabilities, chrome_options=chrome_options)
        except WebDriverException as exc:
            self.logger.exception(exc)
            raise UtomarketError('初始化chrome失败')

        self.browser.implicitly_wait(self.page_delay)

    def _get_logger(self, show_log_in_console):
        existing_logger = Settings.loggers.get(self.username)
        if existing_logger is not None:
            return existing_logger
        else:
            # initialize and setup logging system for the InstaPy object
            logger = logging.getLogger(self.username)
            logger.setLevel(logging.DEBUG)
            file_handler = logging.FileHandler('{}general.log'.format(self.log_folder))
            file_handler.setLevel(logging.DEBUG)
            extra = {"username": self.username}
            logger_formatter = logging.Formatter('%(levelname)s [%(asctime)s] [%(username)s]  %(message)s',
                                                 datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(logger_formatter)
            logger.addHandler(file_handler)

            if show_log_in_console:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.DEBUG)
                console_handler.setFormatter(logger_formatter)
                logger.addHandler(console_handler)

            logger = logging.LoggerAdapter(logger, extra)

            Settings.loggers[self.username] = logger
            Settings.logger = logger
            return logger

    def get_url(self):
        now_url = get_current_url(self.browser)

        return now_url

    def login(self):
        login_user(self.browser, self.username, self.password, self.logger)

        return self

    def login_two(self):
        login_user_two(self.browser, self.username, self.password, self.logger)
        # google_login(self.browser)

        return self

    def withdraw_internal(self, address, amount):
        enter_wallet_home(self.browser)
        do_withdraw_internal(self.browser, address, amount)

        return self

    def after_withdraw_internal(self, address, amount, method):
        after_withdraw(self.browser, address, amount, method)

        return self

    def top_notice_internal(self):
        top_notice_o(self.browser)

        return self

    def popup(self, text):
        popup_o(text)

        return self

    def logout(self, menu):
        logout_o(self.browser, self.logger, menu)

        return self

    def register(self, email, code, country, invitation_code):
        register_test(self.browser, email, code, self.username, self.password, country, invitation_code)

        return self

    def forget(self, verification_mode, account, code, new_pw):
        forget_pw(self.browser, verification_mode, account, code, new_pw)

        return self

    def my_center(self, menu):
        user_info(self.browser, menu)

        return self

    def ad_btn(self, menu):
        ad_management(self.browser, menu)

        return self

    def enter_menu(self, menu):
        enter_menu_o(self.browser, menu)

        return self

    def upload_avatar(self):
        upload_avatar_o(self.browser)

        return self

    def change_mail(self, email, code):
        change_mail_o(self.browser, email, code)

        return self

    def band_telephone(self, phone, code, country):
        band_telephone_o(self.browser, phone, code, country)

        return self

    def change_telephone(self, phone, code, country):
        change_telephone_o(self.browser, phone, code, country)

        return self

    def band_google(self, code):
        band_google_o(self.browser, code)

        return self

    def stop_google(self, code):
        stop_google_o(self.browser, code)

        return self

    def change_pw(self, code, old_pw, new_pw, method):
        change_pw_o(self.browser, code, old_pw, new_pw, method)

        return self

    def auth_c1(self, name, id_number):
        auth_c1_o(self.browser, name, id_number)

        return self

    def auth_c2(self):
        auth_c2_o(self.browser)

        return self

    def payment_alipay(self, method, name, account, receipt_code):
        payment_alipay_o(self.browser, method, name, account, receipt_code)

        return self

    def payment_bank(self, method, name, account, card_number):
        payment_bank_o(self.browser, method, name, account, card_number)

        return self

    def payment_western_union(self, method, name, transfer_information):
        payment_western_union_o(self.browser, method, name, transfer_information)

        return self

    def delete_payment(self):
        delete_payment_o(self.browser)

        return self

    def switch_language(self, language):
        switch_language_o(self.browser, language)

        return self

    def ad_screen(self, country, currency, payment_method):
        ad_screen_o(self.browser, country, currency, payment_method)

        return self

    def cut_type(self, btn):
        cut_type_o(self.browser, btn)

        return self

    def others_information(self):
        others_information_o(self.browser)

        return self

    def release_ad(self, **kwags):
        release_ad_o(self.browser, **kwags)

        return self

    def ad_detail(self, name):
        ad_detail_o(self.browser, name)

        return self

    def create_buy(self, **kwargs):
        create_buy_o(self.browser, **kwargs)

        return self

    def progress_order(self):
        progress_order_o(self.browser)

        return self

    def send_massege(self, massege_content):
        send_massege_o(self.browser, massege_content)

        return self

    def judge_massege_result(self, massege_content):
        judge_massege_result_o(self.browser, massege_content)

        return self

    def cancel_order_buyer(self):
        cancel_order_buyer_o(self.browser)

        return self

    def cancel_order_seller(self):
        cancel_order_seller_o(self.browser)

        return self

    def confirm_payment_buyer(self):
        confirm_payment_buyer_o(self.browser)

        return self

    def confirm_payment_seller(self):
        confirm_payment_seller_o(self.browser)

        return self

    def confirm_release_buyer(self):
        confirm_release_buyer_o(self.browser)

        return self

    def confirm_release_seller(self):
        confirm_release_seller_o(self.browser)

        return self

    def order_rating(self, **kwargs):
        order_rating_o(self.browser, **kwargs)

        return self

    def remove_ad(self):
        remove_ad_o(self.browser)

        return self

    def delete_ad(self):
        delete_ad_o(self.browser)

        return self