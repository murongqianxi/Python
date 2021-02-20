# -*- coding: utf-8 -*-
# @Time : 2021/2/19 14:21
# @Author : Liu Mingshuai
# @File : joke.py


class Joke:
    """
    表示一个笑话。
    其中title是笑话标题，detail是笑话内容
    url是笑话的采集网址，通过url判定笑话是否重复，防止保存重复笑话
    id是数据库生成的唯一标识，刚刚采集下来的笑话是没有id的，所以id可以为空
    """
    def __init__(self, title, detail, url, id=None):
        self.url = url
        self.detail = detail
        self.title = title
        self.id = id

    def __str__(self):
        """
        有了这个方法，print(joke)会把笑话打印成下面格式的字符串，否则只会打印对象的内存地址
        """
        return f'{self.id}-{self.title}\n{self.detail}\n{self.url}'