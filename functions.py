TEXTFILE = "phonebook.txt"
# созание контакта
def contact():
    array = list()
    for i in range(4):
        match i:
            case 0: array.append(input('Введите фамилию: '))
            case 1: array.append(input('Введите имя: '))
            case 2: array.append(input('Введите отчество: '))
            case 3: 
                array.append(input('Введите номер телефона: '))
                while not array[3].isdigit():
                        print('Вы вввели строку, введите пожалуйста номер телефона!')
                        array[3] = input('Введите номер телефона: ')
                else: break
    cont = f'{array[0]} {array[1]} {array[2]} | {int(array[3])}'
    return cont

# добавление контакта в справочник
def add_contact():
    with open(TEXTFILE, 'a', encoding='utf-8') as file:
        file.writelines(f'{contact()}\n')
        
    
# поиск контакта по справочнику
def search_contact():
    with open(TEXTFILE, 'r', encoding='utf-8') as file:
        find = str(input('Введите поиск контакта: '))
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
                temp.append(i)
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