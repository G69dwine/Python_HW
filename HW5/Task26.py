'''
Задача 26: Напишите программу, которая на вход принимае тдва числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
a = 3
b = 5

def powerNums(num1, num2):
    if num2==1: return num1
    return num1*powerNums(num1, num2-1)

print(powerNums(a,b))