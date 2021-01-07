"""
    Description:
        Welcome message
        Ask for bill total, persons and tip percentage

        Print the per-person payment requirement including the tip
"""

if __name__ == "__main__":
    print("Welcome to the tip calculator!", '', sep='\n')
    total_payment = float(input("Enter the total of the bill: $"))
    person_count = int(input("How many people should pay the bill?: "))
    tip_percent = int(input("How many percent is the tip?: "))
    print(F"The per-person payment is: ${round((total_payment * (1.0 + (tip_percent / 100))) / person_count, 2)}")
