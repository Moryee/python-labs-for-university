import re

string = "42342+4124"

second = re.findall(r"\d+$", string)
print(second)

second = int("".join(second))

print(second)


