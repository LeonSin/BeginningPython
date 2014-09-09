# lista are mutable

def printSeparateLines(topic):
	print '-' * 5 + topic + '-' * 5

print list('Hello')

# To convert a list of characters such as the preceding code back to a string, you would use the following expressiona:

print type(''.join(['1','2']))
print ''.join(['1','2'])

# basic list operations
print '----- basic list operation-----'
# item assignments
print '----- assignment-----'
x = [1, 1, 1]
print x
x[1] = 2
print x

# deleting elements
print '-----deletion-----'
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
print names
del names[2]
print names

# Assigning to Slices
print '-----assigning to slices-----'
name = list('Perl')
print name
name[-2:] = list('ar')
print name

# length is different
name = list('Perl')
print name
name[1:] = list('ython')
print name

# insert elements
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print numbers

# reverse operation
numbers[1:4] = []
print numbers

# list methods
# A method is a function that is tightly coupled to some object, be it a list, a number, a string,or whatever
print '-----List Methods-----'

# append
# append does not simply return a new, modified list; instead, it modifies the old one directly.
print '-' * 5 + 'append' + '-' * 5
lst = [1, 2, 3]
lst.append(4)
print lst

# count
# The count method counts the occurrence of an elements in a list
printSeparateLines('count')
print ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x.count(1)
print x.count([1,2])

# extend
printSeparateLines('extend')
a = [1, 2, 3]
b = [4, 5 ,6]
print a

#This may seem similar to concatenation, but the important difference is that the extended sequence (in this case, a) is modified

a = [1, 2, 3]
b = [4, 5 ,6]
print a + b
print a

# index
# The index method is used for searching lists to find the index of the FIRST occurrence of a value

knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print knights.index('who')
print knights[4]

# insert
printSeparateLines('insert')
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print numbers

# pop
printSeparateLines('pop')
x = [1, 2 ,3]
print x.pop()
print x
print x.pop(0)
print x

# remove
# The remove method is used to remove the first occurrence of a value 
printSeparateLines('remove')
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print x

# reverse
printSeparateLines('reverse')
x = [1, 2, 3]
print x
x.reverse()
print x

# reversed function returns an iterator
x = [1, 2, 3]
print list(reversed(x))

# sort
printSeparateLines('sort')
x = [4, 6, 2, 1, 7, 9]
print x
x.sort()
print x

# One correct way of doing this(reserve order of x) would be to first bind y to a copy of x, and then sort y

x = [4, 6, 2, 1, 7, 9]
y = x[:] # y = x wouldn't work
y.sort()
print x
print y

# another way of doing upper task
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print x
print y

# sort in reverse order
x = [4, 6, 2, 1, 7, 9]
y = x[:]
y.sort()
y.reverse()
print x
print y

# advanced sorting
printSeparateLines('Advanced Sorting')
print cmp(42, 32)
print cmp(99, 100)
print cmp(10, 10)

numbers = [5, 2, 9, 7]
numbers.sort(cmp)
print numbers

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key = len)
print x

x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print x
