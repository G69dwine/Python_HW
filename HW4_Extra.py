'''
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов 
"Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" 
(необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, 
нумерация начинается с единицы

Формат входных данных:
В первой строке подаётся число n
n – количество холодильников. В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
5 до 100 символов.

Формат выходных данных:
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n

Sample Output 1:
1 2 3

Sample Input 2:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton

Sample Output 2:
1 2 7 8
'''
# refregerators = ["222anton456", "a1n1t1o1n1", "0000a0000n00t00000o000000n", "gylfole", "richard", "ant0n"]
# refregerators = ["osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen", "anton", "aoooooooooontooooo", "elelelelelelelelelel",
# "ntoneeee", "tonee","253235235a5323352n25235352t253523523235oo235523523523n", "antoooooooooooooooooooooooooooooooooooooooooooooooooooon", "unton"]

num = int(input("количество холодильников: "))                                      #При установке статических значений закомментить строки 48,49
refregerators = [input(f"Номер {i+1}-го холодильника: ") for i in range(num)]

def virusScan(num):
    virus = "anton"
    out = ''
    for i in num:
        if i in virus and out + i == virus[:len(out)+1]:
            out += i
    if out == virus: return True
    else: return False

for ref in refregerators:
    if virusScan(ref):
        print(refregerators.index(ref)+1, end=" ")