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

