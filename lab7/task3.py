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

combo = int(0)
start = int(0)
comboInfo = [0] * 3

for i in range(len(A)):
    result = int(binary_search(B, 0, int(len(B) - 1), A[i]))
    if result == -1:
        if combo == 0:
            start = i
            print(i, "st: ")
        combo += 1
        print(A[i], " ")
    elif result != -1 & comboInfo[0] < combo:
        comboInfo[0] = combo
        comboInfo[1] = start
        comboInfo[2] = i
        combo = 0
    else:
        combo = 0



for i in range(comboInfo[1], comboInfo[2]):
    print(A[i])
