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
