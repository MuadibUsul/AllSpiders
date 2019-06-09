import re
import time
import requests
from search_key import Search

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) "
                  "Chrome/17.0.963.56 Safari/535.11 "
}


def next_img_url(page_url):
    """
    获取一个网页地址，将地址返回资源中的所有iamge_url提取出来
    :param page_url:
    :return:
    """
    # 取到页面ＵＲＬ并用requests的get方法请求资源
    html = requests.get(page_url).text
    print(html)
    # 正则表达式规则，筛选图片URL
    rule = '''data-photo-modal-download-url=\\\\'(.*?)&amp'''
    # 查找所有符合规则的字符串，并返回一个列表
    image_urls = re.findall(rule, html)
    # print(image_urls)
    for img in image_urls:
        # 重组成可用的URL
        image_url = re.search("[a-zA-z]+://[^\s]*", img).group()
        # print(image_url)
        yield image_url


def search():
    search = Search()
    user_info = search.use_search()
    return user_info


def next_page_url():
    """
    接受一个x，代表获取多少页
    :param x:
    :return:
    """
    user_info = search()
    for num in range(0, user_info[1]):
        page_url = user_info[0] + str(num)
        # 生成页面ＵＲＬ
        yield page_url


def save_img(img_url, x):
    """
    保存获取到地址的图片
    :param img_url:
    :param x:
    :return:
    """
    try:
        # 请求图片URL，保存至img
        print("**********************************************************************")
        print("开始抓取第%s个图片" % x)
        img = requests.get(img_url, headers=headers)
        print("已获取第%s个图片" % x)
        img_path = "./images/" + str(x) + ".jpeg"
        # 以二进制的形式将图片写入文件
        with open(img_path, "wb") as fileobj:
            fileobj.writelines(img)
            print("保存%s成功" % img_path)
        print("**********************************************************************")
    except Exception as e:
        print(e.error)


def main():
    """
    整合调度，运行起来
    :param page_nums:
    :return:
    """
    x = 1
    for page_url in next_page_url():
        # 拿到页面URL
        img_url = next_img_url(page_url)
        # 提取页面的图片URL
        for img in img_url:
            print(img)
            # 保存图片URL
            save_img(img, x)
            x += 1
            print("休眠中")
            time.sleep(1)


if __name__ == '__main__':
    main()  # 运行调度函数main()
