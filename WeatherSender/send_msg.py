import wxpy
from GM_elf import getlocalweather


def send_gm():
    # 初始化一个机器人
    # console_qr = True
    bot = wxpy.Bot(cache_path=True)
    # 返回使用者的所有好友名称
    # 创建一个聊天对象
    friend = bot.friends().search("GoodDay")
    # 从列表中取出联系人
    bestfriend = wxpy.ensure_one(found=friend)
    # 获取天气信息
    message = getlocalweather()
    # 发送消息给指定联系人
    bestfriend.send(message)
    print("Send Success!")