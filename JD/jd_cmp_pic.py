import requests
from lxml import etree
import os
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent

'''
构建请求头
'''
headers = {
    "User-Agent": UserAgent().random            # 随机生成请求浏览器头
    # "proxies": get_ip_addr()                  # 从代理池中随机获取ip地址
}

'''获取爬去页面的unid'''


def get_main_page_url():
    for i in range(1, 984):
        main_page_url = "https://list.jd.com/list.html?cat=670,671,672&page=" + str(
            i) + "&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
        response = requests.get(main_page_url, headers=headers)
        html = etree.HTML(response.text)
        page_url_unids = html.xpath('//*[@id="plist"]/ul/li/div/@data-sku')
        # print(page_url_unid)
        for unid in page_url_unids:
            yield unid


'''　
#　 传入unid并拼接成page_url
＃　获取文件夹名字并创建文件夹
＃　获取图片地址并下载至文件夹中
'''


def get_dir_name_and_img_url(unid):
    page_url = "https://item.jd.com/" + unid + ".html"
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    dir_name = soup.find(attrs={"class": "sku-name"}).get_text().strip()
    # print(dir_name)
    html = etree.HTML(response.text)
    path = "/home/chen/Downloads/" + dir_name
    mdkir_dir(path)
    img_data_urls = html.xpath('//*[@id="spec-list"]/ul//li/img/@data-url')
    downloads_img_list(path, img_data_urls)


'''
传入文件夹路径与需要爬取的图片地址url列表
爬去列表中的url并存入指定路径
'''


def downloads_img_list(path, img_url_list):
    number = 1
    for img_data_url in img_url_list:
        img_url = "https://img13.360buyimg.com/n1/s450x450_" + img_data_url
        # print(img_url)
        image = requests.get(img_url, headers=headers)
        image_file_path = path + "/" + str(number) + ".jpg"
        print(image_file_path)
        fp = open(image_file_path, "wb")
        fp.write(image.content)
        fp.close()
        number = number + 1
        time.sleep(random.uniform(0, 3))


'''
在指定路径创建指定名字的文件夹
'''


def mdkir_dir(file_path):
    file_path = file_path.strip()
    file_path = file_path.rstrip("\\")
    isExists = os.path.exists(file_path)
    if not isExists:
        os.makedirs(file_path)
        print(file_path + ' 创建成功')
        return True
    else:
        print(file_path + ' 目录已存在')
        return False


if __name__ == '__main__':
    for page_url_unid in get_main_page_url():
        get_dir_name_and_img_url(page_url_unid)
