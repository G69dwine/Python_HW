'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
# arrN = [7, 6, 1, 0, 2, 3]    # При использовании статических или случайных значений закомментить строки 9-12
# arrM = [7, 6, 5, 4, 3]

# from random import randint
# numN = 50
# arrN = [randint(1,50) for i in range(numN)]
# numM = 50
# arrM = [randint(1,50) for i in range(numM)]

numN = int(input("Кол-во элементов первого множества: "))
arrN = [int(input(f"{i}-й элемент: ")) for i in range(numN)]
numM = int(input("Кол-во элементов второго множества: "))
arrM = [int(input(f"{i}-й элемент: ")) for i in range(numM)]

hub = []

for i in arrN:
    if i in arrM:
        hub.append(i)
hub.sort()
print(set(hub))