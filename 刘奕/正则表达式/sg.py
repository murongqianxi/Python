import re
m1 = re.search('h.*d', 'hello, bide')
print(m1, m1.span(), m1.group())
m2 = re.search('(?P<a>h.*)(?P<b>l.*)(?P<c>a.*y)', 'hello, carry')
print(m2.group(0))
print(m2.group(1))
print(m2.group(2))
print(m2.group(3))
print(m2.groupdict())
print(m2.group('c', 'a', 'b'))













