import random

row = int(5)
column = int(8)
# must be row = 5, column = 8

A = [[0] * column for i in range(row)]
data = [3]

print(A)

for i in range(row):
    for j in range(column):
        A[i][j] = random.randint(-50, 50)
    # A[i, j] = int.Parse(Console.ReadLine())
print(A)

data = [A[0][0], 0, 0]
neg = bool(0)
for i in range(row):
    for j in range(column):
        if A[i][j] < 0:
            data[0] = A[i][j]
            data[1] = i + 1
            data[2] = j + 1
            neg = 1
if neg == 1:
    print("мінімальний елемент ", data[0], "; блок: ", data[1], ", елемент: ", data[2])
else:
    print("немає негативних елементів")
