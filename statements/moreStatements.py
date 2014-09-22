# nothing happened
name = 'Enid'
if name == 'Ralph Auldus Melish':
	print 'Welcome!'
elif name == 'Enid':
	# Not finished yet...
	print 'nothing happened'
	pass
elif name == 'Bill Gates':
	print 'Access Denied'

# deleting with del statements
scoundrel = {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
robin = scoundrel
print scoundrel
print robin
scoundrel = None
print robin
robin = None
print robin

# use del
x = 1
del x
# print x - NameError: name 'x' is not defined

x = ["Hello", "world"]
y = x
y[1]="python"
print x

# del delete only the name, not the value.
# there is no way to delete values in Python
del x
print y

# Executing and evaluating strings with exec and eval
# learn to execute Python code stored in a string

# exec
exec "print 'Hello, world!'"

# namespace and scope
from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt']
print len(scope)
print scope.keys()

# eval
# eval evaluates a Python expression (written in a string) 
# and returns the resulting value
print eval(raw_input("Enter an arithmetic expression: "))
