# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# num = int(input("Введите трехзначное число: "))
# if num/100 < 1 or num/100 >= 10 : print("Это не трехзначное число!")
# else:
#     sum = num//100 + num%100//10 + num%10
#     print(f"Сумма чисел введенного числа равна {sum}")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# origamies = int(input("Сколько журавликов всего собрали ребята? "))
# if origamies%6 != 0: print("С таким кол-вом задача не решается!")
# else:
#     petros = int(origamies/6)
#     sergios = petros
#     kates = 2*(petros + sergios)
#     print(f"Из {origamies} журавликов Петя собрал {petros}, Катя - {kates}, Сережа - {sergios}")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
# счастливость билета.
# 385916 -> yes
# 123456 -> no

# inputNum = input("Введите шестизначный номер билета: ")
# if inputNum.isdigit() and len(inputNum) == 6:
#     i = 0
#     left = 0
#     right = 0
#     while i < len(inputNum)/2:
#         left += int(inputNum[i])
#         right += int(inputNum[len(inputNum) - i -1])
#         i+=1
#     if left == right : print("Билет счастливый!")
#     else: print("Билет обычный...")
# else: print("Неверный формат")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 
# 3 2 4 -> yes
# 3 2 1 -> no

# plateWidth = int(input("Введите кол-во n долек в плитке шоколадки: "))
# plateHeight = int(input("Введите кол-во m долек в плитке шоколадки: "))
# pieceSize = int(input("Введите кол-во k долек, которое хочется отломить: "))
# plate = [["[]"]*plateWidth]*plateHeight
# answer = False

# def PrintPlate():
#     i = 0
#     while i < len(plate):
#         j = 0
#         while j < len(plate[i]):
#             print(plate[i][j], end = "")
#             j += 1
#         i += 1
#         print("")

# if pieceSize < plateWidth*plateHeight:
#     if pieceSize%plateHeight == 0:
#         plate[0].insert(pieceSize//plateHeight, " ")
#         answer = True
#     if pieceSize%plateWidth == 0 and answer == False:
#         plate.insert(pieceSize//plateWidth, " ")
#         answer = True

# match answer:
#     case True: 
#         print(f"Да! Кусочек размером {pieceSize} можно отломить так:")
#         PrintPlate()
#     case False:
#         print(f"Нет! Кусочек размером {pieceSize} отломить не получится.")