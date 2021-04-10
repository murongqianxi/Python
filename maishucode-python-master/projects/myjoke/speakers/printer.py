# 本类是Speaker（发言人)的其中一个实现。所有Speaker都要实现tell_joke接口。
# 本实现只是简单打印笑话内容。其他真正的语音实现包括：ttsx, google, xunfei等。

def tell_joke(joke_id, title, detail):
    print(f'=============😆{title}😆==========')
    print(detail)
