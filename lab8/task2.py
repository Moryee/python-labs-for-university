import re

string = input("write string: ")
r = re.compile("([0-9]|[A-F])([0-9]\.|[A-F]\.)([0-9]|[A-F])([0-9]\.|[A-F]\.)([0-9]|[A-F])([0-9]\.|[A-F]\.)([0-9]|[A-F])([0-9]|[A-F])")
a = re.findall(r, string)  # read
print(a)
# RegExr wasFF.11.FD.1F created by gski99.11.12.1Fnner.com, and is proDA.11.FD.1Fdly hosted by Media Temple.
chs = -1
line = -1
aaa = bool(1)

test2 = [0] * len(a)
for i in range(len(a)):
    test2[i] = "".join(a[i])

print(test2)

while chs != 2:
    while aaa == 1:
        print("What do you want? \n 1. change symbols \n 2. remove symbols")
        chs = int(input())
        print("In which string?")
        for i in range(len(test2)):
            print(i + 1, ". ", test2[i])
        line = int(input())
        if (chs == 1) | (chs == 2) | (line == 0) | (line > len(test2)):
            break

    if chs == 1:
        print("What do you want to replace?")
        change1 = input()
        print("by what?")
        change2 = input()
        test2[line - 1] = test2[line - 1].replace(change1, change2)
        print(test2[line - 1])
    elif chs == 2:
        print("What you want to remove?")
        print("Enter string, which you want to remove")
        change1 = input()
        test2[line - 1] = test2[line - 1].replace(change1, "")
        print(test2[line - 1])

    while aaa == 1:
        print("Something else? \n 1. yes \n 2. no")
        chs = int(input())
        if (chs == 1) | (chs == 2):
            break

print(test2)
