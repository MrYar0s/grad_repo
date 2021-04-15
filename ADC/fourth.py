#Fourth script

import RPi.GPIO as GPIO
import time

num_bits = 8
#comp = 

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

D = [24, 25, 8, 7, 12, 16, 20, 21]
LEDS = []

GPIO.output(17, 1)
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

def transfer(value):
	return (value * 3.3 / 255)

def sigdetection():
	N = 7
	middle = 128
	while N > 0:
		num2dac(middle)
		if GPIO.input(comp) == 1:
			middle -= 2**(N - 1)
		else:
			middle += 2**(N - 1)
		N -= 1
	return middle - 1

while True:
	try:
		num = sigdetection()
		i = 0
		while num != 0:
			i = 2**int(num / 32)
			num--
		for j in range(0, i):
			GPIO.output(LEDS[j], 1)
		print("Digital value: ", num)
	except KeyboardInterrupt:
		print("\n############################################")
		print("# Программа была остановлена пользователем #")
		print("############################################\n")
		exit()
	finally:
		GPIO.cleanup()
