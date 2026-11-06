import re
ph = input("Enter your phone number: ")
p = r"^[6|9]\d{9}$"
if re.fullmatch(p,ph):
    print("valid")
else:
    print("invalid")