'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом 
заданным во входном файле грядки.
'''

from random import randint
patchSize = int(input("Кол-во кустов на грядке: "))
patch = [randint(1,15) for i in range(patchSize)]

modRad = 1 #радиус охвата модуля - количество соседних кустов 
modPick = []

for i in range(len(patch)):
    modPick.append(sum((i<modRad)*patch[len(patch)-modRad+i:] + patch[(i>modRad)*(i-modRad):i+modRad+1]+ patch[:(i>=len(patch)-modRad)*(i-len(patch)+modRad+1)]))
    
print(f"Урожай грядки: {patch}")    
print(f"Варианты сбора модуля: {modPick}")
print(f"Модуль может собрать {max(modPick)} ягод, зайдя на {modPick.index(max(modPick))+1}-ю грядку")

'''
Варианты коллег
'''

# import random
# n = int(input('Введите колличество кустов: '))
# garden = [random.randint(1, 6) for i in range(n)]

# max_bushes  = garden[0] + garden[1] + garden[2]
# indicator = ["|"] * 3 + [" "] * (len(garden) - 3)
# for i in range (len(garden)):
#     following_bushes = garden[1] + garden[2] + garden[3]
#     if following_bushes > max_bushes:
#         max_bushes = following_bushes
#         indicator = ["|"] * 3 + [" "] * (len(garden) - 3)
#     else:
#         temp = indicator.pop(0)
#         indicator.append(temp)    
#     temp = garden.pop(0)
#     garden.append(temp)

# print(*indicator)
# print(*garden)
# print(f"Максимальное число ягод за один заход = {max_bushes}")