# All the standard sequence operations(indexing, slicing,
# multiplication, membership, length, minimum,and maximum)
# work with strings, as you saw in the previous chapter.
# Remember, however ,that strings are immutable, so all
# kinds of item or slice assignments are illegal.

def printSeparateLines(title):
	print '-' * 5 + title + '-' * 5


# string formatting 
printSeparateLines('string formatting')
format = "hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print format % values

format = "Pi with three decimals: %.3f"
from math import pi
print format % pi

# The String module offers another way of formatting values: template strings.
# They work more like variable substitution in many UNIX shells.
printSeparateLines('Template String')
from string import Template
s = Template('$x, gloriois $x!')
# substitute returns a new string
print s.substitute(x = 'slurm')

# part of a word replacement
s = Template("It's ${x}tastic!")
print s.substitute(x='slurm')

# dollar sign input ?
s = Template("Make $$ selling $x")
print s.substitute(x = 'slurm')

# dict argument
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print s.substitute(d)

# simple conversion
printSeparateLines('simple conversion')
print 'Price of eggs: $%d' % 42
print 'Hexadecimal price of eggs: %x' % 42

from math import pi
print 'Pi: %f...' % pi
print 'Very inexact estimate of pi: %i' % pi
print 'Using str: %s' % 42L
print 'Using repr: %r' % 42L

# width and precision
printSeparateLines('width and precision')
print '%10f' % pi # Field width 10
print '%10.2f' % pi # Field width 10, precision 2
print '%.2f' % pi # Precision 2
print '%.5s' % 'Guido van Rossum'
print '%5s' % 'Guido van Rossum'

# Signs, alignment,and zero-padding
printSeparateLines('Signs, alignment,and zero-padding')
print '%010.2f' % pi
print '%-10.2f' % pi # any extra space is put on the right-hand side of the number

# A blank(" ") means that a blank should be put in front of positive numbers
print('% 5d' % 10) + '\n' + ('% 5d' % -10)

# Finally, a plus (+) means that a sign (either plus or minus) 
# should precede both positive and negative numbers
print ('%+5d' % 10) + '\n' + ('%+5d' % -10)
