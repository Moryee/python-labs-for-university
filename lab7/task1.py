import random


def linear_search(arr1, arr2, arr3):
    for a in range(len(arr1)):
        temp = bool(1)
        for j in range(len(arr2)):
            if arr1[a] == arr2[j]:
                temp = 0
        if temp == 1:
            # print(arr1[a])
            arr3.append(arr1[a])


A = [0] * 100
B = [0] * 100
C = []
for i in range(len(A)):
    A[i] = random.randint(-49, 50)
    B[i] = random.randint(-49, 50)

A.sort()
B.sort()

print(A)
print(B)
linear_search(A, B, C)
print(C)
