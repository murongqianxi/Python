import re
text = "aBc, fadsfafas Abc, ABC"
result = re.subn(r'abc', '***', text, flags=re.I)
# print(result)

text = 'abc,  ddd？ xxx。ffff'

result = re.split(r'\s*[,;/]\s*', 'foo,bar  ;  baz / qux')
print(result)


#print(re.sub(r'abc', '***', text, flags=re.I))


# text = '18812345678，他还有一个电话号码是18887654321，0571-52152188他爱好的数字是01234567891，他的座机是：0571-52152166'
# it = re.finditer(r'(\d{4})-(\d{8})', text)
# for m in it:
# 	print(m)


loveyou@qq.com
iloveyou@sina.com.cn

i-love-you
i.love.you@


