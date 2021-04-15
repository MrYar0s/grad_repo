#Second script

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
	return (value * (num2dac(255) - num2dac(0)) / 255)

def sigdetection():
	for i in range(0, 2**num_bits):
		num2dac(i)
		time.sleep(0.1)
		if GPIO.input(comp) == 1:
			return i

while True:
	try:
		num = sigdetection()
		print("Digital value: ", num, ", Analog value: ", transfer(num))
	except KeyboardInterrupt:
		print("\n############################################")
		print("# Программа была остановлена пользователем #")
		print("############################################\n")
		exit()
	finally:
		GPIO.cleanup()