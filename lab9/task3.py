import re

while True:
    print("For terminate program type exit")
    if input() == "exit":
        break
    path1 = r"C:\Users\WWW\Desktop\calculator.txt"
    path2 = r"C:\Users\WWW\Desktop\calculator2.txt"
    file1 = open(path1)
    string = file1.read()
    file1.close()

    chs = 0
    result = 0

    try:
        first = float(re.match(r"^\d+", string).group(0))
        print(first)
        # second = float(re.match(r"\d+$", string).group(0))
        # print(second)
        second = re.findall(r"\d+$", string)
        second = float("".join(second))
        print(second)
    except Exception as e:
        print(e)
        continue

    if re.match(r"\d+(\+|\-|\*|\/)\d+", string):
        temp = re.search(r"\+|-|\*|\/", string).group(0)
        if temp == "+":
            chs = 1
        elif temp == "-":
            chs = 2
        elif temp == "*":
            chs = 3
        elif temp == "/":
            chs = 4
        print(chs)
    else:
        print("program can't recognize expression")
        continue

    try:
        if chs == 1:
            result = first + second
        elif chs == 2:
            result = first - second
        elif chs == 3:
            result = first * second
        elif chs == 4:
            result = first / second
        print(result)
    except Exception as e:
        print(e)
        continue


    file2 = open(path2, 'w')
    string = string + " Результат = " + str(result)
    print(string)
    file2.write(string)
    file2.close()
