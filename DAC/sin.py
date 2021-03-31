import numpy as np
import matplotlib.pyplot as plt
import math

def makesin(time, freq, samplingFrequency):
	step = 1 / samplingFrequency
	npoints = int (time * samplingFrequency + 0.5)
	times = np.arange(0, time + step, step)
	rads = np.arange(0, freq * np.pi * (time + step), freq * step * np.pi)
	cords = 256 * np.sin(rads)
	for i in range(0, npoints, 1):
		cords[i] = abs(int(cords[i]))
	plt.plot(times, cords)
	plt.title('Синус')
	plt.xlabel('Время')
	plt.ylabel('Значения напряжения')
	plt.show()
	return cords

makesin(1, 4, 1000)