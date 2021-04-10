class Car:
    
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def show(self):
        print("Car name is {}, brand is {}".format(self.name, self.brand))

    def run(self):
        print("汽车{}跑起来了。".format(self.name))


# 第4题
class Car4:
    
    def __init__(self, name, brand, max_people, number_of_people=0):
        self.name = name
        self.brand = brand
        self.max_people = max_people
        self.number_of_people = number_of_people

    def show(self):
        print("Car name is {}, brand is {}, {} people on the car".format(self.name, self.brand, self.number_of_people))

    def run(self):
        print("汽车{}跑起来了。".format(self.name))

    def set_people(self, number_of_people):
        if number_of_people > self.max_people:
            print('人太多了')
            # raise Exception('人太多了')
        elif number_of_people <= 0:
            self.number_of_people = 0
        else:
            self.number_of_people = number_of_people

    def increase_people(self):
        number_of_people = self.number_of_people + 1
        self.set_people(number_of_people)

    def reduce_people(self):
        number_of_people = self.number_of_people - 1
        self.set_people(number_of_people)

        
class Pig:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def show(self):
        print("Pig name is {}, weight = {}kg".format(self.name, self.weight))

    def run(self):
        print("{}: 没吃过猪肉，让你看看猪跑！".format(self.name))


def sep(i):
    print()
    print('='*20 + ' {} '.format(i) + '='*20)


# ========================================
if __name__ == "__main__":
    sep(1)
    c = Car('n1', 'BMW')
    print(c.name)
    print(c.brand)
    c.show()
    c.run()


    sep(2)
    for i in range(5):
        c = Car('n'+str(i), 'BMW')
        c.show()


    sep(3)
    for i in range(5):
        p = Pig('P'+str(i), (i+50.2))
        p.show()


    sep(4)
    c4 = Car4('MyCar', 'BMW', 5)
    c4.set_people(1)
    c4.show()

    for i in range(6):
        c4.increase_people()
        c4.show()

    for i in range(6):
        c4.reduce_people()
        c4.show()
