print('制作者:刘明帅\n''时间:2020年2月20日\n')
while True:
    print('满分:6分\n''一道题2分\n')
    print('按q退出\n')
    print('注意事项:\n1.答案之间","隔开\n2.不能空题\n3.请认真读题\n若不遵守以上注意事项,可能会导致答案错误,或导致程序错误\n')
    one = input('1.中国有多少个省,直辖市,自治区,特别行政区?(加单位)')
    one = str(one)
    if one == 'q':
        break
    if one == '23个,4个,5个,2个':
        print('True')
        a = 2
    else:
        print('False')
        a = 0
    two = input("2.'四书'是指哪四书?(按首字母L,Z,D,M排序,加书名号)")
    two = str(two)
    if two == 'q':
        break
    if two == '<<论语>>,<<中庸>>,<<大学>>,<<孟子>>':
        print('True')
        b = 2
    else:
        print('False')
        b = 0
    three = input('3.58*49=(*表示乘号)')
    three = str(three)
    if three == 'q':
        break
    if three == '2842':
        print('True')
        c = 2
    else:
        print('False')
        c = 0
    grade = a+b+c
    print("你的得分是:", grade)
    if grade == 6:
        print('恭喜你,全对,请继续努力.\n')
    elif grade == 4:
        print('很遗憾,你错了一道,请继续努力.你\n')
    elif grade == 2:
        print('很遗憾,你错了两个,请继续努力.\n')
    elif grade == 0:
        print('很遗憾,你全错,请继续努力.\n')
