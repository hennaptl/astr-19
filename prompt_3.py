import numpy as np
import sys

#defines the equation
def f(x):
	return x**3+8

#deines the main variable
def main():
	x = 9
#gives us a connection between f(x) and the result of the problem
	result = f(x)
	print("Result:", result)

#if statement make the following print if true
	if result > 27:
		print("YAY!")

#duhhhh
if __name__ == '__main__':
	main()