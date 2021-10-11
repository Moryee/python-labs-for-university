class Room:
    def __init__(self, x, y, z, windows):
        try:
            self.__lengthX = float(x)
            self.__lengthY = float(y)
            self.__lengthZ = float(z)
            self.__windowsQuantity = int(windows)
        except Exception as e:
            print(e)
            return

    def state(self):
        print("Length axis x: ", self.__lengthX)
        print("Length axis Y: ", self.__lengthY)
        print("Length axis Z: ", self.__lengthZ)
        print("Quantity of windows: ", self.__windowsQuantity)

    def area(self):
        print("Area: ", 2 * (self.__lengthX * self.__lengthY + self.__lengthX * self.__lengthZ + self.__lengthY * self.__lengthZ))

    def volume(self):
        print("Volume: ", self.__lengthX * self.__lengthY * self.__lengthZ)


while True:
    print("1. Edit room \n2. Exit")
    chs = int(input())
    if chs == 1:
        side1 = 0
        side2 = 0
        side3 = 0
        windows = 0
        try:
            print("Enter side a: ")
            side1 = input()
            print("Enter side b: ")
            side2 = input()
            print("Enter side c: ")
            side3 = input()
            print("Windows quantity: ")
            windows = input()
        except Exception as e:
            print(e)
            break
        obj = Room(side1, side2, side3, windows)
    elif chs == 2:
        break
    else:
        print("Wrong number of choise")
        continue

    while True:
        print("1. State \n2. Volume \n3. Area \n4. Exit")
        chs = int(input())
        if chs == 1:
            obj.state()
            continue
        elif chs == 2:
            obj.volume()
            continue
        elif chs == 3:
            obj.area()
            continue
        elif chs == 4:
            break
        else:
            print("Wrong number of choise")
            continue


