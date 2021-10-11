class MatrixShort:
    __codeError = 0
    # 1. fields / 2. c-tors
    def __init__(self):
        self.__array = [0]

    def __init__(self, a, b):
        self.__array = [[0] * a] * b

    def __init__(self, a, b, t):
        self.__array = [[t] * a] * b

    # 4. methods
    def fill_manually(self):
        for i in self.__array:
            for j in i:
                print("- ", end=" ")
                j = input()

    def print(self):
        for i in self.__array:
            for j in i:
                print(j, end=" ")
            print()

    def fill_by_number(self, a):
        self.__array = [[x * 0 + a for x in r] for r in self.__array]

    # 5. properties
    def size(self):
        return len(self.__array)

    def codeError(self):
        return self.__codeError

    # 6. indexer
    def __getitem__(self, i, j):
        try:
            self.__codeError = 0
            return self.__array[i][j]
        except Exception as e:
            self.__codeError = 1
            return e

    # 7. overloads
    def __pos__(self):
        temp = self.__array = [[x+1 for x in r] for r in self.__array]
        return temp

    def __neg__(self):
        temp = self.__array = [[x-1 for x in r] for r in self.__array]
        return temp

    def __invert__(self):
        temp = self.__array = [[~x for x in r] for r in self.__array]
        return temp

    def __add__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x + other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x + other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __sub__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x - other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x + other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __mul__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x * other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x * other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __truediv__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x / other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x / other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __mod__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x % other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x % other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __or__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x | other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x | other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __and__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x & other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x & other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __xor__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x ^ other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x ^ other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __rshift__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x >> other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x >> other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __lshift__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [[x << other for x in r] for r in self.__array]
            return temp
        else:
            temp = []
            temp1 = 0
            temp2 = 0
            for r in self.__array:
                temp2 = 0
                for x in r:
                    temp.append(x << other.__array[temp1][temp2])
                    temp2 += 1
                temp1 += 1
            return temp

    def __eq__(self, other):
        sum1 = sum(len(row) for row in self.__array)
        sum2 = sum(len(row) for row in other.__array)
        if sum1 != sum2:
            return False
        temp1 = 0
        temp2 = 0
        for r in self.__array:
            temp2 = 0
            for x in r:
                if x != other.__array[temp1][temp2]:
                    return False
                temp2 += 1
            temp1 += 1
        return True

    def __ne__(self, other):
        sum1 = sum(len(row) for row in self.__array)
        sum2 = sum(len(row) for row in other.__array)
        if sum1 != sum2:
            return False
        temp1 = 0
        temp2 = 0
        for r in self.__array:
            temp2 = 0
            for x in r:
                if x != other.__array[temp1][temp2]:
                    return True
                temp2 += 1
            temp1 += 1
        return False

    def __gt__(self, other):
        sum1 = sum(len(row) for row in self.__array)
        sum2 = sum(len(row) for row in other.__array)
        if sum1 != sum2:
            return False
        temp1 = 0
        temp2 = 0
        for r in self.__array:
            temp2 = 0
            for x in r:
                if x <= other.__array[temp1][temp2]:
                    return False
                temp2 += 1
            temp1 += 1
        return True

    def __lt__(self, other):
        sum1 = sum(len(row) for row in self.__array)
        sum2 = sum(len(row) for row in other.__array)
        if sum1 != sum2:
            return False
        temp1 = 0
        temp2 = 0
        for r in self.__array:
            temp2 = 0
            for x in r:
                if x >= other.__array[temp1][temp2]:
                    return False
                temp2 += 15
            temp1 += 1
        return True

    def __le__(self, other):
        sum1 = sum(len(row) for row in self.__array)
        sum2 = sum(len(row) for row in other.__array)
        if sum1 != sum2:
            return False
        temp1 = 0
        temp2 = 0
        for r in self.__array:
            temp2 = 0
            for x in r:
                if x > other.__array[temp1][temp2]:
                    return False
                temp2 += 1
            temp1 += 1
        return True

    def __ge__(self, other):
        sum1 = sum(len(row) for row in self.__array)
        sum2 = sum(len(row) for row in other.__array)
        if sum1 != sum2:
            return False
        temp1 = 0
        temp2 = 0
        for r in self.__array:
            temp2 = 0
            for x in r:
                if x < other.__array[temp1][temp2]:
                    return False
                temp2 += 1
            temp1 += 1
        return True

    # 3. destructor
    def __del__(self):
        print("Destructor has been called")


