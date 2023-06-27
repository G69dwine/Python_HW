'''
Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''

numberS = int(input("Сумма загаданных чисел равна "))
numberP = int(input("Произведение загаданных чисел равна "))

def binFind(numS, numP):
    left = 1
    right = numS//2 + 1
    while left <= right:
        middle = (left + right)//2
        if numP/middle == numS - middle:
            return middle
        elif middle*(numS - middle) < numP:
            left = middle + 1
        else: right = middle - 1
    else: return None

x = binFind(numberS, numberP)

if x != None:
    y = numberS - x
    print(f"Петя загадал числа {x} и {y}")
else: print("Нет решений")
