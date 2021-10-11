import re

path1 = r"C:\Users\WWW\Desktop\TF_1.txt"
path2 = r"C:\Users\WWW\Desktop\TF_2.txt"
file = open(path1)
string = re.findall(r"(\w{1,16})", file.read())

# for i in range(len(string) - 1):
#     for j in range(len(string) - 1):
#         if len(string[i]) > len(string[j + 1]):
#             string[j], string[j+1] = string[j+1], string[j]

string = sorted(string, key=len)

counter = 0
for i in range(len(string) - 1):
    counter += 1
    if len(string[i]) < len(string[i + 1]):
        string[i] += " " + str(counter)
        counter = 0
    if i == len(string) - 2:
        counter += 1
        string[i + 1] += " " + str(counter)

temp = ""
for i in range(len(string)):
    temp += string[i] + "\n"

file2 = open(path2, 'w')
file2.write(temp)
file.close()
file2.close()
