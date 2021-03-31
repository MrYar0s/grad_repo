#Forth script

import main
from scipy.io import wavfile
import scipy.io

samplerate, data = wavfile.read(.wav)
print("Частота дискретизации = ", samplerate)
print(f"Количество каналов = {data.shape[1]}")
channels = data.shape[1]
length = data.shape[0] / samplerate
print(f"Длительность = {length}с")

i = 0
for j in range(0, channels, 1):
	rest = length
		while rest > 0:
			num2dac(data[i], j)
			i = i + 1
			rest = rest - 1 / samplerate