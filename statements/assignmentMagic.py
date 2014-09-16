# Sequence Unpacking
x, y ,z = 1, 2, 3
print x, y ,z

# switch the contents of two (or more) 
x, y = y, x
print x, y ,z

values = 1, 2, 3
print values
x, y, z = values
print x

# chained assignments
x = y = dict( name = 'leon')
print x
print y 
# 3-parameters expression( a if b else c)
print 'x = y' if x == y else 'x <> y'

x = dict( name = 'Leon R.Sine' )
y = dict( name = 'Leon R.Sine' )
print 'x = y' if x == y else 'x <> y'

x = tuple([1, 2, 3])
y = tuple([1, 2, 3])
print 'x = y' if x == y else 'x <> y'

# Augmented Assignments
x = 2
x += 1
x *= 2

y = 'foo'
y += 'bar'
y *= 2
print y
