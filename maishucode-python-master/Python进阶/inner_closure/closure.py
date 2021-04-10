import random
def create_room():
    room_no = random.randint(1, 100) 
    print(f'我创建了房间号：{room_no}')

    def toilet():
        print(f'我是{room_no}的内部厕所')
    print('上厕所')
    toilet()
    print('我再次上厕所，自己家的想用就用，随时用')
    toilet()
    print('还可以共享给大家共用')
    return toilet

#调用外部函数，并接受返回值
toilet = create_room()

#调用outter返回的内部函数
print('在外部使用内部厕所')
toilet()

print('在外部再次使用内部厕所')
toilet()
