from fake_useragent import UserAgent

ua = UserAgent()

# 写爬虫最实用的是可以随意变换headers，一定要有随机性。支持随机生成请求头
print(ua.random)