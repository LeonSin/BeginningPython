# break - end a loop
from math import sqrt
for n in range(99, 0, -1):
	root = sqrt(n)
	if root == int(root):
		print n
		break

# range function
print range(0, 10, 2)

# continue - terminates the current loop
# and jumps to the next one

# while True/break idiom
while True:
	word = raw_input('Please enter a word: ')
	if not word : break
	# do sth. with the word
	print 'The word was ' + word


# for - else : else clause only executed if you
# didn't call break
from math import sqrt
for n in range(99, 81, -1):
	root = sqrt(n)
	if root == int(root):
		print n
		break
else:
	print "Didn't find it"
