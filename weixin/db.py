# coding=utf-8
from redis import StrictRedis
from weixin.config import *
from pickle import dumps, loads  # 使用该模块对'存取'做序列化及反序列化
from weixin.request import WeixinRequest

'''
[实现请求队列]
'''


class RedisQueue():
    def __init__(self):
        """
        初始化Redis
        """
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self, request):
        """
        向队列添加序列化后的Request
        :param request: 请求对象
        :param fail_time: 失败次数
        :return: 添加结果
        """
        # attention/ judge the typle +--
        if isinstance(request, WeixinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))
        return False

    def pop(self):
        """
        取出一个Request并反序列化
        :return: Request or None
        """
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def clear(self):
        '''
        清空列表
        :return:
        '''
        self.db.delete(REDIS_KEY)

    def empty(self):
        '''
        判断队列是否为空
        :return:
        '''
        return self.db.llen(REDIS_KEY) == 0


if __name__ == '__main__':  # for test +--
    db = RedisQueue()
    start_url = 'http://www.baidu.com'
    weixin_request = WeixinRequest(url=start_url, callback='hello', need_proxy=True)
    db.add(weixin_request)
    request = db.pop()
    print(request)
    print(request.callback, request.need_proxy)
