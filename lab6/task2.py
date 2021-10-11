import random


def swap(arr, e1, e2):
    arr[e1], arr[e2] = arr[e2], arr[e1]
    return arr


def shaker_sort(array):
    for a in range(int(len(array) / 2)):
        swap_flag = bool(0)
        for j in range(a, len(array) - a - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                swap_flag = 1

        for j in range(len(array) - 2 - a, a, -1):
            if array[j - 1] > array[j]:
                swap(array, j - 1, j)
                swap_flag = 1

        if swap_flag == 0:
            break
    return array


A = [0] * 100
print("We have this massive  A:")
for i in range(len(A)):
    A[i] = random.randint(-49, 50)
print(A)

print("\nSorted massive A")
shaker_sort(A)
print(A)
