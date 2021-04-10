# list1 = ['张三', '李四', '王五', '大美', '如花']
# list2 = ['张三', '李四', '王五', '麦叔']

# set1 = set(list1)
# set2 = set(list2)

# list3 = list(set1.symmetric_difference(set2))
# print(list3)

import sys

list1 = ['张三', '李四', '王五', '大美', '如花']
print("list1所用字节数 = ",sys.getsizeof(list1))

name = '麦叔'
print("name的字节数 = ",sys.getsizeof(name))


late_names = ['张三', '李四', '王五', '大美', '如花', '张三', '李四', '林志颖', '大美']
print("迟到记录= ", late_names)

unqiue_late_names = list(set(late_names))
print("迟到过的人= ", unqiue_late_names)


list1 = [20, 20, 20, 20]
print("list1中都相同吗？", list1.count(list1[0]) == len(list1))

list2 = [20, 20, 20, 50]
print("list2中都相同吗？", list2.count(list2[0]) == len(list2))


from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]

print("相同吗？", Counter(one) == Counter(two))
print("相同吗？", sorted(one) == sorted(two))


def isUnique(item):
    tempSet = set()
    return not any(i in tempSet or tempSet.add(i) for i in item)

list1 = [123, 345, 456, 23, 567]
print("list1都唯一吗？ ", isUnique(list1))

list2 = [123, 345, 567, 23, 567]
print("list2都唯一吗？ ", isUnique(list2))


byteVar = bytes("麦叔密码", 'utf-8')
print(byteVar)

#编码规则不对，乱码
str1 = str(byteVar.decode("gbk"))
print("字符串是：" , str1 )

#编码规则正确，不乱
str2 = str(byteVar.decode("utf-8"))
print("字符串是：" , str2 )



listOne = [123, 345, 456, 23]
for index, element in enumerate(listOne): 
    print(index, element)

names1 = {1: '张三', 2: "李四", 3:"王五"}
names2  = {2: '麦叔', 4: "小强"}
all_names = {**names1, **names2}
#打印结果：{1: '张三', 2: '麦叔', 3: '王五', 4: '小强'}
print(all_names)


ids = [1, 2, 3, 4, 5]
names = ['张三', '李四', '王五', '大美', '如花']

name_dict = dict(zip(ids, names))

print(name_dict)

names1 = {1: '张三', 2: "李四", 3:"王五", 4:'张三'}
tempset = set()
dup_names = [n in tempset or   for n in names1.values()]

