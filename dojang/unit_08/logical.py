# logical
x = True
y = False
z = y

print('x = True, x.id','y = False','z = y',sep='\n',end='\n--------\n')

test = 'x [{x}] and y [{y}] = ' + str(x and y)
print(test.format(x=x,y=y))

test = 'not x [{x}] and y [{y}] = ' + str(not x and y)
print(test.format(x=x,y=y))

test = 'x [{x}] or y [{y}] = ' + str(x or y)
print(test.format(x=x,y=y))

test = 'not x [{x}] or y [{y}] = ' + str(not x or y)
print(test.format(x=x,y=y))

test = 'x [id({x})] is z [id({z})] = ' + str(x is z)
print(test.format(x=id(x),z=id(z)))

test = 'x [id({x})] is not z [id({z})] = ' + str(x is not z)
print(test.format(x=id(x),z=id(z)))

test = 'y [id({y})] is z [id({z})] = ' + str(y is z)
print(test.format(y=id(y),z=id(z)))

test = 'y [id({y})] is not z [id({z})] = ' + str(y is not z)
print(test.format(y=id(y),z=id(z)))