"""
    Calculate the year is a leap-year and print the result
"""

year_to_check = int(input("Enter the year: "))

result = False
if year_to_check % 4 == 0:
    result = True
if year_to_check % 100 == 0 and year_to_check % 400 != 0:
    result = False

print("This is %s a leap year" % ("" if result else "not"))
