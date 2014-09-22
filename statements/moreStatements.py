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
