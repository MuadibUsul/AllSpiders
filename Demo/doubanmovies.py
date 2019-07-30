
'''爬取豆瓣全网电影数据并进行分析'''

import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
}

def parse(url):
    """

    :type url: object
    """
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        return data


def geturl(part_url):
    """

    :type part_url: object
    """
    next_urls = []
    for i in range(0, 9960, 20):
        next_url = part_url + str(i)
        next_urls.append(next_url)
    return next_urls


def database(data):
    # with open('moviedata.json', 'a', encoding='utf-8') as f:
    for item in data:
        movie = dict(id=item['id'], 电影名=item['title'], 评分=item['rate'], 星级=item['star'], 主角=item['directors'],
                      演员=item['casts'], 网址=item['url'], 海报=item['cover'])
        print(movie)
            # f.write(json.dumps(movie, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    x = 0
    part_url = 'https://movie.doubantop250.com/j/new_search_subjects?sort=U&range=0,10&tags=&start='
    urls = geturl(part_url)
    for url in urls:
        datas = parse(url)
        database(datas)
        x += 1
    print(20*x)

