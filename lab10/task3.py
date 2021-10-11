class Plane:

    def __init__(self):
        self.__chassis = True
        self.__throttle = 0
        self.__altitude = 0
        self.__bombs = 5
        self.__isAlive = True
        self.__passengers = 0
        self.__model = "da"

    def gas(self):
        if self.__throttle == 100:
            return
        self.__throttle += 10

    def brake(self):
        if self.__throttle == 0:
            return
        elif self.__altitude > 10 & self.__throttle == 50:
            return
        self.__throttle -= 10

    def up(self):
        if self.__throttle <= 70 & self.__altitude <= 10:
            return
        self.__altitude += 10

    def down(self):
        if self.__altitude == 0:
            return
        self.__altitude -= 10

    def chassis(self):
        if (self.__chassis is True) & (self.__altitude >= 10):
            self.__chassis = False
        elif self.__chassis is False:
            self.__chassis = True

    def bombs(self):
        if self.__bombs <= 0:
            return
        self.__bombs -= 1

    def member_add(self):
        if (self.__passengers >= 5) & (self.__altitude > 0):
            return
        self.__passengers += 1

    def member_remove(self):
        if (self.__passengers <= 1) & (self.__altitude > 0):
            return
        self.__passengers -=1

    def state(self):
        print("Throttle: ", self.__throttle, "/ Altitude: ", self.__altitude, "/ Chassis: ", self.__chassis, "/ Bombs: ", self.__bombs)
        print("Model: ", self.__model, "/ Is alive?: ", self.__isAlive, "/ Members: ", self.__passengers)


uii = Plane()
print("Control: gas, brake, chassis, up, down, bomb", "member+", "member-")
while True:
    chs = input()
    if chs == "gas":
        uii.gas()
    elif chs == "brake":
        uii.brake()
    elif chs == "chassis":
        uii.chassis()
    elif chs == "up":
        uii.up()
    elif chs == "down":
        uii.down()
    elif chs == "bomb":
        uii.bombs()
    elif chs == "member+":
        uii.member_add()
    elif chs == "member-":
        uii.member_remove()
    else:
        continue
    uii.state()

