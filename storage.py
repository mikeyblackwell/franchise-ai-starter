"""
storage.py

Handles local persistence of stories using SQLite.
"""

import sqlite3

class LocalStorage:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute(
                "CREATE TABLE IF NOT EXISTS stories (title TEXT PRIMARY KEY, content TEXT)"
            )

    def save(self, title, content):
        with self.conn:
            self.conn.execute(
                "REPLACE INTO stories (title, content) VALUES (?, ?)",
                (title, content)
            )

    def load(self, title):
        cursor = self.conn.cursor()
        cursor.execute("SELECT content FROM stories WHERE title = ?", (title,))
        result = cursor.fetchone()
        return result[0] if result else "Story not found."

    def list_titles(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT title FROM stories")
        return [row[0] for row in cursor.fetchall()]
