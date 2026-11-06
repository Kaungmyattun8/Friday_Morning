import sqlite3

DB = "library.db"


class Book:
    def __init__(self, title, author, year, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def all(cls):
        conn = sqlite3.connect(DB)
        rows = conn.execute("SELECT * FROM books").fetchall()
        conn.close()
        return [cls(r[1], r[2], r[3], id=r[0]) for r in rows]

    @classmethod
    def load(cls, id):
        conn = sqlite3.connect(DB)
        row = conn.execute(
            "SELECT * FROM books WHERE id = ?", (id,)
        ).fetchone()
        conn.close()

        if row is None:
            return None

        return cls(row[1], row[2], row[3], id=row[0])

    def save(self):
        conn = sqlite3.connect(DB)
        cur = conn.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            (self.title, self.author, self.year),
        )
        conn.commit()
        self.id = cur.lastrowid
        conn.close()

    def update(self):
        conn = sqlite3.connect(DB)
        conn.execute(
            "UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?",
            (self.title, self.author, self.year, self.id),
        )
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect(DB)
        sql = "DELETE FROM books WHERE id = ?"
        conn.execute(sql, (self.id,))
        conn.commit()
        conn.close()

    def validate(self):
        errors = []
        if self.title.strip() == "":
            errors.append("Title is required.")
        if self.author.strip() == "":
            errors.append("Author is required.")
        if not str(self.year).isdigit():
            errors.append("Year must be a number.")
        else:
            self.year = int(self.year)
        return errors

    @classmethod
    def search(cls, text):
        conn = sqlite3.connect(DB)
        pattern = f"%{text}%"
        rows = conn.execute(
            "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
            (pattern, pattern),
        ).fetchall()
        conn.close()
        return [cls(r[1], r[2], r[3], id=r[0]) for r in rows]

    def to_dict(self):
        return {"id": self.id, "title": self.title,
                "author": self.author, "year": self.year}