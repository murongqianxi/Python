#类是一个模板
class Dog:
    #构造方法
    def __init__(self, name, height, power):
        self.name = name
        self.height = height
        self.power = power
        self._blood = 10

    def bark(self):
        '''会说话的狗：会报出自己的名字，身高等信息'''
        print(f'我是{self.name}，身高{self.height}, 血量{self.blood}，攻击力{self.power}')

    def attack(self, dog2):
        '''当前Dog攻击参数中指定的Dog，对方会减少和self.power相同的血量'''
        d2.reduce_blood(d1.power)

    def blood(self):
        return self._blood

    def reduce_blood(self, reduce_value):
        '''减少血量，减到0为止'''
        if(reduce_value > self._blood):
            self._blood = 0
        else:
            self._blood = self._blood - reduce_value


d1 = Dog('大黄', 0.7, 3)  # 创建第1个实例
d2 = Dog('二黑', 0.5, 4)  # 创建第2个实例

print(d2.blood())
for i in range(5):
    d1.attack(d2)

print(d2.blood())
