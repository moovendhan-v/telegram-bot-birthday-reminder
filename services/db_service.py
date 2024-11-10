import sqlite3
from config import DATABASE_DEFAULT_PATH
from database_schema import TENANTS_TABLE, BIRTHDAYS_TABLE 

class DatabaseService:
    def __init__(self, db_path=DATABASE_DEFAULT_PATH):
        """Initialize the database connection."""
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        """Create the tenants and birthdays tables if they do not exist."""
        with self.conn:
            # Execute the table creation queries from the schema
            self.conn.execute(TENANTS_TABLE)
            self.conn.execute(BIRTHDAYS_TABLE)

    def get_cursor(self):
        """Returns a cursor for executing queries."""
        return self.conn.cursor()

    def commit(self):
        """Commits changes to the database."""
        self.conn.commit()

    def close(self):
        """Closes the database connection."""
        self.conn.close()
