'''
Author: your name
Date: 2021-07-06 16:21:51
LastEditTime: 2021-07-11 17:11:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\code\codewars.py
'''

def greatest_common_factor(seq):
    a = sorted(seq)
    d = '0' * len(seq)
    e = ''
    for i in range(1, a[0] + 1):
        for b in a:
            if b % i == 0:
                e += '0'
        if e == d:
            c = i
        e = ''
    return c

d = greatest_common_factor([33, 44, 22])
print(d)