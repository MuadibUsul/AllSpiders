import datetime
import time
from send_msg import send_gm
from update import Update
import sys


sys.setrecursionlimit(1000000)


class Timer:
    def __init__(self):
        self.x = datetime.datetime.now().year
        self.y = datetime.datetime.now().month
        self.z = datetime.datetime.now().day
        print("起始时间为"+str(self.x)+"-"+str(self.y)+"-"+str(self.z))
        self.h = int(input("请输入你要定时的时间（24小时制）:"))

    def timekeeper(self):
        nowTime = datetime.datetime.now()
        startTime = datetime.datetime(self.x, self.y, self.z, self.h, 0)
        print(nowTime)
        print(startTime)
        if nowTime >= startTime:
            print("开始发送天气预报")
            # 发送消息给目标
            send_gm()
            print("天气预报发送成功")
            self.z += 1
            # 更新时间
            Update(self.x, self.y, self.z)
            self.timekeeper()
        else:
            time.sleep(60)
            # 再次调用
            self.timekeeper()


Timer().timekeeper()
