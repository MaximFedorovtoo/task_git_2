<<<<<<< HEAD
<<<<<<< HEAD
from console import console


def main():
    console()


if __name__ == "__main__":
    main()
=======
=======
>>>>>>> parent of 63980a6 (done)
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
        match comand:
            case 'add': add_contact()
            case "find": search_contact()
            case "show": show_phonebook()
            case "edit": edit_contact()
            case "del": del_contact()
            case "stop": i = False
            case _:
                print('Нет такой команды!')
    

if __name__ == '__main__':
<<<<<<< HEAD
    main()
>>>>>>> parent of 63980a6 (done)
=======
    main()
>>>>>>> parent of 63980a6 (done)
