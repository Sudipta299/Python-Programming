import re
roll = input("Enter your rollno: ")
p = r"^(CS)-\d{2}-\d{1,}$"
if re.fullmatch(p,roll):
    print("valid")
else:
    print("invalid")