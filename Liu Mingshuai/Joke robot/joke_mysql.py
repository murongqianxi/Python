# -*- coding: utf-8 -*-
# @Time : 2021/2/19 14:22
# @Author : Liu Mingshuai
# @File : joke_mysql.py

import pymysql
from joke import Joke


def setup():
    """
    创建数据库和创建表，如果已经存在了不会重复创建
    """
    con = pymysql.connect(user='root',
                          password='qwertyuiop123',
                          host='localhost',
                          charset='utf8')
    cur = con.cursor()
    cur.execute("CREATE SCHEMA IF NOT EXISTS `jokes` DEFAULT CHARACTER SET utf8 ;")
    cur.execute("USE `jokes`")
    cur.execute("CREATE TABLE IF NOT EXISTS `joke` "
                "(`id` INT NOT NULL AUTO_INCREMENT,"
                "`title` VARCHAR (256) NOT NULL,"
                "`detail` VARCHAR(256) NOT NULL,"
                "`url` VARCHAR(1024) NOT NULL,"
                "PRIMARY KEY (`id`));")
    con.close()


def save(jokes):
    """
    把笑话保存到数据库
    根据url判断是否已经有这个笑话了，如果已经存在了不再保存
    """
    con = pymysql.connect(user='root',
                          password='qwertyuiop123',
                          host='localhost',
                          charset='utf8')
    cur = con.cursor()
    cur.execute("USE `jokes`")
    cur.execute("SELECT * FROM `joke` WHERE (url = %s)", jokes.url)
    has_joke = cur.fetchone()
    if has_joke:
        print('重复了，不再插入')
    else:
        cur.execute("INSERT INTO joke(title, detail, url) "
                    "VALUE (%s, %s, %s)", (jokes.title, jokes.detail, jokes.url))
        con.commit()
        print('笑话保存成功')
    con.close()


def get_jokes():
    """
    返回所有的笑话列表
    """
    print('Loading jokes...')
    con = pymysql.connect(user='root',
                          password='qwertyuiop123',
                          host='localhost',
                          charset='utf8')
    cur = con.cursor()
    cur.execute("USE `jokes`")
    cur.execute("SELECT * FROM `joke`;")
    all_joke = cur.fetchall()
    jokes = []
    for row in all_joke:
        joke = Joke(row[1], row[2], row[3], row[0])
        jokes.append(joke)
    con.close()
    return jokes


# 调用最上面的代码
setup()

# 测试代码，本模块被别的模块引入的时候，不会执行下面的代码
if __name__ == '__main__':
    # save(Joke('笑话Text', '笑话内容test', 'https://www.joke.com/1.html'))
    # save(Joke('笑话Text2', '笑话内容test2', 'https://www.joke.com/2.html'))
    print('======打印一下所有笑话======')
    for jokes_1 in get_jokes():
        print(jokes_1)
        print()