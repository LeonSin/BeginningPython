# break - end a loop
from math import sqrt
for n in range(99, 0, -1):
	root = sqrt(n)
	if root == int(root):
		print n
		break

# range function
print range(0, 10, 2)
