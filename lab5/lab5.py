# student = int(input("students: "))
student = int(2)
# mark = int(input("mark: "))  # size must be students = 20 marks = 10
mark = int(10)
A = [[0] * mark for i in range(student)]

A[1][2] = 1

for i in range(student):
    print(i + 1, " student: ")
    for j in range(mark):
        # A[i][j] = random.randint(0, 10)
        A[i][j] = int(input())

for i in range(student):
    print(A[i])

for i in range(mark):
    SUM = 0
    for j in range(student):
        SUM += A[j][i]
    print("average mark of ", i + 1, " student: ", SUM / student)

SUM = float(0)
gen_sum = float(0)
for i in range(student):

    # print(i + 1, " student: ")
    for j in range(mark):
        gen_sum += A[i][j]
        # print(A[i][j], "\t")

print("average mark of all class ", gen_sum / (mark * student))
