# dictionary method

def printSeparateLines(title):
	print '-' * 5 + title + '-' * 5

# clear
# An in-place operation, so it returns nothing(or, rather, None)
printSeparateLines('clear')
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print d

returned_value = d.clear()
print d
print returned_value

# consider the two scenarios
x = {}
y = x
x['key'] = 'value'
print y
x = {}
print y

x = {}
y = x
x['key'] = 'value'
print y
x.clear()
print y

# copy 
printSeparateLines('clear')
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
# shallow copy
printSeparateLines('shallow copy')
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print y
print x

# deep copy
printSeparateLines('deep copy')
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c
print dc

# fromkeys
printSeparateLines('fromkeys')
print {}.fromkeys(['name', 'age'])
print dict.fromkeys(['name', 'age'])
print dict.fromkeys(['name', 'age'], '(unknown)')

# get -- you can use get to access a nonexistent key
printSeparateLines('get')
# d = {}  # this will go wrong
# print d['name'] 

d  = {}
print d.get('name')
print d.get('name', 'N/A')

# has_key
# The expression d.has_key(k) is equivalent to k in d
printSeparateLines('has_key')
d = {}
print d.has_key('name')

# items and iteritems
printSeparateLines('items and iteritems')
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print d.items()

it = d.iteritems()
print list(it) # convert the iterator to a list

# keys and iterkeys method

# pop
printSeparateLines('pop')
d = {'x': 1, 'y': 2}
print d.pop('x')
print d

# popitem -  
# This may be very useful 
# if you want to remove and process the items one by one in an efficient way
printSeparateLines('popitem')
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print d.popitem()
print d

# update 
printSeparateLines('update')
d = {
    'title': 'Python Web Site',
	'url': 'http://www.python.org',
	'changed': 'Mar 14 22:09:15 MET 2008'
}
x = {'title': 'Python Language Website'}
d.update(x)
print d

