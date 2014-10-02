# -*- coding: utf-8 -*-
def recursion():
    return recursion()

# recursion() # RuntimeError: maximum recursion depth exceeded

# two classics: Factorial and power


def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result


def factorialWithRecursion(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(10)
print factorialWithRecursion(10)