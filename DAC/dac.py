#First script

import main

while True:
	try:
		num = int(input("Введите положительное число (-1 для выхода):\n"))
		if(num < 0):
			if(num == -1):
				exit()
			print("Вы ввели некорректное число. Производится выход из программы")
			exit()
		else:
			num2dac(num)
			time.sleep(4)
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