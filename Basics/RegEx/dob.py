import re
dob = input("Enter your date of birth: ")
p = r"^(0[1-9]|[1-2][0-9]|3[0-1])-(0[0-9]|1[0-2])-(19|20)\d{2}$"
if re.fullmatch(p,dob):
    print("valid")
else:
    print("invalid")