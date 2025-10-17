import numpy as np
import sys

def main():
    x = 2.0  # this is a floating point number
    y = 3.0  # this is a floating point number
    n = 6    # this is an integer
    t = 4    # also an integer

    # I will add the floats first
    print('x + y =', x + y)
    print(type(x + y))

    # Now we subtract the integers
    print('n - t =', n - t)
    print(type(n - t))

    # Now to multiply the integer and float
    print('x * n =', x * n)
    x = float(x)
    print(type(x * n))

if __name__ == "__main__":
    main()
