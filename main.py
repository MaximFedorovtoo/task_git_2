import json
import datetime

class Note:
    def __init__(self, note_id, title, content):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"Note ID: {self.note_id}\nTitle: {self.title}\nContent: {self.content}\nCreated At: {self.created_at}\nUpdated At: {self.updated_at}"


class NoteManager:
    def __init__(self):
        self.notes = []
        self.file_name = "notes.json"  # Имя файла для сохранения заметок

    def generate_note_id(self):
        if not self.notes:
            return 1
        return self.notes[-1].note_id + 1

    def create_note(self, title, content):
        note_id = self.generate_note_id()
        note = Note(note_id, title, content)
        self.notes.append(note)
        self.save_notes()  # Автоматическое сохранение заметок после создания
        print("Note created successfully.")

    def read_notes(self, filter_date=None):
        if not self.notes:
            print("No notes found.")
            return

        sorted_notes = sorted(self.notes, key=lambda note: note.created_at)

        if filter_date:
            filtered_notes = [note for note in sorted_notes if note.created_at.date() == filter_date]
            if not filtered_notes:
                print("No notes found for the specified date.")
            else:
                for note in filtered_notes:
                    print(note)
                    print()
        else:
            for note in sorted_notes:
                print(note)
                print()

    def edit_note(self, note_id, new_title, new_content):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.content = new_content
                note.updated_at = datetime.datetime.now()
                self.save_notes()  # Автоматическое сохранение заметок после редактирования
                print("Note edited successfully.")
                return
        print("Note not found.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                self.save_notes()  # Автоматическое сохранение заметок после удаления
                print("Note deleted successfully.")
                return
        print("Note not found.")

    def save_notes(self):
        notes_data = []
        for note in self.notes:
            note_data = {
                "note_id": note.note_id,
                "title": note.title,
                "content": note.content,
                "created_at": str(note.created_at),
                "updated_at": str(note.updated_at)
            }
            notes_data.append(note_data)

        with open(self.file_name, "w") as file:
            json.dump(notes_data, file, indent=4)
        print("Notes saved successfully.")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None



    def load_notes(self):
        try:
            with open(self.file_name, "r") as file:
                notes_data = json.load(file)
            self.notes = []
            for note_data in notes_data:
                note_id = note_data["note_id"]
                title = note_data["title"]
                content = note_data["content"]
                created_at = datetime.datetime.fromisoformat(note_data["created_at"])
                updated_at = datetime.datetime.fromisoformat(note_data["updated_at"])
                note = Note(note_id, title, content)
                note.created_at = created_at
                note.updated_at = updated_at
                self.notes.append(note)
            print("Notes loaded successfully.")
        except FileNotFoundError:
            print("File not found.")


def print_menu():
    print("Note App")
    print("1. Create a note")
    print("2. Read notes")
    print("3. Find note by id")
    print("4. Edit a note")
    print("5. Delete a note")
    print("6. Load notes")
    print("0. Exit")


manager = NoteManager()

while True:
    print_menu()
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            manager.create_note(title, content)
        case "2":
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
        case "3":
            note_id = int(input("Enter note ID: "))
            note = manager.get_note_by_id(note_id)
            if note:
                print("Note details:")
                print(note)
            else:
                print("Note not found.")
        case "4":
            note_id = int(input("Enter note ID: "))
            new_title = input("Enter new note title: ")
            new_content = input("Enter new note content: ")
            manager.edit_note(note_id, new_title, new_content)
        case "5":
            note_id = int(input("Enter note ID: "))
            manager.delete_note(note_id)
        case "6":
            manager.load_notes()
        case "0":
            break
        case _:
            print("Invalid choice. Please try again.")
