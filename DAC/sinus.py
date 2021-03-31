#Third script

import main
import sin

try:
	time = float(input("Введите время: "))
	freq = float(input("Введите частоту синусоидального сигнала: "))
	samplingFrequency = int(input("Введите частоту семплирования: "))
	samplingPeriod = 1 / samplingFrequency
	if freq <= 0 or time <= 0 or samplingFrequency <= 0:
		print("Вы ввели некорректное число. Производится выход из программы")
		exit()
	ndarray = sin.makesin(time, freq, samplingFrequency)
	for i in range(0, int(time * samplingFrequency + 0.5), 1):
		main.num2dac(ndarray[i])
		time.sleep(samplingPeriod)
except Exception:
	print("Вы ввели некорректный тип данных. Производится выход из программы")
except KeyboardInterrupt:
	print("\n############################################")
	print("# Программа была остановлена пользователем #")
	print("############################################\n")
#		print("Время = ", i * samplingPeriod," Значение напряжения = ", ndarray[i],"\n")
finally:
	GPIO.cleanup()