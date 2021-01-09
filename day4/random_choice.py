import random

names: str = input("Enter the name list: ")
namelist = names.split(",")
print(F"Random choice is: {random.choice(namelist)}")
