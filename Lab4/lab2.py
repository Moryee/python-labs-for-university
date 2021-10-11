def func(x, i, result):
    if (x > 0) & (i <= 5):
        if i > 5:
            return result
        result += pow(x, i)
        i += 1
        func(x, i, result)
    elif (x <= 0) & (i <= 5):
        if result == 0:
            result = 1
        if i > 5:
            return result
        result *= pow(x, i)
        i += 1
        func(x, i, result)
    return result


a = float(input("a: "))
b = float(input("b: "))

u = float((func(a, 1, 0) + func(2, 1, 0) + func(b, 1, 0)))

print("u = ", u)
