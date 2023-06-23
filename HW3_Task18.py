'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
Пример:
5
1 2 3 4 5
6
-> 5
'''

from random import randint

num = int(input("Кол-во элементов массива: "))
array = [randint(1,100) for i in range(num)]
print(array)
numX = int(input("Искомое число: "))

nearNum = array[0]
for i in range(1, len(array)):
    if abs(numX - array[i]) < abs(numX - nearNum):
        nearNum = array[i]

# nearNum = min(array, key=lambda x: abs(x-numX))
# print(f"{nearNum} - ближайшее к {numX}")