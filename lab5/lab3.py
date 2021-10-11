import random

n = int(3)
A = [[0] * n for i in range(n)]
B = [[0] * n for j in range(n)]

for i in range(n):
    for j in range(n):
        A[i][j] = random.randint(0, 100)
        B[i][j] = random.randint(0, 100)
print(A)
print(B)

X = []
for i in range(n):
    counter = 0
    for j in range(n):
        if A[i][j] == B[j][i]:
            counter += 1
        else:
            counter = 0
    if counter == 3:
        X.append(1)
    else:
        X.append(0)
print(X)
