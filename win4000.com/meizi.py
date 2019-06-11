import requests
from lxml import etree
import re

start_url = "http://www.win4000.com/meitu.html"


# page_url = "http://www.win4000.com/meinv179495.html"


# 从开始ＵＲＬ解析出四个分类ＵＲＬ
def parse_start_url(start_url):
    response = requests.get(start_url)

    html = etree.HTML(response.text)

    results = html.xpath("//div[@class='list_cont list_cont2 w1180']/div[1]/a/@href")

    return results


# 从分类ＵＲＬ中解析出，获取写真集首页
def get_page_url(page_url):
    response = requests.get(page_url)

    html = etree.HTML(response.text)

    results = html.xpath("//div[contains(@class,'Left_bar')]//li//a/@href")

    return results


# 　获取写真集大图的图的数量
def parse_page_url(page_url):
    response = requests.get(page_url)

    html = etree.HTML(response.text)

    img_num = html.xpath("//div[@class='ptitle']/em/text()")

    return img_num[0]


# 通过图的数量拼接图的页面url
def parse_img_url(page_url, num):

    port_of_url = page_url.rstrip('.html')

    for i in range(1, num + 1):

        url = port_of_url + "_" + str(i) + ".html"

        response = requests.get(url)

        html = etree.HTML(response.text)

        img_url = html.xpath("//img[@class='pic-large']/@url")

        name = re.search(r'\/(\w*?.jpg)', img_url[0]).group(1)

        yield img_url[0], name


# 下载图片到指定路径
def download_img(img_url, name):

    image = requests.get(img_url).content

    path = './images/' + name

    fp = open(path, "wb+")

    fp.write(image)

    fp.close()


if __name__ == '__main__':
    for category in parse_start_url(start_url):
        for page_url in get_page_url(category):
            number = parse_page_url(page_url)
            for image in parse_img_url(page_url, int(number)):
                print(image)
                download_img(image[0], image[1])
                print("下载　" + image[1] + "　成功")


