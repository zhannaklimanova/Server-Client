import matplotlib.pyplot as plot
import matplotlib.animation as animation
from matplotlib import style
import time

# Define parameters/style of graph

style.use('fivethirtyeight')
fig = plot.figure() 
figureAxis = fig.add_subplot(1,1,1)

# animate(i) main function that intakes sets of data and plots it

def animate(i):
	graph_data = open('PlottedData.txt', 'r').read() 
	lines = graph_data.split('\n') 
	xAxis = []
	yAxis = [] 
	for element in lines: 
		if len(element) > 1: 
			x, y = element.split(',')
			xAxis.append(int(x))
			yAxis.append(int(y))

	figureAxis.clear() 
	figureAxis.plot(xAxis, yAxis)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plot.show() 

