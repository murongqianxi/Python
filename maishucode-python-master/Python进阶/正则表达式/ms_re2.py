#正则表达式就是为了找到符合某种模式的字符串，这些模式包括：是什么字符，重复多少次，在什么位置，内部有什么关系

#level 1 - 固定的字符串
#确定字符串中是否有123456
text = '麦叔身高:178，体重：168，学号：123456，密码:9527'

target = '123456'
if target in text:
	print('找到了')
print(text.index(target))

import re
print(re.findall(r'123456', text))


#level2 - 一类字符
#找出所有的数字
text = '麦叔身高:178，体重：168，学号：123456，密码:9527'
print(re.findall(r'\d', text))

#level3 - 重复某一类字符 
#要求：找所有的数字，这不是固定的，而是一个模式：连续重复的数字
text = '麦叔身高:178，体重：168，学号：123456，密码:9527'
print(re.findall(r'\d+', text))

#leve4 - 组合level2
#找出座机号码
text = '麦叔电话是18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
print(re.findall(r'\d{4}-\d{8}', text))


#leve5 - 多种情况
#找出电话号码或者座机号码
text = '麦叔电话是18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
print(re.findall(r'\d{4}-\d{8}|1\d{10}', text))


#level6 - 限定位置
#在句子开头的手机号码,或座机
text = '18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
print(re.findall(r'^1\d{10}|^\d{4}-\d{8}', text))

#level7 - 内部约束
#找出形如barbar, dardar的前后三个字母重复的字符串
text = 'barbar carcar harhel'
print(re.findall(r'(\w{3})(\1)', text))

#模式包含几个部分
#各个部分的字符分类是什么
#各个部分如何重复
#是否有外部位置限制
#是否有内部位置限制
text = '随机数字：01234567891，座机1：0571-52152166，座机2：0571-52152188-1234'
print(re.findall(r'\d{3,4}-\d{7,8}-\d{3,4}|\d{3,4}-\d{7,8}', text))



