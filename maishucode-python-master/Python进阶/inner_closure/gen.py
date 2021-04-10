def team_maker(type, level, temperature):
    '''
    type: 品种，如绿茶，红茶
    level: 等级，特级，一级，二级
    temper: 温度
    '''
    def tea(water):
        print('正在沏茶中')
        print(f'{type},{level}, {temperature}')
        print(f'{water}毫升给您冲好了')
    return tea


#创建符合我口味的沏茶函数
mytea = team_maker('绿茶', '特级', '66.6')
#创建符合她口味的沏茶函数
herteam = team_maker('红茶', '一级', '88.8')

print('我们来一杯')
mytea(500)
herteam(300)
print('多喝点')
mytea(800)
herteam(600)
print('完了，我喝醉了...')