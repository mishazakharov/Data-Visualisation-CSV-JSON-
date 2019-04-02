import matplotlib.pyplot as plt 

x_values = list(range(1,6))
y_values = [x**3 for x in x_values]

plot.scatter(x_values,y_values,c='green',s=20)