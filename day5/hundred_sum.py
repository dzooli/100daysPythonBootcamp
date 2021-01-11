summa = 0
number_array = [x for x in range(1, 101)]

for number in range(1, 101):
    summa += number

print(F"Sum of 1 to 100 is {summa}")
print()

print("Using list comprehension...")
print(F"Sum as an array is {sum(number_array)}")