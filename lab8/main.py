import re

string = "RegExr wasFF.11.FD.1F created by gski99.11.12.1Fnner.com, and is proDA.11.FD.1Fdly hosted by Media Temple."
r = re.compile("([0-9]|[A-F])([0-9]\.|[A-F]\.)([0-9]|[A-F])([0-9]\.|[A-F]\.)([0-9]|[A-F])([0-9]\.|[A-F]\.)([0-9]|[A-F])([0-9]|[A-F])")
test2 = re.findall(r, string)  # read

test = list(["fasfsad", "sfsafsfd"])
print(test)
print(test2)

a = [0] * len(test2)
for i in range(len(test2)):
    a[i] = "".join(test2[i])

print(a)
# RegExr wasFF.11.FD.1F created by gski99.11.12.1Fnner.com, and is proDA.11.FD.1Fdly hosted by Media Temple.
