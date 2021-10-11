import random

n = int(input("columns: "))
A = [[0] * (i + 1) for i in range(n)]
B = [0] * n

counter = int(0)
for i in range(n):
    # print(i + 1, " row:")
    for j in range(counter + 1):
        A[i][j] = random.randint(-5, 5)
        # A[i][j] = int(input())

        # summing negative numbers
        if A[i][j] < 0:
            B[i] += A[i][j]
    counter += 1
    # print("sum of ", i + 1, " row: ", B)

print(A)
print(B)
