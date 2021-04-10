text = '有一个Up主叫麦叔，还有一个Up主叫麦二叔，还有一个Up叫麦三'

#找到所有姓麦的Up主的名字: 麦x | 麦xx
import re
result = re.findall(r'麦\w{1,2}', text)
# print(result)

# - 所有的数字
text = "身高:178，体重：168，学号：123456，密码:9527"
result = re.findall(r'\d+', text)
# print(result)


# - 所有的单词
text = "hello, 你好吗？, My name is maishu"
result = re.findall(r'[a-zA-Z]+', text)
# print(result)


# - 包含手机号码
text = '麦叔的电话是18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
result = re.findall(r'1[3-9]\d{9}', text)
# print(result)

# - 包含区号和电话号码
text = '麦叔的电话是18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
result = re.findall(r'\d{3,4}-\d{7,8}', text)
# print(result)

# - 手机号码或者电话号码
text = '麦叔的电话是18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
result = re.findall(r'1[3-9]\d{9}|\d{3,4}-\d{7,8}', text)
# print(result)

# - 区号和电话号码
# - 包含区号和电话号码
text = '麦叔的电话是18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
result = re.search(r'(\d{3,4})-(\d{7,8})', text)
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))

text = '麦叔的电话是18812345678，麦二叔他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
result = re.findall(r'^麦\w', text)
# print(result)

text = '麦叔的电话是18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
# print(re.subn(r'1[3-9]\d{9}|\d{3,4}-\d{7,8}', '***', text))
# print(text)

text = "  how ARE you? what are your names?  "
# print(re.findall(r'^\s+|\s+$', text, flags=re.I))


text = 'barbar carcar harhel'
# print(re.findall(r'(\w{3})(\1)', text))


text = "身高:178，体重：168，学号：123456，密码:9527"
print(re.findall(r'(?<=密码.)\d+', text))



