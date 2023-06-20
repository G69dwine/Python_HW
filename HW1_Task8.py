# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 
# 3 2 4 -> yes
# 3 2 1 -> no

plateWidth = int(input("Введите кол-во n долек в плитке шоколадки: "))
plateHeight = int(input("Введите кол-во m долек в плитке шоколадки: "))
pieceSize = int(input("Введите кол-во k долек, которое хочется отломить: "))
plate = [["[]"]*plateWidth]*plateHeight
answer = False

def PrintPlate():
    i = 0
    while i < len(plate):
        j = 0
        while j < len(plate[i]):
            print(plate[i][j], end = "")
            j += 1
        i += 1
        print("")

if pieceSize < plateWidth*plateHeight:
    if pieceSize%plateHeight == 0:
        plate[0].insert(pieceSize//plateHeight, " ")
        answer = True
    if pieceSize%plateWidth == 0 and answer == False:
        plate.insert(pieceSize//plateWidth, " ")
        answer = True

match answer:
    case True: 
        print(f"Да! Кусочек размером {pieceSize} можно отломить так:")
        PrintPlate()
    case False:
        print(f"Нет! Кусочек размером {pieceSize} отломить не получится.")