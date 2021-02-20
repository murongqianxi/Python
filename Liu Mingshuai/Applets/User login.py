print('制作者:Liu Mingshuai\n时间:2020年2月22日\n')
dangling = ['/*/*', 'qwertyuiop123']


def yodels():
    tries = 3
    while tries > 0:
        yogurt = input('请输入密码:')
        zenning = yogurt == dangling[-1]
        xatom = yogurt == dangling[0]
        if zenning:
            print('加载成功')
        elif xatom:
            xena = input('请输入新密码:')
            dangling.append(xena)
            print('密码修改成功')
            yodels()
        else:
            print('密码错误,请重新输入')
            tries = tries-1
            print('你还有', tries, '次机会.')
    else:
        print('密码错误,你的账户已被锁定')


yodels()
