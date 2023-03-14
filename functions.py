TEXTFILE = "phonebook.txt"
# созание контакта
def contact():
    array = list()
    for i in range(4):
        if i == 0:
           array.append(input('Введите фамилию: '))
        elif i == 1:
           array.append(input('Введите имя: '))
        elif i == 2:
           array.append(input('Введите отчество: '))
        elif i == 3:
           array.append(input('Введите номер телефона: '))
    cont = f'{array[0]} {array[1]} {array[2]} | {int(array[3])}'
    return cont

# добавление контакта в справочник
def add_contact():
    with open(TEXTFILE, 'a', encoding='utf-8') as file:
        file.writelines(f'{contact()}\n')
        
    
# поиск контакта по справочнику
def search_contact():
    with open(TEXTFILE, 'r', encoding='utf-8') as file:
        find = input('Введите поиск контакта: ')
        book = file.read().split('\n')
        index = 1
        temp = list()
        for i in book:
            if find.lower() in i.lower():
                print(f'{index}. {i}')
                temp.append(i)
            index +=1
        if bool(temp) == False:
            print('Нет такого контакта!')

# показывает спрвочник
def show_phonebook():
    with open(TEXTFILE, 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        index = 1
        for i in book:
           print(f'{index}. {i}')
           index +=1

   
# удаляет контакт из спавочника
def del_contact():
    with open(TEXTFILE, 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        find = input('Введите данные контакта который хотите удалить: ')
        index = 0
        temp = list()
        for i in book:
            if find.lower() in i.lower():
                print(f'Ведитете "{index}" чтобы удалить контакт "{i}"')
            index +=1
        if bool(temp):
            del_index = int(input(""))
            book.pop(del_index)    
            with open(TEXTFILE, 'w', encoding='utf-8') as file:
                for i in book:
                    file.writelines(f'{str(i)}\n')
        else:
            print('Нет такого контакта!')

# редактирует контакт в справочнике
def edit_contact():
    with open(TEXTFILE, 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        find = input('Введите данные контакта который хотите изменить: ')
        index = 0
        temp = list()
        for i in book:
            if find.lower() in i.lower():
                print(f'Ведитете "{index}" чтобы удалить контакт "{i}"')
                temp.append(i)
            index +=1
        if bool(temp):
            remake_index = int(input(""))
            book[remake_index] = contact()    
            with open(TEXTFILE, 'w', encoding='utf-8') as file:
                for i in book:
                    file.writelines(f'{str(i)}\n')
        else:
            print('Нет такого контакта!')