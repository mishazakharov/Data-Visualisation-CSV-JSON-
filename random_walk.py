import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
	def __init__(self,numpoints=3):
		'''Класс для генерирования случайных событий.'''
		self.numpoints = numpoints

		# Все блуждания начинаются с точки (0,0).
		self.x_values = [0]
		self.y_values = [0]


	def get_step_x(self):
		'''Вычисляет шаг.'''
		
		# Определение направление и длины шага.
		x_direction = choice([1,-1])
		x_distance = choice([0,1,2,3,4])
		x_step = x_direction * x_distance
		return x_step

	def get_step_y(self):
		y_direction = choice([1,-1])
		y_distance = choice([0,1,2,3,4])
		y_step = y_direction * y_distance
		return y_step

	def fill_walk(self,x,y):
		'''Вычисляет все точки блуждания.'''
		# Шаги генерируются до достижения нужной длины.
		while len(self.x_values) < self.numpoints:
			x_step = x
			y_step = y
			if x_step == 0 and y_step == 0:
				continue
			# Вычисление следующих значений x и y.
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)

	

			
