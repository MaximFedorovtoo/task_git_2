import datetime
from note_manager import NoteManager

manager = NoteManager()


def print_menu():
    print("Note App")
    print("1. Create a note")
    print("2. Read notes")
    print("3. Find note by id")
    print("4. Edit a note")
    print("5. Delete a note")
    print("0. Exit")


def crate():
    title = input("\033[32mEnter note title: ")
    content = input("Enter note content: \033[0m")
    manager.create_note(title, content)


def read():
    try:
        filter_choice = input("Do you want to filter notes by date? (Y/N): ")
        if filter_choice.upper() == "Y":
            year = input("\033[32mEnter year format YYYY : \033[0m")
            while not year.isdigit() or len(year) != 4:
                print('\033[3;31mYou enter wrong format data\033[0m')
                year = input("\033[32mEnter year format YYYY : \033[0m")
            month = input("\033[32mEnter month format MM: \033[0m")
            while not month.isdigit() or len(month) != 2:
                print('\033[3;31mYou enter wrong format data\033[0m')
                month = input("\033[32mEnter month format MM: \033[0m")
            day = input("\033[32mEnter day format DD: \033[0m")
            while not day.isdigit() or len(day) != 2:
                print('\033[3;31mYou enter wrong format data\033[0m')
                day = input("\033[32mEnter day format DD: \033[0m")
            filter_date = f"{year}-{month}-{day}"
            filter_date = datetime.datetime.strptime(filter_date, "%Y-%m-%d").date()
            manager.read_notes(filter_date=filter_date)
        else:
            manager.read_notes()
    except ValueError:
        print("\033[3;31mYou have an error in the date\033[0m")


def find():
    try:
        note_id = int(input("Enter note ID: "))
        note = manager.get_note_by_id(note_id)
        if note:
            print("Note details:")
            print(note)
        else:
            print("Note not found.")
    except ValueError:
        print("\033[3;31mThe entered ID must be a number\033[0m")


def delete():
    try:
        note_id = int(input("Enter note ID: "))
        manager.delete_note(note_id)
    except ValueError:
        print("\033[3;31mThe entered ID must be a number\033[0m")


def edit():
    try:
        note_id = int(input("Enter note ID: "))
        new_title = input("Enter new note title: ")
        new_content = input("Enter new note content: ")
        manager.edit_note(note_id, new_title, new_content)
    except ValueError:
        print("\033[3;31mThe entered ID must be a number\033[0m")
