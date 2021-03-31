#Second script

import main

def repetitions(num):
	for j in range(0, num, 1):
			for i in range(0, 256, 1):
				dac.num2dac(i)
				time.sleep(0.3)
			time.sleep(0.3)
			for i in range(256, 0, -1):
				dac.num2dac(i)
				time.sleep(0.3)
		time.sleep(0.3)

try:
	number = int(input("Введите число повторений: "))
	if(number < 0):
		print("Вы ввели некорректное число. Производится выход из программы")
		exit()
	repetitions(number)
except Exception:
	print("Вы ввели некорректный тип данных. Производится выход из программы")
except KeyboardInterrupt:
	print("\n############################################")
	print("# Программа была остановлена пользователем #")
	print("############################################\n")
finally:
	GPIO.cleanup()