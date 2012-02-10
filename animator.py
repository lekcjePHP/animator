
"""
a="#-----"
b="##----"
c="###---"
d="####--"
e="#####-"
f="######"
"""

import os
import time



while True:

	for i in range(80):
		j = 80-(2*i)
		k = 2*i
		klatka = k * "#"+j*'-'
		os.system("clear")
		print(klatka)
		time.sleep(0.1)
"""
	os.system("clear")
	print(a)
	time.sleep(0.5)
	os.system("clear")
	print(b)
	time.sleep(0.5)
	os.system("clear")
	print(c)
	time.sleep(0.5)
	os.system("clear")
	print(d)
	time.sleep(0.5)
	os.system("clear")
	print(e)
	time.sleep(0.5)
	os.system("clear")
	print(f)
	time.sleep(0.5)
	os.system("clear")
"""