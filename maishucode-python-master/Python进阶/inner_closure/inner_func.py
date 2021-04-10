def outter():
    print('我是外部函数')
    def inner():
        print('我是outter的内部函数')
    print('调用内部函数')
    inner()
    print('我再次调用内部函数，自己家的想用就用，随时用')
    inner()
    print('还可以返回给大家共用')
    return inner 

#调用外部函数，并接受返回值
func = outter()

#调用outter返回的内部函数
print('在外部调用内部函数')
func()
