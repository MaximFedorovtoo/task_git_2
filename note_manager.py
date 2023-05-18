import datetime
import json
from note import Note


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

        except FileNotFoundError:
            print("File not found.")
