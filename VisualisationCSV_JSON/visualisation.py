import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = 'sanfrancisco.csv'
with open(file_name) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	dates,highs,lows = [], [], []
	for row in reader:
		try:
			low = int(row[4])
			high = int(row[2])
			date = datetime.strptime(row[1],'%Y-%m-%d')
		except ValueError:
			print('There is an empty string existing in file!')
		else:
			lows.append(low)
			highs.append(high)
			dates.append(date)

plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.title('Highs and Lows of Temperatures')
plt.xlabel('Dates',fontsize=16)
plt.ylabel('Farenheits',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
