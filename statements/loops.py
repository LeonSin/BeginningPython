# while loops
x = 1
while x <= 100:
	print x
	x += 1

# for loops
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
	print word

print range(0, 10)
print range(10)

for number in range(1, 101):
	print number

# iterating over dictionaries
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
	print key, 'corresponds to', d[key]

print d.items()
for key, value in d.items():
	print key, 'corresponds to', value
