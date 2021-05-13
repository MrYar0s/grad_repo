import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time as t

#Array of DAC pins (blue)
D = [26, 19, 13, 6, 5, 11, 9, 10]
#Array of LEDS pins (green)
LEDS = [21, 20, 16, 12, 7, 8, 25, 24]

#Setmode for RPI
GPIO.setmode(GPIO.BCM)
#Setup for DAC
GPIO.setup(D, GPIO.OUT)
#Setup for LEDS
GPIO.setup(LEDS, GPIO.OUT)
#Setup for comparator
GPIO.setup(4, GPIO.IN)
#Setup for troykaModule
GPIO.setup(17, GPIO.OUT)

#Turn off all pins
GPIO.output(D, 0)
GPIO.output(LEDS, 0)

def decToBinList(decNumber):
	decNumber = decNumber % 256
	N = num_bits - 1
	bits = []
	while N > 0:
		if(int(decNumber/(2**N)) == 1):
			bits.append(1)
			decNumber -= 2**N
		else:
			bits.append(0)
		N -= 1
	bits.append(decNumber)
	return bits

def num2leds(value):
	bits = decToBinList(value)
	GPIO.output(LEDS, bits)

def num2dac(value):
	bits = decToBinList(value)
	GPIO.output(D, bits)

def adc():
	#num of bits - 1
	N = 7
	#middle amount between 0 and 256
	middle = 128
	#status of the comparatop
	#status = 1 -- value is higher
	#status = 0 -- value is lower
	status = GPIO.input(4)
	while N > 0:
		num2dac(middle)
		time.sleep(0.001)
		if !status:
			middle -= 2**(N - 1)
		else:
			middle += 2**(N - 1)
		N -= 1
	if !status:
		middle -= 1
	else:
		middle += 1
	return middle

def prepare():
	#Turn off troykaModule supply
	GPIO.output(17, 0)
	while adc > 0:
		print('Wait! There is a discharge of the capacitor')
		t.sleep(1)

measure = []
listT = []
listV = []
time_start = t.time()

def charge():
	GPIO.output(17, 1)
	while adc < 254:
		measure.append(adc)
		listT.append(t.time() - time_start)
		t.sleep(0.0001)

def discharge():
	GPIO.output(17, 0)
	while adc > 0:
		measure.append(adc)
		listT.append(t.time() - time_start)
		t.sleep(0.0001)

def convertion():
	num_of_elements = len(measure)
	for i in range(0, num_of_elements):
		listV[i] = (measure[i] * 3.3)/ 255

def makeplotV():
	plt.plot(listT, listV)
	plt.title('Процесс зарядки и разрядки конденсатора')
	plt.xlabel('Время t, с')
	plt.ylabel('Напряжение на конденсаторе U, В')

def makeplotM():
	plt.plot(listT, measure)
	plt.title('Процесс зарядки и разрядки конденсатора')

def makefile():
	np.savetxt('data.txt', listV, fmt='%d')
	num_of_elements = len(listV)
	sumV = 0
	sumT = 0
	for i in range(0, num_of_elements):
		sumV += listV[i]
		sumT += listT[i]
	dT = sumT / num_of_elements
	dV = sumV / num_of_elements
	with open('settings.txt', 'w') as settings:
		settings.write('dT = ' + repr(dT) + 'с' + '\n' + 'dV = ' + repr(dV) + 'В')
		settings.close
try:
	prepare()
	charge()
	discharge()
	convertion()
	makeplotM()
	makeplotV()
	makefile()
finally:
	GPIO.cleanup()