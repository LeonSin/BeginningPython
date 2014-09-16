# printing with commas
print 'Age:', 42
# The arguments of print do not form a tuple, as one might expect:
print 1, 2, 3
print (1, 2, 3)

# import something as someting
import math as foobar
print foobar.sqrt(4)

from math import sqrt as foobar
print foobar(4)
