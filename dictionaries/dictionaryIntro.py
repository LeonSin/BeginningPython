
def printSeparateLines(title):
	print '-' * 5 + title + '-' * 5

printSeparateLines('dict definition')
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

printSeparateLines('dict function')
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print d

d = dict(name='Gumby', age=42)
print d

# x = []
# x[42] = 'Foobar' # list assignment index out of range
# but there is no problem below
x = {}
x[42] = 'Foobar'
print x

printSeparateLines('String Formating with Dictionaries')
print phonebook
print "Cecil's phone number is %(Cecil)s." % phonebook

template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<P>%(text)s</p>
</body>'''

data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print template % data
