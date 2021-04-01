from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
import math

num_bits = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

D = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.output(D[:], 0)

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

def num2dac(value):
    bits = decToBinList(value)
    for i in range (0, num_bits):
        GPIO.output(D[i], bits[num_bits - (i + 1)])

def makesin(time, freq, samplingFrequency):
	step = 1 / samplingFrequency
	npoints = int (time * samplingFrequency)
	rads = [0 for i in range(npoints)]
	cords = [0 for i in range(npoints)]
	times = [0 for i in range(npoints)]
	for i in range(0, npoints, 1):
		rads[i] = freq * step * np.pi * i
		cords[i] = (int(128 * math.sin(rads[i])))
		times[i] = step * i
		cords[i] = cords[i] + 128
	plt.plot(times, cords)
	plt.title('Синусоида')
	plt.xlabel('Время')
	plt.ylabel('Значения напряжения')
	plt.show()
	return cords

samplerate, data = wavfile.read("B01-006/DAC/SOUND.WAV")
print("Частота дискретизации = ", samplerate)
print(f"Количество каналов = {data.shape[1]}")
channels = data.shape[1]
length = float(data.shape[0] / samplerate)
print(f"Длительность = {length}с")
samperiod = 1 / samplerate
number = int(length / (samperiod))
print(number)
minimum = 0
maximum = 0
for i in range(0, number, 1):
    if(data[i, 0] < minimum):
        minimum = data[i, 0]
    if(data[i, 0] > maximum):
        maximum = data[i, 0]

print(maximum)
print(minimum)

rads = [0 for i in range(number)]
"""
for i in range(0, number, 1):
    rads[i] = int(256 * ((data[i, 0])/(abs(minimum)+maximum) + abs(minimum)/(abs(minimum)+maximum)))
"""
for i in range(0, number, 1):
    num2dac(int(256 * ((data[i, 1])/(abs(minimum)+maximum) + abs(minimum)/(abs(minimum)+maximum))))
    time.sleep(samperiod)
