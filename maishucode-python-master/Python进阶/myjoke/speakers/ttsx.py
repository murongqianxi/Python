import pyttsx3
# 初始化， 必须要有奥
engine = pyttsx3.init()

def tell_joke(title, detail):
    engine.say(title)
    engine.say(detail)
    # 注意，没有本句话是没有声音的
    engine.runAndWait()


if __name__ == '__main__':
    tell_joke('测试笑话', '测试笑话内容123')