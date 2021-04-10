import requests

url = 'http://api.w-seo.cn/qd.php?qq='

with open('qq-phone.txt') as f:
	for qq in range(10000, 1000000000):
    	response = requests.get(f'{url}{qq}')
    	phone = response.text
    	f.write(f'{qq}, {phone}\n')
