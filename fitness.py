import re
import time
import random

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
}
pat = re.compile('''"video_url":"(.+?).mp4''')
pat2 = re.compile('''content="(.+?)：类型：(.+?)，级别：(.+?)，主要肌肉群：(.+?)，其他肌肉：(.+?)，器械要求：(.+?)"''')


# 将编号拼装成URL
def get_page_url():
    for i in range(231, 1603):
        url = "https://www.hiyd.com/dongzuo/" + str(i)
        yield url


# 从页面中获取GIF的URL和NAME,并生成一个字典迭代器
def get_gif_info():
    for url in get_page_url():
        gif_box = {}
        page_html = requests.get(url, headers=headers).text
        video_urls = re.findall(pat, page_html)
        for video_url in video_urls:
            gif_url = video_url.replace('\\', "") + ".mp4"
        # yield gif_url
        video_name = re.findall(pat2, page_html)
        gif_name = ''
        for i in video_name[0]:
            gif_name = gif_name + i + "_"
        # yield gif_name
        gif_box[gif_name] = gif_url
        yield gif_box


# 从字典中取出URL和NAME，并将其保存至同目录下的gif文件夹
def save_gif():
    for gif_dict in get_gif_info():
        for gif_item in gif_dict:
            gif = requests.get(gif_dict[gif_item], headers=headers)
            print("开始写入" + gif_item)
            # print("url="+gif_dict[gif_item])
            try:
                with open("./gif/" + gif_item + ".mp4", "wb") as file_object:
                    file_object.writelines(gif)
                print("写入" + gif_item + "成功")
                time.sleep(timer())
            except Exception as e:
                continue


def timer():
    random_time = random.uniform(1.0, 3.0)
    return random_time


# main函数为调度函数
def main():
    print("hiyd健身动图爬虫开始运行")
    save_gif()
    print("爬取完成")


if __name__ == '__main__':
    main()
