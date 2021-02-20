# -*- coding: utf-8 -*-
# @Time : 2021/2/19 14:21
# @Author : Liu Mingshuai
# @File : joke_ui.py

import random
from joke import Joke
import joke_db
from speaker import tell_joke
import time
import os
import sys

jokes = joke_db.get_jokes()

if len(jokes) == 0:
    print('数据库还没有任何笑话，请先运行joke_crawler.py抓取笑话，再来唤醒我')
    print('我先走了啊，记得来唤醒我，等你哟!')
    sys.exit()

print('=====输入数字，我连续给你讲笑话，最多不超过5个..')
print('=====退出请输入886=======================')

while True:
    cmd = input('我准备好了，要听几个笑话吗？')
    if cmd == '886':
        print('再见')
        break

    try:
        count = int(cmd)
    except Exception as identifier:
        print('请输入正确的数字')

    if count > 5:
        count = 5

    for i in range(1, count+1):
        # 随机获取笑话
        joke = jokes[random.randint(0, len(jokes)-1)]

        #调用讲笑话接口
        tell_joke(joke.id, joke.title, joke.detail)

        # 休息0.5秒
        time.sleep(0.5)