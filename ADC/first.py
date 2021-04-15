#First script

import RPi.GPIO as GPIO
import time

num_bits = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

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

while True:
	try:
		num = int(input("Enter value (-1 to exit) > \n"))
		if(num < 0):
			if(num == -1):
				exit()
			print("Вы ввели некорректное число. Производится выход из программы")
			exit()
		else:
			num2dac(num)
			print(num ,"=", transfer(num))
	except ValueError:
			print("Вы ввели некорректный тип данных. Производится выход из программы")
			exit()
	except KeyboardInterrupt:
		print("\n############################################")
		print("# Программа была остановлена пользователем #")
		print("############################################\n")
		exit()
	finally:
		GPIO.cleanup()