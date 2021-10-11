class VectorShort:
    __codeError = 0

    # 1. fields / 2. c-tors
    def __init__(self):
        self.__short_array = [0]

    def __init__(self, size):
        self.__short_array = [0] * size

    def __init__(self, size, t):
        self.__short_array = [t] * size

    # 4. methods
    def fill_manually(self):
        for i in range(len(self.__short_array)):
            self.__short_array[i] = input("- ")

    def print(self):
        print(self.__short_array)

    def fill_by_number(self, number):
        for i in range(len(self.__short_array)):
            self.__short_array[i] = number

    # 5. properties
    def size(self):
        return len(self.__short_array)

    def codeError(self):
        return self.__codeError

    def codeError(self, number):
        self.__codeError = number

    # 6. indexer
    def __getitem__(self, item):
        try:
            self.__codeError = 0
            return self.__short_array[item]
        except Exception as e:
            self.__codeError = 1
            return e

    def __setitem__(self, item, number):
        self.__codeError = number

    # 7. overloads
    def __pos__(self):
        temp = self.__short_array = [x+1 for x in self.__short_array]
        return temp

    def __neg__(self):
        temp = self.__short_array = [x-1 for x in self.__short_array]
        return temp

    def __bool__(self):
        if len(self.__short_array) != 0:
            for i in self.__short_array:
                if self.__short_array[i] != 0:
                    return True
            return False

    def __invert__(self):
        temp = self.__short_array = [~x for x in self.__short_array]
        return temp

    def __add__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x + other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] + other.__short_array[x])
            return temp

    def __sub__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x - other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] + other.__short_array[x])
            return temp

    def __mul__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x * other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] * other.__short_array[x])
            return temp

    def __truediv__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x / other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] / other.__short_array[x])
        return temp

    def __mod__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x % other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] % other.__short_array[x])
            return temp

    def __or__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x | other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] | other.__short_array[x])
            return temp

    def __and__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x & other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] & other.__short_array[x])
            return temp

    def __xor__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x ^ other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] ^ other.__short_array[x])
            return temp

    def __rshift__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x >> other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] >> other.__short_array[x])
            return temp

    def __lshift__(self, other):
        if isinstance(other, int):
            temp = self.__short_array = [x << other for x in self.__short_array]
            return temp
        else:
            temp = []
            for x in range(len(self.__short_array)):
                temp.append(self.__short_array[x] << other.__short_array[x])
            return temp

    def __eq__(self, other):
        if len(self.__short_array) != len(other.__short_array):
            return False
        for i in range(len(self.__short_array)):
            if self.__short_array[i] != other.__short_array[i]:
                return False
        return True

    def __ne__(self, other):
        if len(self.__short_array) != len(other.__short_array):
            return False
        for i in range(len(self.__short_array)):
            if self.__short_array[i] != other.__short_array[i]:
                return True
        return False

    def __gt__(self, other):
        if len(self.__short_array) != len(other.__short_array):
            return False
        for i in range(len(self.__short_array)):
            if self.__short_array[i] <= other.__short_array[i]:
                return False
        return True

    def __lt__(self, other):
        if len(self.__short_array) != len(other.__short_array):
            return False
        for i in range(len(self.__short_array)):
            if self.__short_array[i] >= other.__short_array[i]:
                return False
        return True

    def __ge__(self, other):
        if len(self.__short_array) != len(other.__short_array):
            return False
        for i in range(len(self.__short_array)):
            if self.__short_array[i] < other.__short_array[i]:
                return False
        return True

    def __le__(self, other):
        if len(self.__short_array) != len(other.__short_array):
            return False
        for i in range(len(self.__short_array)):
            if self.__short_array[i] > other.__short_array[i]:
                return False
        return True

    # 3. destructor
    def __del__(self):
        print("Destructor has been called")


obj1 = VectorShort
obj2 = VectorShort
while True:
    try:
        print("Vector 1")
        temp1 = int(input("Size: "))
        temp2 = int(input("Argument: "))
        obj1 = VectorShort(temp1, temp2)

        print("Vector 2")
        temp1 = int(input("Size: "))
        temp2 = int(input("Argument: "))
        obj2 = VectorShort(temp1, temp2)
        break
    except Exception as e:
        print(e)
        continue
while True:
    try:
        print("\n\n1. New vectors \n2. Type elements of vector manually \n3. Show vector \n4. Fill by number "
              "\n5. Quantity of vectors \n6. ??? \n7. Size of vector \n8. Indexer \n9. Overload")
        chs = int(input())
        if chs == 1:
            print("Vector 1")
            temp1 = int(input("Size: "))
            temp2 = int(input("Argument: "))
            obj1 = VectorShort(temp1, temp2)

            print("Vector 2")
            temp1 = int(input("Size: "))
            temp2 = int(input("Argument: "))
            obj2 = VectorShort(temp1, temp2)
            continue
        elif chs == 2:
            print("Which vector?")
            chs = int(input("1/2: "))
            if chs == 1:
                obj1.fill_manually()
            elif chs == 2:
                obj2.fill_manually()
            continue
        elif chs == 3:
            print("Which vector?")
            chs = int(input("1/2: "))
            if chs == 1:
                obj1.print()
            elif chs == 2:
                obj2.print()
            continue
        elif chs == 4:
            print("Which vector?")
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
            print("Which vector?")
            chs = int(input("1/2: "))
            if chs == 1:
                print(obj1.size())
            elif chs == 2:
                print(obj2.size())
            continue
        elif chs == 8:
            print("Which vector?")
            chs = int(input("1/2: "))
            temp1 = int(input("index: "))
            if chs == 1:
                print(obj1[temp1])
            elif chs == 2:
                print(obj2[temp1])
            continue
        elif chs == 9:
            while True:
                try:
                    print("\n\n1. vector++ \n2. vector-- \n3. vector = True/False \n4. !vector \n5. ~vector"
                          "\n6. vector + vector \n7. vector + scalar \n8. vector - vector \n9. vector - scalar"
                          "\n10. vector * vector \n11. vector * scalar \n12. vector / vector \n13. vector / scalar"
                          "\n14. vector % vector \n15. vector % scalar \n16. vector == vector \n17. vector != vector"
                          "\n18. vector > vector \n19. vector < vector \n20. vector >= vector \n21. vector <= vector"
                          "\n22. vector | vector \n23. vector | scalar \n24. vector & vector \n25. vector & scalar"
                          "\n26. vector ^ vector \n27. vector ^ scalar \n28. vector >> scalar \n29. vector << scalar")
                    chs = int(input())
                    if chs == 1:
                        print("Which vector?")
                        chs = int(input("1/2: "))
                        if chs == 1:
                            print(+obj1)
                        elif chs == 2:
                            print(+obj2)
                        continue
                    elif chs == 2:
                        print("Which vector?")
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
                        print("Which vector?")
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
