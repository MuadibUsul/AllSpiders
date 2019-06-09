import time
import requests
import tornado.gen
import tornado.httpclient
import tornado.ioloop
from tornado import gen


N = 3
URL = "http://localhost:8888/sleep"


@gen.coroutine
def main():
    http_client =tornado.httpclient.AsyncHTTPClient()
    response = yield [
        http_client.fetch(URL) for i in range(N)
    ]


beg1 = time.time()
tornado.ioloop.IOLoop.current().run_sync(main)
print("asunc", time.time()-beg1)

beg = time.time()
for i in range(N):
    requests.get(URL)
print("req", time.time()-beg)
