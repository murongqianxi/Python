# -*- coding: utf-8 -*-
# @Time : 2021/2/19 17:57
# @Author : Liu Mingshuai
# @File : speaker.py


import pyttsx3

# 初始化引擎
engine = pyttsx3.init()


def tell_joke(joke_id, title, detail):
    engine.say(joke_id)
    engine.say(title)
    engine.say(detail)

    # 注意，没有本句话是没有声音的
    engine.runAndWait()


if __name__ == '__main__':
    tell_joke(9527, '测试笑话', '测试笑话内容123')