# services/birthday_service.py
import uuid
import sqlite3

class BirthdayService:
    def __init__(self, db_service):
        """Initialize with a db_service instance."""
        self.db_service = db_service

    def add_birthday(self, chat_id: int, friend_name: str, birthday: str):
        """Adds a friend's birthday to the database."""
        cursor = self.db_service.get_cursor()

        try:
            cursor.execute(
                "INSERT INTO birthdays (id, chat_id, friend_name, birthday) VALUES (?, ?, ?, ?)",
                (str(uuid.uuid4()), chat_id, friend_name, birthday)
            )
            self.db_service.conn.commit()

            if cursor.rowcount > 0:
                print(f"Birthday for {friend_name} successfully added!")
            else:
                print("Insertion failed, no rows affected.")
        except sqlite3.Error as e:
            print(f"Error occurred while adding birthday: {e}")
            self.db_service.conn.rollback()

    def get_birthdays(self, chat_id: int):
        """Retrieves all birthdays for a given chat_id."""
        cursor = self.db_service.get_cursor()
        results = cursor.execute(
            "SELECT friend_name, birthday FROM birthdays WHERE chat_id = ?",
            (chat_id,)
        ).fetchall()
        print(results)
        return [(row[0], row[1]) for row in results]
