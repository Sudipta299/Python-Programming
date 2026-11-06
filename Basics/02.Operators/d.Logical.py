# Logical Operators:
a = 50
b = 30

#logic NOT
print(not False) # not False = True
print(not True) # not True = False
print("\n")
print(not (a > b))
print(not (a == b))

#logic AND

print("\n")
print(False and True) # if one condition is true and another is false then it returns false 
print(True and True) # if both conditions are true it returns true
print(a>b and a==b)
print(a>b and b<a)

#logic OR

print("\n")
print(False or True) # if one of the condition is true and other is false it returns true
print(True or True) # if both conditions are true it returns true
print(False and False) # if both conditions are false true it returns false
print(a>b or a==b)
print(a>b or b<a)
print(a==b or a<b)