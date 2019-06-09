import re
import requests
from key_value import key_dict
from Agents import get_agent


class Search:
    def __init__(self):
        self.Search_Key = key_dict
        self.headers = {
            "User-Agent": get_agent()
        }

    def use_search(self):
        # search_item = sorted(list(self.Search_Key.keys()))
        search_item = sorted(self.Search_Key)
        print("**********************************************************************")
        for i in search_item:
            print("[" + str(search_item.index(i) + 1) + "] " + i)
        print("**********************************************************************")
        key_num = int(input("请输入你想要爬取的类别编号： "))
        key = search_item[key_num]
        value = self.Search_Key.get(key)
        pages = self.page_num(value)
        print("共有" + str(pages) + "页，每页有20张图片")
        get_page_num = int(input("请输入你想要爬取的页面数"))
        return value, get_page_num

    def page_num(self, url):
        url = url + str(1)
        rep = requests.get(url, headers=self.headers).text
        rule = "totalPage.+?(-?[1-9]\d*),"
        results = re.findall(rule, rep)
        for result in results:
            if result:
                print(result)
                return result
            else:
                print("获取页面数失败")

    def test(self):
        print(self.headers)

# Search().use_search()
