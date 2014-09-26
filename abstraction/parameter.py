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

xlink = test()

print xlink

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


def print_params(*params):
    """
    collecting parameters
    The star in front of the parameter puts all the values into the same tuple
    *params refers to a tuple
    """
    print params

print_params('Testing')
print_params(1, 2, 3)


def print_params_2(title, *params):
    """
    collecting parameters
    """
    print title
    print params

print_params_2('Params:', 1, 2, 3)
print_params_2('Nothing:')


def print_params_3(**params):
    """
    **params refers to a map
    """
    print params

print_params_3(x=1, y=2, z=3)


def print_params_4(x, y, z=3, *pospar, **keypar):
    """
    put the above together
    """
    print x, y, z
    print pospar
    print keypar

print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)




def add(x, y):
    # reverse the process described above
    return x + y

params = (1, 2)
print add(*params)

params = {'name': 'Sir Robin', 'greeting': 'Well me'}
hello_3(**params)

# Tips:It may be useful to use these splicing operators to "pass through" parameters,
# without worrying too much about how many there are


def foo(x, y, z, m=0, n=0):
    print x, y, z, m, n


def call_foo(*args, **kwds):
    print "Calling foo!"
    print args
    print kwds
    foo(*args, **kwds)

# This can be particularly useful when calling the constructor of a superclass
call_foo(1,2,3, m=1, n=2)