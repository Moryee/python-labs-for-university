import random


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


def shell_sort(array):
    d = int(len(array) / 2)
    while d >= 1:
        for a in range(d, len(array)):
            j = a
            while (j >= d) & (array[j - d] > array[j]):
                swap(array, j, j - d)
                j = j - d
        d = int(d / 2)
    return array


B = [0] * 100
print("We have this massive B:")
for i in range(len(B)):
    B[i] = random.randint(-49, 50)
print(B)

print("\nSorted massive B")
print(shell_sort(B))
