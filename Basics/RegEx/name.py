import re
name = input("Enter your name: ")
p = r"^[A-Z][]$"
if re.fullmatch(p,name):
    print("valid")
else:
    print("invalid")