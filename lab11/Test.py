import random

choise = 1  # выбор всегда 1 дверь
choiseParadox = 1  # выбор меняет

count1 = 0  # количество выиграшей без смены двери
countParadox = 0  # количество выиграшей со сменой

for i in range(1000000):

    prize = random.randint(1, 3)  # ставит приз за рандомной дверью

    master = 0
    if prize == 3:  # если приз за третьей дверью, ведущий не открывает её, а открывает вторую
        master = 2
        choiseParadox = 3  # игрок меняет дверь, с 1 на 3
    elif prize == 2:  # если приз за второй дверью, ведущий не открывает её, а открывает третью
        master = 3
        choiseParadox = 2  # игрок меняет дверь, с 1 на 3

    if choiseParadox == prize:  # если игрок, изменивший выбор угадал, это записывается
        countParadox += 1
    elif choise == prize:  # если игрок, который всегда выбирал 1 дверь угадал, это записывается
        count1 += 1

print(count1)
print(countParadox)
