import random

A = [0] * 100
B = [0] * 100

print("We have this massive A:")

for i in range(len(A)):
    A[i] = random.randint(-49, 50)
print(A)

print()
print("sorted massive A:")
for write in range(len(A)):
    for sort in range(len(A) - 1):
        if A[sort] > A[sort + 1]:
            temp = A[sort + 1]
            A[sort + 1] = A[sort]
            A[sort] = temp
print(A)
