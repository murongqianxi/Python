# -*- coding: utf-8 -*-
# @Time : 2021/2/19 18:04
# @Author : Liu Mingshuai
# @File : joke_gui_model.py

import random
import joke_sqlite
from speaker import tell_joke

# 加载所有笑话，所以你需要先有笑话才能运行。如果还没有，可以运行joke_crawler.py抓取笑话
jokes = joke_sqlite.get_jokes()


def select_jokes(count=1):
    """随机选取count指定个数的笑话"""
    return random.sample(jokes, count)


def speak_joke(joke):
    """调用语音引擎朗读笑话"""
    tell_joke(joke.id, joke.title, joke.detail)
