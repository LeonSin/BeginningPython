# Parallel iteration
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
	print names[i], 'is', ages[i], 'years old'

# A useful tool for parallel iteration is the built-in 
# function zip, which 'zips' together t
# sequences, returning a list of tuples:

print zip(names, ages)


# range calculates all the numbers
# xrange calculates only those numbers needed
print zip(range(5), xrange(10000000))

# Number iteraton

# enumerate() function lets you iterate over 
# index-value pairs,where the indices are
# supplied automatically
strings = ['xxx00xxx000xx000', 'xxx000', '000']
print list(enumerate(strings))
for index, string in enumerate(strings):
	if 'xxx' in string:
		strings[index] = '[censored]'
print strings

# Reversed and sorted iteration
print sorted([4, 3, 6, 8, 3])
print sorted('Hello, world!')
print list(reversed('Hello, world!'))
print ''.join(reversed('Hello, world!'))

