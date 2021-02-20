from random import randint
import pygal


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die1 = Die()
die2 = Die(10)
results = []
for roll_num in range(50000):
    result = die1.roll()+die2.roll()
    results.append(result)
frequencies = []
max_result = die1.num_sides+die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 对结果进行可视化
hist = pygal.Bar()
hist.title = 'Results of rolling a D6 and a D10 50,000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual(3).svg')
