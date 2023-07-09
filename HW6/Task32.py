'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] Диапазон: [5, 15]
Вывод: [1, 9, 13, 14, 19]
'''

inpArray = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
arrayRange = [5,15]

def IndexRangeArray(arr, arrRange):
    output = []
    for i in range(len(arr)):
        if arr[i] >= min(arrRange) and arr[i] <= max(arrRange):
            output.append(i)
    return output

print(IndexRangeArray(inpArray, arrayRange))