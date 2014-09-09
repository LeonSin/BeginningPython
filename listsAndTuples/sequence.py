# Python has 6 built-in types of sequences:
# lists and tuples(most common)
# strings, Unicode strings, buffer objects, and 
# xrange objects.

# Main difference between lists and tuples is that you can change
# a list,but you can't change a tuple.
# That's why you may see built-in functions returning tuples.

# Common Sequence Operations

# Indexing
print '-----Indexing-----'
greeting = 'Hello'
print greeting[0]
print greeting[-1]
print 'Hello'[1] # string literal

# Slicing
print '-----Slicing-----'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[3:6]
print numbers[0:1]
print numbers[-3:-1]
print numbers[-3:0]
print numbers[-3:]
print numbers[:3]
print numbers[:] # copy the entire sequence

# longer steps
print '-----Slicing:Longer Steps-----'
print numbers[0:10:1]
print numbers[0:10:2]
print numbers[1:10:2]

# step size can be negative
# When using a negative step size, you need to have a first limit (start index) that is higher than the second one.
print numbers[8:3:-1]
print numbers[10:0:-2]
print numbers[0:10:-2]
print numbers[::-2]
print numbers[5::-2]
print numbers[:5:-2]

# Adding sequences
print '-----Adding-----'
print [1, 2, 3] + [4, 5, 6]

# Multiplication
print '-----multiplication-----'
print 'python' * 5
print [42] * 10

# membership
print '-----Membership-----'
permission = 'rw'
print 'w' in permissions
print 'x' in permissions

#Length, Minimum, and Maximum
numbers = [100, 34, 678]
print len(numbers)
print max(numbers)
print min(numbers)
print max(2,3)
print max(9, 3, 2, 5)



