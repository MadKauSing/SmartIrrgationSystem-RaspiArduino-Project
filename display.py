import plotext as plt
import csv
import time
def func():
	plt.clt()
	plt.cld()
	x=[]
	temp=[]
	soil=[]
	humid=[]
	light=[]
	height=[]

	with open('PlantData.csv','r') as csvfile:
		plots = csv.reader((x.replace('\0', '') for x in csvfile), delimiter = ',')
		for row in plots:
			x.append(row[0])
			temp.append(int(row[1]))
			soil.append(int(row[2]))
			humid.append(int(row[3]))
			light.append(int(row[4]))
			height.append(int(row[5]))


	x_values = range(1,len(x))
	plt.plot(temp[-20:],label="Temperature")
	plt.plot(soil[-20:],label="Soil moisture")
	plt.plot(humid[-20:],label="Humidity")
	plt.plot(light[-20:],label="Light")
	plt.plot(height[-20:],label="Height")
	plt.show()

if __name__ == "__main__":
	while True:
		#plt.clc()
		func()
		time.sleep(3)
