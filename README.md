# 一个小小的自动生成headers的模块
It's ElectroUnity, not European Union!

非常简单的小模块，主要是本人懒得写headers搞的，没什么技术含量。

使用了fake_useragent这个库，别忘了装。

主要使用方法：
```
import headers

headers = headers.create_headers()
```
会自动返回一个假UA（随机，每次都不一样）：
```
# print(headers)效果
{'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8'}
```
