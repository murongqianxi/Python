# reptile(pc)百度翻译(by)
import requests
import json
url = "https://fanyi.baidu.com/sug"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
nm = input()
li = {'kw': nm}
x = requests.post(url, li, header)
t = x.json()
n = nm + '.text'
fp = open(n, 'w', encoding='utf-8')
json.dump(t, fp, ensure_ascii=False)















