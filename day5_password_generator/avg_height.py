"""
    for loop practice
    Calculate the average without using len() and sum()
"""

student_heights = input("Enter a space separated list of your student's heights: ").split()
summa = 0.0
student_count = 0
for height in student_heights:
    summa += float(height)
    student_count += 1

print(F"The average height is {summa/student_count}")
