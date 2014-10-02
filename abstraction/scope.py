# -*- coding: utf-8 -*-

# There is a built-in function called vars, which returns this dictionary:
y = 1
scope = vars()
print scope['y']

# this sort of "invisible dictionary" is called a namespace or scope.


def foo(): x = 42
x = 1
foo()
print x

# nested scope


def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor

double = multiplier(2)
print double(5)

triple = multiplier(3)
triple(3)

print multiplier(5)(4)

# A function such as multiplyByFactor that stores its enclosing scopes is called a closure