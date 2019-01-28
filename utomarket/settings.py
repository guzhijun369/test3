import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings:
    log_location = os.path.join(BASE_DIR, 'logs')
    browser_language = 'zh-CN'
    loggers = {}
    login_url = 'https://dev.utomarket.com:9094/#/user/login'