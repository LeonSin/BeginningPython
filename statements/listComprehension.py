# list comprehensionis a way of making lists from other lists
print [x*x for x in range(10)]

print [ x for x in range(10) if  x % 3 == 0]

print [(x, y) for x in range(3) for y in range(3)]

# 2 for loops combined with an if clause
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print [b+'+'+g for b in girls for g in boys if b[0]==g[0]]
