# -*- coding: utf-8 -*-
# @Time : 2021/2/19 14:22
# @Author : Liu Mingshuai
# @File : joke_db.py

import sqlite3
from joke import Joke


def setup():
    """
    创建数据库和创建表，如果已经存在了不会重复创建
    """
    con = sqlite3.connect('jokeDB.db')
    with con:
        con.execute('''CREATE TABLE IF NOT EXISTS jokes
                    (id INTEGER PRIMARY KEY,
                    title varchar(256) NOT NULL,
                    detail varchar(1024) NOT NULL,
                    url varchar(1024) NOT NULL)''')


def save(joke):
    """
    把笑话保存到数据库
    根据url判断是否已经有这个笑话了，如果有了就不再保存
    """
    con = sqlite3.connect('jokeDB.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM jokes WHERE (url = ?)', [joke.url])
        has_joke = cur.fetchone()
        if has_joke:
            print('重复了，不再插入')
        else:
            con.execute('INSERT INTO jokes(title, detail, url) VALUES (?,?,?)', (joke.title, joke.detail, joke.url))
            print('笑话保存成功')


def get_jokes():
    """
    返回所有的笑话列表
    """
    print('Loading jokes...')
    con = sqlite3.connect('jokeDB.db')
    jokes = []
    with con:
        for row in con.execute('SELECT * FROM jokes'):
            joke = Joke(row[1], row[2], row[3], row[0])
            jokes.append(joke)
    return jokes


# 调用最上面的代码
setup()

# 测试代码，本模块被别的模块引入的时候，不会执行下面的代码
if __name__ == '__main__':
    # save(Joke('笑话Test', '笑话内容test', 'https://www.joke.com/1.html'))
    # save(Joke('笑话Test2', '笑话内容test', 'https://www.joke.com/2.html'))
    print('========打印一下所有的笑话======')
    for joke_1 in get_jokes():
        print(joke_1)
        print()