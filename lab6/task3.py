import random


def insertion_sort(arr):
    for a in range(len(arr) - 1):
        for j in range(a + 1, 0, -1):
            if arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
    return arr


A = [0] * 100
print("We have this massive A:")
for i in range(len(A)):
    A[i] = random.randint(-49, 50)
print(A)

print("\nSorted massive A")
insertion_sort(A)
print(A)
