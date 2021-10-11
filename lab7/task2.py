import random


def binary_search(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        return binary_search(arr, mid + 1, r, x)
    return -1


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

for i in range(len(A)):
    result = binary_search(B, 0, int(len(B) - 1), A[i])
    if result == -1:
        # print(A[i])
        C.append(A[i])
print(C)
