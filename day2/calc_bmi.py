height: int = int(input("Enter your height [cm]: "))
weight: float = float(input("Enter your weight [kg]: "))
print(F"Your BMI is: {weight / ((height / 100.0) ** 2)}")