obj1 = MatrixShort
obj2 = MatrixShort
while True:
    try:
        print("Matrix 1")
        temp1 = input("Size1: ")
        temp2 = input("Size2: ")
        chs = input("Argument: ")
        obj1 = MatrixShort(int(temp1), int(temp2), int(chs))

        print("Matrix 2")
        temp1 = input("Size1: ")
        temp2 = input("Size2: ")
        chs = input("Argument: ")
        obj2 = MatrixShort(int(temp1), int(temp2), int(chs))
        break
    except Exception as e:
        print(e)
        continue
while True:
    try:
        print("\n\n1. New Matrix \n2. Type elements of Matrix manually \n3. Show Matrix \n4. Fill by number "
              "\n5. Quantity of Matrix \n6. ??? \n7. Size of Matrix \n8. Indexer \n9. Overload")
        chs = int(input())
        if chs == 1:
            print("Matrix 1")
            temp1 = input("Size1: ")
            temp2 = input("Size2: ")
            chs = input("Argument: ")
            obj1 = MatrixShort(int(temp1), int(temp2), int(chs))

            print("Matrix 2")
            temp1 = input("Size1: ")
            temp2 = input("Size2: ")
            chs = input("Argument: ")
            obj2 = MatrixShort(int(temp1), int(temp2), int(chs))
            continue
        elif chs == 2:
            print("Which Matrix?")
            chs = int(input("1/2: "))
            if chs == 1:
                obj1.fill_manually()
            elif chs == 2:
                obj2.fill_manually()
            continue
        elif chs == 3:
            print("Which Matrix?")
            chs = int(input("1/2: "))
            if chs == 1:
                obj1.print()
            elif chs == 2:
                obj2.print()
            continue
        elif chs == 4:
            print("Which Matrix?")
            chs = int(input("1/2: "))
            temp1 = int(input("Number: "))
            if chs == 1:
                obj1.fill_by_number(temp1)
            elif chs == 2:
                obj2.fill_by_number(temp1)
            continue
        elif chs == 5:
            print(None)
            continue
        elif chs == 6:
            print(None)
            continue
        elif chs == 7:
            print("Which Matrix?")
            chs = int(input("1/2: "))
            if chs == 1:
                print(obj1.size())
            elif chs == 2:
                print(obj2.size())
            continue
        elif chs == 8:
            print("Which Matrix?")
            chs = int(input("1/2: "))
            temp1 = int(input("index1: "))
            temp2 = int(input("index2: "))
            if chs == 1:
                print(obj1[temp1][temp2])
            elif chs == 2:
                print(obj2[temp1][temp2])
            continue
        elif chs == 9:
            while True:
                try:
                    print("\n\n1. Matrix++ \n2. Matrix-- \n3. Matrix = True/False \n4. !Matrix \n5. ~Matrix"
                          "\n6. Matrix + Matrix \n7. Matrix + scalar \n8. Matrix - Matrix \n9. Matrix - scalar"
                          "\n10. Matrix * Matrix \n11. Matrix * scalar \n12. Matrix / Matrix \n13. Matrix / scalar"
                          "\n14. Matrix % Matrix \n15. Matrix % scalar \n16. Matrix == Matrix \n17. Matrix != Matrix"
                          "\n18. Matrix > Matrix \n19. Matrix < Matrix \n20. Matrix >= Matrix \n21. Matrix <= Matrix"
                          "\n22. Matrix | Matrix \n23. Matrix | scalar \n24. Matrix & Matrix \n25. Matrix & scalar"
                          "\n26. Matrix ^ Matrix \n27. Matrix ^ scalar \n28. Matrix >> scalar \n29. Matrix << scalar")
                    chs = int(input())
                    if chs == 1:
                        print("Which Matrix?")
                        chs = int(input("1/2: "))
                        if chs == 1:
                            print(+obj1)
                        elif chs == 2:
                            print(+obj2)
                        continue
                    elif chs == 2:
                        print("Which Matrix?")
                        chs = int(input("1/2: "))
                        if chs == 1:
                            print(-obj1)
                        elif chs == 2:
                            print(-obj2)
                        continue
                    elif chs == 3:
                        print(None)
                        continue
                    elif chs == 4:
                        print(None)
                        continue
                    elif chs == 5:
                        print("Which Matrix?")
                        chs = int(input("1/2: "))
                        if chs == 1:
                            print(~obj1)
                        elif chs == 2:
                            print(~obj2)
                        continue
                    elif chs == 6:
                        print(obj1 + obj2)
                        continue
                    elif chs == 7:
                        temp1 = int(input("Scalar: "))
                        print(obj1 + temp1)
                        continue
                    elif chs == 8:
                        print(obj1 - obj2)
                        continue
                    elif chs == 9:
                        temp1 = int(input("Scalar: "))
                        print(obj1 - temp1)
                        continue
                    elif chs == 10:
                        print(obj1 * obj2)
                        continue
                    elif chs == 11:
                        temp1 = int(input("Scalar: "))
                        print(obj1 * temp1)
                        continue
                    elif chs == 12:
                        print(obj1 / obj2)
                        continue
                    elif chs == 13:
                        temp1 = int(input("Scalar: "))
                        print(obj1 / temp1)
                        continue
                    elif chs == 14:
                        print(obj1 % obj2)
                        continue
                    elif chs == 15:
                        temp1 = int(input("Scalar: "))
                        print(obj1 % temp1)
                        continue
                    elif chs == 16:
                        if obj1 == obj2:
                            print(True)
                        else:
                            print(False)
                        continue
                    elif chs == 17:
                        if obj1 != obj2:
                            print(True)
                        else:
                            print(False)
                        continue
                    elif chs == 18:
                        if obj1 > obj2:
                            print(True)
                        else:
                            print(False)
                        continue
                    elif chs == 19:
                        if obj1 < obj2:
                            print(True)
                        else:
                            print(False)
                        continue
                    elif chs == 20:
                        if obj1 >= obj2:
                            print(True)
                        else:
                            print(False)
                        continue
                    elif chs == 21:
                        if obj1 <= obj2:
                            print(True)
                        else:
                            print(False)
                        continue
                    elif chs == 22:
                        print(obj1 | obj2)
                        continue
                    elif chs == 23:
                        temp1 = int(input("Scalar: "))
                        print(obj1 | temp1)
                        continue
                    elif chs == 24:
                        print(obj1 & obj2)
                        continue
                    elif chs == 25:
                        temp1 = int(input("Scalar: "))
                        print(obj1 & temp1)
                        continue
                    elif chs == 26:
                        print(obj1 ^ obj2)
                        continue
                    elif chs == 27:
                        temp1 = int(input("Scalar: "))
                        print(obj1 ^ temp1)
                        continue
                    elif chs == 28:
                        print("Which vector?")
                        chs = int(input("1/2: "))
                        temp1 = int(input("Scalar: "))
                        if chs == 1:
                            print(obj1 >> temp1)
                        elif chs == 2:
                            print(obj2 >> temp1)
                        continue
                    elif chs == 29:
                        print("Which vector?")
                        chs = int(input("1/2: "))
                        temp1 = int(input("Scalar: "))
                        if chs == 1:
                            print(obj1 << temp1)
                        elif chs == 2:
                            print(obj2 << temp1)
                        continue
                    else:
                        print("Wrong choise")
                        if int(input("1 to exit")) == 1:
                            break
                except Exception as e:
                    print(e)
                    continue
        else:
            print("Wrong choise")
            if int(input("1 to exit")) == 1:
                break
    except Exception as e:
        print(e)
        continue
