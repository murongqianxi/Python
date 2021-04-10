# 本类是Speaker（发言人)的其中一个实现。所有Speaker都要实现tell_joke接口。
# 其他实现包括：google, xunfei, printer等。

import pyttsx3

# 初始化引擎
engine = pyttsx3.init()

def tell_joke(joke_id, title, detail):
    engine.say(title)
    engine.say(detail)
   
    # 注意，没有本句话是没有声音的
    engine.runAndWait()


if __name__ == '__main__':
    tell_joke(9527, '结婚以后', '女：为什么从前你对我百依百顺，可结婚才三天，你就跟我吵了两天的架？男：因为我的忍耐是有限度的。')
