# comparison
x = 1
y = 2

test = 'x [{x}] > y [{y}] = ' + str(x > y) 
print(test.format(x=x,y=y))

test = 'x [{x}] < y [{y}] = ' + str(x < y)
print(test.format(x=x,y=y))

test = 'x [{x}] != y [{y}] = ' + str(x != y)
print(test.format(x=x,y=y))

test = 'x [{x}] == y [{y}] = ' + str(x == y)
print(test.format(x=x,y=y))

test = 'x [{x}] <= y [{y}] = ' + str(x <= y)
print(test.format(x=x,y=y))

test = 'x [{x}] >= y [{y}] = ' + str(x >= y)
print(test.format(x=x,y=y))