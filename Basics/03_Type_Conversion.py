#Auto conversion by Interpreter

a = 22         #int
b = 50.34      #float
c = a + b      #float
print(c)
print(type(c))


'''NOTE: Type conversion is done when the expression has variable (a and b) of different data types (int and float)
         so to evaluate the expression the data type is promoted from lower to higher leve data type.'''

'''double > float > long > int > short > char.'''


m = 220.3
n = 34.00
o = m*n
print(o)
print(type(o))