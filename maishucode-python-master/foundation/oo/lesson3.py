import random

#类是一个模板
class Dog:
    num_of_dogs = 0  # 类属性
    police_height = 60 # 成为警犬的身高标准

	#构造方法 - 添加实例属性，做其他的初始化工作
    def __init__(self, name, height, power):
        self.name = name
        self.height = height
        self.power = power
        self.blood = 10
        print(f"{self.name}出生了，汪汪！")
        Dog.num_of_dogs += 1
    
    def die(self):
        print(f"{self.name}已安息！")
        Dog.num_of_dogs -= 1

    # 判定是否可以成为警犬，返回True或者False
    def can_be_police(self):
        return self.height > Dog.police_height
    
    # 类方法
    @classmethod 
    def wangwang(cls):
        print('我们是狗，我们是人类的朋友')
        print('''
^..^      /
/_/\_____/
/\   /\
/  \ /  \
        ''')
        print(f'我们共有{cls.num_of_dogs}个成员')

    #静态方法：小狗的图像
    @staticmethod
    def pic_little():
        print('''
  /^ ^\ 
 / 0 0 \ 
 V\ Y /V
  / - \ 
 /    |
V__) ||
        ''')

    #静态方法：大狗的图像
    @staticmethod
    def pic_big():
        print('''
    ___
 __/_  `.  .-"""-.
 \_,` | \-'  /   )`-')
  "") `"`    \  ((`"`
 ___Y  ,    .'7 /|
(_,___/...-` (_/_/ 
        ''')
    
    #静态方法：长的图像
    @staticmethod
    def pic_long():
        print('''
                                    .-.
     (___________________________() `-,
     (   ______________________   /''"`
     //\\                      //\\
     "" ""                     "" ""

        ''')


# 创建100条狗，放到列表中
dogs = []
for i in range(100):
    d = Dog(f"dog{i}", random.randint(30, 80), random.randint(1,12))
    print(Dog.num_of_dogs)
    dogs.append(d)

# 循环30次，每次随机选择一条狗，让它死掉
for i in range(30):
    dog = random.choice(dogs)
    dog.die()
    print(Dog.num_of_dogs)

print(f'成为警犬的身高标准是：{Dog.police_height}')
for d in dogs:
    if(d.can_be_police()):
        print(f'{d.name} 可以成为警犬')
    

Dog.wangwang()
Dog.pic_little()
Dog.pic_big()
Dog.pic_long()
