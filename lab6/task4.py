import random


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


def stooge_sort2(array, start_index, end_index):
    if array[start_index] > array[end_index]:
        swap(array, start_index, end_index)

    if end_index - start_index > 1:
        length = int((end_index - start_index + 1) / 3)
        stooge_sort2(array, start_index, end_index - length)
        stooge_sort2(array, start_index + length, end_index)
        stooge_sort2(array, start_index, end_index - length)

    return array


def stooge_sort1(array):
    return stooge_sort2(array, 0, len(array) - 1)


A = [0] * 100
print("We have this massive A:")
for i in range(len(A)):
    A[i] = random.randint(-49, 50)
print(A)

print("\nSorted massive A")
stooge_sort1(A)
print(A)
