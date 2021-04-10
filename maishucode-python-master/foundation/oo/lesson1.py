# 面向过程的代码

#表示狗的属性
dog1_name = '大黄'
dog1_height = 0.7
dog1_blood = 1.0
dog1_power = 0.1

dog2_name = '二黑'
dog2_height = 0.7
dog2_blood = 1.0
dog2_power = 0.2


#dog1攻击dog2
print('dog1 attacking dog2')
dog2_blood = dog2_blood - dog1_power

#dog2攻击dog1
print('dog2 attacking dog1')
dog1_blood = dog1_blood - dog2_power


# 面向对象的代码

#类是一个模板
class Dog:
	#构造方法
	def __init__(self, name, height, blood, power):
	self.name = name
	self.height = height
	self.blood = blood
	self.power = power

	def attack(self, dog2):
	dog2.blood = dog2.blood - self.power


d1 = Dog('大黄', 0.7, 10, 3)  # 创建第1个实例
d2 = Dog('二黑', 0.5, 10, 4)  # 创建第2个实例

print(f'攻击前：{d2.blood}')
d1.attack(d2)
print(f'攻击后：{d2.blood}')
