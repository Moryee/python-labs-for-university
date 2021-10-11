import random

size = int(25)
A = [[0] * 5 for i in range(5)]

for i in range(5):
    for j in range(int(size / 5)):
        A[i][j] = int(random.randint(-10, 20))

for i in range(5):
    print(A[i])


NUMB = [A[0], A[0], 0, 0, 0, 0]
mini = int(A[0][0])
maxi = int(A[0][0])

print()

for i in range(5):
    for j in range(5):
        blya = int(A[i][j])
        if blya < mini:
            mini = A[i][j]
            NUMB[2] = i  # index of minimum
            NUMB[4] = j
        if blya > maxi:
            maxi = A[i][j]
            NUMB[3] = i  # index of maximum
            NUMB[5] = j

# print("index of minimum ", NUMB[2] + 1, " ", NUMB[4] + 1)
# print("index of maximum", NUMB[3] + 1, " ", NUMB[5] + 1)

A[NUMB[2]][NUMB[4]] = maxi  # min -> max
A[NUMB[3]][NUMB[5]] = mini  # max -> min

for i in range(int(size / 5)):
    print(A[i])
