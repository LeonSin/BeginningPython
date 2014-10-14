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


def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


def powerWithRecursion(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

print power(3, 4)
print powerWithRecursion(3, 4)


# Another classic: Binary Search
def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


# Python has a few functions that are useful for this sort of “functional programming”:
# map, filter, and reduce
# In Python 3.0, these are moved to the functools module
print map(str, range(10))
# Equivalent to [str(i) for i in range(10)]

def func(x):
    return x.isalnum()

seq = ["foo", "x41", "?!", "***"]
print filter(func, seq)

# Actually, there is a feature called lambda expressions,
# which lets you define simple functions in-line
# (primarily used with map, filter, and reduce):
# "lamdba" is used in mathematics to indicate an anonymous functions.


print filter(lambda x: x.isalnum(), seq)
