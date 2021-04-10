import random 
from joke import Joke
import joke_db
from speakers.ttsx import tell_joke


print('你好，我比小度更会讲笑话！')
print('输入数字，我连续给你讲笑话，最多不超过5个..')
print('退出输入886')

#加载笑话
jokes = joke_db.get_jokes()

while(True):
    cmd = input('要听笑话吗？')
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
        joke = jokes[random.randint(0, len(jokes)-1)]
        tell_joke(joke.title, joke.detail)

