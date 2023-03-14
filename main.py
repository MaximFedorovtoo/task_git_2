from functions import *



def main():
    print(f"'add' добавить контакт\n"
          "'show' посмотреть справочник\n"
          "'find' поиск контакта \n"
          "'del' удалить контакт\n"
          "'edit' редактировать\n"
          "'stop' завершение программы")
    
    i = True
    while i == True:
        comand = input('Введите команду ')
        if comand == 'add': add_contact()
        elif comand == 'find': search_contact()
        elif comand == 'show': show_phonebook()
        elif comand == 'edit': edit_contact()
        elif comand == 'del': del_contact()
        elif comand == 'stop': i = False
    

if __name__ == '__main__':
    main()