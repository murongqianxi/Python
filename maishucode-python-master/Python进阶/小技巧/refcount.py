import sys
name = '麦叔'
print(sys.getrefcount(name))  #打印4
name2 = name
print(sys.getrefcount(name))  #打印5
name3 = name 
print(sys.getrefcount(name))  #打印6
