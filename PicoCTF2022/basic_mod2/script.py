#! /usr/bin/python3
import string


def modInv(x,y) :
	for z in range(0,y) :
		if((x*z)%y) == 1 :
			return z
	print("No Inverse Found")


with open('message.txt') as f:
	inputList = [int(x) for x in next(f).split()]
	for i in inputList :
		m = i%41
		m = modInv(m,41)
		if m in range(1,27):
                	print(string.ascii_uppercase[m-1], end="")
		elif m in range(27,37):
                	print(string.digits[m-27], end="")
		else:
                	print("_", end="")
