# Author: InferiorAK
# Spinning Cursor in Python

from time import sleep as ghum

def spin():
	# symbols = ["|","/","-","\\"]
	symbols = ["| Loading. Please Wait", "/ Loading. Please Wait", "- Loading. Please Wait", "\\ Loading. Please Wait"]
	while True:
		for symbol in symbols:
			print(f"\r{symbol}", end="")
			ghum(0.5)

spin()
