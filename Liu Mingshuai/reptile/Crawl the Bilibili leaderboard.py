"""Crawl the Bilibili leaderboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YvINo0uC5LxdiDWe28e1i-_gnEmKrFtA
"""

import requests
from bs4 import BeautifulSoup
import csv
import datetime


class Video:
    def __init__(self, rank, title, score, visit, up, space, url, barrage):
        self.rank = rank
        self.title = title
        self.score = score
        self.visit = visit
        self.up = up
        self.space = space
        self.url = url
        self.barrage = barrage

    def to_csv(self):
        return [self.rank, self.title, self.score, self.visit, self.up, self.space, self.url, self.barrage]

    @staticmethod
    def csv_title():
        return ['排名', '标题', '综合分数', '播放量', 'Up主', '个人空间', '视频地址', '弹幕']


url = 'https://www.bilibili.com/v/popular/rank/all'
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')
videos = []

items = soup.findAll('li', {'class': 'rank-item'})
for itm in items:
    visit = itm.find_all('span', {'class': 'data-box'})[0].text.strip()
    barrage = itm.find_all('span', {'class': 'data-box'})[1].text.strip()
    up = itm.find_all('span', {'class': 'data-box'})[2].text.strip()
    title = itm.find('a', {'class': 'title'}).text
    rank = itm.find('div', {'class': 'num'}).text
    score = itm.find('div', {'class': 'pts'}).find('div').text
    url = itm.find('a', {'class': 'title'}).get('href')
    space = itm.find('div', {'class': 'detail'}).find('a').get('href')
    v = Video(rank, title, score, visit, up, space, url, barrage)
    videos.append(v)

now_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
file_name = f'top100_{now_str}.csv'
with open(file_name, 'w', newline='',encoding='utf-8') as f:
    pen = csv.writer(f)
    pen.writerow(Video.csv_title())
    for v in videos:
        pen.writerow(v.to_csv())
