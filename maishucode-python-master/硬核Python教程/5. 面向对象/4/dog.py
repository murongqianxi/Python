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



d1 = Dog('大黄', 0.7, 10, 3) #创建第1个实例
d2 = Dog('二黑', 0.5, 10, 4) #创建第2个实例

print(f'攻击前：{d2.blood}')
d1.attack(d2)
print(f'攻击后：{d2.blood}')

