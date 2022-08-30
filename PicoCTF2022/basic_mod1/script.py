#! /usr/bin/python3
import string


with open('message.txt') as f:
	inputList = [int(x) for x in next(f).split()]
	for i in inputList :
		m = i%37
		if m in range(0,26):
                	print(string.ascii_uppercase[m], end="")
		elif m in range(26,36):
                	print(string.digits[m-26], end="")
		else:
                	print("_", end="")
