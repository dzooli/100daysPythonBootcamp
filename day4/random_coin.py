import random

coin_val : int = random.randint(0, 100)
coin_side = (coin_val % 2) == 0

print("The coin side is %s" % ('Head' if coin_side else 'Tails'))
