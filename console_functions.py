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
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    manager.create_note(title, content)


def read():
    filter_choice = input("Do you want to filter notes by date? (Y/N): ")
    if filter_choice.upper() == "Y":
        year = input("Enter year format YYYY : ")
        while not year.isdigit() or len(year) != 4:
            print('You enter wrong format data')
            year = input("Enter year format YYYY : ")
        month = input("Enter month format MM: ")
        while not month.isdigit() or len(month) != 2:
            print('You enter wrong format data')
            month = input("Enter month format MM: ")
        day = input("Enter day format DD: ")
        while not day.isdigit() or len(day) != 2:
            print('You enter wrong format data')
            day = input("Enter day format DD: ")
        filter_date = f"{year}-{month}-{day}"
        filter_date = datetime.datetime.strptime(filter_date, "%Y-%m-%d").date()
        manager.read_notes(filter_date=filter_date)
    else:
        manager.read_notes()


def find():
    note_id = int(input("Enter note ID: "))
    note = manager.get_note_by_id(note_id)
    if note:
        print("Note details:")
        print(note)
    else:
        print("Note not found.")


def delete():
    note_id = int(input("Enter note ID: "))
    manager.delete_note(note_id)


def edit():
    note_id = int(input("Enter note ID: "))
    new_title = input("Enter new note title: ")
    new_content = input("Enter new note content: ")
    manager.edit_note(note_id, new_title, new_content)
