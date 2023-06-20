# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

import random
coinSides = ["O","P"]
num = int(input("Сколько монет бросаем на стол? "))
coins = []
for i in range(num):
    coins.append(random.choice(coinSides))
    print(coins[i], end=" ")
if coins.count("O") >= coins.count("P"):
    print(coins.count("P"))
else: print(coins.count("O"))