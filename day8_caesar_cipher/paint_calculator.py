"""
    Painting a wall:
    1 can of paint cal cover 5 square meters
    input:
        height
        width
        coverage : how many layers do we need
    output:
        number of full cans required
"""

import math

def calc_cans(height=0, width=0, coverage=5):
    return math.ceil((height * width) / coverage)


h = float(input("Wall height: \n"))
w = float(input("Wall width: \n"))
cov = int(input("Number of layers: \n"))
print(F"\nRequired cans: {calc_cans(h, w, cov)}")
