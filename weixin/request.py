# coding=utf-8
from weixin.config import *
from requests import Request

'''
[重写Request模块]
'''


class WeixinRequest(Request):
    '''
    该类的对象是一个整体,每个对象都有其专有属性
    '''

    def __init__(self, url, callback, method='GET', headers=None, need_proxy=False, fail_time=0, timeout=TIMEOUT):
        # 继承调用Request中的方法
        Request.__init__(self, method, url, headers)
        # 添加额外的参数 +--
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout
