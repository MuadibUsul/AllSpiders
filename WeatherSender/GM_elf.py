import requests


def getlocalweather():
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    key = 'dfbaa5dce05a9dfe64413d20c3dbb57a'
    myname = input("请输入你的名字（你想被对方看到的名字）：")
    yourname = input("请输入接收方的名字（你想如何称呼对方）：")
    data = {'key': key, "city": 530100}
    req = requests.post(url, data)
    info = dict(req.json())
    info = dict(info)
    newinfo = info['lives'][0]
    message = yourname + "，早上好。我是"+myname+"。\n\n亲爱的你现在位于"+newinfo['province'] + newinfo['city'] + \
              "。\n\n经过了一晚上的休息，现在一定神清气爽吧！\n\n" \
              "现在是" + newinfo['reporttime'] + "，又是新的一天哟。\n\n" \
              "今天天气状态为"+newinfo['weather']+"\n\n气温"+newinfo['temperature']+"℃\n\n" \
              ""+newinfo['winddirection']+"风，风力"+newinfo['windpower']+"级" \
              "\n\n相对湿度为"+newinfo['humidity']+"%，" \
              "\n\n祝你度过美好的一天 "
    return message
