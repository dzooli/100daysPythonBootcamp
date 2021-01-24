import math

def prime_checker(number=0):
    if number <= 2:
        return True
    for i in range(2, int(math.floor(number / 2))):
        if number % i == 0:
            return False
    return True


n = int(input("Check this number: \n"))
print("Prime" if prime_checker(number=n) else "Not prime")
