import pygal
from random import randint
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll in range(1000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

frequencies = []
max_result = die_1.numsides + die_2.numsides + die_3.numsides
for value in range(3,max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Rolling a cubes'
hist.x_labels = []
for number in range(3,max_result + 1):
	hist.x_labels.append(str(number))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6 + D6',frequencies)
hist.render_to_file('dive_visual.svg')
