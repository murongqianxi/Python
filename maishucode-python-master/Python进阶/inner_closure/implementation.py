import random


def create_room():
    room_no = random.randint(1, 100)
    print(f'我创建了房间号：{room_no}')

    def toilet():
        print(f'我是{room_no}的内部厕所')
    return toilet


print('调用外部函数')
toilet = create_room()

print('打印一下toilet函数的变量，其中有一个是__closure__')
print(dir(toilet))
print('__closure__是一个包含它携带的变量的元组')
print(toilet.__closure__)
print('__closure__元组里是cell，通过cell_contents可以访问所携带的变量值')
print(toilet.__closure__[0].cell_contents)
