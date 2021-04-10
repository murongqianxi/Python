class Pet:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

class Dog(Pet):
    def __init__(self, name, age, color):
        #super().__init__(name, age)
        self.name = name
        self.age = age 
        self.color = color 

d = Dog('wangcai', 4, 'yellow')
print(d.name)