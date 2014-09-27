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