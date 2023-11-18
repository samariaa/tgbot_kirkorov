import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def chat_exists(self, chat_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'chats' WHERE 'chat_id' = ?", (chat_id,)).fetchmany(1)
            return bool(len(result))

    def add_chat(self, chat_id, type):
        with self.connection:
            return self.cursor.execute("INSERT OR IGNORE INTO 'chats' ('chat_id', 'type') VALUES (?, ?)",
                                       (chat_id, type,))

    def set_active(self, chat_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE chats SET active = ? WHERE chat_id = ?", (active, chat_id,))

    def get_chats(self):
        with self.connection:
            return self.cursor.execute("SELECT chat_id, active FROM chats").fetchall()

#USERS!!!!!!!!!!

    def user_exists(self, chat_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'chat_id' = ?", (chat_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, chat_id, type, firstname, lastname, username):
        with self.connection:
            return self.cursor.execute("INSERT OR IGNORE INTO 'users' ('chat_id', 'type', 'firstname', 'lastname', 'username') VALUES (?, ?, ?, ?, ?)",
                                       (chat_id, type, firstname, lastname, username,))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users").fetchall()
