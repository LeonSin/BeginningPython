# thorough introduction to parameters and scoping

# laziness is a virtue

# Fibonacci numbers
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

print fibs

# creating your own functions

# documenting functions
# If you put a string at the beginning of a function,
# it's stored as part of the function and is called
# a docstring


def square(x):
    """Calculates the square fo the number x."""
    return x * x


print square.__doc__

# help(square)

# functions that aren't really functions


def test():
    print 'This is printed'

x = test()

print x

# return None

# the magic of parameters

# Parameters are kept in what is called a local scope

# keyword parameters and defaults

#  positional parameters are above


def hello_1(greeting, name):
    print '%s, %s!' % (greeting, name)


def hello_2(name, greeting):
    print '%s, %s!' % (name, greeting)


hello_1('Hello', 'world')
hello_2('Hello', 'world')
# supply the name of your parameter that called as keyword parameters.
hello_1(greeting='Hello', name='world')
hello_1(name='world', greeting='Hello')


def hello_3(greeting='Hello', name='world'):
    """ arguments that have default values"""
    print '%s, %s!' % (greeting, name)

hello_3()
hello_3('Greetings')
hello_3('Greetings', 'universe')