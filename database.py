import sqlite3


class Database:
    def __init__(self):
        self.connect = sqlite3.connect('jokebot.db')
        self.cursor = self.connect.cursor()
        # Looking for a table
        if len(self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name='joke'").fetchall()) == 0:
            self.cursor.execute("CREATE TABLE joke(id INT, page INT, newday BOOLEAN)")
            self.connect.commit()

    def add_user(self, user):
        self.connect = sqlite3.connect('jokebot.db')
        self.cursor = self.connect.cursor()
        # Create a user profile
        self.cursor.execute("INSERT INTO joke VALUES (?, ?, ?)", (user, 0, False))
        self.connect.commit()

    def all_reset(self):
        self.connect = sqlite3.connect('jokebot.db')
        self.cursor = self.connect.cursor()
        # Reset all
        self.cursor.execute("UPDATE joke SET page = 0 WHERE page != 0")
        self.cursor.execute("UPDATE joke SET newday = False WHERE newday != False")
        self.connect.commit()

    def user_reset(self, user):
        self.connect = sqlite3.connect('jokebot.db')
        self.cursor = self.connect.cursor()
        # Give page a value of 0
        self.cursor.execute("UPDATE joke SET page = ? WHERE id = ?", (0, user))
        self.connect.commit()

    def get_user_page(self, user):
        self.connect = sqlite3.connect('jokebot.db')
        self.cursor = self.connect.cursor()
        # Get user page from database and add page+1 in database
        page = self.cursor.execute(f"SELECT page from joke WHERE id = {user}").fetchone()[0]
        newday = self.cursor.execute(f"SELECT newday from joke WHERE id = {user}").fetchone()[0]
        self.cursor.execute("UPDATE joke SET page = ? WHERE id = ?", (page + 1, user))
        if not newday:
            self.cursor.execute("UPDATE joke SET newday = ? WHERE id = ?", (True, user))
        self.connect.commit()
        data = {
            'page': page,
            'newday': newday,
        }
        return data

    def search(self, user):
        self.connect = sqlite3.connect('jokebot.db')
        self.cursor = self.connect.cursor()
        # Looking for a user
        if self.cursor.execute(f"SELECT id from joke WHERE id = {user}").fetchone() is None:
            self.add_user(user)
