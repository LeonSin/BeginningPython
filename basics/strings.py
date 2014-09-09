
# repr creates a string that is a representation 
# of the value as a legal Python expression.
print repr("hello, world!")
print repr(10000L)
print '-----------'
# str simply converts a value into a string in some reasonable
# fashion that will probably be understood by a user.

print str("Hello, world!")
print str(10000L)
print '-----------'

# ` is backstick which locates on the left of num 1 in keyboard
# however backsticks are removed in Python 3.0
temp = 42
print "the temperature is " + `temp`
print '-----------'

'''
In short, str, repr, and backticks are three ways of converting a Python value to a string. 
The function str makes it look good, while repr (and the backticks) tries to make the resulting 
string a legal Python expression.
'''

# long strings - use triple quotes instead of ordinary quotes
print '''This is a very long string.
It continues here.
And it's not over yet.
"Hello, world!"
Still here.'''
print '-----------'

# Every character you put into a raw string stays the way you wrote it:
print r'C:\nowhere'
print r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz'
print '-----------'


# Unicode Strings
# Normal strings in Python are stored internally as 8-bit ASCII,
# while Unicode strings are stored as 16-bit Unicode.
print u'Hello, world!'
print '-----------'
# In Python 3.0, all strings will be Unicode strings.
