"""Author: ElectroUnity
Date: Who cares?
"""
from fake_useragent import UserAgent

ua = UserAgent()

def create_headers():
    ua_last = ua.random
    headers = {'User-Agent': ua_last}
    return headers # 返回一个字典
