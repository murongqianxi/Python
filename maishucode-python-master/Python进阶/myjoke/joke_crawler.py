import requests
import bs4
import time
import random
import joke_db
from joke import Joke

#起始URL
url = 'http://xiaohua.zol.com.cn/detail1/1.html'  

#网站的域名地址，用来拼接完整地址
host = 'http://xiaohua.zol.com.cn'

def craw_joke(url):
    '''
    抓取指定的URL，返回一个Joke对象，和下一个要抓取的URL
    如果抓取失败，返回None, None
    必须设置User-Agent header，否则容易被封
    '''
    print(f'正在抓取：{url}')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    soup = bs4.BeautifulSoup(html, 'lxml')
    try:
        #分别使用css选择器提取title, detail和next_url
        title = soup.select_one('h1.article-title').getText()
        detail = soup.select_one('div.article-text').getText().strip()
        next_url = soup.select_one('span.next > a')['href']
        return Joke(title, detail, url), next_url
    except Exception as e:
        print('出错了：', e)
        print(html)
        return None, None 

# 抓取笑话，以学习为目的，建议不要抓取太多，本例子只抓取了10个
count = 0
for i in range(0, 10):
    joke, next_url = craw_joke(url)
    if joke:
        joke_db.save(joke)
        url = host + next_url
    print('歇一会儿再抓!')
    time.sleep(random.randint(1, 5))
print('抓完收工！')




