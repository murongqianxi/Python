# -*- coding: utf-8 -*-
# @Time : 2021/2/19 10:55
# @Author : Liu Mingshuai
# @File : Crawl book list.py

import requests
import json
import time
import csv
import datetime


class Book:
    def __init__(self, name, code, author, price):
        self.name = name
        self.code = code
        self.price = price
        self.author = author

    def __str__(self):
        return f'书名：{self.name}，作者：{self.author}，价格：{self.price}，编号：{self.code}'

    def to_csv(self):
        return [self.name, self.author, self.price, self.code]


def get_page(page=1):
    url = f'https://www.epubit.com/pubcloud/content/front/portal/getUbookList?page={page}&row=20&=&startPrice=&endPrice=&tagId='
    headers = {'Origin-Domain': 'www.epubit.com'}
    res = requests.get(url, headers=headers)
    return parse_book(res.text)


def parse_book(json_text):
    book = []
    book_json = json.loads(json_text)
    records = book_json['data']['records']
    for r in records:
        author = r['authors']
        name = r['name']
        code = r['code']
        price = r['price']
        book_2 = Book(name, code, author, price)
        book.append(book_2)
    return book


all_books = []
for i in range(1, 10):
    print(f'======抓取第{i}页======')
    books = get_page(i)
    for b in books:
        print(b)
    all_books.extend(books)
    print('抓完一页，休息5秒钟...')
    time.sleep(5)

now_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
file_name = f'book_list_{now_str}.csv'
with open(file_name, 'w', newline='', encoding='utf-8') as f:
    pen = csv.writer(f)
    pen.writerow(['书名', '作者', '价格', '编号'])
    for v in all_books:
        pen.writerow(v.to_csv())
