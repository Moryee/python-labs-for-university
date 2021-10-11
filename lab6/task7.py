import random

B = [0] * 100
print("We have this massive B:")
for i in range(len(B)):
    B[i] = random.randint(-49, 50)
print(B)

for i in range(len(B)):

    min_idx = i
    for j in range(i + 1, len(B)):
        if B[min_idx] > B[j]:
            min_idx = j

    B[i], B[min_idx] = B[min_idx], B[i]

print("\nSorted array B")
print(B)
