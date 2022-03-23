# summary unit 03 to 07
# integer to float, float to integer
float_to_integer = int(5/3)
integer_to_float = float(3+1)
print('float_to_integer = ',float_to_integer)
print('integer_to_float = ',integer_to_float)

# delete variable
my_var = 10
del my_var
# print(my_var) # error : 'my_var' is not defined

# define multiple variables
a, b, c = 10, 20, 30
print('a = ',a,', b = ',b,', c = ',c)
d = e = f = 30
print('d = ',d,', e = ',e,', f = ',f)

# get type of variable
my_string = 'hello'
my_int = 4
my_float = 1.0
print('my_string : ', type(my_string),' = ',my_string)
print('my_int : ', type(my_int),' = ',my_int)
print('my_float : ', type(my_float),' = ',my_float)

# assign input value to variable

input_string = input('input string : ')
input_int = int(input('input integer : '))
input_float = float(input('input float : '))
print('input_string : ', type(input_string),' = ',input_string)
print('input_int : ', type(input_int),' = ',input_int)
print('input_float : ', type(input_float),' = ',input_float)

# assign multiple variables from input
input_str_a, input_str_b = input('input "string_a string_b" : ').split()
input_int_a, input_int_b = map(int, input('input "int_a int_b" : ').split())
input_float_a, input_float_b = map(float, input('input "float_a float_b" : ').split())
print('input_str_a = ',input_str_a, ', input_str_b = ',  input_str_b)
print('input_int_a = ',input_int_a, ', input_int_b = ',  input_int_b)
print('input_float_a = ',input_float_a, ', input_float_b = ',  input_float_b)

# print with seperator
print(1,2,3,sep=', ')

# print with end
print(1,2,3,end='.')

# line break
print('1\n2\n3')