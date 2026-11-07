import pandas as pd

dataset = {"Name": ["Pablo", "Frank", "Khun", "Amado", "Gilberto"],
           "roll": ["cs-99-21", "cs-98-34", "cs-85-60", "cs-99-12", "cs-99-45"],
           "marks": [54, 65, 55, 67, 45],
           "redge": [9901230100, 9801230102, 8501230103, 9901230104, 9901230105],
           "dsf": [98, 89, 97, 90, 88],
           "ds": [90, 88, 89, 87, 86],
           "oops": [88, 87, 86, 85, 84],
           "math": [87, 86, 85, 84, 83],
           "dec": [86, 85, 84, 83, 82],
           "ob": [50, 50, 50, 50, 50]}
df = pd.DataFrame(dataset)
print(df)

df["total"] = df["dsf"] + df["ds"] + df["oops"] + df["math"] + df["dec"] + df["ob"]
print(df)

df["percentage"] = df["total"]/600 *100
print(df)

def cal(percentage):
    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "E"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

df["grade"] = df["percentage"].apply(cal)
print(df)

#To convert the file into a CSV file:
df.to_csv("Student.csv")

#To read the csv file:
data = pd.read_csv("Student.csv")

