import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
	# Построение случайного блуждания и нанесение точек на диаграмму.
	rw = RandomWalk()
	x = rw.get_step_x()
	y = rw.get_step_y()
	rw.fill_walk(x,y)
	num_points = list(range(1,4))
	plt.scatter(rw.x_values,rw.y_values,c=num_points,cmap=plt.cm.Blues,
												edgecolor='none',s=15)
	# Выделение первой и последней точек.
	plt.scatter(0,0,c='Red',edgecolor='none',s=40)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='Red',
							edgecolor='none',s=40)
	# Удаление осей.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()
	answer = input('Do you want to continue ?')
	if answer == 'n':
		break