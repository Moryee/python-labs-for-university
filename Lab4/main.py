import math


def s(r):
    return 4 * math.pi * pow(r, 2)


radius = int(input("radius: "))
print(s(radius))
