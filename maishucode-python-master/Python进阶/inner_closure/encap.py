import random

def create_room():
    room_no = random.randint(1, 100)
    print(f'我创建了房间号：{room_no}')

    def toilet():
        print(f'欢迎进入{room_no}的VIP厕所')
        print('冲水')
        print('请君入厕')
        print('洗手')
        print('热毛巾')
        print('欢迎下次光临')

    print('上厕所')
    toilet()
    print('上厕所')
    toilet()
    print('上厕所')
    toilet()

#调用外部函数，并接受返回值
create_room()
