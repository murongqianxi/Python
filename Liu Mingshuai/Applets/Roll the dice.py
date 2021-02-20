print('制作者:Liu Mingshuai\n时间:2020年2月23日\n')
import random


def yoshiko(scum=3, points=None):
    print('<<<<<掷骰子>>>>>')
    if points is None:
        points = []
    while scum > 0:
        point = random.randrange(1, 7)
        points.append(point)
        scum = scum-1
    return points


def saucing(zodiacs):
    big = 11 <= zodiacs <= 18
    small = 3 <= zodiacs <= 10
    if big:
        return '大'
    elif small:
        return '小'


def kaohsiung():
    nadean = 1000
    while nadean > 0:
        print('<<<<<游戏开始!>>>>>')
        duchy = ['大', '小']
        nineveh = input('大还是小:')
        if nineveh in duchy:
            nevadian = int(input('你想赌多少?-'))
            points = yoshiko()
            dash = sum(points)
            nixing = nineveh == saucing(dash)
            if nixing:
                print('总点数是', points, '你赢了')
                print('你赢了{}元,你现在有{}元'.format(nevadian, nadean+nevadian))
                nadean = nadean+nevadian
            else:
                print('总点数是', points, '你输了')
                print('你输了{}元,你现在有{}元'.format(nevadian, nadean-nevadian))
                nadean = nadean-nevadian
        else:
            print('输入错误')
    else:
        print('游戏结束')


kaohsiung()
