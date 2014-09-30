# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import string

def printSeparateLines(title):
	print '-' * 5 + title + '-' * 5

printSeparateLines('Useful constants')	
print string.digits # A string containing the digits 0–9 
print string.letters # A string containing all letters (uppercase and lowercase) 
print string.lowercase # A string containing all lowercase letters
print string.printable # A string containing all printable characters
print string.punctuation # A string containing all punctuation characters
print string.uppercase # A string containing all uppercase letters

# find 
printSeparateLines('find')	
title = "Monty Python's Flying Circus"
print title.find('Monty')
print title.find('Python')
print title.find('Flying')
print title.find('Zirquss')

subject = '$$$ Get rich now!!! $$$'
print subject.find('$$$')
print subject.find('$$$', 1) # Only supplying the start
print subject.find('!!!')
print subject.find('!!!', 0, 16) # Supplying start and end

# join
printSeparateLines('join')	
seq = ['1', '2', '3', '4', '5']
sep = '+'
print sep.join(seq) # Joining a list of strings

dirs = 'user', 'bin', 'env'
print '/'.join(dirs)
dirs = '', 'user', 'bin', 'env'
print '/'.join(dirs)
print 'C:' + '\\'.join(dirs)

# lower
printSeparateLines('lower')	
print 'Trondheim Hammer Dance'.lower()

# title
printSeparateLines('title')	
print "that's all folks".title()
print string.capwords("that's all, folks")

# replace
printSeparateLines('replace')	
print 'This is a test'.replace('is', 'eez')

# split: split is the inverse of join
printSeparateLines('split')	
print '1+2+3+4+5'.split('+')
print '/usr/bin/env'.split('/')
print 'Using   the   default'.split()

# strip
printSeparateLines('strip')	
print '      internal whitespace is kept      '.strip()
print '*** SPAM * for * everyone!!! ***'.strip(' *!')

# translate
printSeparateLines('translate')
from string import maketrans
table = maketrans('cs', 'kz') # translate dictionary for search
# Rprint len(table)
print table[97:123]
print maketrans('', '')[97:123]

print 'this is an incredible test'.translate(table)
