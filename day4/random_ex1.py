import random
import my_module

random_int: int = random.randint(1, 10)
print(F"A random integer: {random_int}")

print(F"Pi's value is: {my_module.pi}")

random_float: float = random.random()
random_float_scaled : float = random.random() * 5.0

print(F"Random val: {random_float}\nScaled random float: {random_float_scaled}")

love_score = random.randint(1, 100)
print(F"Your love score is: {love_score}")