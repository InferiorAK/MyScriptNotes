# Author: InferiorAK
## Spinning Cursor in Python

from time import sleep as ghum

symbols = ["|","/","-","\\"]

for i in range(10):
	for symbol in symbols:
		print(f"\r{symbol}", end = "")
		ghum(0.5)
