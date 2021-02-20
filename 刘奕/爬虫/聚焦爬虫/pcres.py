# 爬虫(pc)requests模块(res)
import requests
url = 'https://www.sogou.com/web'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
k = input()
ui = {'query': k}
t = requests.get(url=url, params=ui, headers=header)
x = t.text
with open(k + '.html', 'w', encoding='utf-8') as fp:
    fp.write(x)




