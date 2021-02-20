# reptile(pc)豆瓣排行榜(db)
from typing import List, Any

import requests
import json
url = 'https://movie.douban.com/j/chart/top_list'
x = {'type': '19', 'interval_id': '100:90', 'action': '', 'start': '0',
     'limit': '100'}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
t = requests.get(url=url, params=x, headers=header).json()
po = []
for i in t:
     po.append(i['title'])
fp = open('豆瓣排行.text', 'w', encoding='utf-8')
json.dump(po, fp, ensure_ascii=False)
























