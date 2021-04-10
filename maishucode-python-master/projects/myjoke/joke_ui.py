import random 
from joke import Joke
import joke_db
# 要使用哪个语音引擎，就反注释哪个，最开始只有printer，后面陆续实现其他
#from speakers.ttsx.ttsx import tell_joke
#from speakers.google.google import tell_joke
#from speakers.printer import tell_joke
from speakers.xunfei.xunfei import tell_joke
import time 
import sys

print('''
==============我是麦叔😆=====================
.___     .____     ________ ____   _______________     ____ ___  
|   |    |    |    \_____  \\   \ /   /\_   _____/    |    |   \ 
|   |    |    |     /   |   \\   Y   /  |    __)_     |    |   / 
|   |    |    |___ /    |    \\     /   |        \    |    |  /  
|___|    |_______ \\_______  / \___/   /_______  /    |______/   
                 \/        \/                  \/                
=============正在更衣，请稍等...==============
''')

# 加载所有笑话，所以你需要先有笑话, 才能运行
jokes = joke_db.get_jokes()

if(len(jokes) == 0):
    print('数据库还没有任何笑话，请先运行joke_crawler.py抓取笑话，再来唤醒我')
    print('我先走了啊，记得来唤醒我，等你哟!')
    sys.exit()

print('=====输入数字，我连续给你讲笑话，最多不超过5个..')
print('=====退出请输入886=======================')

while(True):
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

