"""Author: 
Date: 
"""
from fake_useragent import UserAgent

ua = UserAgent()


def create_headers():
    """
    :return:
    """
    ua_last = ua.random
    headers = {'User-Agent': ua_last}
    return headers
