names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
	print names[i], 'is', ages[i], 'years old'

# A useful tool for parallel iteration is the built-in 
# function zip, which 'zips' together t
# sequences, returning a list of tuples:

print zip(names, ages)
