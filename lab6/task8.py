import random


def partition(arr, low, high):
    a = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            a = a + 1
            arr[a], arr[j] = arr[j], arr[a]
    arr[a + 1], arr[high] = arr[high], arr[a + 1]
    return a + 1


def quick_sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


B = [0] * 100

print("We have this massive B:")
for i in range(len(B)):
    B[i] = random.randint(-49, 50)
print(B)

quick_sort(B, 0, len(B) - 1)
print("Sorted array B")
print(B)
