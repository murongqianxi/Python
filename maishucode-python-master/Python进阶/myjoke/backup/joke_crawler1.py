import requests
import bs4
import time
base = 'http://xiaohua.zol.com.cn/detail1/'

for i in range(1, 11):
    url = base + str(i) + '.html'
    print(url)
    html = requests.get(url).text
    #print(html)
    soup = bs4.BeautifulSoup(html, 'lxml')
    try:
        print(soup.select('div.article-text')[0].getText().strip())
    except:
        print('error, sleeep a while')
        time.sleep(3)
    print('sleeping...')
    time.sleep(1)
