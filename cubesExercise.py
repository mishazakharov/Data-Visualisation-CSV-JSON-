import matplotlib.pyplot as plt 

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,c=x_values,cmap=plt.cm.Blues,
										edgecolor='none',s=20)

plt.title('Cubes',fontsize=24)
plt.xlabel('Values',fontsize=12)
plt.ylabel('Cubes of.Values',fontsize=12)
plt.tick_params(axis='both',labelsize=12)

plt.show()
plt.savefig('cubes.png')