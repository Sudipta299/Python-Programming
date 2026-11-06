# Assigning Operator
a = 50
b = 30

#(/=): it first execute the operation between 'a' nd 'b' , and then assign the value into 'a' ( a = a/b)
a /= b
print(a)

# (*=):(x = x*y)
x = 20
y = 10
x *= y
print(x)

#(+=):(y = y+b)
y += b
print(y)

#(-=):(a = a+y)
a -=y
print(a)

#(%=):(m = m%n)
m = 60
n = 20
print(f"m = {m}")
print(f"n = {n}")
m %= n
print(f"m = {m}")

#(**=):()
p = 8
q = 2
print(f"p = {p}")
print(f"q = {q}")
p **= q
print(f"p = {p}")