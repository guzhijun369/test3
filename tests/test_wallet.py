import time
from utomarket.util import explicit_wait
from utomarket.utomarket import Utomarket


def test_withdraw_internal_inner():  # 内部转账
    ins = Utomarket('test129', '3201')
    address = '37jzbkEiZW4KfY7ueFLiXtnCJbu98Ay7wS'
    amount = '0.0005'
    method = '内部'
    ins.login().withdraw_internal(address, amount)
    ins.after_withdraw_internal(address, amount, method)
    time.sleep(2)
    ins.browser.close()


def test_withdraw_internal_out():   # 外部转账
    ins = Utomarket('test129', '3201')
    address = '3Cni6jyLVEYL73dVJYN6zasVryLWbJtAAb'
    amount = '0.0005'
    method = '外部'
    ins.login().withdraw_internal(address, amount).after_withdraw_internal(address, amount, method)
    time.sleep(2)
    ins.browser.close()


def test_withdraw_myself():    # 转给自己
    ins = Utomarket('test129', '3201')
    address = '34eSJjag5rRWsjPsiwp45rosnqYmteYwWq'
    amount = '0.0005'
    ins.login().withdraw_internal(address, amount)
    explicit_wait(ins.browser, 'VOEL', ['ant-message-custom-content', 'class'])
    notice = ins.browser.find_element_by_class_name('ant-message-custom-content').find_element_by_tag_name('span').text
    assert notice == '不能转账给自己'
    ins.browser.close()
