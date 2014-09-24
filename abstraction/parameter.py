# thorough introdution to parameters and scoping

# laziness is a virtue

# Fibonacci numbers
fibs = [0, 1]
for i in range(8):
	fibs.append(fibs[-2] + fibs[-1])

print fibs

# creating your own functions

# documenting fcuntions
# If you put a string at the beginning of a function,
# it's stored as part of the function and is called
# a docstring

def square(x):
	'Calculates the square fo the number x.'
	return x * x 
print square.__doc__
