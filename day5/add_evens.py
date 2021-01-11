summa = 0
for number in range(2, 101, 2):
    summa += number

print(F"Summa of even numbers between 1 and 100 is {summa}")

even_numbers = [ x for x in range(2, 101) if x % 2 == 0 ]
print()
print("Using conditional list comprehension...")
print(even_numbers)
print(F"Sum of the array above is {sum(even_numbers)}")