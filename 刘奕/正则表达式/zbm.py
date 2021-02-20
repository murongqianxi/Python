import re
a = 'hello\\yi'
c = 'xjkxsjlkx'
d = 'a3ks5d7af3ka5'
print('1:re.match')
print(re.match('h', a))  # 在a里找h, 只能找第一个
print('2:re.search')
print(re.search(r'\\', a))  # 在a里找\\
print('3:re.finditer')
b = re.finditer('x', c)   # 从头找到尾, 可用for循环一个个找出坐标
for i in b:
    print(i)
print('4:re.findall')
print(re.findall('a\d+', d))    # a\d+中的\d+是指后面加数字的
print('5:re.fullmatch')
print(re.fullmatch('ahgashgahghda', 'ahgashgahghda'))   #只有两个都一样才行, 否则返回None
print(re.fullmatch('a.*d', 'ahgashgahghd'))     # a.*d是指从a到最后一个d














