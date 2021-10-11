import math


def integral(x1, x2):
    result = math.sqrt(4 * x2 + math.sin(math.sqrt(pow(x2, 3)))) - math.sqrt(4 * x1 + math.sin(math.sqrt(pow(x1, 3))))
    return result


a = float(input("a :"))
b = float(input("b :"))
s = integral(a, 3) + integral(a, b)
print(s)