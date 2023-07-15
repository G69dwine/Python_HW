'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
'''
import csv

def main_menu():
    print("\nКоманды:\n"
          "1. Добавить абонента в справочник\n"
          "2. Удалить абонента\n"
          "3. Изменить данные абонента\n"
          "4. Сохранить изменения справичника\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу\n")
    choice = input("Введите номер команды или строку для поиска: ")
    return choice

def work_with_phonebook():
    
    show(phone_book)
    choice = main_menu()

    while (choice != '6'):
        match choice:
            case '':
                show(phone_book)
            case '1':
                user_data = get_new_user()
                add_user(phone_book, user_data)
                show(phone_book)
            case '2':
                delete_user(phone_book, input("Укажите ID записи (через #): "))
                show(phone_book)
            case '3':
                edit_user(phone_book, input("Укажите ID записи (через #): "))
                show(phone_book)
            case '4':
                write_csv(dir ,phone_book)
                print("Справочник успешно сохранен!")
                show(phone_book)
            case '5':
                write_txt('phon.txt', phone_book)
                print(f"Файл phon.txt успешно сохранен!")
                show(phone_book)
            case _:
                show(find_user(phone_book, choice))
        choice = main_menu()

def read_csv(filename: str) -> list:
    data = []
    with open(filename, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            data.append(row)
    return data

def show(data):
    data.sort(key= lambda x:x["ID"])
    for vol in fields:
        print(vol.ljust(15), end="")
    print("\n")
    for row in data:
        for val in row:
            print(f"{str(row[val]).ljust(15)}", end="")
        print()

def write_csv(filename: str, data: list):
    with open(filename, 'w',newline="", encoding='utf-8') as fout:
        writer = csv.DictWriter(fout, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

def get_ID(book):
    id = lambda x: int(x["ID"][1:])
    for i in range(1, len(book)):
        if id(book[i]) - id(book[i-1]) > 1:
            return f"#{id(book[i-1])+1}"
    return f"#{id(book[i])+1}"

def get_new_user():
    user = {"ID":get_ID(phone_book)}
    for i in fields[1:]:
        user[i] = input(f"{i}:")
    return user

def add_user(book: list, user: dict):
    book.append(user)

def find_user(book, val):
    if val!='':
        data = []
        for row in book:
            for key in row:
                if row[key] == val:
                    data.append(row)
        return data

def delete_user(data: list, id):
    for row in data:
        if row["ID"] == id: data.remove(row)

def edit_user(data: list, id):
    for row in data:
        if row["ID"] == id:
            print("Введите новые значения для полей или оставьте их пустыми для пропуска")
            for key in fields[1:]:
                inp = input(f"{key}: ")
                if inp!= '':
                    row[key] = inp

def write_txt(filename: str, data: list):
    with open(filename, 'w') as file:
        for row in range(len(data)):
            s = ''
            for v in data[row].values():
                s += v + ','
            file.write(f"{s[:-1]}\n")


dir = 'HW8/phonebook.csv'
phone_book = read_csv(dir)
fields = ["ID","Фамилия", "Имя", "Телефон", "Описание"]

work_with_phonebook()