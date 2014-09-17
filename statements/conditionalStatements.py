# more complex conditions

# comparison operators
# x == y  x equals y.
# x < y  x is less than y.
# x > y  x is greater than y.
# x >= y  x is greater than or equal to y.
# x <= y  x is less than or equal to y.
# x != y  x is not equal to y.
# x is y  x and y are the same object.
# x is not y  x and y are different objects.
# x in y  x is a member of the container (e.g., sequence) y.
# x not in y  x is not a member of the container (e.g., sequence) y.

# The Equality operators
print "foo" == "foo"
print "foo" == "bar"

# is : The identity operator
x = y = [1, 2, 3]
z = [1, 2, 3]
print x == y
print x == z
print x is y
print x is z
# To summarize: use == to see if two objects are equal, 
# and use is to see if they are identical (the same object).

# in : the membership operator
name = 'Leon' 
if 's' in name:
    print 'Your name contains the letter "s".'
else:
	print 'Your name does not contain the letter "s".'


# string and sequence comparisons
# Strings are compared according to their order when sorted alphabetically
print "alpha" < "beta"
print 'FnOrD'.lower() == 'Fnord'.lower()
print [1, 2] < [2, 1]
print [2, [1, 4]] < [2, [1, 5]]

# Boolean Operators
# and / or 
# ternary operator / conditional operator
# a if b else c
# If b is true, a is returned; otherwise, c is returned.
