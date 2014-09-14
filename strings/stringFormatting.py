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
