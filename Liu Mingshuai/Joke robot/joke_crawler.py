# -*- coding: utf-8 -*-
# @Time : 2021/2/19 14:21
# @Author : Liu Mingshuai
# @File : joke_crawler.py

import requests
import bs4
import time
import random
import joke_db
from joke import Joke

# 起始url
url = 'https://xiaohua.zol.com.cn/detail1/73.html'

# 网站的域名地址，用来拼接完整地址
host = 'http://xiaohua.zol.com.cn'


def craw_joke(url_1):
    """
    抓取指定的URL，返回一个joke对象，和下一个要抓取的URL
    如果抓取失败，返回None，None
    必须设置User-Agent header，否则容易被封
    """
    print(f'正在抓取：{url_1}')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    html = requests.get(url_1, headers=headers).text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    try:
        # 提取title, detail和next_url
        title = soup.find('h1', {'class': 'article-title'}).text
        detail = soup.find('div', {'class': 'article-text'}).text.strip()
        new_url = soup.find('span', {'class': 'next'}).find('a').get('href')
        return Joke(title, detail, url), new_url
    except Exception as e:
        print('出错了:', e)
        print(html)
        return None, None


# 抓取笑话，建议不要太多，本例子只抓取了10个
count = 0
for i in range(0, 10):
    joke, next_url = craw_joke(url)
    if joke:
        joke_db.save(joke)
        print(joke)
        url = host + next_url
    print('歇一会再抓！')
    time.sleep(random.randint(1, 5))
print('抓完收工！')