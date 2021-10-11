import math


class ATriangle:
    def __init__(self, a, b):
        try:
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(math.sqrt(pow(self.__a, 2) + pow(self.__b, 2)))
        except Exception as ex:
            print(ex)
            return

    def __init__(self):
        self.__a = 1
        self.__b = 1
        self.__c = float(math.sqrt(pow(self.__a, 2) + pow(self.__b, 2)))

    def a(self):
        return self.__a
    def a(self, a):
        self.__a = a
        self.__c = float(math.sqrt(pow(self.__a, 2) + pow(self.__b, 2)))

    def b(self):
        return self.__b
    def b(self, b):
        self.__b = b
        self.__c = float(math.sqrt(pow(self.__a, 2) + pow(self.__b, 2)))


    def length_of_sides(self):
        print("Length of side a: " + str(self.__a))
        print("Length of side b: " + str(self.__b))
        print("Length of side c: " + str(self.__c))

    def perimeter(self):
        print("Perimeter: ", self.__a + self.__b + self.__c)

    def area(self):
        print("Area: ", 1/2 * self.__a * self.__b)

    def is_exist(self, a, b):
        if (float(a) == self.__a) & (float(b) == self.__b):
            return True
        else:
            return False


while True:
    print("1. New sides \n2. Exit")
    chs = int(input())
    if chs == 1:
        side1 = 0
        side2 = 0
        try:
            print("Enter side a: ")
            side1 = input()
            print("Enter side b: ")
            side2 = input()
        except Exception as e:
            print(e)
            break
        obj = ATriangle(side1, side2)
    elif chs == 2:
        break
    else:
        print("Wrong number of choise")
        continue

    while True:
        print("1. Length of sides \n2. Perimetr \n3. Area \n4. Is Exist \n5. Exit")
        chs = int(input())
        if chs == 1:
            obj.length_of_sides()
            continue
        elif chs == 2:
            obj.perimeter()
            continue
        elif chs == 3:
            obj.area()
            continue
        elif chs == 4:
            print("Enter side a: ")
            temp1 = float(input())
            print("Enter side b: ")
            temp2 = float(input())
            if obj.is_exist(temp1, temp2):
                print("exist")
            else:
                print("does not exist")
            continue
        elif chs == 5:
            break
        else:
            print("Wrong number of choise")
            continue


